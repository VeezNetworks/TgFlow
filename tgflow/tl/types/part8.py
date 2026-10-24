from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class ChannelAdminLogEventActionToggleAutotranslation(TLObject):
    ID: int = 0xc517f77e

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleAutotranslation':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionParticipantEditRank(TLObject):
    ID: int = 0x5806b4ec

    def __init__(self, user_id: Any = None, prev_rank: Any = None, new_rank: Any = None) -> None:
        self.user_id = user_id
        self.prev_rank = prev_rank
        self.new_rank = new_rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(self.prev_rank or '')
        writer.write_string(self.new_rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantEditRank':
        user_id = reader.read_int64()
        prev_rank = reader.read_string()
        new_rank = reader.read_string()
        return cls(user_id=user_id, prev_rank=prev_rank, new_rank=new_rank)


@register_tl
class ChannelAdminLogEvent(TLObject):
    ID: int = 0x1fad68cd

    def __init__(self, id: Any = None, date: Any = None, user_id: Any = None, action: Any = None) -> None:
        self.id = id
        self.date = date
        self.user_id = user_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.user_id or 0)
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEvent':
        id = reader.read_int64()
        date = reader.read_int32()
        user_id = reader.read_int64()
        action = reader.read_object()
        return cls(id=id, date=date, user_id=user_id, action=action)


@register_tl
class ChannelsAdminLogResults(TLObject):
    ID: int = 0xed8af74d

    def __init__(self, events: Any = None, chats: Any = None, users: Any = None) -> None:
        self.events = events
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.events or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsAdminLogResults':
        events = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(events=events, chats=chats, users=users)


@register_tl
class ChannelAdminLogEventsFilter(TLObject):
    ID: int = 0xea107ae4

    def __init__(self, join: bool = False, leave: bool = False, invite: bool = False, ban: bool = False, unban: bool = False, kick: bool = False, unkick: bool = False, promote: bool = False, demote: bool = False, info: bool = False, settings: bool = False, pinned: bool = False, edit: bool = False, delete: bool = False, group_call: bool = False, invites: bool = False, send: bool = False, forums: bool = False, sub_extend: bool = False, edit_rank: bool = False) -> None:
        self.join = join
        self.leave = leave
        self.invite = invite
        self.ban = ban
        self.unban = unban
        self.kick = kick
        self.unkick = unkick
        self.promote = promote
        self.demote = demote
        self.info = info
        self.settings = settings
        self.pinned = pinned
        self.edit = edit
        self.delete = delete
        self.group_call = group_call
        self.invites = invites
        self.send = send
        self.forums = forums
        self.sub_extend = sub_extend
        self.edit_rank = edit_rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.join:
            flags |= (1 << 0)
        if self.leave:
            flags |= (1 << 1)
        if self.invite:
            flags |= (1 << 2)
        if self.ban:
            flags |= (1 << 3)
        if self.unban:
            flags |= (1 << 4)
        if self.kick:
            flags |= (1 << 5)
        if self.unkick:
            flags |= (1 << 6)
        if self.promote:
            flags |= (1 << 7)
        if self.demote:
            flags |= (1 << 8)
        if self.info:
            flags |= (1 << 9)
        if self.settings:
            flags |= (1 << 10)
        if self.pinned:
            flags |= (1 << 11)
        if self.edit:
            flags |= (1 << 12)
        if self.delete:
            flags |= (1 << 13)
        if self.group_call:
            flags |= (1 << 14)
        if self.invites:
            flags |= (1 << 15)
        if self.send:
            flags |= (1 << 16)
        if self.forums:
            flags |= (1 << 17)
        if self.sub_extend:
            flags |= (1 << 18)
        if self.edit_rank:
            flags |= (1 << 19)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventsFilter':
        flags = reader.read_uint32()
        join = bool(flags & (1 << 0))
        leave = bool(flags & (1 << 1))
        invite = bool(flags & (1 << 2))
        ban = bool(flags & (1 << 3))
        unban = bool(flags & (1 << 4))
        kick = bool(flags & (1 << 5))
        unkick = bool(flags & (1 << 6))
        promote = bool(flags & (1 << 7))
        demote = bool(flags & (1 << 8))
        info = bool(flags & (1 << 9))
        settings = bool(flags & (1 << 10))
        pinned = bool(flags & (1 << 11))
        edit = bool(flags & (1 << 12))
        delete = bool(flags & (1 << 13))
        group_call = bool(flags & (1 << 14))
        invites = bool(flags & (1 << 15))
        send = bool(flags & (1 << 16))
        forums = bool(flags & (1 << 17))
        sub_extend = bool(flags & (1 << 18))
        edit_rank = bool(flags & (1 << 19))
        return cls(join=join, leave=leave, invite=invite, ban=ban, unban=unban, kick=kick, unkick=unkick, promote=promote, demote=demote, info=info, settings=settings, pinned=pinned, edit=edit, delete=delete, group_call=group_call, invites=invites, send=send, forums=forums, sub_extend=sub_extend, edit_rank=edit_rank)


@register_tl
class PopularContact(TLObject):
    ID: int = 0x5ce14175

    def __init__(self, client_id: Any = None, importers: Any = None) -> None:
        self.client_id = client_id
        self.importers = importers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.client_id or 0)
        writer.write_int32(self.importers or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PopularContact':
        client_id = reader.read_int64()
        importers = reader.read_int32()
        return cls(client_id=client_id, importers=importers)


@register_tl
class MessagesFavedStickersNotModified(TLObject):
    ID: int = 0x9e8fa6d3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFavedStickersNotModified':
        return cls()


@register_tl
class MessagesFavedStickers(TLObject):
    ID: int = 0x2cb51097

    def __init__(self, hash: Any = None, packs: Any = None, stickers: Any = None) -> None:
        self.hash = hash
        self.packs = packs
        self.stickers = stickers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.packs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFavedStickers':
        hash = reader.read_int64()
        packs = reader.read_vector(lambda r: reader.read_object())
        stickers = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, packs=packs, stickers=stickers)


@register_tl
class RecentMeUrlUnknown(TLObject):
    ID: int = 0x46e1d13d

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'RecentMeUrlUnknown':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class RecentMeUrlUser(TLObject):
    ID: int = 0xb92c09e2

    def __init__(self, url: Any = None, user_id: Any = None) -> None:
        self.url = url
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'RecentMeUrlUser':
        url = reader.read_string()
        user_id = reader.read_int64()
        return cls(url=url, user_id=user_id)


@register_tl
class RecentMeUrlChat(TLObject):
    ID: int = 0xb2da71d2

    def __init__(self, url: Any = None, chat_id: Any = None) -> None:
        self.url = url
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'RecentMeUrlChat':
        url = reader.read_string()
        chat_id = reader.read_int64()
        return cls(url=url, chat_id=chat_id)


@register_tl
class RecentMeUrlChatInvite(TLObject):
    ID: int = 0xeb49081d

    def __init__(self, url: Any = None, chat_invite: Any = None) -> None:
        self.url = url
        self.chat_invite = chat_invite

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        if self.chat_invite is not None and hasattr(self.chat_invite, 'write'): self.chat_invite.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RecentMeUrlChatInvite':
        url = reader.read_string()
        chat_invite = reader.read_object()
        return cls(url=url, chat_invite=chat_invite)


@register_tl
class RecentMeUrlStickerSet(TLObject):
    ID: int = 0xbc0a57dc

    def __init__(self, url: Any = None, set: Any = None) -> None:
        self.url = url
        self.set = set

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        if self.set is not None and hasattr(self.set, 'write'): self.set.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RecentMeUrlStickerSet':
        url = reader.read_string()
        set = reader.read_object()
        return cls(url=url, set=set)


@register_tl
class HelpRecentMeUrls(TLObject):
    ID: int = 0xe0310d7

    def __init__(self, urls: Any = None, chats: Any = None, users: Any = None) -> None:
        self.urls = urls
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.urls or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpRecentMeUrls':
        urls = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(urls=urls, chats=chats, users=users)


@register_tl
class InputSingleMedia(TLObject):
    ID: int = 0x1cc6e91f

    def __init__(self, entities: Any = None, media: Any = None, random_id: Any = None, message: Any = None) -> None:
        self.entities = entities
        self.media = media
        self.random_id = random_id
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.entities is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        writer.write_int64(self.random_id or 0)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSingleMedia':
        flags = reader.read_uint32()
        media = reader.read_object()
        random_id = reader.read_int64()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        return cls(media=media, random_id=random_id, message=message, entities=entities)


