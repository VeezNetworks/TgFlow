from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class MessageEntityCode(TLObject):
    ID: int = 0x28a20571

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityCode':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityPre(TLObject):
    ID: int = 0x73924be0

    def __init__(self, offset: Any = None, length: Any = None, language: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.language = language

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_string(self.language or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityPre':
        offset = reader.read_int32()
        length = reader.read_int32()
        language = reader.read_string()
        return cls(offset=offset, length=length, language=language)


@register_tl
class MessageEntityTextUrl(TLObject):
    ID: int = 0x76a6d327

    def __init__(self, offset: Any = None, length: Any = None, url: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityTextUrl':
        offset = reader.read_int32()
        length = reader.read_int32()
        url = reader.read_string()
        return cls(offset=offset, length=length, url=url)


@register_tl
class MessageEntityMentionName(TLObject):
    ID: int = 0xdc7b1140

    def __init__(self, offset: Any = None, length: Any = None, user_id: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityMentionName':
        offset = reader.read_int32()
        length = reader.read_int32()
        user_id = reader.read_int64()
        return cls(offset=offset, length=length, user_id=user_id)


@register_tl
class InputMessageEntityMentionName(TLObject):
    ID: int = 0x208e68c9

    def __init__(self, offset: Any = None, length: Any = None, user_id: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessageEntityMentionName':
        offset = reader.read_int32()
        length = reader.read_int32()
        user_id = reader.read_object()
        return cls(offset=offset, length=length, user_id=user_id)


@register_tl
class MessageEntityPhone(TLObject):
    ID: int = 0x9b69e34b

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityPhone':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityCashtag(TLObject):
    ID: int = 0x4c4e743f

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityCashtag':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityUnderline(TLObject):
    ID: int = 0x9c4e7e8b

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityUnderline':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityStrike(TLObject):
    ID: int = 0xbf0693d4

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityStrike':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityBankCard(TLObject):
    ID: int = 0x761e6af4

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityBankCard':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntitySpoiler(TLObject):
    ID: int = 0x32ca960f

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntitySpoiler':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityCustomEmoji(TLObject):
    ID: int = 0xc8cf05f8

    def __init__(self, offset: Any = None, length: Any = None, document_id: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_int64(self.document_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityCustomEmoji':
        offset = reader.read_int32()
        length = reader.read_int32()
        document_id = reader.read_int64()
        return cls(offset=offset, length=length, document_id=document_id)


@register_tl
class MessageEntityBlockquote(TLObject):
    ID: int = 0xf1ccaaac

    def __init__(self, collapsed: bool = False, offset: Any = None, length: Any = None) -> None:
        self.collapsed = collapsed
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.collapsed:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityBlockquote':
        flags = reader.read_uint32()
        collapsed = bool(flags & (1 << 0))
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(collapsed=collapsed, offset=offset, length=length)


@register_tl
class MessageEntityFormattedDate(TLObject):
    ID: int = 0x904ac7c7

    def __init__(self, relative: bool = False, short_time: bool = False, long_time: bool = False, short_date: bool = False, long_date: bool = False, day_of_week: bool = False, offset: Any = None, length: Any = None, date: Any = None) -> None:
        self.relative = relative
        self.short_time = short_time
        self.long_time = long_time
        self.short_date = short_date
        self.long_date = long_date
        self.day_of_week = day_of_week
        self.offset = offset
        self.length = length
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.relative:
            flags |= (1 << 0)
        if self.short_time:
            flags |= (1 << 1)
        if self.long_time:
            flags |= (1 << 2)
        if self.short_date:
            flags |= (1 << 3)
        if self.long_date:
            flags |= (1 << 4)
        if self.day_of_week:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityFormattedDate':
        flags = reader.read_uint32()
        relative = bool(flags & (1 << 0))
        short_time = bool(flags & (1 << 1))
        long_time = bool(flags & (1 << 2))
        short_date = bool(flags & (1 << 3))
        long_date = bool(flags & (1 << 4))
        day_of_week = bool(flags & (1 << 5))
        offset = reader.read_int32()
        length = reader.read_int32()
        date = reader.read_int32()
        return cls(relative=relative, short_time=short_time, long_time=long_time, short_date=short_date, long_date=long_date, day_of_week=day_of_week, offset=offset, length=length, date=date)


@register_tl
class MessageEntityDiffInsert(TLObject):
    ID: int = 0x71777116

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityDiffInsert':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityDiffReplace(TLObject):
    ID: int = 0xc6c1e5a7

    def __init__(self, offset: Any = None, length: Any = None, old_text: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.old_text = old_text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_string(self.old_text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityDiffReplace':
        offset = reader.read_int32()
        length = reader.read_int32()
        old_text = reader.read_string()
        return cls(offset=offset, length=length, old_text=old_text)


@register_tl
class MessageEntityDiffDelete(TLObject):
    ID: int = 0x652c1c5

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityDiffDelete':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class InputChannelEmpty(TLObject):
    ID: int = 0xee8c1e86

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChannelEmpty':
        return cls()


@register_tl
class InputChannel(TLObject):
    ID: int = 0xf35aec28

    def __init__(self, channel_id: Any = None, access_hash: Any = None) -> None:
        self.channel_id = channel_id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChannel':
        channel_id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(channel_id=channel_id, access_hash=access_hash)


@register_tl
class InputChannelFromMessage(TLObject):
    ID: int = 0x5b934f9d

    def __init__(self, peer: Any = None, msg_id: Any = None, channel_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChannelFromMessage':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        channel_id = reader.read_int64()
        return cls(peer=peer, msg_id=msg_id, channel_id=channel_id)


@register_tl
class ContactsResolvedPeer(TLObject):
    ID: int = 0x7f077ad9

    def __init__(self, peer: Any = None, chats: Any = None, users: Any = None) -> None:
        self.peer = peer
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsResolvedPeer':
        peer = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, chats=chats, users=users)


@register_tl
class MessageRange(TLObject):
    ID: int = 0xae30253

    def __init__(self, min_id: Any = None, max_id: Any = None) -> None:
        self.min_id = min_id
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.min_id or 0)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageRange':
        min_id = reader.read_int32()
        max_id = reader.read_int32()
        return cls(min_id=min_id, max_id=max_id)


@register_tl
class UpdatesChannelDifferenceEmpty(TLObject):
    ID: int = 0x3e11affb

    def __init__(self, final: bool = False, timeout: Any = None, pts: Any = None) -> None:
        self.final = final
        self.timeout = timeout
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.final:
            flags |= (1 << 0)
        if self.timeout is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.pts or 0)
        if self.timeout is not None:
            writer.write_int32(self.timeout or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesChannelDifferenceEmpty':
        flags = reader.read_uint32()
        final = bool(flags & (1 << 0))
        pts = reader.read_int32()
        timeout = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(final=final, pts=pts, timeout=timeout)


@register_tl
class UpdatesChannelDifferenceTooLong(TLObject):
    ID: int = 0xa4bcc6fe

    def __init__(self, final: bool = False, timeout: Any = None, dialog: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.final = final
        self.timeout = timeout
        self.dialog = dialog
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.final:
            flags |= (1 << 0)
        if self.timeout is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.timeout is not None:
            writer.write_int32(self.timeout or 0)
        if self.dialog is not None and hasattr(self.dialog, 'write'): self.dialog.write(writer)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesChannelDifferenceTooLong':
        flags = reader.read_uint32()
        final = bool(flags & (1 << 0))
        timeout = reader.read_int32() if (flags & (1 << 1)) else None
        dialog = reader.read_object()
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(final=final, timeout=timeout, dialog=dialog, messages=messages, chats=chats, users=users)


@register_tl
class UpdatesChannelDifference(TLObject):
    ID: int = 0x2064674e

    def __init__(self, final: bool = False, timeout: Any = None, pts: Any = None, new_messages: Any = None, other_updates: Any = None, chats: Any = None, users: Any = None) -> None:
        self.final = final
        self.timeout = timeout
        self.pts = pts
        self.new_messages = new_messages
        self.other_updates = other_updates
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.final:
            flags |= (1 << 0)
        if self.timeout is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.pts or 0)
        if self.timeout is not None:
            writer.write_int32(self.timeout or 0)
        writer.write_vector(self.new_messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.other_updates or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesChannelDifference':
        flags = reader.read_uint32()
        final = bool(flags & (1 << 0))
        pts = reader.read_int32()
        timeout = reader.read_int32() if (flags & (1 << 1)) else None
        new_messages = reader.read_vector(lambda r: reader.read_object())
        other_updates = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(final=final, pts=pts, timeout=timeout, new_messages=new_messages, other_updates=other_updates, chats=chats, users=users)


@register_tl
class ChannelMessagesFilterEmpty(TLObject):
    ID: int = 0x94d42ee7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelMessagesFilterEmpty':
        return cls()


@register_tl
class ChannelMessagesFilter(TLObject):
    ID: int = 0xcd77d957

    def __init__(self, exclude_new_messages: bool = False, ranges: Any = None) -> None:
        self.exclude_new_messages = exclude_new_messages
        self.ranges = ranges

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.exclude_new_messages:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_vector(self.ranges or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelMessagesFilter':
        flags = reader.read_uint32()
        exclude_new_messages = bool(flags & (1 << 1))
        ranges = reader.read_vector(lambda r: reader.read_object())
        return cls(exclude_new_messages=exclude_new_messages, ranges=ranges)


@register_tl
class ChannelParticipant(TLObject):
    ID: int = 0x1bd54456

    def __init__(self, subscription_until_date: Any = None, rank: Any = None, user_id: Any = None, date: Any = None) -> None:
        self.subscription_until_date = subscription_until_date
        self.rank = rank
        self.user_id = user_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.subscription_until_date is not None:
            flags |= (1 << 0)
        if self.rank is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.date or 0)
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipant':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        date = reader.read_int32()
        subscription_until_date = reader.read_int32() if (flags & (1 << 0)) else None
        rank = reader.read_string() if (flags & (1 << 2)) else None
        return cls(user_id=user_id, date=date, subscription_until_date=subscription_until_date, rank=rank)


@register_tl
class ChannelParticipantSelf(TLObject):
    ID: int = 0xa9478a1a

    def __init__(self, via_request: bool = False, subscription_until_date: Any = None, rank: Any = None, user_id: Any = None, inviter_id: Any = None, date: Any = None) -> None:
        self.via_request = via_request
        self.subscription_until_date = subscription_until_date
        self.rank = rank
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_request:
            flags |= (1 << 0)
        if self.subscription_until_date is not None:
            flags |= (1 << 1)
        if self.rank is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantSelf':
        flags = reader.read_uint32()
        via_request = bool(flags & (1 << 0))
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        subscription_until_date = reader.read_int32() if (flags & (1 << 1)) else None
        rank = reader.read_string() if (flags & (1 << 2)) else None
        return cls(via_request=via_request, user_id=user_id, inviter_id=inviter_id, date=date, subscription_until_date=subscription_until_date, rank=rank)


@register_tl
class ChannelParticipantCreator(TLObject):
    ID: int = 0x2fe601d3

    def __init__(self, rank: Any = None, user_id: Any = None, admin_rights: Any = None) -> None:
        self.rank = rank
        self.user_id = user_id
        self.admin_rights = admin_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.admin_rights is not None and hasattr(self.admin_rights, 'write'): self.admin_rights.write(writer)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantCreator':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        admin_rights = reader.read_object()
        rank = reader.read_string() if (flags & (1 << 0)) else None
        return cls(user_id=user_id, admin_rights=admin_rights, rank=rank)


@register_tl
class ChannelParticipantAdmin(TLObject):
    ID: int = 0x34c3bb53

    def __init__(self, can_edit: bool = False, self_: bool = False, inviter_id: Any = None, rank: Any = None, user_id: Any = None, promoted_by: Any = None, date: Any = None, admin_rights: Any = None) -> None:
        self.can_edit = can_edit
        self.self_ = self_
        self.inviter_id = inviter_id
        self.rank = rank
        self.user_id = user_id
        self.promoted_by = promoted_by
        self.date = date
        self.admin_rights = admin_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_edit:
            flags |= (1 << 0)
        if self.self_:
            flags |= (1 << 1)
        if self.inviter_id is not None:
            flags |= (1 << 1)
        if self.rank is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.inviter_id is not None:
            writer.write_int64(self.inviter_id or 0)
        writer.write_int64(self.promoted_by or 0)
        writer.write_int32(self.date or 0)
        if self.admin_rights is not None and hasattr(self.admin_rights, 'write'): self.admin_rights.write(writer)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantAdmin':
        flags = reader.read_uint32()
        can_edit = bool(flags & (1 << 0))
        self_ = bool(flags & (1 << 1))
        user_id = reader.read_int64()
        inviter_id = reader.read_int64() if (flags & (1 << 1)) else None
        promoted_by = reader.read_int64()
        date = reader.read_int32()
        admin_rights = reader.read_object()
        rank = reader.read_string() if (flags & (1 << 2)) else None
        return cls(can_edit=can_edit, self_=self_, user_id=user_id, inviter_id=inviter_id, promoted_by=promoted_by, date=date, admin_rights=admin_rights, rank=rank)


@register_tl
class ChannelParticipantBanned(TLObject):
    ID: int = 0xd5f0ad91

    def __init__(self, left: bool = False, rank: Any = None, peer: Any = None, kicked_by: Any = None, date: Any = None, banned_rights: Any = None) -> None:
        self.left = left
        self.rank = rank
        self.peer = peer
        self.kicked_by = kicked_by
        self.date = date
        self.banned_rights = banned_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.left:
            flags |= (1 << 0)
        if self.rank is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.kicked_by or 0)
        writer.write_int32(self.date or 0)
        if self.banned_rights is not None and hasattr(self.banned_rights, 'write'): self.banned_rights.write(writer)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantBanned':
        flags = reader.read_uint32()
        left = bool(flags & (1 << 0))
        peer = reader.read_object()
        kicked_by = reader.read_int64()
        date = reader.read_int32()
        banned_rights = reader.read_object()
        rank = reader.read_string() if (flags & (1 << 2)) else None
        return cls(left=left, peer=peer, kicked_by=kicked_by, date=date, banned_rights=banned_rights, rank=rank)


@register_tl
class ChannelParticipantLeft(TLObject):
    ID: int = 0x1b03f006

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantLeft':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class ChannelParticipantsRecent(TLObject):
    ID: int = 0xde3f3c79

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsRecent':
        return cls()


@register_tl
class ChannelParticipantsAdmins(TLObject):
    ID: int = 0xb4608969

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsAdmins':
        return cls()


@register_tl
class ChannelParticipantsKicked(TLObject):
    ID: int = 0xa3b54985

    def __init__(self, q: Any = None) -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsKicked':
        q = reader.read_string()
        return cls(q=q)


@register_tl
class ChannelParticipantsBots(TLObject):
    ID: int = 0xb0d1865b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsBots':
        return cls()


@register_tl
class ChannelParticipantsBanned(TLObject):
    ID: int = 0x1427a5e1

    def __init__(self, q: Any = None) -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsBanned':
        q = reader.read_string()
        return cls(q=q)


@register_tl
class ChannelParticipantsSearch(TLObject):
    ID: int = 0x656ac4b

    def __init__(self, q: Any = None) -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsSearch':
        q = reader.read_string()
        return cls(q=q)


@register_tl
class ChannelParticipantsContacts(TLObject):
    ID: int = 0xbb6ae88d

    def __init__(self, q: Any = None) -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsContacts':
        q = reader.read_string()
        return cls(q=q)


@register_tl
class ChannelParticipantsMentions(TLObject):
    ID: int = 0xe04b5ceb

    def __init__(self, q: Any = None, top_msg_id: Any = None) -> None:
        self.q = q
        self.top_msg_id = top_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.q is not None:
            flags |= (1 << 0)
        if self.top_msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.q is not None:
            writer.write_string(self.q or '')
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelParticipantsMentions':
        flags = reader.read_uint32()
        q = reader.read_string() if (flags & (1 << 0)) else None
        top_msg_id = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(q=q, top_msg_id=top_msg_id)


@register_tl
class ChannelsChannelParticipants(TLObject):
    ID: int = 0x9ab0feaf

    def __init__(self, count: Any = None, participants: Any = None, chats: Any = None, users: Any = None) -> None:
        self.count = count
        self.participants = participants
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.participants or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsChannelParticipants':
        count = reader.read_int32()
        participants = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, participants=participants, chats=chats, users=users)


@register_tl
class ChannelsChannelParticipantsNotModified(TLObject):
    ID: int = 0xf0173fe9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsChannelParticipantsNotModified':
        return cls()


@register_tl
class ChannelsChannelParticipant(TLObject):
    ID: int = 0xdfb80317

    def __init__(self, participant: Any = None, chats: Any = None, users: Any = None) -> None:
        self.participant = participant
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsChannelParticipant':
        participant = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(participant=participant, chats=chats, users=users)


@register_tl
class HelpTermsOfService(TLObject):
    ID: int = 0x780a0310

    def __init__(self, popup: bool = False, min_age_confirm: Any = None, id: Any = None, text: Any = None, entities: Any = None) -> None:
        self.popup = popup
        self.min_age_confirm = min_age_confirm
        self.id = id
        self.text = text
        self.entities = entities

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.popup:
            flags |= (1 << 0)
        if self.min_age_confirm is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_string(self.text or '')
        writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.min_age_confirm is not None:
            writer.write_int32(self.min_age_confirm or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpTermsOfService':
        flags = reader.read_uint32()
        popup = bool(flags & (1 << 0))
        id = reader.read_object()
        text = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object())
        min_age_confirm = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(popup=popup, id=id, text=text, entities=entities, min_age_confirm=min_age_confirm)


@register_tl
class MessagesSavedGifsNotModified(TLObject):
    ID: int = 0xe8025ca2

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavedGifsNotModified':
        return cls()


@register_tl
class MessagesSavedGifs(TLObject):
    ID: int = 0x84a02a0d

    def __init__(self, hash: Any = None, gifs: Any = None) -> None:
        self.hash = hash
        self.gifs = gifs

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.gifs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavedGifs':
        hash = reader.read_int64()
        gifs = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, gifs=gifs)


@register_tl
class InputBotInlineMessageMediaAuto(TLObject):
    ID: int = 0x3380c786

    def __init__(self, invert_media: bool = False, entities: Any = None, reply_markup: Any = None, message: Any = None) -> None:
        self.invert_media = invert_media
        self.entities = entities
        self.reply_markup = reply_markup
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.invert_media:
            flags |= (1 << 3)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageMediaAuto':
        flags = reader.read_uint32()
        invert_media = bool(flags & (1 << 3))
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(invert_media=invert_media, message=message, entities=entities, reply_markup=reply_markup)


@register_tl
class InputBotInlineMessageText(TLObject):
    ID: int = 0x3dcd7a87

    def __init__(self, no_webpage: bool = False, invert_media: bool = False, entities: Any = None, reply_markup: Any = None, message: Any = None) -> None:
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.entities = entities
        self.reply_markup = reply_markup
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 0)
        if self.invert_media:
            flags |= (1 << 3)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageText':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 0))
        invert_media = bool(flags & (1 << 3))
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(no_webpage=no_webpage, invert_media=invert_media, message=message, entities=entities, reply_markup=reply_markup)


@register_tl
class InputBotInlineMessageMediaGeo(TLObject):
    ID: int = 0x96929a85

    def __init__(self, heading: Any = None, period: Any = None, proximity_notification_radius: Any = None, reply_markup: Any = None, geo_point: Any = None) -> None:
        self.heading = heading
        self.period = period
        self.proximity_notification_radius = proximity_notification_radius
        self.reply_markup = reply_markup
        self.geo_point = geo_point

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.heading is not None:
            flags |= (1 << 0)
        if self.period is not None:
            flags |= (1 << 1)
        if self.proximity_notification_radius is not None:
            flags |= (1 << 3)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        if self.heading is not None:
            writer.write_int32(self.heading or 0)
        if self.period is not None:
            writer.write_int32(self.period or 0)
        if self.proximity_notification_radius is not None:
            writer.write_int32(self.proximity_notification_radius or 0)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageMediaGeo':
        flags = reader.read_uint32()
        geo_point = reader.read_object()
        heading = reader.read_int32() if (flags & (1 << 0)) else None
        period = reader.read_int32() if (flags & (1 << 1)) else None
        proximity_notification_radius = reader.read_int32() if (flags & (1 << 3)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(geo_point=geo_point, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius, reply_markup=reply_markup)


@register_tl
class InputBotInlineMessageMediaVenue(TLObject):
    ID: int = 0x417bbf11

    def __init__(self, reply_markup: Any = None, geo_point: Any = None, title: Any = None, address: Any = None, provider: Any = None, venue_id: Any = None, venue_type: Any = None) -> None:
        self.reply_markup = reply_markup
        self.geo_point = geo_point
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        writer.write_string(self.title or '')
        writer.write_string(self.address or '')
        writer.write_string(self.provider or '')
        writer.write_string(self.venue_id or '')
        writer.write_string(self.venue_type or '')
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageMediaVenue':
        flags = reader.read_uint32()
        geo_point = reader.read_object()
        title = reader.read_string()
        address = reader.read_string()
        provider = reader.read_string()
        venue_id = reader.read_string()
        venue_type = reader.read_string()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(geo_point=geo_point, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type, reply_markup=reply_markup)


@register_tl
class InputBotInlineMessageMediaContact(TLObject):
    ID: int = 0xa6edbffd

    def __init__(self, reply_markup: Any = None, phone_number: Any = None, first_name: Any = None, last_name: Any = None, vcard: Any = None) -> None:
        self.reply_markup = reply_markup
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_string(self.vcard or '')
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageMediaContact':
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        vcard = reader.read_string()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard, reply_markup=reply_markup)


@register_tl
class InputBotInlineMessageGame(TLObject):
    ID: int = 0x4b425864

    def __init__(self, reply_markup: Any = None) -> None:
        self.reply_markup = reply_markup

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageGame':
        flags = reader.read_uint32()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(reply_markup=reply_markup)


@register_tl
class InputBotInlineMessageMediaInvoice(TLObject):
    ID: int = 0xd7e78225

    def __init__(self, photo: Any = None, reply_markup: Any = None, title: Any = None, description: Any = None, invoice: Any = None, payload: Any = None, provider: Any = None, provider_data: Any = None) -> None:
        self.photo = photo
        self.reply_markup = reply_markup
        self.title = title
        self.description = description
        self.invoice = invoice
        self.payload = payload
        self.provider = provider
        self.provider_data = provider_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.photo is not None:
            flags |= (1 << 0)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        writer.write_bytes(self.payload or b'')
        writer.write_string(self.provider or '')
        if self.provider_data is not None and hasattr(self.provider_data, 'write'): self.provider_data.write(writer)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageMediaInvoice':
        flags = reader.read_uint32()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 0)) else None
        invoice = reader.read_object()
        payload = reader.read_bytes()
        provider = reader.read_string()
        provider_data = reader.read_object()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(title=title, description=description, photo=photo, invoice=invoice, payload=payload, provider=provider, provider_data=provider_data, reply_markup=reply_markup)


@register_tl
class InputBotInlineMessageMediaWebPage(TLObject):
    ID: int = 0xbddcc510

    def __init__(self, invert_media: bool = False, force_large_media: bool = False, force_small_media: bool = False, optional: bool = False, entities: Any = None, reply_markup: Any = None, message: Any = None, url: Any = None) -> None:
        self.invert_media = invert_media
        self.force_large_media = force_large_media
        self.force_small_media = force_small_media
        self.optional = optional
        self.entities = entities
        self.reply_markup = reply_markup
        self.message = message
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.invert_media:
            flags |= (1 << 3)
        if self.force_large_media:
            flags |= (1 << 4)
        if self.force_small_media:
            flags |= (1 << 5)
        if self.optional:
            flags |= (1 << 6)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.url or '')
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageMediaWebPage':
        flags = reader.read_uint32()
        invert_media = bool(flags & (1 << 3))
        force_large_media = bool(flags & (1 << 4))
        force_small_media = bool(flags & (1 << 5))
        optional = bool(flags & (1 << 6))
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        url = reader.read_string()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(invert_media=invert_media, force_large_media=force_large_media, force_small_media=force_small_media, optional=optional, message=message, entities=entities, url=url, reply_markup=reply_markup)


@register_tl
class InputBotInlineResult(TLObject):
    ID: int = 0x88bf9319

    def __init__(self, title: Any = None, description: Any = None, url: Any = None, thumb: Any = None, content: Any = None, id: Any = None, type: Any = None, send_message: Any = None) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.thumb = thumb
        self.content = content
        self.id = id
        self.type = type
        self.send_message = send_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 1)
        if self.description is not None:
            flags |= (1 << 2)
        if self.url is not None:
            flags |= (1 << 3)
        if self.thumb is not None:
            flags |= (1 << 4)
        if self.content is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        writer.write_string(self.type or '')
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.thumb is not None:
            if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        if self.content is not None:
            if self.content is not None and hasattr(self.content, 'write'): self.content.write(writer)
        if self.send_message is not None and hasattr(self.send_message, 'write'): self.send_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineResult':
        flags = reader.read_uint32()
        id = reader.read_string()
        type = reader.read_string()
        title = reader.read_string() if (flags & (1 << 1)) else None
        description = reader.read_string() if (flags & (1 << 2)) else None
        url = reader.read_string() if (flags & (1 << 3)) else None
        thumb = reader.read_object() if (flags & (1 << 4)) else None
        content = reader.read_object() if (flags & (1 << 5)) else None
        send_message = reader.read_object()
        return cls(id=id, type=type, title=title, description=description, url=url, thumb=thumb, content=content, send_message=send_message)


@register_tl
class InputBotInlineResultPhoto(TLObject):
    ID: int = 0xa8d864a7

    def __init__(self, id: Any = None, type: Any = None, photo: Any = None, send_message: Any = None) -> None:
        self.id = id
        self.type = type
        self.photo = photo
        self.send_message = send_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_string(self.type or '')
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.send_message is not None and hasattr(self.send_message, 'write'): self.send_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineResultPhoto':
        id = reader.read_string()
        type = reader.read_string()
        photo = reader.read_object()
        send_message = reader.read_object()
        return cls(id=id, type=type, photo=photo, send_message=send_message)


@register_tl
class InputBotInlineResultDocument(TLObject):
    ID: int = 0xfff8fdc4

    def __init__(self, title: Any = None, description: Any = None, id: Any = None, type: Any = None, document: Any = None, send_message: Any = None) -> None:
        self.title = title
        self.description = description
        self.id = id
        self.type = type
        self.document = document
        self.send_message = send_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 1)
        if self.description is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        writer.write_string(self.type or '')
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.send_message is not None and hasattr(self.send_message, 'write'): self.send_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineResultDocument':
        flags = reader.read_uint32()
        id = reader.read_string()
        type = reader.read_string()
        title = reader.read_string() if (flags & (1 << 1)) else None
        description = reader.read_string() if (flags & (1 << 2)) else None
        document = reader.read_object()
        send_message = reader.read_object()
        return cls(id=id, type=type, title=title, description=description, document=document, send_message=send_message)


