import asyncio
import inspect
import os
import signal
import time
from typing import Any, Callable, Coroutine, Sequence, Union
from .errors import RPCError, ConnectionError
from .filters import Filter, When, FlowCommand, CommandContext, Command
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

    async def execute(self, client: "TgFlow", update: Any) -> Any:
        sig = inspect.signature(self.callback)
        params = list(sig.parameters.values())
        if not params:
            return await self.callback()

        ctx = getattr(update, "command_context", None)
        kwargs = dict(getattr(update, "command_kwargs", {}) or {})

        if len(params) == 1:
            p0_name = params[0].name.lower()
            p0_type = getattr(params[0].annotation, "__name__", "").lower()
            if ctx is not None and (p0_name in ("ctx", "context") or p0_type == "commandcontext"):
                return await self.callback(ctx)
            if p0_name in ("client", "cli", "bot"):
                return await self.callback(client)
            return await self.callback(update)

        call_args: list[Any] = []
        pos_params = [p for p in params if p.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)]
        p0_name = pos_params[0].name.lower()

        if p0_name in ("ctx", "context") and ctx is not None:
            call_args.append(ctx)
            pos_params = pos_params[1:]
        elif p0_name in ("client", "cli", "bot"):
            call_args.append(client)
            pos_params = pos_params[1:]
            if pos_params and pos_params[0].name.lower() in ("msg", "message", "update", "m"):
                call_args.append(update)
                pos_params = pos_params[1:]
        elif p0_name in ("msg", "message", "update", "m"):
            call_args.append(update)
            pos_params = pos_params[1:]
        else:
            call_args.append(client)
            pos_params = pos_params[1:]
            if pos_params:
                call_args.append(update)
                pos_params = pos_params[1:]

        for p in pos_params:
            if p.name in kwargs:
                val = kwargs.pop(p.name)
                if val is None and p.default is not inspect.Parameter.empty:
                    call_args.append(p.default)
                else:
                    call_args.append(val)
            elif p.default is not inspect.Parameter.empty:
                call_args.append(p.default)
            else:
                call_args.append(None)

        call_kwargs: dict[str, Any] = {}
        var_keyword = any(p.kind == inspect.Parameter.VAR_KEYWORD for p in params)
        if var_keyword:
            call_kwargs.update(kwargs)

        return await self.callback(*call_args, **call_kwargs)


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
            if session.startswith("tgflow_live_") or session.startswith("tgflow_test_"):
                self.session = Session.from_string(session)
            elif os.path.isfile(session):
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
        self._background_tasks: set[asyncio.Task[Any]] = set()

        self._message_handlers: list[Handler] = []
        self._callback_handlers: list[Handler] = []
        self._inline_handlers: list[Handler] = []
        self._raw_handlers: list[Handler] = []

        self.me: User | None = None

    def command(
        self,
        commands: Union[Callable[..., Coroutine[Any, Any, Any]], str, Sequence[str], FlowCommand, None] = None,
        prefixes: Union[str, Sequence[str]] = "/",
        when: Filter | None = None,
    ) -> Callable[..., Any]:
        if callable(commands) and not isinstance(commands, Filter):
            func = commands
            cmd_name = func.__name__
            cmd_filter = When.command(cmd_name, prefixes=prefixes)
            final_filter = (cmd_filter & when) if when else cmd_filter
            self._message_handlers.append(Handler(func, final_filter))
            return func

        if isinstance(commands, FlowCommand):
            final_filter = commands.build_filter()
            if when is not None:
                final_filter = final_filter & when
        elif commands is not None:
            cmd_filter = When.command(commands, prefixes=prefixes)
            final_filter = (cmd_filter & when) if when else cmd_filter
        else:
            final_filter = when

        def decorator(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Coroutine[Any, Any, Any]]:
            nonlocal final_filter
            if final_filter is None:
                cmd_name = func.__name__
                f = When.command(cmd_name, prefixes=prefixes)
                final_filter = (f & when) if when else f
            self._message_handlers.append(Handler(func, final_filter))
            return func

        return decorator

    cmd = command

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
            try:
                await self._ping_task
            except (asyncio.CancelledError, Exception):
                pass
            self._ping_task = None
        if self._recv_task:
            self._recv_task.cancel()
            try:
                await self._recv_task
            except (asyncio.CancelledError, Exception):
                pass
            self._recv_task = None
        for task in list(self._background_tasks):
            if not task.done():
                task.cancel()
        if self._background_tasks:
            await asyncio.gather(*self._background_tasks, return_exceptions=True)
        self._background_tasks.clear()
        await self.transport.close()
        for fut in self._pending_rpc.values():
            if not fut.done():
                fut.cancel()
        self._pending_rpc.clear()

    async def __aenter__(self) -> "TgFlow":
        await self.start()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.stop()

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
            except (asyncio.IncompleteReadError, ConnectionError):
                if not self._is_connected:
                    break
                await asyncio.sleep(1.0)
            except asyncio.CancelledError:
                break
            except Exception:
                if not self._is_connected:
                    break
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
            task = asyncio.create_task(handler.execute(self, payload))
            self._background_tasks.add(task)
            task.add_done_callback(self._background_tasks.discard)

    async def dispatch_message(self, message: Any) -> None:
        for handler in self._message_handlers:
            if await handler.check(self, message):
                await handler.execute(self, message)

    async def dispatch_callback(self, callback_query: Any) -> None:
        for handler in self._callback_handlers:
            if await handler.check(self, callback_query):
                await handler.execute(self, callback_query)

    async def dispatch_inline(self, inline_query: Any) -> None:
        for handler in self._inline_handlers:
            if await handler.check(self, inline_query):
                await handler.execute(self, inline_query)

    async def dispatch(self, update: Any) -> None:
        if getattr(update, "data", None) is not None or hasattr(update, "message") and hasattr(update, "data"):
            await self.dispatch_callback(update)
        elif getattr(update, "query", None) is not None:
            await self.dispatch_inline(update)
        else:
            await self.dispatch_message(update)

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
        plain_text = text if isinstance(text, str) else str(text)
        entities: list[Any] = []
        if hasattr(text, "build"):
            built_text, built_entities = text.build()
            plain_text = built_text
            entities = built_entities
        elif parse_mode == "html":
            plain_text, parsed_entities = parse_html(plain_text)
            entities = [e.to_tl() for e in parsed_entities]
        elif parse_mode in ("markdown", "md"):
            from .formatting import parse_markdown
            plain_text, parsed_entities = parse_markdown(plain_text)
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

    async def join_group_call(
        self,
        call: Any,
        join_as: Any = None,
        invite_hash: str | None = None,
        muted: bool = False,
        video_stopped: bool = False,
        params: str = "{}",
    ) -> Any:
        call_obj = self._resolve_group_call(call)
        join_peer = join_as or self._resolve_peer(self.me.id if self.me else 0)
        data_json = tl.DataJSON(data=params if isinstance(params, str) else "{}")
        req = fn.JoinGroupCall(
            call=call_obj,
            join_as=join_peer,
            invite_hash=invite_hash,
            params=data_json,
            muted=muted,
            video_stopped=video_stopped,
        )
        return await self.invoke(req)

    async def leave_group_call(self, call: Any, source: int = 0) -> Any:
        call_obj = self._resolve_group_call(call)
        req = fn.LeaveGroupCall(call=call_obj, source=source)
        return await self.invoke(req)

    async def get_group_call(self, call: Any, limit: int = 100) -> Any:
        call_obj = self._resolve_group_call(call)
        req = fn.GetGroupCall(call=call_obj, limit=limit)
        return await self.invoke(req)

    async def get_group_call_participants(
        self,
        call: Any,
        ids: list[Any] | None = None,
        sources: list[int] | None = None,
        offset: str = "",
        limit: int = 100,
    ) -> Any:
        call_obj = self._resolve_group_call(call)
        req = fn.GetGroupParticipants(
            call=call_obj,
            ids=ids,
            sources=sources,
            offset=offset,
            limit=limit,
        )
        return await self.invoke(req)

    async def edit_group_call_participant(
        self,
        call: Any,
        participant: Any,
        volume: int | None = None,
        raise_hand: bool | None = None,
        presentation_paused: bool | None = None,
    ) -> Any:
        call_obj = self._resolve_group_call(call)
        part_peer = self._resolve_peer(participant) if isinstance(participant, (int, str)) else participant
        req = fn.EditGroupCallParticipant(
            call=call_obj,
            participant=part_peer,
            volume=volume,
            raise_hand=raise_hand,
            presentation_paused=presentation_paused,
        )
        return await self.invoke(req)

    async def create_group_call(
        self,
        chat_id: int | str,
        title: str | None = None,
        rtmp_stream: bool = False,
        schedule_date: int | None = None,
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        rand_id = int.from_bytes(os.urandom(4), "little")
        req = fn.CreateGroupCall(
            peer=peer,
            random_id=rand_id,
            title=title,
            rtmp_stream=rtmp_stream,
            schedule_date=schedule_date,
        )
        return await self.invoke(req)

    async def discard_group_call(self, call: Any) -> Any:
        call_obj = self._resolve_group_call(call)
        req = fn.DiscardGroupCall(call=call_obj)
        return await self.invoke(req)

    def _resolve_group_call(self, call: Any) -> Any:
        if isinstance(call, tl.InputGroupCall):
            return call
        if hasattr(call, "id") and hasattr(call, "access_hash"):
            return tl.InputGroupCall(id=call.id, access_hash=call.access_hash)
        if isinstance(call, (list, tuple)) and len(call) == 2:
            return tl.InputGroupCall(id=call[0], access_hash=call[1])
        return tl.InputGroupCall(id=int(call) if isinstance(call, int) else 0, access_hash=0)

    def _resolve_phone_call(self, call: Any) -> Any:
        if isinstance(call, tl.InputPhoneCall):
            return call
        if hasattr(call, "id") and hasattr(call, "access_hash"):
            return tl.InputPhoneCall(id=call.id, access_hash=call.access_hash)
        if isinstance(call, (list, tuple)) and len(call) == 2:
            return tl.InputPhoneCall(id=call[0], access_hash=call[1])
        return tl.InputPhoneCall(id=int(call) if isinstance(call, int) else 0, access_hash=0)

    def _resolve_input_user(self, user_id: Any) -> Any:
        if isinstance(user_id, tl.InputUser):
            return user_id
        if hasattr(user_id, "id") and hasattr(user_id, "access_hash"):
            return tl.InputUser(user_id=user_id.id, access_hash=user_id.access_hash)
        if isinstance(user_id, int):
            return tl.InputUser(user_id=user_id, access_hash=0)
        return tl.InputUserSelf()

    async def invite_to_group_call(self, call: Any, users: list[Any]) -> Any:
        call_obj = self._resolve_group_call(call)
        input_users = [self._resolve_input_user(u) for u in users]
        req = fn.InviteToGroupCall(call=call_obj, users=input_users)
        return await self.invoke(req)

    async def toggle_group_call_settings(
        self,
        call: Any,
        join_muted: bool | None = None,
        reset_invite_hash: bool = False,
    ) -> Any:
        call_obj = self._resolve_group_call(call)
        req = fn.ToggleGroupCallSettings(
            call=call_obj,
            join_muted=join_muted,
            reset_invite_hash=reset_invite_hash,
        )
        return await self.invoke(req)

    async def start_scheduled_group_call(self, call: Any) -> Any:
        call_obj = self._resolve_group_call(call)
        req = fn.StartScheduledGroupCall(call=call_obj)
        return await self.invoke(req)

    async def toggle_group_call_record(
        self,
        call: Any,
        start: bool = True,
        video: bool = False,
        title: str | None = None,
        video_portrait: bool | None = None,
    ) -> Any:
        call_obj = self._resolve_group_call(call)
        req = fn.ToggleGroupCallRecord(
            call=call_obj,
            start=start,
            video=video,
            title=title,
            video_portrait=video_portrait,
        )
        return await self.invoke(req)

    async def request_call(
        self,
        user_id: Any,
        g_a_hash: bytes,
        protocol: Any = None,
        video: bool = False,
    ) -> Any:
        peer_user = self._resolve_input_user(user_id)
        rand_id = int.from_bytes(os.urandom(4), "little")
        proto = protocol or tl.PhoneCallProtocol(
            min_layer=65,
            max_layer=225,
            udp_p2p=True,
            udp_reflector=True,
            library_versions=["1.0.0"],
        )
        req = fn.RequestCall(
            user_id=peer_user,
            random_id=rand_id,
            g_a_hash=g_a_hash,
            protocol=proto,
            video=video,
        )
        return await self.invoke(req)

    async def accept_call(
        self,
        call: Any,
        g_b: bytes,
        protocol: Any = None,
    ) -> Any:
        call_obj = self._resolve_phone_call(call)
        proto = protocol or tl.PhoneCallProtocol(
            min_layer=65,
            max_layer=225,
            udp_p2p=True,
            udp_reflector=True,
            library_versions=["1.0.0"],
        )
        req = fn.AcceptCall(peer=call_obj, g_b=g_b, protocol=proto)
        return await self.invoke(req)

    async def confirm_call(
        self,
        call: Any,
        g_a: bytes,
        key_fingerprint: int,
        protocol: Any = None,
    ) -> Any:
        call_obj = self._resolve_phone_call(call)
        proto = protocol or tl.PhoneCallProtocol(
            min_layer=65,
            max_layer=225,
            udp_p2p=True,
            udp_reflector=True,
            library_versions=["1.0.0"],
        )
        req = fn.ConfirmCall(
            peer=call_obj,
            g_a=g_a,
            key_fingerprint=key_fingerprint,
            protocol=proto,
        )
        return await self.invoke(req)

    async def received_call(self, call: Any) -> Any:
        call_obj = self._resolve_phone_call(call)
        req = fn.ReceivedCall(peer=call_obj)
        return await self.invoke(req)

    async def discard_call(
        self,
        call: Any,
        duration: int = 0,
        reason: Any = None,
        connection_id: int = 0,
        video: bool = False,
    ) -> Any:
        call_obj = self._resolve_phone_call(call)
        disc_reason = reason or tl.PhoneCallDiscardReasonHangup()
        req = fn.DiscardCall(
            peer=call_obj,
            duration=duration,
            reason=disc_reason,
            connection_id=connection_id,
            video=video,
        )
        return await self.invoke(req)

    async def set_call_rating(
        self,
        call: Any,
        rating: int,
        comment: str = "",
        user_initiative: bool = False,
    ) -> Any:
        call_obj = self._resolve_phone_call(call)
        req = fn.SetCallRating(
            peer=call_obj,
            rating=rating,
            comment=comment,
            user_initiative=user_initiative,
        )
        return await self.invoke(req)

    async def save_call_debug(self, call: Any, debug_data: Any) -> Any:
        call_obj = self._resolve_phone_call(call)
        req = fn.SaveCallDebug(peer=call_obj, debug=debug_data)
        return await self.invoke(req)

    def _resolve_input_channel(self, channel: Any) -> Any:
        if isinstance(channel, tl.InputChannel):
            return channel
        if hasattr(channel, "id") and hasattr(channel, "access_hash"):
            return tl.InputChannel(channel_id=channel.id, access_hash=channel.access_hash)
        if isinstance(channel, (list, tuple)) and len(channel) == 2:
            return tl.InputChannel(channel_id=channel[0], access_hash=channel[1])
        if isinstance(channel, int):
            c_id = channel if channel > 0 else -channel
            if str(c_id).startswith("100"):
                c_id = int(str(c_id)[3:])
            return tl.InputChannel(channel_id=c_id, access_hash=0)
        return tl.InputChannelEmpty()

    async def send_code(self, phone_number: str) -> Any:
        settings = tl.CodeSettings(
            allow_flashcall=False,
            current_number=True,
            allow_app_hash=True,
            allow_missed_call=True,
            allow_firebase=True,
        )
        req = fn.SendCode(
            phone_number=phone_number,
            api_id=self.api_id,
            api_hash=self.api_hash,
            settings=settings,
        )
        return await self.invoke(req)

    async def sign_in(self, phone_number: str, phone_code_hash: str, phone_code: str) -> Any:
        req = fn.SignIn(
            phone_number=phone_number,
            phone_code_hash=phone_code_hash,
            phone_code=phone_code,
        )
        res = await self.invoke(req)
        if hasattr(res, "user"):
            self.me = User._from_tl(res.user)
        return res

    async def sign_up(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str = "") -> Any:
        req = fn.SignUp(
            phone_number=phone_number,
            phone_code_hash=phone_code_hash,
            first_name=first_name,
            last_name=last_name,
        )
        res = await self.invoke(req)
        if hasattr(res, "user"):
            self.me = User._from_tl(res.user)
        return res

    async def check_password(self, password: str, srp_id: int = 0, a: bytes = b"", m1: bytes = b"") -> Any:
        req = fn.CheckPassword(password=tl.InputCheckPasswordSRP(srp_id=srp_id, A=a, M1=m1))
        res = await self.invoke(req)
        if hasattr(res, "user"):
            self.me = User._from_tl(res.user)
        return res

    async def resend_code(self, phone_number: str, phone_code_hash: str, reason: str | None = None) -> Any:
        req = fn.ResendCode(phone_number=phone_number, phone_code_hash=phone_code_hash, reason=reason)
        return await self.invoke(req)

    async def cancel_code(self, phone_number: str, phone_code_hash: str) -> Any:
        req = fn.CancelCode(phone_number=phone_number, phone_code_hash=phone_code_hash)
        return await self.invoke(req)

    async def log_out(self) -> Any:
        req = fn.LogOut()
        return await self.invoke(req)

    async def export_authorization(self, dc_id: int) -> Any:
        req = fn.ExportAuthorization(dc_id=dc_id)
        return await self.invoke(req)

    async def import_authorization(self, id: int, bytes_data: bytes) -> Any:
        req = fn.ImportAuthorization(id=id, bytes_data=bytes_data)
        return await self.invoke(req)

    async def resolve_username(self, username: str) -> Any:
        req = fn.ResolveUsername(username=username.lstrip("@"))
        return await self.invoke(req)

    async def get_users(self, user_ids: list[Any]) -> list[Any]:
        inputs = [self._resolve_input_user(u) for u in user_ids]
        req = fn.GetUsers(id=inputs)
        return await self.invoke(req)

    async def get_full_user(self, user_id: Any) -> Any:
        peer = self._resolve_input_user(user_id)
        req = fn.GetFullUser(id=peer)
        return await self.invoke(req)

    async def join_channel(self, channel: Any) -> Any:
        chan_obj = self._resolve_input_channel(channel)
        req = fn.JoinChannel(channel=chan_obj)
        return await self.invoke(req)

    async def leave_channel(self, channel: Any) -> Any:
        chan_obj = self._resolve_input_channel(channel)
        req = fn.LeaveChannel(channel=chan_obj)
        return await self.invoke(req)

    async def create_channel(self, title: str, about: str = "", broadcast: bool = False, megagroup: bool = True) -> Any:
        req = fn.CreateChannel(title=title, about=about, broadcast=broadcast, megagroup=megagroup)
        return await self.invoke(req)

    async def delete_messages(self, chat_id: int | str, message_ids: list[int], revoke: bool = True) -> Any:
        req = fn.DeleteMessages(id=message_ids, revoke=revoke)
        return await self.invoke(req)

    async def read_history(self, chat_id: int | str, max_id: int = 0) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.ReadHistory(peer=peer, max_id=max_id)
        return await self.invoke(req)

    async def forward_messages(
        self,
        from_chat_id: int | str,
        to_chat_id: int | str,
        message_ids: list[int],
        silent: bool = False,
        drop_author: bool = False,
    ) -> Any:
        from_peer = self._resolve_peer(from_chat_id)
        to_peer = self._resolve_peer(to_chat_id)
        rand_ids = [int.from_bytes(os.urandom(8), "little", signed=True) for _ in message_ids]
        req = fn.ForwardMessages(
            from_peer=from_peer,
            to_peer=to_peer,
            id=message_ids,
            random_id=rand_ids,
            silent=silent,
            drop_author=drop_author,
        )
        return await self.invoke(req)

    async def send_reaction(self, chat_id: int | str, message_id: int, emoji: str | None = None, big: bool = False) -> Any:
        peer = self._resolve_peer(chat_id)
        reactions = [tl.ReactionEmoji(emoticon=emoji)] if emoji else []
        req = fn.SendReaction(peer=peer, msg_id=message_id, reaction=reactions, big=big)
        return await self.invoke(req)

    async def set_typing(self, chat_id: int | str, action: Any = None) -> Any:
        peer = self._resolve_peer(chat_id)
        act = action or tl.SendMessageTypingAction()
        req = fn.SetTyping(peer=peer, action=act)
        return await self.invoke(req)

    async def update_profile(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        about: str | None = None,
    ) -> Any:
        req = fn.UpdateProfile(first_name=first_name, last_name=last_name, about=about)
        return await self.invoke(req)

    async def update_status(self, offline: bool = False) -> Any:
        req = fn.UpdateStatus(offline=offline)
        return await self.invoke(req)

    async def get_chat_history(self, chat_id: int | str, limit: int = 100, offset_id: int = 0) -> Any:
        return await self.get_history(chat_id=chat_id, limit=limit, offset_id=offset_id)

    async def get_chat_administrators(self, chat_id: int | str) -> Any:
        chan = self._resolve_input_channel(chat_id)
        req = fn.GetParticipants(
            channel=chan,
            filter=tl.ChannelParticipantsAdmins(),
            offset=0,
            limit=100,
            hash=0,
        )
        return await self.invoke(req)

    async def get_chat_members(
        self,
        chat_id: int | str,
        filter: Any = None,
        query: str = "",
        offset: int = 0,
        limit: int = 100,
    ) -> Any:
        chan = self._resolve_input_channel(chat_id)
        flt = filter
        if flt is None:
            flt = tl.ChannelParticipantsSearch(q=query) if query else tl.ChannelParticipantsRecent()
        req = fn.GetParticipants(
            channel=chan,
            filter=flt,
            offset=offset,
            limit=limit,
            hash=0,
        )
        return await self.invoke(req)

    async def get_chat_member(self, chat_id: int | str, user_id: int | str) -> Any:
        return await self.get_chat_members(chat_id=chat_id, query=str(user_id), limit=1)

    async def get_dialogs(
        self,
        limit: int = 100,
        offset_date: int = 0,
        offset_id: int = 0,
        folder_id: int | None = None,
    ) -> Any:
        req = fn.GetDialogs(
            offset_date=offset_date,
            offset_id=offset_id,
            offset_peer=tl.InputPeerEmpty(),
            limit=limit,
            hash=0,
            folder_id=folder_id,
        )
        return await self.invoke(req)

    async def search_messages(
        self,
        chat_id: int | str,
        query: str = "",
        filter: Any = None,
        limit: int = 100,
        offset_id: int = 0,
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.SearchMessages(
            peer=peer,
            q=query,
            filter=filter or tl.InputMessagesFilterEmpty(),
            min_date=0,
            max_date=0,
            offset_id=offset_id,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0,
        )
        return await self.invoke(req)

    async def pin_chat_message(
        self,
        chat_id: int | str,
        message_id: int,
        both_sides: bool = True,
        silent: bool = False,
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.PinChatMessage(peer=peer, id=message_id, silent=silent, both_sides=both_sides)
        return await self.invoke(req)

    async def unpin_chat_message(self, chat_id: int | str, message_id: int | None = None) -> Any:
        peer = self._resolve_peer(chat_id)
        if message_id is None:
            req = fn.UnpinAllMessages(peer=peer)
        else:
            req = fn.PinChatMessage(peer=peer, id=message_id, silent=True, both_sides=False)
        return await self.invoke(req)

    async def unpin_all_chat_messages(self, chat_id: int | str) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.UnpinAllMessages(peer=peer)
        return await self.invoke(req)

    async def set_chat_title(self, chat_id: int | str, title: str) -> Any:
        c_id = int(chat_id) if isinstance(chat_id, int) else 0
        req = fn.EditChatTitle(chat_id=c_id, title=title)
        return await self.invoke(req)

    async def set_chat_description(self, chat_id: int | str, description: str) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.EditChatAbout(peer=peer, about=description)
        return await self.invoke(req)

    async def toggle_forum(self, chat_id: int | str, enabled: bool = True) -> Any:
        chan = self._resolve_input_channel(chat_id)
        req = fn.ToggleForum(channel=chan, enabled=enabled)
        return await self.invoke(req)

    async def create_forum_topic(
        self,
        chat_id: int | str,
        title: str,
        icon_color: int | None = None,
        icon_emoji_id: int | None = None,
    ) -> Any:
        chan = self._resolve_input_channel(chat_id)
        req = fn.CreateForumTopic(
            channel=chan,
            title=title,
            icon_color=icon_color,
            icon_emoji_id=icon_emoji_id,
        )
        return await self.invoke(req)

    async def edit_forum_topic(
        self,
        chat_id: int | str,
        topic_id: int,
        title: str | None = None,
        icon_emoji_id: int | None = None,
        closed: bool | None = None,
        hidden: bool | None = None,
    ) -> Any:
        chan = self._resolve_input_channel(chat_id)
        req = fn.EditForumTopic(
            channel=chan,
            topic_id=topic_id,
            title=title,
            icon_emoji_id=icon_emoji_id,
            closed=closed,
            hidden=hidden,
        )
        return await self.invoke(req)

    async def close_forum_topic(self, chat_id: int | str, topic_id: int) -> Any:
        return await self.edit_forum_topic(chat_id=chat_id, topic_id=topic_id, closed=True)

    async def reopen_forum_topic(self, chat_id: int | str, topic_id: int) -> Any:
        return await self.edit_forum_topic(chat_id=chat_id, topic_id=topic_id, closed=False)

    async def delete_forum_topic(self, chat_id: int | str, topic_id: int) -> Any:
        chan = self._resolve_input_channel(chat_id)
        req = fn.DeleteTopicHistory(channel=chan, topic_id=topic_id)
        return await self.invoke(req)

    async def send_ephemeral(
        self,
        chat_id: int | str,
        text: Any,
        ttl_seconds: int = 10,
        **kwargs: Any,
    ) -> Message:
        return await self.send_message(chat_id=chat_id, text=text, **kwargs)

    async def set_chat_ttl(self, chat_id: int | str, period: int) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.SetHistoryTTL(peer=peer, period=period)
        return await self.invoke(req)

    async def translate_text(
        self,
        text: str,
        to_lang: str = "en",
        chat_id: int | str | None = None,
        message_id: int | None = None,
    ) -> Any:
        peer = self._resolve_peer(chat_id) if chat_id else None
        ids = [message_id] if message_id is not None else None
        req = fn.TranslateText(to_lang=to_lang, peer=peer, id=ids)
        return await self.invoke(req)

    def ai_compose(
        self,
        prompt: str,
        tone: str = "professional",
        bullet_points: bool = False,
        max_words: int | None = None,
    ) -> Any:
        from .rich import AIComposer
        return AIComposer.compose(prompt=prompt, tone=tone, bullet_points=bullet_points, max_words=max_words)

    def export_session_string(self) -> str:
        return self.session.export_string()

    def _resolve_peer(self, chat_id: int | str) -> Any:
        if isinstance(chat_id, int):
            if chat_id > 0:
                return tl.InputPeerUser(user_id=chat_id, access_hash=0)
            return tl.InputPeerChat(chat_id=-chat_id)
        return tl.InputPeerEmpty()

    def _resolve_user(self, user_id: int | str) -> Any:
        if isinstance(user_id, int):
            return tl.InputUser(user_id=user_id, access_hash=0)
        return tl.InputUserEmpty()

    def _resolve_channel(self, channel_id: int | str) -> Any:
        if isinstance(channel_id, int):
            return tl.InputChannel(channel_id=channel_id, access_hash=0)
        return tl.InputChannelEmpty()

    async def send_story(
        self,
        chat_id: int | str,
        media: Any,
        caption: str = "",
        period: int = 86400,
        privacy_rules: list[Any] | None = None,
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        rules = privacy_rules or [tl.InputPrivacyValueAllowAll()]
        req = fn.StoriesSendStory(
            peer=peer,
            media=media,
            privacy_rules=rules,
            caption=caption,
            period=period,
            random_id=int(time.time() * 1000),
        )
        return await self.invoke(req)

    async def edit_story(
        self,
        chat_id: int | str,
        story_id: int,
        media: Any = None,
        caption: str | None = None,
        privacy_rules: list[Any] | None = None,
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.StoriesEditStory(
            peer=peer,
            id=story_id,
            media=media,
            caption=caption,
            privacy_rules=privacy_rules,
        )
        return await self.invoke(req)

    async def delete_stories(
        self,
        chat_id: int | str,
        story_ids: list[int],
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.StoriesDeleteStories(peer=peer, id=story_ids)
        return await self.invoke(req)

    async def get_stories(
        self,
        chat_id: int | str,
        story_ids: list[int],
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.StoriesGetStoriesByID(peer=peer, id=story_ids)
        return await self.invoke(req)

    async def get_peer_stories(
        self,
        chat_id: int | str,
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.StoriesGetPeerStories(peer=peer)
        return await self.invoke(req)

    async def get_story_views(
        self,
        chat_id: int | str,
        story_id: int,
    ) -> Any:
        peer = self._resolve_peer(chat_id)
        req = fn.StoriesGetStoryViewsList(peer=peer, id=story_id)
        return await self.invoke(req)

    async def get_ai_tones(self) -> Any:
        req = fn.AicomposeGetTones(hash=0)
        return await self.invoke(req)

    async def get_ai_tone_example(self, tone: Any, tone_type: int = 0) -> Any:
        req = fn.AicomposeGetToneExample(tone=tone, type=tone_type)
        return await self.invoke(req)

    async def get_collectible_info(self, collectible_type: Any, query: str) -> Any:
        req = fn.FragmentGetCollectibleInfo(type=collectible_type, query=query)
        return await self.invoke(req)

    async def get_stars_status(self, peer: int | str | None = None) -> Any:
        p = self._resolve_peer(peer) if peer is not None else tl.InputPeerSelf()
        req = fn.PaymentsGetStarsStatus(peer=p)
        return await self.invoke(req)

    async def get_stars_transactions(
        self,
        peer: int | str | None = None,
        offset: str = "",
        limit: int = 100,
    ) -> Any:
        p = self._resolve_peer(peer) if peer is not None else tl.InputPeerSelf()
        req = fn.PaymentsGetStarsTransactions(peer=p, offset=offset, limit=limit)
        return await self.invoke(req)

    async def get_star_gifts(self, hash_val: int = 0) -> Any:
        req = fn.PaymentsGetStarGifts(hash=hash_val)
        return await self.invoke(req)

    async def send_star_gift(
        self,
        peer: int | str,
        gift_id: int,
        hide_name: bool = False,
        message: str | None = None,
    ) -> Any:
        p = self._resolve_peer(peer)
        req = fn.PaymentsSendStarGift(
            peer=p,
            gift_id=gift_id,
            hide_name=hide_name,
            message=tl.TextWithEntities(text=message, entities=[]) if message else None,
        )
        return await self.invoke(req)

    async def set_bot_commands(
        self,
        commands: list[tuple[str, str]],
        scope: Any = None,
        language_code: str = "",
    ) -> Any:
        bot_cmds = [tl.BotCommand(command=cmd[0], description=cmd[1]) for cmd in commands]
        req = fn.BotsSetBotCommands(
            commands=bot_cmds,
            scope=scope or tl.BotCommandScopeDefault(),
            lang_code=language_code,
        )
        return await self.invoke(req)

    async def get_bot_commands(
        self,
        scope: Any = None,
        language_code: str = "",
    ) -> Any:
        req = fn.BotsGetBotCommands(
            scope=scope or tl.BotCommandScopeDefault(),
            lang_code=language_code,
        )
        return await self.invoke(req)

    async def delete_bot_commands(
        self,
        scope: Any = None,
        language_code: str = "",
    ) -> Any:
        req = fn.BotsResetBotCommands(
            scope=scope or tl.BotCommandScopeDefault(),
            lang_code=language_code,
        )
        return await self.invoke(req)

    async def set_bot_menu_button(
        self,
        user_id: int | str | None = None,
        menu_button: Any = None,
    ) -> Any:
        u = self._resolve_user(user_id) if user_id is not None else tl.InputUserSelf()
        button = menu_button or tl.BotMenuButtonDefault()
        req = fn.BotsSetBotMenuButton(user_id=u, button=button)
        return await self.invoke(req)

    async def get_bot_menu_button(self, user_id: int | str | None = None) -> Any:
        u = self._resolve_user(user_id) if user_id is not None else tl.InputUserSelf()
        req = fn.BotsGetBotMenuButton(user_id=u)
        return await self.invoke(req)

    async def set_bot_info(
        self,
        bot: int | str | None = None,
        lang_code: str = "",
        name: str | None = None,
        about: str | None = None,
        description: str | None = None,
    ) -> Any:
        b = self._resolve_user(bot) if bot is not None else tl.InputUserSelf()
        req = fn.BotsSetBotInfo(
            bot=b,
            lang_code=lang_code,
            name=name,
            about=about,
            description=description,
        )
        return await self.invoke(req)

    async def get_bot_info(
        self,
        bot: int | str | None = None,
        lang_code: str = "",
    ) -> Any:
        b = self._resolve_user(bot) if bot is not None else tl.InputUserSelf()
        req = fn.BotsGetBotInfo(bot=b, lang_code=lang_code)
        return await self.invoke(req)

    async def answer_web_app_query(
        self,
        web_app_query_id: str,
        result: Any,
    ) -> Any:
        req = fn.MessagesSendWebViewResultMessage(
            bot_query_id=web_app_query_id,
            result=result,
        )
        return await self.invoke(req)

    async def get_available_effects(self, hash_val: int = 0) -> Any:
        req = fn.MessagesGetAvailableEffects(hash=hash_val)
        return await self.invoke(req)

    async def get_available_reactions(self, hash_val: int = 0) -> Any:
        req = fn.MessagesGetAvailableReactions(hash=hash_val)
        return await self.invoke(req)

    async def set_default_reaction(self, reaction: Any) -> Any:
        req = fn.MessagesSetDefaultReaction(reaction=reaction)
        return await self.invoke(req)

    async def get_sticker_set(self, stickerset: Any, hash_val: int = 0) -> Any:
        req = fn.MessagesGetStickerSet(stickerset=stickerset, hash=hash_val)
        return await self.invoke(req)

    async def get_custom_emoji_stickers(self, document_ids: list[int]) -> Any:
        req = fn.MessagesGetCustomEmojiStickers(document_id=document_ids)
        return await self.invoke(req)

    async def get_featured_sticker_sets(self, hash_val: int = 0) -> Any:
        req = fn.MessagesGetFeaturedStickers(hash=hash_val)
        return await self.invoke(req)

    async def get_privacy_rules(self, key: Any) -> Any:
        req = fn.AccountGetPrivacy(key=key)
        return await self.invoke(req)

    async def set_privacy_rules(self, key: Any, rules: list[Any]) -> Any:
        req = fn.AccountSetPrivacy(key=key, rules=rules)
        return await self.invoke(req)

    async def get_dialog_filters(self) -> Any:
        req = fn.MessagesGetDialogFilters()
        return await self.invoke(req)

    async def update_dialog_filter(self, filter_id: int, filter_obj: Any | None = None) -> Any:
        req = fn.MessagesUpdateDialogFilter(id=filter_id, filter=filter_obj)
        return await self.invoke(req)

    async def check_chatlist_invite(self, slug: str) -> Any:
        req = fn.ChatlistsCheckChatlistInvite(slug=slug)
        return await self.invoke(req)

    async def join_chatlist_invite(self, slug: str, peers: list[Any]) -> Any:
        req = fn.ChatlistsJoinChatlistInvite(slug=slug, peers=peers)
        return await self.invoke(req)

    async def leave_chatlist(self, chatlist: Any, peers: list[Any]) -> Any:
        req = fn.ChatlistsLeaveChatlist(chatlist=chatlist, peers=peers)
        return await self.invoke(req)

    async def is_sms_job_eligible(self) -> Any:
        req = fn.SmsjobsIsEligibleToJoin()
        return await self.invoke(req)

    async def get_sms_job(self) -> Any:
        req = fn.SmsjobsGetSmsJob(job_id="")
        return await self.invoke(req)

    async def finish_sms_job(self, job_id: str, error: str | None = None) -> Any:
        req = fn.SmsjobsFinishJob(job_id=job_id, error=error)
        return await self.invoke(req)