@register_tl
class WebAuthorization(TLObject):
    ID: int = 0xa6f8f452

    def __init__(self, hash: Any = None, bot_id: Any = None, domain: Any = None, browser: Any = None, platform: Any = None, date_created: Any = None, date_active: Any = None, ip: Any = None, region: Any = None) -> None:
        self.hash = hash
        self.bot_id = bot_id
        self.domain = domain
        self.browser = browser
        self.platform = platform
        self.date_created = date_created
        self.date_active = date_active
        self.ip = ip
        self.region = region

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_int64(self.bot_id or 0)
        writer.write_string(self.domain or '')
        writer.write_string(self.browser or '')
        writer.write_string(self.platform or '')
        writer.write_int32(self.date_created or 0)
        writer.write_int32(self.date_active or 0)
        writer.write_string(self.ip or '')
        writer.write_string(self.region or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'WebAuthorization':
        hash = reader.read_int64()
        bot_id = reader.read_int64()
        domain = reader.read_string()
        browser = reader.read_string()
        platform = reader.read_string()
        date_created = reader.read_int32()
        date_active = reader.read_int32()
        ip = reader.read_string()
        region = reader.read_string()
        return cls(hash=hash, bot_id=bot_id, domain=domain, browser=browser, platform=platform, date_created=date_created, date_active=date_active, ip=ip, region=region)


@register_tl
class AccountWebAuthorizations(TLObject):
    ID: int = 0xed56c9fc

    def __init__(self, authorizations: Any = None, users: Any = None) -> None:
        self.authorizations = authorizations
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.authorizations or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountWebAuthorizations':
        authorizations = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(authorizations=authorizations, users=users)


@register_tl
class InputMessageID(TLObject):
    ID: int = 0xa676a322

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessageID':
        id = reader.read_int32()
        return cls(id=id)


@register_tl
class InputMessageReplyTo(TLObject):
    ID: int = 0xbad88395

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessageReplyTo':
        id = reader.read_int32()
        return cls(id=id)


@register_tl
class InputMessagePinned(TLObject):
    ID: int = 0x86872538

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagePinned':
        return cls()


@register_tl
class InputMessageCallbackQuery(TLObject):
    ID: int = 0xacfa1a7e

    def __init__(self, id: Any = None, query_id: Any = None) -> None:
        self.id = id
        self.query_id = query_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.query_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessageCallbackQuery':
        id = reader.read_int32()
        query_id = reader.read_int64()
        return cls(id=id, query_id=query_id)


@register_tl
class InputDialogPeer(TLObject):
    ID: int = 0xfcaafeb7

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputDialogPeer':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class InputDialogPeerFolder(TLObject):
    ID: int = 0x64600527

    def __init__(self, folder_id: Any = None) -> None:
        self.folder_id = folder_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.folder_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputDialogPeerFolder':
        folder_id = reader.read_int32()
        return cls(folder_id=folder_id)


@register_tl
class DialogPeer(TLObject):
    ID: int = 0xe56dbf05

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogPeer':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class DialogPeerFolder(TLObject):
    ID: int = 0x514519e2

    def __init__(self, folder_id: Any = None) -> None:
        self.folder_id = folder_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.folder_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogPeerFolder':
        folder_id = reader.read_int32()
        return cls(folder_id=folder_id)


@register_tl
class MessagesFoundStickerSetsNotModified(TLObject):
    ID: int = 0xd54b65d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFoundStickerSetsNotModified':
        return cls()


@register_tl
class MessagesFoundStickerSets(TLObject):
    ID: int = 0x8af09dd2

    def __init__(self, hash: Any = None, sets: Any = None) -> None:
        self.hash = hash
        self.sets = sets

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.sets or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFoundStickerSets':
        hash = reader.read_int64()
        sets = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, sets=sets)


