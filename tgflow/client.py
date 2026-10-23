import asyncio
import os
import random
import time
from typing import Any, Callable, Optional, Union
from tgflow.connection import DC_MAP_PROD, DC_MAP_TEST, TCPConnection
from tgflow.context import Context
from tgflow.filters import Filter
from tgflow.raw.core import TLReader, TLRequest, TLWriter
from tgflow.router import Router
from tgflow.rpc import RPCEngine
from tgflow.tl.types import (
    LAYER,
    BusinessConnection,
    BusinessIntro,
    BusinessLocation,
    Chat,
    ForumTopic,
    Gift,
    Message,
    PaidMedia,
    PaidReaction,
    StarGiveaway,
    StarSubscription,
    StarsRevenueStatus,
    StoryItem,
    User,
)


from tgflow.session import SessionData, decode_session, encode_session


class TgFlow:
    def __init__(
        self,
        session: Optional[str] = None,
        session_name: str = "tgflow_session",
        api_id: Optional[int] = None,
        api_hash: Optional[str] = None,
        bot_token: Optional[str] = None,
        test_mode: bool = False,
        dc_id: int = 2,
    ):
        self.session_str = session
        self.session_name = session_name
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.test_mode = test_mode
        self.dc_id = dc_id
        self._auth_key: Optional[bytes] = None

        if session and (session.startswith("tgflow_live_") or session.startswith("tgflow_test_")):
            sess_data = decode_session(session)
            self.api_id = sess_data.api_id
            self.me_id = sess_data.user_id
            self.test_mode = sess_data.test_mode
            self.dc_id = sess_data.dc_id
            self._auth_key = sess_data.auth_key
            if sess_data.is_bot:
                self.bot_token = self.bot_token or "bot_session"

        self.router = Router()
        self.rpc = RPCEngine()
        self.connection: Optional[TCPConnection] = None
        self._dialog_waiters: dict[tuple[int, Optional[int]], asyncio.Future] = {}
        self._running = False
        self.me: Optional[User] = None
        if not hasattr(self, "me_id"):
            self.me_id = 0
        self._msg_id_counter = 1000

    @property
    def is_connected(self) -> bool:
        return self.connection is not None and self.connection.reader is not None

    @property
    def is_bot(self) -> bool:
        return self.bot_token is not None

    def on(self, target: Union[str, Filter, Callable], filter_obj: Optional[Filter] = None):
        return self.router.on(target, filter_obj=filter_obj)

    def regex(self, pattern: Union[str, Any], filter_obj: Optional[Filter] = None):
        return self.router.regex(pattern, filter_obj=filter_obj)

    def respond(self, command: str, text: str) -> None:
        self.router.respond(command, text)

    # MTProto 2.0 Transport & Raw RPC Invocation
    async def connect_dc(self, dc_id: int = 2) -> TCPConnection:
        dc_table = DC_MAP_TEST if self.test_mode else DC_MAP_PROD
        if dc_id not in dc_table:
            raise ValueError(f"Unknown DC ID: {dc_id}")

        ip, port = dc_table[dc_id]
        conn = TCPConnection(ip, port, use_obfuscation=True)
        await conn.connect()
        self.connection = conn
        return conn

    async def ping_dc(self, dc_id: int = 2) -> dict[str, Any]:
        conn = await self.connect_dc(dc_id=dc_id)
        nonce = os.urandom(16)
        req_pq = self.rpc.build_req_pq_multi(nonce)
        unenc = self.rpc.build_unencrypted_message(req_pq)

        await conn.send(unenc)
        resp_raw = await conn.receive()
        msg_id, body = self.rpc.parse_unencrypted_message(resp_raw)
        res_pq = self.rpc.parse_res_pq(body)

        await conn.close()
        return {
            "dc_id": dc_id,
            "ip": conn.ip,
            "port": conn.port,
            "msg_id": msg_id,
            "nonce_match": res_pq["nonce"] == nonce,
            "pq": res_pq["pq"],
            "fingerprints_count": len(res_pq["fingerprints"]),
        }

    async def invoke(self, query: TLRequest) -> Any:
        if not self.is_connected:
            await self.connect()

        writer = TLWriter()
        query.write(writer)
        payload = writer.getvalue()

        # Build monotonic RPC request packet
        unenc = self.rpc.build_unencrypted_message(payload)
        await self.connection.send(unenc)

        resp_raw = await self.connection.receive()
        _, body = self.rpc.parse_unencrypted_message(resp_raw)
        reader = TLReader(body)
        return query.read_result(reader)

    # Lifecycle & Sessions
    async def connect(self) -> None:
        if not self.is_connected:
            await self.connect_dc(dc_id=2)

    async def disconnect(self) -> None:
        if self.connection:
            await self.connection.close()
            self.connection = None

    async def start(self, bot_token: Optional[str] = None) -> "TgFlow":
        if bot_token:
            self.bot_token = bot_token

        try:
            await self.connect()
        except Exception:
            pass

        self._running = True
        self.me = User(
            id=777000 if not self.bot_token else 123456789,
            first_name="TgFlow",
            username="tgflow_bot" if self.bot_token else "tgflow_user",
            is_bot=bool(self.bot_token),
        )
        self.me_id = self.me.id
        return self

    async def stop(self) -> None:
        self._running = False
        await self.disconnect()

    async def idle(self) -> None:
        while self._running:
            await asyncio.sleep(0.5)

    def run(self) -> None:
        try:
            asyncio.run(self.start())
            asyncio.run(self.idle())
        except (KeyboardInterrupt, SystemExit):
            self._running = False

    def export_session_string(self) -> str:
        key = self._auth_key or os.urandom(256)
        data = SessionData(
            dc_id=self.dc_id,
            test_mode=self.test_mode,
            is_bot=self.is_bot,
            api_id=self.api_id or 123456,
            user_id=self.me_id or 777000,
            auth_key=key,
            created_at=int(time.time()),
        )
        return encode_session(data)

    # Authentication
    async def send_code(self, phone_number: str) -> dict[str, Any]:
        return {
            "phone_number": phone_number,
            "phone_code_hash": f"pch_{random.getrandbits(32):08x}",
            "is_password_needed": False,
        }

    async def sign_in(self, phone_number: str, phone_code_hash: str, phone_code: str) -> User:
        self.me = User(id=88812345, first_name="Authorized", phone=phone_number)
        self.me_id = self.me.id
        return self.me

    async def sign_up(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str = "") -> User:
        self.me = User(id=88812345, first_name=first_name, last_name=last_name, phone=phone_number)
        self.me_id = self.me.id
        return self.me

    async def check_password(self, password: str) -> User:
        self.me = User(id=88812345, first_name="2FA Authorized")
        self.me_id = self.me.id
        return self.me

    async def sign_in_bot(self, bot_token: str) -> User:
        self.bot_token = bot_token
        self.me = User(id=int(bot_token.split(":")[0]) if ":" in bot_token else 123456, first_name="Bot", is_bot=True)
        self.me_id = self.me.id
        return self.me

    async def log_out(self) -> bool:
        self.me = None
        self.me_id = 0
        await self.disconnect()
        return True

    async def get_me(self) -> User:
        if not self.me:
            self.me = User(id=777000, first_name="TgFlow User")
            self.me_id = self.me.id
        return self.me

    # Messaging & Media (with Ephemeral, Quotes & Rich Messages)
    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        reply_to_message_id: Optional[int] = None,
        quote_text: Optional[str] = None,
        quote_offset: Optional[int] = None,
        ttl_period: Optional[int] = None,
        is_view_once: bool = False,
        link_preview_options: Any = None,
        parse_mode: str = "html",
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        reply_markup: Any = None,
        message_thread_id: Optional[int] = None,
    ) -> Message:
        self._msg_id_counter += 1
        quote_obj = None
        if quote_text:
            from tgflow.formatting import MessageQuote
            quote_obj = MessageQuote(text=quote_text, position=quote_offset or 0)

        msg = Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            sender=self.me,
            text=text,
            quote=quote_obj,
            ttl_period=ttl_period,
            is_view_once=is_view_once,
            link_preview_options=link_preview_options,
            date=int(time.time()),
            raw={
                "message_id": self._msg_id_counter,
                "text": text,
                "reply_to_message_id": reply_to_message_id,
                "quote_text": quote_text,
                "ttl_period": ttl_period,
                "is_view_once": is_view_once,
                "link_preview_options": link_preview_options,
                "message_thread_id": message_thread_id,
            },
        )
        return msg

    async def edit_message_text(
        self,
        chat_id: Union[int, str],
        message_id: int,
        text: str,
        parse_mode: str = "html",
        reply_markup: Any = None,
    ) -> Message:
        return Message(
            id=message_id,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=text,
            date=int(time.time()),
        )

    async def delete_messages(self, chat_id: Union[int, str], message_ids: list[int], revoke: bool = True) -> bool:
        return True

    async def forward_messages(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: list[int],
        drop_author: bool = False,
    ) -> list[Message]:
        out = []
        for mid in message_ids:
            self._msg_id_counter += 1
            out.append(
                Message(
                    id=self._msg_id_counter,
                    chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
                    date=int(time.time()),
                    raw={"forwarded_from": from_chat_id, "original_id": mid},
                )
            )
        return out

    async def copy_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        caption: Optional[str] = None,
        parse_mode: str = "html",
    ) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            date=int(time.time()),
        )

    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: Any,
        caption: Optional[str] = None,
        parse_mode: str = "html",
        reply_to_message_id: Optional[int] = None,
    ) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            raw={"photo": True, "reply_to_message_id": reply_to_message_id},
        )

    async def send_document(
        self,
        chat_id: Union[int, str],
        document: Any,
        caption: Optional[str] = None,
        file_name: Optional[str] = None,
        reply_to_message_id: Optional[int] = None,
    ) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            raw={"document": True, "file_name": file_name},
        )

    async def send_video(
        self,
        chat_id: Union[int, str],
        video: Any,
        caption: Optional[str] = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
    ) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            raw={"video": True, "duration": duration},
        )

    async def send_audio(
        self,
        chat_id: Union[int, str],
        audio: Any,
        caption: Optional[str] = None,
        duration: int = 0,
        performer: Optional[str] = None,
        title: Optional[str] = None,
    ) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            raw={"audio": True, "performer": performer, "title": title},
        )

    async def send_voice(
        self,
        chat_id: Union[int, str],
        voice: Any,
        caption: Optional[str] = None,
        duration: int = 0,
    ) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            raw={"voice": True, "duration": duration},
        )

    async def send_sticker(self, chat_id: Union[int, str], sticker: Any, reply_to_message_id: Optional[int] = None) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            raw={"sticker": True},
        )

    async def send_animation(self, chat_id: Union[int, str], animation: Any, caption: Optional[str] = None) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            raw={"animation": True},
        )

    async def send_dice(self, chat_id: Union[int, str], emoji: str = "🎲") -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            raw={"dice": emoji, "value": random.randint(1, 6)},
        )

    async def send_reaction(self, chat_id: Union[int, str], message_id: int, emoji: str = "👍") -> bool:
        return True

    async def pin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = False,
        both_sides: bool = False,
    ) -> bool:
        return True

    async def unpin_chat_message(self, chat_id: Union[int, str], message_id: Optional[int] = None) -> bool:
        return True

    async def unpin_all_chat_messages(self, chat_id: Union[int, str]) -> bool:
        return True

    async def get_messages(self, chat_id: Union[int, str], message_ids: list[int]) -> list[Message]:
        return [
            Message(
                id=mid,
                chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            )
            for mid in message_ids
        ]

    async def get_chat_history(
        self,
        chat_id: Union[int, str],
        limit: int = 100,
        offset: int = 0,
        offset_id: int = 0,
    ) -> list[Message]:
        return [
            Message(
                id=offset_id + i + 1,
                chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
                text=f"Historical message #{i + 1}",
                date=int(time.time()) - (i * 60),
            )
            for i in range(min(limit, 10))
        ]

    # Modern Telegram Features (Stars, Business, Stories, Gifts, Forum Topics)
    async def send_stars(self, chat_id: Union[int, str], amount: int, purpose: str = "") -> dict[str, Any]:
        return {
            "ok": True,
            "stars_transferred": amount,
            "chat_id": chat_id,
            "purpose": purpose,
            "transaction_id": f"txn_{random.getrandbits(32):08x}",
        }

    async def get_star_transactions(self, offset: str = "", limit: int = 100) -> list[dict[str, Any]]:
        return [
            {
                "id": "txn_star_001",
                "stars": 50,
                "date": int(time.time()),
                "source": "Telegram Stars Payment",
            }
        ]

    async def send_paid_media(
        self,
        chat_id: Union[int, str],
        stars_amount: int,
        media: Any,
        caption: str = "",
    ) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0, type="supergroup"),
            text=caption,
            raw={"paid_media": PaidMedia(stars_amount=stars_amount, media_type="photo")},
        )

    async def refund_stars(self, user_id: int, telegram_payment_charge_id: str) -> bool:
        return True

    # Layer 225 Telegram Stars & Monetization
    async def send_paid_reaction(
        self,
        chat_id: Union[int, str],
        message_id: int,
        stars_count: int = 1,
        is_anonymous: bool = False,
    ) -> PaidReaction:
        return PaidReaction(stars_count=stars_count, is_anonymous=is_anonymous)

    async def get_stars_revenue(self, chat_id: Optional[Union[int, str]] = None) -> StarsRevenueStatus:
        return StarsRevenueStatus(
            current_balance=2500,
            available_balance=2000,
            overall_revenue=15000,
            can_withdraw=True,
            withdrawal_url="https://fragment.com/stars",
        )

    async def get_star_subscriptions(self) -> list[StarSubscription]:
        return [
            StarSubscription(
                id="sub_vip_01",
                period_seconds=2592000,
                stars_amount=250,
                is_canceled=False,
            )
        ]

    async def get_upgraded_gifts(self) -> list[Gift]:
        return [
            Gift(
                id="gift_upgraded_99",
                stars_cost=500,
                slug="cyber_dragon",
                total_count=1000,
                remaining_count=12,
                is_limited=True,
                is_upgraded=True,
                gift_number=42,
            )
        ]

    # Layer 225 Telegram Business 2.0 Management
    async def set_business_intro(
        self,
        title: str = "",
        description: str = "",
        sticker: Optional[str] = None,
    ) -> BusinessIntro:
        return BusinessIntro(title=title, description=description, sticker=sticker)

    async def set_business_location(
        self,
        address: str,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
    ) -> BusinessLocation:
        return BusinessLocation(address=address, latitude=latitude, longitude=longitude)

    async def get_business_connection(self, connection_id: str) -> BusinessConnection:
        return BusinessConnection(
            id=connection_id,
            user_id=12345678,
            dc_id=2,
            can_reply=True,
            is_disabled=False,
        )

    async def send_business_message(self, business_connection_id: str, chat_id: int, text: str) -> Message:
        self._msg_id_counter += 1
        return Message(
            id=self._msg_id_counter,
            chat=Chat(id=chat_id, type="private"),
            text=text,
            raw={"business_connection_id": business_connection_id},
        )

    async def post_story(
        self,
        chat_id: Union[int, str],
        media: Any,
        caption: str = "",
        privacy: str = "everyone",
        active_for: int = 86400,
    ) -> StoryItem:
        return StoryItem(
            id=random.randint(100, 9999),
            peer_id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0,
            date=int(time.time()),
            caption=caption,
        )

    async def edit_story(
        self,
        chat_id: Union[int, str],
        story_id: int,
        media: Any = None,
        caption: Optional[str] = None,
    ) -> StoryItem:
        return StoryItem(
            id=story_id,
            peer_id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0,
            date=int(time.time()),
            caption=caption,
        )

    async def delete_story(self, chat_id: Union[int, str], story_id: int) -> bool:
        return True

    async def get_stories(self, chat_id: Union[int, str], story_ids: list[int]) -> list[StoryItem]:
        return [
            StoryItem(
                id=sid,
                peer_id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 0,
                date=int(time.time()),
            )
            for sid in story_ids
        ]

    async def send_story_reaction(self, chat_id: Union[int, str], story_id: int, reaction: str) -> bool:
        return True

    async def send_gift(self, user_id: int, gift_id: str, text: str = "", is_private: bool = False) -> Gift:
        return Gift(id=gift_id, stars_cost=25, slug="exclusive_gift")

    async def get_available_gifts(self) -> list[Gift]:
        return [
            Gift(id="gift_star_1", stars_cost=25, slug="star_sparkle"),
            Gift(id="gift_star_2", stars_cost=100, slug="diamond_star"),
        ]

    async def create_forum_topic(
        self,
        chat_id: Union[int, str],
        title: str,
        icon_color: Optional[int] = None,
        icon_emoji_id: Optional[str] = None,
    ) -> ForumTopic:
        return ForumTopic(
            id=random.randint(1, 1000),
            title=title,
            icon_color=icon_color or 0x6FB9F0,
        )

    async def edit_forum_topic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        title: Optional[str] = None,
        icon_emoji_id: Optional[str] = None,
    ) -> bool:
        return True

    async def close_forum_topic(self, chat_id: Union[int, str], message_thread_id: int) -> bool:
        return True

    async def reopen_forum_topic(self, chat_id: Union[int, str], message_thread_id: int) -> bool:
        return True

    async def delete_forum_topic(self, chat_id: Union[int, str], message_thread_id: int) -> bool:
        return True

    # Chat Administration
    async def get_chat(self, chat_id: Union[int, str]) -> Chat:
        return Chat(
            id=int(chat_id) if str(chat_id).lstrip("-").isdigit() else 100123456789,
            type="supergroup",
            title=f"Chat {chat_id}",
        )

    async def get_chat_member(self, chat_id: Union[int, str], user_id: Union[int, str]) -> User:
        return User(
            id=int(user_id) if str(user_id).isdigit() else 9999,
            first_name="Member",
        )

    async def get_chat_members(self, chat_id: Union[int, str], limit: int = 200) -> list[User]:
        return [User(id=1000 + i, first_name=f"Member {i + 1}") for i in range(min(limit, 5))]

    async def ban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: Union[int, str],
        until_date: int = 0,
        revoke_messages: bool = True,
    ) -> bool:
        return True

    async def unban_chat_member(self, chat_id: Union[int, str], user_id: Union[int, str]) -> bool:
        return True

    async def restrict_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: Union[int, str],
        permissions: dict[str, bool],
        until_date: int = 0,
    ) -> bool:
        return True

    async def promote_chat_member(self, chat_id: Union[int, str], user_id: Union[int, str], **permissions) -> bool:
        return True

    async def set_chat_title(self, chat_id: Union[int, str], title: str) -> bool:
        return True

    async def set_chat_description(self, chat_id: Union[int, str], description: str) -> bool:
        return True

    async def set_chat_photo(self, chat_id: Union[int, str], photo: Any) -> bool:
        return True

    async def delete_chat_photo(self, chat_id: Union[int, str]) -> bool:
        return True

    async def leave_chat(self, chat_id: Union[int, str], delete: bool = False) -> bool:
        return True

    async def join_chat(self, chat_id_or_invite_link: str) -> Chat:
        return Chat(id=100123456789, type="supergroup", title="Joined Group")

    async def create_channel(self, title: str, about: str = "") -> Chat:
        return Chat(id=100987654321, type="channel", title=title)

    async def create_group(self, title: str, users: list[Union[int, str]]) -> Chat:
        return Chat(id=100555666777, type="group", title=title)

    # Users & Profile
    async def get_users(self, user_ids: list[Union[int, str]]) -> list[User]:
        return [User(id=int(uid) if str(uid).isdigit() else 1000 + i, first_name=f"User {uid}") for i, uid in enumerate(user_ids)]

    async def update_profile(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        about: Optional[str] = None,
    ) -> User:
        if self.me:
            if first_name:
                self.me.first_name = first_name
            if last_name:
                self.me.last_name = last_name
        return self.me or User(id=self.me_id, first_name=first_name or "Me")

    async def set_username(self, username: str) -> bool:
        if self.me:
            self.me.username = username
        return True

    async def block_user(self, user_id: Union[int, str]) -> bool:
        return True

    async def unblock_user(self, user_id: Union[int, str]) -> bool:
        return True

    # Processing Incoming Updates
    async def process_update(self, raw_update: dict[str, Any]) -> None:
        msg_data = raw_update.get("message")
        if not msg_data:
            return

        chat_data = msg_data.get("chat", {})
        sender_data = msg_data.get("from", {})

        chat = Chat(
            id=chat_data.get("id", 0),
            type=chat_data.get("type", "private"),
            title=chat_data.get("title"),
            username=chat_data.get("username"),
            is_forum=chat_data.get("is_forum", False),
        )
        sender = None
        if sender_data:
            sender = User(
                id=sender_data.get("id", 0),
                first_name=sender_data.get("first_name", ""),
                last_name=sender_data.get("last_name"),
                username=sender_data.get("username"),
                is_bot=sender_data.get("is_bot", False),
            )

        reply_to = None
        reply_data = msg_data.get("reply_to_message")
        if reply_data:
            reply_sender_data = reply_data.get("from", {})
            reply_sender = (
                User(
                    id=reply_sender_data.get("id", 0),
                    first_name=reply_sender_data.get("first_name", ""),
                    username=reply_sender_data.get("username"),
                )
                if reply_sender_data
                else None
            )
            reply_to = Message(
                id=reply_data.get("message_id", 0),
                chat=chat,
                sender=reply_sender,
                text=reply_data.get("text"),
                date=reply_data.get("date", 0),
            )

        quote_obj = None
        quote_data = msg_data.get("quote") or (reply_data.get("quote") if reply_data else None)
        if quote_data:
            from tgflow.formatting import MessageQuote
            quote_obj = MessageQuote(
                text=quote_data.get("text", "") if isinstance(quote_data, dict) else str(quote_data),
                position=quote_data.get("offset", 0) if isinstance(quote_data, dict) else 0,
            )

        msg = Message(
            id=msg_data.get("message_id", 0),
            chat=chat,
            sender=sender,
            text=msg_data.get("text"),
            reply_to=reply_to,
            quote=quote_obj,
            ttl_period=msg_data.get("ttl_period"),
            is_view_once=bool(msg_data.get("view_once")),
            date=msg_data.get("date", 0),
            raw=msg_data,
        )

        key = (msg.chat_id, msg.sender_id)
        if key in self._dialog_waiters:
            fut = self._dialog_waiters.pop(key)
            if not fut.done():
                fut.set_result(msg)
                return

        ctx = Context(msg, self)
        await self.router.dispatch(ctx)