@register_tl
class InputBotInlineResultGame(TLObject):
    ID: int = 0x4fa417f2

    def __init__(self, id: Any = None, short_name: Any = None, send_message: Any = None) -> None:
        self.id = id
        self.short_name = short_name
        self.send_message = send_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_string(self.short_name or '')
        if self.send_message is not None and hasattr(self.send_message, 'write'): self.send_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineResultGame':
        id = reader.read_string()
        short_name = reader.read_string()
        send_message = reader.read_object()
        return cls(id=id, short_name=short_name, send_message=send_message)


@register_tl
class BotInlineMessageMediaAuto(TLObject):
    ID: int = 0x764cf810

    def __init__(self, invert_media: bool = False, entities: Any = None, reply_markup: Any = None, message: Any = None) -> None:
        self.invert_media = invert_media
        self.entities = entities
        self.reply_markup = reply_markup
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.invert_media:
            flags |= (1 << 3)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMessageMediaAuto':
        flags = reader.read_uint32()
        invert_media = bool(flags & (1 << 3))
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(invert_media=invert_media, message=message, entities=entities, reply_markup=reply_markup)


@register_tl
class BotInlineMessageText(TLObject):
    ID: int = 0x8c7f65e2

    def __init__(self, no_webpage: bool = False, invert_media: bool = False, entities: Any = None, reply_markup: Any = None, message: Any = None) -> None:
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.entities = entities
        self.reply_markup = reply_markup
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 0)
        if self.invert_media:
            flags |= (1 << 3)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMessageText':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 0))
        invert_media = bool(flags & (1 << 3))
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(no_webpage=no_webpage, invert_media=invert_media, message=message, entities=entities, reply_markup=reply_markup)


