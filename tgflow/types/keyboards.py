from typing import Any, Optional
from ..tl import types as tl


class InlineKeyboardButton:
    def __init__(
        self,
        text: str,
        callback_data: str | None = None,
        url: str | None = None,
        switch_inline_query: str | None = None,
        switch_inline_query_current_chat: str | None = None,
        copy_text: str | None = None,
        web_app: Any = None,
        user_id: int | None = None,
    ) -> None:
        self.text = text
        self.callback_data = callback_data
        self.url = url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.copy_text = copy_text
        self.web_app = web_app
        self.user_id = user_id

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
        if self.web_app is not None:
            data["web_app"] = {"url": self.web_app if isinstance(self.web_app, str) else getattr(self.web_app, "url", "")}
        if self.user_id is not None:
            data["user_id"] = self.user_id
        return data

    def to_tl(self) -> Any:
        if self.callback_data is not None:
            cb_bytes = self.callback_data.encode("utf-8") if isinstance(self.callback_data, str) else bytes(self.callback_data)
            return tl.KeyboardButtonCallback(text=self.text, data=cb_bytes)
        if self.url is not None:
            return tl.KeyboardButtonUrl(text=self.text, url=self.url)
        if self.copy_text is not None:
            return tl.KeyboardButtonCopyText(text=self.text, copy_text=self.copy_text)
        if self.user_id is not None:
            return tl.KeyboardButtonUserProfile(text=self.text, user_id=self.user_id)
        if self.web_app is not None:
            url_str = self.web_app if isinstance(self.web_app, str) else getattr(self.web_app, "url", "")
            return tl.KeyboardButtonWebView(text=self.text, url=url_str)
        if self.switch_inline_query is not None:
            return tl.KeyboardButtonSwitchInline(text=self.text, query=self.switch_inline_query, same_peer=False)
        if self.switch_inline_query_current_chat is not None:
            return tl.KeyboardButtonSwitchInline(text=self.text, query=self.switch_inline_query_current_chat, same_peer=True)
        return tl.KeyboardButton(text=self.text)


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

    def to_tl(self) -> Any:
        tl_rows = []
        for row in self.inline_keyboard:
            buttons = [b.to_tl() if hasattr(b, "to_tl") else b for b in row]
            tl_rows.append(tl.KeyboardButtonRow(buttons=buttons))
        return tl.ReplyInlineMarkup(rows=tl_rows)


class KeyboardButton:
    def __init__(
        self,
        text: str,
        request_contact: bool = False,
        request_location: bool = False,
        request_poll: Any = None,
        request_users: Any = None,
        request_chat: Any = None,
        web_app: Any = None,
    ) -> None:
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.request_users = request_users
        self.request_chat = request_chat
        self.web_app = web_app

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"text": self.text}
        if self.request_contact:
            data["request_contact"] = True
        if self.request_location:
            data["request_location"] = True
        if self.request_poll:
            data["request_poll"] = self.request_poll
        if self.request_users:
            data["request_users"] = self.request_users
        if self.request_chat:
            data["request_chat"] = self.request_chat
        if self.web_app:
            data["web_app"] = self.web_app
        return data

    def to_tl(self) -> Any:
        if self.web_app:
            url_str = self.web_app if isinstance(self.web_app, str) else getattr(self.web_app, "url", "")
            return tl.KeyboardButtonWebView(text=self.text, url=url_str)
        return tl.KeyboardButton(text=self.text)


class ReplyKeyboardMarkup:
    def __init__(
        self,
        keyboard: list[list[KeyboardButton]],
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
        selective: bool = False,
        is_persistent: bool = False,
        input_field_placeholder: str | None = None,
    ) -> None:
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.is_persistent = is_persistent
        self.input_field_placeholder = input_field_placeholder

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
            "input_field_placeholder": self.input_field_placeholder,
        }

    def to_tl(self) -> Any:
        tl_rows = []
        for row in self.keyboard:
            buttons = [b.to_tl() if hasattr(b, "to_tl") else b for b in row]
            tl_rows.append(tl.KeyboardButtonRow(buttons=buttons))
        return tl.ReplyKeyboardMarkup(
            rows=tl_rows,
            resize=self.resize_keyboard,
            single_use=self.one_time_keyboard,
            selective=self.selective,
            persistent=self.is_persistent,
            placeholder=self.input_field_placeholder,
        )


