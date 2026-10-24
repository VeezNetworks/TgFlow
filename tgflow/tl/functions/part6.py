from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class StatsGetStoryPublicForwards(TLRequest):
    ID: int = 0xa6437ef6

    def __init__(self, peer: Any = None, id: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.peer = peer
        self.id = id
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGetStoryPublicForwards':
        peer = reader.read_object()
        id = reader.read_int32()
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(peer=peer, id=id, offset=offset, limit=limit)


@register_tl
class StatsGetPollStats(TLRequest):
    ID: int = 0xc27dfa68

    def __init__(self, dark: bool = False, peer: Any = None, msg_id: Any = None) -> None:
        self.dark = dark
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGetPollStats':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(dark=dark, peer=peer, msg_id=msg_id)


@register_tl
class ChatlistsExportChatlistInvite(TLRequest):
    ID: int = 0x8472478e

    def __init__(self, chatlist: Any = None, title: Any = None, peers: Any = None) -> None:
        self.chatlist = chatlist
        self.title = title
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)
        writer.write_string(self.title or '')
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsExportChatlistInvite':
        chatlist = reader.read_object()
        title = reader.read_string()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(chatlist=chatlist, title=title, peers=peers)


@register_tl
class ChatlistsDeleteExportedInvite(TLRequest):
    ID: int = 0x719c5c5e

    def __init__(self, chatlist: Any = None, slug: Any = None) -> None:
        self.chatlist = chatlist
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsDeleteExportedInvite':
        chatlist = reader.read_object()
        slug = reader.read_string()
        return cls(chatlist=chatlist, slug=slug)


@register_tl
class ChatlistsEditExportedInvite(TLRequest):
    ID: int = 0x653db63d

    def __init__(self, title: Any = None, peers: Any = None, chatlist: Any = None, slug: Any = None) -> None:
        self.title = title
        self.peers = peers
        self.chatlist = chatlist
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 1)
        if self.peers is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)
        writer.write_string(self.slug or '')
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.peers is not None:
            writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsEditExportedInvite':
        flags = reader.read_uint32()
        chatlist = reader.read_object()
        slug = reader.read_string()
        title = reader.read_string() if (flags & (1 << 1)) else None
        peers = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 2)) else None
        return cls(chatlist=chatlist, slug=slug, title=title, peers=peers)


@register_tl
class ChatlistsGetExportedInvites(TLRequest):
    ID: int = 0xce03da83

    def __init__(self, chatlist: Any = None) -> None:
        self.chatlist = chatlist

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsGetExportedInvites':
        chatlist = reader.read_object()
        return cls(chatlist=chatlist)


@register_tl
class ChatlistsCheckChatlistInvite(TLRequest):
    ID: int = 0x41c10fff

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsCheckChatlistInvite':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class ChatlistsJoinChatlistInvite(TLRequest):
    ID: int = 0xa6b1e39a

    def __init__(self, slug: Any = None, peers: Any = None) -> None:
        self.slug = slug
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsJoinChatlistInvite':
        slug = reader.read_string()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(slug=slug, peers=peers)


@register_tl
class ChatlistsGetChatlistUpdates(TLRequest):
    ID: int = 0x89419521

    def __init__(self, chatlist: Any = None) -> None:
        self.chatlist = chatlist

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsGetChatlistUpdates':
        chatlist = reader.read_object()
        return cls(chatlist=chatlist)


@register_tl
class ChatlistsJoinChatlistUpdates(TLRequest):
    ID: int = 0xe089f8f5

    def __init__(self, chatlist: Any = None, peers: Any = None) -> None:
        self.chatlist = chatlist
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsJoinChatlistUpdates':
        chatlist = reader.read_object()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(chatlist=chatlist, peers=peers)


@register_tl
class ChatlistsHideChatlistUpdates(TLRequest):
    ID: int = 0x66e486fb

    def __init__(self, chatlist: Any = None) -> None:
        self.chatlist = chatlist

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsHideChatlistUpdates':
        chatlist = reader.read_object()
        return cls(chatlist=chatlist)


