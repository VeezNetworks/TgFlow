from dataclasses import dataclass, field
from typing import Any, Optional
from tgflow.raw.core import TLObject, TLReader, TLRequest, TLWriter
from tgflow.raw import types


# Auth
@dataclass(slots=True)
class SendCode(TLRequest):
    ID: int = 0xA677244F
    QUALNAME: str = "functions.auth.SendCode"
    phone_number: str = ""
    api_id: int = 0
    api_hash: str = ""

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_string(self.phone_number)
        writer.write_int(self.api_id)
        writer.write_string(self.api_hash)


@dataclass(slots=True)
class SignIn(TLRequest):
    ID: int = 0x8D52A951
    QUALNAME: str = "functions.auth.SignIn"
    phone_number: str = ""
    phone_code_hash: str = ""
    phone_code: str = ""

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.phone_code)


@dataclass(slots=True)
class SignUp(TLRequest):
    ID: int = 0x80EEE427
    QUALNAME: str = "functions.auth.SignUp"
    phone_number: str = ""
    phone_code_hash: str = ""
    first_name: str = ""
    last_name: str = ""

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.first_name)
        writer.write_string(self.last_name)


@dataclass(slots=True)
class LogOut(TLRequest):
    ID: int = 0x3E72BA14
    QUALNAME: str = "functions.auth.LogOut"


# Help
@dataclass(slots=True)
class GetConfig(TLRequest):
    ID: int = 0xC4F918E0
    QUALNAME: str = "functions.help.GetConfig"


@dataclass(slots=True)
class GetNearestDc(TLRequest):
    ID: int = 0x1FB33026
    QUALNAME: str = "functions.help.GetNearestDc"


# Users & Contacts
@dataclass(slots=True)
class GetUsers(TLRequest):
    ID: int = 0x0D91A548
    QUALNAME: str = "functions.users.GetUsers"
    id: list[TLObject] = field(default_factory=list)

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_vector(self.id, lambda item: item.write(writer))


@dataclass(slots=True)
class ResolveUsername(TLRequest):
    ID: int = 0xF9434D82
    QUALNAME: str = "functions.contacts.ResolveUsername"
    username: str = ""

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_string(self.username)


# Messages
@dataclass(slots=True)
class SendMessage(TLRequest):
    ID: int = 0x520C3870
    QUALNAME: str = "functions.messages.SendMessage"
    peer: TLObject = field(default_factory=types.InputPeerSelf)
    message: str = ""
    random_id: int = 0
    reply_to_msg_id: Optional[int] = None

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        self.peer.write(writer)
        writer.write_string(self.message)
        writer.write_long(self.random_id)


@dataclass(slots=True)
class DeleteMessages(TLRequest):
    ID: int = 0xE58E95D2
    QUALNAME: str = "functions.messages.DeleteMessages"
    id: list[int] = field(default_factory=list)
    revoke: bool = True

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_vector(self.id, lambda x: writer.write_int(x))
        writer.write_bool(self.revoke)


@dataclass(slots=True)
class ForwardMessages(TLRequest):
    ID: int = 0xD91140AD
    QUALNAME: str = "functions.messages.ForwardMessages"
    from_peer: TLObject = field(default_factory=types.InputPeerSelf)
    id: list[int] = field(default_factory=list)
    to_peer: TLObject = field(default_factory=types.InputPeerSelf)

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        self.from_peer.write(writer)
        writer.write_vector(self.id, lambda x: writer.write_int(x))
        self.to_peer.write(writer)


@dataclass(slots=True)
class GetHistory(TLRequest):
    ID: int = 0x4423E6C5
    QUALNAME: str = "functions.messages.GetHistory"
    peer: TLObject = field(default_factory=types.InputPeerSelf)
    offset_id: int = 0
    offset_date: int = 0
    add_offset: int = 0
    limit: int = 100
    max_id: int = 0
    min_id: int = 0
    hash: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        self.peer.write(writer)
        writer.write_int(self.offset_id)
        writer.write_int(self.offset_date)
        writer.write_int(self.add_offset)
        writer.write_int(self.limit)
        writer.write_int(self.max_id)
        writer.write_int(self.min_id)
        writer.write_long(self.hash)


# Channels & Forum Topics
@dataclass(slots=True)
class CreateForumTopic(TLRequest):
    ID: int = 0xF40C0224
    QUALNAME: str = "functions.channels.CreateForumTopic"
    channel: TLObject = field(default_factory=types.InputPeerChannel)
    title: str = ""
    icon_color: int = 0
    icon_emoji_id: Optional[int] = None

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        self.channel.write(writer)
        writer.write_string(self.title)
        writer.write_int(self.icon_color)


@dataclass(slots=True)
class EditBanned(TLRequest):
    ID: int = 0x96E6CED3
    QUALNAME: str = "functions.channels.EditBanned"
    channel: TLObject = field(default_factory=types.InputPeerChannel)
    participant: TLObject = field(default_factory=types.InputPeerUser)
    banned_rights: int = 0

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        self.channel.write(writer)
        self.participant.write(writer)
        writer.write_int(self.banned_rights)


# Modern Payments & Stars
@dataclass(slots=True)
class SendStarsForm(TLRequest):
    ID: int = 0x777085DA
    QUALNAME: str = "functions.payments.SendStarsForm"
    form_id: int = 0
    invoice: TLObject = field(default_factory=types.InputPeerSelf)

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_long(self.form_id)
        self.invoice.write(writer)


@dataclass(slots=True)
class GetStarsTransactions(TLRequest):
    ID: int = 0x69da4539
    QUALNAME: str = "functions.payments.GetStarsTransactions"
    offset: str = ""
    limit: int = 100

    def write(self, writer: TLWriter) -> None:
        super().write(writer)
        writer.write_string(self.offset)
        writer.write_int(self.limit)
