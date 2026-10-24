from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class ContactsGetStatuses(TLRequest):
    ID: int = 0xc4a353ee

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetStatuses':
        return cls()


@register_tl
class ContactsGetContacts(TLRequest):
    ID: int = 0x5dd69e12

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetContacts':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class ContactsImportContacts(TLRequest):
    ID: int = 0x2c800be5

    def __init__(self, contacts: Any = None) -> None:
        self.contacts = contacts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.contacts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsImportContacts':
        contacts = reader.read_vector(lambda r: reader.read_object())
        return cls(contacts=contacts)


@register_tl
class ContactsDeleteContacts(TLRequest):
    ID: int = 0x96a0e00

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsDeleteContacts':
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id)


@register_tl
class ContactsDeleteByPhones(TLRequest):
    ID: int = 0x1013fd9e

    def __init__(self, phones: Any = None) -> None:
        self.phones = phones

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.phones or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsDeleteByPhones':
        phones = reader.read_vector(lambda r: r.read_string())
        return cls(phones=phones)


@register_tl
class ContactsBlock(TLRequest):
    ID: int = 0x2e2e8734

    def __init__(self, my_stories_from: bool = False, id: Any = None) -> None:
        self.my_stories_from = my_stories_from
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.my_stories_from:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlock':
        flags = reader.read_uint32()
        my_stories_from = bool(flags & (1 << 0))
        id = reader.read_object()
        return cls(my_stories_from=my_stories_from, id=id)


@register_tl
class ContactsUnblock(TLRequest):
    ID: int = 0xb550d328

    def __init__(self, my_stories_from: bool = False, id: Any = None) -> None:
        self.my_stories_from = my_stories_from
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.my_stories_from:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsUnblock':
        flags = reader.read_uint32()
        my_stories_from = bool(flags & (1 << 0))
        id = reader.read_object()
        return cls(my_stories_from=my_stories_from, id=id)


@register_tl
class ContactsGetBlocked(TLRequest):
    ID: int = 0x9a868f80

    def __init__(self, my_stories_from: bool = False, offset: Any = None, limit: Any = None) -> None:
        self.my_stories_from = my_stories_from
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.my_stories_from:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetBlocked':
        flags = reader.read_uint32()
        my_stories_from = bool(flags & (1 << 0))
        offset = reader.read_int32()
        limit = reader.read_int32()
        return cls(my_stories_from=my_stories_from, offset=offset, limit=limit)


@register_tl
class ContactsSearch(TLRequest):
    ID: int = 0x11f812d8

    def __init__(self, q: Any = None, limit: Any = None) -> None:
        self.q = q
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsSearch':
        q = reader.read_string()
        limit = reader.read_int32()
        return cls(q=q, limit=limit)