@register_tl
class ChatlistsGetLeaveChatlistSuggestions(TLRequest):
    ID: int = 0xfdbcd714

    def __init__(self, chatlist: Any = None) -> None:
        self.chatlist = chatlist

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsGetLeaveChatlistSuggestions':
        chatlist = reader.read_object()
        return cls(chatlist=chatlist)


@register_tl
class ChatlistsLeaveChatlist(TLRequest):
    ID: int = 0x74fae13a

    def __init__(self, chatlist: Any = None, peers: Any = None) -> None:
        self.chatlist = chatlist
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chatlist is not None and hasattr(self.chatlist, 'write'): self.chatlist.write(writer)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsLeaveChatlist':
        chatlist = reader.read_object()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(chatlist=chatlist, peers=peers)


@register_tl
class StoriesCanSendStory(TLRequest):
    ID: int = 0x30eb63f0

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesCanSendStory':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class StoriesSendStory(TLRequest):
    ID: int = 0x8f9e6898

    def __init__(self, pinned: bool = False, noforwards: bool = False, fwd_modified: bool = False, media_areas: Any = None, caption: Any = None, entities: Any = None, period: Any = None, fwd_from_id: Any = None, fwd_from_story: Any = None, albums: Any = None, music: Any = None, peer: Any = None, media: Any = None, privacy_rules: Any = None, random_id: Any = None) -> None:
        self.pinned = pinned
        self.noforwards = noforwards
        self.fwd_modified = fwd_modified
        self.media_areas = media_areas
        self.caption = caption
        self.entities = entities
        self.period = period
        self.fwd_from_id = fwd_from_id
        self.fwd_from_story = fwd_from_story
        self.albums = albums
        self.music = music
        self.peer = peer
        self.media = media
        self.privacy_rules = privacy_rules
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 2)
        if self.noforwards:
            flags |= (1 << 4)
        if self.fwd_modified:
            flags |= (1 << 7)
        if self.media_areas is not None:
            flags |= (1 << 5)
        if self.caption is not None:
            flags |= (1 << 0)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.period is not None:
            flags |= (1 << 3)
        if self.fwd_from_id is not None:
            flags |= (1 << 6)
        if self.fwd_from_story is not None:
            flags |= (1 << 6)
        if self.albums is not None:
            flags |= (1 << 8)
        if self.music is not None:
            flags |= (1 << 9)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.media_areas is not None:
            writer.write_vector(self.media_areas or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.caption is not None:
            writer.write_string(self.caption or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.privacy_rules or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int64(self.random_id or 0)
        if self.period is not None:
            writer.write_int32(self.period or 0)
        if self.fwd_from_id is not None:
            if self.fwd_from_id is not None and hasattr(self.fwd_from_id, 'write'): self.fwd_from_id.write(writer)
        if self.fwd_from_story is not None:
            writer.write_int32(self.fwd_from_story or 0)
        if self.albums is not None:
            writer.write_vector(self.albums or [], lambda w, x: w.write_int32(x))
        if self.music is not None:
            if self.music is not None and hasattr(self.music, 'write'): self.music.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesSendStory':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 2))
        noforwards = bool(flags & (1 << 4))
        fwd_modified = bool(flags & (1 << 7))
        peer = reader.read_object()
        media = reader.read_object()
        media_areas = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 5)) else None
        caption = reader.read_string() if (flags & (1 << 0)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        privacy_rules = reader.read_vector(lambda r: reader.read_object())
        random_id = reader.read_int64()
        period = reader.read_int32() if (flags & (1 << 3)) else None
        fwd_from_id = reader.read_object() if (flags & (1 << 6)) else None
        fwd_from_story = reader.read_int32() if (flags & (1 << 6)) else None
        albums = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 8)) else None
        music = reader.read_object() if (flags & (1 << 9)) else None
        return cls(pinned=pinned, noforwards=noforwards, fwd_modified=fwd_modified, peer=peer, media=media, media_areas=media_areas, caption=caption, entities=entities, privacy_rules=privacy_rules, random_id=random_id, period=period, fwd_from_id=fwd_from_id, fwd_from_story=fwd_from_story, albums=albums, music=music)


