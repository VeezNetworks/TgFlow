import html
import re
from dataclasses import dataclass, field
from typing import Any, Optional, Union


# ==========================================================
# Rich Message Entities (Layer 225)
# ==========================================================
@dataclass(slots=True)
class MessageEntity:
    type: str
    offset: int
    length: int
    url: Optional[str] = None
    user_id: Optional[int] = None
    language: Optional[str] = None
    custom_emoji_id: Optional[str] = None
    is_collapsed: bool = False  # Expandable Blockquote support


# Formatting Helpers
def bold(text: str) -> str:
    return f"<b>{html.escape(text)}</b>"


def italic(text: str) -> str:
    return f"<i>{html.escape(text)}</i>"


def underline(text: str) -> str:
    return f"<u>{html.escape(text)}</u>"


def strikethrough(text: str) -> str:
    return f"<s>{html.escape(text)}</s>"


def spoiler(text: str) -> str:
    return f"<tg-spoiler>{html.escape(text)}</tg-spoiler>"


def code(text: str) -> str:
    return f"<code>{html.escape(text)}</code>"


def pre(text: str, language: str = "") -> str:
    if language:
        return f'<pre><code class="language-{language}">{html.escape(text)}</code></pre>'
    return f"<pre>{html.escape(text)}</pre>"


def custom_emoji(text: str, custom_emoji_id: Union[str, int] = "", emoji_id: Union[str, int] = "") -> str:
    """Rich Custom Animated Emoji (Layer 180–225)"""
    cid = custom_emoji_id or emoji_id
    return f'<tg-emoji emoji-id="{cid}">{html.escape(text)}</tg-emoji>'


def blockquote(text: str, expandable: bool = False) -> str:
    """
    Rich Blockquote or Collapsible/Expandable Blockquote (Layer 180–225).
    """
    tag = "blockquote"
    attr = ' expandable="true"' if expandable else ""
    return f"<{tag}{attr}>{html.escape(text)}</{tag}>"


# ==========================================================
# Rich Link Previews (Layer 190–225)
# ==========================================================
@dataclass(slots=True)
class LinkPreviewOptions:
    is_disabled: bool = False
    url: Optional[str] = None
    prefer_small_media: bool = False
    prefer_large_media: bool = False
    show_above_text: bool = False


# ==========================================================
# Rich Keyboards & Modern Buttons (Copy Text, Web App)
# ==========================================================
@dataclass(slots=True)
class InlineKeyboardButton:
    text: str
    url: Optional[str] = None
    callback_data: Optional[str] = None
    web_app_url: Optional[str] = None
    copy_text: Optional[str] = None  # 1-Click Copy Button (Layer 210+)
    switch_inline_query: Optional[str] = None


@dataclass(slots=True)
class InlineKeyboardMarkup:
    inline_keyboard: list[list[InlineKeyboardButton]] = field(default_factory=list)

    def add_row(self, *buttons: InlineKeyboardButton) -> "InlineKeyboardMarkup":
        self.inline_keyboard.append(list(buttons))
        return self


@dataclass(slots=True)
class KeyboardButton:
    text: str
    request_contact: bool = False
    request_location: bool = False


@dataclass(slots=True)
class ReplyKeyboardMarkup:
    keyboard: list[list[KeyboardButton]] = field(default_factory=list)
    resize_keyboard: bool = True
    one_time_keyboard: bool = False


# ==========================================================
# Rich Quotes (Layer 166–225)
# ==========================================================
@dataclass(slots=True)
class MessageQuote:
    text: str
    position: int = 0
    is_manual: bool = True
    entities: list[MessageEntity] = field(default_factory=list)
