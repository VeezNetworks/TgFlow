from typing import Any, Optional


class PhotoSize:
    def __init__(self, file_id: str, file_unique_id: str, width: int, height: int, file_size: int | None = None) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size


class Photo:
    def __init__(self, sizes: list[PhotoSize]) -> None:
        self.sizes = sizes

    @property
    def file_id(self) -> str:
        return self.sizes[-1].file_id if self.sizes else ""

    @property
    def file_unique_id(self) -> str:
        return self.sizes[-1].file_unique_id if self.sizes else ""

    @property
    def width(self) -> int:
        return self.sizes[-1].width if self.sizes else 0

    @property
    def height(self) -> int:
        return self.sizes[-1].height if self.sizes else 0


class Video:
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: PhotoSize | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
        file_size: int | None = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Audio:
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        performer: str | None = None,
        title: str | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
        file_size: int | None = None,
        thumbnail: PhotoSize | None = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail


class Document:
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        thumbnail: PhotoSize | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
        file_size: int | None = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Voice:
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        mime_type: str | None = None,
        file_size: int | None = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


class Animation:
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: PhotoSize | None = None,
        file_name: str | None = None,
        mime_type: str | None = None,
        file_size: int | None = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Sticker:
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        type: str,
        width: int,
        height: int,
        is_animated: bool = False,
        is_video: bool = False,
        emoji: str | None = None,
        set_name: str | None = None,
        file_size: int | None = None,
        custom_emoji_id: str | None = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.emoji = emoji
        self.set_name = set_name
        self.file_size = file_size
        self.custom_emoji_id = custom_emoji_id


class Location:
    def __init__(self, latitude: float, longitude: float, horizontal_accuracy: float | None = None) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy


class Venue:
    def __init__(self, location: Location, title: str, address: str, foursquare_id: str | None = None) -> None:
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id


class Contact:
    def __init__(self, phone_number: str, first_name: str, last_name: str | None = None, user_id: int | None = None, vcard: str | None = None) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard


class Dice:
    def __init__(self, emoji: str, value: int) -> None:
        self.emoji = emoji
        self.value = value
