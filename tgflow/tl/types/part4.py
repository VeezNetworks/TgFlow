from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl

@register_tl
class InputMessagesFilterChatPhotos(TLObject):
    ID: int = 0x3a20ecb8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterChatPhotos':
        return cls()
@register_tl
class InputMessagesFilterPhoneCalls(TLObject):
    ID: int = 0x80c99768

    def __init__(self, missed: bool = False) -> None:
        self.missed = missed

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.missed:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPhoneCalls':
        flags = reader.read_uint32()
        missed = bool(flags & (1 << 0))
        return cls(missed=missed)
@register_tl
class InputMessagesFilterRoundVoice(TLObject):
    ID: int = 0x7a7c17a4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterRoundVoice':
        return cls()
@register_tl
class InputMessagesFilterRoundVideo(TLObject):
    ID: int = 0xb549da53

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterRoundVideo':
        return cls()
@register_tl
class InputMessagesFilterMyMentions(TLObject):
    ID: int = 0xc1f8e69a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterMyMentions':
        return cls()
@register_tl
class InputMessagesFilterGeo(TLObject):
    ID: int = 0xe7026d0d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterGeo':
        return cls()
@register_tl
class InputMessagesFilterContacts(TLObject):
    ID: int = 0xe062db83

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterContacts':
        return cls()
@register_tl
class InputMessagesFilterPinned(TLObject):
    ID: int = 0x1bb00451

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPinned':
        return cls()
@register_tl
class InputMessagesFilterPoll(TLObject):
    ID: int = 0xfa2bc90a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPoll':
        return cls()
@register_tl
class UpdateNewMessage(TLObject):
    ID: int = 0x1f2b0afd

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)
@register_tl
class UpdateMessageID(TLObject):
    ID: int = 0x4e90bfd6

    def __init__(self, id: Any = None, random_id: Any = None) -> None:
        self.id = id
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.random_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessageID':
        id = reader.read_int32()
        random_id = reader.read_int64()
        return cls(id=id, random_id=random_id)