@register_tl
class BotInlineMessageMediaGeo(TLObject):
    ID: int = 0x51846fd

    def __init__(self, heading: Any = None, period: Any = None, proximity_notification_radius: Any = None, reply_markup: Any = None, geo: Any = None) -> None:
        self.heading = heading
        self.period = period
        self.proximity_notification_radius = proximity_notification_radius
        self.reply_markup = reply_markup
        self.geo = geo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.heading is not None:
            flags |= (1 << 0)
        if self.period is not None:
            flags |= (1 << 1)
        if self.proximity_notification_radius is not None:
            flags |= (1 << 3)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        if self.heading is not None:
            writer.write_int32(self.heading or 0)
        if self.period is not None:
            writer.write_int32(self.period or 0)
        if self.proximity_notification_radius is not None:
            writer.write_int32(self.proximity_notification_radius or 0)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMessageMediaGeo':
        flags = reader.read_uint32()
        geo = reader.read_object()
        heading = reader.read_int32() if (flags & (1 << 0)) else None
        period = reader.read_int32() if (flags & (1 << 1)) else None
        proximity_notification_radius = reader.read_int32() if (flags & (1 << 3)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(geo=geo, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius, reply_markup=reply_markup)


@register_tl
class BotInlineMessageMediaVenue(TLObject):
    ID: int = 0x8a86659c

    def __init__(self, reply_markup: Any = None, geo: Any = None, title: Any = None, address: Any = None, provider: Any = None, venue_id: Any = None, venue_type: Any = None) -> None:
        self.reply_markup = reply_markup
        self.geo = geo
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        writer.write_string(self.title or '')
        writer.write_string(self.address or '')
        writer.write_string(self.provider or '')
        writer.write_string(self.venue_id or '')
        writer.write_string(self.venue_type or '')
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMessageMediaVenue':
        flags = reader.read_uint32()
        geo = reader.read_object()
        title = reader.read_string()
        address = reader.read_string()
        provider = reader.read_string()
        venue_id = reader.read_string()
        venue_type = reader.read_string()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type, reply_markup=reply_markup)