@register_tl
class StoriesEditStory(TLRequest):
    ID: int = 0x2c63a72b

    def __init__(self, media: Any = None, media_areas: Any = None, caption: Any = None, entities: Any = None, privacy_rules: Any = None, music: Any = None, peer: Any = None, id: Any = None) -> None:
        self.media = media
        self.media_areas = media_areas
        self.caption = caption
        self.entities = entities
        self.privacy_rules = privacy_rules
        self.music = music
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.media is not None:
            flags |= (1 << 0)
        if self.media_areas is not None:
            flags |= (1 << 3)
        if self.caption is not None:
            flags |= (1 << 1)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.privacy_rules is not None:
            flags |= (1 << 2)
        if self.music is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.media_areas is not None:
            writer.write_vector(self.media_areas or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.caption is not None:
            writer.write_string(self.caption or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.privacy_rules is not None:
            writer.write_vector(self.privacy_rules or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.music is not None:
            if self.music is not None and hasattr(self.music, 'write'): self.music.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesEditStory':
        flags = reader.read_uint32()
        peer = reader.read_object()
        id = reader.read_int32()
        media = reader.read_object() if (flags & (1 << 0)) else None
        media_areas = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        caption = reader.read_string() if (flags & (1 << 1)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        privacy_rules = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 2)) else None
        music = reader.read_object() if (flags & (1 << 4)) else None
        return cls(peer=peer, id=id, media=media, media_areas=media_areas, caption=caption, entities=entities, privacy_rules=privacy_rules, music=music)


@register_tl
class StoriesDeleteStories(TLRequest):
    ID: int = 0xae59db5f

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesDeleteStories':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class StoriesTogglePinned(TLRequest):
    ID: int = 0x9a75a1ef

    def __init__(self, peer: Any = None, id: Any = None, pinned: Any = None) -> None:
        self.peer = peer
        self.id = id
        self.pinned = pinned

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))
        writer.write_bool(bool(self.pinned))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesTogglePinned':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        pinned = reader.read_bool()
        return cls(peer=peer, id=id, pinned=pinned)


@register_tl
class StoriesGetAllStories(TLRequest):
    ID: int = 0xeeb0d625

    def __init__(self, next: bool = False, hidden: bool = False, state: Any = None) -> None:
        self.next = next
        self.hidden = hidden
        self.state = state

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next:
            flags |= (1 << 1)
        if self.hidden:
            flags |= (1 << 2)
        if self.state is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.state is not None:
            writer.write_string(self.state or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetAllStories':
        flags = reader.read_uint32()
        next = bool(flags & (1 << 1))
        hidden = bool(flags & (1 << 2))
        state = reader.read_string() if (flags & (1 << 0)) else None
        return cls(next=next, hidden=hidden, state=state)


@register_tl
class StoriesGetPinnedStories(TLRequest):
    ID: int = 0x5821a5dc

    def __init__(self, peer: Any = None, offset_id: Any = None, limit: Any = None) -> None:
        self.peer = peer
        self.offset_id = offset_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetPinnedStories':
        peer = reader.read_object()
        offset_id = reader.read_int32()
        limit = reader.read_int32()
        return cls(peer=peer, offset_id=offset_id, limit=limit)


@register_tl
class StoriesGetStoriesArchive(TLRequest):
    ID: int = 0xb4352016

    def __init__(self, peer: Any = None, offset_id: Any = None, limit: Any = None) -> None:
        self.peer = peer
        self.offset_id = offset_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetStoriesArchive':
        peer = reader.read_object()
        offset_id = reader.read_int32()
        limit = reader.read_int32()
        return cls(peer=peer, offset_id=offset_id, limit=limit)


@register_tl
class StoriesGetStoriesByID(TLRequest):
    ID: int = 0x5774ca74

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetStoriesByID':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class StoriesToggleAllStoriesHidden(TLRequest):
    ID: int = 0x7c2557c4

    def __init__(self, hidden: Any = None) -> None:
        self.hidden = hidden

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.hidden))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesToggleAllStoriesHidden':
        hidden = reader.read_bool()
        return cls(hidden=hidden)


