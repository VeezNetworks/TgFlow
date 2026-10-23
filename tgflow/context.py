import asyncio
from typing import Any, Optional, Union
from tgflow.tl.types import Chat, Message, User


class TargetActionProxy:
    def __init__(self, target: Any, client: Any, chat_id: int):
        self.target = target
        self.client = client
        self.chat_id = chat_id

    @property
    def id(self) -> int:
        if isinstance(self.target, User):
            return self.target.id
        if isinstance(self.target, int):
            return self.target
        if isinstance(self.target, str) and self.target.isdigit():
            return int(self.target)
        return 0

    @property
    def name(self) -> str:
        if isinstance(self.target, User):
            return self.target.full_name
        return str(self.target)

    async def ban(self, duration: int = 0) -> bool:
        return await self.client.ban_chat_member(self.chat_id, self.id, until_date=duration)

    async def unban(self) -> bool:
        return await self.client.unban_chat_member(self.chat_id, self.id)

    async def kick(self) -> bool:
        await self.client.ban_chat_member(self.chat_id, self.id, until_date=0)
        return await self.client.unban_chat_member(self.chat_id, self.id)

    async def mute(self, duration: int = 60) -> bool:
        return await self.client.restrict_chat_member(
            self.chat_id,
            self.id,
            permissions={"can_send_messages": False},
            until_date=duration,
        )

    async def promote(self, **permissions) -> bool:
        return await self.client.promote_chat_member(self.chat_id, self.id, **permissions)


