import html
import re
from typing import Any
from .tl import types as tl


class MessageEntity:
    def __init__(self, type: str, offset: int, length: int, url: str | None = None, custom_emoji_id: int | None = None, language: str | None = None) -> None:
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.custom_emoji_id = custom_emoji_id
        self.language = language

    def to_tl(self) -> Any:
        if self.type == "bold":
            return tl.MessageEntityBold(offset=self.offset, length=self.length)
        if self.type == "italic":
            return tl.MessageEntityItalic(offset=self.offset, length=self.length)
        if self.type == "underline":
            return tl.MessageEntityUnderline(offset=self.offset, length=self.length)
        if self.type == "strike":
            return tl.MessageEntityStrike(offset=self.offset, length=self.length)
        if self.type == "code":
            return tl.MessageEntityCode(offset=self.offset, length=self.length)
        if self.type == "pre":
            return tl.MessageEntityPre(offset=self.offset, length=self.length, language=self.language or "")
        if self.type == "spoiler":
            return tl.MessageEntitySpoiler(offset=self.offset, length=self.length)
        if self.type == "blockquote":
            return tl.MessageEntityBlockquote(offset=self.offset, length=self.length)
        if self.type == "expandable_blockquote":
            return tl.MessageEntityExpandableBlockquote(offset=self.offset, length=self.length)
        if self.type == "custom_emoji":
            return tl.MessageEntityCustomEmoji(offset=self.offset, length=self.length, document_id=self.custom_emoji_id or 0)
        if self.type == "text_url":
            return tl.MessageEntityTextUrl(offset=self.offset, length=self.length, url=self.url or "")
        return tl.MessageEntityUnknown(offset=self.offset, length=self.length)


def bold(text: str) -> str:
    return f"<b>{html.escape(str(text))}</b>"


def italic(text: str) -> str:
    return f"<i>{html.escape(str(text))}</i>"


def underline(text: str) -> str:
    return f"<u>{html.escape(str(text))}</u>"


def strike(text: str) -> str:
    return f"<s>{html.escape(str(text))}</s>"


def spoiler(text: str) -> str:
    return f"<tg-spoiler>{html.escape(str(text))}</tg-spoiler>"


def code(text: str) -> str:
    return f"<code>{html.escape(str(text))}</code>"


def pre(text: str, language: str = "") -> str:
    lang_attr = f' class="language-{html.escape(language)}"' if language else ""
    return f"<pre{lang_attr}>{html.escape(str(text))}</pre>"


def blockquote(text: str) -> str:
    return f"<blockquote>{html.escape(str(text))}</blockquote>"


def expandable_blockquote(text: str) -> str:
    return f"<blockquote expandable>{html.escape(str(text))}</blockquote>"


def link(text: str, url: str) -> str:
    return f'<a href="{html.escape(url)}">{html.escape(str(text))}</a>'


def custom_emoji(emoji: str, emoji_id: int) -> str:
    return f'<tg-emoji emoji-id="{emoji_id}">{html.escape(emoji)}</tg-emoji>'


def parse_html(text: str) -> tuple[str, list[MessageEntity]]:
    tag_pattern = re.compile(r"<\s*(/)?\s*([a-zA-Z0-9_\-]+)([^>]*)>", re.DOTALL)
    plain_chars: list[str] = []
    entities: list[MessageEntity] = []
    stack: list[tuple[str, int, dict[str, str]]] = []

    last_idx = 0
    for match in tag_pattern.finditer(text):
        chunk = text[last_idx:match.start()]
        plain_chars.append(chunk)
        last_idx = match.end()

        is_closing = bool(match.group(1))
        tag_name = match.group(2).lower()
        raw_attrs = match.group(3)

        attrs: dict[str, str] = {}
        for attr_m in re.finditer(r'([a-zA-Z0-9_\-]+)(?:\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+)))?', raw_attrs):
            name = attr_m.group(1).lower()
            val = attr_m.group(2) or attr_m.group(3) or attr_m.group(4) or ""
            attrs[name] = val

        curr_offset = sum(len(c) for c in plain_chars)

        if not is_closing:
            stack.append((tag_name, curr_offset, attrs))
        else:
            for i in range(len(stack) - 1, -1, -1):
                st_tag, st_offset, st_attrs = stack[i]
                if st_tag == tag_name:
                    stack.pop(i)
                    length = curr_offset - st_offset
                    if length > 0:
                        if tag_name in ("b", "strong"):
                            entities.append(MessageEntity("bold", st_offset, length))
                        elif tag_name in ("i", "em"):
                            entities.append(MessageEntity("italic", st_offset, length))
                        elif tag_name in ("u", "ins"):
                            entities.append(MessageEntity("underline", st_offset, length))
                        elif tag_name in ("s", "strike", "del"):
                            entities.append(MessageEntity("strike", st_offset, length))
                        elif tag_name == "code":
                            entities.append(MessageEntity("code", st_offset, length))
                        elif tag_name == "pre":
                            entities.append(MessageEntity("pre", st_offset, length, language=st_attrs.get("language")))
                        elif tag_name == "tg-spoiler":
                            entities.append(MessageEntity("spoiler", st_offset, length))
                        elif tag_name == "blockquote":
                            if "expandable" in st_attrs or st_attrs.get("class") == "expandable":
                                entities.append(MessageEntity("expandable_blockquote", st_offset, length))
                            else:
                                entities.append(MessageEntity("blockquote", st_offset, length))
                        elif tag_name == "a":
                            entities.append(MessageEntity("text_url", st_offset, length, url=st_attrs.get("href")))
                        elif tag_name == "tg-emoji":
                            eid = int(st_attrs.get("emoji-id", 0)) if st_attrs.get("emoji-id") else None
                            entities.append(MessageEntity("custom_emoji", st_offset, length, custom_emoji_id=eid))
                    break

    plain_chars.append(text[last_idx:])
    plain_text = html.unescape("".join(plain_chars))
    return plain_text, entities


def parse_markdown(text: str) -> tuple[str, list[MessageEntity]]:
    return parse_html(text)