@register_tl
class StoriesReadStories(TLRequest):
    ID: int = 0xa556dac8

    def __init__(self, peer: Any = None, max_id: Any = None) -> None:
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesReadStories':
        peer = reader.read_object()
        max_id = reader.read_int32()
        return cls(peer=peer, max_id=max_id)


@register_tl
class StoriesIncrementStoryViews(TLRequest):
    ID: int = 0xb2028afb

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesIncrementStoryViews':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class StoriesGetStoryViewsList(TLRequest):
    ID: int = 0x7ed23c57

    def __init__(self, just_contacts: bool = False, reactions_first: bool = False, forwards_first: bool = False, q: Any = None, peer: Any = None, id: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.just_contacts = just_contacts
        self.reactions_first = reactions_first
        self.forwards_first = forwards_first
        self.q = q
        self.peer = peer
        self.id = id
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.just_contacts:
            flags |= (1 << 0)
        if self.reactions_first:
            flags |= (1 << 2)
        if self.forwards_first:
            flags |= (1 << 3)
        if self.q is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.q is not None:
            writer.write_string(self.q or '')
        writer.write_int32(self.id or 0)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetStoryViewsList':
        flags = reader.read_uint32()
        just_contacts = bool(flags & (1 << 0))
        reactions_first = bool(flags & (1 << 2))
        forwards_first = bool(flags & (1 << 3))
        peer = reader.read_object()
        q = reader.read_string() if (flags & (1 << 1)) else None
        id = reader.read_int32()
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(just_contacts=just_contacts, reactions_first=reactions_first, forwards_first=forwards_first, peer=peer, q=q, id=id, offset=offset, limit=limit)


@register_tl
class StoriesGetStoriesViews(TLRequest):
    ID: int = 0x28e16cc8

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetStoriesViews':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class StoriesExportStoryLink(TLRequest):
    ID: int = 0x7b8def20

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesExportStoryLink':
        peer = reader.read_object()
        id = reader.read_int32()
        return cls(peer=peer, id=id)


@register_tl
class StoriesReport(TLRequest):
    ID: int = 0x19d8eb45

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
    def read(cls, reader: TLReader) -> 'StoriesReport':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        option = reader.read_bytes()
        message = reader.read_string()
        return cls(peer=peer, id=id, option=option, message=message)


@register_tl
class StoriesActivateStealthMode(TLRequest):
    ID: int = 0x57bbd166

    def __init__(self, past: bool = False, future: bool = False) -> None:
        self.past = past
        self.future = future

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.past:
            flags |= (1 << 0)
        if self.future:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesActivateStealthMode':
        flags = reader.read_uint32()
        past = bool(flags & (1 << 0))
        future = bool(flags & (1 << 1))
        return cls(past=past, future=future)


@register_tl
class StoriesSendReaction(TLRequest):
    ID: int = 0x7fd736b2

    def __init__(self, add_to_recent: bool = False, peer: Any = None, story_id: Any = None, reaction: Any = None) -> None:
        self.add_to_recent = add_to_recent
        self.peer = peer
        self.story_id = story_id
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.add_to_recent:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.story_id or 0)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesSendReaction':
        flags = reader.read_uint32()
        add_to_recent = bool(flags & (1 << 0))
        peer = reader.read_object()
        story_id = reader.read_int32()
        reaction = reader.read_object()
        return cls(add_to_recent=add_to_recent, peer=peer, story_id=story_id, reaction=reaction)


