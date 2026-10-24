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
def bold(text: Any) -> str:
    return f"<b>{html.escape(str(text or ''))}</b>"


def italic(text: Any) -> str:
    return f"<i>{html.escape(str(text or ''))}</i>"


def underline(text: Any) -> str:
    return f"<u>{html.escape(str(text or ''))}</u>"


def strikethrough(text: Any) -> str:
    return f"<s>{html.escape(str(text or ''))}</s>"


def spoiler(text: Any) -> str:
    return f"<tg-spoiler>{html.escape(str(text or ''))}</tg-spoiler>"


def code(text: Any) -> str:
    return f"<code>{html.escape(str(text or ''))}</code>"


def pre(text: Any, language: str = "") -> str:
    content = html.escape(str(text or ''))
    if language:
        return f'<pre><code class="language-{language}">{content}</code></pre>'
    return f"<pre>{content}</pre>"


def custom_emoji(text: Any, custom_emoji_id: Union[str, int] = "", emoji_id: Union[str, int] = "") -> str:
    """Rich Custom Animated Emoji (Layer 180–225)"""
    cid = custom_emoji_id or emoji_id
    return f'<tg-emoji emoji-id="{cid}">{html.escape(str(text or ""))}</tg-emoji>'


def blockquote(text: Any, expandable: bool = False) -> str:
    """
    Rich Blockquote or Collapsible/Expandable Blockquote (Layer 180–225).
    """
    tag = "blockquote"
    attr = ' expandable="true"' if expandable else ""
    return f"<{tag}{attr}>{html.escape(str(text or ''))}</{tag}>"


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