@register_tl
class BotInlineMessageMediaContact(TLObject):
    ID: int = 0x18d1cdc2

    def __init__(self, reply_markup: Any = None, phone_number: Any = None, first_name: Any = None, last_name: Any = None, vcard: Any = None) -> None:
        self.reply_markup = reply_markup
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_string(self.vcard or '')
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMessageMediaContact':
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        vcard = reader.read_string()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard, reply_markup=reply_markup)


@register_tl
class BotInlineMessageMediaInvoice(TLObject):
    ID: int = 0x354a9b09

    def __init__(self, shipping_address_requested: bool = False, test: bool = False, photo: Any = None, reply_markup: Any = None, title: Any = None, description: Any = None, currency: Any = None, total_amount: Any = None) -> None:
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.photo = photo
        self.reply_markup = reply_markup
        self.title = title
        self.description = description
        self.currency = currency
        self.total_amount = total_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.shipping_address_requested:
            flags |= (1 << 1)
        if self.test:
            flags |= (1 << 3)
        if self.photo is not None:
            flags |= (1 << 0)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMessageMediaInvoice':
        flags = reader.read_uint32()
        shipping_address_requested = bool(flags & (1 << 1))
        test = bool(flags & (1 << 3))
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 0)) else None
        currency = reader.read_string()
        total_amount = reader.read_int64()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(shipping_address_requested=shipping_address_requested, test=test, title=title, description=description, photo=photo, currency=currency, total_amount=total_amount, reply_markup=reply_markup)