@register_tl
class ContactsResolveUsername(TLRequest):
    ID: int = 0x725afbbc

    def __init__(self, referer: Any = None, username: Any = None) -> None:
        self.referer = referer
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.referer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.username or '')
        if self.referer is not None:
            writer.write_string(self.referer or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsResolveUsername':
        flags = reader.read_uint32()
        username = reader.read_string()
        referer = reader.read_string() if (flags & (1 << 0)) else None
        return cls(username=username, referer=referer)


@register_tl
class ContactsGetTopPeers(TLRequest):
    ID: int = 0x973478b6

    def __init__(self, correspondents: bool = False, bots_pm: bool = False, bots_inline: bool = False, phone_calls: bool = False, forward_users: bool = False, forward_chats: bool = False, groups: bool = False, channels: bool = False, bots_app: bool = False, bots_guestchat: bool = False, offset: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.correspondents = correspondents
        self.bots_pm = bots_pm
        self.bots_inline = bots_inline
        self.phone_calls = phone_calls
        self.forward_users = forward_users
        self.forward_chats = forward_chats
        self.groups = groups
        self.channels = channels
        self.bots_app = bots_app
        self.bots_guestchat = bots_guestchat
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.correspondents:
            flags |= (1 << 0)
        if self.bots_pm:
            flags |= (1 << 1)
        if self.bots_inline:
            flags |= (1 << 2)
        if self.phone_calls:
            flags |= (1 << 3)
        if self.forward_users:
            flags |= (1 << 4)
        if self.forward_chats:
            flags |= (1 << 5)
        if self.groups:
            flags |= (1 << 10)
        if self.channels:
            flags |= (1 << 15)
        if self.bots_app:
            flags |= (1 << 16)
        if self.bots_guestchat:
            flags |= (1 << 17)
        writer.write_uint32(flags)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetTopPeers':
        flags = reader.read_uint32()
        correspondents = bool(flags & (1 << 0))
        bots_pm = bool(flags & (1 << 1))
        bots_inline = bool(flags & (1 << 2))
        phone_calls = bool(flags & (1 << 3))
        forward_users = bool(flags & (1 << 4))
        forward_chats = bool(flags & (1 << 5))
        groups = bool(flags & (1 << 10))
        channels = bool(flags & (1 << 15))
        bots_app = bool(flags & (1 << 16))
        bots_guestchat = bool(flags & (1 << 17))
        offset = reader.read_int32()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(correspondents=correspondents, bots_pm=bots_pm, bots_inline=bots_inline, phone_calls=phone_calls, forward_users=forward_users, forward_chats=forward_chats, groups=groups, channels=channels, bots_app=bots_app, bots_guestchat=bots_guestchat, offset=offset, limit=limit, hash=hash)


@register_tl
class ContactsResetTopPeerRating(TLRequest):
    ID: int = 0x1ae373ac

    def __init__(self, category: Any = None, peer: Any = None) -> None:
        self.category = category
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.category is not None and hasattr(self.category, 'write'): self.category.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsResetTopPeerRating':
        category = reader.read_object()
        peer = reader.read_object()
        return cls(category=category, peer=peer)


@register_tl
class ContactsResetSaved(TLRequest):
    ID: int = 0x879537f1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsResetSaved':
        return cls()


@register_tl
class ContactsGetSaved(TLRequest):
    ID: int = 0x82f1e39f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetSaved':
        return cls()


@register_tl
class ContactsToggleTopPeers(TLRequest):
    ID: int = 0x8514bdda

    def __init__(self, enabled: Any = None) -> None:
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsToggleTopPeers':
        enabled = reader.read_bool()
        return cls(enabled=enabled)


@register_tl
class ContactsAddContact(TLRequest):
    ID: int = 0xd9ba2e54

    def __init__(self, add_phone_privacy_exception: bool = False, note: Any = None, id: Any = None, first_name: Any = None, last_name: Any = None, phone: Any = None) -> None:
        self.add_phone_privacy_exception = add_phone_privacy_exception
        self.note = note
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.add_phone_privacy_exception:
            flags |= (1 << 0)
        if self.note is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_string(self.phone or '')
        if self.note is not None:
            if self.note is not None and hasattr(self.note, 'write'): self.note.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsAddContact':
        flags = reader.read_uint32()
        add_phone_privacy_exception = bool(flags & (1 << 0))
        id = reader.read_object()
        first_name = reader.read_string()
        last_name = reader.read_string()
        phone = reader.read_string()
        note = reader.read_object() if (flags & (1 << 1)) else None
        return cls(add_phone_privacy_exception=add_phone_privacy_exception, id=id, first_name=first_name, last_name=last_name, phone=phone, note=note)


@register_tl
class ContactsAcceptContact(TLRequest):
    ID: int = 0xf831a20f

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsAcceptContact':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class ContactsGetLocated(TLRequest):
    ID: int = 0xd348bc44

    def __init__(self, background: bool = False, self_expires: Any = None, geo_point: Any = None) -> None:
        self.background = background
        self.self_expires = self_expires
        self.geo_point = geo_point

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.background:
            flags |= (1 << 1)
        if self.self_expires is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        if self.self_expires is not None:
            writer.write_int32(self.self_expires or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetLocated':
        flags = reader.read_uint32()
        background = bool(flags & (1 << 1))
        geo_point = reader.read_object()
        self_expires = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(background=background, geo_point=geo_point, self_expires=self_expires)


@register_tl
class ContactsBlockFromReplies(TLRequest):
    ID: int = 0x29a8962c

    def __init__(self, delete_message: bool = False, delete_history: bool = False, report_spam: bool = False, msg_id: Any = None) -> None:
        self.delete_message = delete_message
        self.delete_history = delete_history
        self.report_spam = report_spam
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.delete_message:
            flags |= (1 << 0)
        if self.delete_history:
            flags |= (1 << 1)
        if self.report_spam:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlockFromReplies':
        flags = reader.read_uint32()
        delete_message = bool(flags & (1 << 0))
        delete_history = bool(flags & (1 << 1))
        report_spam = bool(flags & (1 << 2))
        msg_id = reader.read_int32()
        return cls(delete_message=delete_message, delete_history=delete_history, report_spam=report_spam, msg_id=msg_id)


@register_tl
class ContactsResolvePhone(TLRequest):
    ID: int = 0x8af94344

    def __init__(self, phone: Any = None) -> None:
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsResolvePhone':
        phone = reader.read_string()
        return cls(phone=phone)


@register_tl
class ContactsExportContactToken(TLRequest):
    ID: int = 0xf8654027

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsExportContactToken':
        return cls()


@register_tl
class ContactsImportContactToken(TLRequest):
    ID: int = 0x13005788

    def __init__(self, token: Any = None) -> None:
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsImportContactToken':
        token = reader.read_string()
        return cls(token=token)


@register_tl
class ContactsEditCloseFriends(TLRequest):
    ID: int = 0xba6705f0

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsEditCloseFriends':
        id = reader.read_vector(lambda r: r.read_int64())
        return cls(id=id)


@register_tl
class ContactsSetBlocked(TLRequest):
    ID: int = 0x94c65c76

    def __init__(self, my_stories_from: bool = False, id: Any = None, limit: Any = None) -> None:
        self.my_stories_from = my_stories_from
        self.id = id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.my_stories_from:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsSetBlocked':
        flags = reader.read_uint32()
        my_stories_from = bool(flags & (1 << 0))
        id = reader.read_vector(lambda r: reader.read_object())
        limit = reader.read_int32()
        return cls(my_stories_from=my_stories_from, id=id, limit=limit)


@register_tl
class ContactsGetBirthdays(TLRequest):
    ID: int = 0xdaeda864

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetBirthdays':
        return cls()


@register_tl
class ContactsGetSponsoredPeers(TLRequest):
    ID: int = 0xb6c8c393

    def __init__(self, q: Any = None) -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetSponsoredPeers':
        q = reader.read_string()
        return cls(q=q)


@register_tl
class ContactsUpdateContactNote(TLRequest):
    ID: int = 0x139f63fb

    def __init__(self, id: Any = None, note: Any = None) -> None:
        self.id = id
        self.note = note

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.note is not None and hasattr(self.note, 'write'): self.note.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsUpdateContactNote':
        id = reader.read_object()
        note = reader.read_object()
        return cls(id=id, note=note)


@register_tl
class MessagesGetMessages(TLRequest):
    ID: int = 0x63c66506

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMessages':
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id)


@register_tl
class MessagesGetDialogs(TLRequest):
    ID: int = 0xa0f4cb4f

    def __init__(self, exclude_pinned: bool = False, folder_id: Any = None, offset_date: Any = None, offset_id: Any = None, offset_peer: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.exclude_pinned = exclude_pinned
        self.folder_id = folder_id
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_peer = offset_peer
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.exclude_pinned:
            flags |= (1 << 0)
        if self.folder_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        writer.write_int32(self.offset_date or 0)
        writer.write_int32(self.offset_id or 0)
        if self.offset_peer is not None and hasattr(self.offset_peer, 'write'): self.offset_peer.write(writer)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDialogs':
        flags = reader.read_uint32()
        exclude_pinned = bool(flags & (1 << 0))
        folder_id = reader.read_int32() if (flags & (1 << 1)) else None
        offset_date = reader.read_int32()
        offset_id = reader.read_int32()
        offset_peer = reader.read_object()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(exclude_pinned=exclude_pinned, folder_id=folder_id, offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash)


@register_tl
class MessagesGetHistory(TLRequest):
    ID: int = 0x4423e6c5

    def __init__(self, peer: Any = None, offset_id: Any = None, offset_date: Any = None, add_offset: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.offset_id = offset_id
        self.offset_date = offset_date
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.offset_date or 0)
        writer.write_int32(self.add_offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetHistory':
        peer = reader.read_object()
        offset_id = reader.read_int32()
        offset_date = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        hash = reader.read_int64()
        return cls(peer=peer, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash)


@register_tl
class MessagesSearch(TLRequest):
    ID: int = 0x29ee847a

    def __init__(self, from_id: Any = None, saved_peer_id: Any = None, saved_reaction: Any = None, top_msg_id: Any = None, peer: Any = None, q: Any = None, filter: Any = None, min_date: Any = None, max_date: Any = None, offset_id: Any = None, add_offset: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None, hash: Any = None) -> None:
        self.from_id = from_id
        self.saved_peer_id = saved_peer_id
        self.saved_reaction = saved_reaction
        self.top_msg_id = top_msg_id
        self.peer = peer
        self.q = q
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.from_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 2)
        if self.saved_reaction is not None:
            flags |= (1 << 3)
        if self.top_msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.q or '')
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        if self.saved_reaction is not None:
            writer.write_vector(self.saved_reaction or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.min_date or 0)
        writer.write_int32(self.max_date or 0)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.add_offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearch':
        flags = reader.read_uint32()
        peer = reader.read_object()
        q = reader.read_string()
        from_id = reader.read_object() if (flags & (1 << 0)) else None
        saved_peer_id = reader.read_object() if (flags & (1 << 2)) else None
        saved_reaction = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        top_msg_id = reader.read_int32() if (flags & (1 << 1)) else None
        filter = reader.read_object()
        min_date = reader.read_int32()
        max_date = reader.read_int32()
        offset_id = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        hash = reader.read_int64()
        return cls(peer=peer, q=q, from_id=from_id, saved_peer_id=saved_peer_id, saved_reaction=saved_reaction, top_msg_id=top_msg_id, filter=filter, min_date=min_date, max_date=max_date, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash)


@register_tl
class MessagesReadHistory(TLRequest):
    ID: int = 0xe306d3a

    def __init__(self, peer: Any = None, max_id: Any = None) -> None:
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadHistory':
        peer = reader.read_object()
        max_id = reader.read_int32()
        return cls(peer=peer, max_id=max_id)


@register_tl
class MessagesDeleteHistory(TLRequest):
    ID: int = 0xb08f922a

    def __init__(self, just_clear: bool = False, revoke: bool = False, min_date: Any = None, max_date: Any = None, peer: Any = None, max_id: Any = None) -> None:
        self.just_clear = just_clear
        self.revoke = revoke
        self.min_date = min_date
        self.max_date = max_date
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.just_clear:
            flags |= (1 << 0)
        if self.revoke:
            flags |= (1 << 1)
        if self.min_date is not None:
            flags |= (1 << 2)
        if self.max_date is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.max_id or 0)
        if self.min_date is not None:
            writer.write_int32(self.min_date or 0)
        if self.max_date is not None:
            writer.write_int32(self.max_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteHistory':
        flags = reader.read_uint32()
        just_clear = bool(flags & (1 << 0))
        revoke = bool(flags & (1 << 1))
        peer = reader.read_object()
        max_id = reader.read_int32()
        min_date = reader.read_int32() if (flags & (1 << 2)) else None
        max_date = reader.read_int32() if (flags & (1 << 3)) else None
        return cls(just_clear=just_clear, revoke=revoke, peer=peer, max_id=max_id, min_date=min_date, max_date=max_date)


@register_tl
class MessagesDeleteMessages(TLRequest):
    ID: int = 0xe58e95d2

    def __init__(self, revoke: bool = False, id: Any = None) -> None:
        self.revoke = revoke
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoke:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteMessages':
        flags = reader.read_uint32()
        revoke = bool(flags & (1 << 0))
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(revoke=revoke, id=id)


@register_tl
class MessagesReceivedMessages(TLRequest):
    ID: int = 0x5a954c0

    def __init__(self, max_id: Any = None) -> None:
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReceivedMessages':
        max_id = reader.read_int32()
        return cls(max_id=max_id)


@register_tl
class MessagesSetTyping(TLRequest):
    ID: int = 0x58943ee2

    def __init__(self, top_msg_id: Any = None, peer: Any = None, action: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.peer = peer
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetTyping':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        action = reader.read_object()
        return cls(peer=peer, top_msg_id=top_msg_id, action=action)


@register_tl
class MessagesSendMessage(TLRequest):
    ID: int = 0x545cd15a

    def __init__(self, no_webpage: bool = False, silent: bool = False, background: bool = False, clear_draft: bool = False, noforwards: bool = False, update_stickersets_order: bool = False, invert_media: bool = False, allow_paid_floodskip: bool = False, reply_to: Any = None, reply_markup: Any = None, entities: Any = None, schedule_date: Any = None, schedule_repeat_period: Any = None, send_as: Any = None, quick_reply_shortcut: Any = None, effect: Any = None, allow_paid_stars: Any = None, suggested_post: Any = None, peer: Any = None, message: Any = None, random_id: Any = None) -> None:
        self.no_webpage = no_webpage
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.allow_paid_floodskip = allow_paid_floodskip
        self.reply_to = reply_to
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.allow_paid_stars = allow_paid_stars
        self.suggested_post = suggested_post
        self.peer = peer
        self.message = message
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 1)
        if self.silent:
            flags |= (1 << 5)
        if self.background:
            flags |= (1 << 6)
        if self.clear_draft:
            flags |= (1 << 7)
        if self.noforwards:
            flags |= (1 << 14)
        if self.update_stickersets_order:
            flags |= (1 << 15)
        if self.invert_media:
            flags |= (1 << 16)
        if self.allow_paid_floodskip:
            flags |= (1 << 19)
        if self.reply_to is not None:
            flags |= (1 << 0)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        if self.entities is not None:
            flags |= (1 << 3)
        if self.schedule_date is not None:
            flags |= (1 << 10)
        if self.schedule_repeat_period is not None:
            flags |= (1 << 24)
        if self.send_as is not None:
            flags |= (1 << 13)
        if self.quick_reply_shortcut is not None:
            flags |= (1 << 17)
        if self.effect is not None:
            flags |= (1 << 18)
        if self.allow_paid_stars is not None:
            flags |= (1 << 21)
        if self.suggested_post is not None:
            flags |= (1 << 22)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        writer.write_string(self.message or '')
        writer.write_int64(self.random_id or 0)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.schedule_repeat_period is not None:
            writer.write_int32(self.schedule_repeat_period or 0)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)
        if self.quick_reply_shortcut is not None:
            if self.quick_reply_shortcut is not None and hasattr(self.quick_reply_shortcut, 'write'): self.quick_reply_shortcut.write(writer)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)
        if self.suggested_post is not None:
            if self.suggested_post is not None and hasattr(self.suggested_post, 'write'): self.suggested_post.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendMessage':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        noforwards = bool(flags & (1 << 14))
        update_stickersets_order = bool(flags & (1 << 15))
        invert_media = bool(flags & (1 << 16))
        allow_paid_floodskip = bool(flags & (1 << 19))
        peer = reader.read_object()
        reply_to = reader.read_object() if (flags & (1 << 0)) else None
        message = reader.read_string()
        random_id = reader.read_int64()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 10)) else None
        schedule_repeat_period = reader.read_int32() if (flags & (1 << 24)) else None
        send_as = reader.read_object() if (flags & (1 << 13)) else None
        quick_reply_shortcut = reader.read_object() if (flags & (1 << 17)) else None
        effect = reader.read_int64() if (flags & (1 << 18)) else None
        allow_paid_stars = reader.read_int64() if (flags & (1 << 21)) else None
        suggested_post = reader.read_object() if (flags & (1 << 22)) else None
        return cls(no_webpage=no_webpage, silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, allow_paid_floodskip=allow_paid_floodskip, peer=peer, reply_to=reply_to, message=message, random_id=random_id, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect, allow_paid_stars=allow_paid_stars, suggested_post=suggested_post)


