from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class MessagesGetSplitRanges(TLRequest):
    ID: int = 0x1cff7e08

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSplitRanges':
        return cls()


@register_tl
class MessagesMarkDialogUnread(TLRequest):
    ID: int = 0x8c5006f8

    def __init__(self, unread: bool = False, parent_peer: Any = None, peer: Any = None) -> None:
        self.unread = unread
        self.parent_peer = parent_peer
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unread:
            flags |= (1 << 0)
        if self.parent_peer is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMarkDialogUnread':
        flags = reader.read_uint32()
        unread = bool(flags & (1 << 0))
        parent_peer = reader.read_object() if (flags & (1 << 1)) else None
        peer = reader.read_object()
        return cls(unread=unread, parent_peer=parent_peer, peer=peer)


@register_tl
class MessagesGetDialogUnreadMarks(TLRequest):
    ID: int = 0x21202222

    def __init__(self, parent_peer: Any = None) -> None:
        self.parent_peer = parent_peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.parent_peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDialogUnreadMarks':
        flags = reader.read_uint32()
        parent_peer = reader.read_object() if (flags & (1 << 0)) else None
        return cls(parent_peer=parent_peer)


@register_tl
class MessagesClearAllDrafts(TLRequest):
    ID: int = 0x7e58ee9c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesClearAllDrafts':
        return cls()


@register_tl
class MessagesUpdatePinnedMessage(TLRequest):
    ID: int = 0xd2aaf7ec

    def __init__(self, silent: bool = False, unpin: bool = False, pm_oneside: bool = False, peer: Any = None, id: Any = None) -> None:
        self.silent = silent
        self.unpin = unpin
        self.pm_oneside = pm_oneside
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 0)
        if self.unpin:
            flags |= (1 << 1)
        if self.pm_oneside:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUpdatePinnedMessage':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 0))
        unpin = bool(flags & (1 << 1))
        pm_oneside = bool(flags & (1 << 2))
        peer = reader.read_object()
        id = reader.read_int32()
        return cls(silent=silent, unpin=unpin, pm_oneside=pm_oneside, peer=peer, id=id)