@register_tl
class StoriesGetPeerStories(TLRequest):
    ID: int = 0x2c4ada50

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetPeerStories':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class StoriesGetAllReadPeerStories(TLRequest):
    ID: int = 0x9b5ae7f9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetAllReadPeerStories':
        return cls()


@register_tl
class StoriesGetPeerMaxIDs(TLRequest):
    ID: int = 0x78499170

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetPeerMaxIDs':
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id)


@register_tl
class StoriesGetChatsToSend(TLRequest):
    ID: int = 0xa56a8b60

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetChatsToSend':
        return cls()


@register_tl
class StoriesTogglePeerStoriesHidden(TLRequest):
    ID: int = 0xbd0415c4

    def __init__(self, peer: Any = None, hidden: Any = None) -> None:
        self.peer = peer
        self.hidden = hidden

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bool(bool(self.hidden))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesTogglePeerStoriesHidden':
        peer = reader.read_object()
        hidden = reader.read_bool()
        return cls(peer=peer, hidden=hidden)


@register_tl
class StoriesGetStoryReactionsList(TLRequest):
    ID: int = 0xb9b2881f

    def __init__(self, forwards_first: bool = False, reaction: Any = None, offset: Any = None, peer: Any = None, id: Any = None, limit: Any = None) -> None:
        self.forwards_first = forwards_first
        self.reaction = reaction
        self.offset = offset
        self.peer = peer
        self.id = id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.forwards_first:
            flags |= (1 << 2)
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
    def read(cls, reader: TLReader) -> 'StoriesGetStoryReactionsList':
        flags = reader.read_uint32()
        forwards_first = bool(flags & (1 << 2))
        peer = reader.read_object()
        id = reader.read_int32()
        reaction = reader.read_object() if (flags & (1 << 0)) else None
        offset = reader.read_string() if (flags & (1 << 1)) else None
        limit = reader.read_int32()
        return cls(forwards_first=forwards_first, peer=peer, id=id, reaction=reaction, offset=offset, limit=limit)


@register_tl
class StoriesTogglePinnedToTop(TLRequest):
    ID: int = 0xb297e9b

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesTogglePinnedToTop':
        peer = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, id=id)


@register_tl
class StoriesSearchPosts(TLRequest):
    ID: int = 0xd1810907

    def __init__(self, hashtag: Any = None, area: Any = None, peer: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.hashtag = hashtag
        self.area = area
        self.peer = peer
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.hashtag is not None:
            flags |= (1 << 0)
        if self.area is not None:
            flags |= (1 << 1)
        if self.peer is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.hashtag is not None:
            writer.write_string(self.hashtag or '')
        if self.area is not None:
            if self.area is not None and hasattr(self.area, 'write'): self.area.write(writer)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesSearchPosts':
        flags = reader.read_uint32()
        hashtag = reader.read_string() if (flags & (1 << 0)) else None
        area = reader.read_object() if (flags & (1 << 1)) else None
        peer = reader.read_object() if (flags & (1 << 2)) else None
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(hashtag=hashtag, area=area, peer=peer, offset=offset, limit=limit)


@register_tl
class StoriesCreateAlbum(TLRequest):
    ID: int = 0xa36396e5

    def __init__(self, peer: Any = None, title: Any = None, stories: Any = None) -> None:
        self.peer = peer
        self.title = title
        self.stories = stories

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.title or '')
        writer.write_vector(self.stories or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesCreateAlbum':
        peer = reader.read_object()
        title = reader.read_string()
        stories = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, title=title, stories=stories)