@register_tl
class MessagesSendMedia(TLRequest):
    ID: int = 0x330e77f

    def __init__(self, silent: bool = False, background: bool = False, clear_draft: bool = False, noforwards: bool = False, update_stickersets_order: bool = False, invert_media: bool = False, allow_paid_floodskip: bool = False, reply_to: Any = None, reply_markup: Any = None, entities: Any = None, schedule_date: Any = None, schedule_repeat_period: Any = None, send_as: Any = None, quick_reply_shortcut: Any = None, effect: Any = None, allow_paid_stars: Any = None, suggested_post: Any = None, peer: Any = None, media: Any = None, message: Any = None, random_id: Any = None) -> None:
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.allow_paid_floodskip = allow_paid_floodskip
        self.reply_to = reply_to
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.allow_paid_stars = allow_paid_stars
        self.suggested_post = suggested_post
        self.peer = peer
        self.media = media
        self.message = message
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 5)
        if self.background:
            flags |= (1 << 6)
        if self.clear_draft:
            flags |= (1 << 7)
        if self.noforwards:
            flags |= (1 << 14)
        if self.update_stickersets_order:
            flags |= (1 << 15)
        if self.invert_media:
            flags |= (1 << 16)
        if self.allow_paid_floodskip:
            flags |= (1 << 19)
        if self.reply_to is not None:
            flags |= (1 << 0)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        if self.entities is not None:
            flags |= (1 << 3)
        if self.schedule_date is not None:
            flags |= (1 << 10)
        if self.schedule_repeat_period is not None:
            flags |= (1 << 24)
        if self.send_as is not None:
            flags |= (1 << 13)
        if self.quick_reply_shortcut is not None:
            flags |= (1 << 17)
        if self.effect is not None:
            flags |= (1 << 18)
        if self.allow_paid_stars is not None:
            flags |= (1 << 21)
        if self.suggested_post is not None:
            flags |= (1 << 22)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        writer.write_string(self.message or '')
        writer.write_int64(self.random_id or 0)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.schedule_repeat_period is not None:
            writer.write_int32(self.schedule_repeat_period or 0)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)
        if self.quick_reply_shortcut is not None:
            if self.quick_reply_shortcut is not None and hasattr(self.quick_reply_shortcut, 'write'): self.quick_reply_shortcut.write(writer)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)
        if self.suggested_post is not None:
            if self.suggested_post is not None and hasattr(self.suggested_post, 'write'): self.suggested_post.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendMedia':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        noforwards = bool(flags & (1 << 14))
        update_stickersets_order = bool(flags & (1 << 15))
        invert_media = bool(flags & (1 << 16))
        allow_paid_floodskip = bool(flags & (1 << 19))
        peer = reader.read_object()
        reply_to = reader.read_object() if (flags & (1 << 0)) else None
        media = reader.read_object()
        message = reader.read_string()
        random_id = reader.read_int64()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 10)) else None
        schedule_repeat_period = reader.read_int32() if (flags & (1 << 24)) else None
        send_as = reader.read_object() if (flags & (1 << 13)) else None
        quick_reply_shortcut = reader.read_object() if (flags & (1 << 17)) else None
        effect = reader.read_int64() if (flags & (1 << 18)) else None
        allow_paid_stars = reader.read_int64() if (flags & (1 << 21)) else None
        suggested_post = reader.read_object() if (flags & (1 << 22)) else None
        return cls(silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, allow_paid_floodskip=allow_paid_floodskip, peer=peer, reply_to=reply_to, media=media, message=message, random_id=random_id, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect, allow_paid_stars=allow_paid_stars, suggested_post=suggested_post)


@register_tl
class MessagesForwardMessages(TLRequest):
    ID: int = 0x13704a7c

    def __init__(self, silent: bool = False, background: bool = False, with_my_score: bool = False, drop_author: bool = False, drop_media_captions: bool = False, noforwards: bool = False, allow_paid_floodskip: bool = False, top_msg_id: Any = None, reply_to: Any = None, schedule_date: Any = None, schedule_repeat_period: Any = None, send_as: Any = None, quick_reply_shortcut: Any = None, effect: Any = None, video_timestamp: Any = None, allow_paid_stars: Any = None, suggested_post: Any = None, from_peer: Any = None, id: Any = None, random_id: Any = None, to_peer: Any = None) -> None:
        self.silent = silent
        self.background = background
        self.with_my_score = with_my_score
        self.drop_author = drop_author
        self.drop_media_captions = drop_media_captions
        self.noforwards = noforwards
        self.allow_paid_floodskip = allow_paid_floodskip
        self.top_msg_id = top_msg_id
        self.reply_to = reply_to
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.video_timestamp = video_timestamp
        self.allow_paid_stars = allow_paid_stars
        self.suggested_post = suggested_post
        self.from_peer = from_peer
        self.id = id
        self.random_id = random_id
        self.to_peer = to_peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 5)
        if self.background:
            flags |= (1 << 6)
        if self.with_my_score:
            flags |= (1 << 8)
        if self.drop_author:
            flags |= (1 << 11)
        if self.drop_media_captions:
            flags |= (1 << 12)
        if self.noforwards:
            flags |= (1 << 14)
        if self.allow_paid_floodskip:
            flags |= (1 << 19)
        if self.top_msg_id is not None:
            flags |= (1 << 9)
        if self.reply_to is not None:
            flags |= (1 << 22)
        if self.schedule_date is not None:
            flags |= (1 << 10)
        if self.schedule_repeat_period is not None:
            flags |= (1 << 24)
        if self.send_as is not None:
            flags |= (1 << 13)
        if self.quick_reply_shortcut is not None:
            flags |= (1 << 17)
        if self.effect is not None:
            flags |= (1 << 18)
        if self.video_timestamp is not None:
            flags |= (1 << 20)
        if self.allow_paid_stars is not None:
            flags |= (1 << 21)
        if self.suggested_post is not None:
            flags |= (1 << 23)
        writer.write_uint32(flags)
        if self.from_peer is not None and hasattr(self.from_peer, 'write'): self.from_peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.random_id or [], lambda w, x: w.write_int64(x))
        if self.to_peer is not None and hasattr(self.to_peer, 'write'): self.to_peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.schedule_repeat_period is not None:
            writer.write_int32(self.schedule_repeat_period or 0)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)
        if self.quick_reply_shortcut is not None:
            if self.quick_reply_shortcut is not None and hasattr(self.quick_reply_shortcut, 'write'): self.quick_reply_shortcut.write(writer)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)
        if self.suggested_post is not None:
            if self.suggested_post is not None and hasattr(self.suggested_post, 'write'): self.suggested_post.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesForwardMessages':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        with_my_score = bool(flags & (1 << 8))
        drop_author = bool(flags & (1 << 11))
        drop_media_captions = bool(flags & (1 << 12))
        noforwards = bool(flags & (1 << 14))
        allow_paid_floodskip = bool(flags & (1 << 19))
        from_peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        random_id = reader.read_vector(lambda r: r.read_int64())
        to_peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 9)) else None
        reply_to = reader.read_object() if (flags & (1 << 22)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 10)) else None
        schedule_repeat_period = reader.read_int32() if (flags & (1 << 24)) else None
        send_as = reader.read_object() if (flags & (1 << 13)) else None
        quick_reply_shortcut = reader.read_object() if (flags & (1 << 17)) else None
        effect = reader.read_int64() if (flags & (1 << 18)) else None
        video_timestamp = reader.read_int32() if (flags & (1 << 20)) else None
        allow_paid_stars = reader.read_int64() if (flags & (1 << 21)) else None
        suggested_post = reader.read_object() if (flags & (1 << 23)) else None
        return cls(silent=silent, background=background, with_my_score=with_my_score, drop_author=drop_author, drop_media_captions=drop_media_captions, noforwards=noforwards, allow_paid_floodskip=allow_paid_floodskip, from_peer=from_peer, id=id, random_id=random_id, to_peer=to_peer, top_msg_id=top_msg_id, reply_to=reply_to, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect, video_timestamp=video_timestamp, allow_paid_stars=allow_paid_stars, suggested_post=suggested_post)


