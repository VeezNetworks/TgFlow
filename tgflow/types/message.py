import asyncio
from typing import Any, Optional
from .user import User
from .chat import Chat
from .media import Photo, Video, Audio, Document, Voice, Animation, Sticker


class Message:
    def __init__(
        self,
        id: int,
        date: int = 0,
        chat: Optional[Chat] = None,
        from_user: Optional[User] = None,
        text: str = "",
        entities: list[Any] | None = None,
        reply_to_message: Optional["Message"] = None,
        reply_to_message_id: int | None = None,
        quote: str | None = None,
        photo: Optional[Photo] = None,
        video: Optional[Video] = None,
        audio: Optional[Audio] = None,
        document: Optional[Document] = None,
        voice: Optional[Voice] = None,
        animation: Optional[Animation] = None,
        sticker: Optional[Sticker] = None,
        caption: str | None = None,
        media: Any = None,
        client: Any = None,
    ) -> None:
        self.id = id
        self.date = date
        self.chat = chat or Chat(id=0)
        self.from_user = from_user
        self.text = text
        self.entities = entities or []
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.quote = quote
        self.photo = photo
        self.video = video
        self.audio = audio
        self.document = document
        self.voice = voice
        self.animation = animation
        self.sticker = sticker
        self.caption = caption
        self.media = media
        self._client = client
        self.command: list[str] | None = None
        self.matches: list[Any] | None = None

    async def reply(self, text: str, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.send_message(
            chat_id=self.chat.id,
            text=text,
            reply_to_message_id=self.id,
            **kwargs,
        )

    async def reply_quote(self, text: str, quote: str, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.send_message(
            chat_id=self.chat.id,
            text=text,
            reply_to_message_id=self.id,
            quote=quote,
            **kwargs,
        )

    async def reply_ephemeral(self, text: str, ttl_seconds: int = 10, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        sent = await self._client.send_message(
            chat_id=self.chat.id,
            text=text,
            reply_to_message_id=self.id,
            **kwargs,
        )

        async def _auto_delete() -> None:
            await asyncio.sleep(ttl_seconds)
            try:
                await sent.delete()
            except Exception:
                pass

        asyncio.create_task(_auto_delete())
        return sent

    async def reply_photo(self, photo: Any, caption: str | None = None, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.send_photo(
            chat_id=self.chat.id,
            photo=photo,
            caption=caption,
            reply_to_message_id=self.id,
            **kwargs,
        )

    async def reply_document(self, document: Any, caption: str | None = None, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.send_document(
            chat_id=self.chat.id,
            document=document,
            caption=caption,
            reply_to_message_id=self.id,
            **kwargs,
        )

    async def edit(self, text: str, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.edit_message_text(
            chat_id=self.chat.id,
            message_id=self.id,
            text=text,
            **kwargs,
        )

    async def edit_caption(self, caption: str, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.edit_message_caption(
            chat_id=self.chat.id,
            message_id=self.id,
            caption=caption,
            **kwargs,
        )

    async def delete(self, revoke: bool = True) -> bool:
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.delete_messages(
            chat_id=self.chat.id,
            message_ids=[self.id],
            revoke=revoke,
        )

    async def react(self, emoji: str) -> bool:
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.send_reaction(
            chat_id=self.chat.id,
            message_id=self.id,
            emoji=emoji,
        )

    async def forward(self, chat_id: int | str) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.forward_messages(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_ids=[self.id],
        )

    async def copy(self, chat_id: int | str, caption: str | None = None, **kwargs: Any) -> "Message":
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.copy_message(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_id=self.id,
            caption=caption,
            **kwargs,
        )

    async def pin(self, disable_notification: bool = False) -> bool:
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.pin_chat_message(
            chat_id=self.chat.id,
            message_id=self.id,
            disable_notification=disable_notification,
        )

    async def unpin(self) -> bool:
        if not self._client:
            raise RuntimeError("Client instance not bound to message")
        return await self._client.unpin_chat_message(
            chat_id=self.chat.id,
            message_id=self.id,
        )
