from typing import Any, Optional
from .user import User
from .message import Message


class ReactionTypeEmoji:
    def __init__(self, emoji: str) -> None:
        self.type = "emoji"
        self.emoji = emoji


class ReactionTypeCustomEmoji:
    def __init__(self, custom_emoji_id: str) -> None:
        self.type = "custom_emoji"
        self.custom_emoji_id = custom_emoji_id


class Reaction:
    def __init__(self, type: ReactionTypeEmoji | ReactionTypeCustomEmoji | str) -> None:
        if isinstance(type, str):
            self.type = ReactionTypeEmoji(type)
        else:
            self.type = type


class CallbackQuery:
    def __init__(
        self,
        id: str,
        from_user: User,
        message: Optional[Message] = None,
        data: str = "",
        chat_instance: str = "",
        client: Any = None,
    ) -> None:
        self.id = id
        self.from_user = from_user
        self.message = message
        self.data = data
        self.chat_instance = chat_instance
        self._client = client
        self.matches: list[Any] | None = None

    async def answer(self, text: str = "", show_alert: bool = False, url: str | None = None, cache_time: int = 0) -> bool:
        if not self._client:
            raise RuntimeError("Client not bound")
        return await self._client.answer_callback_query(
            callback_query_id=self.id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )

    async def edit_message_text(self, text: str, **kwargs: Any) -> Optional[Message]:
        if not self.message:
            raise RuntimeError("Callback query has no associated message")
        return await self.message.edit(text, **kwargs)


class InlineQuery:
    def __init__(
        self,
        id: str,
        from_user: User,
        query: str = "",
        offset: str = "",
        client: Any = None,
    ) -> None:
        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self._client = client
        self.matches: list[Any] | None = None

    async def answer(self, results: list[Any], cache_time: int = 300, is_personal: bool = False, next_offset: str = "") -> bool:
        if not self._client:
            raise RuntimeError("Client not bound")
        return await self._client.answer_inline_query(
            inline_query_id=self.id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
        )


class ChosenInlineResult:
    def __init__(self, result_id: str, from_user: User, query: str, inline_message_id: str | None = None) -> None:
        self.result_id = result_id
        self.from_user = from_user
        self.query = query
        self.inline_message_id = inline_message_id