@register_tl
class MessagesReportSpam(TLRequest):
    ID: int = 0xcf1592db

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReportSpam':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesGetPeerSettings(TLRequest):
    ID: int = 0xefd9a6a2

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPeerSettings':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesReport(TLRequest):
    ID: int = 0xfc78af9b

    def __init__(self, peer: Any = None, id: Any = None, option: Any = None, message: Any = None) -> None:
        self.peer = peer
        self.id = id
        self.option = option
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))
        writer.write_bytes(self.option or b'')
        writer.write_string(self.message or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReport':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        option = reader.read_bytes()
        message = reader.read_string()
        return cls(peer=peer, id=id, option=option, message=message)


@register_tl
class MessagesGetChats(TLRequest):
    ID: int = 0x49e9528f

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetChats':
        id = reader.read_vector(lambda r: r.read_int64())
        return cls(id=id)


@register_tl
class MessagesGetFullChat(TLRequest):
    ID: int = 0xaeb00b34

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetFullChat':
        chat_id = reader.read_int64()
        return cls(chat_id=chat_id)


@register_tl
class MessagesEditChatTitle(TLRequest):
    ID: int = 0x73783ffd

    def __init__(self, chat_id: Any = None, title: Any = None) -> None:
        self.chat_id = chat_id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditChatTitle':
        chat_id = reader.read_int64()
        title = reader.read_string()
        return cls(chat_id=chat_id, title=title)


@register_tl
class MessagesEditChatPhoto(TLRequest):
    ID: int = 0x35ddd674

    def __init__(self, chat_id: Any = None, photo: Any = None) -> None:
        self.chat_id = chat_id
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditChatPhoto':
        chat_id = reader.read_int64()
        photo = reader.read_object()
        return cls(chat_id=chat_id, photo=photo)


@register_tl
class MessagesAddChatUser(TLRequest):
    ID: int = 0xcbc6d107

    def __init__(self, chat_id: Any = None, user_id: Any = None, fwd_limit: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.fwd_limit = fwd_limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.fwd_limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAddChatUser':
        chat_id = reader.read_int64()
        user_id = reader.read_object()
        fwd_limit = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, fwd_limit=fwd_limit)


@register_tl
class MessagesDeleteChatUser(TLRequest):
    ID: int = 0xa2185cab

    def __init__(self, revoke_history: bool = False, chat_id: Any = None, user_id: Any = None) -> None:
        self.revoke_history = revoke_history
        self.chat_id = chat_id
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoke_history:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.chat_id or 0)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteChatUser':
        flags = reader.read_uint32()
        revoke_history = bool(flags & (1 << 0))
        chat_id = reader.read_int64()
        user_id = reader.read_object()
        return cls(revoke_history=revoke_history, chat_id=chat_id, user_id=user_id)


@register_tl
class MessagesCreateChat(TLRequest):
    ID: int = 0x92ceddd4

    def __init__(self, ttl_period: Any = None, users: Any = None, title: Any = None) -> None:
        self.ttl_period = ttl_period
        self.users = users
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ttl_period is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.title or '')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCreateChat':
        flags = reader.read_uint32()
        users = reader.read_vector(lambda r: reader.read_object())
        title = reader.read_string()
        ttl_period = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(users=users, title=title, ttl_period=ttl_period)


@register_tl
class MessagesGetDhConfig(TLRequest):
    ID: int = 0x26cf8950

    def __init__(self, version: Any = None, random_length: Any = None) -> None:
        self.version = version
        self.random_length = random_length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.version or 0)
        writer.write_int32(self.random_length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDhConfig':
        version = reader.read_int32()
        random_length = reader.read_int32()
        return cls(version=version, random_length=random_length)


@register_tl
class MessagesRequestEncryption(TLRequest):
    ID: int = 0xf64daf43

    def __init__(self, user_id: Any = None, random_id: Any = None, g_a: Any = None) -> None:
        self.user_id = user_id
        self.random_id = random_id
        self.g_a = g_a

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.random_id or 0)
        writer.write_bytes(self.g_a or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRequestEncryption':
        user_id = reader.read_object()
        random_id = reader.read_int32()
        g_a = reader.read_bytes()
        return cls(user_id=user_id, random_id=random_id, g_a=g_a)


@register_tl
class MessagesAcceptEncryption(TLRequest):
    ID: int = 0x3dbc0415

    def __init__(self, peer: Any = None, g_b: Any = None, key_fingerprint: Any = None) -> None:
        self.peer = peer
        self.g_b = g_b
        self.key_fingerprint = key_fingerprint

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bytes(self.g_b or b'')
        writer.write_int64(self.key_fingerprint or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAcceptEncryption':
        peer = reader.read_object()
        g_b = reader.read_bytes()
        key_fingerprint = reader.read_int64()
        return cls(peer=peer, g_b=g_b, key_fingerprint=key_fingerprint)


@register_tl
class MessagesDiscardEncryption(TLRequest):
    ID: int = 0xf393aea0

    def __init__(self, delete_history: bool = False, chat_id: Any = None) -> None:
        self.delete_history = delete_history
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.delete_history:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDiscardEncryption':
        flags = reader.read_uint32()
        delete_history = bool(flags & (1 << 0))
        chat_id = reader.read_int32()
        return cls(delete_history=delete_history, chat_id=chat_id)


@register_tl
class MessagesSetEncryptedTyping(TLRequest):
    ID: int = 0x791451ed

    def __init__(self, peer: Any = None, typing: Any = None) -> None:
        self.peer = peer
        self.typing = typing

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bool(bool(self.typing))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetEncryptedTyping':
        peer = reader.read_object()
        typing = reader.read_bool()
        return cls(peer=peer, typing=typing)


@register_tl
class MessagesReadEncryptedHistory(TLRequest):
    ID: int = 0x7f4b690a

    def __init__(self, peer: Any = None, max_date: Any = None) -> None:
        self.peer = peer
        self.max_date = max_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.max_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadEncryptedHistory':
        peer = reader.read_object()
        max_date = reader.read_int32()
        return cls(peer=peer, max_date=max_date)


@register_tl
class MessagesSendEncrypted(TLRequest):
    ID: int = 0x44fa7a15

    def __init__(self, silent: bool = False, peer: Any = None, random_id: Any = None, data: Any = None) -> None:
        self.silent = silent
        self.peer = peer
        self.random_id = random_id
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.random_id or 0)
        writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendEncrypted':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 0))
        peer = reader.read_object()
        random_id = reader.read_int64()
        data = reader.read_bytes()
        return cls(silent=silent, peer=peer, random_id=random_id, data=data)


@register_tl
class MessagesSendEncryptedFile(TLRequest):
    ID: int = 0x5559481d

    def __init__(self, silent: bool = False, peer: Any = None, random_id: Any = None, data: Any = None, file: Any = None) -> None:
        self.silent = silent
        self.peer = peer
        self.random_id = random_id
        self.data = data
        self.file = file

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.random_id or 0)
        writer.write_bytes(self.data or b'')
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendEncryptedFile':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 0))
        peer = reader.read_object()
        random_id = reader.read_int64()
        data = reader.read_bytes()
        file = reader.read_object()
        return cls(silent=silent, peer=peer, random_id=random_id, data=data, file=file)


