from typing import Any, Optional


class LinkPreviewOptions:
    def __init__(
        self,
        is_disabled: bool = False,
        url: str | None = None,
        prefer_small_media: bool = False,
        prefer_large_media: bool = False,
        show_above_text: bool = False,
    ) -> None:
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text


class ForumTopic:
    def __init__(
        self,
        message_thread_id: int,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: str | None = None,
    ) -> None:
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id


class StoryItem:
    def __init__(
        self,
        id: int,
        chat_id: int,
        date: int,
        media: Any = None,
        caption: str | None = None,
        views_count: int = 0,
    ) -> None:
        self.id = id
        self.chat_id = chat_id
        self.date = date
        self.media = media
        self.caption = caption
        self.views_count = views_count


class PaidMedia:
    def __init__(
        self,
        stars_amount: int,
        media: list[Any] | None = None,
    ) -> None:
        self.stars_amount = stars_amount
        self.media = media or []


class Gift:
    def __init__(
        self,
        id: str,
        sticker: Any = None,
        star_count: int = 0,
        total_count: int | None = None,
        remaining_count: int | None = None,
    ) -> None:
        self.id = id
        self.sticker = sticker
        self.star_count = star_count
        self.total_count = total_count
        self.remaining_count = remaining_count