@register_tl
class BotInlineMessageMediaWebPage(TLObject):
    ID: int = 0x809ad9a6

    def __init__(self, invert_media: bool = False, force_large_media: bool = False, force_small_media: bool = False, manual: bool = False, safe: bool = False, entities: Any = None, reply_markup: Any = None, message: Any = None, url: Any = None) -> None:
        self.invert_media = invert_media
        self.force_large_media = force_large_media
        self.force_small_media = force_small_media
        self.manual = manual
        self.safe = safe
        self.entities = entities
        self.reply_markup = reply_markup
        self.message = message
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.invert_media:
            flags |= (1 << 3)
        if self.force_large_media:
            flags |= (1 << 4)
        if self.force_small_media:
            flags |= (1 << 5)
        if self.manual:
            flags |= (1 << 7)
        if self.safe:
            flags |= (1 << 8)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.url or '')
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMessageMediaWebPage':
        flags = reader.read_uint32()
        invert_media = bool(flags & (1 << 3))
        force_large_media = bool(flags & (1 << 4))
        force_small_media = bool(flags & (1 << 5))
        manual = bool(flags & (1 << 7))
        safe = bool(flags & (1 << 8))
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        url = reader.read_string()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        return cls(invert_media=invert_media, force_large_media=force_large_media, force_small_media=force_small_media, manual=manual, safe=safe, message=message, entities=entities, url=url, reply_markup=reply_markup)


@register_tl
class BotInlineResult(TLObject):
    ID: int = 0x11965f3a

    def __init__(self, title: Any = None, description: Any = None, url: Any = None, thumb: Any = None, content: Any = None, id: Any = None, type: Any = None, send_message: Any = None) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.thumb = thumb
        self.content = content
        self.id = id
        self.type = type
        self.send_message = send_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 1)
        if self.description is not None:
            flags |= (1 << 2)
        if self.url is not None:
            flags |= (1 << 3)
        if self.thumb is not None:
            flags |= (1 << 4)
        if self.content is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        writer.write_string(self.type or '')
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.thumb is not None:
            if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        if self.content is not None:
            if self.content is not None and hasattr(self.content, 'write'): self.content.write(writer)
        if self.send_message is not None and hasattr(self.send_message, 'write'): self.send_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineResult':
        flags = reader.read_uint32()
        id = reader.read_string()
        type = reader.read_string()
        title = reader.read_string() if (flags & (1 << 1)) else None
        description = reader.read_string() if (flags & (1 << 2)) else None
        url = reader.read_string() if (flags & (1 << 3)) else None
        thumb = reader.read_object() if (flags & (1 << 4)) else None
        content = reader.read_object() if (flags & (1 << 5)) else None
        send_message = reader.read_object()
        return cls(id=id, type=type, title=title, description=description, url=url, thumb=thumb, content=content, send_message=send_message)


@register_tl
class BotInlineMediaResult(TLObject):
    ID: int = 0x17db940b

    def __init__(self, photo: Any = None, document: Any = None, title: Any = None, description: Any = None, id: Any = None, type: Any = None, send_message: Any = None) -> None:
        self.photo = photo
        self.document = document
        self.title = title
        self.description = description
        self.id = id
        self.type = type
        self.send_message = send_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.photo is not None:
            flags |= (1 << 0)
        if self.document is not None:
            flags |= (1 << 1)
        if self.title is not None:
            flags |= (1 << 2)
        if self.description is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        writer.write_string(self.type or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.send_message is not None and hasattr(self.send_message, 'write'): self.send_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInlineMediaResult':
        flags = reader.read_uint32()
        id = reader.read_string()
        type = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 0)) else None
        document = reader.read_object() if (flags & (1 << 1)) else None
        title = reader.read_string() if (flags & (1 << 2)) else None
        description = reader.read_string() if (flags & (1 << 3)) else None
        send_message = reader.read_object()
        return cls(id=id, type=type, photo=photo, document=document, title=title, description=description, send_message=send_message)


@register_tl
class MessagesBotResults(TLObject):
    ID: int = 0xe021f2f6

    def __init__(self, gallery: bool = False, next_offset: Any = None, switch_pm: Any = None, switch_webview: Any = None, query_id: Any = None, results: Any = None, cache_time: Any = None, users: Any = None) -> None:
        self.gallery = gallery
        self.next_offset = next_offset
        self.switch_pm = switch_pm
        self.switch_webview = switch_webview
        self.query_id = query_id
        self.results = results
        self.cache_time = cache_time
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.gallery:
            flags |= (1 << 0)
        if self.next_offset is not None:
            flags |= (1 << 1)
        if self.switch_pm is not None:
            flags |= (1 << 2)
        if self.switch_webview is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        if self.switch_pm is not None:
            if self.switch_pm is not None and hasattr(self.switch_pm, 'write'): self.switch_pm.write(writer)
        if self.switch_webview is not None:
            if self.switch_webview is not None and hasattr(self.switch_webview, 'write'): self.switch_webview.write(writer)
        writer.write_vector(self.results or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.cache_time or 0)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesBotResults':
        flags = reader.read_uint32()
        gallery = bool(flags & (1 << 0))
        query_id = reader.read_int64()
        next_offset = reader.read_string() if (flags & (1 << 1)) else None
        switch_pm = reader.read_object() if (flags & (1 << 2)) else None
        switch_webview = reader.read_object() if (flags & (1 << 3)) else None
        results = reader.read_vector(lambda r: reader.read_object())
        cache_time = reader.read_int32()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(gallery=gallery, query_id=query_id, next_offset=next_offset, switch_pm=switch_pm, switch_webview=switch_webview, results=results, cache_time=cache_time, users=users)