@register_tl
class StoriesUpdateAlbum(TLRequest):
    ID: int = 0x5e5259b6

    def __init__(self, title: Any = None, delete_stories: Any = None, add_stories: Any = None, order: Any = None, peer: Any = None, album_id: Any = None) -> None:
        self.title = title
        self.delete_stories = delete_stories
        self.add_stories = add_stories
        self.order = order
        self.peer = peer
        self.album_id = album_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        if self.delete_stories is not None:
            flags |= (1 << 1)
        if self.add_stories is not None:
            flags |= (1 << 2)
        if self.order is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.album_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.delete_stories is not None:
            writer.write_vector(self.delete_stories or [], lambda w, x: w.write_int32(x))
        if self.add_stories is not None:
            writer.write_vector(self.add_stories or [], lambda w, x: w.write_int32(x))
        if self.order is not None:
            writer.write_vector(self.order or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesUpdateAlbum':
        flags = reader.read_uint32()
        peer = reader.read_object()
        album_id = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        delete_stories = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 1)) else None
        add_stories = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 2)) else None
        order = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 3)) else None
        return cls(peer=peer, album_id=album_id, title=title, delete_stories=delete_stories, add_stories=add_stories, order=order)


@register_tl
class StoriesReorderAlbums(TLRequest):
    ID: int = 0x8535fbd9

    def __init__(self, peer: Any = None, order: Any = None) -> None:
        self.peer = peer
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.order or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesReorderAlbums':
        peer = reader.read_object()
        order = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, order=order)


@register_tl
class StoriesDeleteAlbum(TLRequest):
    ID: int = 0x8d3456d0

    def __init__(self, peer: Any = None, album_id: Any = None) -> None:
        self.peer = peer
        self.album_id = album_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.album_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesDeleteAlbum':
        peer = reader.read_object()
        album_id = reader.read_int32()
        return cls(peer=peer, album_id=album_id)


