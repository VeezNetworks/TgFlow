from typing import Any, Optional


class InlineKeyboardButton:
    def __init__(
        self,
        text: str,
        callback_data: str | None = None,
        url: str | None = None,
        switch_inline_query: str | None = None,
        switch_inline_query_current_chat: str | None = None,
        copy_text: str | None = None,
    ) -> None:
        self.text = text
        self.callback_data = callback_data
        self.url = url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.copy_text = copy_text

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"text": self.text}
        if self.callback_data is not None:
            data["callback_data"] = self.callback_data
        if self.url is not None:
            data["url"] = self.url
        if self.switch_inline_query is not None:
            data["switch_inline_query"] = self.switch_inline_query
        if self.switch_inline_query_current_chat is not None:
            data["switch_inline_query_current_chat"] = self.switch_inline_query_current_chat
        if self.copy_text is not None:
            data["copy_text"] = {"text": self.copy_text}
        return data


class InlineKeyboardMarkup:
    def __init__(self, inline_keyboard: list[list[InlineKeyboardButton]]) -> None:
        self.inline_keyboard = inline_keyboard

    def to_dict(self) -> dict[str, Any]:
        return {
            "inline_keyboard": [
                [btn.to_dict() if isinstance(btn, InlineKeyboardButton) else btn for btn in row]
                for row in self.inline_keyboard
            ]
        }


class KeyboardButton:
    def __init__(
        self,
        text: str,
        request_contact: bool = False,
        request_location: bool = False,
        request_poll: Any = None,
    ) -> None:
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"text": self.text}
        if self.request_contact:
            data["request_contact"] = True
        if self.request_location:
            data["request_location"] = True
        if self.request_poll:
            data["request_poll"] = self.request_poll
        return data


class ReplyKeyboardMarkup:
    def __init__(
        self,
        keyboard: list[list[KeyboardButton]],
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
        selective: bool = False,
        is_persistent: bool = False,
    ) -> None:
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.is_persistent = is_persistent

    def to_dict(self) -> dict[str, Any]:
        return {
            "keyboard": [
                [btn.to_dict() if isinstance(btn, KeyboardButton) else btn for btn in row]
                for row in self.keyboard
            ],
            "resize_keyboard": self.resize_keyboard,
            "one_time_keyboard": self.one_time_keyboard,
            "selective": self.selective,
            "is_persistent": self.is_persistent,
        }


class ReplyKeyboardRemove:
    def __init__(self, selective: bool = False) -> None:
        self.remove_keyboard = True
        self.selective = selective

    def to_dict(self) -> dict[str, Any]:
        return {"remove_keyboard": True, "selective": self.selective}


class ForceReply:
    def __init__(self, selective: bool = False, input_field_placeholder: str | None = None) -> None:
        self.force_reply = True
        self.selective = selective
        self.input_field_placeholder = input_field_placeholder

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"force_reply": True, "selective": self.selective}
        if self.input_field_placeholder:
            data["input_field_placeholder"] = self.input_field_placeholder
        return data
