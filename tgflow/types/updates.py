from typing import Any, Optional
from .user import User
from .message import Message


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

    async def answer(self, text: str = "", show_alert: bool = False, cache_time: int = 0) -> bool:
        if not self._client:
            raise RuntimeError("Client not bound")
        return await self._client.answer_callback_query(
            callback_query_id=self.id,
            text=text,
            show_alert=show_alert,
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

    async def answer(self, results: list[Any], cache_time: int = 300, is_personal: bool = False) -> bool:
        if not self._client:
            raise RuntimeError("Client not bound")
        return await self._client.answer_inline_query(
            inline_query_id=self.id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
        )