@register_tl
class StoriesGetAlbums(TLRequest):
    ID: int = 0x25b3eac7

    def __init__(self, peer: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetAlbums':
        peer = reader.read_object()
        hash = reader.read_int64()
        return cls(peer=peer, hash=hash)


@register_tl
class StoriesGetAlbumStories(TLRequest):
    ID: int = 0xac806d61

    def __init__(self, peer: Any = None, album_id: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.peer = peer
        self.album_id = album_id
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.album_id or 0)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesGetAlbumStories':
        peer = reader.read_object()
        album_id = reader.read_int32()
        offset = reader.read_int32()
        limit = reader.read_int32()
        return cls(peer=peer, album_id=album_id, offset=offset, limit=limit)


@register_tl
class StoriesStartLive(TLRequest):
    ID: int = 0xd069ccde

    def __init__(self, pinned: bool = False, noforwards: bool = False, rtmp_stream: bool = False, caption: Any = None, entities: Any = None, messages_enabled: Any = None, send_paid_messages_stars: Any = None, peer: Any = None, privacy_rules: Any = None, random_id: Any = None) -> None:
        self.pinned = pinned
        self.noforwards = noforwards
        self.rtmp_stream = rtmp_stream
        self.caption = caption
        self.entities = entities
        self.messages_enabled = messages_enabled
        self.send_paid_messages_stars = send_paid_messages_stars
        self.peer = peer
        self.privacy_rules = privacy_rules
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 2)
        if self.noforwards:
            flags |= (1 << 4)
        if self.rtmp_stream:
            flags |= (1 << 5)
        if self.caption is not None:
            flags |= (1 << 0)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.messages_enabled is not None:
            flags |= (1 << 6)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 7)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.caption is not None:
            writer.write_string(self.caption or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.privacy_rules or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int64(self.random_id or 0)
        if self.messages_enabled is not None:
            writer.write_bool(bool(self.messages_enabled))
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesStartLive':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 2))
        noforwards = bool(flags & (1 << 4))
        rtmp_stream = bool(flags & (1 << 5))
        peer = reader.read_object()
        caption = reader.read_string() if (flags & (1 << 0)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        privacy_rules = reader.read_vector(lambda r: reader.read_object())
        random_id = reader.read_int64()
        messages_enabled = reader.read_bool() if (flags & (1 << 6)) else None
        send_paid_messages_stars = reader.read_int64() if (flags & (1 << 7)) else None
        return cls(pinned=pinned, noforwards=noforwards, rtmp_stream=rtmp_stream, peer=peer, caption=caption, entities=entities, privacy_rules=privacy_rules, random_id=random_id, messages_enabled=messages_enabled, send_paid_messages_stars=send_paid_messages_stars)


@register_tl
class PremiumGetBoostsList(TLRequest):
    ID: int = 0x60f67660

    def __init__(self, gifts: bool = False, peer: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.gifts = gifts
        self.peer = peer
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.gifts:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumGetBoostsList':
        flags = reader.read_uint32()
        gifts = bool(flags & (1 << 0))
        peer = reader.read_object()
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(gifts=gifts, peer=peer, offset=offset, limit=limit)


@register_tl
class PremiumGetMyBoosts(TLRequest):
    ID: int = 0xbe77b4a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumGetMyBoosts':
        return cls()


@register_tl
class PremiumApplyBoost(TLRequest):
    ID: int = 0x6b7da746

    def __init__(self, slots: Any = None, peer: Any = None) -> None:
        self.slots = slots
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.slots is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.slots is not None:
            writer.write_vector(self.slots or [], lambda w, x: w.write_int32(x))
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumApplyBoost':
        flags = reader.read_uint32()
        slots = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        peer = reader.read_object()
        return cls(slots=slots, peer=peer)


@register_tl
class PremiumGetBoostsStatus(TLRequest):
    ID: int = 0x42f1f61

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumGetBoostsStatus':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class PremiumGetUserBoosts(TLRequest):
    ID: int = 0x39854d1f

    def __init__(self, peer: Any = None, user_id: Any = None) -> None:
        self.peer = peer
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumGetUserBoosts':
        peer = reader.read_object()
        user_id = reader.read_object()
        return cls(peer=peer, user_id=user_id)


@register_tl
class SmsjobsIsEligibleToJoin(TLRequest):
    ID: int = 0xedc39d0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsIsEligibleToJoin':
        return cls()


@register_tl
class SmsjobsJoin(TLRequest):
    ID: int = 0xa74ece2d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsJoin':
        return cls()


@register_tl
class SmsjobsLeave(TLRequest):
    ID: int = 0x9898ad73

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsLeave':
        return cls()


@register_tl
class SmsjobsUpdateSettings(TLRequest):
    ID: int = 0x93fa0bf

    def __init__(self, allow_international: bool = False) -> None:
        self.allow_international = allow_international

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.allow_international:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsUpdateSettings':
        flags = reader.read_uint32()
        allow_international = bool(flags & (1 << 0))
        return cls(allow_international=allow_international)


@register_tl
class SmsjobsGetStatus(TLRequest):
    ID: int = 0x10a698e8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsGetStatus':
        return cls()


@register_tl
class SmsjobsGetSmsJob(TLRequest):
    ID: int = 0x778d902f

    def __init__(self, job_id: Any = None) -> None:
        self.job_id = job_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.job_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsGetSmsJob':
        job_id = reader.read_string()
        return cls(job_id=job_id)


@register_tl
class SmsjobsFinishJob(TLRequest):
    ID: int = 0x4f1ebf24

    def __init__(self, error: Any = None, job_id: Any = None) -> None:
        self.error = error
        self.job_id = job_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.error is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.job_id or '')
        if self.error is not None:
            writer.write_string(self.error or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsFinishJob':
        flags = reader.read_uint32()
        job_id = reader.read_string()
        error = reader.read_string() if (flags & (1 << 0)) else None
        return cls(job_id=job_id, error=error)


@register_tl
class FragmentGetCollectibleInfo(TLRequest):
    ID: int = 0xbe1e85ba

    def __init__(self, collectible: Any = None) -> None:
        self.collectible = collectible

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.collectible is not None and hasattr(self.collectible, 'write'): self.collectible.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'FragmentGetCollectibleInfo':
        collectible = reader.read_object()
        return cls(collectible=collectible)


@register_tl
class AicomposeCreateTone(TLRequest):
    ID: int = 0x4aa83913

    def __init__(self, display_author: bool = False, emoji_id: Any = None, title: Any = None, prompt: Any = None) -> None:
        self.display_author = display_author
        self.emoji_id = emoji_id
        self.title = title
        self.prompt = prompt

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.display_author:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.emoji_id or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.prompt or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeCreateTone':
        flags = reader.read_uint32()
        display_author = bool(flags & (1 << 0))
        emoji_id = reader.read_int64()
        title = reader.read_string()
        prompt = reader.read_string()
        return cls(display_author=display_author, emoji_id=emoji_id, title=title, prompt=prompt)


@register_tl
class AicomposeUpdateTone(TLRequest):
    ID: int = 0x903bcf59

    def __init__(self, display_author: Any = None, emoji_id: Any = None, title: Any = None, prompt: Any = None, tone: Any = None) -> None:
        self.display_author = display_author
        self.emoji_id = emoji_id
        self.title = title
        self.prompt = prompt
        self.tone = tone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.display_author is not None:
            flags |= (1 << 0)
        if self.emoji_id is not None:
            flags |= (1 << 1)
        if self.title is not None:
            flags |= (1 << 2)
        if self.prompt is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.tone is not None and hasattr(self.tone, 'write'): self.tone.write(writer)
        if self.display_author is not None:
            writer.write_bool(bool(self.display_author))
        if self.emoji_id is not None:
            writer.write_int64(self.emoji_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.prompt is not None:
            writer.write_string(self.prompt or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeUpdateTone':
        flags = reader.read_uint32()
        tone = reader.read_object()
        display_author = reader.read_bool() if (flags & (1 << 0)) else None
        emoji_id = reader.read_int64() if (flags & (1 << 1)) else None
        title = reader.read_string() if (flags & (1 << 2)) else None
        prompt = reader.read_string() if (flags & (1 << 3)) else None
        return cls(tone=tone, display_author=display_author, emoji_id=emoji_id, title=title, prompt=prompt)


@register_tl
class AicomposeSaveTone(TLRequest):
    ID: int = 0x1782cbb1

    def __init__(self, tone: Any = None, unsave: Any = None) -> None:
        self.tone = tone
        self.unsave = unsave

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.tone is not None and hasattr(self.tone, 'write'): self.tone.write(writer)
        writer.write_bool(bool(self.unsave))

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeSaveTone':
        tone = reader.read_object()
        unsave = reader.read_bool()
        return cls(tone=tone, unsave=unsave)


@register_tl
class AicomposeDeleteTone(TLRequest):
    ID: int = 0xdd39316a

    def __init__(self, tone: Any = None) -> None:
        self.tone = tone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.tone is not None and hasattr(self.tone, 'write'): self.tone.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeDeleteTone':
        tone = reader.read_object()
        return cls(tone=tone)


@register_tl
class AicomposeGetTone(TLRequest):
    ID: int = 0xb2e8ba03

    def __init__(self, tone: Any = None) -> None:
        self.tone = tone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.tone is not None and hasattr(self.tone, 'write'): self.tone.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeGetTone':
        tone = reader.read_object()
        return cls(tone=tone)


@register_tl
class AicomposeGetTones(TLRequest):
    ID: int = 0xabd59201

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeGetTones':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AicomposeGetToneExample(TLRequest):
    ID: int = 0xd1b4ab14

    def __init__(self, tone: Any = None, num: Any = None) -> None:
        self.tone = tone
        self.num = num

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.tone is not None and hasattr(self.tone, 'write'): self.tone.write(writer)
        writer.write_int32(self.num or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeGetToneExample':
        tone = reader.read_object()
        num = reader.read_int32()
        return cls(tone=tone, num=num)