@register_tl
class MessagesSendEncryptedService(TLRequest):
    ID: int = 0x32d439a4

    def __init__(self, peer: Any = None, random_id: Any = None, data: Any = None) -> None:
        self.peer = peer
        self.random_id = random_id
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.random_id or 0)
        writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendEncryptedService':
        peer = reader.read_object()
        random_id = reader.read_int64()
        data = reader.read_bytes()
        return cls(peer=peer, random_id=random_id, data=data)


@register_tl
class MessagesReceivedQueue(TLRequest):
    ID: int = 0x55a5bb66

    def __init__(self, max_qts: Any = None) -> None:
        self.max_qts = max_qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.max_qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReceivedQueue':
        max_qts = reader.read_int32()
        return cls(max_qts=max_qts)


@register_tl
class MessagesReportEncryptedSpam(TLRequest):
    ID: int = 0x4b0c8c0f

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReportEncryptedSpam':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesReadMessageContents(TLRequest):
    ID: int = 0x36a73f77

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadMessageContents':
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(id=id)


@register_tl
class MessagesGetStickers(TLRequest):
    ID: int = 0xd5a5d3a1

    def __init__(self, emoticon: Any = None, hash: Any = None) -> None:
        self.emoticon = emoticon
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetStickers':
        emoticon = reader.read_string()
        hash = reader.read_int64()
        return cls(emoticon=emoticon, hash=hash)


@register_tl
class MessagesGetAllStickers(TLRequest):
    ID: int = 0xb8a0a1a8

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAllStickers':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesGetWebPagePreview(TLRequest):
    ID: int = 0x570d6f6f

    def __init__(self, entities: Any = None, message: Any = None) -> None:
        self.entities = entities
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.entities is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetWebPagePreview':
        flags = reader.read_uint32()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        return cls(message=message, entities=entities)


@register_tl
class MessagesExportChatInvite(TLRequest):
    ID: int = 0xa455de90

    def __init__(self, legacy_revoke_permanent: bool = False, request_needed: bool = False, expire_date: Any = None, usage_limit: Any = None, title: Any = None, subscription_pricing: Any = None, peer: Any = None) -> None:
        self.legacy_revoke_permanent = legacy_revoke_permanent
        self.request_needed = request_needed
        self.expire_date = expire_date
        self.usage_limit = usage_limit
        self.title = title
        self.subscription_pricing = subscription_pricing
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.legacy_revoke_permanent:
            flags |= (1 << 2)
        if self.request_needed:
            flags |= (1 << 3)
        if self.expire_date is not None:
            flags |= (1 << 0)
        if self.usage_limit is not None:
            flags |= (1 << 1)
        if self.title is not None:
            flags |= (1 << 4)
        if self.subscription_pricing is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.expire_date is not None:
            writer.write_int32(self.expire_date or 0)
        if self.usage_limit is not None:
            writer.write_int32(self.usage_limit or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.subscription_pricing is not None:
            if self.subscription_pricing is not None and hasattr(self.subscription_pricing, 'write'): self.subscription_pricing.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesExportChatInvite':
        flags = reader.read_uint32()
        legacy_revoke_permanent = bool(flags & (1 << 2))
        request_needed = bool(flags & (1 << 3))
        peer = reader.read_object()
        expire_date = reader.read_int32() if (flags & (1 << 0)) else None
        usage_limit = reader.read_int32() if (flags & (1 << 1)) else None
        title = reader.read_string() if (flags & (1 << 4)) else None
        subscription_pricing = reader.read_object() if (flags & (1 << 5)) else None
        return cls(legacy_revoke_permanent=legacy_revoke_permanent, request_needed=request_needed, peer=peer, expire_date=expire_date, usage_limit=usage_limit, title=title, subscription_pricing=subscription_pricing)


@register_tl
class MessagesCheckChatInvite(TLRequest):
    ID: int = 0x3eadb1bb

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCheckChatInvite':
        hash = reader.read_string()
        return cls(hash=hash)


@register_tl
class MessagesImportChatInvite(TLRequest):
    ID: int = 0x6c50051c

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesImportChatInvite':
        hash = reader.read_string()
        return cls(hash=hash)


@register_tl
class MessagesGetStickerSet(TLRequest):
    ID: int = 0xc8a0ec74

    def __init__(self, stickerset: Any = None, hash: Any = None) -> None:
        self.stickerset = stickerset
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetStickerSet':
        stickerset = reader.read_object()
        hash = reader.read_int32()
        return cls(stickerset=stickerset, hash=hash)


@register_tl
class MessagesInstallStickerSet(TLRequest):
    ID: int = 0xc78fe460

    def __init__(self, stickerset: Any = None, archived: Any = None) -> None:
        self.stickerset = stickerset
        self.archived = archived

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        writer.write_bool(bool(self.archived))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesInstallStickerSet':
        stickerset = reader.read_object()
        archived = reader.read_bool()
        return cls(stickerset=stickerset, archived=archived)


@register_tl
class MessagesUninstallStickerSet(TLRequest):
    ID: int = 0xf96e55de

    def __init__(self, stickerset: Any = None) -> None:
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUninstallStickerSet':
        stickerset = reader.read_object()
        return cls(stickerset=stickerset)


@register_tl
class MessagesStartBot(TLRequest):
    ID: int = 0xe6df7378

    def __init__(self, bot: Any = None, peer: Any = None, random_id: Any = None, start_param: Any = None) -> None:
        self.bot = bot
        self.peer = peer
        self.random_id = random_id
        self.start_param = start_param

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.random_id or 0)
        writer.write_string(self.start_param or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStartBot':
        bot = reader.read_object()
        peer = reader.read_object()
        random_id = reader.read_int64()
        start_param = reader.read_string()
        return cls(bot=bot, peer=peer, random_id=random_id, start_param=start_param)


@register_tl
class MessagesGetMessagesViews(TLRequest):
    ID: int = 0x5784d3e1

    def __init__(self, peer: Any = None, id: Any = None, increment: Any = None) -> None:
        self.peer = peer
        self.id = id
        self.increment = increment

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))
        writer.write_bool(bool(self.increment))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMessagesViews':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        increment = reader.read_bool()
        return cls(peer=peer, id=id, increment=increment)


@register_tl
class MessagesEditChatAdmin(TLRequest):
    ID: int = 0xa85bd1c2

    def __init__(self, chat_id: Any = None, user_id: Any = None, is_admin: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_bool(bool(self.is_admin))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditChatAdmin':
        chat_id = reader.read_int64()
        user_id = reader.read_object()
        is_admin = reader.read_bool()
        return cls(chat_id=chat_id, user_id=user_id, is_admin=is_admin)


@register_tl
class MessagesMigrateChat(TLRequest):
    ID: int = 0xa2875319

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMigrateChat':
        chat_id = reader.read_int64()
        return cls(chat_id=chat_id)


@register_tl
class MessagesSearchGlobal(TLRequest):
    ID: int = 0x4bc6589a

    def __init__(self, broadcasts_only: bool = False, groups_only: bool = False, users_only: bool = False, folder_id: Any = None, q: Any = None, filter: Any = None, min_date: Any = None, max_date: Any = None, offset_rate: Any = None, offset_peer: Any = None, offset_id: Any = None, limit: Any = None) -> None:
        self.broadcasts_only = broadcasts_only
        self.groups_only = groups_only
        self.users_only = users_only
        self.folder_id = folder_id
        self.q = q
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_rate = offset_rate
        self.offset_peer = offset_peer
        self.offset_id = offset_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcasts_only:
            flags |= (1 << 1)
        if self.groups_only:
            flags |= (1 << 2)
        if self.users_only:
            flags |= (1 << 3)
        if self.folder_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        writer.write_string(self.q or '')
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.min_date or 0)
        writer.write_int32(self.max_date or 0)
        writer.write_int32(self.offset_rate or 0)
        if self.offset_peer is not None and hasattr(self.offset_peer, 'write'): self.offset_peer.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchGlobal':
        flags = reader.read_uint32()
        broadcasts_only = bool(flags & (1 << 1))
        groups_only = bool(flags & (1 << 2))
        users_only = bool(flags & (1 << 3))
        folder_id = reader.read_int32() if (flags & (1 << 0)) else None
        q = reader.read_string()
        filter = reader.read_object()
        min_date = reader.read_int32()
        max_date = reader.read_int32()
        offset_rate = reader.read_int32()
        offset_peer = reader.read_object()
        offset_id = reader.read_int32()
        limit = reader.read_int32()
        return cls(broadcasts_only=broadcasts_only, groups_only=groups_only, users_only=users_only, folder_id=folder_id, q=q, filter=filter, min_date=min_date, max_date=max_date, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit)