@register_tl
class MessagesSendVote(TLRequest):
    ID: int = 0x10ea6184

    def __init__(self, peer: Any = None, msg_id: Any = None, options: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.options = options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_vector(self.options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendVote':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        options = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, msg_id=msg_id, options=options)


@register_tl
class MessagesGetPollResults(TLRequest):
    ID: int = 0xeda3e33b

    def __init__(self, peer: Any = None, msg_id: Any = None, poll_hash: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.poll_hash = poll_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.poll_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPollResults':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        poll_hash = reader.read_int64()
        return cls(peer=peer, msg_id=msg_id, poll_hash=poll_hash)


@register_tl
class MessagesGetOnlines(TLRequest):
    ID: int = 0x6e2be050

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetOnlines':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesEditChatAbout(TLRequest):
    ID: int = 0xdef60797

    def __init__(self, peer: Any = None, about: Any = None) -> None:
        self.peer = peer
        self.about = about

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.about or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditChatAbout':
        peer = reader.read_object()
        about = reader.read_string()
        return cls(peer=peer, about=about)


@register_tl
class MessagesEditChatDefaultBannedRights(TLRequest):
    ID: int = 0xa5866b41

    def __init__(self, peer: Any = None, banned_rights: Any = None) -> None:
        self.peer = peer
        self.banned_rights = banned_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.banned_rights is not None and hasattr(self.banned_rights, 'write'): self.banned_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditChatDefaultBannedRights':
        peer = reader.read_object()
        banned_rights = reader.read_object()
        return cls(peer=peer, banned_rights=banned_rights)


@register_tl
class MessagesGetEmojiKeywords(TLRequest):
    ID: int = 0x35a0e062

    def __init__(self, lang_code: Any = None) -> None:
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiKeywords':
        lang_code = reader.read_string()
        return cls(lang_code=lang_code)


@register_tl
class MessagesGetEmojiKeywordsDifference(TLRequest):
    ID: int = 0x1508b6af

    def __init__(self, lang_code: Any = None, from_version: Any = None) -> None:
        self.lang_code = lang_code
        self.from_version = from_version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')
        writer.write_int32(self.from_version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiKeywordsDifference':
        lang_code = reader.read_string()
        from_version = reader.read_int32()
        return cls(lang_code=lang_code, from_version=from_version)


@register_tl
class MessagesGetEmojiKeywordsLanguages(TLRequest):
    ID: int = 0x4e9963b2

    def __init__(self, lang_codes: Any = None) -> None:
        self.lang_codes = lang_codes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.lang_codes or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiKeywordsLanguages':
        lang_codes = reader.read_vector(lambda r: r.read_string())
        return cls(lang_codes=lang_codes)


@register_tl
class MessagesGetEmojiURL(TLRequest):
    ID: int = 0xd5b10c26

    def __init__(self, lang_code: Any = None) -> None:
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiURL':
        lang_code = reader.read_string()
        return cls(lang_code=lang_code)


@register_tl
class MessagesGetSearchCounters(TLRequest):
    ID: int = 0x1bbcf300

    def __init__(self, saved_peer_id: Any = None, top_msg_id: Any = None, peer: Any = None, filters: Any = None) -> None:
        self.saved_peer_id = saved_peer_id
        self.top_msg_id = top_msg_id
        self.peer = peer
        self.filters = filters

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.saved_peer_id is not None:
            flags |= (1 << 2)
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_vector(self.filters or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSearchCounters':
        flags = reader.read_uint32()
        peer = reader.read_object()
        saved_peer_id = reader.read_object() if (flags & (1 << 2)) else None
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        filters = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, saved_peer_id=saved_peer_id, top_msg_id=top_msg_id, filters=filters)


@register_tl
class MessagesRequestUrlAuth(TLRequest):
    ID: int = 0x894cc99c

    def __init__(self, peer: Any = None, msg_id: Any = None, button_id: Any = None, url: Any = None, in_app_origin: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.url = url
        self.in_app_origin = in_app_origin

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer is not None:
            flags |= (1 << 1)
        if self.msg_id is not None:
            flags |= (1 << 1)
        if self.button_id is not None:
            flags |= (1 << 1)
        if self.url is not None:
            flags |= (1 << 2)
        if self.in_app_origin is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.button_id is not None:
            writer.write_int32(self.button_id or 0)
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.in_app_origin is not None:
            writer.write_string(self.in_app_origin or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRequestUrlAuth':
        flags = reader.read_uint32()
        peer = reader.read_object() if (flags & (1 << 1)) else None
        msg_id = reader.read_int32() if (flags & (1 << 1)) else None
        button_id = reader.read_int32() if (flags & (1 << 1)) else None
        url = reader.read_string() if (flags & (1 << 2)) else None
        in_app_origin = reader.read_string() if (flags & (1 << 3)) else None
        return cls(peer=peer, msg_id=msg_id, button_id=button_id, url=url, in_app_origin=in_app_origin)


@register_tl
class MessagesAcceptUrlAuth(TLRequest):
    ID: int = 0x67a3f0de

    def __init__(self, write_allowed: bool = False, share_phone_number: bool = False, peer: Any = None, msg_id: Any = None, button_id: Any = None, url: Any = None, match_code: Any = None) -> None:
        self.write_allowed = write_allowed
        self.share_phone_number = share_phone_number
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.url = url
        self.match_code = match_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.write_allowed:
            flags |= (1 << 0)
        if self.share_phone_number:
            flags |= (1 << 3)
        if self.peer is not None:
            flags |= (1 << 1)
        if self.msg_id is not None:
            flags |= (1 << 1)
        if self.button_id is not None:
            flags |= (1 << 1)
        if self.url is not None:
            flags |= (1 << 2)
        if self.match_code is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.button_id is not None:
            writer.write_int32(self.button_id or 0)
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.match_code is not None:
            writer.write_string(self.match_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAcceptUrlAuth':
        flags = reader.read_uint32()
        write_allowed = bool(flags & (1 << 0))
        share_phone_number = bool(flags & (1 << 3))
        peer = reader.read_object() if (flags & (1 << 1)) else None
        msg_id = reader.read_int32() if (flags & (1 << 1)) else None
        button_id = reader.read_int32() if (flags & (1 << 1)) else None
        url = reader.read_string() if (flags & (1 << 2)) else None
        match_code = reader.read_string() if (flags & (1 << 4)) else None
        return cls(write_allowed=write_allowed, share_phone_number=share_phone_number, peer=peer, msg_id=msg_id, button_id=button_id, url=url, match_code=match_code)


@register_tl
class MessagesHidePeerSettingsBar(TLRequest):
    ID: int = 0x4facb138

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesHidePeerSettingsBar':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesGetScheduledHistory(TLRequest):
    ID: int = 0xf516760b

    def __init__(self, peer: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetScheduledHistory':
        peer = reader.read_object()
        hash = reader.read_int64()
        return cls(peer=peer, hash=hash)


@register_tl
class MessagesGetScheduledMessages(TLRequest):
    ID: int = 0xbdbb0464

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetScheduledMessages':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class MessagesSendScheduledMessages(TLRequest):
    ID: int = 0xbd38850a

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendScheduledMessages':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class MessagesDeleteScheduledMessages(TLRequest):
    ID: int = 0x59ae2b16

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteScheduledMessages':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class MessagesGetPollVotes(TLRequest):
    ID: int = 0xb86e380e

    def __init__(self, option: Any = None, offset: Any = None, peer: Any = None, id: Any = None, limit: Any = None) -> None:
        self.option = option
        self.offset = offset
        self.peer = peer
        self.id = id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.option is not None:
            flags |= (1 << 0)
        if self.offset is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.option is not None:
            writer.write_bytes(self.option or b'')
        if self.offset is not None:
            writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPollVotes':
        flags = reader.read_uint32()
        peer = reader.read_object()
        id = reader.read_int32()
        option = reader.read_bytes() if (flags & (1 << 0)) else None
        offset = reader.read_string() if (flags & (1 << 1)) else None
        limit = reader.read_int32()
        return cls(peer=peer, id=id, option=option, offset=offset, limit=limit)


@register_tl
class MessagesToggleStickerSets(TLRequest):
    ID: int = 0xb5052fea

    def __init__(self, uninstall: bool = False, archive: bool = False, unarchive: bool = False, stickersets: Any = None) -> None:
        self.uninstall = uninstall
        self.archive = archive
        self.unarchive = unarchive
        self.stickersets = stickersets

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.uninstall:
            flags |= (1 << 0)
        if self.archive:
            flags |= (1 << 1)
        if self.unarchive:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_vector(self.stickersets or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesToggleStickerSets':
        flags = reader.read_uint32()
        uninstall = bool(flags & (1 << 0))
        archive = bool(flags & (1 << 1))
        unarchive = bool(flags & (1 << 2))
        stickersets = reader.read_vector(lambda r: reader.read_object())
        return cls(uninstall=uninstall, archive=archive, unarchive=unarchive, stickersets=stickersets)


@register_tl
class MessagesGetDialogFilters(TLRequest):
    ID: int = 0xefd48c89

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDialogFilters':
        return cls()


@register_tl
class MessagesGetSuggestedDialogFilters(TLRequest):
    ID: int = 0xa29cd42c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSuggestedDialogFilters':
        return cls()


@register_tl
class MessagesUpdateDialogFilter(TLRequest):
    ID: int = 0x1ad4a04a

    def __init__(self, filter: Any = None, id: Any = None) -> None:
        self.filter = filter
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.filter is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.filter is not None:
            if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUpdateDialogFilter':
        flags = reader.read_uint32()
        id = reader.read_int32()
        filter = reader.read_object() if (flags & (1 << 0)) else None
        return cls(id=id, filter=filter)


@register_tl
class MessagesUpdateDialogFiltersOrder(TLRequest):
    ID: int = 0xc563c1e4

    def __init__(self, order: Any = None) -> None:
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.order or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUpdateDialogFiltersOrder':
        order = reader.read_vector(lambda r: r.read_int32())
        return cls(order=order)


@register_tl
class MessagesGetOldFeaturedStickers(TLRequest):
    ID: int = 0x7ed094a1

    def __init__(self, offset: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetOldFeaturedStickers':
        offset = reader.read_int32()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(offset=offset, limit=limit, hash=hash)


@register_tl
class MessagesGetReplies(TLRequest):
    ID: int = 0x22ddd30c

    def __init__(self, peer: Any = None, msg_id: Any = None, offset_id: Any = None, offset_date: Any = None, add_offset: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
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
        writer.write_int32(self.msg_id or 0)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.offset_date or 0)
        writer.write_int32(self.add_offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetReplies':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        offset_id = reader.read_int32()
        offset_date = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        hash = reader.read_int64()
        return cls(peer=peer, msg_id=msg_id, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash)


@register_tl
class MessagesGetDiscussionMessage(TLRequest):
    ID: int = 0x446972fd

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDiscussionMessage':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class MessagesReadDiscussion(TLRequest):
    ID: int = 0xf731a9f4

    def __init__(self, peer: Any = None, msg_id: Any = None, read_max_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.read_max_id = read_max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int32(self.read_max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadDiscussion':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        read_max_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id, read_max_id=read_max_id)


@register_tl
class MessagesUnpinAllMessages(TLRequest):
    ID: int = 0x62dd747

    def __init__(self, top_msg_id: Any = None, saved_peer_id: Any = None, peer: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUnpinAllMessages':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        saved_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        return cls(peer=peer, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id)


@register_tl
class MessagesDeleteChat(TLRequest):
    ID: int = 0x5bd0ee50

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteChat':
        chat_id = reader.read_int64()
        return cls(chat_id=chat_id)


@register_tl
class MessagesDeletePhoneCallHistory(TLRequest):
    ID: int = 0xf9cbe409

    def __init__(self, revoke: bool = False) -> None:
        self.revoke = revoke

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoke:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeletePhoneCallHistory':
        flags = reader.read_uint32()
        revoke = bool(flags & (1 << 0))
        return cls(revoke=revoke)


@register_tl
class MessagesCheckHistoryImport(TLRequest):
    ID: int = 0x43fe19f3

    def __init__(self, import_head: Any = None) -> None:
        self.import_head = import_head

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.import_head or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCheckHistoryImport':
        import_head = reader.read_string()
        return cls(import_head=import_head)


@register_tl
class MessagesInitHistoryImport(TLRequest):
    ID: int = 0x34090c3b

    def __init__(self, peer: Any = None, file: Any = None, media_count: Any = None) -> None:
        self.peer = peer
        self.file = file
        self.media_count = media_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        writer.write_int32(self.media_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesInitHistoryImport':
        peer = reader.read_object()
        file = reader.read_object()
        media_count = reader.read_int32()
        return cls(peer=peer, file=file, media_count=media_count)


@register_tl
class MessagesUploadImportedMedia(TLRequest):
    ID: int = 0x2a862092

    def __init__(self, peer: Any = None, import_id: Any = None, file_name: Any = None, media: Any = None) -> None:
        self.peer = peer
        self.import_id = import_id
        self.file_name = file_name
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.import_id or 0)
        writer.write_string(self.file_name or '')
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUploadImportedMedia':
        peer = reader.read_object()
        import_id = reader.read_int64()
        file_name = reader.read_string()
        media = reader.read_object()
        return cls(peer=peer, import_id=import_id, file_name=file_name, media=media)


@register_tl
class MessagesStartHistoryImport(TLRequest):
    ID: int = 0xb43df344

    def __init__(self, peer: Any = None, import_id: Any = None) -> None:
        self.peer = peer
        self.import_id = import_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.import_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStartHistoryImport':
        peer = reader.read_object()
        import_id = reader.read_int64()
        return cls(peer=peer, import_id=import_id)


@register_tl
class MessagesGetExportedChatInvites(TLRequest):
    ID: int = 0xa2b5a3f6

    def __init__(self, revoked: bool = False, offset_date: Any = None, offset_link: Any = None, peer: Any = None, admin_id: Any = None, limit: Any = None) -> None:
        self.revoked = revoked
        self.offset_date = offset_date
        self.offset_link = offset_link
        self.peer = peer
        self.admin_id = admin_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoked:
            flags |= (1 << 3)
        if self.offset_date is not None:
            flags |= (1 << 2)
        if self.offset_link is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.admin_id is not None and hasattr(self.admin_id, 'write'): self.admin_id.write(writer)
        if self.offset_date is not None:
            writer.write_int32(self.offset_date or 0)
        if self.offset_link is not None:
            writer.write_string(self.offset_link or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetExportedChatInvites':
        flags = reader.read_uint32()
        revoked = bool(flags & (1 << 3))
        peer = reader.read_object()
        admin_id = reader.read_object()
        offset_date = reader.read_int32() if (flags & (1 << 2)) else None
        offset_link = reader.read_string() if (flags & (1 << 2)) else None
        limit = reader.read_int32()
        return cls(revoked=revoked, peer=peer, admin_id=admin_id, offset_date=offset_date, offset_link=offset_link, limit=limit)


@register_tl
class MessagesGetExportedChatInvite(TLRequest):
    ID: int = 0x73746f5c

    def __init__(self, peer: Any = None, link: Any = None) -> None:
        self.peer = peer
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.link or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetExportedChatInvite':
        peer = reader.read_object()
        link = reader.read_string()
        return cls(peer=peer, link=link)


@register_tl
class MessagesEditExportedChatInvite(TLRequest):
    ID: int = 0xbdca2f75

    def __init__(self, revoked: bool = False, expire_date: Any = None, usage_limit: Any = None, request_needed: Any = None, title: Any = None, peer: Any = None, link: Any = None) -> None:
        self.revoked = revoked
        self.expire_date = expire_date
        self.usage_limit = usage_limit
        self.request_needed = request_needed
        self.title = title
        self.peer = peer
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoked:
            flags |= (1 << 2)
        if self.expire_date is not None:
            flags |= (1 << 0)
        if self.usage_limit is not None:
            flags |= (1 << 1)
        if self.request_needed is not None:
            flags |= (1 << 3)
        if self.title is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.link or '')
        if self.expire_date is not None:
            writer.write_int32(self.expire_date or 0)
        if self.usage_limit is not None:
            writer.write_int32(self.usage_limit or 0)
        if self.request_needed is not None:
            writer.write_bool(bool(self.request_needed))
        if self.title is not None:
            writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditExportedChatInvite':
        flags = reader.read_uint32()
        revoked = bool(flags & (1 << 2))
        peer = reader.read_object()
        link = reader.read_string()
        expire_date = reader.read_int32() if (flags & (1 << 0)) else None
        usage_limit = reader.read_int32() if (flags & (1 << 1)) else None
        request_needed = reader.read_bool() if (flags & (1 << 3)) else None
        title = reader.read_string() if (flags & (1 << 4)) else None
        return cls(revoked=revoked, peer=peer, link=link, expire_date=expire_date, usage_limit=usage_limit, request_needed=request_needed, title=title)


@register_tl
class MessagesDeleteRevokedExportedChatInvites(TLRequest):
    ID: int = 0x56987bd5

    def __init__(self, peer: Any = None, admin_id: Any = None) -> None:
        self.peer = peer
        self.admin_id = admin_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.admin_id is not None and hasattr(self.admin_id, 'write'): self.admin_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteRevokedExportedChatInvites':
        peer = reader.read_object()
        admin_id = reader.read_object()
        return cls(peer=peer, admin_id=admin_id)


@register_tl
class MessagesDeleteExportedChatInvite(TLRequest):
    ID: int = 0xd464a42b

    def __init__(self, peer: Any = None, link: Any = None) -> None:
        self.peer = peer
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.link or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteExportedChatInvite':
        peer = reader.read_object()
        link = reader.read_string()
        return cls(peer=peer, link=link)


@register_tl
class MessagesGetAdminsWithInvites(TLRequest):
    ID: int = 0x3920e6ef

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAdminsWithInvites':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesGetChatInviteImporters(TLRequest):
    ID: int = 0xdf04dd4e

    def __init__(self, requested: bool = False, subscription_expired: bool = False, link: Any = None, q: Any = None, peer: Any = None, offset_date: Any = None, offset_user: Any = None, limit: Any = None) -> None:
        self.requested = requested
        self.subscription_expired = subscription_expired
        self.link = link
        self.q = q
        self.peer = peer
        self.offset_date = offset_date
        self.offset_user = offset_user
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.requested:
            flags |= (1 << 0)
        if self.subscription_expired:
            flags |= (1 << 3)
        if self.link is not None:
            flags |= (1 << 1)
        if self.q is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.link is not None:
            writer.write_string(self.link or '')
        if self.q is not None:
            writer.write_string(self.q or '')
        writer.write_int32(self.offset_date or 0)
        if self.offset_user is not None and hasattr(self.offset_user, 'write'): self.offset_user.write(writer)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetChatInviteImporters':
        flags = reader.read_uint32()
        requested = bool(flags & (1 << 0))
        subscription_expired = bool(flags & (1 << 3))
        peer = reader.read_object()
        link = reader.read_string() if (flags & (1 << 1)) else None
        q = reader.read_string() if (flags & (1 << 2)) else None
        offset_date = reader.read_int32()
        offset_user = reader.read_object()
        limit = reader.read_int32()
        return cls(requested=requested, subscription_expired=subscription_expired, peer=peer, link=link, q=q, offset_date=offset_date, offset_user=offset_user, limit=limit)


@register_tl
class MessagesSetHistoryTTL(TLRequest):
    ID: int = 0xb80e5fe4

    def __init__(self, peer: Any = None, period: Any = None) -> None:
        self.peer = peer
        self.period = period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetHistoryTTL':
        peer = reader.read_object()
        period = reader.read_int32()
        return cls(peer=peer, period=period)


@register_tl
class MessagesCheckHistoryImportPeer(TLRequest):
    ID: int = 0x5dc60f03

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCheckHistoryImportPeer':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesSetChatTheme(TLRequest):
    ID: int = 0x81202c9

    def __init__(self, peer: Any = None, theme: Any = None) -> None:
        self.peer = peer
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetChatTheme':
        peer = reader.read_object()
        theme = reader.read_object()
        return cls(peer=peer, theme=theme)


@register_tl
class MessagesGetMessageReadParticipants(TLRequest):
    ID: int = 0x31c1c44f

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMessageReadParticipants':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class MessagesGetSearchResultsCalendar(TLRequest):
    ID: int = 0x6aa3f6bd

    def __init__(self, saved_peer_id: Any = None, peer: Any = None, filter: Any = None, offset_id: Any = None, offset_date: Any = None) -> None:
        self.saved_peer_id = saved_peer_id
        self.peer = peer
        self.filter = filter
        self.offset_id = offset_id
        self.offset_date = offset_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.saved_peer_id is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.offset_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSearchResultsCalendar':
        flags = reader.read_uint32()
        peer = reader.read_object()
        saved_peer_id = reader.read_object() if (flags & (1 << 2)) else None
        filter = reader.read_object()
        offset_id = reader.read_int32()
        offset_date = reader.read_int32()
        return cls(peer=peer, saved_peer_id=saved_peer_id, filter=filter, offset_id=offset_id, offset_date=offset_date)


@register_tl
class MessagesGetSearchResultsPositions(TLRequest):
    ID: int = 0x9c7f2f10

    def __init__(self, saved_peer_id: Any = None, peer: Any = None, filter: Any = None, offset_id: Any = None, limit: Any = None) -> None:
        self.saved_peer_id = saved_peer_id
        self.peer = peer
        self.filter = filter
        self.offset_id = offset_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.saved_peer_id is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSearchResultsPositions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        saved_peer_id = reader.read_object() if (flags & (1 << 2)) else None
        filter = reader.read_object()
        offset_id = reader.read_int32()
        limit = reader.read_int32()
        return cls(peer=peer, saved_peer_id=saved_peer_id, filter=filter, offset_id=offset_id, limit=limit)


@register_tl
class MessagesHideChatJoinRequest(TLRequest):
    ID: int = 0x7fe7e815

    def __init__(self, approved: bool = False, peer: Any = None, user_id: Any = None) -> None:
        self.approved = approved
        self.peer = peer
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.approved:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesHideChatJoinRequest':
        flags = reader.read_uint32()
        approved = bool(flags & (1 << 0))
        peer = reader.read_object()
        user_id = reader.read_object()
        return cls(approved=approved, peer=peer, user_id=user_id)


@register_tl
class MessagesHideAllChatJoinRequests(TLRequest):
    ID: int = 0xe085f4ea

    def __init__(self, approved: bool = False, link: Any = None, peer: Any = None) -> None:
        self.approved = approved
        self.link = link
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.approved:
            flags |= (1 << 0)
        if self.link is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.link is not None:
            writer.write_string(self.link or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesHideAllChatJoinRequests':
        flags = reader.read_uint32()
        approved = bool(flags & (1 << 0))
        peer = reader.read_object()
        link = reader.read_string() if (flags & (1 << 1)) else None
        return cls(approved=approved, peer=peer, link=link)


@register_tl
class MessagesToggleNoForwards(TLRequest):
    ID: int = 0xb2081a35

    def __init__(self, request_msg_id: Any = None, peer: Any = None, enabled: Any = None) -> None:
        self.request_msg_id = request_msg_id
        self.peer = peer
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.request_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bool(bool(self.enabled))
        if self.request_msg_id is not None:
            writer.write_int32(self.request_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesToggleNoForwards':
        flags = reader.read_uint32()
        peer = reader.read_object()
        enabled = reader.read_bool()
        request_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(peer=peer, enabled=enabled, request_msg_id=request_msg_id)


@register_tl
class MessagesSaveDefaultSendAs(TLRequest):
    ID: int = 0xccfddf96

    def __init__(self, peer: Any = None, send_as: Any = None) -> None:
        self.peer = peer
        self.send_as = send_as

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSaveDefaultSendAs':
        peer = reader.read_object()
        send_as = reader.read_object()
        return cls(peer=peer, send_as=send_as)


@register_tl
class MessagesSendReaction(TLRequest):
    ID: int = 0xd30d78d4

    def __init__(self, big: bool = False, add_to_recent: bool = False, reaction: Any = None, peer: Any = None, msg_id: Any = None) -> None:
        self.big = big
        self.add_to_recent = add_to_recent
        self.reaction = reaction
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.big:
            flags |= (1 << 1)
        if self.add_to_recent:
            flags |= (1 << 2)
        if self.reaction is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        if self.reaction is not None:
            writer.write_vector(self.reaction or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendReaction':
        flags = reader.read_uint32()
        big = bool(flags & (1 << 1))
        add_to_recent = bool(flags & (1 << 2))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        reaction = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        return cls(big=big, add_to_recent=add_to_recent, peer=peer, msg_id=msg_id, reaction=reaction)


@register_tl
class MessagesGetMessagesReactions(TLRequest):
    ID: int = 0x8bba90e6

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMessagesReactions':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class MessagesGetMessageReactionsList(TLRequest):
    ID: int = 0x461b3f48

    def __init__(self, reaction: Any = None, offset: Any = None, peer: Any = None, id: Any = None, limit: Any = None) -> None:
        self.reaction = reaction
        self.offset = offset
        self.peer = peer
        self.id = id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reaction is not None:
            flags |= (1 << 0)
        if self.offset is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.reaction is not None:
            if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)
        if self.offset is not None:
            writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMessageReactionsList':
        flags = reader.read_uint32()
        peer = reader.read_object()
        id = reader.read_int32()
        reaction = reader.read_object() if (flags & (1 << 0)) else None
        offset = reader.read_string() if (flags & (1 << 1)) else None
        limit = reader.read_int32()
        return cls(peer=peer, id=id, reaction=reaction, offset=offset, limit=limit)


@register_tl
class MessagesSetChatAvailableReactions(TLRequest):
    ID: int = 0x864b2581

    def __init__(self, reactions_limit: Any = None, paid_enabled: Any = None, peer: Any = None, available_reactions: Any = None) -> None:
        self.reactions_limit = reactions_limit
        self.paid_enabled = paid_enabled
        self.peer = peer
        self.available_reactions = available_reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reactions_limit is not None:
            flags |= (1 << 0)
        if self.paid_enabled is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.available_reactions is not None and hasattr(self.available_reactions, 'write'): self.available_reactions.write(writer)
        if self.reactions_limit is not None:
            writer.write_int32(self.reactions_limit or 0)
        if self.paid_enabled is not None:
            writer.write_bool(bool(self.paid_enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetChatAvailableReactions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        available_reactions = reader.read_object()
        reactions_limit = reader.read_int32() if (flags & (1 << 0)) else None
        paid_enabled = reader.read_bool() if (flags & (1 << 1)) else None
        return cls(peer=peer, available_reactions=available_reactions, reactions_limit=reactions_limit, paid_enabled=paid_enabled)


@register_tl
class MessagesGetAvailableReactions(TLRequest):
    ID: int = 0x18dea0ac

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAvailableReactions':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class MessagesSetDefaultReaction(TLRequest):
    ID: int = 0x4f47a016

    def __init__(self, reaction: Any = None) -> None:
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetDefaultReaction':
        reaction = reader.read_object()
        return cls(reaction=reaction)


@register_tl
class MessagesTranslateText(TLRequest):
    ID: int = 0xa5eec345

    def __init__(self, peer: Any = None, id: Any = None, text: Any = None, tone: Any = None, to_lang: Any = None) -> None:
        self.peer = peer
        self.id = id
        self.text = text
        self.tone = tone
        self.to_lang = to_lang

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer is not None:
            flags |= (1 << 0)
        if self.id is not None:
            flags |= (1 << 0)
        if self.text is not None:
            flags |= (1 << 1)
        if self.tone is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.id is not None:
            writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))
        if self.text is not None:
            writer.write_vector(self.text or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.to_lang or '')
        if self.tone is not None:
            writer.write_string(self.tone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesTranslateText':
        flags = reader.read_uint32()
        peer = reader.read_object() if (flags & (1 << 0)) else None
        id = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        text = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        to_lang = reader.read_string()
        tone = reader.read_string() if (flags & (1 << 2)) else None
        return cls(peer=peer, id=id, text=text, to_lang=to_lang, tone=tone)


@register_tl
class MessagesGetUnreadReactions(TLRequest):
    ID: int = 0xbd7f90ac

    def __init__(self, top_msg_id: Any = None, saved_peer_id: Any = None, peer: Any = None, offset_id: Any = None, add_offset: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
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
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.add_offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetUnreadReactions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        saved_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        offset_id = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        return cls(peer=peer, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id)


@register_tl
class MessagesReadReactions(TLRequest):
    ID: int = 0x9ec44f93

    def __init__(self, top_msg_id: Any = None, saved_peer_id: Any = None, peer: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadReactions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        saved_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        return cls(peer=peer, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id)


@register_tl
class MessagesSearchSentMedia(TLRequest):
    ID: int = 0x107e31a0

    def __init__(self, q: Any = None, filter: Any = None, limit: Any = None) -> None:
        self.q = q
        self.filter = filter
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q or '')
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchSentMedia':
        q = reader.read_string()
        filter = reader.read_object()
        limit = reader.read_int32()
        return cls(q=q, filter=filter, limit=limit)


@register_tl
class MessagesGetAttachMenuBots(TLRequest):
    ID: int = 0x16fcc2cb

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAttachMenuBots':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesGetAttachMenuBot(TLRequest):
    ID: int = 0x77216192

    def __init__(self, bot: Any = None) -> None:
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAttachMenuBot':
        bot = reader.read_object()
        return cls(bot=bot)


@register_tl
class MessagesToggleBotInAttachMenu(TLRequest):
    ID: int = 0x69f59d69

    def __init__(self, write_allowed: bool = False, bot: Any = None, enabled: Any = None) -> None:
        self.write_allowed = write_allowed
        self.bot = bot
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.write_allowed:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesToggleBotInAttachMenu':
        flags = reader.read_uint32()
        write_allowed = bool(flags & (1 << 0))
        bot = reader.read_object()
        enabled = reader.read_bool()
        return cls(write_allowed=write_allowed, bot=bot, enabled=enabled)


@register_tl
class MessagesRequestWebView(TLRequest):
    ID: int = 0x269dc2c1

    def __init__(self, from_bot_menu: bool = False, silent: bool = False, compact: bool = False, fullscreen: bool = False, url: Any = None, start_param: Any = None, theme_params: Any = None, reply_to: Any = None, send_as: Any = None, peer: Any = None, bot: Any = None, platform: Any = None) -> None:
        self.from_bot_menu = from_bot_menu
        self.silent = silent
        self.compact = compact
        self.fullscreen = fullscreen
        self.url = url
        self.start_param = start_param
        self.theme_params = theme_params
        self.reply_to = reply_to
        self.send_as = send_as
        self.peer = peer
        self.bot = bot
        self.platform = platform

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.from_bot_menu:
            flags |= (1 << 4)
        if self.silent:
            flags |= (1 << 5)
        if self.compact:
            flags |= (1 << 7)
        if self.fullscreen:
            flags |= (1 << 8)
        if self.url is not None:
            flags |= (1 << 1)
        if self.start_param is not None:
            flags |= (1 << 3)
        if self.theme_params is not None:
            flags |= (1 << 2)
        if self.reply_to is not None:
            flags |= (1 << 0)
        if self.send_as is not None:
            flags |= (1 << 13)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.start_param is not None:
            writer.write_string(self.start_param or '')
        if self.theme_params is not None:
            if self.theme_params is not None and hasattr(self.theme_params, 'write'): self.theme_params.write(writer)
        writer.write_string(self.platform or '')
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRequestWebView':
        flags = reader.read_uint32()
        from_bot_menu = bool(flags & (1 << 4))
        silent = bool(flags & (1 << 5))
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        peer = reader.read_object()
        bot = reader.read_object()
        url = reader.read_string() if (flags & (1 << 1)) else None
        start_param = reader.read_string() if (flags & (1 << 3)) else None
        theme_params = reader.read_object() if (flags & (1 << 2)) else None
        platform = reader.read_string()
        reply_to = reader.read_object() if (flags & (1 << 0)) else None
        send_as = reader.read_object() if (flags & (1 << 13)) else None
        return cls(from_bot_menu=from_bot_menu, silent=silent, compact=compact, fullscreen=fullscreen, peer=peer, bot=bot, url=url, start_param=start_param, theme_params=theme_params, platform=platform, reply_to=reply_to, send_as=send_as)


@register_tl
class MessagesProlongWebView(TLRequest):
    ID: int = 0xb0d81a83

    def __init__(self, silent: bool = False, reply_to: Any = None, send_as: Any = None, peer: Any = None, bot: Any = None, query_id: Any = None) -> None:
        self.silent = silent
        self.reply_to = reply_to
        self.send_as = send_as
        self.peer = peer
        self.bot = bot
        self.query_id = query_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 5)
        if self.reply_to is not None:
            flags |= (1 << 0)
        if self.send_as is not None:
            flags |= (1 << 13)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_int64(self.query_id or 0)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesProlongWebView':
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 5))
        peer = reader.read_object()
        bot = reader.read_object()
        query_id = reader.read_int64()
        reply_to = reader.read_object() if (flags & (1 << 0)) else None
        send_as = reader.read_object() if (flags & (1 << 13)) else None
        return cls(silent=silent, peer=peer, bot=bot, query_id=query_id, reply_to=reply_to, send_as=send_as)


@register_tl
class MessagesRequestSimpleWebView(TLRequest):
    ID: int = 0x413a3e73

    def __init__(self, from_switch_webview: bool = False, from_side_menu: bool = False, compact: bool = False, fullscreen: bool = False, url: Any = None, start_param: Any = None, theme_params: Any = None, bot: Any = None, platform: Any = None) -> None:
        self.from_switch_webview = from_switch_webview
        self.from_side_menu = from_side_menu
        self.compact = compact
        self.fullscreen = fullscreen
        self.url = url
        self.start_param = start_param
        self.theme_params = theme_params
        self.bot = bot
        self.platform = platform

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.from_switch_webview:
            flags |= (1 << 1)
        if self.from_side_menu:
            flags |= (1 << 2)
        if self.compact:
            flags |= (1 << 7)
        if self.fullscreen:
            flags |= (1 << 8)
        if self.url is not None:
            flags |= (1 << 3)
        if self.start_param is not None:
            flags |= (1 << 4)
        if self.theme_params is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.start_param is not None:
            writer.write_string(self.start_param or '')
        if self.theme_params is not None:
            if self.theme_params is not None and hasattr(self.theme_params, 'write'): self.theme_params.write(writer)
        writer.write_string(self.platform or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRequestSimpleWebView':
        flags = reader.read_uint32()
        from_switch_webview = bool(flags & (1 << 1))
        from_side_menu = bool(flags & (1 << 2))
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        bot = reader.read_object()
        url = reader.read_string() if (flags & (1 << 3)) else None
        start_param = reader.read_string() if (flags & (1 << 4)) else None
        theme_params = reader.read_object() if (flags & (1 << 0)) else None
        platform = reader.read_string()
        return cls(from_switch_webview=from_switch_webview, from_side_menu=from_side_menu, compact=compact, fullscreen=fullscreen, bot=bot, url=url, start_param=start_param, theme_params=theme_params, platform=platform)


@register_tl
class MessagesSendWebViewResultMessage(TLRequest):
    ID: int = 0xa4314f5

    def __init__(self, bot_query_id: Any = None, result: Any = None) -> None:
        self.bot_query_id = bot_query_id
        self.result = result

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.bot_query_id or '')
        if self.result is not None and hasattr(self.result, 'write'): self.result.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendWebViewResultMessage':
        bot_query_id = reader.read_string()
        result = reader.read_object()
        return cls(bot_query_id=bot_query_id, result=result)


@register_tl
class MessagesSendWebViewData(TLRequest):
    ID: int = 0xdc0242c8

    def __init__(self, bot: Any = None, random_id: Any = None, button_text: Any = None, data: Any = None) -> None:
        self.bot = bot
        self.random_id = random_id
        self.button_text = button_text
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_int64(self.random_id or 0)
        writer.write_string(self.button_text or '')
        writer.write_string(self.data or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendWebViewData':
        bot = reader.read_object()
        random_id = reader.read_int64()
        button_text = reader.read_string()
        data = reader.read_string()
        return cls(bot=bot, random_id=random_id, button_text=button_text, data=data)


@register_tl
class MessagesTranscribeAudio(TLRequest):
    ID: int = 0x269e9a49

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesTranscribeAudio':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class MessagesRateTranscribedAudio(TLRequest):
    ID: int = 0x7f1d072f

    def __init__(self, peer: Any = None, msg_id: Any = None, transcription_id: Any = None, good: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.transcription_id = transcription_id
        self.good = good

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.transcription_id or 0)
        writer.write_bool(bool(self.good))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRateTranscribedAudio':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        transcription_id = reader.read_int64()
        good = reader.read_bool()
        return cls(peer=peer, msg_id=msg_id, transcription_id=transcription_id, good=good)


@register_tl
class MessagesGetCustomEmojiDocuments(TLRequest):
    ID: int = 0xd9ab0f54

    def __init__(self, document_id: Any = None) -> None:
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.document_id or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetCustomEmojiDocuments':
        document_id = reader.read_vector(lambda r: r.read_int64())
        return cls(document_id=document_id)


@register_tl
class MessagesGetEmojiStickers(TLRequest):
    ID: int = 0xfbfca18f

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiStickers':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesGetFeaturedEmojiStickers(TLRequest):
    ID: int = 0xecf6736

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetFeaturedEmojiStickers':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesReportReaction(TLRequest):
    ID: int = 0x3f64c076

    def __init__(self, peer: Any = None, id: Any = None, reaction_peer: Any = None) -> None:
        self.peer = peer
        self.id = id
        self.reaction_peer = reaction_peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.reaction_peer is not None and hasattr(self.reaction_peer, 'write'): self.reaction_peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReportReaction':
        peer = reader.read_object()
        id = reader.read_int32()
        reaction_peer = reader.read_object()
        return cls(peer=peer, id=id, reaction_peer=reaction_peer)


@register_tl
class MessagesGetTopReactions(TLRequest):
    ID: int = 0xbb8125ba

    def __init__(self, limit: Any = None, hash: Any = None) -> None:
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetTopReactions':
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(limit=limit, hash=hash)


@register_tl
class MessagesGetRecentReactions(TLRequest):
    ID: int = 0x39461db2

    def __init__(self, limit: Any = None, hash: Any = None) -> None:
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetRecentReactions':
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(limit=limit, hash=hash)


@register_tl
class MessagesClearRecentReactions(TLRequest):
    ID: int = 0x9dfeefb4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesClearRecentReactions':
        return cls()


@register_tl
class MessagesGetExtendedMedia(TLRequest):
    ID: int = 0x84f80814

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetExtendedMedia':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class MessagesSetDefaultHistoryTTL(TLRequest):
    ID: int = 0x9eb51445

    def __init__(self, period: Any = None) -> None:
        self.period = period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetDefaultHistoryTTL':
        period = reader.read_int32()
        return cls(period=period)


@register_tl
class MessagesGetDefaultHistoryTTL(TLRequest):
    ID: int = 0x658b7188

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDefaultHistoryTTL':
        return cls()


@register_tl
class MessagesSendBotRequestedPeer(TLRequest):
    ID: int = 0x6c5cf2a7

    def __init__(self, msg_id: Any = None, webapp_req_id: Any = None, peer: Any = None, button_id: Any = None, requested_peers: Any = None) -> None:
        self.msg_id = msg_id
        self.webapp_req_id = webapp_req_id
        self.peer = peer
        self.button_id = button_id
        self.requested_peers = requested_peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.msg_id is not None:
            flags |= (1 << 0)
        if self.webapp_req_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.webapp_req_id is not None:
            writer.write_string(self.webapp_req_id or '')
        writer.write_int32(self.button_id or 0)
        writer.write_vector(self.requested_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendBotRequestedPeer':
        flags = reader.read_uint32()
        peer = reader.read_object()
        msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        webapp_req_id = reader.read_string() if (flags & (1 << 1)) else None
        button_id = reader.read_int32()
        requested_peers = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, msg_id=msg_id, webapp_req_id=webapp_req_id, button_id=button_id, requested_peers=requested_peers)


@register_tl
class MessagesGetEmojiGroups(TLRequest):
    ID: int = 0x7488ce5b

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiGroups':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class MessagesGetEmojiStatusGroups(TLRequest):
    ID: int = 0x2ecd56cd

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiStatusGroups':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class MessagesGetEmojiProfilePhotoGroups(TLRequest):
    ID: int = 0x21a548f3

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiProfilePhotoGroups':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class MessagesSearchCustomEmoji(TLRequest):
    ID: int = 0x2c11c0d7

    def __init__(self, emoticon: Any = None, hash: Any = None) -> None:
        self.emoticon = emoticon
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchCustomEmoji':
        emoticon = reader.read_string()
        hash = reader.read_int64()
        return cls(emoticon=emoticon, hash=hash)


@register_tl
class MessagesTogglePeerTranslations(TLRequest):
    ID: int = 0xe47cb579

    def __init__(self, disabled: bool = False, peer: Any = None) -> None:
        self.disabled = disabled
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.disabled:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesTogglePeerTranslations':
        flags = reader.read_uint32()
        disabled = bool(flags & (1 << 0))
        peer = reader.read_object()
        return cls(disabled=disabled, peer=peer)


@register_tl
class MessagesGetBotApp(TLRequest):
    ID: int = 0x34fdc5c3

    def __init__(self, app: Any = None, hash: Any = None) -> None:
        self.app = app
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.app is not None and hasattr(self.app, 'write'): self.app.write(writer)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetBotApp':
        app = reader.read_object()
        hash = reader.read_int64()
        return cls(app=app, hash=hash)


@register_tl
class MessagesRequestAppWebView(TLRequest):
    ID: int = 0x53618bce

    def __init__(self, write_allowed: bool = False, compact: bool = False, fullscreen: bool = False, start_param: Any = None, theme_params: Any = None, peer: Any = None, app: Any = None, platform: Any = None) -> None:
        self.write_allowed = write_allowed
        self.compact = compact
        self.fullscreen = fullscreen
        self.start_param = start_param
        self.theme_params = theme_params
        self.peer = peer
        self.app = app
        self.platform = platform

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.write_allowed:
            flags |= (1 << 0)
        if self.compact:
            flags |= (1 << 7)
        if self.fullscreen:
            flags |= (1 << 8)
        if self.start_param is not None:
            flags |= (1 << 1)
        if self.theme_params is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.app is not None and hasattr(self.app, 'write'): self.app.write(writer)
        if self.start_param is not None:
            writer.write_string(self.start_param or '')
        if self.theme_params is not None:
            if self.theme_params is not None and hasattr(self.theme_params, 'write'): self.theme_params.write(writer)
        writer.write_string(self.platform or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRequestAppWebView':
        flags = reader.read_uint32()
        write_allowed = bool(flags & (1 << 0))
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        peer = reader.read_object()
        app = reader.read_object()
        start_param = reader.read_string() if (flags & (1 << 1)) else None
        theme_params = reader.read_object() if (flags & (1 << 2)) else None
        platform = reader.read_string()
        return cls(write_allowed=write_allowed, compact=compact, fullscreen=fullscreen, peer=peer, app=app, start_param=start_param, theme_params=theme_params, platform=platform)


@register_tl
class MessagesSetChatWallPaper(TLRequest):
    ID: int = 0x8ffacae1

    def __init__(self, for_both: bool = False, revert: bool = False, wallpaper: Any = None, settings: Any = None, id: Any = None, peer: Any = None) -> None:
        self.for_both = for_both
        self.revert = revert
        self.wallpaper = wallpaper
        self.settings = settings
        self.id = id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.for_both:
            flags |= (1 << 3)
        if self.revert:
            flags |= (1 << 4)
        if self.wallpaper is not None:
            flags |= (1 << 0)
        if self.settings is not None:
            flags |= (1 << 2)
        if self.id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.wallpaper is not None:
            if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)
        if self.settings is not None:
            if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)
        if self.id is not None:
            writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetChatWallPaper':
        flags = reader.read_uint32()
        for_both = bool(flags & (1 << 3))
        revert = bool(flags & (1 << 4))
        peer = reader.read_object()
        wallpaper = reader.read_object() if (flags & (1 << 0)) else None
        settings = reader.read_object() if (flags & (1 << 2)) else None
        id = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(for_both=for_both, revert=revert, peer=peer, wallpaper=wallpaper, settings=settings, id=id)


@register_tl
class MessagesSearchEmojiStickerSets(TLRequest):
    ID: int = 0x92b4494c

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
    def read(cls, reader: TLReader) -> 'MessagesSearchEmojiStickerSets':
        flags = reader.read_uint32()
        exclude_featured = bool(flags & (1 << 0))
        q = reader.read_string()
        hash = reader.read_int64()
        return cls(exclude_featured=exclude_featured, q=q, hash=hash)


@register_tl
class MessagesGetSavedDialogs(TLRequest):
    ID: int = 0x1e91fc99

    def __init__(self, exclude_pinned: bool = False, parent_peer: Any = None, offset_date: Any = None, offset_id: Any = None, offset_peer: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.exclude_pinned = exclude_pinned
        self.parent_peer = parent_peer
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
        if self.parent_peer is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        writer.write_int32(self.offset_date or 0)
        writer.write_int32(self.offset_id or 0)
        if self.offset_peer is not None and hasattr(self.offset_peer, 'write'): self.offset_peer.write(writer)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSavedDialogs':
        flags = reader.read_uint32()
        exclude_pinned = bool(flags & (1 << 0))
        parent_peer = reader.read_object() if (flags & (1 << 1)) else None
        offset_date = reader.read_int32()
        offset_id = reader.read_int32()
        offset_peer = reader.read_object()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(exclude_pinned=exclude_pinned, parent_peer=parent_peer, offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash)


@register_tl
class MessagesGetSavedHistory(TLRequest):
    ID: int = 0x998ab009

    def __init__(self, parent_peer: Any = None, peer: Any = None, offset_id: Any = None, offset_date: Any = None, add_offset: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None, hash: Any = None) -> None:
        self.parent_peer = parent_peer
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
        flags = 0
        if self.parent_peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.offset_date or 0)
        writer.write_int32(self.add_offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSavedHistory':
        flags = reader.read_uint32()
        parent_peer = reader.read_object() if (flags & (1 << 0)) else None
        peer = reader.read_object()
        offset_id = reader.read_int32()
        offset_date = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        hash = reader.read_int64()
        return cls(parent_peer=parent_peer, peer=peer, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash)


@register_tl
class MessagesDeleteSavedHistory(TLRequest):
    ID: int = 0x4dc5085f

    def __init__(self, parent_peer: Any = None, min_date: Any = None, max_date: Any = None, peer: Any = None, max_id: Any = None) -> None:
        self.parent_peer = parent_peer
        self.min_date = min_date
        self.max_date = max_date
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.parent_peer is not None:
            flags |= (1 << 0)
        if self.min_date is not None:
            flags |= (1 << 2)
        if self.max_date is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.max_id or 0)
        if self.min_date is not None:
            writer.write_int32(self.min_date or 0)
        if self.max_date is not None:
            writer.write_int32(self.max_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteSavedHistory':
        flags = reader.read_uint32()
        parent_peer = reader.read_object() if (flags & (1 << 0)) else None
        peer = reader.read_object()
        max_id = reader.read_int32()
        min_date = reader.read_int32() if (flags & (1 << 2)) else None
        max_date = reader.read_int32() if (flags & (1 << 3)) else None
        return cls(parent_peer=parent_peer, peer=peer, max_id=max_id, min_date=min_date, max_date=max_date)


@register_tl
class MessagesGetPinnedSavedDialogs(TLRequest):
    ID: int = 0xd63d94e0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPinnedSavedDialogs':
        return cls()


@register_tl
class MessagesToggleSavedDialogPin(TLRequest):
    ID: int = 0xac81bbde

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
    def read(cls, reader: TLReader) -> 'MessagesToggleSavedDialogPin':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        peer = reader.read_object()
        return cls(pinned=pinned, peer=peer)


@register_tl
class MessagesReorderPinnedSavedDialogs(TLRequest):
    ID: int = 0x8b716587

    def __init__(self, force: bool = False, order: Any = None) -> None:
        self.force = force
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.force:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.order or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReorderPinnedSavedDialogs':
        flags = reader.read_uint32()
        force = bool(flags & (1 << 0))
        order = reader.read_vector(lambda r: reader.read_object())
        return cls(force=force, order=order)


@register_tl
class MessagesGetSavedReactionTags(TLRequest):
    ID: int = 0x3637e05b

    def __init__(self, peer: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSavedReactionTags':
        flags = reader.read_uint32()
        peer = reader.read_object() if (flags & (1 << 0)) else None
        hash = reader.read_int64()
        return cls(peer=peer, hash=hash)


@register_tl
class MessagesUpdateSavedReactionTag(TLRequest):
    ID: int = 0x60297dec

    def __init__(self, title: Any = None, reaction: Any = None) -> None:
        self.title = title
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)
        if self.title is not None:
            writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUpdateSavedReactionTag':
        flags = reader.read_uint32()
        reaction = reader.read_object()
        title = reader.read_string() if (flags & (1 << 0)) else None
        return cls(reaction=reaction, title=title)


@register_tl
class MessagesGetDefaultTagReactions(TLRequest):
    ID: int = 0xbdf93428

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetDefaultTagReactions':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesGetOutboxReadDate(TLRequest):
    ID: int = 0x8c4bfe5d

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetOutboxReadDate':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class MessagesGetQuickReplies(TLRequest):
    ID: int = 0xd483f2a8

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetQuickReplies':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class MessagesReorderQuickReplies(TLRequest):
    ID: int = 0x60331907

    def __init__(self, order: Any = None) -> None:
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.order or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReorderQuickReplies':
        order = reader.read_vector(lambda r: r.read_int32())
        return cls(order=order)


@register_tl
class MessagesCheckQuickReplyShortcut(TLRequest):
    ID: int = 0xf1d0fbd3

    def __init__(self, shortcut: Any = None) -> None:
        self.shortcut = shortcut

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.shortcut or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCheckQuickReplyShortcut':
        shortcut = reader.read_string()
        return cls(shortcut=shortcut)


@register_tl
class MessagesEditQuickReplyShortcut(TLRequest):
    ID: int = 0x5c003cef

    def __init__(self, shortcut_id: Any = None, shortcut: Any = None) -> None:
        self.shortcut_id = shortcut_id
        self.shortcut = shortcut

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)
        writer.write_string(self.shortcut or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditQuickReplyShortcut':
        shortcut_id = reader.read_int32()
        shortcut = reader.read_string()
        return cls(shortcut_id=shortcut_id, shortcut=shortcut)


@register_tl
class MessagesDeleteQuickReplyShortcut(TLRequest):
    ID: int = 0x3cc04740

    def __init__(self, shortcut_id: Any = None) -> None:
        self.shortcut_id = shortcut_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteQuickReplyShortcut':
        shortcut_id = reader.read_int32()
        return cls(shortcut_id=shortcut_id)


@register_tl
class MessagesGetQuickReplyMessages(TLRequest):
    ID: int = 0x94a495c3

    def __init__(self, id: Any = None, shortcut_id: Any = None, hash: Any = None) -> None:
        self.id = id
        self.shortcut_id = shortcut_id
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.shortcut_id or 0)
        if self.id is not None:
            writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetQuickReplyMessages':
        flags = reader.read_uint32()
        shortcut_id = reader.read_int32()
        id = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        hash = reader.read_int64()
        return cls(shortcut_id=shortcut_id, id=id, hash=hash)


@register_tl
class MessagesSendQuickReplyMessages(TLRequest):
    ID: int = 0x6c750de1

    def __init__(self, peer: Any = None, shortcut_id: Any = None, id: Any = None, random_id: Any = None) -> None:
        self.peer = peer
        self.shortcut_id = shortcut_id
        self.id = id
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.shortcut_id or 0)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.random_id or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendQuickReplyMessages':
        peer = reader.read_object()
        shortcut_id = reader.read_int32()
        id = reader.read_vector(lambda r: r.read_int32())
        random_id = reader.read_vector(lambda r: r.read_int64())
        return cls(peer=peer, shortcut_id=shortcut_id, id=id, random_id=random_id)


@register_tl
class MessagesDeleteQuickReplyMessages(TLRequest):
    ID: int = 0xe105e910

    def __init__(self, shortcut_id: Any = None, id: Any = None) -> None:
        self.shortcut_id = shortcut_id
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteQuickReplyMessages':
        shortcut_id = reader.read_int32()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(shortcut_id=shortcut_id, id=id)


@register_tl
class MessagesToggleDialogFilterTags(TLRequest):
    ID: int = 0xfd2dda49

    def __init__(self, enabled: Any = None) -> None:
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesToggleDialogFilterTags':
        enabled = reader.read_bool()
        return cls(enabled=enabled)


@register_tl
class MessagesGetMyStickers(TLRequest):
    ID: int = 0xd0b5e1fc

    def __init__(self, offset_id: Any = None, limit: Any = None) -> None:
        self.offset_id = offset_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.offset_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetMyStickers':
        offset_id = reader.read_int64()
        limit = reader.read_int32()
        return cls(offset_id=offset_id, limit=limit)


@register_tl
class MessagesGetEmojiStickerGroups(TLRequest):
    ID: int = 0x1dd840f5

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiStickerGroups':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class MessagesGetAvailableEffects(TLRequest):
    ID: int = 0xdea20a39

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetAvailableEffects':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class MessagesEditFactCheck(TLRequest):
    ID: int = 0x589ee75

    def __init__(self, peer: Any = None, msg_id: Any = None, text: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditFactCheck':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        text = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, text=text)


@register_tl
class MessagesDeleteFactCheck(TLRequest):
    ID: int = 0xd1da940c

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteFactCheck':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class MessagesGetFactCheck(TLRequest):
    ID: int = 0xb9cdc5ee

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.msg_id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetFactCheck':
        peer = reader.read_object()
        msg_id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class MessagesRequestMainWebView(TLRequest):
    ID: int = 0xc9e01e7b

    def __init__(self, compact: bool = False, fullscreen: bool = False, start_param: Any = None, theme_params: Any = None, peer: Any = None, bot: Any = None, platform: Any = None) -> None:
        self.compact = compact
        self.fullscreen = fullscreen
        self.start_param = start_param
        self.theme_params = theme_params
        self.peer = peer
        self.bot = bot
        self.platform = platform

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.compact:
            flags |= (1 << 7)
        if self.fullscreen:
            flags |= (1 << 8)
        if self.start_param is not None:
            flags |= (1 << 1)
        if self.theme_params is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.start_param is not None:
            writer.write_string(self.start_param or '')
        if self.theme_params is not None:
            if self.theme_params is not None and hasattr(self.theme_params, 'write'): self.theme_params.write(writer)
        writer.write_string(self.platform or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesRequestMainWebView':
        flags = reader.read_uint32()
        compact = bool(flags & (1 << 7))
        fullscreen = bool(flags & (1 << 8))
        peer = reader.read_object()
        bot = reader.read_object()
        start_param = reader.read_string() if (flags & (1 << 1)) else None
        theme_params = reader.read_object() if (flags & (1 << 0)) else None
        platform = reader.read_string()
        return cls(compact=compact, fullscreen=fullscreen, peer=peer, bot=bot, start_param=start_param, theme_params=theme_params, platform=platform)


@register_tl
class MessagesSendPaidReaction(TLRequest):
    ID: int = 0x58bbcb50

    def __init__(self, private: Any = None, peer: Any = None, msg_id: Any = None, count: Any = None, random_id: Any = None) -> None:
        self.private = private
        self.peer = peer
        self.msg_id = msg_id
        self.count = count
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.private is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int32(self.count or 0)
        writer.write_int64(self.random_id or 0)
        if self.private is not None:
            if self.private is not None and hasattr(self.private, 'write'): self.private.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSendPaidReaction':
        flags = reader.read_uint32()
        peer = reader.read_object()
        msg_id = reader.read_int32()
        count = reader.read_int32()
        random_id = reader.read_int64()
        private = reader.read_object() if (flags & (1 << 0)) else None
        return cls(peer=peer, msg_id=msg_id, count=count, random_id=random_id, private=private)


@register_tl
class MessagesTogglePaidReactionPrivacy(TLRequest):
    ID: int = 0x435885b5

    def __init__(self, peer: Any = None, msg_id: Any = None, private: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.private = private

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        if self.private is not None and hasattr(self.private, 'write'): self.private.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesTogglePaidReactionPrivacy':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        private = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, private=private)


@register_tl
class MessagesGetPaidReactionPrivacy(TLRequest):
    ID: int = 0x472455aa

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPaidReactionPrivacy':
        return cls()


@register_tl
class MessagesViewSponsoredMessage(TLRequest):
    ID: int = 0x269e3643

    def __init__(self, random_id: Any = None) -> None:
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.random_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesViewSponsoredMessage':
        random_id = reader.read_bytes()
        return cls(random_id=random_id)


@register_tl
class MessagesClickSponsoredMessage(TLRequest):
    ID: int = 0x8235057e

    def __init__(self, media: bool = False, fullscreen: bool = False, random_id: Any = None) -> None:
        self.media = media
        self.fullscreen = fullscreen
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.media:
            flags |= (1 << 0)
        if self.fullscreen:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_bytes(self.random_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesClickSponsoredMessage':
        flags = reader.read_uint32()
        media = bool(flags & (1 << 0))
        fullscreen = bool(flags & (1 << 1))
        random_id = reader.read_bytes()
        return cls(media=media, fullscreen=fullscreen, random_id=random_id)


@register_tl
class MessagesReportSponsoredMessage(TLRequest):
    ID: int = 0x12cbf0c4

    def __init__(self, random_id: Any = None, option: Any = None) -> None:
        self.random_id = random_id
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.random_id or b'')
        writer.write_bytes(self.option or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReportSponsoredMessage':
        random_id = reader.read_bytes()
        option = reader.read_bytes()
        return cls(random_id=random_id, option=option)


@register_tl
class MessagesGetSponsoredMessages(TLRequest):
    ID: int = 0x3d6ce850

    def __init__(self, msg_id: Any = None, peer: Any = None) -> None:
        self.msg_id = msg_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSponsoredMessages':
        flags = reader.read_uint32()
        peer = reader.read_object()
        msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class MessagesSavePreparedInlineMessage(TLRequest):
    ID: int = 0xf21f7f2f

    def __init__(self, peer_types: Any = None, result: Any = None, user_id: Any = None) -> None:
        self.peer_types = peer_types
        self.result = result
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer_types is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.result is not None and hasattr(self.result, 'write'): self.result.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        if self.peer_types is not None:
            writer.write_vector(self.peer_types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavePreparedInlineMessage':
        flags = reader.read_uint32()
        result = reader.read_object()
        user_id = reader.read_object()
        peer_types = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        return cls(result=result, user_id=user_id, peer_types=peer_types)


@register_tl
class MessagesGetPreparedInlineMessage(TLRequest):
    ID: int = 0x857ebdb8

    def __init__(self, bot: Any = None, id: Any = None) -> None:
        self.bot = bot
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPreparedInlineMessage':
        bot = reader.read_object()
        id = reader.read_string()
        return cls(bot=bot, id=id)


@register_tl
class MessagesSearchStickers(TLRequest):
    ID: int = 0x29b1c66a

    def __init__(self, emojis: bool = False, q: Any = None, emoticon: Any = None, lang_code: Any = None, offset: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.emojis = emojis
        self.q = q
        self.emoticon = emoticon
        self.lang_code = lang_code
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.emojis:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.q or '')
        writer.write_string(self.emoticon or '')
        writer.write_vector(self.lang_code or [], lambda w, x: w.write_string(x))
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchStickers':
        flags = reader.read_uint32()
        emojis = bool(flags & (1 << 0))
        q = reader.read_string()
        emoticon = reader.read_string()
        lang_code = reader.read_vector(lambda r: r.read_string())
        offset = reader.read_int32()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(emojis=emojis, q=q, emoticon=emoticon, lang_code=lang_code, offset=offset, limit=limit, hash=hash)


@register_tl
class MessagesReportMessagesDelivery(TLRequest):
    ID: int = 0x5a6d7395

    def __init__(self, push: bool = False, peer: Any = None, id: Any = None) -> None:
        self.push = push
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.push:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReportMessagesDelivery':
        flags = reader.read_uint32()
        push = bool(flags & (1 << 0))
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(push=push, peer=peer, id=id)


@register_tl
class MessagesGetSavedDialogsByID(TLRequest):
    ID: int = 0x6f6f9c96

    def __init__(self, parent_peer: Any = None, ids: Any = None) -> None:
        self.parent_peer = parent_peer
        self.ids = ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.parent_peer is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        writer.write_vector(self.ids or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetSavedDialogsByID':
        flags = reader.read_uint32()
        parent_peer = reader.read_object() if (flags & (1 << 1)) else None
        ids = reader.read_vector(lambda r: reader.read_object())
        return cls(parent_peer=parent_peer, ids=ids)


@register_tl
class MessagesReadSavedHistory(TLRequest):
    ID: int = 0xba4a3b5b

    def __init__(self, parent_peer: Any = None, peer: Any = None, max_id: Any = None) -> None:
        self.parent_peer = parent_peer
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadSavedHistory':
        parent_peer = reader.read_object()
        peer = reader.read_object()
        max_id = reader.read_int32()
        return cls(parent_peer=parent_peer, peer=peer, max_id=max_id)

