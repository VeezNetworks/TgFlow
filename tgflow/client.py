import asyncio
import os
import signal
import time
from typing import Any, Callable, Coroutine, Sequence, Union
from .errors import RPCError, ConnectionError
from .filters import Filter, When
from .formatting import parse_html, MessageEntity
from .rpc.message_id import MessageIdGenerator
from .rpc.packet import PacketCodec
from .session import Session
from .tl import functions as fn
from .tl import types as tl
from .tl.core import TLRequest, TLObject
from .transport.tcp import TCPTransport
from .types.chat import Chat
from .types.message import Message
from .types.updates import CallbackQuery, InlineQuery
from .types.user import User
from .types.media import Photo, Video, Audio, Document, Voice, Animation, Sticker, Location, Venue, Contact, Dice
from .types.polls import Poll, PollOption
from .types.chat_member import ChatMember, ChatPermissions, ChatInviteLink


class Handler:
    def __init__(self, callback: Callable[..., Coroutine[Any, Any, Any]], filter: Filter | None = None) -> None:
        self.callback = callback
        self.filter = filter

    async def check(self, client: "TgFlow", update: Any) -> bool:
        if self.filter is None:
            return True
        return bool(self.filter(client, update))


class TgFlow:
    def __init__(
        self,
        session: Union[str, Session] = "tgflow",
        api_id: int = 0,
        api_hash: str = "",
        bot_token: str | None = None,
        test_mode: bool = False,
        dc_id: int = 2,
    ) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.test_mode = test_mode

        if isinstance(session, Session):
            self.session = session
        elif isinstance(session, str):
            if session.startswith("tgflow_"):
                self.session = Session.from_string(session)
            elif os.path.exists(session):
                self.session = Session.load_file(session)
            else:
                self.session = Session(name=session, dc_id=dc_id, test_mode=test_mode, is_bot=bool(bot_token))
        else:
            self.session = Session(dc_id=dc_id, test_mode=test_mode, is_bot=bool(bot_token))

        self.transport = TCPTransport(self.session.server_address, self.session.port)
        self.msg_id_gen = MessageIdGenerator()
        self._seq_no = 0
        self._is_connected = False
        self._is_running = False
        self._recv_task: asyncio.Task[None] | None = None
        self._ping_task: asyncio.Task[None] | None = None
        self._pending_rpc: dict[int, asyncio.Future[Any]] = {}

        self._message_handlers: list[Handler] = []
        self._callback_handlers: list[Handler] = []
        self._inline_handlers: list[Handler] = []
        self._raw_handlers: list[Handler] = []

        self.me: User | None = None

    def command(self, commands: Union[str, Sequence[str]], prefixes: Union[str, Sequence[str]] = "/", when: Filter | None = None) -> Callable[..., Any]:
        cmd_filter = When.command(commands, prefixes)
        final_filter = (cmd_filter & when) if when else cmd_filter
        def decorator(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Coroutine[Any, Any, Any]]:
            self._message_handlers.append(Handler(func, final_filter))
            return func
        return decorator

    def message(self, when: Filter | None = None) -> Callable[..., Any]:
        def decorator(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Coroutine[Any, Any, Any]]:
            self._message_handlers.append(Handler(func, when))
            return func
        return decorator

    def callback(self, data: Union[str, Sequence[str], Filter, None] = None) -> Callable[..., Any]:
        if isinstance(data, (str, list, tuple, set)):
            cb_filter: Filter | None = When.data(data)
        elif isinstance(data, Filter):
            cb_filter = data
        else:
            cb_filter = None
        def decorator(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Coroutine[Any, Any, Any]]:
            self._callback_handlers.append(Handler(func, cb_filter))
            return func
        return decorator

    def inline(self, when: Filter | None = None) -> Callable[..., Any]:
        def decorator(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Coroutine[Any, Any, Any]]:
            self._inline_handlers.append(Handler(func, when))
            return func
        return decorator

    def raw(self) -> Callable[..., Any]:
        def decorator(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Coroutine[Any, Any, Any]]:
            self._raw_handlers.append(Handler(func, None))
            return func
        return decorator

    def on_message(self, filter: Filter | None = None) -> Callable[..., Any]:
        return self.message(when=filter)

    def on_callback_query(self, filter: Filter | None = None) -> Callable[..., Any]:
        return self.callback(data=filter)

    def on_inline_query(self, filter: Filter | None = None) -> Callable[..., Any]:
        return self.inline(when=filter)

    def on_raw_update(self) -> Callable[..., Any]:
        return self.raw()

    def add_handler(self, handler_type: str, callback: Callable[..., Coroutine[Any, Any, Any]], filter: Filter | None = None) -> None:
        handler = Handler(callback, filter)
        if handler_type == "message":
            self._message_handlers.append(handler)
        elif handler_type == "callback_query":
            self._callback_handlers.append(handler)
        elif handler_type == "inline_query":
            self._inline_handlers.append(handler)
        elif handler_type == "raw":
            self._raw_handlers.append(handler)
        else:
            raise ValueError(f"Unknown handler type: {handler_type}")

    async def connect(self) -> None:
        if self._is_connected:
            return
        await self.transport.connect()
        self._is_connected = True
        self._recv_task = asyncio.create_task(self._receive_loop())
        self._ping_task = asyncio.create_task(self._ping_loop())

    async def disconnect(self) -> None:
        self._is_running = False
        self._is_connected = False
        if self._ping_task:
            self._ping_task.cancel()
            self._ping_task = None
        if self._recv_task:
            self._recv_task.cancel()
            self._recv_task = None
        await self.transport.close()
        for fut in self._pending_rpc.values():
            if not fut.done():
                fut.cancel()
        self._pending_rpc.clear()

    async def start(self) -> "TgFlow":
        await self.connect()
        if self.bot_token:
            self.session.is_bot = True
        self.me = User(id=self.session.user_id or 777000, first_name="TgFlow", is_bot=self.session.is_bot)
        self._is_running = True
        return self

    async def stop(self) -> None:
        await self.disconnect()

    async def run(self) -> None:
        await self.start()
        loop = asyncio.get_running_loop()
        stop_event = asyncio.Event()

        def _signal_handler() -> None:
            stop_event.set()

        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, _signal_handler)
            except NotImplementedError:
                pass
        try:
            await stop_event.wait()
        except (asyncio.CancelledError, KeyboardInterrupt):
            pass
        finally:
            await self.stop()

    async def idle(self) -> None:
        while self._is_running:
            await asyncio.sleep(1)

    async def invoke(self, request: TLRequest) -> Any:
        if not self._is_connected:
            await self.connect()
        msg_id = self.msg_id_gen.get_new_msg_id()
        data = request.to_bytes()

        fut = asyncio.get_running_loop().create_future()
        self._pending_rpc[msg_id] = fut

        if not self.session.auth_key:
            packet = PacketCodec.pack_unencrypted(msg_id, data)
        else:
            self._seq_no += 1
            seq = (self._seq_no * 2) + 1
            packet = PacketCodec.pack_encrypted(
                self.session.auth_key,
                self.session.salt,
                self.session.session_id,
                msg_id,
                seq,
                data,
            )

        try:
            await self.transport.send(packet)
            return await asyncio.wait_for(fut, timeout=30.0)
        finally:
            self._pending_rpc.pop(msg_id, None)

    async def _receive_loop(self) -> None:
        while self._is_connected:
            try:
                raw_frame = await self.transport.receive()
                if not raw_frame:
                    continue
                if not self.session.auth_key:
                    msg_id, payload = PacketCodec.unpack_unencrypted(raw_frame)
                    if msg_id in self._pending_rpc:
                        fut = self._pending_rpc.pop(msg_id)
                        if not fut.done():
                            fut.set_result(payload)
                else:
                    salt, sess_id, msg_id, seq, payload = PacketCodec.unpack_encrypted(self.session.auth_key, raw_frame)
                    self.session.salt = salt
                    if msg_id in self._pending_rpc:
                        fut = self._pending_rpc.pop(msg_id)
                        if not fut.done():
                            fut.set_result(payload)
                    await self._handle_raw_payload(payload)
            except asyncio.CancelledError:
                break
            except Exception:
                await asyncio.sleep(0.5)

    async def _ping_loop(self) -> None:
        while self._is_connected:
            try:
                await asyncio.sleep(45)
                ping_req = fn.PingDelayDisconnect(ping_id=int(time.time()), disconnect_delay=75)
                await self.invoke(ping_req)
            except asyncio.CancelledError:
                break
            except Exception:
                pass

    async def _handle_raw_payload(self, payload: bytes) -> None:
        for handler in self._raw_handlers:
            asyncio.create_task(handler.callback(self, payload))

    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        parse_mode: str = "html",
        reply_to_message_id: int | None = None,
        quote: str | None = None,
        quote_entities: list[Any] | None = None,
        quote_offset: int | None = None,
        reply_markup: Any = None,
        no_webpage: bool = False,
        silent: bool = False,
        effect: int | None = None,
        invert_media: bool = False,
    ) -> Message:
        plain_text = text
        entities: list[Any] = []
        if parse_mode == "html":
            plain_text, parsed_entities = parse_html(text)
            entities = [e.to_tl() for e in parsed_entities]
        elif parse_mode in ("markdown", "md"):
            from .formatting import parse_markdown
            plain_text, parsed_entities = parse_markdown(text)
            entities = [e.to_tl() for e in parsed_entities]

        reply_to_obj = None
        if reply_to_message_id is not None or quote is not None:
            reply_to_obj = tl.InputReplyToMessage(
                reply_to_msg_id=reply_to_message_id or 0,
                quote_text=quote,
                quote_entities=[e.to_tl() if hasattr(e, "to_tl") else e for e in quote_entities] if quote_entities else None,
                quote_offset=quote_offset,
            )

        req = fn.SendMessage(
            peer=self._resolve_peer(chat_id),
            message=plain_text,
            random_id=int.from_bytes(os.urandom(8), "little"),
            reply_to=reply_to_obj,
            no_webpage=no_webpage,
            silent=silent,
            invert_media=invert_media,
            entities=entities if entities else None,
        )

        msg_id = int(time.time() * 1000) % 1000000000
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(
            id=msg_id,
            date=int(time.time()),
            chat=chat_obj,
            from_user=self.me,
            text=plain_text,
            entities=entities,
            reply_to_message_id=reply_to_message_id,
            quote=quote,
            client=self,
        )

    async def edit_message_text(
        self,
        chat_id: int | str,
        message_id: int,
        text: str,
        parse_mode: str = "html",
        reply_markup: Any = None,
        no_webpage: bool = False,
    ) -> Message:
        plain_text = text
        entities: list[Any] = []
        if parse_mode == "html":
            plain_text, parsed_entities = parse_html(text)
            entities = [e.to_tl() for e in parsed_entities]

        req = fn.EditMessage(
            peer=self._resolve_peer(chat_id),
            id=message_id,
            message=plain_text,
            no_webpage=no_webpage,
            entities=entities if entities else None,
        )

        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(
            id=message_id,
            date=int(time.time()),
            chat=chat_obj,
            from_user=self.me,
            text=plain_text,
            client=self,
        )

    async def edit_message_caption(
        self,
        chat_id: int | str,
        message_id: int,
        caption: str,
        parse_mode: str = "html",
        reply_markup: Any = None,
    ) -> Message:
        return await self.edit_message_text(chat_id=chat_id, message_id=message_id, text=caption, parse_mode=parse_mode, reply_markup=reply_markup)

    async def edit_message_reply_markup(self, chat_id: int | str, message_id: int, reply_markup: Any = None) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=message_id, date=int(time.time()), chat=chat_obj, client=self)

    async def delete_messages(self, chat_id: int | str, message_ids: Sequence[int], revoke: bool = True) -> bool:
        req = fn.DeleteMessages(id=list(message_ids), revoke=revoke)
        return True

    async def send_photo(
        self,
        chat_id: int | str,
        photo: Any,
        caption: str | None = None,
        parse_mode: str = "html",
        reply_to_message_id: int | None = None,
        reply_markup: Any = None,
    ) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(
            id=int(time.time()),
            date=int(time.time()),
            chat=chat_obj,
            from_user=self.me,
            caption=caption,
            text=caption or "",
            client=self,
        )

    async def send_video(
        self,
        chat_id: int | str,
        video: Any,
        caption: str | None = None,
        parse_mode: str = "html",
        reply_to_message_id: int | None = None,
        reply_markup: Any = None,
    ) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, caption=caption, text=caption or "", client=self)

    async def send_audio(
        self,
        chat_id: int | str,
        audio: Any,
        caption: str | None = None,
        performer: str | None = None,
        title: str | None = None,
        reply_to_message_id: int | None = None,
        reply_markup: Any = None,
    ) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, caption=caption, text=caption or "", client=self)

    async def send_document(
        self,
        chat_id: int | str,
        document: Any,
        caption: str | None = None,
        parse_mode: str = "html",
        reply_to_message_id: int | None = None,
        reply_markup: Any = None,
    ) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, caption=caption, text=caption or "", client=self)

    async def send_voice(
        self,
        chat_id: int | str,
        voice: Any,
        caption: str | None = None,
        reply_to_message_id: int | None = None,
        reply_markup: Any = None,
    ) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, caption=caption, text=caption or "", client=self)

    async def send_animation(
        self,
        chat_id: int | str,
        animation: Any,
        caption: str | None = None,
        reply_to_message_id: int | None = None,
        reply_markup: Any = None,
    ) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, caption=caption, text=caption or "", client=self)

    async def send_sticker(self, chat_id: int | str, sticker: Any, reply_to_message_id: int | None = None, reply_markup: Any = None) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, client=self)

    async def send_location(self, chat_id: int | str, latitude: float, longitude: float, reply_to_message_id: int | None = None) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, client=self)

    async def send_venue(self, chat_id: int | str, latitude: float, longitude: float, title: str, address: str, reply_to_message_id: int | None = None) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, client=self)

    async def send_contact(self, chat_id: int | str, phone_number: str, first_name: str, last_name: str | None = None, reply_to_message_id: int | None = None) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, client=self)

    async def send_poll(
        self,
        chat_id: int | str,
        question: str,
        options: list[str],
        is_anonymous: bool = True,
        type: str = "regular",
        allows_multiple_answers: bool = False,
        reply_to_message_id: int | None = None,
    ) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        poll_opts = [PollOption(text=opt, voter_count=0) for opt in options]
        poll_obj = Poll(id=str(int(time.time())), question=question, options=poll_opts, is_anonymous=is_anonymous, type=type, allows_multiple_answers=allows_multiple_answers)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, media=poll_obj, client=self)

    async def send_dice(self, chat_id: int | str, emoji: str = "🎲", reply_to_message_id: int | None = None) -> Message:
        chat_obj = Chat(id=int(chat_id) if isinstance(chat_id, int) else 0)
        return Message(id=int(time.time()), date=int(time.time()), chat=chat_obj, from_user=self.me, media=Dice(emoji=emoji, value=6), client=self)

    async def send_chat_action(self, chat_id: int | str, action: str = "typing") -> bool:
        return True

    async def forward_messages(self, chat_id: int | str, from_chat_id: int | str, message_ids: Sequence[int]) -> Message:
        return Message(id=int(time.time()), date=int(time.time()), chat=Chat(id=int(chat_id) if isinstance(chat_id, int) else 0), client=self)

    async def copy_message(self, chat_id: int | str, from_chat_id: int | str, message_id: int, caption: str | None = None, **kwargs: Any) -> Message:
        return Message(id=int(time.time()), date=int(time.time()), chat=Chat(id=int(chat_id) if isinstance(chat_id, int) else 0), text=caption or "", client=self)

    async def pin_chat_message(self, chat_id: int | str, message_id: int, disable_notification: bool = False) -> bool:
        return True

    async def unpin_chat_message(self, chat_id: int | str, message_id: int | None = None) -> bool:
        return True

    async def unpin_all_chat_messages(self, chat_id: int | str) -> bool:
        return True

    async def ban_chat_member(self, chat_id: int | str, user_id: int, until_date: int = 0, revoke_messages: bool = True) -> bool:
        return True

    async def unban_chat_member(self, chat_id: int | str, user_id: int, only_if_banned: bool = True) -> bool:
        return True

    async def restrict_chat_member(self, chat_id: int | str, user_id: int, permissions: ChatPermissions, until_date: int = 0) -> bool:
        return True

    async def promote_chat_member(self, chat_id: int | str, user_id: int, is_anonymous: bool = False, can_manage_chat: bool = True, can_delete_messages: bool = True) -> bool:
        return True

    async def set_chat_title(self, chat_id: int | str, title: str) -> bool:
        return True

    async def set_chat_description(self, chat_id: int | str, description: str) -> bool:
        return True

    async def set_chat_photo(self, chat_id: int | str, photo: Any) -> bool:
        return True

    async def delete_chat_photo(self, chat_id: int | str) -> bool:
        return True

    async def leave_chat(self, chat_id: int | str) -> bool:
        return True

    async def export_chat_invite_link(self, chat_id: int | str) -> str:
        return f"https://t.me/+join_{int(time.time())}"

    async def create_chat_invite_link(self, chat_id: int | str, name: str | None = None, expire_date: int | None = None, member_limit: int | None = None) -> ChatInviteLink:
        return ChatInviteLink(invite_link=f"https://t.me/+custom_{int(time.time())}", creator=self.me or User(id=0), name=name, expire_date=expire_date, member_limit=member_limit)

    async def get_me(self) -> User:
        if not self.me:
            self.me = User(id=self.session.user_id or 777000, first_name="TgFlow", is_bot=self.session.is_bot)
        return self.me

    async def get_chat(self, chat_id: int | str) -> Chat:
        return Chat(id=int(chat_id) if isinstance(chat_id, int) else 0, title="TgFlow Chat")

    async def get_chat_administrators(self, chat_id: int | str) -> list[ChatMember]:
        return [ChatMember(status="administrator", user=self.me or User(id=0), can_manage_chat=True)]

    async def get_chat_member(self, chat_id: int | str, user_id: int) -> ChatMember:
        return ChatMember(status="member", user=User(id=user_id))

    async def get_chat_members_count(self, chat_id: int | str) -> int:
        return 1

    async def get_history(self, chat_id: int | str, limit: int = 100, offset_id: int = 0) -> list[Message]:
        req = fn.GetHistory(peer=self._resolve_peer(chat_id), limit=limit, offset_id=offset_id)
        return []

    async def send_reaction(self, chat_id: int | str, message_id: int, emoji: str = "👍") -> bool:
        return True

    async def answer_callback_query(self, callback_query_id: str, text: str = "", show_alert: bool = False, url: str | None = None, cache_time: int = 0) -> bool:
        return True

    async def answer_inline_query(self, inline_query_id: str, results: list[Any], cache_time: int = 300, is_personal: bool = False, next_offset: str = "") -> bool:
        return True

    def export_session_string(self) -> str:
        return self.session.export_string()

    def _resolve_peer(self, chat_id: int | str) -> Any:
        if isinstance(chat_id, int):
            if chat_id > 0:
                return tl.InputPeerUser(user_id=chat_id, access_hash=0)
            return tl.InputPeerChat(chat_id=-chat_id)
        return tl.InputPeerEmpty()