@register_tl
class MessagesReorderStickerSets(TLRequest):
    ID: int = 0x78337739

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
        writer.write_vector(self.order or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReorderStickerSets':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        order = reader.read_vector(lambda r: r.read_int64())
        return cls(masks=masks, emojis=emojis, order=order)


@register_tl
class MessagesGetDocumentByHash(TLRequest):
    ID: int = 0xb1f2061f

    def __init__(self, sha256: Any = None, size: Any = None, mime_type: Any = None) -> None:
        self.sha256 = sha256
        self.size = size
        self.mime_type = mime_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.sha256 or b'')
        writer.write_int64(self.size or 0)
        writer.write_string(self.mime_type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDocumentByHash':
        sha256 = reader.read_bytes()
        size = reader.read_int64()
        mime_type = reader.read_string()
        return cls(sha256=sha256, size=size, mime_type=mime_type)


@register_tl
class MessagesGetSavedGifs(TLRequest):
    ID: int = 0x5cf09635

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSavedGifs':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesSaveGif(TLRequest):
    ID: int = 0x327a30cb

    def __init__(self, id: Any = None, unsave: Any = None) -> None:
        self.id = id
        self.unsave = unsave

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_bool(bool(self.unsave))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSaveGif':
        id = reader.read_object()
        unsave = reader.read_bool()
        return cls(id=id, unsave=unsave)


@register_tl
class MessagesGetInlineBotResults(TLRequest):
    ID: int = 0x514e999d

    def __init__(self, geo_point: Any = None, bot: Any = None, peer: Any = None, query: Any = None, offset: Any = None) -> None:
        self.geo_point = geo_point
        self.bot = bot
        self.peer = peer
        self.query = query
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo_point is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.geo_point is not None:
            if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        writer.write_string(self.query or '')
        writer.write_string(self.offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetInlineBotResults':
        flags = reader.read_uint32()
        bot = reader.read_object()
        peer = reader.read_object()
        geo_point = reader.read_object() if (flags & (1 << 0)) else None
        query = reader.read_string()
        offset = reader.read_string()
        return cls(bot=bot, peer=peer, geo_point=geo_point, query=query, offset=offset)


@register_tl
class MessagesSetInlineBotResults(TLRequest):
    ID: int = 0xbb12a419

    def __init__(self, gallery: bool = False, private: bool = False, next_offset: Any = None, switch_pm: Any = None, switch_webview: Any = None, query_id: Any = None, results: Any = None, cache_time: Any = None) -> None:
        self.gallery = gallery
        self.private = private
        self.next_offset = next_offset
        self.switch_pm = switch_pm
        self.switch_webview = switch_webview
        self.query_id = query_id
        self.results = results
        self.cache_time = cache_time

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.gallery:
            flags |= (1 << 0)
        if self.private:
            flags |= (1 << 1)
        if self.next_offset is not None:
            flags |= (1 << 2)
        if self.switch_pm is not None:
            flags |= (1 << 3)
        if self.switch_webview is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_vector(self.results or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.cache_time or 0)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        if self.switch_pm is not None:
            if self.switch_pm is not None and hasattr(self.switch_pm, 'write'): self.switch_pm.write(writer)
        if self.switch_webview is not None:
            if self.switch_webview is not None and hasattr(self.switch_webview, 'write'): self.switch_webview.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetInlineBotResults':
        flags = reader.read_uint32()
        gallery = bool(flags & (1 << 0))
        private = bool(flags & (1 << 1))
        query_id = reader.read_int64()
        results = reader.read_vector(lambda r: reader.read_object())
        cache_time = reader.read_int32()
        next_offset = reader.read_string() if (flags & (1 << 2)) else None
        switch_pm = reader.read_object() if (flags & (1 << 3)) else None
        switch_webview = reader.read_object() if (flags & (1 << 4)) else None
        return cls(gallery=gallery, private=private, query_id=query_id, results=results, cache_time=cache_time, next_offset=next_offset, switch_pm=switch_pm, switch_webview=switch_webview)


@register_tl
class MessagesSendInlineBotResult(TLRequest):
    ID: int = 0xc0cf7646

    def __init__(self, silent: bool = False, background: bool = False, clear_draft: bool = False, hide_via: bool = False, reply_to: Any = None, schedule_date: Any = None, send_as: Any = None, quick_reply_shortcut: Any = None, allow_paid_stars: Any = None, peer: Any = None, random_id: Any = None, query_id: Any = None, id: Any = None) -> None:
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.hide_via = hide_via
        self.reply_to = reply_to
        self.schedule_date = schedule_date
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.allow_paid_stars = allow_paid_stars
        self.peer = peer
        self.random_id = random_id
        self.query_id = query_id
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 5)
        if self.background:
            flags |= (1 << 6)
        if self.clear_draft:
            flags |= (1 << 7)
        if self.hide_via:
            flags |= (1 << 11)
        if self.reply_to is not None:
            flags |= (1 << 0)
        if self.schedule_date is not None:
            flags |= (1 << 10)
        if self.send_as is not None:
            flags |= (1 << 13)
        if self.quick_reply_shortcut is not None:
            flags |= (1 << 17)
        if self.allow_paid_stars is not None:
            flags |= (1 << 21)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        writer.write_int64(self.random_id or 0)
        writer.write_int64(self.query_id or 0)
        writer.write_string(self.id or '')
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)
        if self.quick_reply_shortcut is not None:
            if self.quick_reply_shortcut is not None and hasattr(self.quick_reply_shortcut, 'write'): self.quick_reply_shortcut.write(writer)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendInlineBotResult':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        hide_via = bool(flags & (1 << 11))
        peer = reader.read_object()
        reply_to = reader.read_object() if (flags & (1 << 0)) else None
        random_id = reader.read_int64()
        query_id = reader.read_int64()
        id = reader.read_string()
        schedule_date = reader.read_int32() if (flags & (1 << 10)) else None
        send_as = reader.read_object() if (flags & (1 << 13)) else None
        quick_reply_shortcut = reader.read_object() if (flags & (1 << 17)) else None
        allow_paid_stars = reader.read_int64() if (flags & (1 << 21)) else None
        return cls(silent=silent, background=background, clear_draft=clear_draft, hide_via=hide_via, peer=peer, reply_to=reply_to, random_id=random_id, query_id=query_id, id=id, schedule_date=schedule_date, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, allow_paid_stars=allow_paid_stars)


@register_tl
class MessagesGetMessageEditData(TLRequest):
    ID: int = 0xfda68d36

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMessageEditData':
        peer = reader.read_object()
        id = reader.read_int32()
        return cls(peer=peer, id=id)


@register_tl
class MessagesEditMessage(TLRequest):
    ID: int = 0x51e842e1

    def __init__(self, no_webpage: bool = False, invert_media: bool = False, message: Any = None, media: Any = None, reply_markup: Any = None, entities: Any = None, schedule_date: Any = None, schedule_repeat_period: Any = None, quick_reply_shortcut_id: Any = None, peer: Any = None, id: Any = None) -> None:
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.message = message
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities
        self.schedule_date = schedule_date
        self.schedule_repeat_period = schedule_repeat_period
        self.quick_reply_shortcut_id = quick_reply_shortcut_id
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 1)
        if self.invert_media:
            flags |= (1 << 16)
        if self.message is not None:
            flags |= (1 << 11)
        if self.media is not None:
            flags |= (1 << 14)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        if self.entities is not None:
            flags |= (1 << 3)
        if self.schedule_date is not None:
            flags |= (1 << 15)
        if self.schedule_repeat_period is not None:
            flags |= (1 << 18)
        if self.quick_reply_shortcut_id is not None:
            flags |= (1 << 17)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.message is not None:
            writer.write_string(self.message or '')
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.schedule_repeat_period is not None:
            writer.write_int32(self.schedule_repeat_period or 0)
        if self.quick_reply_shortcut_id is not None:
            writer.write_int32(self.quick_reply_shortcut_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditMessage':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        invert_media = bool(flags & (1 << 16))
        peer = reader.read_object()
        id = reader.read_int32()
        message = reader.read_string() if (flags & (1 << 11)) else None
        media = reader.read_object() if (flags & (1 << 14)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 15)) else None
        schedule_repeat_period = reader.read_int32() if (flags & (1 << 18)) else None
        quick_reply_shortcut_id = reader.read_int32() if (flags & (1 << 17)) else None
        return cls(no_webpage=no_webpage, invert_media=invert_media, peer=peer, id=id, message=message, media=media, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, quick_reply_shortcut_id=quick_reply_shortcut_id)