class ReplyKeyboardRemove:
    def __init__(self, selective: bool = False) -> None:
        self.remove_keyboard = True
        self.selective = selective

    def to_dict(self) -> dict[str, Any]:
        return {"remove_keyboard": True, "selective": self.selective}

    def to_tl(self) -> Any:
        return tl.ReplyKeyboardHide(selective=self.selective)


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

    def to_tl(self) -> Any:
        return tl.ReplyKeyboardForceReply(
            selective=self.selective,
            placeholder=self.input_field_placeholder,
        )


class FlowButton:
    @staticmethod
    def data(text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)

    @staticmethod
    def callback(text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)

    @staticmethod
    def url(text: str, url: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, url=url)

    @staticmethod
    def web_app(text: str, url: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, web_app=url)

    @staticmethod
    def copy(text: str, copy_text: str | None = None, **kwargs: Any) -> InlineKeyboardButton:
        c_text = copy_text or kwargs.get("text") or text
        return InlineKeyboardButton(text=text, copy_text=c_text)

    @staticmethod
    def user(text: str, user_id: int) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, user_id=user_id)

    @staticmethod
    def switch_inline(text: str, query: str = "", current_chat: bool = False) -> InlineKeyboardButton:
        if current_chat:
            return InlineKeyboardButton(text=text, switch_inline_query_current_chat=query)
        return InlineKeyboardButton(text=text, switch_inline_query=query)

    @staticmethod
    def buy(text: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data="buy")

    @staticmethod
    def text(text: str, callback_data: str | None = None) -> Any:
        if callback_data is not None:
            return InlineKeyboardButton(text=text, callback_data=callback_data)
        return KeyboardButton(text=text)

    @staticmethod
    def contact(text: str) -> KeyboardButton:
        return KeyboardButton(text=text, request_contact=True)

    @staticmethod
    def location(text: str) -> KeyboardButton:
        return KeyboardButton(text=text, request_location=True)

    @staticmethod
    def poll(text: str, poll_type: str | None = None) -> KeyboardButton:
        return KeyboardButton(text=text, request_poll={"type": poll_type} if poll_type else {})


class FlowMarkup:
    def __init__(self, rows: list[list[Any]] | None = None) -> None:
        self.rows: list[list[Any]] = [list(r) for r in rows] if rows else []

    def row(self, *buttons: Any) -> Any:
        if isinstance(self, FlowMarkup):
            self.rows.append(list(buttons))
            return self
        return [self] + list(buttons)

    def add(self, *buttons: Any) -> "FlowMarkup":
        if not self.rows:
            self.rows.append([])
        self.rows[-1].extend(buttons)
        return self

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=self.rows)

    @classmethod
    def inline(cls, rows: list[list[InlineKeyboardButton]]) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=rows)

    @classmethod
    def grid(cls, buttons: list[InlineKeyboardButton], cols: int = 2) -> InlineKeyboardMarkup:
        rows = [buttons[i : i + cols] for i in range(0, len(buttons), cols)]
        return InlineKeyboardMarkup(inline_keyboard=rows)

    @staticmethod
    def create_row(*buttons: InlineKeyboardButton) -> list[InlineKeyboardButton]:
        return list(buttons)

    @classmethod
    def reply(
        cls,
        rows: list[list[KeyboardButton]],
        resize: bool = True,
        persistent: bool = False,
        placeholder: str | None = None,
        one_time: bool = False,
    ) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=rows,
            resize_keyboard=resize,
            is_persistent=persistent,
            input_field_placeholder=placeholder,
            one_time_keyboard=one_time,
        )

    @classmethod
    def remove(cls, selective: bool = False) -> ReplyKeyboardRemove:
        return ReplyKeyboardRemove(selective=selective)

    @classmethod
    def force_reply(cls, placeholder: str | None = None, selective: bool = False) -> ForceReply:
        return ForceReply(selective=selective, input_field_placeholder=placeholder)