@register_tl
class FileHash(TLObject):
    ID: int = 0xf39b035c

    def __init__(self, offset: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_bytes(self.hash or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'FileHash':
        offset = reader.read_int64()
        limit = reader.read_int32()
        hash = reader.read_bytes()
        return cls(offset=offset, limit=limit, hash=hash)


@register_tl
class InputClientProxy(TLObject):
    ID: int = 0x75588b3f

    def __init__(self, address: Any = None, port: Any = None) -> None:
        self.address = address
        self.port = port

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.address or '')
        writer.write_int32(self.port or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputClientProxy':
        address = reader.read_string()
        port = reader.read_int32()
        return cls(address=address, port=port)


@register_tl
class HelpTermsOfServiceUpdateEmpty(TLObject):
    ID: int = 0xe3309f7f

    def __init__(self, expires: Any = None) -> None:
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.expires or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpTermsOfServiceUpdateEmpty':
        expires = reader.read_int32()
        return cls(expires=expires)


@register_tl
class HelpTermsOfServiceUpdate(TLObject):
    ID: int = 0x28ecf961

    def __init__(self, expires: Any = None, terms_of_service: Any = None) -> None:
        self.expires = expires
        self.terms_of_service = terms_of_service

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.expires or 0)
        if self.terms_of_service is not None and hasattr(self.terms_of_service, 'write'): self.terms_of_service.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpTermsOfServiceUpdate':
        expires = reader.read_int32()
        terms_of_service = reader.read_object()
        return cls(expires=expires, terms_of_service=terms_of_service)


@register_tl
class InputSecureFileUploaded(TLObject):
    ID: int = 0x3334b0f0

    def __init__(self, id: Any = None, parts: Any = None, md5_checksum: Any = None, file_hash: Any = None, secret: Any = None) -> None:
        self.id = id
        self.parts = parts
        self.md5_checksum = md5_checksum
        self.file_hash = file_hash
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int32(self.parts or 0)
        writer.write_string(self.md5_checksum or '')
        writer.write_bytes(self.file_hash or b'')
        writer.write_bytes(self.secret or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSecureFileUploaded':
        id = reader.read_int64()
        parts = reader.read_int32()
        md5_checksum = reader.read_string()
        file_hash = reader.read_bytes()
        secret = reader.read_bytes()
        return cls(id=id, parts=parts, md5_checksum=md5_checksum, file_hash=file_hash, secret=secret)


@register_tl
class InputSecureFile(TLObject):
    ID: int = 0x5367e5be

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSecureFile':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class SecureFileEmpty(TLObject):
    ID: int = 0x64199744

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureFileEmpty':
        return cls()


@register_tl
class SecureFile(TLObject):
    ID: int = 0x7d09c27e

    def __init__(self, id: Any = None, access_hash: Any = None, size: Any = None, dc_id: Any = None, date: Any = None, file_hash: Any = None, secret: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.size = size
        self.dc_id = dc_id
        self.date = date
        self.file_hash = file_hash
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int64(self.size or 0)
        writer.write_int32(self.dc_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_bytes(self.file_hash or b'')
        writer.write_bytes(self.secret or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureFile':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        size = reader.read_int64()
        dc_id = reader.read_int32()
        date = reader.read_int32()
        file_hash = reader.read_bytes()
        secret = reader.read_bytes()
        return cls(id=id, access_hash=access_hash, size=size, dc_id=dc_id, date=date, file_hash=file_hash, secret=secret)


@register_tl
class SecureData(TLObject):
    ID: int = 0x8aeabec3

    def __init__(self, data: Any = None, data_hash: Any = None, secret: Any = None) -> None:
        self.data = data
        self.data_hash = data_hash
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.data or b'')
        writer.write_bytes(self.data_hash or b'')
        writer.write_bytes(self.secret or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureData':
        data = reader.read_bytes()
        data_hash = reader.read_bytes()
        secret = reader.read_bytes()
        return cls(data=data, data_hash=data_hash, secret=secret)


@register_tl
class SecurePlainPhone(TLObject):
    ID: int = 0x7d6099dd

    def __init__(self, phone: Any = None) -> None:
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecurePlainPhone':
        phone = reader.read_string()
        return cls(phone=phone)


@register_tl
class SecurePlainEmail(TLObject):
    ID: int = 0x21ec5a5f

    def __init__(self, email: Any = None) -> None:
        self.email = email

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.email or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecurePlainEmail':
        email = reader.read_string()
        return cls(email=email)


@register_tl
class SecureValueTypePersonalDetails(TLObject):
    ID: int = 0x9d2a81e3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypePersonalDetails':
        return cls()


@register_tl
class SecureValueTypePassport(TLObject):
    ID: int = 0x3dac6a00

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypePassport':
        return cls()


@register_tl
class SecureValueTypeDriverLicense(TLObject):
    ID: int = 0x6e425c4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeDriverLicense':
        return cls()


@register_tl
class SecureValueTypeIdentityCard(TLObject):
    ID: int = 0xa0d0744b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeIdentityCard':
        return cls()


@register_tl
class SecureValueTypeInternalPassport(TLObject):
    ID: int = 0x99a48f23

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeInternalPassport':
        return cls()


@register_tl
class SecureValueTypeAddress(TLObject):
    ID: int = 0xcbe31e26

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeAddress':
        return cls()


@register_tl
class SecureValueTypeUtilityBill(TLObject):
    ID: int = 0xfc36954e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeUtilityBill':
        return cls()


@register_tl
class SecureValueTypeBankStatement(TLObject):
    ID: int = 0x89137c0d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeBankStatement':
        return cls()


@register_tl
class SecureValueTypeRentalAgreement(TLObject):
    ID: int = 0x8b883488

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeRentalAgreement':
        return cls()


@register_tl
class SecureValueTypePassportRegistration(TLObject):
    ID: int = 0x99e3806a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypePassportRegistration':
        return cls()


@register_tl
class SecureValueTypeTemporaryRegistration(TLObject):
    ID: int = 0xea02ec33

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeTemporaryRegistration':
        return cls()


@register_tl
class SecureValueTypePhone(TLObject):
    ID: int = 0xb320aadb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypePhone':
        return cls()


@register_tl
class SecureValueTypeEmail(TLObject):
    ID: int = 0x8e3ca7ee

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueTypeEmail':
        return cls()


@register_tl
class SecureValue(TLObject):
    ID: int = 0x187fa0ca

    def __init__(self, data: Any = None, front_side: Any = None, reverse_side: Any = None, selfie: Any = None, translation: Any = None, files: Any = None, plain_data: Any = None, type: Any = None, hash: Any = None) -> None:
        self.data = data
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.files = files
        self.plain_data = plain_data
        self.type = type
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.front_side is not None:
            flags |= (1 << 1)
        if self.reverse_side is not None:
            flags |= (1 << 2)
        if self.selfie is not None:
            flags |= (1 << 3)
        if self.translation is not None:
            flags |= (1 << 6)
        if self.files is not None:
            flags |= (1 << 4)
        if self.plain_data is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        if self.data is not None:
            if self.data is not None and hasattr(self.data, 'write'): self.data.write(writer)
        if self.front_side is not None:
            if self.front_side is not None and hasattr(self.front_side, 'write'): self.front_side.write(writer)
        if self.reverse_side is not None:
            if self.reverse_side is not None and hasattr(self.reverse_side, 'write'): self.reverse_side.write(writer)
        if self.selfie is not None:
            if self.selfie is not None and hasattr(self.selfie, 'write'): self.selfie.write(writer)
        if self.translation is not None:
            writer.write_vector(self.translation or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.files is not None:
            writer.write_vector(self.files or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.plain_data is not None:
            if self.plain_data is not None and hasattr(self.plain_data, 'write'): self.plain_data.write(writer)
        writer.write_bytes(self.hash or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValue':
        flags = reader.read_uint32()
        type = reader.read_object()
        data = reader.read_object() if (flags & (1 << 0)) else None
        front_side = reader.read_object() if (flags & (1 << 1)) else None
        reverse_side = reader.read_object() if (flags & (1 << 2)) else None
        selfie = reader.read_object() if (flags & (1 << 3)) else None
        translation = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 6)) else None
        files = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        plain_data = reader.read_object() if (flags & (1 << 5)) else None
        hash = reader.read_bytes()
        return cls(type=type, data=data, front_side=front_side, reverse_side=reverse_side, selfie=selfie, translation=translation, files=files, plain_data=plain_data, hash=hash)


@register_tl
class InputSecureValue(TLObject):
    ID: int = 0xdb21d0a7

    def __init__(self, data: Any = None, front_side: Any = None, reverse_side: Any = None, selfie: Any = None, translation: Any = None, files: Any = None, plain_data: Any = None, type: Any = None) -> None:
        self.data = data
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.files = files
        self.plain_data = plain_data
        self.type = type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.front_side is not None:
            flags |= (1 << 1)
        if self.reverse_side is not None:
            flags |= (1 << 2)
        if self.selfie is not None:
            flags |= (1 << 3)
        if self.translation is not None:
            flags |= (1 << 6)
        if self.files is not None:
            flags |= (1 << 4)
        if self.plain_data is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        if self.data is not None:
            if self.data is not None and hasattr(self.data, 'write'): self.data.write(writer)
        if self.front_side is not None:
            if self.front_side is not None and hasattr(self.front_side, 'write'): self.front_side.write(writer)
        if self.reverse_side is not None:
            if self.reverse_side is not None and hasattr(self.reverse_side, 'write'): self.reverse_side.write(writer)
        if self.selfie is not None:
            if self.selfie is not None and hasattr(self.selfie, 'write'): self.selfie.write(writer)
        if self.translation is not None:
            writer.write_vector(self.translation or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.files is not None:
            writer.write_vector(self.files or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.plain_data is not None:
            if self.plain_data is not None and hasattr(self.plain_data, 'write'): self.plain_data.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSecureValue':
        flags = reader.read_uint32()
        type = reader.read_object()
        data = reader.read_object() if (flags & (1 << 0)) else None
        front_side = reader.read_object() if (flags & (1 << 1)) else None
        reverse_side = reader.read_object() if (flags & (1 << 2)) else None
        selfie = reader.read_object() if (flags & (1 << 3)) else None
        translation = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 6)) else None
        files = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        plain_data = reader.read_object() if (flags & (1 << 5)) else None
        return cls(type=type, data=data, front_side=front_side, reverse_side=reverse_side, selfie=selfie, translation=translation, files=files, plain_data=plain_data)


@register_tl
class SecureValueHash(TLObject):
    ID: int = 0xed1ecdb0

    def __init__(self, type: Any = None, hash: Any = None) -> None:
        self.type = type
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.hash or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueHash':
        type = reader.read_object()
        hash = reader.read_bytes()
        return cls(type=type, hash=hash)


@register_tl
class SecureValueErrorData(TLObject):
    ID: int = 0xe8a40bd9

    def __init__(self, type: Any = None, data_hash: Any = None, field: Any = None, text: Any = None) -> None:
        self.type = type
        self.data_hash = data_hash
        self.field = field
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.data_hash or b'')
        writer.write_string(self.field or '')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorData':
        type = reader.read_object()
        data_hash = reader.read_bytes()
        field = reader.read_string()
        text = reader.read_string()
        return cls(type=type, data_hash=data_hash, field=field, text=text)


@register_tl
class SecureValueErrorFrontSide(TLObject):
    ID: int = 0xbe3dfa

    def __init__(self, type: Any = None, file_hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.file_hash or b'')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorFrontSide':
        type = reader.read_object()
        file_hash = reader.read_bytes()
        text = reader.read_string()
        return cls(type=type, file_hash=file_hash, text=text)


@register_tl
class SecureValueErrorReverseSide(TLObject):
    ID: int = 0x868a2aa5

    def __init__(self, type: Any = None, file_hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.file_hash or b'')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorReverseSide':
        type = reader.read_object()
        file_hash = reader.read_bytes()
        text = reader.read_string()
        return cls(type=type, file_hash=file_hash, text=text)


@register_tl
class SecureValueErrorSelfie(TLObject):
    ID: int = 0xe537ced6

    def __init__(self, type: Any = None, file_hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.file_hash or b'')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorSelfie':
        type = reader.read_object()
        file_hash = reader.read_bytes()
        text = reader.read_string()
        return cls(type=type, file_hash=file_hash, text=text)


@register_tl
class SecureValueErrorFile(TLObject):
    ID: int = 0x7a700873

    def __init__(self, type: Any = None, file_hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.file_hash or b'')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorFile':
        type = reader.read_object()
        file_hash = reader.read_bytes()
        text = reader.read_string()
        return cls(type=type, file_hash=file_hash, text=text)


@register_tl
class SecureValueErrorFiles(TLObject):
    ID: int = 0x666220e9

    def __init__(self, type: Any = None, file_hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_vector(self.file_hash or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorFiles':
        type = reader.read_object()
        file_hash = reader.read_vector(lambda r: reader.read_object())
        text = reader.read_string()
        return cls(type=type, file_hash=file_hash, text=text)


@register_tl
class SecureValueError(TLObject):
    ID: int = 0x869d758f

    def __init__(self, type: Any = None, hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.hash = hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.hash or b'')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueError':
        type = reader.read_object()
        hash = reader.read_bytes()
        text = reader.read_string()
        return cls(type=type, hash=hash, text=text)


@register_tl
class SecureValueErrorTranslationFile(TLObject):
    ID: int = 0xa1144770

    def __init__(self, type: Any = None, file_hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_bytes(self.file_hash or b'')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorTranslationFile':
        type = reader.read_object()
        file_hash = reader.read_bytes()
        text = reader.read_string()
        return cls(type=type, file_hash=file_hash, text=text)


@register_tl
class SecureValueErrorTranslationFiles(TLObject):
    ID: int = 0x34636dd8

    def __init__(self, type: Any = None, file_hash: Any = None, text: Any = None) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_vector(self.file_hash or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureValueErrorTranslationFiles':
        type = reader.read_object()
        file_hash = reader.read_vector(lambda r: reader.read_object())
        text = reader.read_string()
        return cls(type=type, file_hash=file_hash, text=text)


@register_tl
class SecureCredentialsEncrypted(TLObject):
    ID: int = 0x33f0ea47

    def __init__(self, data: Any = None, hash: Any = None, secret: Any = None) -> None:
        self.data = data
        self.hash = hash
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.data or b'')
        writer.write_bytes(self.hash or b'')
        writer.write_bytes(self.secret or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureCredentialsEncrypted':
        data = reader.read_bytes()
        hash = reader.read_bytes()
        secret = reader.read_bytes()
        return cls(data=data, hash=hash, secret=secret)


@register_tl
class AccountAuthorizationForm(TLObject):
    ID: int = 0xad2e1cd8

    def __init__(self, privacy_policy_url: Any = None, required_types: Any = None, values: Any = None, errors: Any = None, users: Any = None) -> None:
        self.privacy_policy_url = privacy_policy_url
        self.required_types = required_types
        self.values = values
        self.errors = errors
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.privacy_policy_url is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.required_types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.values or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.errors or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.privacy_policy_url is not None:
            writer.write_string(self.privacy_policy_url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountAuthorizationForm':
        flags = reader.read_uint32()
        required_types = reader.read_vector(lambda r: reader.read_object())
        values = reader.read_vector(lambda r: reader.read_object())
        errors = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        privacy_policy_url = reader.read_string() if (flags & (1 << 0)) else None
        return cls(required_types=required_types, values=values, errors=errors, users=users, privacy_policy_url=privacy_policy_url)


@register_tl
class AccountSentEmailCode(TLObject):
    ID: int = 0x811f854f

    def __init__(self, email_pattern: Any = None, length: Any = None) -> None:
        self.email_pattern = email_pattern
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.email_pattern or '')
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSentEmailCode':
        email_pattern = reader.read_string()
        length = reader.read_int32()
        return cls(email_pattern=email_pattern, length=length)


@register_tl
class HelpDeepLinkInfoEmpty(TLObject):
    ID: int = 0x66afa166

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpDeepLinkInfoEmpty':
        return cls()


@register_tl
class HelpDeepLinkInfo(TLObject):
    ID: int = 0x6a4ee832

    def __init__(self, update_app: bool = False, entities: Any = None, message: Any = None) -> None:
        self.update_app = update_app
        self.entities = entities
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.update_app:
            flags |= (1 << 0)
        if self.entities is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpDeepLinkInfo':
        flags = reader.read_uint32()
        update_app = bool(flags & (1 << 0))
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        return cls(update_app=update_app, message=message, entities=entities)


@register_tl
class SavedPhoneContact(TLObject):
    ID: int = 0x1142bd56

    def __init__(self, phone: Any = None, first_name: Any = None, last_name: Any = None, date: Any = None) -> None:
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SavedPhoneContact':
        phone = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        date = reader.read_int32()
        return cls(phone=phone, first_name=first_name, last_name=last_name, date=date)


@register_tl
class AccountTakeout(TLObject):
    ID: int = 0x4dba4501

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountTakeout':
        id = reader.read_int64()
        return cls(id=id)


@register_tl
class PasswordKdfAlgoUnknown(TLObject):
    ID: int = 0xd45ab096

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PasswordKdfAlgoUnknown':
        return cls()


@register_tl
class PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(TLObject):
    ID: int = 0x3a912d4a

    def __init__(self, salt1: Any = None, salt2: Any = None, g: Any = None, p: Any = None) -> None:
        self.salt1 = salt1
        self.salt2 = salt2
        self.g = g
        self.p = p

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.salt1 or b'')
        writer.write_bytes(self.salt2 or b'')
        writer.write_int32(self.g or 0)
        writer.write_bytes(self.p or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow':
        salt1 = reader.read_bytes()
        salt2 = reader.read_bytes()
        g = reader.read_int32()
        p = reader.read_bytes()
        return cls(salt1=salt1, salt2=salt2, g=g, p=p)


@register_tl
class SecurePasswordKdfAlgoUnknown(TLObject):
    ID: int = 0x4a8537

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecurePasswordKdfAlgoUnknown':
        return cls()


@register_tl
class SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000(TLObject):
    ID: int = 0xbbf2dda0

    def __init__(self, salt: Any = None) -> None:
        self.salt = salt

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.salt or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000':
        salt = reader.read_bytes()
        return cls(salt=salt)


@register_tl
class SecurePasswordKdfAlgoSHA512(TLObject):
    ID: int = 0x86471d92

    def __init__(self, salt: Any = None) -> None:
        self.salt = salt

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.salt or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SecurePasswordKdfAlgoSHA512':
        salt = reader.read_bytes()
        return cls(salt=salt)


@register_tl
class SecureSecretSettings(TLObject):
    ID: int = 0x1527bcac

    def __init__(self, secure_algo: Any = None, secure_secret: Any = None, secure_secret_id: Any = None) -> None:
        self.secure_algo = secure_algo
        self.secure_secret = secure_secret
        self.secure_secret_id = secure_secret_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.secure_algo is not None and hasattr(self.secure_algo, 'write'): self.secure_algo.write(writer)
        writer.write_bytes(self.secure_secret or b'')
        writer.write_int64(self.secure_secret_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureSecretSettings':
        secure_algo = reader.read_object()
        secure_secret = reader.read_bytes()
        secure_secret_id = reader.read_int64()
        return cls(secure_algo=secure_algo, secure_secret=secure_secret, secure_secret_id=secure_secret_id)


@register_tl
class InputCheckPasswordEmpty(TLObject):
    ID: int = 0x9880f658

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputCheckPasswordEmpty':
        return cls()


@register_tl
class InputCheckPasswordSRP(TLObject):
    ID: int = 0xd27ff082

    def __init__(self, srp_id: Any = None, A: Any = None, M1: Any = None) -> None:
        self.srp_id = srp_id
        self.A = A
        self.M1 = M1

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.srp_id or 0)
        writer.write_bytes(self.A or b'')
        writer.write_bytes(self.M1 or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputCheckPasswordSRP':
        srp_id = reader.read_int64()
        A = reader.read_bytes()
        M1 = reader.read_bytes()
        return cls(srp_id=srp_id, A=A, M1=M1)


@register_tl
class SecureRequiredType(TLObject):
    ID: int = 0x829d99da

    def __init__(self, native_names: bool = False, selfie_required: bool = False, translation_required: bool = False, type: Any = None) -> None:
        self.native_names = native_names
        self.selfie_required = selfie_required
        self.translation_required = translation_required
        self.type = type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.native_names:
            flags |= (1 << 0)
        if self.selfie_required:
            flags |= (1 << 1)
        if self.translation_required:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureRequiredType':
        flags = reader.read_uint32()
        native_names = bool(flags & (1 << 0))
        selfie_required = bool(flags & (1 << 1))
        translation_required = bool(flags & (1 << 2))
        type = reader.read_object()
        return cls(native_names=native_names, selfie_required=selfie_required, translation_required=translation_required, type=type)


@register_tl
class SecureRequiredTypeOneOf(TLObject):
    ID: int = 0x27477b4

    def __init__(self, types: Any = None) -> None:
        self.types = types

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'SecureRequiredTypeOneOf':
        types = reader.read_vector(lambda r: reader.read_object())
        return cls(types=types)


@register_tl
class HelpPassportConfigNotModified(TLObject):
    ID: int = 0xbfb9f457

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPassportConfigNotModified':
        return cls()


@register_tl
class HelpPassportConfig(TLObject):
    ID: int = 0xa098d6af

    def __init__(self, hash: Any = None, countries_langs: Any = None) -> None:
        self.hash = hash
        self.countries_langs = countries_langs

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)
        if self.countries_langs is not None and hasattr(self.countries_langs, 'write'): self.countries_langs.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPassportConfig':
        hash = reader.read_int32()
        countries_langs = reader.read_object()
        return cls(hash=hash, countries_langs=countries_langs)


@register_tl
class InputAppEvent(TLObject):
    ID: int = 0x1d1b1245

    def __init__(self, time: Any = None, type: Any = None, peer: Any = None, data: Any = None) -> None:
        self.time = time
        self.type = type
        self.peer = peer
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_double(self.time or 0.0)
        writer.write_string(self.type or '')
        writer.write_int64(self.peer or 0)
        if self.data is not None and hasattr(self.data, 'write'): self.data.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputAppEvent':
        time = reader.read_double()
        type = reader.read_string()
        peer = reader.read_int64()
        data = reader.read_object()
        return cls(time=time, type=type, peer=peer, data=data)


@register_tl
class JsonObjectValue(TLObject):
    ID: int = 0xc0de1bd9

    def __init__(self, key: Any = None, value: Any = None) -> None:
        self.key = key
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.key or '')
        if self.value is not None and hasattr(self.value, 'write'): self.value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonObjectValue':
        key = reader.read_string()
        value = reader.read_object()
        return cls(key=key, value=value)


@register_tl
class JsonNull(TLObject):
    ID: int = 0x3f6d7b68

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonNull':
        return cls()


@register_tl
class JsonBool(TLObject):
    ID: int = 0xc7345e6a

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.value))

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonBool':
        value = reader.read_bool()
        return cls(value=value)


@register_tl
class JsonNumber(TLObject):
    ID: int = 0x2be0dfa4

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_double(self.value or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonNumber':
        value = reader.read_double()
        return cls(value=value)


@register_tl
class JsonString(TLObject):
    ID: int = 0xb71e767a

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.value or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonString':
        value = reader.read_string()
        return cls(value=value)


@register_tl
class JsonArray(TLObject):
    ID: int = 0xf7444763

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.value or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonArray':
        value = reader.read_vector(lambda r: reader.read_object())
        return cls(value=value)


@register_tl
class JsonObject(TLObject):
    ID: int = 0x99c1d49d

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.value or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonObject':
        value = reader.read_vector(lambda r: reader.read_object())
        return cls(value=value)


@register_tl
class PageTableCell(TLObject):
    ID: int = 0x34566b6a

    def __init__(self, header: bool = False, align_center: bool = False, align_right: bool = False, valign_middle: bool = False, valign_bottom: bool = False, text: Any = None, colspan: Any = None, rowspan: Any = None) -> None:
        self.header = header
        self.align_center = align_center
        self.align_right = align_right
        self.valign_middle = valign_middle
        self.valign_bottom = valign_bottom
        self.text = text
        self.colspan = colspan
        self.rowspan = rowspan

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.header:
            flags |= (1 << 0)
        if self.align_center:
            flags |= (1 << 3)
        if self.align_right:
            flags |= (1 << 4)
        if self.valign_middle:
            flags |= (1 << 5)
        if self.valign_bottom:
            flags |= (1 << 6)
        if self.text is not None:
            flags |= (1 << 7)
        if self.colspan is not None:
            flags |= (1 << 1)
        if self.rowspan is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.text is not None:
            if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        if self.colspan is not None:
            writer.write_int32(self.colspan or 0)
        if self.rowspan is not None:
            writer.write_int32(self.rowspan or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageTableCell':
        flags = reader.read_uint32()
        header = bool(flags & (1 << 0))
        align_center = bool(flags & (1 << 3))
        align_right = bool(flags & (1 << 4))
        valign_middle = bool(flags & (1 << 5))
        valign_bottom = bool(flags & (1 << 6))
        text = reader.read_object() if (flags & (1 << 7)) else None
        colspan = reader.read_int32() if (flags & (1 << 1)) else None
        rowspan = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(header=header, align_center=align_center, align_right=align_right, valign_middle=valign_middle, valign_bottom=valign_bottom, text=text, colspan=colspan, rowspan=rowspan)


@register_tl
class PageTableRow(TLObject):
    ID: int = 0xe0c0c5e5

    def __init__(self, cells: Any = None) -> None:
        self.cells = cells

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.cells or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageTableRow':
        cells = reader.read_vector(lambda r: reader.read_object())
        return cls(cells=cells)


@register_tl
class PageCaption(TLObject):
    ID: int = 0x6f747657

    def __init__(self, text: Any = None, credit: Any = None) -> None:
        self.text = text
        self.credit = credit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        if self.credit is not None and hasattr(self.credit, 'write'): self.credit.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageCaption':
        text = reader.read_object()
        credit = reader.read_object()
        return cls(text=text, credit=credit)


@register_tl
class PageListItemText(TLObject):
    ID: int = 0xb92fb6cd

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageListItemText':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageListItemBlocks(TLObject):
    ID: int = 0x25e073fc

    def __init__(self, blocks: Any = None) -> None:
        self.blocks = blocks

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.blocks or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageListItemBlocks':
        blocks = reader.read_vector(lambda r: reader.read_object())
        return cls(blocks=blocks)


@register_tl
class PageListOrderedItemText(TLObject):
    ID: int = 0x5e068047

    def __init__(self, num: Any = None, text: Any = None) -> None:
        self.num = num
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.num or '')
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageListOrderedItemText':
        num = reader.read_string()
        text = reader.read_object()
        return cls(num=num, text=text)


@register_tl
class PageListOrderedItemBlocks(TLObject):
    ID: int = 0x98dd8936

    def __init__(self, num: Any = None, blocks: Any = None) -> None:
        self.num = num
        self.blocks = blocks

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.num or '')
        writer.write_vector(self.blocks or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageListOrderedItemBlocks':
        num = reader.read_string()
        blocks = reader.read_vector(lambda r: reader.read_object())
        return cls(num=num, blocks=blocks)


@register_tl
class PageRelatedArticle(TLObject):
    ID: int = 0xb390dc08

    def __init__(self, title: Any = None, description: Any = None, photo_id: Any = None, author: Any = None, published_date: Any = None, url: Any = None, webpage_id: Any = None) -> None:
        self.title = title
        self.description = description
        self.photo_id = photo_id
        self.author = author
        self.published_date = published_date
        self.url = url
        self.webpage_id = webpage_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        if self.description is not None:
            flags |= (1 << 1)
        if self.photo_id is not None:
            flags |= (1 << 2)
        if self.author is not None:
            flags |= (1 << 3)
        if self.published_date is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(self.url or '')
        writer.write_int64(self.webpage_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.photo_id is not None:
            writer.write_int64(self.photo_id or 0)
        if self.author is not None:
            writer.write_string(self.author or '')
        if self.published_date is not None:
            writer.write_int32(self.published_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageRelatedArticle':
        flags = reader.read_uint32()
        url = reader.read_string()
        webpage_id = reader.read_int64()
        title = reader.read_string() if (flags & (1 << 0)) else None
        description = reader.read_string() if (flags & (1 << 1)) else None
        photo_id = reader.read_int64() if (flags & (1 << 2)) else None
        author = reader.read_string() if (flags & (1 << 3)) else None
        published_date = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(url=url, webpage_id=webpage_id, title=title, description=description, photo_id=photo_id, author=author, published_date=published_date)


@register_tl
class Page(TLObject):
    ID: int = 0x98657f0d

    def __init__(self, part: bool = False, rtl: bool = False, v2: bool = False, views: Any = None, url: Any = None, blocks: Any = None, photos: Any = None, documents: Any = None) -> None:
        self.part = part
        self.rtl = rtl
        self.v2 = v2
        self.views = views
        self.url = url
        self.blocks = blocks
        self.photos = photos
        self.documents = documents

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.part:
            flags |= (1 << 0)
        if self.rtl:
            flags |= (1 << 1)
        if self.v2:
            flags |= (1 << 2)
        if self.views is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_string(self.url or '')
        writer.write_vector(self.blocks or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.photos or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.views is not None:
            writer.write_int32(self.views or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Page':
        flags = reader.read_uint32()
        part = bool(flags & (1 << 0))
        rtl = bool(flags & (1 << 1))
        v2 = bool(flags & (1 << 2))
        url = reader.read_string()
        blocks = reader.read_vector(lambda r: reader.read_object())
        photos = reader.read_vector(lambda r: reader.read_object())
        documents = reader.read_vector(lambda r: reader.read_object())
        views = reader.read_int32() if (flags & (1 << 3)) else None
        return cls(part=part, rtl=rtl, v2=v2, url=url, blocks=blocks, photos=photos, documents=documents, views=views)


@register_tl
class HelpSupportName(TLObject):
    ID: int = 0x8c05f1c9

    def __init__(self, name: Any = None) -> None:
        self.name = name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpSupportName':
        name = reader.read_string()
        return cls(name=name)


@register_tl
class HelpUserInfoEmpty(TLObject):
    ID: int = 0xf3ae2eed

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpUserInfoEmpty':
        return cls()


@register_tl
class HelpUserInfo(TLObject):
    ID: int = 0x1eb3758

    def __init__(self, message: Any = None, entities: Any = None, author: Any = None, date: Any = None) -> None:
        self.message = message
        self.entities = entities
        self.author = author
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.message or '')
        writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.author or '')
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpUserInfo':
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object())
        author = reader.read_string()
        date = reader.read_int32()
        return cls(message=message, entities=entities, author=author, date=date)


@register_tl
class PollAnswer(TLObject):
    ID: int = 0x4b7d786a

    def __init__(self, media: Any = None, added_by: Any = None, date: Any = None, text: Any = None, option: Any = None) -> None:
        self.media = media
        self.added_by = added_by
        self.date = date
        self.text = text
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.media is not None:
            flags |= (1 << 0)
        if self.added_by is not None:
            flags |= (1 << 1)
        if self.date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        writer.write_bytes(self.option or b'')
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.added_by is not None:
            if self.added_by is not None and hasattr(self.added_by, 'write'): self.added_by.write(writer)
        if self.date is not None:
            writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PollAnswer':
        flags = reader.read_uint32()
        text = reader.read_object()
        option = reader.read_bytes()
        media = reader.read_object() if (flags & (1 << 0)) else None
        added_by = reader.read_object() if (flags & (1 << 1)) else None
        date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(text=text, option=option, media=media, added_by=added_by, date=date)


@register_tl
class InputPollAnswer(TLObject):
    ID: int = 0x199fed96

    def __init__(self, media: Any = None, text: Any = None) -> None:
        self.media = media
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.media is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPollAnswer':
        flags = reader.read_uint32()
        text = reader.read_object()
        media = reader.read_object() if (flags & (1 << 0)) else None
        return cls(text=text, media=media)


@register_tl
class Poll(TLObject):
    ID: int = 0x966e2dbf

    def __init__(self, closed: bool = False, public_voters: bool = False, multiple_choice: bool = False, quiz: bool = False, open_answers: bool = False, revoting_disabled: bool = False, shuffle_answers: bool = False, hide_results_until_close: bool = False, creator: bool = False, subscribers_only: bool = False, close_period: Any = None, close_date: Any = None, countries_iso2: Any = None, id: Any = None, question: Any = None, answers: Any = None, hash: Any = None) -> None:
        self.closed = closed
        self.public_voters = public_voters
        self.multiple_choice = multiple_choice
        self.quiz = quiz
        self.open_answers = open_answers
        self.revoting_disabled = revoting_disabled
        self.shuffle_answers = shuffle_answers
        self.hide_results_until_close = hide_results_until_close
        self.creator = creator
        self.subscribers_only = subscribers_only
        self.close_period = close_period
        self.close_date = close_date
        self.countries_iso2 = countries_iso2
        self.id = id
        self.question = question
        self.answers = answers
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.closed:
            flags |= (1 << 0)
        if self.public_voters:
            flags |= (1 << 1)
        if self.multiple_choice:
            flags |= (1 << 2)
        if self.quiz:
            flags |= (1 << 3)
        if self.open_answers:
            flags |= (1 << 6)
        if self.revoting_disabled:
            flags |= (1 << 7)
        if self.shuffle_answers:
            flags |= (1 << 8)
        if self.hide_results_until_close:
            flags |= (1 << 9)
        if self.creator:
            flags |= (1 << 10)
        if self.subscribers_only:
            flags |= (1 << 11)
        if self.close_period is not None:
            flags |= (1 << 4)
        if self.close_date is not None:
            flags |= (1 << 5)
        if self.countries_iso2 is not None:
            flags |= (1 << 12)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.question is not None and hasattr(self.question, 'write'): self.question.write(writer)
        writer.write_vector(self.answers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.close_period is not None:
            writer.write_int32(self.close_period or 0)
        if self.close_date is not None:
            writer.write_int32(self.close_date or 0)
        if self.countries_iso2 is not None:
            writer.write_vector(self.countries_iso2 or [], lambda w, x: w.write_string(x))
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Poll':
        flags = reader.read_uint32()
        id = reader.read_int64()
        closed = bool(flags & (1 << 0))
        public_voters = bool(flags & (1 << 1))
        multiple_choice = bool(flags & (1 << 2))
        quiz = bool(flags & (1 << 3))
        open_answers = bool(flags & (1 << 6))
        revoting_disabled = bool(flags & (1 << 7))
        shuffle_answers = bool(flags & (1 << 8))
        hide_results_until_close = bool(flags & (1 << 9))
        creator = bool(flags & (1 << 10))
        subscribers_only = bool(flags & (1 << 11))
        question = reader.read_object()
        answers = reader.read_vector(lambda r: reader.read_object())
        close_period = reader.read_int32() if (flags & (1 << 4)) else None
        close_date = reader.read_int32() if (flags & (1 << 5)) else None
        countries_iso2 = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 12)) else None
        hash = reader.read_int64()
        return cls(id=id, closed=closed, public_voters=public_voters, multiple_choice=multiple_choice, quiz=quiz, open_answers=open_answers, revoting_disabled=revoting_disabled, shuffle_answers=shuffle_answers, hide_results_until_close=hide_results_until_close, creator=creator, subscribers_only=subscribers_only, question=question, answers=answers, close_period=close_period, close_date=close_date, countries_iso2=countries_iso2, hash=hash)


@register_tl
class PollAnswerVoters(TLObject):
    ID: int = 0x3645230a

    def __init__(self, chosen: bool = False, correct: bool = False, voters: Any = None, recent_voters: Any = None, option: Any = None) -> None:
        self.chosen = chosen
        self.correct = correct
        self.voters = voters
        self.recent_voters = recent_voters
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.chosen:
            flags |= (1 << 0)
        if self.correct:
            flags |= (1 << 1)
        if self.voters is not None:
            flags |= (1 << 2)
        if self.recent_voters is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_bytes(self.option or b'')
        if self.voters is not None:
            writer.write_int32(self.voters or 0)
        if self.recent_voters is not None:
            writer.write_vector(self.recent_voters or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PollAnswerVoters':
        flags = reader.read_uint32()
        chosen = bool(flags & (1 << 0))
        correct = bool(flags & (1 << 1))
        option = reader.read_bytes()
        voters = reader.read_int32() if (flags & (1 << 2)) else None
        recent_voters = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 2)) else None
        return cls(chosen=chosen, correct=correct, option=option, voters=voters, recent_voters=recent_voters)


@register_tl
class PollResults(TLObject):
    ID: int = 0xba7bb15e

    def __init__(self, min: bool = False, has_unread_votes: bool = False, can_view_stats: bool = False, results: Any = None, total_voters: Any = None, recent_voters: Any = None, solution: Any = None, solution_entities: Any = None, solution_media: Any = None) -> None:
        self.min = min
        self.has_unread_votes = has_unread_votes
        self.can_view_stats = can_view_stats
        self.results = results
        self.total_voters = total_voters
        self.recent_voters = recent_voters
        self.solution = solution
        self.solution_entities = solution_entities
        self.solution_media = solution_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.min:
            flags |= (1 << 0)
        if self.has_unread_votes:
            flags |= (1 << 6)
        if self.can_view_stats:
            flags |= (1 << 7)
        if self.results is not None:
            flags |= (1 << 1)
        if self.total_voters is not None:
            flags |= (1 << 2)
        if self.recent_voters is not None:
            flags |= (1 << 3)
        if self.solution is not None:
            flags |= (1 << 4)
        if self.solution_entities is not None:
            flags |= (1 << 4)
        if self.solution_media is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.results is not None:
            writer.write_vector(self.results or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.total_voters is not None:
            writer.write_int32(self.total_voters or 0)
        if self.recent_voters is not None:
            writer.write_vector(self.recent_voters or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.solution is not None:
            writer.write_string(self.solution or '')
        if self.solution_entities is not None:
            writer.write_vector(self.solution_entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.solution_media is not None:
            if self.solution_media is not None and hasattr(self.solution_media, 'write'): self.solution_media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PollResults':
        flags = reader.read_uint32()
        min = bool(flags & (1 << 0))
        has_unread_votes = bool(flags & (1 << 6))
        can_view_stats = bool(flags & (1 << 7))
        results = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        total_voters = reader.read_int32() if (flags & (1 << 2)) else None
        recent_voters = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        solution = reader.read_string() if (flags & (1 << 4)) else None
        solution_entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        solution_media = reader.read_object() if (flags & (1 << 5)) else None
        return cls(min=min, has_unread_votes=has_unread_votes, can_view_stats=can_view_stats, results=results, total_voters=total_voters, recent_voters=recent_voters, solution=solution, solution_entities=solution_entities, solution_media=solution_media)


@register_tl
class ChatOnlines(TLObject):
    ID: int = 0xf041e250

    def __init__(self, onlines: Any = None) -> None:
        self.onlines = onlines

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.onlines or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatOnlines':
        onlines = reader.read_int32()
        return cls(onlines=onlines)


@register_tl
class StatsURL(TLObject):
    ID: int = 0x47a971e0

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsURL':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class ChatAdminRights(TLObject):
    ID: int = 0x5fb224d5

    def __init__(self, change_info: bool = False, post_messages: bool = False, edit_messages: bool = False, delete_messages: bool = False, ban_users: bool = False, invite_users: bool = False, pin_messages: bool = False, add_admins: bool = False, anonymous: bool = False, manage_call: bool = False, other: bool = False, manage_topics: bool = False, post_stories: bool = False, edit_stories: bool = False, delete_stories: bool = False, manage_direct_messages: bool = False, manage_ranks: bool = False) -> None:
        self.change_info = change_info
        self.post_messages = post_messages
        self.edit_messages = edit_messages
        self.delete_messages = delete_messages
        self.ban_users = ban_users
        self.invite_users = invite_users
        self.pin_messages = pin_messages
        self.add_admins = add_admins
        self.anonymous = anonymous
        self.manage_call = manage_call
        self.other = other
        self.manage_topics = manage_topics
        self.post_stories = post_stories
        self.edit_stories = edit_stories
        self.delete_stories = delete_stories
        self.manage_direct_messages = manage_direct_messages
        self.manage_ranks = manage_ranks

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.change_info:
            flags |= (1 << 0)
        if self.post_messages:
            flags |= (1 << 1)
        if self.edit_messages:
            flags |= (1 << 2)
        if self.delete_messages:
            flags |= (1 << 3)
        if self.ban_users:
            flags |= (1 << 4)
        if self.invite_users:
            flags |= (1 << 5)
        if self.pin_messages:
            flags |= (1 << 7)
        if self.add_admins:
            flags |= (1 << 9)
        if self.anonymous:
            flags |= (1 << 10)
        if self.manage_call:
            flags |= (1 << 11)
        if self.other:
            flags |= (1 << 12)
        if self.manage_topics:
            flags |= (1 << 13)
        if self.post_stories:
            flags |= (1 << 14)
        if self.edit_stories:
            flags |= (1 << 15)
        if self.delete_stories:
            flags |= (1 << 16)
        if self.manage_direct_messages:
            flags |= (1 << 17)
        if self.manage_ranks:
            flags |= (1 << 18)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatAdminRights':
        flags = reader.read_uint32()
        change_info = bool(flags & (1 << 0))
        post_messages = bool(flags & (1 << 1))
        edit_messages = bool(flags & (1 << 2))
        delete_messages = bool(flags & (1 << 3))
        ban_users = bool(flags & (1 << 4))
        invite_users = bool(flags & (1 << 5))
        pin_messages = bool(flags & (1 << 7))
        add_admins = bool(flags & (1 << 9))
        anonymous = bool(flags & (1 << 10))
        manage_call = bool(flags & (1 << 11))
        other = bool(flags & (1 << 12))
        manage_topics = bool(flags & (1 << 13))
        post_stories = bool(flags & (1 << 14))
        edit_stories = bool(flags & (1 << 15))
        delete_stories = bool(flags & (1 << 16))
        manage_direct_messages = bool(flags & (1 << 17))
        manage_ranks = bool(flags & (1 << 18))
        return cls(change_info=change_info, post_messages=post_messages, edit_messages=edit_messages, delete_messages=delete_messages, ban_users=ban_users, invite_users=invite_users, pin_messages=pin_messages, add_admins=add_admins, anonymous=anonymous, manage_call=manage_call, other=other, manage_topics=manage_topics, post_stories=post_stories, edit_stories=edit_stories, delete_stories=delete_stories, manage_direct_messages=manage_direct_messages, manage_ranks=manage_ranks)


@register_tl
class ChatBannedRights(TLObject):
    ID: int = 0x9f120418

    def __init__(self, view_messages: bool = False, send_messages: bool = False, send_media: bool = False, send_stickers: bool = False, send_gifs: bool = False, send_games: bool = False, send_inline: bool = False, embed_links: bool = False, send_polls: bool = False, change_info: bool = False, invite_users: bool = False, pin_messages: bool = False, manage_topics: bool = False, send_photos: bool = False, send_videos: bool = False, send_roundvideos: bool = False, send_audios: bool = False, send_voices: bool = False, send_docs: bool = False, send_plain: bool = False, edit_rank: bool = False, send_reactions: bool = False, until_date: Any = None) -> None:
        self.view_messages = view_messages
        self.send_messages = send_messages
        self.send_media = send_media
        self.send_stickers = send_stickers
        self.send_gifs = send_gifs
        self.send_games = send_games
        self.send_inline = send_inline
        self.embed_links = embed_links
        self.send_polls = send_polls
        self.change_info = change_info
        self.invite_users = invite_users
        self.pin_messages = pin_messages
        self.manage_topics = manage_topics
        self.send_photos = send_photos
        self.send_videos = send_videos
        self.send_roundvideos = send_roundvideos
        self.send_audios = send_audios
        self.send_voices = send_voices
        self.send_docs = send_docs
        self.send_plain = send_plain
        self.edit_rank = edit_rank
        self.send_reactions = send_reactions
        self.until_date = until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.view_messages:
            flags |= (1 << 0)
        if self.send_messages:
            flags |= (1 << 1)
        if self.send_media:
            flags |= (1 << 2)
        if self.send_stickers:
            flags |= (1 << 3)
        if self.send_gifs:
            flags |= (1 << 4)
        if self.send_games:
            flags |= (1 << 5)
        if self.send_inline:
            flags |= (1 << 6)
        if self.embed_links:
            flags |= (1 << 7)
        if self.send_polls:
            flags |= (1 << 8)
        if self.change_info:
            flags |= (1 << 10)
        if self.invite_users:
            flags |= (1 << 15)
        if self.pin_messages:
            flags |= (1 << 17)
        if self.manage_topics:
            flags |= (1 << 18)
        if self.send_photos:
            flags |= (1 << 19)
        if self.send_videos:
            flags |= (1 << 20)
        if self.send_roundvideos:
            flags |= (1 << 21)
        if self.send_audios:
            flags |= (1 << 22)
        if self.send_voices:
            flags |= (1 << 23)
        if self.send_docs:
            flags |= (1 << 24)
        if self.send_plain:
            flags |= (1 << 25)
        if self.edit_rank:
            flags |= (1 << 26)
        if self.send_reactions:
            flags |= (1 << 27)
        writer.write_uint32(flags)
        writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatBannedRights':
        flags = reader.read_uint32()
        view_messages = bool(flags & (1 << 0))
        send_messages = bool(flags & (1 << 1))
        send_media = bool(flags & (1 << 2))
        send_stickers = bool(flags & (1 << 3))
        send_gifs = bool(flags & (1 << 4))
        send_games = bool(flags & (1 << 5))
        send_inline = bool(flags & (1 << 6))
        embed_links = bool(flags & (1 << 7))
        send_polls = bool(flags & (1 << 8))
        change_info = bool(flags & (1 << 10))
        invite_users = bool(flags & (1 << 15))
        pin_messages = bool(flags & (1 << 17))
        manage_topics = bool(flags & (1 << 18))
        send_photos = bool(flags & (1 << 19))
        send_videos = bool(flags & (1 << 20))
        send_roundvideos = bool(flags & (1 << 21))
        send_audios = bool(flags & (1 << 22))
        send_voices = bool(flags & (1 << 23))
        send_docs = bool(flags & (1 << 24))
        send_plain = bool(flags & (1 << 25))
        edit_rank = bool(flags & (1 << 26))
        send_reactions = bool(flags & (1 << 27))
        until_date = reader.read_int32()
        return cls(view_messages=view_messages, send_messages=send_messages, send_media=send_media, send_stickers=send_stickers, send_gifs=send_gifs, send_games=send_games, send_inline=send_inline, embed_links=embed_links, send_polls=send_polls, change_info=change_info, invite_users=invite_users, pin_messages=pin_messages, manage_topics=manage_topics, send_photos=send_photos, send_videos=send_videos, send_roundvideos=send_roundvideos, send_audios=send_audios, send_voices=send_voices, send_docs=send_docs, send_plain=send_plain, edit_rank=edit_rank, send_reactions=send_reactions, until_date=until_date)


@register_tl
class InputWallPaper(TLObject):
    ID: int = 0xe630b979

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputWallPaper':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputWallPaperSlug(TLObject):
    ID: int = 0x72091c80

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputWallPaperSlug':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class InputWallPaperNoFile(TLObject):
    ID: int = 0x967a462e

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputWallPaperNoFile':
        id = reader.read_int64()
        return cls(id=id)


@register_tl
class AccountWallPapersNotModified(TLObject):
    ID: int = 0x1c199183

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountWallPapersNotModified':
        return cls()


@register_tl
class AccountWallPapers(TLObject):
    ID: int = 0xcdc3858c

    def __init__(self, hash: Any = None, wallpapers: Any = None) -> None:
        self.hash = hash
        self.wallpapers = wallpapers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.wallpapers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountWallPapers':
        hash = reader.read_int64()
        wallpapers = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, wallpapers=wallpapers)


@register_tl
class CodeSettings(TLObject):
    ID: int = 0xad253d78

    def __init__(self, allow_flashcall: bool = False, current_number: bool = False, allow_app_hash: bool = False, allow_missed_call: bool = False, allow_firebase: bool = False, unknown_number: bool = False, logout_tokens: Any = None, token: Any = None, app_sandbox: Any = None) -> None:
        self.allow_flashcall = allow_flashcall
        self.current_number = current_number
        self.allow_app_hash = allow_app_hash
        self.allow_missed_call = allow_missed_call
        self.allow_firebase = allow_firebase
        self.unknown_number = unknown_number
        self.logout_tokens = logout_tokens
        self.token = token
        self.app_sandbox = app_sandbox

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.allow_flashcall:
            flags |= (1 << 0)
        if self.current_number:
            flags |= (1 << 1)
        if self.allow_app_hash:
            flags |= (1 << 4)
        if self.allow_missed_call:
            flags |= (1 << 5)
        if self.allow_firebase:
            flags |= (1 << 7)
        if self.unknown_number:
            flags |= (1 << 9)
        if self.logout_tokens is not None:
            flags |= (1 << 6)
        if self.token is not None:
            flags |= (1 << 8)
        if self.app_sandbox is not None:
            flags |= (1 << 8)
        writer.write_uint32(flags)
        if self.logout_tokens is not None:
            writer.write_vector(self.logout_tokens or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.token is not None:
            writer.write_string(self.token or '')
        if self.app_sandbox is not None:
            writer.write_bool(bool(self.app_sandbox))

    @classmethod
    def read(cls, reader: TLReader) -> 'CodeSettings':
        flags = reader.read_uint32()
        allow_flashcall = bool(flags & (1 << 0))
        current_number = bool(flags & (1 << 1))
        allow_app_hash = bool(flags & (1 << 4))
        allow_missed_call = bool(flags & (1 << 5))
        allow_firebase = bool(flags & (1 << 7))
        unknown_number = bool(flags & (1 << 9))
        logout_tokens = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 6)) else None
        token = reader.read_string() if (flags & (1 << 8)) else None
        app_sandbox = reader.read_bool() if (flags & (1 << 8)) else None
        return cls(allow_flashcall=allow_flashcall, current_number=current_number, allow_app_hash=allow_app_hash, allow_missed_call=allow_missed_call, allow_firebase=allow_firebase, unknown_number=unknown_number, logout_tokens=logout_tokens, token=token, app_sandbox=app_sandbox)


@register_tl
class WallPaperSettings(TLObject):
    ID: int = 0x372efcd0

    def __init__(self, blur: bool = False, motion: bool = False, background_color: Any = None, second_background_color: Any = None, third_background_color: Any = None, fourth_background_color: Any = None, intensity: Any = None, rotation: Any = None, emoticon: Any = None) -> None:
        self.blur = blur
        self.motion = motion
        self.background_color = background_color
        self.second_background_color = second_background_color
        self.third_background_color = third_background_color
        self.fourth_background_color = fourth_background_color
        self.intensity = intensity
        self.rotation = rotation
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blur:
            flags |= (1 << 1)
        if self.motion:
            flags |= (1 << 2)
        if self.background_color is not None:
            flags |= (1 << 0)
        if self.second_background_color is not None:
            flags |= (1 << 4)
        if self.third_background_color is not None:
            flags |= (1 << 5)
        if self.fourth_background_color is not None:
            flags |= (1 << 6)
        if self.intensity is not None:
            flags |= (1 << 3)
        if self.rotation is not None:
            flags |= (1 << 4)
        if self.emoticon is not None:
            flags |= (1 << 7)
        writer.write_uint32(flags)
        if self.background_color is not None:
            writer.write_int32(self.background_color or 0)
        if self.second_background_color is not None:
            writer.write_int32(self.second_background_color or 0)
        if self.third_background_color is not None:
            writer.write_int32(self.third_background_color or 0)
        if self.fourth_background_color is not None:
            writer.write_int32(self.fourth_background_color or 0)
        if self.intensity is not None:
            writer.write_int32(self.intensity or 0)
        if self.rotation is not None:
            writer.write_int32(self.rotation or 0)
        if self.emoticon is not None:
            writer.write_string(self.emoticon or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'WallPaperSettings':
        flags = reader.read_uint32()
        blur = bool(flags & (1 << 1))
        motion = bool(flags & (1 << 2))
        background_color = reader.read_int32() if (flags & (1 << 0)) else None
        second_background_color = reader.read_int32() if (flags & (1 << 4)) else None
        third_background_color = reader.read_int32() if (flags & (1 << 5)) else None
        fourth_background_color = reader.read_int32() if (flags & (1 << 6)) else None
        intensity = reader.read_int32() if (flags & (1 << 3)) else None
        rotation = reader.read_int32() if (flags & (1 << 4)) else None
        emoticon = reader.read_string() if (flags & (1 << 7)) else None
        return cls(blur=blur, motion=motion, background_color=background_color, second_background_color=second_background_color, third_background_color=third_background_color, fourth_background_color=fourth_background_color, intensity=intensity, rotation=rotation, emoticon=emoticon)


@register_tl
class AutoDownloadSettings(TLObject):
    ID: int = 0xbaa57628

    def __init__(self, disabled: bool = False, video_preload_large: bool = False, audio_preload_next: bool = False, phonecalls_less_data: bool = False, stories_preload: bool = False, photo_size_max: Any = None, video_size_max: Any = None, file_size_max: Any = None, video_upload_maxbitrate: Any = None, small_queue_active_operations_max: Any = None, large_queue_active_operations_max: Any = None) -> None:
        self.disabled = disabled
        self.video_preload_large = video_preload_large
        self.audio_preload_next = audio_preload_next
        self.phonecalls_less_data = phonecalls_less_data
        self.stories_preload = stories_preload
        self.photo_size_max = photo_size_max
        self.video_size_max = video_size_max
        self.file_size_max = file_size_max
        self.video_upload_maxbitrate = video_upload_maxbitrate
        self.small_queue_active_operations_max = small_queue_active_operations_max
        self.large_queue_active_operations_max = large_queue_active_operations_max

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.disabled:
            flags |= (1 << 0)
        if self.video_preload_large:
            flags |= (1 << 1)
        if self.audio_preload_next:
            flags |= (1 << 2)
        if self.phonecalls_less_data:
            flags |= (1 << 3)
        if self.stories_preload:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int32(self.photo_size_max or 0)
        writer.write_int64(self.video_size_max or 0)
        writer.write_int64(self.file_size_max or 0)
        writer.write_int32(self.video_upload_maxbitrate or 0)
        writer.write_int32(self.small_queue_active_operations_max or 0)
        writer.write_int32(self.large_queue_active_operations_max or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AutoDownloadSettings':
        flags = reader.read_uint32()
        disabled = bool(flags & (1 << 0))
        video_preload_large = bool(flags & (1 << 1))
        audio_preload_next = bool(flags & (1 << 2))
        phonecalls_less_data = bool(flags & (1 << 3))
        stories_preload = bool(flags & (1 << 4))
        photo_size_max = reader.read_int32()
        video_size_max = reader.read_int64()
        file_size_max = reader.read_int64()
        video_upload_maxbitrate = reader.read_int32()
        small_queue_active_operations_max = reader.read_int32()
        large_queue_active_operations_max = reader.read_int32()
        return cls(disabled=disabled, video_preload_large=video_preload_large, audio_preload_next=audio_preload_next, phonecalls_less_data=phonecalls_less_data, stories_preload=stories_preload, photo_size_max=photo_size_max, video_size_max=video_size_max, file_size_max=file_size_max, video_upload_maxbitrate=video_upload_maxbitrate, small_queue_active_operations_max=small_queue_active_operations_max, large_queue_active_operations_max=large_queue_active_operations_max)


@register_tl
class AccountAutoDownloadSettings(TLObject):
    ID: int = 0x63cacf26

    def __init__(self, low: Any = None, medium: Any = None, high: Any = None) -> None:
        self.low = low
        self.medium = medium
        self.high = high

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.low is not None and hasattr(self.low, 'write'): self.low.write(writer)
        if self.medium is not None and hasattr(self.medium, 'write'): self.medium.write(writer)
        if self.high is not None and hasattr(self.high, 'write'): self.high.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountAutoDownloadSettings':
        low = reader.read_object()
        medium = reader.read_object()
        high = reader.read_object()
        return cls(low=low, medium=medium, high=high)


@register_tl
class EmojiKeyword(TLObject):
    ID: int = 0xd5b3b9f9

    def __init__(self, keyword: Any = None, emoticons: Any = None) -> None:
        self.keyword = keyword
        self.emoticons = emoticons

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.keyword or '')
        writer.write_vector(self.emoticons or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiKeyword':
        keyword = reader.read_string()
        emoticons = reader.read_vector(lambda r: r.read_string())
        return cls(keyword=keyword, emoticons=emoticons)


@register_tl
class EmojiKeywordDeleted(TLObject):
    ID: int = 0x236df622

    def __init__(self, keyword: Any = None, emoticons: Any = None) -> None:
        self.keyword = keyword
        self.emoticons = emoticons

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.keyword or '')
        writer.write_vector(self.emoticons or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiKeywordDeleted':
        keyword = reader.read_string()
        emoticons = reader.read_vector(lambda r: r.read_string())
        return cls(keyword=keyword, emoticons=emoticons)


@register_tl
class EmojiKeywordsDifference(TLObject):
    ID: int = 0x5cc761bd

    def __init__(self, lang_code: Any = None, from_version: Any = None, version: Any = None, keywords: Any = None) -> None:
        self.lang_code = lang_code
        self.from_version = from_version
        self.version = version
        self.keywords = keywords

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')
        writer.write_int32(self.from_version or 0)
        writer.write_int32(self.version or 0)
        writer.write_vector(self.keywords or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiKeywordsDifference':
        lang_code = reader.read_string()
        from_version = reader.read_int32()
        version = reader.read_int32()
        keywords = reader.read_vector(lambda r: reader.read_object())
        return cls(lang_code=lang_code, from_version=from_version, version=version, keywords=keywords)


@register_tl
class EmojiURL(TLObject):
    ID: int = 0xa575739d

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiURL':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class EmojiLanguage(TLObject):
    ID: int = 0xb3fb5361

    def __init__(self, lang_code: Any = None) -> None:
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiLanguage':
        lang_code = reader.read_string()
        return cls(lang_code=lang_code)


@register_tl
class Folder(TLObject):
    ID: int = 0xff544e65

    def __init__(self, autofill_new_broadcasts: bool = False, autofill_public_groups: bool = False, autofill_new_correspondents: bool = False, photo: Any = None, id: Any = None, title: Any = None) -> None:
        self.autofill_new_broadcasts = autofill_new_broadcasts
        self.autofill_public_groups = autofill_public_groups
        self.autofill_new_correspondents = autofill_new_correspondents
        self.photo = photo
        self.id = id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.autofill_new_broadcasts:
            flags |= (1 << 0)
        if self.autofill_public_groups:
            flags |= (1 << 1)
        if self.autofill_new_correspondents:
            flags |= (1 << 2)
        if self.photo is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_string(self.title or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'Folder':
        flags = reader.read_uint32()
        autofill_new_broadcasts = bool(flags & (1 << 0))
        autofill_public_groups = bool(flags & (1 << 1))
        autofill_new_correspondents = bool(flags & (1 << 2))
        id = reader.read_int32()
        title = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 3)) else None
        return cls(autofill_new_broadcasts=autofill_new_broadcasts, autofill_public_groups=autofill_public_groups, autofill_new_correspondents=autofill_new_correspondents, id=id, title=title, photo=photo)


@register_tl
class InputFolderPeer(TLObject):
    ID: int = 0xfbd2c296

    def __init__(self, peer: Any = None, folder_id: Any = None) -> None:
        self.peer = peer
        self.folder_id = folder_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.folder_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputFolderPeer':
        peer = reader.read_object()
        folder_id = reader.read_int32()
        return cls(peer=peer, folder_id=folder_id)


@register_tl
class FolderPeer(TLObject):
    ID: int = 0xe9baa668

    def __init__(self, peer: Any = None, folder_id: Any = None) -> None:
        self.peer = peer
        self.folder_id = folder_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.folder_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'FolderPeer':
        peer = reader.read_object()
        folder_id = reader.read_int32()
        return cls(peer=peer, folder_id=folder_id)


@register_tl
class MessagesSearchCounter(TLObject):
    ID: int = 0xe844ebff

    def __init__(self, inexact: bool = False, filter: Any = None, count: Any = None) -> None:
        self.inexact = inexact
        self.filter = filter
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inexact:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchCounter':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 1))
        filter = reader.read_object()
        count = reader.read_int32()
        return cls(inexact=inexact, filter=filter, count=count)


@register_tl
class UrlAuthResultRequest(TLObject):
    ID: int = 0x3cd623ec

    def __init__(self, request_write_access: bool = False, request_phone_number: bool = False, match_codes_first: bool = False, is_app: bool = False, browser: Any = None, platform: Any = None, ip: Any = None, region: Any = None, match_codes: Any = None, user_id_hint: Any = None, verified_app_name: Any = None, bot: Any = None, domain: Any = None) -> None:
        self.request_write_access = request_write_access
        self.request_phone_number = request_phone_number
        self.match_codes_first = match_codes_first
        self.is_app = is_app
        self.browser = browser
        self.platform = platform
        self.ip = ip
        self.region = region
        self.match_codes = match_codes
        self.user_id_hint = user_id_hint
        self.verified_app_name = verified_app_name
        self.bot = bot
        self.domain = domain

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.request_write_access:
            flags |= (1 << 0)
        if self.request_phone_number:
            flags |= (1 << 1)
        if self.match_codes_first:
            flags |= (1 << 5)
        if self.is_app:
            flags |= (1 << 6)
        if self.browser is not None:
            flags |= (1 << 2)
        if self.platform is not None:
            flags |= (1 << 2)
        if self.ip is not None:
            flags |= (1 << 2)
        if self.region is not None:
            flags |= (1 << 2)
        if self.match_codes is not None:
            flags |= (1 << 3)
        if self.user_id_hint is not None:
            flags |= (1 << 4)
        if self.verified_app_name is not None:
            flags |= (1 << 7)
        writer.write_uint32(flags)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.domain or '')
        if self.browser is not None:
            writer.write_string(self.browser or '')
        if self.platform is not None:
            writer.write_string(self.platform or '')
        if self.ip is not None:
            writer.write_string(self.ip or '')
        if self.region is not None:
            writer.write_string(self.region or '')
        if self.match_codes is not None:
            writer.write_vector(self.match_codes or [], lambda w, x: w.write_string(x))
        if self.user_id_hint is not None:
            writer.write_int64(self.user_id_hint or 0)
        if self.verified_app_name is not None:
            writer.write_string(self.verified_app_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UrlAuthResultRequest':
        flags = reader.read_uint32()
        request_write_access = bool(flags & (1 << 0))
        request_phone_number = bool(flags & (1 << 1))
        match_codes_first = bool(flags & (1 << 5))
        is_app = bool(flags & (1 << 6))
        bot = reader.read_object()
        domain = reader.read_string()
        browser = reader.read_string() if (flags & (1 << 2)) else None
        platform = reader.read_string() if (flags & (1 << 2)) else None
        ip = reader.read_string() if (flags & (1 << 2)) else None
        region = reader.read_string() if (flags & (1 << 2)) else None
        match_codes = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 3)) else None
        user_id_hint = reader.read_int64() if (flags & (1 << 4)) else None
        verified_app_name = reader.read_string() if (flags & (1 << 7)) else None
        return cls(request_write_access=request_write_access, request_phone_number=request_phone_number, match_codes_first=match_codes_first, is_app=is_app, bot=bot, domain=domain, browser=browser, platform=platform, ip=ip, region=region, match_codes=match_codes, user_id_hint=user_id_hint, verified_app_name=verified_app_name)


@register_tl
class UrlAuthResultAccepted(TLObject):
    ID: int = 0x623a8fa0

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.url is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.url is not None:
            writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UrlAuthResultAccepted':
        flags = reader.read_uint32()
        url = reader.read_string() if (flags & (1 << 0)) else None
        return cls(url=url)


@register_tl
class UrlAuthResultDefault(TLObject):
    ID: int = 0xa9d6db1f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UrlAuthResultDefault':
        return cls()


@register_tl
class ChannelLocationEmpty(TLObject):
    ID: int = 0xbfb5ad8b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelLocationEmpty':
        return cls()


@register_tl
class ChannelLocation(TLObject):
    ID: int = 0x209b82db

    def __init__(self, geo_point: Any = None, address: Any = None) -> None:
        self.geo_point = geo_point
        self.address = address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        writer.write_string(self.address or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelLocation':
        geo_point = reader.read_object()
        address = reader.read_string()
        return cls(geo_point=geo_point, address=address)


@register_tl
class PeerLocated(TLObject):
    ID: int = 0xca461b5d

    def __init__(self, peer: Any = None, expires: Any = None, distance: Any = None) -> None:
        self.peer = peer
        self.expires = expires
        self.distance = distance

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.expires or 0)
        writer.write_int32(self.distance or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerLocated':
        peer = reader.read_object()
        expires = reader.read_int32()
        distance = reader.read_int32()
        return cls(peer=peer, expires=expires, distance=distance)


@register_tl
class PeerSelfLocated(TLObject):
    ID: int = 0xf8ec284b

    def __init__(self, expires: Any = None) -> None:
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.expires or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerSelfLocated':
        expires = reader.read_int32()
        return cls(expires=expires)