@register_tl
class UpdateDeleteMessages(TLObject):
    ID: int = 0xa20db0e5

    def __init__(self, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteMessages':
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(messages=messages, pts=pts, pts_count=pts_count)
@register_tl
class UpdateUserTyping(TLObject):
    ID: int = 0x2a17bf5c

    def __init__(self, user_id: Any = None, top_msg_id: Any = None, action: Any = None) -> None:
        self.user_id = user_id
        self.top_msg_id = top_msg_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserTyping':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        action = reader.read_object()
        return cls(user_id=user_id, top_msg_id=top_msg_id, action=action)
@register_tl
class UpdateChatUserTyping(TLObject):
    ID: int = 0x83487af0

    def __init__(self, chat_id: Any = None, from_id: Any = None, action: Any = None) -> None:
        self.chat_id = chat_id
        self.from_id = from_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        if hasattr(self.from_id, 'write'):
            self.from_id.write(writer)
        else:
            writer.write_bytes(self.from_id or b'')
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatUserTyping':
        chat_id = reader.read_int64()
        from_id = reader.read_object()
        action = reader.read_object()
        return cls(chat_id=chat_id, from_id=from_id, action=action)
@register_tl
class UpdateChatParticipants(TLObject):
    ID: int = 0x7761198

    def __init__(self, participants: Any = None) -> None:
        self.participants = participants

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.participants, 'write'):
            self.participants.write(writer)
        else:
            writer.write_bytes(self.participants or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipants':
        participants = reader.read_object()
        return cls(participants=participants)
@register_tl
class UpdateUserStatus(TLObject):
    ID: int = 0xe5bdf8de

    def __init__(self, user_id: Any = None, status: Any = None) -> None:
        self.user_id = user_id
        self.status = status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.status, 'write'):
            self.status.write(writer)
        else:
            writer.write_bytes(self.status or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserStatus':
        user_id = reader.read_int64()
        status = reader.read_object()
        return cls(user_id=user_id, status=status)
@register_tl
class UpdateUserName(TLObject):
    ID: int = 0xa7848924

    def __init__(self, user_id: Any = None, first_name: Any = None, last_name: Any = None, usernames: Any = None) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.usernames = usernames

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.first_name or ''))
        writer.write_string(str(self.last_name or ''))
        writer.write_vector(self.usernames or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserName':
        user_id = reader.read_int64()
        first_name = reader.read_string()
        last_name = reader.read_string()
        usernames = reader.read_vector(lambda r: r.read_object())
        return cls(user_id=user_id, first_name=first_name, last_name=last_name, usernames=usernames)
@register_tl
class UpdateNewAuthorization(TLObject):
    ID: int = 0x8951abef

    def __init__(self, unconfirmed: bool = False, hash: Any = None, date: Any = None, device: Any = None, location: Any = None) -> None:
        self.unconfirmed = unconfirmed
        self.hash = hash
        self.date = date
        self.device = device
        self.location = location

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unconfirmed:
            flags |= (1 << 0)
        if self.date is not None:
            flags |= (1 << 0)
        if self.device is not None:
            flags |= (1 << 0)
        if self.location is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)
        if self.date is not None:
            writer.write_int32(self.date or 0)
        if self.device is not None:
            writer.write_string(str(self.device or ''))
        if self.location is not None:
            writer.write_string(str(self.location or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewAuthorization':
        flags = reader.read_uint32()
        unconfirmed = bool(flags & (1 << 0))
        hash = reader.read_int64()
        date = None
        if flags & (1 << 0):
            date = reader.read_int32()
        device = None
        if flags & (1 << 0):
            device = reader.read_string()
        location = None
        if flags & (1 << 0):
            location = reader.read_string()
        return cls(unconfirmed=unconfirmed, hash=hash, date=date, device=device, location=location)
@register_tl
class UpdateNewEncryptedMessage(TLObject):
    ID: int = 0x12bcbd9a

    def __init__(self, message: Any = None, qts: Any = None) -> None:
        self.message = message
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewEncryptedMessage':
        message = reader.read_object()
        qts = reader.read_int32()
        return cls(message=message, qts=qts)
@register_tl
class UpdateEncryptedChatTyping(TLObject):
    ID: int = 0x1710f156

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryptedChatTyping':
        chat_id = reader.read_int32()
        return cls(chat_id=chat_id)
@register_tl
class UpdateEncryption(TLObject):
    ID: int = 0xb4a2e88d

    def __init__(self, chat: Any = None, date: Any = None) -> None:
        self.chat = chat
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.chat, 'write'):
            self.chat.write(writer)
        else:
            writer.write_bytes(self.chat or b'')
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryption':
        chat = reader.read_object()
        date = reader.read_int32()
        return cls(chat=chat, date=date)
@register_tl
class UpdateEncryptedMessagesRead(TLObject):
    ID: int = 0x38fe25b7

    def __init__(self, chat_id: Any = None, max_date: Any = None, date: Any = None) -> None:
        self.chat_id = chat_id
        self.max_date = max_date
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.chat_id or 0)
        writer.write_int32(self.max_date or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryptedMessagesRead':
        chat_id = reader.read_int32()
        max_date = reader.read_int32()
        date = reader.read_int32()
        return cls(chat_id=chat_id, max_date=max_date, date=date)
@register_tl
class UpdateChatParticipantAdd(TLObject):
    ID: int = 0x3dda5451

    def __init__(self, chat_id: Any = None, user_id: Any = None, inviter_id: Any = None, date: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantAdd':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, inviter_id=inviter_id, date=date, version=version)
@register_tl
class UpdateChatParticipantDelete(TLObject):
    ID: int = 0xe32f3d77

    def __init__(self, chat_id: Any = None, user_id: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantDelete':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, version=version)
@register_tl
class UpdateDcOptions(TLObject):
    ID: int = 0x8e5e9873

    def __init__(self, dc_options: Any = None) -> None:
        self.dc_options = dc_options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dc_options or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDcOptions':
        dc_options = reader.read_vector(lambda r: r.read_object())
        return cls(dc_options=dc_options)
@register_tl
class UpdateNotifySettings(TLObject):
    ID: int = 0xbec268ef

    def __init__(self, peer: Any = None, notify_settings: Any = None) -> None:
        self.peer = peer
        self.notify_settings = notify_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNotifySettings':
        peer = reader.read_object()
        notify_settings = reader.read_object()
        return cls(peer=peer, notify_settings=notify_settings)
@register_tl
class UpdateServiceNotification(TLObject):
    ID: int = 0xebe46819

    def __init__(self, popup: bool = False, invert_media: bool = False, inbox_date: Any = None, type: Any = None, message: Any = None, media: Any = None, entities: Any = None) -> None:
        self.popup = popup
        self.invert_media = invert_media
        self.inbox_date = inbox_date
        self.type = type
        self.message = message
        self.media = media
        self.entities = entities

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.popup:
            flags |= (1 << 0)
        if self.invert_media:
            flags |= (1 << 2)
        if self.inbox_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.inbox_date is not None:
            writer.write_int32(self.inbox_date or 0)
        writer.write_string(str(self.type or ''))
        writer.write_string(str(self.message or ''))
        if hasattr(self.media, 'write'):
            self.media.write(writer)
        else:
            writer.write_bytes(self.media or b'')
        writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateServiceNotification':
        flags = reader.read_uint32()
        popup = bool(flags & (1 << 0))
        invert_media = bool(flags & (1 << 2))
        inbox_date = None
        if flags & (1 << 1):
            inbox_date = reader.read_int32()
        type = reader.read_string()
        message = reader.read_string()
        media = reader.read_object()
        entities = reader.read_vector(lambda r: r.read_object())
        return cls(popup=popup, invert_media=invert_media, inbox_date=inbox_date, type=type, message=message, media=media, entities=entities)
@register_tl
class UpdatePrivacy(TLObject):
    ID: int = 0xee3b272a

    def __init__(self, key: Any = None, rules: Any = None) -> None:
        self.key = key
        self.rules = rules

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.key, 'write'):
            self.key.write(writer)
        else:
            writer.write_bytes(self.key or b'')
        writer.write_vector(self.rules or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePrivacy':
        key = reader.read_object()
        rules = reader.read_vector(lambda r: r.read_object())
        return cls(key=key, rules=rules)
@register_tl
class UpdateUserPhone(TLObject):
    ID: int = 0x5492a13

    def __init__(self, user_id: Any = None, phone: Any = None) -> None:
        self.user_id = user_id
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.phone or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserPhone':
        user_id = reader.read_int64()
        phone = reader.read_string()
        return cls(user_id=user_id, phone=phone)
@register_tl
class UpdateReadHistoryInbox(TLObject):
    ID: int = 0x9e84bc99

    def __init__(self, folder_id: Any = None, peer: Any = None, top_msg_id: Any = None, max_id: Any = None, still_unread_count: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.folder_id = folder_id
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.max_id = max_id
        self.still_unread_count = still_unread_count
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 0)
        if self.top_msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.still_unread_count or 0)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadHistoryInbox':
        flags = reader.read_uint32()
        folder_id = None
        if flags & (1 << 0):
            folder_id = reader.read_int32()
        peer = reader.read_object()
        top_msg_id = None
        if flags & (1 << 1):
            top_msg_id = reader.read_int32()
        max_id = reader.read_int32()
        still_unread_count = reader.read_int32()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(folder_id=folder_id, peer=peer, top_msg_id=top_msg_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts, pts_count=pts_count)
@register_tl
class UpdateReadHistoryOutbox(TLObject):
    ID: int = 0x2f2f21bf

    def __init__(self, peer: Any = None, max_id: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.peer = peer
        self.max_id = max_id
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadHistoryOutbox':
        peer = reader.read_object()
        max_id = reader.read_int32()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(peer=peer, max_id=max_id, pts=pts, pts_count=pts_count)
@register_tl
class UpdateWebPage(TLObject):
    ID: int = 0x7f891213

    def __init__(self, webpage: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.webpage, 'write'):
            self.webpage.write(writer)
        else:
            writer.write_bytes(self.webpage or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateWebPage':
        webpage = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(webpage=webpage, pts=pts, pts_count=pts_count)
@register_tl
class UpdateReadMessagesContents(TLObject):
    ID: int = 0xf8227181

    def __init__(self, messages: Any = None, pts: Any = None, pts_count: Any = None, date: Any = None) -> None:
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.date is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        if self.date is not None:
            writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadMessagesContents':
        flags = reader.read_uint32()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        date = None
        if flags & (1 << 0):
            date = reader.read_int32()
        return cls(messages=messages, pts=pts, pts_count=pts_count, date=date)
@register_tl
class UpdateChannelTooLong(TLObject):
    ID: int = 0x108d941f

    def __init__(self, channel_id: Any = None, pts: Any = None) -> None:
        self.channel_id = channel_id
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pts is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.pts is not None:
            writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelTooLong':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        pts = None
        if flags & (1 << 0):
            pts = reader.read_int32()
        return cls(channel_id=channel_id, pts=pts)
@register_tl
class UpdateChannel(TLObject):
    ID: int = 0x635b4c09

    def __init__(self, channel_id: Any = None) -> None:
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannel':
        channel_id = reader.read_int64()
        return cls(channel_id=channel_id)
@register_tl
class UpdateNewChannelMessage(TLObject):
    ID: int = 0x62ba04d9

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewChannelMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)
@register_tl
class UpdateReadChannelInbox(TLObject):
    ID: int = 0x922e6e10

    def __init__(self, folder_id: Any = None, channel_id: Any = None, max_id: Any = None, still_unread_count: Any = None, pts: Any = None) -> None:
        self.folder_id = folder_id
        self.channel_id = channel_id
        self.max_id = max_id
        self.still_unread_count = still_unread_count
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.still_unread_count or 0)
        writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelInbox':
        flags = reader.read_uint32()
        folder_id = None
        if flags & (1 << 0):
            folder_id = reader.read_int32()
        channel_id = reader.read_int64()
        max_id = reader.read_int32()
        still_unread_count = reader.read_int32()
        pts = reader.read_int32()
        return cls(folder_id=folder_id, channel_id=channel_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts)
@register_tl
class UpdateDeleteChannelMessages(TLObject):
    ID: int = 0xc32d5b12

    def __init__(self, channel_id: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.channel_id = channel_id
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteChannelMessages':
        channel_id = reader.read_int64()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count)
@register_tl
class UpdateChannelMessageViews(TLObject):
    ID: int = 0xf226ac08

    def __init__(self, channel_id: Any = None, id: Any = None, views: Any = None) -> None:
        self.channel_id = channel_id
        self.id = id
        self.views = views

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.views or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelMessageViews':
        channel_id = reader.read_int64()
        id = reader.read_int32()
        views = reader.read_int32()
        return cls(channel_id=channel_id, id=id, views=views)
@register_tl
class UpdateChatParticipantAdmin(TLObject):
    ID: int = 0xd7ca61a2

    def __init__(self, chat_id: Any = None, user_id: Any = None, is_admin: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bool(bool(self.is_admin))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantAdmin':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        is_admin = reader.read_bool()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, is_admin=is_admin, version=version)
@register_tl
class UpdateNewStickerSet(TLObject):
    ID: int = 0x688a30aa

    def __init__(self, stickerset: Any = None) -> None:
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.stickerset, 'write'):
            self.stickerset.write(writer)
        else:
            writer.write_bytes(self.stickerset or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewStickerSet':
        stickerset = reader.read_object()
        return cls(stickerset=stickerset)
@register_tl
class UpdateStickerSetsOrder(TLObject):
    ID: int = 0xbb2d201

    def __init__(self, masks: bool = False, emojis: bool = False, order: Any = None) -> None:
        self.masks = masks
        self.emojis = emojis
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStickerSetsOrder':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        order = reader.read_vector(lambda r: r.read_object())
        return cls(masks=masks, emojis=emojis, order=order)
@register_tl
class UpdateStickerSets(TLObject):
    ID: int = 0x31c24808

    def __init__(self, masks: bool = False, emojis: bool = False) -> None:
        self.masks = masks
        self.emojis = emojis

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStickerSets':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        return cls(masks=masks, emojis=emojis)
@register_tl
class UpdateSavedGifs(TLObject):
    ID: int = 0x9375341e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSavedGifs':
        return cls()
@register_tl
class UpdateBotInlineQuery(TLObject):
    ID: int = 0x496f379c

    def __init__(self, query_id: Any = None, user_id: Any = None, query: Any = None, geo: Any = None, peer_type: Any = None, offset: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.query = query
        self.geo = geo
        self.peer_type = peer_type
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo is not None:
            flags |= (1 << 0)
        if self.peer_type is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.query or ''))
        if self.geo is not None:
            if hasattr(self.geo, 'write'):
                self.geo.write(writer)
            else:
                writer.write_bytes(self.geo or b'')
        if self.peer_type is not None:
            if hasattr(self.peer_type, 'write'):
                self.peer_type.write(writer)
            else:
                writer.write_bytes(self.peer_type or b'')
        writer.write_string(str(self.offset or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotInlineQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        query = reader.read_string()
        geo = None
        if flags & (1 << 0):
            geo = reader.read_object()
        peer_type = None
        if flags & (1 << 1):
            peer_type = reader.read_object()
        offset = reader.read_string()
        return cls(query_id=query_id, user_id=user_id, query=query, geo=geo, peer_type=peer_type, offset=offset)
@register_tl
class UpdateBotInlineSend(TLObject):
    ID: int = 0x12f12a07

    def __init__(self, user_id: Any = None, query: Any = None, geo: Any = None, id: Any = None, msg_id: Any = None) -> None:
        self.user_id = user_id
        self.query = query
        self.geo = geo
        self.id = id
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo is not None:
            flags |= (1 << 0)
        if self.msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.query or ''))
        if self.geo is not None:
            if hasattr(self.geo, 'write'):
                self.geo.write(writer)
            else:
                writer.write_bytes(self.geo or b'')
        writer.write_string(str(self.id or ''))
        if self.msg_id is not None:
            if hasattr(self.msg_id, 'write'):
                self.msg_id.write(writer)
            else:
                writer.write_bytes(self.msg_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotInlineSend':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        query = reader.read_string()
        geo = None
        if flags & (1 << 0):
            geo = reader.read_object()
        id = reader.read_string()
        msg_id = None
        if flags & (1 << 1):
            msg_id = reader.read_object()
        return cls(user_id=user_id, query=query, geo=geo, id=id, msg_id=msg_id)
@register_tl
class UpdateEditChannelMessage(TLObject):
    ID: int = 0x1b3f4df7

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEditChannelMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)
@register_tl
class UpdateBotCallbackQuery(TLObject):
    ID: int = 0xb9cfc48d

    def __init__(self, query_id: Any = None, user_id: Any = None, peer: Any = None, msg_id: Any = None, chat_instance: Any = None, data: Any = None, game_short_name: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.peer = peer
        self.msg_id = msg_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.game_short_name is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.chat_instance or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')
        if self.game_short_name is not None:
            writer.write_string(str(self.game_short_name or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotCallbackQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        peer = reader.read_object()
        msg_id = reader.read_int32()
        chat_instance = reader.read_int64()
        data = None
        if flags & (1 << 0):
            data = reader.read_bytes()
        game_short_name = None
        if flags & (1 << 1):
            game_short_name = reader.read_string()
        return cls(query_id=query_id, user_id=user_id, peer=peer, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)
@register_tl
class UpdateEditMessage(TLObject):
    ID: int = 0xe40370a3

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEditMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)
@register_tl
class UpdateInlineBotCallbackQuery(TLObject):
    ID: int = 0x691e9052

    def __init__(self, query_id: Any = None, user_id: Any = None, msg_id: Any = None, chat_instance: Any = None, data: Any = None, game_short_name: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.msg_id = msg_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.game_short_name is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.msg_id, 'write'):
            self.msg_id.write(writer)
        else:
            writer.write_bytes(self.msg_id or b'')
        writer.write_int64(self.chat_instance or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')
        if self.game_short_name is not None:
            writer.write_string(str(self.game_short_name or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateInlineBotCallbackQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        msg_id = reader.read_object()
        chat_instance = reader.read_int64()
        data = None
        if flags & (1 << 0):
            data = reader.read_bytes()
        game_short_name = None
        if flags & (1 << 1):
            game_short_name = reader.read_string()
        return cls(query_id=query_id, user_id=user_id, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)
@register_tl
class UpdateReadChannelOutbox(TLObject):
    ID: int = 0xb75f99a9

    def __init__(self, channel_id: Any = None, max_id: Any = None) -> None:
        self.channel_id = channel_id
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelOutbox':
        channel_id = reader.read_int64()
        max_id = reader.read_int32()
        return cls(channel_id=channel_id, max_id=max_id)
@register_tl
class UpdateDraftMessage(TLObject):
    ID: int = 0xedfc111e

    def __init__(self, peer: Any = None, top_msg_id: Any = None, saved_peer_id: Any = None, draft: Any = None) -> None:
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.draft = draft

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if hasattr(self.draft, 'write'):
            self.draft.write(writer)
        else:
            writer.write_bytes(self.draft or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDraftMessage':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        draft = reader.read_object()
        return cls(peer=peer, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, draft=draft)
@register_tl
class UpdateReadFeaturedStickers(TLObject):
    ID: int = 0x571d2742

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadFeaturedStickers':
        return cls()
@register_tl
class UpdateRecentStickers(TLObject):
    ID: int = 0x9a422c20

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateRecentStickers':
        return cls()
@register_tl
class UpdateConfig(TLObject):
    ID: int = 0xa229dd06

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateConfig':
        return cls()
@register_tl
class UpdatePtsChanged(TLObject):
    ID: int = 0x3354678f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePtsChanged':
        return cls()
@register_tl
class UpdateChannelWebPage(TLObject):
    ID: int = 0x2f2ba99f

    def __init__(self, channel_id: Any = None, webpage: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.channel_id = channel_id
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        if hasattr(self.webpage, 'write'):
            self.webpage.write(writer)
        else:
            writer.write_bytes(self.webpage or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelWebPage':
        channel_id = reader.read_int64()
        webpage = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(channel_id=channel_id, webpage=webpage, pts=pts, pts_count=pts_count)
@register_tl
class UpdateDialogPinned(TLObject):
    ID: int = 0x6e6fe51c

    def __init__(self, pinned: bool = False, folder_id: Any = None, peer: Any = None) -> None:
        self.pinned = pinned
        self.folder_id = folder_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        if self.folder_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogPinned':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        folder_id = None
        if flags & (1 << 1):
            folder_id = reader.read_int32()
        peer = reader.read_object()
        return cls(pinned=pinned, folder_id=folder_id, peer=peer)
@register_tl
class UpdatePinnedDialogs(TLObject):
    ID: int = 0xfa0f3ca2

    def __init__(self, folder_id: Any = None, order: Any = None) -> None:
        self.folder_id = folder_id
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 1)
        if self.order is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.order is not None:
            writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedDialogs':
        flags = reader.read_uint32()
        folder_id = None
        if flags & (1 << 1):
            folder_id = reader.read_int32()
        order = None
        if flags & (1 << 0):
            order = reader.read_vector(lambda r: r.read_object())
        return cls(folder_id=folder_id, order=order)
@register_tl
class UpdateBotWebhookJSON(TLObject):
    ID: int = 0x8317c0c3

    def __init__(self, data: Any = None) -> None:
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.data, 'write'):
            self.data.write(writer)
        else:
            writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotWebhookJSON':
        data = reader.read_object()
        return cls(data=data)
@register_tl
class UpdateBotWebhookJSONQuery(TLObject):
    ID: int = 0x9b9240a6

    def __init__(self, query_id: Any = None, data: Any = None, timeout: Any = None) -> None:
        self.query_id = query_id
        self.data = data
        self.timeout = timeout

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        if hasattr(self.data, 'write'):
            self.data.write(writer)
        else:
            writer.write_bytes(self.data or b'')
        writer.write_int32(self.timeout or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotWebhookJSONQuery':
        query_id = reader.read_int64()
        data = reader.read_object()
        timeout = reader.read_int32()
        return cls(query_id=query_id, data=data, timeout=timeout)
@register_tl
class UpdateBotShippingQuery(TLObject):
    ID: int = 0xb5aefd7d

    def __init__(self, query_id: Any = None, user_id: Any = None, payload: Any = None, shipping_address: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.payload = payload
        self.shipping_address = shipping_address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bytes(self.payload or b'')
        if hasattr(self.shipping_address, 'write'):
            self.shipping_address.write(writer)
        else:
            writer.write_bytes(self.shipping_address or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotShippingQuery':
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        payload = reader.read_bytes()
        shipping_address = reader.read_object()
        return cls(query_id=query_id, user_id=user_id, payload=payload, shipping_address=shipping_address)
@register_tl
class UpdateBotPrecheckoutQuery(TLObject):
    ID: int = 0x8caa9a96

    def __init__(self, query_id: Any = None, user_id: Any = None, payload: Any = None, info: Any = None, shipping_option_id: Any = None, currency: Any = None, total_amount: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.payload = payload
        self.info = info
        self.shipping_option_id = shipping_option_id
        self.currency = currency
        self.total_amount = total_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.info is not None:
            flags |= (1 << 0)
        if self.shipping_option_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bytes(self.payload or b'')
        if self.info is not None:
            if hasattr(self.info, 'write'):
                self.info.write(writer)
            else:
                writer.write_bytes(self.info or b'')
        if self.shipping_option_id is not None:
            writer.write_string(str(self.shipping_option_id or ''))
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotPrecheckoutQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        payload = reader.read_bytes()
        info = None
        if flags & (1 << 0):
            info = reader.read_object()
        shipping_option_id = None
        if flags & (1 << 1):
            shipping_option_id = reader.read_string()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        return cls(query_id=query_id, user_id=user_id, payload=payload, info=info, shipping_option_id=shipping_option_id, currency=currency, total_amount=total_amount)
@register_tl
class UpdatePhoneCall(TLObject):
    ID: int = 0xab0f6b1e

    def __init__(self, phone_call: Any = None) -> None:
        self.phone_call = phone_call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.phone_call, 'write'):
            self.phone_call.write(writer)
        else:
            writer.write_bytes(self.phone_call or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePhoneCall':
        phone_call = reader.read_object()
        return cls(phone_call=phone_call)
@register_tl
class UpdateLangPackTooLong(TLObject):
    ID: int = 0x46560264

    def __init__(self, lang_code: Any = None) -> None:
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.lang_code or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLangPackTooLong':
        lang_code = reader.read_string()
        return cls(lang_code=lang_code)
@register_tl
class UpdateLangPack(TLObject):
    ID: int = 0x56022f4d

    def __init__(self, difference: Any = None) -> None:
        self.difference = difference

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.difference, 'write'):
            self.difference.write(writer)
        else:
            writer.write_bytes(self.difference or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLangPack':
        difference = reader.read_object()
        return cls(difference=difference)
@register_tl
class UpdateFavedStickers(TLObject):
    ID: int = 0xe511996d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateFavedStickers':
        return cls()
@register_tl
class UpdateChannelReadMessagesContents(TLObject):
    ID: int = 0x25f324f7

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, saved_peer_id: Any = None, messages: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelReadMessagesContents':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, messages=messages)
@register_tl
class UpdateContactsReset(TLObject):
    ID: int = 0x7084a7be

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateContactsReset':
        return cls()
@register_tl
class UpdateChannelAvailableMessages(TLObject):
    ID: int = 0xb23fc698

    def __init__(self, channel_id: Any = None, available_min_id: Any = None) -> None:
        self.channel_id = channel_id
        self.available_min_id = available_min_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.available_min_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelAvailableMessages':
        channel_id = reader.read_int64()
        available_min_id = reader.read_int32()
        return cls(channel_id=channel_id, available_min_id=available_min_id)
@register_tl
class UpdateDialogUnreadMark(TLObject):
    ID: int = 0xb658f23e

    def __init__(self, unread: bool = False, peer: Any = None, saved_peer_id: Any = None) -> None:
        self.unread = unread
        self.peer = peer
        self.saved_peer_id = saved_peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unread:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogUnreadMark':
        flags = reader.read_uint32()
        unread = bool(flags & (1 << 0))
        peer = reader.read_object()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        return cls(unread=unread, peer=peer, saved_peer_id=saved_peer_id)
@register_tl
class UpdateMessagePoll(TLObject):
    ID: int = 0xd64c522b

    def __init__(self, peer: Any = None, msg_id: Any = None, top_msg_id: Any = None, poll_id: Any = None, poll: Any = None, results: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.top_msg_id = top_msg_id
        self.poll_id = poll_id
        self.poll = poll
        self.results = results

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer is not None:
            flags |= (1 << 1)
        if self.msg_id is not None:
            flags |= (1 << 1)
        if self.top_msg_id is not None:
            flags |= (1 << 2)
        if self.poll is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int64(self.poll_id or 0)
        if self.poll is not None:
            if hasattr(self.poll, 'write'):
                self.poll.write(writer)
            else:
                writer.write_bytes(self.poll or b'')
        if hasattr(self.results, 'write'):
            self.results.write(writer)
        else:
            writer.write_bytes(self.results or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessagePoll':
        flags = reader.read_uint32()
        peer = None
        if flags & (1 << 1):
            peer = reader.read_object()
        msg_id = None
        if flags & (1 << 1):
            msg_id = reader.read_int32()
        top_msg_id = None
        if flags & (1 << 2):
            top_msg_id = reader.read_int32()
        poll_id = reader.read_int64()
        poll = None
        if flags & (1 << 0):
            poll = reader.read_object()
        results = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, top_msg_id=top_msg_id, poll_id=poll_id, poll=poll, results=results)
@register_tl
class UpdateChatDefaultBannedRights(TLObject):
    ID: int = 0x54c01850

    def __init__(self, peer: Any = None, default_banned_rights: Any = None, version: Any = None) -> None:
        self.peer = peer
        self.default_banned_rights = default_banned_rights
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.default_banned_rights, 'write'):
            self.default_banned_rights.write(writer)
        else:
            writer.write_bytes(self.default_banned_rights or b'')
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatDefaultBannedRights':
        peer = reader.read_object()
        default_banned_rights = reader.read_object()
        version = reader.read_int32()
        return cls(peer=peer, default_banned_rights=default_banned_rights, version=version)
@register_tl
class UpdateFolderPeers(TLObject):
    ID: int = 0x19360dc0

    def __init__(self, folder_peers: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.folder_peers = folder_peers
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.folder_peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateFolderPeers':
        folder_peers = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(folder_peers=folder_peers, pts=pts, pts_count=pts_count)
@register_tl
class UpdatePeerSettings(TLObject):
    ID: int = 0x6a7e7366

    def __init__(self, peer: Any = None, settings: Any = None) -> None:
        self.peer = peer
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.settings, 'write'):
            self.settings.write(writer)
        else:
            writer.write_bytes(self.settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerSettings':
        peer = reader.read_object()
        settings = reader.read_object()
        return cls(peer=peer, settings=settings)
@register_tl
class UpdatePeerLocated(TLObject):
    ID: int = 0xb4afcfb0

    def __init__(self, peers: Any = None) -> None:
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerLocated':
        peers = reader.read_vector(lambda r: r.read_object())
        return cls(peers=peers)
@register_tl
class UpdateNewScheduledMessage(TLObject):
    ID: int = 0x39a51dfb

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewScheduledMessage':
        message = reader.read_object()
        return cls(message=message)
@register_tl
class UpdateDeleteScheduledMessages(TLObject):
    ID: int = 0xf2a71983

    def __init__(self, peer: Any = None, messages: Any = None, sent_messages: Any = None) -> None:
        self.peer = peer
        self.messages = messages
        self.sent_messages = sent_messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sent_messages is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.sent_messages is not None:
            writer.write_vector(self.sent_messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteScheduledMessages':
        flags = reader.read_uint32()
        peer = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        sent_messages = None
        if flags & (1 << 0):
            sent_messages = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, messages=messages, sent_messages=sent_messages)
@register_tl
class UpdateTheme(TLObject):
    ID: int = 0x8216fba3

    def __init__(self, theme: Any = None) -> None:
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.theme, 'write'):
            self.theme.write(writer)
        else:
            writer.write_bytes(self.theme or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateTheme':
        theme = reader.read_object()
        return cls(theme=theme)
@register_tl
class UpdateGeoLiveViewed(TLObject):
    ID: int = 0x871fb939

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGeoLiveViewed':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)
@register_tl
class UpdateLoginToken(TLObject):
    ID: int = 0x564fe691

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLoginToken':
        return cls()
@register_tl
class UpdateMessagePollVote(TLObject):
    ID: int = 0x7699f014

    def __init__(self, poll_id: Any = None, peer: Any = None, options: Any = None, positions: Any = None, qts: Any = None) -> None:
        self.poll_id = poll_id
        self.peer = peer
        self.options = options
        self.positions = positions
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.poll_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_vector(self.options or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.positions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessagePollVote':
        poll_id = reader.read_int64()
        peer = reader.read_object()
        options = reader.read_vector(lambda r: r.read_object())
        positions = reader.read_vector(lambda r: r.read_object())
        qts = reader.read_int32()
        return cls(poll_id=poll_id, peer=peer, options=options, positions=positions, qts=qts)
@register_tl
class UpdateDialogFilter(TLObject):
    ID: int = 0x26ffde7d

    def __init__(self, id: Any = None, filter: Any = None) -> None:
        self.id = id
        self.filter = filter

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.filter is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.filter is not None:
            if hasattr(self.filter, 'write'):
                self.filter.write(writer)
            else:
                writer.write_bytes(self.filter or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilter':
        flags = reader.read_uint32()
        id = reader.read_int32()
        filter = None
        if flags & (1 << 0):
            filter = reader.read_object()
        return cls(id=id, filter=filter)
@register_tl
class UpdateDialogFilterOrder(TLObject):
    ID: int = 0xa5d72105

    def __init__(self, order: Any = None) -> None:
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilterOrder':
        order = reader.read_vector(lambda r: r.read_object())
        return cls(order=order)
@register_tl
class UpdateDialogFilters(TLObject):
    ID: int = 0x3504914f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilters':
        return cls()
@register_tl
class UpdatePhoneCallSignalingData(TLObject):
    ID: int = 0x2661bf09

    def __init__(self, phone_call_id: Any = None, data: Any = None) -> None:
        self.phone_call_id = phone_call_id
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.phone_call_id or 0)
        writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePhoneCallSignalingData':
        phone_call_id = reader.read_int64()
        data = reader.read_bytes()
        return cls(phone_call_id=phone_call_id, data=data)
@register_tl
class UpdateChannelMessageForwards(TLObject):
    ID: int = 0xd29a27f4

    def __init__(self, channel_id: Any = None, id: Any = None, forwards: Any = None) -> None:
        self.channel_id = channel_id
        self.id = id
        self.forwards = forwards

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.forwards or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelMessageForwards':
        channel_id = reader.read_int64()
        id = reader.read_int32()
        forwards = reader.read_int32()
        return cls(channel_id=channel_id, id=id, forwards=forwards)
@register_tl
class UpdateReadChannelDiscussionInbox(TLObject):
    ID: int = 0xd6b19546

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, read_max_id: Any = None, broadcast_id: Any = None, broadcast_post: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.read_max_id = read_max_id
        self.broadcast_id = broadcast_id
        self.broadcast_post = broadcast_post

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast_id is not None:
            flags |= (1 << 0)
        if self.broadcast_post is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.read_max_id or 0)
        if self.broadcast_id is not None:
            writer.write_int64(self.broadcast_id or 0)
        if self.broadcast_post is not None:
            writer.write_int32(self.broadcast_post or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelDiscussionInbox':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        top_msg_id = reader.read_int32()
        read_max_id = reader.read_int32()
        broadcast_id = None
        if flags & (1 << 0):
            broadcast_id = reader.read_int64()
        broadcast_post = None
        if flags & (1 << 0):
            broadcast_post = reader.read_int32()
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, read_max_id=read_max_id, broadcast_id=broadcast_id, broadcast_post=broadcast_post)
@register_tl
class UpdateReadChannelDiscussionOutbox(TLObject):
    ID: int = 0x695c9e7c

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, read_max_id: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.read_max_id = read_max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.read_max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelDiscussionOutbox':
        channel_id = reader.read_int64()
        top_msg_id = reader.read_int32()
        read_max_id = reader.read_int32()
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, read_max_id=read_max_id)
@register_tl
class UpdatePeerBlocked(TLObject):
    ID: int = 0xebe07752

    def __init__(self, blocked: bool = False, blocked_my_stories_from: bool = False, peer_id: Any = None) -> None:
        self.blocked = blocked
        self.blocked_my_stories_from = blocked_my_stories_from
        self.peer_id = peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blocked:
            flags |= (1 << 0)
        if self.blocked_my_stories_from:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer_id, 'write'):
            self.peer_id.write(writer)
        else:
            writer.write_bytes(self.peer_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerBlocked':
        flags = reader.read_uint32()
        blocked = bool(flags & (1 << 0))
        blocked_my_stories_from = bool(flags & (1 << 1))
        peer_id = reader.read_object()
        return cls(blocked=blocked, blocked_my_stories_from=blocked_my_stories_from, peer_id=peer_id)
@register_tl
class UpdateChannelUserTyping(TLObject):
    ID: int = 0x8c88c923

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, from_id: Any = None, action: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.from_id = from_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if hasattr(self.from_id, 'write'):
            self.from_id.write(writer)
        else:
            writer.write_bytes(self.from_id or b'')
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelUserTyping':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        from_id = reader.read_object()
        action = reader.read_object()
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, from_id=from_id, action=action)
@register_tl
class UpdatePinnedMessages(TLObject):
    ID: int = 0xed85eab5

    def __init__(self, pinned: bool = False, peer: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.pinned = pinned
        self.peer = peer
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedMessages':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        peer = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(pinned=pinned, peer=peer, messages=messages, pts=pts, pts_count=pts_count)
@register_tl
class UpdatePinnedChannelMessages(TLObject):
    ID: int = 0x5bb98608

    def __init__(self, pinned: bool = False, channel_id: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.pinned = pinned
        self.channel_id = channel_id
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedChannelMessages':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        channel_id = reader.read_int64()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(pinned=pinned, channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count)
@register_tl
class UpdateChat(TLObject):
    ID: int = 0xf89a6a4e

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChat':
        chat_id = reader.read_int64()
        return cls(chat_id=chat_id)
@register_tl
class UpdateGroupCallParticipants(TLObject):
    ID: int = 0xf2ebdb4e

    def __init__(self, call: Any = None, participants: Any = None, version: Any = None) -> None:
        self.call = call
        self.participants = participants
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        writer.write_vector(self.participants or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCallParticipants':
        call = reader.read_object()
        participants = reader.read_vector(lambda r: r.read_object())
        version = reader.read_int32()
        return cls(call=call, participants=participants, version=version)
@register_tl
class UpdateGroupCall(TLObject):
    ID: int = 0x9d2216e0

    def __init__(self, live_story: bool = False, peer: Any = None, call: Any = None) -> None:
        self.live_story = live_story
        self.peer = peer
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.live_story:
            flags |= (1 << 2)
        if self.peer is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCall':
        flags = reader.read_uint32()
        live_story = bool(flags & (1 << 2))
        peer = None
        if flags & (1 << 1):
            peer = reader.read_object()
        call = reader.read_object()
        return cls(live_story=live_story, peer=peer, call=call)
@register_tl
class UpdatePeerHistoryTTL(TLObject):
    ID: int = 0xbb9bb9a5

    def __init__(self, peer: Any = None, ttl_period: Any = None) -> None:
        self.peer = peer
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ttl_period is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerHistoryTTL':
        flags = reader.read_uint32()
        peer = reader.read_object()
        ttl_period = None
        if flags & (1 << 0):
            ttl_period = reader.read_int32()
        return cls(peer=peer, ttl_period=ttl_period)
@register_tl
class UpdateChatParticipant(TLObject):
    ID: int = 0xd087663a

    def __init__(self, chat_id: Any = None, date: Any = None, actor_id: Any = None, user_id: Any = None, prev_participant: Any = None, new_participant: Any = None, invite: Any = None, qts: Any = None) -> None:
        self.chat_id = chat_id
        self.date = date
        self.actor_id = actor_id
        self.user_id = user_id
        self.prev_participant = prev_participant
        self.new_participant = new_participant
        self.invite = invite
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.prev_participant is not None:
            flags |= (1 << 0)
        if self.new_participant is not None:
            flags |= (1 << 1)
        if self.invite is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.chat_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.actor_id or 0)
        writer.write_int64(self.user_id or 0)
        if self.prev_participant is not None:
            if hasattr(self.prev_participant, 'write'):
                self.prev_participant.write(writer)
            else:
                writer.write_bytes(self.prev_participant or b'')
        if self.new_participant is not None:
            if hasattr(self.new_participant, 'write'):
                self.new_participant.write(writer)
            else:
                writer.write_bytes(self.new_participant or b'')
        if self.invite is not None:
            if hasattr(self.invite, 'write'):
                self.invite.write(writer)
            else:
                writer.write_bytes(self.invite or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipant':
        flags = reader.read_uint32()
        chat_id = reader.read_int64()
        date = reader.read_int32()
        actor_id = reader.read_int64()
        user_id = reader.read_int64()
        prev_participant = None
        if flags & (1 << 0):
            prev_participant = reader.read_object()
        new_participant = None
        if flags & (1 << 1):
            new_participant = reader.read_object()
        invite = None
        if flags & (1 << 2):
            invite = reader.read_object()
        qts = reader.read_int32()
        return cls(chat_id=chat_id, date=date, actor_id=actor_id, user_id=user_id, prev_participant=prev_participant, new_participant=new_participant, invite=invite, qts=qts)
@register_tl
class UpdateChannelParticipant(TLObject):
    ID: int = 0x985d3abb

    def __init__(self, via_chatlist: bool = False, channel_id: Any = None, date: Any = None, actor_id: Any = None, user_id: Any = None, prev_participant: Any = None, new_participant: Any = None, invite: Any = None, qts: Any = None) -> None:
        self.via_chatlist = via_chatlist
        self.channel_id = channel_id
        self.date = date
        self.actor_id = actor_id
        self.user_id = user_id
        self.prev_participant = prev_participant
        self.new_participant = new_participant
        self.invite = invite
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_chatlist:
            flags |= (1 << 3)
        if self.prev_participant is not None:
            flags |= (1 << 0)
        if self.new_participant is not None:
            flags |= (1 << 1)
        if self.invite is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.actor_id or 0)
        writer.write_int64(self.user_id or 0)
        if self.prev_participant is not None:
            if hasattr(self.prev_participant, 'write'):
                self.prev_participant.write(writer)
            else:
                writer.write_bytes(self.prev_participant or b'')
        if self.new_participant is not None:
            if hasattr(self.new_participant, 'write'):
                self.new_participant.write(writer)
            else:
                writer.write_bytes(self.new_participant or b'')
        if self.invite is not None:
            if hasattr(self.invite, 'write'):
                self.invite.write(writer)
            else:
                writer.write_bytes(self.invite or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelParticipant':
        flags = reader.read_uint32()
        via_chatlist = bool(flags & (1 << 3))
        channel_id = reader.read_int64()
        date = reader.read_int32()
        actor_id = reader.read_int64()
        user_id = reader.read_int64()
        prev_participant = None
        if flags & (1 << 0):
            prev_participant = reader.read_object()
        new_participant = None
        if flags & (1 << 1):
            new_participant = reader.read_object()
        invite = None
        if flags & (1 << 2):
            invite = reader.read_object()
        qts = reader.read_int32()
        return cls(via_chatlist=via_chatlist, channel_id=channel_id, date=date, actor_id=actor_id, user_id=user_id, prev_participant=prev_participant, new_participant=new_participant, invite=invite, qts=qts)
@register_tl
class UpdateBotStopped(TLObject):
    ID: int = 0xc4870a49

    def __init__(self, user_id: Any = None, date: Any = None, stopped: Any = None, qts: Any = None) -> None:
        self.user_id = user_id
        self.date = date
        self.stopped = stopped
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_bool(bool(self.stopped))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotStopped':
        user_id = reader.read_int64()
        date = reader.read_int32()
        stopped = reader.read_bool()
        qts = reader.read_int32()
        return cls(user_id=user_id, date=date, stopped=stopped, qts=qts)
@register_tl
class UpdateGroupCallConnection(TLObject):
    ID: int = 0xb783982

    def __init__(self, presentation: bool = False, params: Any = None) -> None:
        self.presentation = presentation
        self.params = params

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.presentation:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.params, 'write'):
            self.params.write(writer)
        else:
            writer.write_bytes(self.params or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCallConnection':
        flags = reader.read_uint32()
        presentation = bool(flags & (1 << 0))
        params = reader.read_object()
        return cls(presentation=presentation, params=params)
@register_tl
class UpdateBotCommands(TLObject):
    ID: int = 0x4d712f2e

    def __init__(self, peer: Any = None, bot_id: Any = None, commands: Any = None) -> None:
        self.peer = peer
        self.bot_id = bot_id
        self.commands = commands

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int64(self.bot_id or 0)
        writer.write_vector(self.commands or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotCommands':
        peer = reader.read_object()
        bot_id = reader.read_int64()
        commands = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, bot_id=bot_id, commands=commands)
@register_tl
class UpdatePendingJoinRequests(TLObject):
    ID: int = 0x7063c3db

    def __init__(self, peer: Any = None, requests_pending: Any = None, recent_requesters: Any = None) -> None:
        self.peer = peer
        self.requests_pending = requests_pending
        self.recent_requesters = recent_requesters

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.requests_pending or 0)
        writer.write_vector(self.recent_requesters or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePendingJoinRequests':
        peer = reader.read_object()
        requests_pending = reader.read_int32()
        recent_requesters = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, requests_pending=requests_pending, recent_requesters=recent_requesters)
@register_tl
class UpdateBotChatInviteRequester(TLObject):
    ID: int = 0x11dfa986

    def __init__(self, peer: Any = None, date: Any = None, user_id: Any = None, about: Any = None, invite: Any = None, qts: Any = None) -> None:
        self.peer = peer
        self.date = date
        self.user_id = user_id
        self.about = about
        self.invite = invite
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.date or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.about or ''))
        if hasattr(self.invite, 'write'):
            self.invite.write(writer)
        else:
            writer.write_bytes(self.invite or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotChatInviteRequester':
        peer = reader.read_object()
        date = reader.read_int32()
        user_id = reader.read_int64()
        about = reader.read_string()
        invite = reader.read_object()
        qts = reader.read_int32()
        return cls(peer=peer, date=date, user_id=user_id, about=about, invite=invite, qts=qts)
@register_tl
class UpdateMessageReactions(TLObject):
    ID: int = 0x1e297bfa

    def __init__(self, peer: Any = None, msg_id: Any = None, top_msg_id: Any = None, saved_peer_id: Any = None, reactions: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.reactions = reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if hasattr(self.reactions, 'write'):
            self.reactions.write(writer)
        else:
            writer.write_bytes(self.reactions or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessageReactions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        msg_id = reader.read_int32()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        reactions = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, reactions=reactions)
@register_tl
class UpdateAttachMenuBots(TLObject):
    ID: int = 0x17b7a20b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateAttachMenuBots':
        return cls()
@register_tl
class UpdateWebViewResultSent(TLObject):
    ID: int = 0x1592b79d

    def __init__(self, query_id: Any = None) -> None:
        self.query_id = query_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateWebViewResultSent':
        query_id = reader.read_int64()
        return cls(query_id=query_id)
@register_tl
class UpdateBotMenuButton(TLObject):
    ID: int = 0x14b85813

    def __init__(self, bot_id: Any = None, button: Any = None) -> None:
        self.bot_id = bot_id
        self.button = button

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bot_id or 0)
        if hasattr(self.button, 'write'):
            self.button.write(writer)
        else:
            writer.write_bytes(self.button or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotMenuButton':
        bot_id = reader.read_int64()
        button = reader.read_object()
        return cls(bot_id=bot_id, button=button)
@register_tl
class UpdateSavedRingtones(TLObject):
    ID: int = 0x74d8be99

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSavedRingtones':
        return cls()
@register_tl
class UpdateTranscribedAudio(TLObject):
    ID: int = 0x84cd5a

    def __init__(self, pending: bool = False, peer: Any = None, msg_id: Any = None, transcription_id: Any = None, text: Any = None) -> None:
        self.pending = pending
        self.peer = peer
        self.msg_id = msg_id
        self.transcription_id = transcription_id
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pending:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.transcription_id or 0)
        writer.write_string(str(self.text or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateTranscribedAudio':
        flags = reader.read_uint32()
        pending = bool(flags & (1 << 0))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        transcription_id = reader.read_int64()
        text = reader.read_string()
        return cls(pending=pending, peer=peer, msg_id=msg_id, transcription_id=transcription_id, text=text)
@register_tl
class UpdateReadFeaturedEmojiStickers(TLObject):
    ID: int = 0xfb4c496c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadFeaturedEmojiStickers':
        return cls()
@register_tl
class UpdateUserEmojiStatus(TLObject):
    ID: int = 0x28373599

    def __init__(self, user_id: Any = None, emoji_status: Any = None) -> None:
        self.user_id = user_id
        self.emoji_status = emoji_status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.emoji_status, 'write'):
            self.emoji_status.write(writer)
        else:
            writer.write_bytes(self.emoji_status or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserEmojiStatus':
        user_id = reader.read_int64()
        emoji_status = reader.read_object()
        return cls(user_id=user_id, emoji_status=emoji_status)
@register_tl
class UpdateRecentEmojiStatuses(TLObject):
    ID: int = 0x30f443db

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateRecentEmojiStatuses':
        return cls()
@register_tl
class UpdateRecentReactions(TLObject):
    ID: int = 0x6f7863f4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateRecentReactions':
        return cls()
@register_tl
class UpdateMoveStickerSetToTop(TLObject):
    ID: int = 0x86fccf85

    def __init__(self, masks: bool = False, emojis: bool = False, stickerset: Any = None) -> None:
        self.masks = masks
        self.emojis = emojis
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.stickerset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMoveStickerSetToTop':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        stickerset = reader.read_int64()
        return cls(masks=masks, emojis=emojis, stickerset=stickerset)
@register_tl
class UpdateMessageExtendedMedia(TLObject):
    ID: int = 0xd5a41724

    def __init__(self, peer: Any = None, msg_id: Any = None, extended_media: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.extended_media = extended_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_vector(self.extended_media or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessageExtendedMedia':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        extended_media = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, msg_id=msg_id, extended_media=extended_media)
@register_tl
class UpdateUser(TLObject):
    ID: int = 0x20529438

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUser':
        user_id = reader.read_int64()
        return cls(user_id=user_id)
@register_tl
class UpdateAutoSaveSettings(TLObject):
    ID: int = 0xec05b097

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateAutoSaveSettings':
        return cls()
@register_tl
class UpdateStory(TLObject):
    ID: int = 0x75b3b798

    def __init__(self, peer: Any = None, story: Any = None) -> None:
        self.peer = peer
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.story, 'write'):
            self.story.write(writer)
        else:
            writer.write_bytes(self.story or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStory':
        peer = reader.read_object()
        story = reader.read_object()
        return cls(peer=peer, story=story)
@register_tl
class UpdateReadStories(TLObject):
    ID: int = 0xf74e932b

    def __init__(self, peer: Any = None, max_id: Any = None) -> None:
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadStories':
        peer = reader.read_object()
        max_id = reader.read_int32()
        return cls(peer=peer, max_id=max_id)