class Context:
    def __init__(self, message: Message, client: Any):
        self.message = message
        self.client = client

    @property
    def chat(self) -> Chat:
        return self.message.chat

    @property
    def chat_id(self) -> int:
        return self.message.chat.id

    @property
    def sender(self) -> Optional[User]:
        return self.message.sender

    @property
    def sender_id(self) -> Optional[int]:
        return self.message.sender_id

    @property
    def text(self) -> Optional[str]:
        return self.message.text

    @property
    def reply_to(self) -> Optional[Message]:
        return self.message.reply_to

    @property
    def topic_id(self) -> Optional[int]:
        return self.message.raw.get("message_thread_id")

    @property
    def quote(self) -> Optional[str]:
        """Extracted quote text if this message is quoting another."""
        return self.message.quote.text if self.message.quote else None

    @property
    def is_ephemeral(self) -> bool:
        """True if the message has an auto-delete TTL timer or is view-once."""
        return self.message.is_ephemeral

    # Reply shortcuts
    async def reply(self, text: str, **kwargs) -> Any:
        return await self.client.send_message(
            self.chat_id,
            text,
            reply_to_message_id=self.message.id,
            **kwargs,
        )

    async def reply_quote(self, text: str, quote_text: Optional[str] = None, **kwargs) -> Any:
        """Reply quoting a specific sentence or snippet of the user's message."""
        selected_quote = quote_text or (self.text[:128] if self.text else "")
        return await self.client.send_message(
            self.chat_id,
            text,
            reply_to_message_id=self.message.id,
            quote_text=selected_quote,
            **kwargs,
        )

    async def reply_ephemeral(self, text: str, ttl: int = 30, **kwargs) -> Any:
        """Send a self-destructing/auto-delete message with a TTL period in seconds."""
        return await self.client.send_message(
            self.chat_id,
            text,
            reply_to_message_id=self.message.id,
            ttl_period=ttl,
            **kwargs,
        )

    async def reply_rich(
        self,
        text: str,
        reply_markup: Any = None,
        link_preview_options: Any = None,
        **kwargs,
    ) -> Any:
        """Send rich message with modern keyboards (e.g. 1-click copy text) and link preview options."""
        return await self.client.send_message(
            self.chat_id,
            text,
            reply_to_message_id=self.message.id,
            reply_markup=reply_markup,
            link_preview_options=link_preview_options,
            **kwargs,
        )

    async def reply_text(self, text: str, **kwargs) -> Any:
        return await self.reply(text, **kwargs)

    async def reply_photo(self, photo: Any, caption: Optional[str] = None, **kwargs) -> Any:
        return await self.client.send_photo(
            self.chat_id,
            photo,
            caption=caption,
            reply_to_message_id=self.message.id,
            **kwargs,
        )

    async def reply_document(self, document: Any, caption: Optional[str] = None, **kwargs) -> Any:
        return await self.client.send_document(
            self.chat_id,
            document,
            caption=caption,
            reply_to_message_id=self.message.id,
            **kwargs,
        )

    async def reply_video(self, video: Any, caption: Optional[str] = None, **kwargs) -> Any:
        return await self.client.send_video(
            self.chat_id,
            video,
            caption=caption,
            reply_to_message_id=self.message.id,
            **kwargs,
        )

    async def reply_in_topic(self, text: str, **kwargs) -> Any:
        thread_id = self.topic_id
        return await self.client.send_message(
            self.chat_id,
            text,
            message_thread_id=thread_id,
            **kwargs,
        )

    # Message manipulations
    async def edit(self, text: str, **kwargs) -> Any:
        return await self.client.edit_message_text(
            self.chat_id,
            self.message.id,
            text,
            **kwargs,
        )

    async def delete(self) -> bool:
        return await self.client.delete_messages(self.chat_id, [self.message.id])

    async def forward(self, to_chat_id: int, **kwargs) -> Any:
        return await self.client.forward_messages(
            chat_id=to_chat_id,
            from_chat_id=self.chat_id,
            message_ids=[self.message.id],
            **kwargs,
        )

    async def pin(self, disable_notification: bool = False) -> bool:
        return await self.client.pin_chat_message(
            self.chat_id,
            self.message.id,
            disable_notification=disable_notification,
        )

    async def unpin(self) -> bool:
        return await self.client.unpin_chat_message(self.chat_id, self.message.id)

    # Interactive flow dialogues
    async def ask(self, prompt: str, timeout: int = 60) -> Message:
        await self.reply(prompt)
        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        key = (self.chat_id, self.sender_id)
        self.client._dialog_waiters[key] = fut

        try:
            return await asyncio.wait_for(fut, timeout=timeout)
        except asyncio.TimeoutError:
            self.client._dialog_waiters.pop(key, None)
            raise TimeoutError("User response timed out.")

    async def choose(self, prompt: str, options: list[str], timeout: int = 60) -> str:
        buttons_text = "\n".join(f"{i + 1}. {opt}" for i, opt in enumerate(options))
        full_prompt = f"{prompt}\n\n{buttons_text}\n\nReply with the number of your choice."
        response_msg = await self.ask(full_prompt, timeout=timeout)

        selected_text = (response_msg.text or "").strip()
        if selected_text.isdigit():
            idx = int(selected_text) - 1
            if 0 <= idx < len(options):
                return options[idx]

        for opt in options:
            if selected_text.lower() == opt.lower():
                return opt

        return selected_text

    async def confirm(self, prompt: str, timeout: int = 60) -> bool:
        res = await self.choose(prompt, options=["Yes", "No"], timeout=timeout)
        return res.lower() in ("yes", "y", "1", "true")

    # Member actions
    async def ban(self, user_id: Optional[int] = None, duration: int = 0) -> bool:
        target_id = user_id or self.sender_id
        if not target_id:
            return False
        return await self.client.ban_chat_member(self.chat_id, target_id, until_date=duration)

    async def unban(self, user_id: Optional[int] = None) -> bool:
        target_id = user_id or self.sender_id
        if not target_id:
            return False
        return await self.client.unban_chat_member(self.chat_id, target_id)

    async def kick(self, user_id: Optional[int] = None) -> bool:
        target_id = user_id or self.sender_id
        if not target_id:
            return False
        await self.client.ban_chat_member(self.chat_id, target_id, until_date=0)
        return await self.client.unban_chat_member(self.chat_id, target_id)

    async def mute(self, user_id: Optional[int] = None, duration: int = 60) -> bool:
        target_id = user_id or self.sender_id
        if not target_id:
            return False
        return await self.client.restrict_chat_member(
            self.chat_id,
            target_id,
            permissions={"can_send_messages": False},
            until_date=duration,
        )

    # Stars
    async def send_stars(self, amount: int, purpose: str = "") -> dict[str, Any]:
        return await self.client.send_stars(self.chat_id, amount=amount, purpose=purpose)

    def target(self, user_or_id: Any) -> TargetActionProxy:
        return TargetActionProxy(user_or_id, self.client, self.chat_id)
