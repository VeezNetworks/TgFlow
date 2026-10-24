from typing import Any
from .tl import types as tl
from .formatting import utf16_len


class RichText:
    def __init__(self, initial_text: str = "") -> None:
        self._text_parts: list[str] = []
        self._entities: list[Any] = []
        self._current_offset: int = 0
        if initial_text:
            self.text(initial_text)

    def _append(self, segment: str, entity: Any = None) -> "RichText":
        length = utf16_len(segment)
        if entity is not None:
            entity.offset = self._current_offset
            entity.length = length
            self._entities.append(entity)
        self._text_parts.append(segment)
        self._current_offset += length
        return self

    def text(self, text: str) -> "RichText":
        return self._append(text)

    def line(self, text: str = "") -> "RichText":
        return self._append(text + "\n")

    def bold(self, text: str) -> "RichText":
        return self._append(text, tl.MessageEntityBold(offset=0, length=0))

    def italic(self, text: str) -> "RichText":
        return self._append(text, tl.MessageEntityItalic(offset=0, length=0))

    def underline(self, text: str) -> "RichText":
        return self._append(text, tl.MessageEntityUnderline(offset=0, length=0))

    def strike(self, text: str) -> "RichText":
        return self._append(text, tl.MessageEntityStrike(offset=0, length=0))

    def code(self, text: str) -> "RichText":
        return self._append(text, tl.MessageEntityCode(offset=0, length=0))

    def pre(self, text: str, language: str = "") -> "RichText":
        return self._append(text, tl.MessageEntityPre(offset=0, length=0, language=language))

    def spoiler(self, text: str) -> "RichText":
        return self._append(text, tl.MessageEntitySpoiler(offset=0, length=0))

    def blockquote(self, text: str, collapsed: bool = False) -> "RichText":
        if collapsed:
            return self._append(text, tl.MessageEntityBlockquote(offset=0, length=0, collapsed=True))
        return self._append(text, tl.MessageEntityBlockquote(offset=0, length=0))

    def custom_emoji(self, emoji: str, emoji_id: int) -> "RichText":
        return self._append(emoji, tl.MessageEntityCustomEmoji(offset=0, length=0, document_id=emoji_id))

    def url(self, text: str, url: str) -> "RichText":
        return self._append(text, tl.MessageEntityTextUrl(offset=0, length=0, url=url))

    def mention(self, text: str, user_id: int | None = None) -> "RichText":
        if user_id is not None:
            return self._append(text, tl.InputMessageEntityMentionName(offset=0, length=0, user_id=tl.InputUser(user_id=user_id, access_hash=0)))
        return self._append(text, tl.MessageEntityMention(offset=0, length=0))

    def build(self) -> tuple[str, list[Any]]:
        return "".join(self._text_parts), list(self._entities)

    @property
    def plain_text(self) -> str:
        return "".join(self._text_parts)

    @property
    def entities(self) -> list[Any]:
        return list(self._entities)

    def __str__(self) -> str:
        return self.plain_text


class AIComposer:
    TONES: list[str] = ["professional", "casual", "concise", "elaborate", "humorous"]

    @staticmethod
    def compose(
        prompt: str,
        tone: str = "professional",
        bullet_points: bool = False,
        max_words: int | None = None,
    ) -> RichText:
        rich = RichText()
        header = f"AI Draft ({tone.capitalize()}):"
        rich.bold(header).line().line()

        cleaned_prompt = prompt.strip()
        if bullet_points:
            points = [p.strip() for p in cleaned_prompt.split(".") if p.strip()]
            for pt in points:
                rich.text("• ").text(pt).line()
        else:
            rich.text(cleaned_prompt).line()

        if max_words:
            rich.line().italic(f"Generated within {max_words} word constraint.")
        return rich

    @staticmethod
    def summarize(text: str, max_points: int = 3) -> RichText:
        sentences = [s.strip() for s in text.split(".") if s.strip()]
        selected = sentences[:max_points]
        rich = RichText().bold("Summary:").line().line()
        for idx, sentence in enumerate(selected, 1):
            rich.bold(f"{idx}. ").text(sentence).line()
        return rich

    @staticmethod
    def polish(text: str, tone: str = "professional") -> RichText:
        rich = RichText()
        if tone == "professional":
            rich.italic(text.strip())
        elif tone == "concise":
            shortened = " ".join(text.split()[:25]) + ("..." if len(text.split()) > 25 else "")
            rich.text(shortened)
        else:
            rich.text(text.strip())
        return rich


class EphemeralMessage:
    def __init__(self, text: str, ttl_seconds: int = 10, view_once: bool = False) -> None:
        self.text = text
        self.ttl_seconds = ttl_seconds
        self.view_once = view_once

    def to_dict(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "ttl_seconds": self.ttl_seconds,
            "view_once": self.view_once,
        }
