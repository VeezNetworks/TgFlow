import html
import re
from typing import Any, Optional
from .tl import types as tl


def utf16_len(s: str) -> int:
    return len(s.encode("utf-16-le")) // 2


class MessageEntity:
    def __init__(
        self,
        type: str,
        offset: int,
        length: int,
        url: str | None = None,
        custom_emoji_id: int | None = None,
        language: str | None = None,
    ) -> None:
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

    @classmethod
    def from_tl(cls, obj: Any) -> "MessageEntity":
        cname = obj.__class__.__name__
        offset = getattr(obj, "offset", 0)
        length = getattr(obj, "length", 0)
        if cname == "MessageEntityBold":
            return cls("bold", offset, length)
        if cname == "MessageEntityItalic":
            return cls("italic", offset, length)
        if cname == "MessageEntityUnderline":
            return cls("underline", offset, length)
        if cname == "MessageEntityStrike":
            return cls("strike", offset, length)
        if cname == "MessageEntityCode":
            return cls("code", offset, length)
        if cname == "MessageEntityPre":
            return cls("pre", offset, length, language=getattr(obj, "language", None))
        if cname == "MessageEntitySpoiler":
            return cls("spoiler", offset, length)
        if cname == "MessageEntityBlockquote":
            return cls("blockquote", offset, length)
        if cname == "MessageEntityExpandableBlockquote":
            return cls("expandable_blockquote", offset, length)
        if cname == "MessageEntityCustomEmoji":
            return cls("custom_emoji", offset, length, custom_emoji_id=getattr(obj, "document_id", None))
        if cname == "MessageEntityTextUrl":
            return cls("text_url", offset, length, url=getattr(obj, "url", None))
        return cls("unknown", offset, length)


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
    plain_chunks: list[str] = []
    entities: list[MessageEntity] = []
    stack: list[tuple[str, int, dict[str, str]]] = []

    last_idx = 0
    for match in tag_pattern.finditer(text):
        chunk = html.unescape(text[last_idx:match.start()])
        plain_chunks.append(chunk)
        last_idx = match.end()

        is_closing = bool(match.group(1))
        tag_name = match.group(2).lower()
        raw_attrs = match.group(3)

        attrs: dict[str, str] = {}
        for attr_m in re.finditer(r'([a-zA-Z0-9_\-]+)(?:\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+)))?', raw_attrs):
            name = attr_m.group(1).lower()
            val = attr_m.group(2) or attr_m.group(3) or attr_m.group(4) or ""
            attrs[name] = val

        curr_utf16_offset = sum(utf16_len(c) for c in plain_chunks)

        if not is_closing:
            stack.append((tag_name, curr_utf16_offset, attrs))
        else:
            for i in range(len(stack) - 1, -1, -1):
                st_tag, st_offset, st_attrs = stack[i]
                if st_tag == tag_name:
                    stack.pop(i)
                    length = curr_utf16_offset - st_offset
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

    plain_chunks.append(html.unescape(text[last_idx:]))
    plain_text = "".join(plain_chunks)
    return plain_text, entities


MARKDOWN_RE = re.compile(
    r"(?P<pre>```(?P<lang>[a-zA-Z0-9_\-]+)?\n?(?P<pre_inner>[^`]+)```)"
    r"|(?P<code>`(?P<code_inner>[^`\n]+)`)"
    r"|(?P<spoiler>\|\|(?P<spoiler_inner>[^\|]+)\|\|)"
    r"|(?P<bold>\*\*(?P<bold_inner>[^\*]+)\*\*)"
    r"|(?P<italic>__(?P<italic_inner>[^_]+)__)"
    r"|(?P<strike>~~(?P<strike_inner>[^~]+)~~)"
    r"|(?P<expandable_blockquote>^\*\*> (?P<exp_bq_inner>[^\n]+)$)"
    r"|(?P<blockquote>^> (?P<bq_inner>[^\n]+)$)"
    r"|(?P<custom_emoji>!\[(?P<emoji_alt>[^\]]+)\]\(tg://emoji\?id=(?P<emoji_id>\d+)\))"
    r"|(?P<text_url>\[(?P<url_text>[^\]]+)\]\((?P<url>[^)]+)\))",
    re.MULTILINE
)


