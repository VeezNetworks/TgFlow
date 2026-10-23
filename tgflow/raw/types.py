from dataclasses import dataclass, field
from typing import Any, Optional
from tgflow.raw.core import TLObject, TLReader, TLWriter


# Input Peers
@dataclass(slots=True)
class InputPeerEmpty(TLObject):
    ID: int = 0x7F3B18EA
    QUALNAME: str = "types.InputPeerEmpty"


@dataclass(slots=True)
class InputPeerSelf(TLObject):
    ID: int = 0x7DA07EC9
    QUALNAME: str = "types.InputPeerSelf"


@dataclass(slots=True)
class InputPeerChat(TLObject):
    ID: int = 0x35A95D82
    QUALNAME: str = "types.InputPeerChat"
    chat_id: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_long(self.chat_id)

    @classmethod
    def read(cls, reader: TLReader) -> "InputPeerChat":
        return cls(chat_id=reader.read_long())


@dataclass(slots=True)
class InputPeerUser(TLObject):
    ID: int = 0xDDE8BA3C
    QUALNAME: str = "types.InputPeerUser"
    user_id: int = 0
    access_hash: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_long(self.user_id)
        writer.write_long(self.access_hash)

    @classmethod
    def read(cls, reader: TLReader) -> "InputPeerUser":
        return cls(user_id=reader.read_long(), access_hash=reader.read_long())


@dataclass(slots=True)
class InputPeerChannel(TLObject):
    ID: int = 0x27BC2CA7
    QUALNAME: str = "types.InputPeerChannel"
    channel_id: int = 0
    access_hash: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_long(self.channel_id)
        writer.write_long(self.access_hash)

    @classmethod
    def read(cls, reader: TLReader) -> "InputPeerChannel":
        return cls(channel_id=reader.read_long(), access_hash=reader.read_long())


# Peers
@dataclass(slots=True)
class PeerUser(TLObject):
    ID: int = 0x595F5663
    QUALNAME: str = "types.PeerUser"
    user_id: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_long(self.user_id)

    @classmethod
    def read(cls, reader: TLReader) -> "PeerUser":
        return cls(user_id=reader.read_long())


@dataclass(slots=True)
class PeerChat(TLObject):
    ID: int = 0x36C6088A
    QUALNAME: str = "types.PeerChat"
    chat_id: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_long(self.chat_id)

    @classmethod
    def read(cls, reader: TLReader) -> "PeerChat":
        return cls(chat_id=reader.read_long())


@dataclass(slots=True)
class PeerChannel(TLObject):
    ID: int = 0xA2A5379E
    QUALNAME: str = "types.PeerChannel"
    channel_id: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_long(self.channel_id)

    @classmethod
    def read(cls, reader: TLReader) -> "PeerChannel":
        return cls(channel_id=reader.read_long())


# Users & Chats
@dataclass(slots=True)
class User(TLObject):
    ID: int = 0x838EC744
    QUALNAME: str = "types.User"
    id: int = 0
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    phone: Optional[str] = None
    access_hash: Optional[int] = None
    is_bot: bool = False
    is_premium: bool = False


@dataclass(slots=True)
class Chat(TLObject):
    ID: int = 0x41CFAF56
    QUALNAME: str = "types.Chat"
    id: int = 0
    title: str = ""
    participants_count: int = 0
    date: int = 0


@dataclass(slots=True)
class Channel(TLObject):
    ID: int = 0x826619C0
    QUALNAME: str = "types.Channel"
    id: int = 0
    title: str = ""
    username: Optional[str] = None
    access_hash: Optional[int] = None
    is_megagroup: bool = False
    is_forum: bool = False


# Messages & Updates
@dataclass(slots=True)
class Message(TLObject):
    ID: int = 0x76145363
    QUALNAME: str = "types.Message"
    id: int = 0
    peer_id: Optional[TLObject] = None
    date: int = 0
    message: str = ""
    reply_to_msg_id: Optional[int] = None


@dataclass(slots=True)
class Updates(TLObject):
    ID: int = 0x74CC1123
    QUALNAME: str = "types.Updates"
    updates: list[Any] = field(default_factory=list)
    users: list[User] = field(default_factory=list)
    chats: list[Any] = field(default_factory=list)
    date: int = 0
    seq: int = 0


# Modern Features (Stars, Business, Stories, Topics, Gifts)
@dataclass(slots=True)
class StarsTransaction(TLObject):
    ID: int = 0x89D29A10
    QUALNAME: str = "types.StarsTransaction"
    id: str = ""
    stars: int = 0
    date: int = 0
    title: Optional[str] = None
    description: Optional[str] = None


@dataclass(slots=True)
class BusinessConnection(TLObject):
    ID: int = 0xA26F90E1
    QUALNAME: str = "types.BusinessConnection"
    id: str = ""
    user_id: int = 0
    dc_id: int = 0
    can_reply: bool = True
    is_disabled: bool = False


@dataclass(slots=True)
class StoryItem(TLObject):
    ID: int = 0x79B5B2E8
    QUALNAME: str = "types.StoryItem"
    id: int = 0
    date: int = 0
    expire_date: int = 0
    caption: Optional[str] = None
    views_count: int = 0


@dataclass(slots=True)
class ForumTopic(TLObject):
    ID: int = 0x71701DA9
    QUALNAME: str = "types.ForumTopic"
    id: int = 0
    title: str = ""
    icon_color: int = 0
    icon_emoji_id: Optional[int] = None
    is_closed: bool = False


@dataclass(slots=True)
class StarGift(TLObject):
    ID: int = 0x5D8489F3
    QUALNAME: str = "types.StarGift"
    id: int = 0
    stars: int = 0
    total_count: int = 0
    remaining_count: int = 0