@register_tl
class ExportedMessageLink(TLObject):
    ID: int = 0x5dab1af4

    def __init__(self, link: Any = None, html: Any = None) -> None:
        self.link = link
        self.html = html

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.link or '')
        writer.write_string(self.html or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ExportedMessageLink':
        link = reader.read_string()
        html = reader.read_string()
        return cls(link=link, html=html)


@register_tl
class MessageFwdHeader(TLObject):
    ID: int = 0x4e4df4bb

    def __init__(self, imported: bool = False, saved_out: bool = False, from_id: Any = None, from_name: Any = None, channel_post: Any = None, post_author: Any = None, saved_from_peer: Any = None, saved_from_msg_id: Any = None, saved_from_id: Any = None, saved_from_name: Any = None, saved_date: Any = None, psa_type: Any = None, date: Any = None) -> None:
        self.imported = imported
        self.saved_out = saved_out
        self.from_id = from_id
        self.from_name = from_name
        self.channel_post = channel_post
        self.post_author = post_author
        self.saved_from_peer = saved_from_peer
        self.saved_from_msg_id = saved_from_msg_id
        self.saved_from_id = saved_from_id
        self.saved_from_name = saved_from_name
        self.saved_date = saved_date
        self.psa_type = psa_type
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.imported:
            flags |= (1 << 7)
        if self.saved_out:
            flags |= (1 << 11)
        if self.from_id is not None:
            flags |= (1 << 0)
        if self.from_name is not None:
            flags |= (1 << 5)
        if self.channel_post is not None:
            flags |= (1 << 2)
        if self.post_author is not None:
            flags |= (1 << 3)
        if self.saved_from_peer is not None:
            flags |= (1 << 4)
        if self.saved_from_msg_id is not None:
            flags |= (1 << 4)
        if self.saved_from_id is not None:
            flags |= (1 << 8)
        if self.saved_from_name is not None:
            flags |= (1 << 9)
        if self.saved_date is not None:
            flags |= (1 << 10)
        if self.psa_type is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.from_name is not None:
            writer.write_string(self.from_name or '')
        writer.write_int32(self.date or 0)
        if self.channel_post is not None:
            writer.write_int32(self.channel_post or 0)
        if self.post_author is not None:
            writer.write_string(self.post_author or '')
        if self.saved_from_peer is not None:
            if self.saved_from_peer is not None and hasattr(self.saved_from_peer, 'write'): self.saved_from_peer.write(writer)
        if self.saved_from_msg_id is not None:
            writer.write_int32(self.saved_from_msg_id or 0)
        if self.saved_from_id is not None:
            if self.saved_from_id is not None and hasattr(self.saved_from_id, 'write'): self.saved_from_id.write(writer)
        if self.saved_from_name is not None:
            writer.write_string(self.saved_from_name or '')
        if self.saved_date is not None:
            writer.write_int32(self.saved_date or 0)
        if self.psa_type is not None:
            writer.write_string(self.psa_type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageFwdHeader':
        flags = reader.read_uint32()
        imported = bool(flags & (1 << 7))
        saved_out = bool(flags & (1 << 11))
        from_id = reader.read_object() if (flags & (1 << 0)) else None
        from_name = reader.read_string() if (flags & (1 << 5)) else None
        date = reader.read_int32()
        channel_post = reader.read_int32() if (flags & (1 << 2)) else None
        post_author = reader.read_string() if (flags & (1 << 3)) else None
        saved_from_peer = reader.read_object() if (flags & (1 << 4)) else None
        saved_from_msg_id = reader.read_int32() if (flags & (1 << 4)) else None
        saved_from_id = reader.read_object() if (flags & (1 << 8)) else None
        saved_from_name = reader.read_string() if (flags & (1 << 9)) else None
        saved_date = reader.read_int32() if (flags & (1 << 10)) else None
        psa_type = reader.read_string() if (flags & (1 << 6)) else None
        return cls(imported=imported, saved_out=saved_out, from_id=from_id, from_name=from_name, date=date, channel_post=channel_post, post_author=post_author, saved_from_peer=saved_from_peer, saved_from_msg_id=saved_from_msg_id, saved_from_id=saved_from_id, saved_from_name=saved_from_name, saved_date=saved_date, psa_type=psa_type)


@register_tl
class AuthCodeTypeSms(TLObject):
    ID: int = 0x72a3158c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCodeTypeSms':
        return cls()


@register_tl
class AuthCodeTypeCall(TLObject):
    ID: int = 0x741cd3e3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCodeTypeCall':
        return cls()


@register_tl
class AuthCodeTypeFlashCall(TLObject):
    ID: int = 0x226ccefb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCodeTypeFlashCall':
        return cls()


@register_tl
class AuthCodeTypeMissedCall(TLObject):
    ID: int = 0xd61ad6ee

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCodeTypeMissedCall':
        return cls()


@register_tl
class AuthCodeTypeFragmentSms(TLObject):
    ID: int = 0x6ed998c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCodeTypeFragmentSms':
        return cls()


@register_tl
class AuthSentCodeTypeApp(TLObject):
    ID: int = 0x3dbb5986

    def __init__(self, length: Any = None) -> None:
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeApp':
        length = reader.read_int32()
        return cls(length=length)


@register_tl
class AuthSentCodeTypeSms(TLObject):
    ID: int = 0xc000bba2

    def __init__(self, length: Any = None) -> None:
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeSms':
        length = reader.read_int32()
        return cls(length=length)


@register_tl
class AuthSentCodeTypeCall(TLObject):
    ID: int = 0x5353e5a7

    def __init__(self, length: Any = None) -> None:
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeCall':
        length = reader.read_int32()
        return cls(length=length)


@register_tl
class AuthSentCodeTypeFlashCall(TLObject):
    ID: int = 0xab03c6d9

    def __init__(self, pattern: Any = None) -> None:
        self.pattern = pattern

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.pattern or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeFlashCall':
        pattern = reader.read_string()
        return cls(pattern=pattern)


@register_tl
class AuthSentCodeTypeMissedCall(TLObject):
    ID: int = 0x82006484

    def __init__(self, prefix: Any = None, length: Any = None) -> None:
        self.prefix = prefix
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.prefix or '')
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeMissedCall':
        prefix = reader.read_string()
        length = reader.read_int32()
        return cls(prefix=prefix, length=length)


@register_tl
class AuthSentCodeTypeEmailCode(TLObject):
    ID: int = 0xf450f59b

    def __init__(self, apple_signin_allowed: bool = False, google_signin_allowed: bool = False, reset_available_period: Any = None, reset_pending_date: Any = None, email_pattern: Any = None, length: Any = None) -> None:
        self.apple_signin_allowed = apple_signin_allowed
        self.google_signin_allowed = google_signin_allowed
        self.reset_available_period = reset_available_period
        self.reset_pending_date = reset_pending_date
        self.email_pattern = email_pattern
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.apple_signin_allowed:
            flags |= (1 << 0)
        if self.google_signin_allowed:
            flags |= (1 << 1)
        if self.reset_available_period is not None:
            flags |= (1 << 3)
        if self.reset_pending_date is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(self.email_pattern or '')
        writer.write_int32(self.length or 0)
        if self.reset_available_period is not None:
            writer.write_int32(self.reset_available_period or 0)
        if self.reset_pending_date is not None:
            writer.write_int32(self.reset_pending_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeEmailCode':
        flags = reader.read_uint32()
        apple_signin_allowed = bool(flags & (1 << 0))
        google_signin_allowed = bool(flags & (1 << 1))
        email_pattern = reader.read_string()
        length = reader.read_int32()
        reset_available_period = reader.read_int32() if (flags & (1 << 3)) else None
        reset_pending_date = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(apple_signin_allowed=apple_signin_allowed, google_signin_allowed=google_signin_allowed, email_pattern=email_pattern, length=length, reset_available_period=reset_available_period, reset_pending_date=reset_pending_date)


@register_tl
class AuthSentCodeTypeSetUpEmailRequired(TLObject):
    ID: int = 0xa5491dea

    def __init__(self, apple_signin_allowed: bool = False, google_signin_allowed: bool = False) -> None:
        self.apple_signin_allowed = apple_signin_allowed
        self.google_signin_allowed = google_signin_allowed

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.apple_signin_allowed:
            flags |= (1 << 0)
        if self.google_signin_allowed:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeSetUpEmailRequired':
        flags = reader.read_uint32()
        apple_signin_allowed = bool(flags & (1 << 0))
        google_signin_allowed = bool(flags & (1 << 1))
        return cls(apple_signin_allowed=apple_signin_allowed, google_signin_allowed=google_signin_allowed)


@register_tl
class AuthSentCodeTypeFragmentSms(TLObject):
    ID: int = 0xd9565c39

    def __init__(self, url: Any = None, length: Any = None) -> None:
        self.url = url
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeFragmentSms':
        url = reader.read_string()
        length = reader.read_int32()
        return cls(url=url, length=length)


@register_tl
class AuthSentCodeTypeFirebaseSms(TLObject):
    ID: int = 0x9fd736

    def __init__(self, nonce: Any = None, play_integrity_project_id: Any = None, play_integrity_nonce: Any = None, receipt: Any = None, push_timeout: Any = None, length: Any = None) -> None:
        self.nonce = nonce
        self.play_integrity_project_id = play_integrity_project_id
        self.play_integrity_nonce = play_integrity_nonce
        self.receipt = receipt
        self.push_timeout = push_timeout
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.nonce is not None:
            flags |= (1 << 0)
        if self.play_integrity_project_id is not None:
            flags |= (1 << 2)
        if self.play_integrity_nonce is not None:
            flags |= (1 << 2)
        if self.receipt is not None:
            flags |= (1 << 1)
        if self.push_timeout is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.nonce is not None:
            writer.write_bytes(self.nonce or b'')
        if self.play_integrity_project_id is not None:
            writer.write_int64(self.play_integrity_project_id or 0)
        if self.play_integrity_nonce is not None:
            writer.write_bytes(self.play_integrity_nonce or b'')
        if self.receipt is not None:
            writer.write_string(self.receipt or '')
        if self.push_timeout is not None:
            writer.write_int32(self.push_timeout or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeFirebaseSms':
        flags = reader.read_uint32()
        nonce = reader.read_bytes() if (flags & (1 << 0)) else None
        play_integrity_project_id = reader.read_int64() if (flags & (1 << 2)) else None
        play_integrity_nonce = reader.read_bytes() if (flags & (1 << 2)) else None
        receipt = reader.read_string() if (flags & (1 << 1)) else None
        push_timeout = reader.read_int32() if (flags & (1 << 1)) else None
        length = reader.read_int32()
        return cls(nonce=nonce, play_integrity_project_id=play_integrity_project_id, play_integrity_nonce=play_integrity_nonce, receipt=receipt, push_timeout=push_timeout, length=length)


@register_tl
class AuthSentCodeTypeSmsWord(TLObject):
    ID: int = 0xa416ac81

    def __init__(self, beginning: Any = None) -> None:
        self.beginning = beginning

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.beginning is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.beginning is not None:
            writer.write_string(self.beginning or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeSmsWord':
        flags = reader.read_uint32()
        beginning = reader.read_string() if (flags & (1 << 0)) else None
        return cls(beginning=beginning)


@register_tl
class AuthSentCodeTypeSmsPhrase(TLObject):
    ID: int = 0xb37794af

    def __init__(self, beginning: Any = None) -> None:
        self.beginning = beginning

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.beginning is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.beginning is not None:
            writer.write_string(self.beginning or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeTypeSmsPhrase':
        flags = reader.read_uint32()
        beginning = reader.read_string() if (flags & (1 << 0)) else None
        return cls(beginning=beginning)


@register_tl
class MessagesBotCallbackAnswer(TLObject):
    ID: int = 0x36585ea4

    def __init__(self, alert: bool = False, has_url: bool = False, native_ui: bool = False, message: Any = None, url: Any = None, cache_time: Any = None) -> None:
        self.alert = alert
        self.has_url = has_url
        self.native_ui = native_ui
        self.message = message
        self.url = url
        self.cache_time = cache_time

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.alert:
            flags |= (1 << 1)
        if self.has_url:
            flags |= (1 << 3)
        if self.native_ui:
            flags |= (1 << 4)
        if self.message is not None:
            flags |= (1 << 0)
        if self.url is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.message is not None:
            writer.write_string(self.message or '')
        if self.url is not None:
            writer.write_string(self.url or '')
        writer.write_int32(self.cache_time or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesBotCallbackAnswer':
        flags = reader.read_uint32()
        alert = bool(flags & (1 << 1))
        has_url = bool(flags & (1 << 3))
        native_ui = bool(flags & (1 << 4))
        message = reader.read_string() if (flags & (1 << 0)) else None
        url = reader.read_string() if (flags & (1 << 2)) else None
        cache_time = reader.read_int32()
        return cls(alert=alert, has_url=has_url, native_ui=native_ui, message=message, url=url, cache_time=cache_time)


@register_tl
class MessagesMessageEditData(TLObject):
    ID: int = 0x26b5dde6

    def __init__(self, caption: bool = False) -> None:
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.caption:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessageEditData':
        flags = reader.read_uint32()
        caption = bool(flags & (1 << 0))
        return cls(caption=caption)


@register_tl
class InputBotInlineMessageID(TLObject):
    ID: int = 0x890c3d89

    def __init__(self, dc_id: Any = None, id: Any = None, access_hash: Any = None) -> None:
        self.dc_id = dc_id
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id or 0)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageID':
        dc_id = reader.read_int32()
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(dc_id=dc_id, id=id, access_hash=access_hash)


@register_tl
class InputBotInlineMessageID64(TLObject):
    ID: int = 0xb6d915d7

    def __init__(self, dc_id: Any = None, owner_id: Any = None, id: Any = None, access_hash: Any = None) -> None:
        self.dc_id = dc_id
        self.owner_id = owner_id
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id or 0)
        writer.write_int64(self.owner_id or 0)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotInlineMessageID64':
        dc_id = reader.read_int32()
        owner_id = reader.read_int64()
        id = reader.read_int32()
        access_hash = reader.read_int64()
        return cls(dc_id=dc_id, owner_id=owner_id, id=id, access_hash=access_hash)


@register_tl
class InlineBotSwitchPM(TLObject):
    ID: int = 0x3c20629f

    def __init__(self, text: Any = None, start_param: Any = None) -> None:
        self.text = text
        self.start_param = start_param

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_string(self.start_param or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineBotSwitchPM':
        text = reader.read_string()
        start_param = reader.read_string()
        return cls(text=text, start_param=start_param)


@register_tl
class MessagesPeerDialogs(TLObject):
    ID: int = 0x3371c354

    def __init__(self, dialogs: Any = None, messages: Any = None, chats: Any = None, users: Any = None, state: Any = None) -> None:
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users
        self.state = state

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dialogs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.state is not None and hasattr(self.state, 'write'): self.state.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesPeerDialogs':
        dialogs = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        state = reader.read_object()
        return cls(dialogs=dialogs, messages=messages, chats=chats, users=users, state=state)


@register_tl
class TopPeer(TLObject):
    ID: int = 0xedcdc05b

    def __init__(self, peer: Any = None, rating: Any = None) -> None:
        self.peer = peer
        self.rating = rating

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_double(self.rating or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeer':
        peer = reader.read_object()
        rating = reader.read_double()
        return cls(peer=peer, rating=rating)


@register_tl
class TopPeerCategoryBotsPM(TLObject):
    ID: int = 0xab661b5b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryBotsPM':
        return cls()


@register_tl
class TopPeerCategoryBotsInline(TLObject):
    ID: int = 0x148677e2

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryBotsInline':
        return cls()


@register_tl
class TopPeerCategoryCorrespondents(TLObject):
    ID: int = 0x637b7ed

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryCorrespondents':
        return cls()


@register_tl
class TopPeerCategoryGroups(TLObject):
    ID: int = 0xbd17a14a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryGroups':
        return cls()


@register_tl
class TopPeerCategoryChannels(TLObject):
    ID: int = 0x161d9628

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryChannels':
        return cls()


@register_tl
class TopPeerCategoryPhoneCalls(TLObject):
    ID: int = 0x1e76a78c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryPhoneCalls':
        return cls()


@register_tl
class TopPeerCategoryForwardUsers(TLObject):
    ID: int = 0xa8406ca9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryForwardUsers':
        return cls()


@register_tl
class TopPeerCategoryForwardChats(TLObject):
    ID: int = 0xfbeec0f0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryForwardChats':
        return cls()


@register_tl
class TopPeerCategoryBotsApp(TLObject):
    ID: int = 0xfd9e7bec

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryBotsApp':
        return cls()


@register_tl
class TopPeerCategoryBotsGuestChat(TLObject):
    ID: int = 0x6c24f3dd

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryBotsGuestChat':
        return cls()


@register_tl
class TopPeerCategoryPeers(TLObject):
    ID: int = 0xfb834291

    def __init__(self, category: Any = None, count: Any = None, peers: Any = None) -> None:
        self.category = category
        self.count = count
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.category is not None and hasattr(self.category, 'write'): self.category.write(writer)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'TopPeerCategoryPeers':
        category = reader.read_object()
        count = reader.read_int32()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(category=category, count=count, peers=peers)


@register_tl
class ContactsTopPeersNotModified(TLObject):
    ID: int = 0xde266ef5

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsTopPeersNotModified':
        return cls()


@register_tl
class ContactsTopPeers(TLObject):
    ID: int = 0x70b772a8

    def __init__(self, categories: Any = None, chats: Any = None, users: Any = None) -> None:
        self.categories = categories
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.categories or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsTopPeers':
        categories = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(categories=categories, chats=chats, users=users)


@register_tl
class ContactsTopPeersDisabled(TLObject):
    ID: int = 0xb52c939d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsTopPeersDisabled':
        return cls()


@register_tl
class DraftMessageEmpty(TLObject):
    ID: int = 0x1b0c841a

    def __init__(self, date: Any = None) -> None:
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.date is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.date is not None:
            writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DraftMessageEmpty':
        flags = reader.read_uint32()
        date = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(date=date)


@register_tl
class DraftMessage(TLObject):
    ID: int = 0x96eaa5eb

    def __init__(self, no_webpage: bool = False, invert_media: bool = False, reply_to: Any = None, entities: Any = None, media: Any = None, effect: Any = None, suggested_post: Any = None, message: Any = None, date: Any = None) -> None:
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.entities = entities
        self.media = media
        self.effect = effect
        self.suggested_post = suggested_post
        self.message = message
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 1)
        if self.invert_media:
            flags |= (1 << 6)
        if self.reply_to is not None:
            flags |= (1 << 4)
        if self.entities is not None:
            flags |= (1 << 3)
        if self.media is not None:
            flags |= (1 << 5)
        if self.effect is not None:
            flags |= (1 << 7)
        if self.suggested_post is not None:
            flags |= (1 << 8)
        writer.write_uint32(flags)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        writer.write_int32(self.date or 0)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.suggested_post is not None:
            if self.suggested_post is not None and hasattr(self.suggested_post, 'write'): self.suggested_post.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DraftMessage':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        invert_media = bool(flags & (1 << 6))
        reply_to = reader.read_object() if (flags & (1 << 4)) else None
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        media = reader.read_object() if (flags & (1 << 5)) else None
        date = reader.read_int32()
        effect = reader.read_int64() if (flags & (1 << 7)) else None
        suggested_post = reader.read_object() if (flags & (1 << 8)) else None
        return cls(no_webpage=no_webpage, invert_media=invert_media, reply_to=reply_to, message=message, entities=entities, media=media, date=date, effect=effect, suggested_post=suggested_post)


@register_tl
class MessagesFeaturedStickersNotModified(TLObject):
    ID: int = 0xc6dc0c66

    def __init__(self, count: Any = None) -> None:
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFeaturedStickersNotModified':
        count = reader.read_int32()
        return cls(count=count)


@register_tl
class MessagesFeaturedStickers(TLObject):
    ID: int = 0xbe382906

    def __init__(self, premium: bool = False, hash: Any = None, count: Any = None, sets: Any = None, unread: Any = None) -> None:
        self.premium = premium
        self.hash = hash
        self.count = count
        self.sets = sets
        self.unread = unread

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.premium:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.sets or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.unread or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFeaturedStickers':
        flags = reader.read_uint32()
        premium = bool(flags & (1 << 0))
        hash = reader.read_int64()
        count = reader.read_int32()
        sets = reader.read_vector(lambda r: reader.read_object())
        unread = reader.read_vector(lambda r: r.read_int64())
        return cls(premium=premium, hash=hash, count=count, sets=sets, unread=unread)


@register_tl
class MessagesRecentStickersNotModified(TLObject):
    ID: int = 0xb17f890

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRecentStickersNotModified':
        return cls()


@register_tl
class MessagesRecentStickers(TLObject):
    ID: int = 0x88d37c56

    def __init__(self, hash: Any = None, packs: Any = None, stickers: Any = None, dates: Any = None) -> None:
        self.hash = hash
        self.packs = packs
        self.stickers = stickers
        self.dates = dates

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.packs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.dates or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRecentStickers':
        hash = reader.read_int64()
        packs = reader.read_vector(lambda r: reader.read_object())
        stickers = reader.read_vector(lambda r: reader.read_object())
        dates = reader.read_vector(lambda r: r.read_int32())
        return cls(hash=hash, packs=packs, stickers=stickers, dates=dates)


@register_tl
class MessagesArchivedStickers(TLObject):
    ID: int = 0x4fcba9c8

    def __init__(self, count: Any = None, sets: Any = None) -> None:
        self.count = count
        self.sets = sets

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.sets or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesArchivedStickers':
        count = reader.read_int32()
        sets = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, sets=sets)


@register_tl
class MessagesStickerSetInstallResultSuccess(TLObject):
    ID: int = 0x38641628

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStickerSetInstallResultSuccess':
        return cls()


@register_tl
class MessagesStickerSetInstallResultArchive(TLObject):
    ID: int = 0x35e410a8

    def __init__(self, sets: Any = None) -> None:
        self.sets = sets

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.sets or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStickerSetInstallResultArchive':
        sets = reader.read_vector(lambda r: reader.read_object())
        return cls(sets=sets)


@register_tl
class StickerSetCovered(TLObject):
    ID: int = 0x6410a5d2

    def __init__(self, set: Any = None, cover: Any = None) -> None:
        self.set = set
        self.cover = cover

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.set is not None and hasattr(self.set, 'write'): self.set.write(writer)
        if self.cover is not None and hasattr(self.cover, 'write'): self.cover.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickerSetCovered':
        set = reader.read_object()
        cover = reader.read_object()
        return cls(set=set, cover=cover)


@register_tl
class StickerSetMultiCovered(TLObject):
    ID: int = 0x3407e51b

    def __init__(self, set: Any = None, covers: Any = None) -> None:
        self.set = set
        self.covers = covers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.set is not None and hasattr(self.set, 'write'): self.set.write(writer)
        writer.write_vector(self.covers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickerSetMultiCovered':
        set = reader.read_object()
        covers = reader.read_vector(lambda r: reader.read_object())
        return cls(set=set, covers=covers)


@register_tl
class StickerSetFullCovered(TLObject):
    ID: int = 0x40d13c0e

    def __init__(self, set: Any = None, packs: Any = None, keywords: Any = None, documents: Any = None) -> None:
        self.set = set
        self.packs = packs
        self.keywords = keywords
        self.documents = documents

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.set is not None and hasattr(self.set, 'write'): self.set.write(writer)
        writer.write_vector(self.packs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.keywords or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickerSetFullCovered':
        set = reader.read_object()
        packs = reader.read_vector(lambda r: reader.read_object())
        keywords = reader.read_vector(lambda r: reader.read_object())
        documents = reader.read_vector(lambda r: reader.read_object())
        return cls(set=set, packs=packs, keywords=keywords, documents=documents)


@register_tl
class StickerSetNoCovered(TLObject):
    ID: int = 0x77b15d1c

    def __init__(self, set: Any = None) -> None:
        self.set = set

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.set is not None and hasattr(self.set, 'write'): self.set.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickerSetNoCovered':
        set = reader.read_object()
        return cls(set=set)


@register_tl
class MaskCoords(TLObject):
    ID: int = 0xaed6dbb2

    def __init__(self, n: Any = None, x: Any = None, y: Any = None, zoom: Any = None) -> None:
        self.n = n
        self.x = x
        self.y = y
        self.zoom = zoom

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.n or 0)
        writer.write_double(self.x or 0.0)
        writer.write_double(self.y or 0.0)
        writer.write_double(self.zoom or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MaskCoords':
        n = reader.read_int32()
        x = reader.read_double()
        y = reader.read_double()
        zoom = reader.read_double()
        return cls(n=n, x=x, y=y, zoom=zoom)


@register_tl
class InputStickeredMediaPhoto(TLObject):
    ID: int = 0x4a992157

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickeredMediaPhoto':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class InputStickeredMediaDocument(TLObject):
    ID: int = 0x438865b

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickeredMediaDocument':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class Game(TLObject):
    ID: int = 0xbdf9653b

    def __init__(self, document: Any = None, id: Any = None, access_hash: Any = None, short_name: Any = None, title: Any = None, description: Any = None, photo: Any = None) -> None:
        self.document = document
        self.id = id
        self.access_hash = access_hash
        self.short_name = short_name
        self.title = title
        self.description = description
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.document is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_string(self.short_name or '')
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'Game':
        flags = reader.read_uint32()
        id = reader.read_int64()
        access_hash = reader.read_int64()
        short_name = reader.read_string()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object()
        document = reader.read_object() if (flags & (1 << 0)) else None
        return cls(id=id, access_hash=access_hash, short_name=short_name, title=title, description=description, photo=photo, document=document)


@register_tl
class InputGameID(TLObject):
    ID: int = 0x32c3e77

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGameID':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputGameShortName(TLObject):
    ID: int = 0xc331e80a

    def __init__(self, bot_id: Any = None, short_name: Any = None) -> None:
        self.bot_id = bot_id
        self.short_name = short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot_id is not None and hasattr(self.bot_id, 'write'): self.bot_id.write(writer)
        writer.write_string(self.short_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGameShortName':
        bot_id = reader.read_object()
        short_name = reader.read_string()
        return cls(bot_id=bot_id, short_name=short_name)


@register_tl
class HighScore(TLObject):
    ID: int = 0x73a379eb

    def __init__(self, pos: Any = None, user_id: Any = None, score: Any = None) -> None:
        self.pos = pos
        self.user_id = user_id
        self.score = score

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pos or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.score or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HighScore':
        pos = reader.read_int32()
        user_id = reader.read_int64()
        score = reader.read_int32()
        return cls(pos=pos, user_id=user_id, score=score)


@register_tl
class MessagesHighScores(TLObject):
    ID: int = 0x9a3bfd99

    def __init__(self, scores: Any = None, users: Any = None) -> None:
        self.scores = scores
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.scores or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesHighScores':
        scores = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(scores=scores, users=users)


@register_tl
class TextEmpty(TLObject):
    ID: int = 0xdc3d824f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextEmpty':
        return cls()


@register_tl
class TextPlain(TLObject):
    ID: int = 0x744694e0

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'TextPlain':
        text = reader.read_string()
        return cls(text=text)


@register_tl
class TextBold(TLObject):
    ID: int = 0x6724abc4

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextBold':
        text = reader.read_object()
        return cls(text=text)