def parse_markdown(text: str) -> tuple[str, list[MessageEntity]]:
    plain_chunks: list[str] = []
    entities: list[MessageEntity] = []
    last_idx = 0
    curr_offset = 0

    for m in MARKDOWN_RE.finditer(text):
        start, end = m.span()
        chunk = text[last_idx:start]
        plain_chunks.append(chunk)
        curr_offset += utf16_len(chunk)
        last_idx = end

        g = m.groupdict()
        if g.get("bold"):
            inner = g["bold_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("bold", curr_offset, length))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("italic"):
            inner = g["italic_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("italic", curr_offset, length))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("spoiler"):
            inner = g["spoiler_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("spoiler", curr_offset, length))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("code"):
            inner = g["code_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("code", curr_offset, length))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("pre"):
            inner = g["pre_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("pre", curr_offset, length, language=g.get("lang")))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("strike"):
            inner = g["strike_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("strike", curr_offset, length))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("expandable_blockquote"):
            inner = g["exp_bq_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("expandable_blockquote", curr_offset, length))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("blockquote"):
            inner = g["bq_inner"]
            length = utf16_len(inner)
            entities.append(MessageEntity("blockquote", curr_offset, length))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("text_url"):
            inner = g["url_text"]
            length = utf16_len(inner)
            entities.append(MessageEntity("text_url", curr_offset, length, url=g.get("url")))
            plain_chunks.append(inner)
            curr_offset += length
        elif g.get("custom_emoji"):
            inner = g["emoji_alt"]
            length = utf16_len(inner)
            entities.append(MessageEntity("custom_emoji", curr_offset, length, custom_emoji_id=int(g["emoji_id"])))
            plain_chunks.append(inner)
            curr_offset += length

    rest = text[last_idx:]
    plain_chunks.append(rest)
    return "".join(plain_chunks), entities


def unparse_html(text: str, entities: list[MessageEntity] | list[Any]) -> str:
    if not entities:
        return html.escape(text)

    converted: list[MessageEntity] = []
    for e in entities:
        if isinstance(e, MessageEntity):
            converted.append(e)
        elif hasattr(e, "__class__"):
            converted.append(MessageEntity.from_tl(e))

    converted.sort(key=lambda e: (e.offset, -e.length))

    encoded = text.encode("utf-16-le")
    result: list[str] = []
    last_pos = 0

    for e in converted:
        start_byte = e.offset * 2
        end_byte = (e.offset + e.length) * 2
        if start_byte > last_pos:
            result.append(html.escape(encoded[last_pos:start_byte].decode("utf-16-le")))
        inner = html.escape(encoded[start_byte:end_byte].decode("utf-16-le"))

        if e.type == "bold":
            result.append(f"<b>{inner}</b>")
        elif e.type == "italic":
            result.append(f"<i>{inner}</i>")
        elif e.type == "underline":
            result.append(f"<u>{inner}</u>")
        elif e.type == "strike":
            result.append(f"<s>{inner}</s>")
        elif e.type == "code":
            result.append(f"<code>{inner}</code>")
        elif e.type == "pre":
            lang = f' class="language-{html.escape(e.language)}"' if e.language else ""
            result.append(f"<pre{lang}>{inner}</pre>")
        elif e.type == "spoiler":
            result.append(f"<tg-spoiler>{inner}</tg-spoiler>")
        elif e.type == "blockquote":
            result.append(f"<blockquote>{inner}</blockquote>")
        elif e.type == "expandable_blockquote":
            result.append(f"<blockquote expandable>{inner}</blockquote>")
        elif e.type == "text_url":
            result.append(f'<a href="{html.escape(e.url or "")}">{inner}</a>')
        elif e.type == "custom_emoji":
            result.append(f'<tg-emoji emoji-id="{e.custom_emoji_id}">{inner}</tg-emoji>')
        else:
            result.append(inner)
        last_pos = end_byte

    if last_pos < len(encoded):
        result.append(html.escape(encoded[last_pos:].decode("utf-16-le")))

    return "".join(result)


def unparse_markdown(text: str, entities: list[MessageEntity] | list[Any]) -> str:
    if not entities:
        return text

    converted: list[MessageEntity] = []
    for e in entities:
        if isinstance(e, MessageEntity):
            converted.append(e)
        elif hasattr(e, "__class__"):
            converted.append(MessageEntity.from_tl(e))

    converted.sort(key=lambda e: (e.offset, -e.length))

    encoded = text.encode("utf-16-le")
    result: list[str] = []
    last_pos = 0

    for e in converted:
        start_byte = e.offset * 2
        end_byte = (e.offset + e.length) * 2
        if start_byte > last_pos:
            result.append(encoded[last_pos:start_byte].decode("utf-16-le"))
        inner = encoded[start_byte:end_byte].decode("utf-16-le")

        if e.type == "bold":
            result.append(f"**{inner}**")
        elif e.type == "italic":
            result.append(f"__{inner}__")
        elif e.type == "strike":
            result.append(f"~~{inner}~~")
        elif e.type == "code":
            result.append(f"`{inner}`")
        elif e.type == "pre":
            lang = e.language or ""
            result.append(f"```{lang}\n{inner}```")
        elif e.type == "spoiler":
            result.append(f"||{inner}||")
        elif e.type == "blockquote":
            result.append(f"> {inner}")
        elif e.type == "expandable_blockquote":
            result.append(f"**> {inner}")
        elif e.type == "text_url":
            result.append(f"[{inner}]({e.url})")
        elif e.type == "custom_emoji":
            result.append(f"![{inner}](tg://emoji?id={e.custom_emoji_id})")
        else:
            result.append(inner)
        last_pos = end_byte

    if last_pos < len(encoded):
        result.append(encoded[last_pos:].decode("utf-16-le"))

    return "".join(result)