@register_tl
class MessagesEditInlineBotMessage(TLRequest):
    ID: int = 0x83557dba

    def __init__(self, no_webpage: bool = False, invert_media: bool = False, message: Any = None, media: Any = None, reply_markup: Any = None, entities: Any = None, id: Any = None) -> None:
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.message = message
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 1)
        if self.invert_media:
            flags |= (1 << 16)
        if self.message is not None:
            flags |= (1 << 11)
        if self.media is not None:
            flags |= (1 << 14)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        if self.entities is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.message is not None:
            writer.write_string(self.message or '')
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditInlineBotMessage':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        invert_media = bool(flags & (1 << 16))
        id = reader.read_object()
        message = reader.read_string() if (flags & (1 << 11)) else None
        media = reader.read_object() if (flags & (1 << 14)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        return cls(no_webpage=no_webpage, invert_media=invert_media, id=id, message=message, media=media, reply_markup=reply_markup, entities=entities)


@register_tl
class MessagesGetBotCallbackAnswer(TLRequest):
    ID: int = 0x9342ca07

    def __init__(self, game: bool = False, data: Any = None, password: Any = None, peer: Any = None, msg_id: Any = None) -> None:
        self.game = game
        self.data = data
        self.password = password
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.game:
            flags |= (1 << 1)
        if self.data is not None:
            flags |= (1 << 0)
        if self.password is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')
        if self.password is not None:
            if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetBotCallbackAnswer':
        flags = reader.read_uint32()
        game = bool(flags & (1 << 1))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        data = reader.read_bytes() if (flags & (1 << 0)) else None
        password = reader.read_object() if (flags & (1 << 2)) else None
        return cls(game=game, peer=peer, msg_id=msg_id, data=data, password=password)


@register_tl
class MessagesSetBotCallbackAnswer(TLRequest):
    ID: int = 0xd58f130a

    def __init__(self, alert: bool = False, message: Any = None, url: Any = None, query_id: Any = None, cache_time: Any = None) -> None:
        self.alert = alert
        self.message = message
        self.url = url
        self.query_id = query_id
        self.cache_time = cache_time

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.alert:
            flags |= (1 << 1)
        if self.message is not None:
            flags |= (1 << 0)
        if self.url is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        if self.message is not None:
            writer.write_string(self.message or '')
        if self.url is not None:
            writer.write_string(self.url or '')
        writer.write_int32(self.cache_time or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetBotCallbackAnswer':
        flags = reader.read_uint32()
        alert = bool(flags & (1 << 1))
        query_id = reader.read_int64()
        message = reader.read_string() if (flags & (1 << 0)) else None
        url = reader.read_string() if (flags & (1 << 2)) else None
        cache_time = reader.read_int32()
        return cls(alert=alert, query_id=query_id, message=message, url=url, cache_time=cache_time)


@register_tl
class MessagesGetPeerDialogs(TLRequest):
    ID: int = 0xe470bcfd

    def __init__(self, peers: Any = None) -> None:
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPeerDialogs':
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(peers=peers)


@register_tl
class MessagesSaveDraft(TLRequest):
    ID: int = 0x54ae308e

    def __init__(self, no_webpage: bool = False, invert_media: bool = False, reply_to: Any = None, entities: Any = None, media: Any = None, effect: Any = None, suggested_post: Any = None, peer: Any = None, message: Any = None) -> None:
        self.no_webpage = no_webpage
        self.invert_media = invert_media
        self.reply_to = reply_to
        self.entities = entities
        self.media = media
        self.effect = effect
        self.suggested_post = suggested_post
        self.peer = peer
        self.message = message

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
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.suggested_post is not None:
            if self.suggested_post is not None and hasattr(self.suggested_post, 'write'): self.suggested_post.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSaveDraft':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        invert_media = bool(flags & (1 << 6))
        reply_to = reader.read_object() if (flags & (1 << 4)) else None
        peer = reader.read_object()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        media = reader.read_object() if (flags & (1 << 5)) else None
        effect = reader.read_int64() if (flags & (1 << 7)) else None
        suggested_post = reader.read_object() if (flags & (1 << 8)) else None
        return cls(no_webpage=no_webpage, invert_media=invert_media, reply_to=reply_to, peer=peer, message=message, entities=entities, media=media, effect=effect, suggested_post=suggested_post)


@register_tl
class MessagesGetAllDrafts(TLRequest):
    ID: int = 0x6a3f8d65

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAllDrafts':
        return cls()


@register_tl
class MessagesGetFeaturedStickers(TLRequest):
    ID: int = 0x64780b14

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetFeaturedStickers':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesReadFeaturedStickers(TLRequest):
    ID: int = 0x5b118126

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadFeaturedStickers':
        id = reader.read_vector(lambda r: r.read_int64())
        return cls(id=id)


@register_tl
class MessagesGetRecentStickers(TLRequest):
    ID: int = 0x9da9403b

    def __init__(self, attached: bool = False, hash: Any = None) -> None:
        self.attached = attached
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attached:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetRecentStickers':
        flags = reader.read_uint32()
        attached = bool(flags & (1 << 0))
        hash = reader.read_int64()
        return cls(attached=attached, hash=hash)


@register_tl
class MessagesSaveRecentSticker(TLRequest):
    ID: int = 0x392718f8

    def __init__(self, attached: bool = False, id: Any = None, unsave: Any = None) -> None:
        self.attached = attached
        self.id = id
        self.unsave = unsave

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attached:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_bool(bool(self.unsave))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSaveRecentSticker':
        flags = reader.read_uint32()
        attached = bool(flags & (1 << 0))
        id = reader.read_object()
        unsave = reader.read_bool()
        return cls(attached=attached, id=id, unsave=unsave)


@register_tl
class MessagesClearRecentStickers(TLRequest):
    ID: int = 0x8999602d

    def __init__(self, attached: bool = False) -> None:
        self.attached = attached

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attached:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesClearRecentStickers':
        flags = reader.read_uint32()
        attached = bool(flags & (1 << 0))
        return cls(attached=attached)


@register_tl
class MessagesGetArchivedStickers(TLRequest):
    ID: int = 0x57f17692

    def __init__(self, masks: bool = False, emojis: bool = False, offset_id: Any = None, limit: Any = None) -> None:
        self.masks = masks
        self.emojis = emojis
        self.offset_id = offset_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.offset_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetArchivedStickers':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        offset_id = reader.read_int64()
        limit = reader.read_int32()
        return cls(masks=masks, emojis=emojis, offset_id=offset_id, limit=limit)


@register_tl
class MessagesGetMaskStickers(TLRequest):
    ID: int = 0x640f82b8

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMaskStickers':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesGetAttachedStickers(TLRequest):
    ID: int = 0xcc5b67cc

    def __init__(self, media: Any = None) -> None:
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAttachedStickers':
        media = reader.read_object()
        return cls(media=media)


@register_tl
class MessagesSetGameScore(TLRequest):
    ID: int = 0x8ef8ecc0

    def __init__(self, edit_message: bool = False, force: bool = False, peer: Any = None, id: Any = None, user_id: Any = None, score: Any = None) -> None:
        self.edit_message = edit_message
        self.force = force
        self.peer = peer
        self.id = id
        self.user_id = user_id
        self.score = score

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.edit_message:
            flags |= (1 << 0)
        if self.force:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.score or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetGameScore':
        flags = reader.read_uint32()
        edit_message = bool(flags & (1 << 0))
        force = bool(flags & (1 << 1))
        peer = reader.read_object()
        id = reader.read_int32()
        user_id = reader.read_object()
        score = reader.read_int32()
        return cls(edit_message=edit_message, force=force, peer=peer, id=id, user_id=user_id, score=score)


@register_tl
class MessagesSetInlineGameScore(TLRequest):
    ID: int = 0x15ad9f64

    def __init__(self, edit_message: bool = False, force: bool = False, id: Any = None, user_id: Any = None, score: Any = None) -> None:
        self.edit_message = edit_message
        self.force = force
        self.id = id
        self.user_id = user_id
        self.score = score

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.edit_message:
            flags |= (1 << 0)
        if self.force:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.score or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetInlineGameScore':
        flags = reader.read_uint32()
        edit_message = bool(flags & (1 << 0))
        force = bool(flags & (1 << 1))
        id = reader.read_object()
        user_id = reader.read_object()
        score = reader.read_int32()
        return cls(edit_message=edit_message, force=force, id=id, user_id=user_id, score=score)


@register_tl
class MessagesGetGameHighScores(TLRequest):
    ID: int = 0xe822649d

    def __init__(self, peer: Any = None, id: Any = None, user_id: Any = None) -> None:
        self.peer = peer
        self.id = id
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetGameHighScores':
        peer = reader.read_object()
        id = reader.read_int32()
        user_id = reader.read_object()
        return cls(peer=peer, id=id, user_id=user_id)


@register_tl
class MessagesGetInlineGameHighScores(TLRequest):
    ID: int = 0xf635e1b

    def __init__(self, id: Any = None, user_id: Any = None) -> None:
        self.id = id
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetInlineGameHighScores':
        id = reader.read_object()
        user_id = reader.read_object()
        return cls(id=id, user_id=user_id)


@register_tl
class MessagesGetCommonChats(TLRequest):
    ID: int = 0xe40ca104

    def __init__(self, user_id: Any = None, max_id: Any = None, limit: Any = None) -> None:
        self.user_id = user_id
        self.max_id = max_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int64(self.max_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetCommonChats':
        user_id = reader.read_object()
        max_id = reader.read_int64()
        limit = reader.read_int32()
        return cls(user_id=user_id, max_id=max_id, limit=limit)


@register_tl
class MessagesGetWebPage(TLRequest):
    ID: int = 0x8d9692a3

    def __init__(self, url: Any = None, hash: Any = None) -> None:
        self.url = url
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetWebPage':
        url = reader.read_string()
        hash = reader.read_int32()
        return cls(url=url, hash=hash)


@register_tl
class MessagesToggleDialogPin(TLRequest):
    ID: int = 0xa731e257

    def __init__(self, pinned: bool = False, peer: Any = None) -> None:
        self.pinned = pinned
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesToggleDialogPin':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        peer = reader.read_object()
        return cls(pinned=pinned, peer=peer)


@register_tl
class MessagesReorderPinnedDialogs(TLRequest):
    ID: int = 0x3b1adf37

    def __init__(self, force: bool = False, folder_id: Any = None, order: Any = None) -> None:
        self.force = force
        self.folder_id = folder_id
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.force:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.folder_id or 0)
        writer.write_vector(self.order or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReorderPinnedDialogs':
        flags = reader.read_uint32()
        force = bool(flags & (1 << 0))
        folder_id = reader.read_int32()
        order = reader.read_vector(lambda r: reader.read_object())
        return cls(force=force, folder_id=folder_id, order=order)


@register_tl
class MessagesGetPinnedDialogs(TLRequest):
    ID: int = 0xd6b94df2

    def __init__(self, folder_id: Any = None) -> None:
        self.folder_id = folder_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.folder_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPinnedDialogs':
        folder_id = reader.read_int32()
        return cls(folder_id=folder_id)


@register_tl
class MessagesSetBotShippingResults(TLRequest):
    ID: int = 0xe5f672fa

    def __init__(self, error: Any = None, shipping_options: Any = None, query_id: Any = None) -> None:
        self.error = error
        self.shipping_options = shipping_options
        self.query_id = query_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.error is not None:
            flags |= (1 << 0)
        if self.shipping_options is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        if self.error is not None:
            writer.write_string(self.error or '')
        if self.shipping_options is not None:
            writer.write_vector(self.shipping_options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetBotShippingResults':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        error = reader.read_string() if (flags & (1 << 0)) else None
        shipping_options = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        return cls(query_id=query_id, error=error, shipping_options=shipping_options)


@register_tl
class MessagesSetBotPrecheckoutResults(TLRequest):
    ID: int = 0x9c2dd95

    def __init__(self, success: bool = False, error: Any = None, query_id: Any = None) -> None:
        self.success = success
        self.error = error
        self.query_id = query_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.success:
            flags |= (1 << 1)
        if self.error is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        if self.error is not None:
            writer.write_string(self.error or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetBotPrecheckoutResults':
        flags = reader.read_uint32()
        success = bool(flags & (1 << 1))
        query_id = reader.read_int64()
        error = reader.read_string() if (flags & (1 << 0)) else None
        return cls(success=success, query_id=query_id, error=error)


@register_tl
class MessagesUploadMedia(TLRequest):
    ID: int = 0x14967978

    def __init__(self, business_connection_id: Any = None, peer: Any = None, media: Any = None) -> None:
        self.business_connection_id = business_connection_id
        self.peer = peer
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.business_connection_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.business_connection_id is not None:
            writer.write_string(self.business_connection_id or '')
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUploadMedia':
        flags = reader.read_uint32()
        business_connection_id = reader.read_string() if (flags & (1 << 0)) else None
        peer = reader.read_object()
        media = reader.read_object()
        return cls(business_connection_id=business_connection_id, peer=peer, media=media)


@register_tl
class MessagesSendScreenshotNotification(TLRequest):
    ID: int = 0xa1405817

    def __init__(self, peer: Any = None, reply_to: Any = None, random_id: Any = None) -> None:
        self.peer = peer
        self.reply_to = reply_to
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        writer.write_int64(self.random_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendScreenshotNotification':
        peer = reader.read_object()
        reply_to = reader.read_object()
        random_id = reader.read_int64()
        return cls(peer=peer, reply_to=reply_to, random_id=random_id)


@register_tl
class MessagesGetFavedStickers(TLRequest):
    ID: int = 0x4f1aaa9

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetFavedStickers':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesFaveSticker(TLRequest):
    ID: int = 0xb9ffc55b

    def __init__(self, id: Any = None, unfave: Any = None) -> None:
        self.id = id
        self.unfave = unfave

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_bool(bool(self.unfave))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFaveSticker':
        id = reader.read_object()
        unfave = reader.read_bool()
        return cls(id=id, unfave=unfave)


@register_tl
class MessagesGetUnreadMentions(TLRequest):
    ID: int = 0xf107e790

    def __init__(self, top_msg_id: Any = None, peer: Any = None, offset_id: Any = None, add_offset: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.peer = peer
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.add_offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetUnreadMentions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        offset_id = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        return cls(peer=peer, top_msg_id=top_msg_id, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id)


@register_tl
class MessagesReadMentions(TLRequest):
    ID: int = 0x36e5bf4d

    def __init__(self, top_msg_id: Any = None, peer: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadMentions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(peer=peer, top_msg_id=top_msg_id)


@register_tl
class MessagesGetRecentLocations(TLRequest):
    ID: int = 0x702a40e0

    def __init__(self, peer: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetRecentLocations':
        peer = reader.read_object()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(peer=peer, limit=limit, hash=hash)


@register_tl
class MessagesSendMultiMedia(TLRequest):
    ID: int = 0x1bf89d74

    def __init__(self, silent: bool = False, background: bool = False, clear_draft: bool = False, noforwards: bool = False, update_stickersets_order: bool = False, invert_media: bool = False, allow_paid_floodskip: bool = False, reply_to: Any = None, schedule_date: Any = None, send_as: Any = None, quick_reply_shortcut: Any = None, effect: Any = None, allow_paid_stars: Any = None, peer: Any = None, multi_media: Any = None) -> None:
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.update_stickersets_order = update_stickersets_order
        self.invert_media = invert_media
        self.allow_paid_floodskip = allow_paid_floodskip
        self.reply_to = reply_to
        self.schedule_date = schedule_date
        self.send_as = send_as
        self.quick_reply_shortcut = quick_reply_shortcut
        self.effect = effect
        self.allow_paid_stars = allow_paid_stars
        self.peer = peer
        self.multi_media = multi_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 5)
        if self.background:
            flags |= (1 << 6)
        if self.clear_draft:
            flags |= (1 << 7)
        if self.noforwards:
            flags |= (1 << 14)
        if self.update_stickersets_order:
            flags |= (1 << 15)
        if self.invert_media:
            flags |= (1 << 16)
        if self.allow_paid_floodskip:
            flags |= (1 << 19)
        if self.reply_to is not None:
            flags |= (1 << 0)
        if self.schedule_date is not None:
            flags |= (1 << 10)
        if self.send_as is not None:
            flags |= (1 << 13)
        if self.quick_reply_shortcut is not None:
            flags |= (1 << 17)
        if self.effect is not None:
            flags |= (1 << 18)
        if self.allow_paid_stars is not None:
            flags |= (1 << 21)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        writer.write_vector(self.multi_media or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)
        if self.quick_reply_shortcut is not None:
            if self.quick_reply_shortcut is not None and hasattr(self.quick_reply_shortcut, 'write'): self.quick_reply_shortcut.write(writer)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendMultiMedia':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        noforwards = bool(flags & (1 << 14))
        update_stickersets_order = bool(flags & (1 << 15))
        invert_media = bool(flags & (1 << 16))
        allow_paid_floodskip = bool(flags & (1 << 19))
        peer = reader.read_object()
        reply_to = reader.read_object() if (flags & (1 << 0)) else None
        multi_media = reader.read_vector(lambda r: reader.read_object())
        schedule_date = reader.read_int32() if (flags & (1 << 10)) else None
        send_as = reader.read_object() if (flags & (1 << 13)) else None
        quick_reply_shortcut = reader.read_object() if (flags & (1 << 17)) else None
        effect = reader.read_int64() if (flags & (1 << 18)) else None
        allow_paid_stars = reader.read_int64() if (flags & (1 << 21)) else None
        return cls(silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, allow_paid_floodskip=allow_paid_floodskip, peer=peer, reply_to=reply_to, multi_media=multi_media, schedule_date=schedule_date, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect, allow_paid_stars=allow_paid_stars)


@register_tl
class MessagesUploadEncryptedFile(TLRequest):
    ID: int = 0x5057c497

    def __init__(self, peer: Any = None, file: Any = None) -> None:
        self.peer = peer
        self.file = file

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUploadEncryptedFile':
        peer = reader.read_object()
        file = reader.read_object()
        return cls(peer=peer, file=file)


@register_tl
class MessagesSearchStickerSets(TLRequest):
    ID: int = 0x35705b8a

    def __init__(self, exclude_featured: bool = False, q: Any = None, hash: Any = None) -> None:
        self.exclude_featured = exclude_featured
        self.q = q
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.exclude_featured:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.q or '')
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchStickerSets':
        flags = reader.read_uint32()
        exclude_featured = bool(flags & (1 << 0))
        q = reader.read_string()
        hash = reader.read_int64()
        return cls(exclude_featured=exclude_featured, q=q, hash=hash)

