from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class RestrictionReason(TLObject):
    ID: int = 0xd072acb4

    def __init__(self, platform: Any = None, reason: Any = None, text: Any = None) -> None:
        self.platform = platform
        self.reason = reason
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.platform or '')
        writer.write_string(self.reason or '')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'RestrictionReason':
        platform = reader.read_string()
        reason = reader.read_string()
        text = reader.read_string()
        return cls(platform=platform, reason=reason, text=text)


@register_tl
class InputTheme(TLObject):
    ID: int = 0x3c5693e9

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputTheme':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputThemeSlug(TLObject):
    ID: int = 0xf5890df1

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputThemeSlug':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class Theme(TLObject):
    ID: int = 0xa00e67d6

    def __init__(self, creator: bool = False, default: bool = False, for_chat: bool = False, document: Any = None, settings: Any = None, emoticon: Any = None, installs_count: Any = None, id: Any = None, access_hash: Any = None, slug: Any = None, title: Any = None) -> None:
        self.creator = creator
        self.default = default
        self.for_chat = for_chat
        self.document = document
        self.settings = settings
        self.emoticon = emoticon
        self.installs_count = installs_count
        self.id = id
        self.access_hash = access_hash
        self.slug = slug
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.creator:
            flags |= (1 << 0)
        if self.default:
            flags |= (1 << 1)
        if self.for_chat:
            flags |= (1 << 5)
        if self.document is not None:
            flags |= (1 << 2)
        if self.settings is not None:
            flags |= (1 << 3)
        if self.emoticon is not None:
            flags |= (1 << 6)
        if self.installs_count is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_string(self.slug or '')
        writer.write_string(self.title or '')
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.settings is not None:
            writer.write_vector(self.settings or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.emoticon is not None:
            writer.write_string(self.emoticon or '')
        if self.installs_count is not None:
            writer.write_int32(self.installs_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Theme':
        flags = reader.read_uint32()
        creator = bool(flags & (1 << 0))
        default = bool(flags & (1 << 1))
        for_chat = bool(flags & (1 << 5))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        slug = reader.read_string()
        title = reader.read_string()
        document = reader.read_object() if (flags & (1 << 2)) else None
        settings = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        emoticon = reader.read_string() if (flags & (1 << 6)) else None
        installs_count = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(creator=creator, default=default, for_chat=for_chat, id=id, access_hash=access_hash, slug=slug, title=title, document=document, settings=settings, emoticon=emoticon, installs_count=installs_count)


@register_tl
class AccountThemesNotModified(TLObject):
    ID: int = 0xf41eb622

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountThemesNotModified':
        return cls()


@register_tl
class AccountThemes(TLObject):
    ID: int = 0x9a3d8c6d

    def __init__(self, hash: Any = None, themes: Any = None) -> None:
        self.hash = hash
        self.themes = themes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.themes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountThemes':
        hash = reader.read_int64()
        themes = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, themes=themes)


@register_tl
class AuthLoginToken(TLObject):
    ID: int = 0x629f1980

    def __init__(self, expires: Any = None, token: Any = None) -> None:
        self.expires = expires
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.expires or 0)
        writer.write_bytes(self.token or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthLoginToken':
        expires = reader.read_int32()
        token = reader.read_bytes()
        return cls(expires=expires, token=token)


@register_tl
class AuthLoginTokenMigrateTo(TLObject):
    ID: int = 0x68e9916

    def __init__(self, dc_id: Any = None, token: Any = None) -> None:
        self.dc_id = dc_id
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id or 0)
        writer.write_bytes(self.token or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthLoginTokenMigrateTo':
        dc_id = reader.read_int32()
        token = reader.read_bytes()
        return cls(dc_id=dc_id, token=token)


@register_tl
class AuthLoginTokenSuccess(TLObject):
    ID: int = 0x390d5c5e

    def __init__(self, authorization: Any = None) -> None:
        self.authorization = authorization

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.authorization is not None and hasattr(self.authorization, 'write'): self.authorization.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthLoginTokenSuccess':
        authorization = reader.read_object()
        return cls(authorization=authorization)


@register_tl
class AccountContentSettings(TLObject):
    ID: int = 0x57e28221

    def __init__(self, sensitive_enabled: bool = False, sensitive_can_change: bool = False) -> None:
        self.sensitive_enabled = sensitive_enabled
        self.sensitive_can_change = sensitive_can_change

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sensitive_enabled:
            flags |= (1 << 0)
        if self.sensitive_can_change:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountContentSettings':
        flags = reader.read_uint32()
        sensitive_enabled = bool(flags & (1 << 0))
        sensitive_can_change = bool(flags & (1 << 1))
        return cls(sensitive_enabled=sensitive_enabled, sensitive_can_change=sensitive_can_change)


@register_tl
class MessagesInactiveChats(TLObject):
    ID: int = 0xa927fec5

    def __init__(self, dates: Any = None, chats: Any = None, users: Any = None) -> None:
        self.dates = dates
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dates or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesInactiveChats':
        dates = reader.read_vector(lambda r: r.read_int32())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(dates=dates, chats=chats, users=users)


@register_tl
class BaseThemeClassic(TLObject):
    ID: int = 0xc3a12462

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BaseThemeClassic':
        return cls()


@register_tl
class BaseThemeDay(TLObject):
    ID: int = 0xfbd81688

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BaseThemeDay':
        return cls()


@register_tl
class BaseThemeNight(TLObject):
    ID: int = 0xb7b31ea8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BaseThemeNight':
        return cls()


@register_tl
class BaseThemeTinted(TLObject):
    ID: int = 0x6d5f77ee

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BaseThemeTinted':
        return cls()


@register_tl
class BaseThemeArctic(TLObject):
    ID: int = 0x5b11125a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BaseThemeArctic':
        return cls()


@register_tl
class InputThemeSettings(TLObject):
    ID: int = 0x8fde504f

    def __init__(self, message_colors_animated: bool = False, outbox_accent_color: Any = None, message_colors: Any = None, wallpaper: Any = None, wallpaper_settings: Any = None, base_theme: Any = None, accent_color: Any = None) -> None:
        self.message_colors_animated = message_colors_animated
        self.outbox_accent_color = outbox_accent_color
        self.message_colors = message_colors
        self.wallpaper = wallpaper
        self.wallpaper_settings = wallpaper_settings
        self.base_theme = base_theme
        self.accent_color = accent_color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.message_colors_animated:
            flags |= (1 << 2)
        if self.outbox_accent_color is not None:
            flags |= (1 << 3)
        if self.message_colors is not None:
            flags |= (1 << 0)
        if self.wallpaper is not None:
            flags |= (1 << 1)
        if self.wallpaper_settings is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.base_theme is not None and hasattr(self.base_theme, 'write'): self.base_theme.write(writer)
        writer.write_int32(self.accent_color or 0)
        if self.outbox_accent_color is not None:
            writer.write_int32(self.outbox_accent_color or 0)
        if self.message_colors is not None:
            writer.write_vector(self.message_colors or [], lambda w, x: w.write_int32(x))
        if self.wallpaper is not None:
            if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)
        if self.wallpaper_settings is not None:
            if self.wallpaper_settings is not None and hasattr(self.wallpaper_settings, 'write'): self.wallpaper_settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputThemeSettings':
        flags = reader.read_uint32()
        message_colors_animated = bool(flags & (1 << 2))
        base_theme = reader.read_object()
        accent_color = reader.read_int32()
        outbox_accent_color = reader.read_int32() if (flags & (1 << 3)) else None
        message_colors = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        wallpaper = reader.read_object() if (flags & (1 << 1)) else None
        wallpaper_settings = reader.read_object() if (flags & (1 << 1)) else None
        return cls(message_colors_animated=message_colors_animated, base_theme=base_theme, accent_color=accent_color, outbox_accent_color=outbox_accent_color, message_colors=message_colors, wallpaper=wallpaper, wallpaper_settings=wallpaper_settings)


@register_tl
class ThemeSettings(TLObject):
    ID: int = 0xfa58b6d4

    def __init__(self, message_colors_animated: bool = False, outbox_accent_color: Any = None, message_colors: Any = None, wallpaper: Any = None, base_theme: Any = None, accent_color: Any = None) -> None:
        self.message_colors_animated = message_colors_animated
        self.outbox_accent_color = outbox_accent_color
        self.message_colors = message_colors
        self.wallpaper = wallpaper
        self.base_theme = base_theme
        self.accent_color = accent_color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.message_colors_animated:
            flags |= (1 << 2)
        if self.outbox_accent_color is not None:
            flags |= (1 << 3)
        if self.message_colors is not None:
            flags |= (1 << 0)
        if self.wallpaper is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.base_theme is not None and hasattr(self.base_theme, 'write'): self.base_theme.write(writer)
        writer.write_int32(self.accent_color or 0)
        if self.outbox_accent_color is not None:
            writer.write_int32(self.outbox_accent_color or 0)
        if self.message_colors is not None:
            writer.write_vector(self.message_colors or [], lambda w, x: w.write_int32(x))
        if self.wallpaper is not None:
            if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ThemeSettings':
        flags = reader.read_uint32()
        message_colors_animated = bool(flags & (1 << 2))
        base_theme = reader.read_object()
        accent_color = reader.read_int32()
        outbox_accent_color = reader.read_int32() if (flags & (1 << 3)) else None
        message_colors = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        wallpaper = reader.read_object() if (flags & (1 << 1)) else None
        return cls(message_colors_animated=message_colors_animated, base_theme=base_theme, accent_color=accent_color, outbox_accent_color=outbox_accent_color, message_colors=message_colors, wallpaper=wallpaper)


@register_tl
class WebPageAttributeTheme(TLObject):
    ID: int = 0x54b56617

    def __init__(self, documents: Any = None, settings: Any = None) -> None:
        self.documents = documents
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.documents is not None:
            flags |= (1 << 0)
        if self.settings is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.documents is not None:
            writer.write_vector(self.documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.settings is not None:
            if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageAttributeTheme':
        flags = reader.read_uint32()
        documents = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        settings = reader.read_object() if (flags & (1 << 1)) else None
        return cls(documents=documents, settings=settings)


@register_tl
class WebPageAttributeStory(TLObject):
    ID: int = 0x2e94c3e7

    def __init__(self, story: Any = None, peer: Any = None, id: Any = None) -> None:
        self.story = story
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.story is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.story is not None:
            if self.story is not None and hasattr(self.story, 'write'): self.story.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageAttributeStory':
        flags = reader.read_uint32()
        peer = reader.read_object()
        id = reader.read_int32()
        story = reader.read_object() if (flags & (1 << 0)) else None
        return cls(peer=peer, id=id, story=story)


@register_tl
class WebPageAttributeStickerSet(TLObject):
    ID: int = 0x50cc03d3

    def __init__(self, emojis: bool = False, text_color: bool = False, stickers: Any = None) -> None:
        self.emojis = emojis
        self.text_color = text_color
        self.stickers = stickers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.emojis:
            flags |= (1 << 0)
        if self.text_color:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageAttributeStickerSet':
        flags = reader.read_uint32()
        emojis = bool(flags & (1 << 0))
        text_color = bool(flags & (1 << 1))
        stickers = reader.read_vector(lambda r: reader.read_object())
        return cls(emojis=emojis, text_color=text_color, stickers=stickers)


@register_tl
class WebPageAttributeUniqueStarGift(TLObject):
    ID: int = 0xcf6f6db8

    def __init__(self, gift: Any = None) -> None:
        self.gift = gift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageAttributeUniqueStarGift':
        gift = reader.read_object()
        return cls(gift=gift)


@register_tl
class WebPageAttributeStarGiftCollection(TLObject):
    ID: int = 0x31cad303

    def __init__(self, icons: Any = None) -> None:
        self.icons = icons

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.icons or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageAttributeStarGiftCollection':
        icons = reader.read_vector(lambda r: reader.read_object())
        return cls(icons=icons)


@register_tl
class WebPageAttributeStarGiftAuction(TLObject):
    ID: int = 0x1c641c2

    def __init__(self, gift: Any = None, end_date: Any = None) -> None:
        self.gift = gift
        self.end_date = end_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        writer.write_int32(self.end_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageAttributeStarGiftAuction':
        gift = reader.read_object()
        end_date = reader.read_int32()
        return cls(gift=gift, end_date=end_date)


@register_tl
class WebPageAttributeAiComposeTone(TLObject):
    ID: int = 0x7781fe18

    def __init__(self, emoji_id: Any = None) -> None:
        self.emoji_id = emoji_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.emoji_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageAttributeAiComposeTone':
        emoji_id = reader.read_int64()
        return cls(emoji_id=emoji_id)


@register_tl
class MessagesVotesList(TLObject):
    ID: int = 0x4899484e

    def __init__(self, next_offset: Any = None, count: Any = None, votes: Any = None, chats: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.count = count
        self.votes = votes
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.votes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesVotesList':
        flags = reader.read_uint32()
        count = reader.read_int32()
        votes = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        return cls(count=count, votes=votes, chats=chats, users=users, next_offset=next_offset)


@register_tl
class BankCardOpenUrl(TLObject):
    ID: int = 0xf568028a

    def __init__(self, url: Any = None, name: Any = None) -> None:
        self.url = url
        self.name = name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_string(self.name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BankCardOpenUrl':
        url = reader.read_string()
        name = reader.read_string()
        return cls(url=url, name=name)


@register_tl
class PaymentsBankCardData(TLObject):
    ID: int = 0x3e24e573

    def __init__(self, title: Any = None, open_urls: Any = None) -> None:
        self.title = title
        self.open_urls = open_urls

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_vector(self.open_urls or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsBankCardData':
        title = reader.read_string()
        open_urls = reader.read_vector(lambda r: reader.read_object())
        return cls(title=title, open_urls=open_urls)


@register_tl
class DialogFilter(TLObject):
    ID: int = 0xaa472651

    def __init__(self, contacts: bool = False, non_contacts: bool = False, groups: bool = False, broadcasts: bool = False, bots: bool = False, exclude_muted: bool = False, exclude_read: bool = False, exclude_archived: bool = False, title_noanimate: bool = False, emoticon: Any = None, color: Any = None, id: Any = None, title: Any = None, pinned_peers: Any = None, include_peers: Any = None, exclude_peers: Any = None) -> None:
        self.contacts = contacts
        self.non_contacts = non_contacts
        self.groups = groups
        self.broadcasts = broadcasts
        self.bots = bots
        self.exclude_muted = exclude_muted
        self.exclude_read = exclude_read
        self.exclude_archived = exclude_archived
        self.title_noanimate = title_noanimate
        self.emoticon = emoticon
        self.color = color
        self.id = id
        self.title = title
        self.pinned_peers = pinned_peers
        self.include_peers = include_peers
        self.exclude_peers = exclude_peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.contacts:
            flags |= (1 << 0)
        if self.non_contacts:
            flags |= (1 << 1)
        if self.groups:
            flags |= (1 << 2)
        if self.broadcasts:
            flags |= (1 << 3)
        if self.bots:
            flags |= (1 << 4)
        if self.exclude_muted:
            flags |= (1 << 11)
        if self.exclude_read:
            flags |= (1 << 12)
        if self.exclude_archived:
            flags |= (1 << 13)
        if self.title_noanimate:
            flags |= (1 << 28)
        if self.emoticon is not None:
            flags |= (1 << 25)
        if self.color is not None:
            flags |= (1 << 27)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)
        if self.emoticon is not None:
            writer.write_string(self.emoticon or '')
        if self.color is not None:
            writer.write_int32(self.color or 0)
        writer.write_vector(self.pinned_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.include_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.exclude_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogFilter':
        flags = reader.read_uint32()
        contacts = bool(flags & (1 << 0))
        non_contacts = bool(flags & (1 << 1))
        groups = bool(flags & (1 << 2))
        broadcasts = bool(flags & (1 << 3))
        bots = bool(flags & (1 << 4))
        exclude_muted = bool(flags & (1 << 11))
        exclude_read = bool(flags & (1 << 12))
        exclude_archived = bool(flags & (1 << 13))
        title_noanimate = bool(flags & (1 << 28))
        id = reader.read_int32()
        title = reader.read_object()
        emoticon = reader.read_string() if (flags & (1 << 25)) else None
        color = reader.read_int32() if (flags & (1 << 27)) else None
        pinned_peers = reader.read_vector(lambda r: reader.read_object())
        include_peers = reader.read_vector(lambda r: reader.read_object())
        exclude_peers = reader.read_vector(lambda r: reader.read_object())
        return cls(contacts=contacts, non_contacts=non_contacts, groups=groups, broadcasts=broadcasts, bots=bots, exclude_muted=exclude_muted, exclude_read=exclude_read, exclude_archived=exclude_archived, title_noanimate=title_noanimate, id=id, title=title, emoticon=emoticon, color=color, pinned_peers=pinned_peers, include_peers=include_peers, exclude_peers=exclude_peers)


@register_tl
class DialogFilterDefault(TLObject):
    ID: int = 0x363293ae

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogFilterDefault':
        return cls()


@register_tl
class DialogFilterChatlist(TLObject):
    ID: int = 0x96537bd7

    def __init__(self, has_my_invites: bool = False, title_noanimate: bool = False, emoticon: Any = None, color: Any = None, id: Any = None, title: Any = None, pinned_peers: Any = None, include_peers: Any = None) -> None:
        self.has_my_invites = has_my_invites
        self.title_noanimate = title_noanimate
        self.emoticon = emoticon
        self.color = color
        self.id = id
        self.title = title
        self.pinned_peers = pinned_peers
        self.include_peers = include_peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_my_invites:
            flags |= (1 << 26)
        if self.title_noanimate:
            flags |= (1 << 28)
        if self.emoticon is not None:
            flags |= (1 << 25)
        if self.color is not None:
            flags |= (1 << 27)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)
        if self.emoticon is not None:
            writer.write_string(self.emoticon or '')
        if self.color is not None:
            writer.write_int32(self.color or 0)
        writer.write_vector(self.pinned_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.include_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogFilterChatlist':
        flags = reader.read_uint32()
        has_my_invites = bool(flags & (1 << 26))
        title_noanimate = bool(flags & (1 << 28))
        id = reader.read_int32()
        title = reader.read_object()
        emoticon = reader.read_string() if (flags & (1 << 25)) else None
        color = reader.read_int32() if (flags & (1 << 27)) else None
        pinned_peers = reader.read_vector(lambda r: reader.read_object())
        include_peers = reader.read_vector(lambda r: reader.read_object())
        return cls(has_my_invites=has_my_invites, title_noanimate=title_noanimate, id=id, title=title, emoticon=emoticon, color=color, pinned_peers=pinned_peers, include_peers=include_peers)


@register_tl
class DialogFilterSuggested(TLObject):
    ID: int = 0x77744d4a

    def __init__(self, filter: Any = None, description: Any = None) -> None:
        self.filter = filter
        self.description = description

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_string(self.description or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogFilterSuggested':
        filter = reader.read_object()
        description = reader.read_string()
        return cls(filter=filter, description=description)


@register_tl
class StatsDateRangeDays(TLObject):
    ID: int = 0xb637edaf

    def __init__(self, min_date: Any = None, max_date: Any = None) -> None:
        self.min_date = min_date
        self.max_date = max_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.min_date or 0)
        writer.write_int32(self.max_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsDateRangeDays':
        min_date = reader.read_int32()
        max_date = reader.read_int32()
        return cls(min_date=min_date, max_date=max_date)


@register_tl
class StatsAbsValueAndPrev(TLObject):
    ID: int = 0xcb43acde

    def __init__(self, current: Any = None, previous: Any = None) -> None:
        self.current = current
        self.previous = previous

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_double(self.current or 0.0)
        writer.write_double(self.previous or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsAbsValueAndPrev':
        current = reader.read_double()
        previous = reader.read_double()
        return cls(current=current, previous=previous)


@register_tl
class StatsPercentValue(TLObject):
    ID: int = 0xcbce2fe0

    def __init__(self, part: Any = None, total: Any = None) -> None:
        self.part = part
        self.total = total

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_double(self.part or 0.0)
        writer.write_double(self.total or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsPercentValue':
        part = reader.read_double()
        total = reader.read_double()
        return cls(part=part, total=total)


@register_tl
class StatsGraphAsync(TLObject):
    ID: int = 0x4a27eb2d

    def __init__(self, token: Any = None) -> None:
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGraphAsync':
        token = reader.read_string()
        return cls(token=token)


@register_tl
class StatsGraphError(TLObject):
    ID: int = 0xbedc9822

    def __init__(self, error: Any = None) -> None:
        self.error = error

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.error or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGraphError':
        error = reader.read_string()
        return cls(error=error)


@register_tl
class StatsGraph(TLObject):
    ID: int = 0x8ea464b6

    def __init__(self, zoom_token: Any = None, json: Any = None) -> None:
        self.zoom_token = zoom_token
        self.json = json

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.zoom_token is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.json is not None and hasattr(self.json, 'write'): self.json.write(writer)
        if self.zoom_token is not None:
            writer.write_string(self.zoom_token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGraph':
        flags = reader.read_uint32()
        json = reader.read_object()
        zoom_token = reader.read_string() if (flags & (1 << 0)) else None
        return cls(json=json, zoom_token=zoom_token)


@register_tl
class StatsBroadcastStats(TLObject):
    ID: int = 0x396ca5fc

    def __init__(self, period: Any = None, followers: Any = None, views_per_post: Any = None, shares_per_post: Any = None, reactions_per_post: Any = None, views_per_story: Any = None, shares_per_story: Any = None, reactions_per_story: Any = None, enabled_notifications: Any = None, growth_graph: Any = None, followers_graph: Any = None, mute_graph: Any = None, top_hours_graph: Any = None, interactions_graph: Any = None, iv_interactions_graph: Any = None, views_by_source_graph: Any = None, new_followers_by_source_graph: Any = None, languages_graph: Any = None, reactions_by_emotion_graph: Any = None, story_interactions_graph: Any = None, story_reactions_by_emotion_graph: Any = None, recent_posts_interactions: Any = None) -> None:
        self.period = period
        self.followers = followers
        self.views_per_post = views_per_post
        self.shares_per_post = shares_per_post
        self.reactions_per_post = reactions_per_post
        self.views_per_story = views_per_story
        self.shares_per_story = shares_per_story
        self.reactions_per_story = reactions_per_story
        self.enabled_notifications = enabled_notifications
        self.growth_graph = growth_graph
        self.followers_graph = followers_graph
        self.mute_graph = mute_graph
        self.top_hours_graph = top_hours_graph
        self.interactions_graph = interactions_graph
        self.iv_interactions_graph = iv_interactions_graph
        self.views_by_source_graph = views_by_source_graph
        self.new_followers_by_source_graph = new_followers_by_source_graph
        self.languages_graph = languages_graph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph
        self.story_interactions_graph = story_interactions_graph
        self.story_reactions_by_emotion_graph = story_reactions_by_emotion_graph
        self.recent_posts_interactions = recent_posts_interactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.period is not None and hasattr(self.period, 'write'): self.period.write(writer)
        if self.followers is not None and hasattr(self.followers, 'write'): self.followers.write(writer)
        if self.views_per_post is not None and hasattr(self.views_per_post, 'write'): self.views_per_post.write(writer)
        if self.shares_per_post is not None and hasattr(self.shares_per_post, 'write'): self.shares_per_post.write(writer)
        if self.reactions_per_post is not None and hasattr(self.reactions_per_post, 'write'): self.reactions_per_post.write(writer)
        if self.views_per_story is not None and hasattr(self.views_per_story, 'write'): self.views_per_story.write(writer)
        if self.shares_per_story is not None and hasattr(self.shares_per_story, 'write'): self.shares_per_story.write(writer)
        if self.reactions_per_story is not None and hasattr(self.reactions_per_story, 'write'): self.reactions_per_story.write(writer)
        if self.enabled_notifications is not None and hasattr(self.enabled_notifications, 'write'): self.enabled_notifications.write(writer)
        if self.growth_graph is not None and hasattr(self.growth_graph, 'write'): self.growth_graph.write(writer)
        if self.followers_graph is not None and hasattr(self.followers_graph, 'write'): self.followers_graph.write(writer)
        if self.mute_graph is not None and hasattr(self.mute_graph, 'write'): self.mute_graph.write(writer)
        if self.top_hours_graph is not None and hasattr(self.top_hours_graph, 'write'): self.top_hours_graph.write(writer)
        if self.interactions_graph is not None and hasattr(self.interactions_graph, 'write'): self.interactions_graph.write(writer)
        if self.iv_interactions_graph is not None and hasattr(self.iv_interactions_graph, 'write'): self.iv_interactions_graph.write(writer)
        if self.views_by_source_graph is not None and hasattr(self.views_by_source_graph, 'write'): self.views_by_source_graph.write(writer)
        if self.new_followers_by_source_graph is not None and hasattr(self.new_followers_by_source_graph, 'write'): self.new_followers_by_source_graph.write(writer)
        if self.languages_graph is not None and hasattr(self.languages_graph, 'write'): self.languages_graph.write(writer)
        if self.reactions_by_emotion_graph is not None and hasattr(self.reactions_by_emotion_graph, 'write'): self.reactions_by_emotion_graph.write(writer)
        if self.story_interactions_graph is not None and hasattr(self.story_interactions_graph, 'write'): self.story_interactions_graph.write(writer)
        if self.story_reactions_by_emotion_graph is not None and hasattr(self.story_reactions_by_emotion_graph, 'write'): self.story_reactions_by_emotion_graph.write(writer)
        writer.write_vector(self.recent_posts_interactions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsBroadcastStats':
        period = reader.read_object()
        followers = reader.read_object()
        views_per_post = reader.read_object()
        shares_per_post = reader.read_object()
        reactions_per_post = reader.read_object()
        views_per_story = reader.read_object()
        shares_per_story = reader.read_object()
        reactions_per_story = reader.read_object()
        enabled_notifications = reader.read_object()
        growth_graph = reader.read_object()
        followers_graph = reader.read_object()
        mute_graph = reader.read_object()
        top_hours_graph = reader.read_object()
        interactions_graph = reader.read_object()
        iv_interactions_graph = reader.read_object()
        views_by_source_graph = reader.read_object()
        new_followers_by_source_graph = reader.read_object()
        languages_graph = reader.read_object()
        reactions_by_emotion_graph = reader.read_object()
        story_interactions_graph = reader.read_object()
        story_reactions_by_emotion_graph = reader.read_object()
        recent_posts_interactions = reader.read_vector(lambda r: reader.read_object())
        return cls(period=period, followers=followers, views_per_post=views_per_post, shares_per_post=shares_per_post, reactions_per_post=reactions_per_post, views_per_story=views_per_story, shares_per_story=shares_per_story, reactions_per_story=reactions_per_story, enabled_notifications=enabled_notifications, growth_graph=growth_graph, followers_graph=followers_graph, mute_graph=mute_graph, top_hours_graph=top_hours_graph, interactions_graph=interactions_graph, iv_interactions_graph=iv_interactions_graph, views_by_source_graph=views_by_source_graph, new_followers_by_source_graph=new_followers_by_source_graph, languages_graph=languages_graph, reactions_by_emotion_graph=reactions_by_emotion_graph, story_interactions_graph=story_interactions_graph, story_reactions_by_emotion_graph=story_reactions_by_emotion_graph, recent_posts_interactions=recent_posts_interactions)


@register_tl
class HelpPromoDataEmpty(TLObject):
    ID: int = 0x98f6ac75

    def __init__(self, expires: Any = None) -> None:
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.expires or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPromoDataEmpty':
        expires = reader.read_int32()
        return cls(expires=expires)


@register_tl
class HelpPromoData(TLObject):
    ID: int = 0x8a4d87a

    def __init__(self, proxy: bool = False, peer: Any = None, psa_type: Any = None, psa_message: Any = None, custom_pending_suggestion: Any = None, expires: Any = None, pending_suggestions: Any = None, dismissed_suggestions: Any = None, chats: Any = None, users: Any = None) -> None:
        self.proxy = proxy
        self.peer = peer
        self.psa_type = psa_type
        self.psa_message = psa_message
        self.custom_pending_suggestion = custom_pending_suggestion
        self.expires = expires
        self.pending_suggestions = pending_suggestions
        self.dismissed_suggestions = dismissed_suggestions
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.proxy:
            flags |= (1 << 0)
        if self.peer is not None:
            flags |= (1 << 3)
        if self.psa_type is not None:
            flags |= (1 << 1)
        if self.psa_message is not None:
            flags |= (1 << 2)
        if self.custom_pending_suggestion is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int32(self.expires or 0)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.psa_type is not None:
            writer.write_string(self.psa_type or '')
        if self.psa_message is not None:
            writer.write_string(self.psa_message or '')
        writer.write_vector(self.pending_suggestions or [], lambda w, x: w.write_string(x))
        writer.write_vector(self.dismissed_suggestions or [], lambda w, x: w.write_string(x))
        if self.custom_pending_suggestion is not None:
            if self.custom_pending_suggestion is not None and hasattr(self.custom_pending_suggestion, 'write'): self.custom_pending_suggestion.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPromoData':
        flags = reader.read_uint32()
        proxy = bool(flags & (1 << 0))
        expires = reader.read_int32()
        peer = reader.read_object() if (flags & (1 << 3)) else None
        psa_type = reader.read_string() if (flags & (1 << 1)) else None
        psa_message = reader.read_string() if (flags & (1 << 2)) else None
        pending_suggestions = reader.read_vector(lambda r: r.read_string())
        dismissed_suggestions = reader.read_vector(lambda r: r.read_string())
        custom_pending_suggestion = reader.read_object() if (flags & (1 << 4)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(proxy=proxy, expires=expires, peer=peer, psa_type=psa_type, psa_message=psa_message, pending_suggestions=pending_suggestions, dismissed_suggestions=dismissed_suggestions, custom_pending_suggestion=custom_pending_suggestion, chats=chats, users=users)


@register_tl
class VideoSize(TLObject):
    ID: int = 0xde33b094

    def __init__(self, video_start_ts: Any = None, type: Any = None, w: Any = None, h: Any = None, size: Any = None) -> None:
        self.video_start_ts = video_start_ts
        self.type = type
        self.w = w
        self.h = h
        self.size = size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video_start_ts is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.type or '')
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)
        if self.video_start_ts is not None:
            writer.write_double(self.video_start_ts or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'VideoSize':
        flags = reader.read_uint32()
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        video_start_ts = reader.read_double() if (flags & (1 << 0)) else None
        return cls(type=type, w=w, h=h, size=size, video_start_ts=video_start_ts)


@register_tl
class VideoSizeEmojiMarkup(TLObject):
    ID: int = 0xf85c413c

    def __init__(self, emoji_id: Any = None, background_colors: Any = None) -> None:
        self.emoji_id = emoji_id
        self.background_colors = background_colors

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.emoji_id or 0)
        writer.write_vector(self.background_colors or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'VideoSizeEmojiMarkup':
        emoji_id = reader.read_int64()
        background_colors = reader.read_vector(lambda r: r.read_int32())
        return cls(emoji_id=emoji_id, background_colors=background_colors)


@register_tl
class VideoSizeStickerMarkup(TLObject):
    ID: int = 0xda082fe

    def __init__(self, stickerset: Any = None, sticker_id: Any = None, background_colors: Any = None) -> None:
        self.stickerset = stickerset
        self.sticker_id = sticker_id
        self.background_colors = background_colors

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        writer.write_int64(self.sticker_id or 0)
        writer.write_vector(self.background_colors or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'VideoSizeStickerMarkup':
        stickerset = reader.read_object()
        sticker_id = reader.read_int64()
        background_colors = reader.read_vector(lambda r: r.read_int32())
        return cls(stickerset=stickerset, sticker_id=sticker_id, background_colors=background_colors)


@register_tl
class StatsGroupTopPoster(TLObject):
    ID: int = 0x9d04af9b

    def __init__(self, user_id: Any = None, messages: Any = None, avg_chars: Any = None) -> None:
        self.user_id = user_id
        self.messages = messages
        self.avg_chars = avg_chars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.messages or 0)
        writer.write_int32(self.avg_chars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGroupTopPoster':
        user_id = reader.read_int64()
        messages = reader.read_int32()
        avg_chars = reader.read_int32()
        return cls(user_id=user_id, messages=messages, avg_chars=avg_chars)


@register_tl
class StatsGroupTopAdmin(TLObject):
    ID: int = 0xd7584c87

    def __init__(self, user_id: Any = None, deleted: Any = None, kicked: Any = None, banned: Any = None) -> None:
        self.user_id = user_id
        self.deleted = deleted
        self.kicked = kicked
        self.banned = banned

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.deleted or 0)
        writer.write_int32(self.kicked or 0)
        writer.write_int32(self.banned or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGroupTopAdmin':
        user_id = reader.read_int64()
        deleted = reader.read_int32()
        kicked = reader.read_int32()
        banned = reader.read_int32()
        return cls(user_id=user_id, deleted=deleted, kicked=kicked, banned=banned)


@register_tl
class StatsGroupTopInviter(TLObject):
    ID: int = 0x535f779d

    def __init__(self, user_id: Any = None, invitations: Any = None) -> None:
        self.user_id = user_id
        self.invitations = invitations

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.invitations or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGroupTopInviter':
        user_id = reader.read_int64()
        invitations = reader.read_int32()
        return cls(user_id=user_id, invitations=invitations)


@register_tl
class StatsMegagroupStats(TLObject):
    ID: int = 0xef7ff916

    def __init__(self, period: Any = None, members: Any = None, messages: Any = None, viewers: Any = None, posters: Any = None, growth_graph: Any = None, members_graph: Any = None, new_members_by_source_graph: Any = None, languages_graph: Any = None, messages_graph: Any = None, actions_graph: Any = None, top_hours_graph: Any = None, weekdays_graph: Any = None, top_posters: Any = None, top_admins: Any = None, top_inviters: Any = None, users: Any = None) -> None:
        self.period = period
        self.members = members
        self.messages = messages
        self.viewers = viewers
        self.posters = posters
        self.growth_graph = growth_graph
        self.members_graph = members_graph
        self.new_members_by_source_graph = new_members_by_source_graph
        self.languages_graph = languages_graph
        self.messages_graph = messages_graph
        self.actions_graph = actions_graph
        self.top_hours_graph = top_hours_graph
        self.weekdays_graph = weekdays_graph
        self.top_posters = top_posters
        self.top_admins = top_admins
        self.top_inviters = top_inviters
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.period is not None and hasattr(self.period, 'write'): self.period.write(writer)
        if self.members is not None and hasattr(self.members, 'write'): self.members.write(writer)
        if self.messages is not None and hasattr(self.messages, 'write'): self.messages.write(writer)
        if self.viewers is not None and hasattr(self.viewers, 'write'): self.viewers.write(writer)
        if self.posters is not None and hasattr(self.posters, 'write'): self.posters.write(writer)
        if self.growth_graph is not None and hasattr(self.growth_graph, 'write'): self.growth_graph.write(writer)
        if self.members_graph is not None and hasattr(self.members_graph, 'write'): self.members_graph.write(writer)
        if self.new_members_by_source_graph is not None and hasattr(self.new_members_by_source_graph, 'write'): self.new_members_by_source_graph.write(writer)
        if self.languages_graph is not None and hasattr(self.languages_graph, 'write'): self.languages_graph.write(writer)
        if self.messages_graph is not None and hasattr(self.messages_graph, 'write'): self.messages_graph.write(writer)
        if self.actions_graph is not None and hasattr(self.actions_graph, 'write'): self.actions_graph.write(writer)
        if self.top_hours_graph is not None and hasattr(self.top_hours_graph, 'write'): self.top_hours_graph.write(writer)
        if self.weekdays_graph is not None and hasattr(self.weekdays_graph, 'write'): self.weekdays_graph.write(writer)
        writer.write_vector(self.top_posters or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.top_admins or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.top_inviters or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsMegagroupStats':
        period = reader.read_object()
        members = reader.read_object()
        messages = reader.read_object()
        viewers = reader.read_object()
        posters = reader.read_object()
        growth_graph = reader.read_object()
        members_graph = reader.read_object()
        new_members_by_source_graph = reader.read_object()
        languages_graph = reader.read_object()
        messages_graph = reader.read_object()
        actions_graph = reader.read_object()
        top_hours_graph = reader.read_object()
        weekdays_graph = reader.read_object()
        top_posters = reader.read_vector(lambda r: reader.read_object())
        top_admins = reader.read_vector(lambda r: reader.read_object())
        top_inviters = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(period=period, members=members, messages=messages, viewers=viewers, posters=posters, growth_graph=growth_graph, members_graph=members_graph, new_members_by_source_graph=new_members_by_source_graph, languages_graph=languages_graph, messages_graph=messages_graph, actions_graph=actions_graph, top_hours_graph=top_hours_graph, weekdays_graph=weekdays_graph, top_posters=top_posters, top_admins=top_admins, top_inviters=top_inviters, users=users)


@register_tl
class GlobalPrivacySettings(TLObject):
    ID: int = 0xfe41b34f

    def __init__(self, archive_and_mute_new_noncontact_peers: bool = False, keep_archived_unmuted: bool = False, keep_archived_folders: bool = False, hide_read_marks: bool = False, new_noncontact_peers_require_premium: bool = False, display_gifts_button: bool = False, noncontact_peers_paid_stars: Any = None, disallowed_gifts: Any = None) -> None:
        self.archive_and_mute_new_noncontact_peers = archive_and_mute_new_noncontact_peers
        self.keep_archived_unmuted = keep_archived_unmuted
        self.keep_archived_folders = keep_archived_folders
        self.hide_read_marks = hide_read_marks
        self.new_noncontact_peers_require_premium = new_noncontact_peers_require_premium
        self.display_gifts_button = display_gifts_button
        self.noncontact_peers_paid_stars = noncontact_peers_paid_stars
        self.disallowed_gifts = disallowed_gifts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.archive_and_mute_new_noncontact_peers:
            flags |= (1 << 0)
        if self.keep_archived_unmuted:
            flags |= (1 << 1)
        if self.keep_archived_folders:
            flags |= (1 << 2)
        if self.hide_read_marks:
            flags |= (1 << 3)
        if self.new_noncontact_peers_require_premium:
            flags |= (1 << 4)
        if self.display_gifts_button:
            flags |= (1 << 7)
        if self.noncontact_peers_paid_stars is not None:
            flags |= (1 << 5)
        if self.disallowed_gifts is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        if self.noncontact_peers_paid_stars is not None:
            writer.write_int64(self.noncontact_peers_paid_stars or 0)
        if self.disallowed_gifts is not None:
            if self.disallowed_gifts is not None and hasattr(self.disallowed_gifts, 'write'): self.disallowed_gifts.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'GlobalPrivacySettings':
        flags = reader.read_uint32()
        archive_and_mute_new_noncontact_peers = bool(flags & (1 << 0))
        keep_archived_unmuted = bool(flags & (1 << 1))
        keep_archived_folders = bool(flags & (1 << 2))
        hide_read_marks = bool(flags & (1 << 3))
        new_noncontact_peers_require_premium = bool(flags & (1 << 4))
        display_gifts_button = bool(flags & (1 << 7))
        noncontact_peers_paid_stars = reader.read_int64() if (flags & (1 << 5)) else None
        disallowed_gifts = reader.read_object() if (flags & (1 << 6)) else None
        return cls(archive_and_mute_new_noncontact_peers=archive_and_mute_new_noncontact_peers, keep_archived_unmuted=keep_archived_unmuted, keep_archived_folders=keep_archived_folders, hide_read_marks=hide_read_marks, new_noncontact_peers_require_premium=new_noncontact_peers_require_premium, display_gifts_button=display_gifts_button, noncontact_peers_paid_stars=noncontact_peers_paid_stars, disallowed_gifts=disallowed_gifts)


@register_tl
class HelpCountryCode(TLObject):
    ID: int = 0x4203c5ef

    def __init__(self, prefixes: Any = None, patterns: Any = None, country_code: Any = None) -> None:
        self.prefixes = prefixes
        self.patterns = patterns
        self.country_code = country_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.prefixes is not None:
            flags |= (1 << 0)
        if self.patterns is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.country_code or '')
        if self.prefixes is not None:
            writer.write_vector(self.prefixes or [], lambda w, x: w.write_string(x))
        if self.patterns is not None:
            writer.write_vector(self.patterns or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpCountryCode':
        flags = reader.read_uint32()
        country_code = reader.read_string()
        prefixes = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 0)) else None
        patterns = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 1)) else None
        return cls(country_code=country_code, prefixes=prefixes, patterns=patterns)


@register_tl
class HelpCountry(TLObject):
    ID: int = 0xc3878e23

    def __init__(self, hidden: bool = False, name: Any = None, iso2: Any = None, default_name: Any = None, country_codes: Any = None) -> None:
        self.hidden = hidden
        self.name = name
        self.iso2 = iso2
        self.default_name = default_name
        self.country_codes = country_codes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.hidden:
            flags |= (1 << 0)
        if self.name is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.iso2 or '')
        writer.write_string(self.default_name or '')
        if self.name is not None:
            writer.write_string(self.name or '')
        writer.write_vector(self.country_codes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpCountry':
        flags = reader.read_uint32()
        hidden = bool(flags & (1 << 0))
        iso2 = reader.read_string()
        default_name = reader.read_string()
        name = reader.read_string() if (flags & (1 << 1)) else None
        country_codes = reader.read_vector(lambda r: reader.read_object())
        return cls(hidden=hidden, iso2=iso2, default_name=default_name, name=name, country_codes=country_codes)


@register_tl
class HelpCountriesListNotModified(TLObject):
    ID: int = 0x93cc1f32

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpCountriesListNotModified':
        return cls()


@register_tl
class HelpCountriesList(TLObject):
    ID: int = 0x87d0759e

    def __init__(self, countries: Any = None, hash: Any = None) -> None:
        self.countries = countries
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.countries or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpCountriesList':
        countries = reader.read_vector(lambda r: reader.read_object())
        hash = reader.read_int32()
        return cls(countries=countries, hash=hash)


@register_tl
class MessageViews(TLObject):
    ID: int = 0x455b853d

    def __init__(self, views: Any = None, forwards: Any = None, replies: Any = None) -> None:
        self.views = views
        self.forwards = forwards
        self.replies = replies

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.views is not None:
            flags |= (1 << 0)
        if self.forwards is not None:
            flags |= (1 << 1)
        if self.replies is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.views is not None:
            writer.write_int32(self.views or 0)
        if self.forwards is not None:
            writer.write_int32(self.forwards or 0)
        if self.replies is not None:
            if self.replies is not None and hasattr(self.replies, 'write'): self.replies.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageViews':
        flags = reader.read_uint32()
        views = reader.read_int32() if (flags & (1 << 0)) else None
        forwards = reader.read_int32() if (flags & (1 << 1)) else None
        replies = reader.read_object() if (flags & (1 << 2)) else None
        return cls(views=views, forwards=forwards, replies=replies)


@register_tl
class MessagesMessageViews(TLObject):
    ID: int = 0xb6c4f543

    def __init__(self, views: Any = None, chats: Any = None, users: Any = None) -> None:
        self.views = views
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.views or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessageViews':
        views = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(views=views, chats=chats, users=users)


@register_tl
class MessagesDiscussionMessage(TLObject):
    ID: int = 0xa6341782

    def __init__(self, max_id: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, messages: Any = None, unread_count: Any = None, chats: Any = None, users: Any = None) -> None:
        self.max_id = max_id
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.messages = messages
        self.unread_count = unread_count
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.max_id is not None:
            flags |= (1 << 0)
        if self.read_inbox_max_id is not None:
            flags |= (1 << 1)
        if self.read_outbox_max_id is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.max_id is not None:
            writer.write_int32(self.max_id or 0)
        if self.read_inbox_max_id is not None:
            writer.write_int32(self.read_inbox_max_id or 0)
        if self.read_outbox_max_id is not None:
            writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDiscussionMessage':
        flags = reader.read_uint32()
        messages = reader.read_vector(lambda r: reader.read_object())
        max_id = reader.read_int32() if (flags & (1 << 0)) else None
        read_inbox_max_id = reader.read_int32() if (flags & (1 << 1)) else None
        read_outbox_max_id = reader.read_int32() if (flags & (1 << 2)) else None
        unread_count = reader.read_int32()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(messages=messages, max_id=max_id, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chats=chats, users=users)


@register_tl
class MessageReplyHeader(TLObject):
    ID: int = 0x1b97dd66

    def __init__(self, reply_to_scheduled: bool = False, forum_topic: bool = False, quote: bool = False, reply_to_ephemeral: bool = False, reply_to_msg_id: Any = None, reply_to_peer_id: Any = None, reply_from: Any = None, reply_media: Any = None, reply_to_top_id: Any = None, quote_text: Any = None, quote_entities: Any = None, quote_offset: Any = None, todo_item_id: Any = None, poll_option: Any = None) -> None:
        self.reply_to_scheduled = reply_to_scheduled
        self.forum_topic = forum_topic
        self.quote = quote
        self.reply_to_ephemeral = reply_to_ephemeral
        self.reply_to_msg_id = reply_to_msg_id
        self.reply_to_peer_id = reply_to_peer_id
        self.reply_from = reply_from
        self.reply_media = reply_media
        self.reply_to_top_id = reply_to_top_id
        self.quote_text = quote_text
        self.quote_entities = quote_entities
        self.quote_offset = quote_offset
        self.todo_item_id = todo_item_id
        self.poll_option = poll_option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_to_scheduled:
            flags |= (1 << 2)
        if self.forum_topic:
            flags |= (1 << 3)
        if self.quote:
            flags |= (1 << 9)
        if self.reply_to_ephemeral:
            flags |= (1 << 13)
        if self.reply_to_msg_id is not None:
            flags |= (1 << 4)
        if self.reply_to_peer_id is not None:
            flags |= (1 << 0)
        if self.reply_from is not None:
            flags |= (1 << 5)
        if self.reply_media is not None:
            flags |= (1 << 8)
        if self.reply_to_top_id is not None:
            flags |= (1 << 1)
        if self.quote_text is not None:
            flags |= (1 << 6)
        if self.quote_entities is not None:
            flags |= (1 << 7)
        if self.quote_offset is not None:
            flags |= (1 << 10)
        if self.todo_item_id is not None:
            flags |= (1 << 11)
        if self.poll_option is not None:
            flags |= (1 << 12)
        writer.write_uint32(flags)
        if self.reply_to_msg_id is not None:
            writer.write_int32(self.reply_to_msg_id or 0)
        if self.reply_to_peer_id is not None:
            if self.reply_to_peer_id is not None and hasattr(self.reply_to_peer_id, 'write'): self.reply_to_peer_id.write(writer)
        if self.reply_from is not None:
            if self.reply_from is not None and hasattr(self.reply_from, 'write'): self.reply_from.write(writer)
        if self.reply_media is not None:
            if self.reply_media is not None and hasattr(self.reply_media, 'write'): self.reply_media.write(writer)
        if self.reply_to_top_id is not None:
            writer.write_int32(self.reply_to_top_id or 0)
        if self.quote_text is not None:
            writer.write_string(self.quote_text or '')
        if self.quote_entities is not None:
            writer.write_vector(self.quote_entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.quote_offset is not None:
            writer.write_int32(self.quote_offset or 0)
        if self.todo_item_id is not None:
            writer.write_int32(self.todo_item_id or 0)
        if self.poll_option is not None:
            writer.write_bytes(self.poll_option or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageReplyHeader':
        flags = reader.read_uint32()
        reply_to_scheduled = bool(flags & (1 << 2))
        forum_topic = bool(flags & (1 << 3))
        quote = bool(flags & (1 << 9))
        reply_to_ephemeral = bool(flags & (1 << 13))
        reply_to_msg_id = reader.read_int32() if (flags & (1 << 4)) else None
        reply_to_peer_id = reader.read_object() if (flags & (1 << 0)) else None
        reply_from = reader.read_object() if (flags & (1 << 5)) else None
        reply_media = reader.read_object() if (flags & (1 << 8)) else None
        reply_to_top_id = reader.read_int32() if (flags & (1 << 1)) else None
        quote_text = reader.read_string() if (flags & (1 << 6)) else None
        quote_entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 7)) else None
        quote_offset = reader.read_int32() if (flags & (1 << 10)) else None
        todo_item_id = reader.read_int32() if (flags & (1 << 11)) else None
        poll_option = reader.read_bytes() if (flags & (1 << 12)) else None
        return cls(reply_to_scheduled=reply_to_scheduled, forum_topic=forum_topic, quote=quote, reply_to_ephemeral=reply_to_ephemeral, reply_to_msg_id=reply_to_msg_id, reply_to_peer_id=reply_to_peer_id, reply_from=reply_from, reply_media=reply_media, reply_to_top_id=reply_to_top_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset, todo_item_id=todo_item_id, poll_option=poll_option)


@register_tl
class MessageReplyStoryHeader(TLObject):
    ID: int = 0xe5af939

    def __init__(self, peer: Any = None, story_id: Any = None) -> None:
        self.peer = peer
        self.story_id = story_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.story_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageReplyStoryHeader':
        peer = reader.read_object()
        story_id = reader.read_int32()
        return cls(peer=peer, story_id=story_id)


@register_tl
class MessageReplies(TLObject):
    ID: int = 0x83d60fc2

    def __init__(self, comments: bool = False, recent_repliers: Any = None, channel_id: Any = None, max_id: Any = None, read_max_id: Any = None, replies: Any = None, replies_pts: Any = None) -> None:
        self.comments = comments
        self.recent_repliers = recent_repliers
        self.channel_id = channel_id
        self.max_id = max_id
        self.read_max_id = read_max_id
        self.replies = replies
        self.replies_pts = replies_pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.comments:
            flags |= (1 << 0)
        if self.recent_repliers is not None:
            flags |= (1 << 1)
        if self.channel_id is not None:
            flags |= (1 << 0)
        if self.max_id is not None:
            flags |= (1 << 2)
        if self.read_max_id is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int32(self.replies or 0)
        writer.write_int32(self.replies_pts or 0)
        if self.recent_repliers is not None:
            writer.write_vector(self.recent_repliers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.channel_id is not None:
            writer.write_int64(self.channel_id or 0)
        if self.max_id is not None:
            writer.write_int32(self.max_id or 0)
        if self.read_max_id is not None:
            writer.write_int32(self.read_max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageReplies':
        flags = reader.read_uint32()
        comments = bool(flags & (1 << 0))
        replies = reader.read_int32()
        replies_pts = reader.read_int32()
        recent_repliers = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        channel_id = reader.read_int64() if (flags & (1 << 0)) else None
        max_id = reader.read_int32() if (flags & (1 << 2)) else None
        read_max_id = reader.read_int32() if (flags & (1 << 3)) else None
        return cls(comments=comments, replies=replies, replies_pts=replies_pts, recent_repliers=recent_repliers, channel_id=channel_id, max_id=max_id, read_max_id=read_max_id)


@register_tl
class PeerBlocked(TLObject):
    ID: int = 0xe8fd8014

    def __init__(self, peer_id: Any = None, date: Any = None) -> None:
        self.peer_id = peer_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerBlocked':
        peer_id = reader.read_object()
        date = reader.read_int32()
        return cls(peer_id=peer_id, date=date)


@register_tl
class StatsMessageStats(TLObject):
    ID: int = 0x7fe91c14

    def __init__(self, views_graph: Any = None, reactions_by_emotion_graph: Any = None) -> None:
        self.views_graph = views_graph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.views_graph is not None and hasattr(self.views_graph, 'write'): self.views_graph.write(writer)
        if self.reactions_by_emotion_graph is not None and hasattr(self.reactions_by_emotion_graph, 'write'): self.reactions_by_emotion_graph.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsMessageStats':
        views_graph = reader.read_object()
        reactions_by_emotion_graph = reader.read_object()
        return cls(views_graph=views_graph, reactions_by_emotion_graph=reactions_by_emotion_graph)


@register_tl
class GroupCallDiscarded(TLObject):
    ID: int = 0x7780bcb4

    def __init__(self, id: Any = None, access_hash: Any = None, duration: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.duration = duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallDiscarded':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        duration = reader.read_int32()
        return cls(id=id, access_hash=access_hash, duration=duration)


@register_tl
class GroupCall(TLObject):
    ID: int = 0xefb2b617

    def __init__(self, join_muted: bool = False, can_change_join_muted: bool = False, join_date_asc: bool = False, schedule_start_subscribed: bool = False, can_start_video: bool = False, record_video_active: bool = False, rtmp_stream: bool = False, listeners_hidden: bool = False, conference: bool = False, creator: bool = False, messages_enabled: bool = False, can_change_messages_enabled: bool = False, min: bool = False, title: Any = None, stream_dc_id: Any = None, record_start_date: Any = None, schedule_date: Any = None, unmuted_video_count: Any = None, invite_link: Any = None, send_paid_messages_stars: Any = None, default_send_as: Any = None, id: Any = None, access_hash: Any = None, participants_count: Any = None, unmuted_video_limit: Any = None, version: Any = None) -> None:
        self.join_muted = join_muted
        self.can_change_join_muted = can_change_join_muted
        self.join_date_asc = join_date_asc
        self.schedule_start_subscribed = schedule_start_subscribed
        self.can_start_video = can_start_video
        self.record_video_active = record_video_active
        self.rtmp_stream = rtmp_stream
        self.listeners_hidden = listeners_hidden
        self.conference = conference
        self.creator = creator
        self.messages_enabled = messages_enabled
        self.can_change_messages_enabled = can_change_messages_enabled
        self.min = min
        self.title = title
        self.stream_dc_id = stream_dc_id
        self.record_start_date = record_start_date
        self.schedule_date = schedule_date
        self.unmuted_video_count = unmuted_video_count
        self.invite_link = invite_link
        self.send_paid_messages_stars = send_paid_messages_stars
        self.default_send_as = default_send_as
        self.id = id
        self.access_hash = access_hash
        self.participants_count = participants_count
        self.unmuted_video_limit = unmuted_video_limit
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.join_muted:
            flags |= (1 << 1)
        if self.can_change_join_muted:
            flags |= (1 << 2)
        if self.join_date_asc:
            flags |= (1 << 6)
        if self.schedule_start_subscribed:
            flags |= (1 << 8)
        if self.can_start_video:
            flags |= (1 << 9)
        if self.record_video_active:
            flags |= (1 << 11)
        if self.rtmp_stream:
            flags |= (1 << 12)
        if self.listeners_hidden:
            flags |= (1 << 13)
        if self.conference:
            flags |= (1 << 14)
        if self.creator:
            flags |= (1 << 15)
        if self.messages_enabled:
            flags |= (1 << 17)
        if self.can_change_messages_enabled:
            flags |= (1 << 18)
        if self.min:
            flags |= (1 << 19)
        if self.title is not None:
            flags |= (1 << 3)
        if self.stream_dc_id is not None:
            flags |= (1 << 4)
        if self.record_start_date is not None:
            flags |= (1 << 5)
        if self.schedule_date is not None:
            flags |= (1 << 7)
        if self.unmuted_video_count is not None:
            flags |= (1 << 10)
        if self.invite_link is not None:
            flags |= (1 << 16)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 20)
        if self.default_send_as is not None:
            flags |= (1 << 21)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.participants_count or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.stream_dc_id is not None:
            writer.write_int32(self.stream_dc_id or 0)
        if self.record_start_date is not None:
            writer.write_int32(self.record_start_date or 0)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.unmuted_video_count is not None:
            writer.write_int32(self.unmuted_video_count or 0)
        writer.write_int32(self.unmuted_video_limit or 0)
        writer.write_int32(self.version or 0)
        if self.invite_link is not None:
            writer.write_string(self.invite_link or '')
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.default_send_as is not None:
            if self.default_send_as is not None and hasattr(self.default_send_as, 'write'): self.default_send_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCall':
        flags = reader.read_uint32()
        join_muted = bool(flags & (1 << 1))
        can_change_join_muted = bool(flags & (1 << 2))
        join_date_asc = bool(flags & (1 << 6))
        schedule_start_subscribed = bool(flags & (1 << 8))
        can_start_video = bool(flags & (1 << 9))
        record_video_active = bool(flags & (1 << 11))
        rtmp_stream = bool(flags & (1 << 12))
        listeners_hidden = bool(flags & (1 << 13))
        conference = bool(flags & (1 << 14))
        creator = bool(flags & (1 << 15))
        messages_enabled = bool(flags & (1 << 17))
        can_change_messages_enabled = bool(flags & (1 << 18))
        min = bool(flags & (1 << 19))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        participants_count = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 3)) else None
        stream_dc_id = reader.read_int32() if (flags & (1 << 4)) else None
        record_start_date = reader.read_int32() if (flags & (1 << 5)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 7)) else None
        unmuted_video_count = reader.read_int32() if (flags & (1 << 10)) else None
        unmuted_video_limit = reader.read_int32()
        version = reader.read_int32()
        invite_link = reader.read_string() if (flags & (1 << 16)) else None
        send_paid_messages_stars = reader.read_int64() if (flags & (1 << 20)) else None
        default_send_as = reader.read_object() if (flags & (1 << 21)) else None
        return cls(join_muted=join_muted, can_change_join_muted=can_change_join_muted, join_date_asc=join_date_asc, schedule_start_subscribed=schedule_start_subscribed, can_start_video=can_start_video, record_video_active=record_video_active, rtmp_stream=rtmp_stream, listeners_hidden=listeners_hidden, conference=conference, creator=creator, messages_enabled=messages_enabled, can_change_messages_enabled=can_change_messages_enabled, min=min, id=id, access_hash=access_hash, participants_count=participants_count, title=title, stream_dc_id=stream_dc_id, record_start_date=record_start_date, schedule_date=schedule_date, unmuted_video_count=unmuted_video_count, unmuted_video_limit=unmuted_video_limit, version=version, invite_link=invite_link, send_paid_messages_stars=send_paid_messages_stars, default_send_as=default_send_as)


@register_tl
class InputGroupCall(TLObject):
    ID: int = 0xd8aa840f

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGroupCall':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputGroupCallSlug(TLObject):
    ID: int = 0xfe06823f

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGroupCallSlug':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class InputGroupCallInviteMessage(TLObject):
    ID: int = 0x8c10603f

    def __init__(self, msg_id: Any = None) -> None:
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGroupCallInviteMessage':
        msg_id = reader.read_int32()
        return cls(msg_id=msg_id)


@register_tl
class GroupCallParticipant(TLObject):
    ID: int = 0x2a3dc7ac

    def __init__(self, muted: bool = False, left: bool = False, can_self_unmute: bool = False, just_joined: bool = False, versioned: bool = False, min: bool = False, muted_by_you: bool = False, volume_by_admin: bool = False, self_: bool = False, video_joined: bool = False, active_date: Any = None, volume: Any = None, about: Any = None, raise_hand_rating: Any = None, video: Any = None, presentation: Any = None, paid_stars_total: Any = None, peer: Any = None, date: Any = None, source: Any = None) -> None:
        self.muted = muted
        self.left = left
        self.can_self_unmute = can_self_unmute
        self.just_joined = just_joined
        self.versioned = versioned
        self.min = min
        self.muted_by_you = muted_by_you
        self.volume_by_admin = volume_by_admin
        self.self_ = self_
        self.video_joined = video_joined
        self.active_date = active_date
        self.volume = volume
        self.about = about
        self.raise_hand_rating = raise_hand_rating
        self.video = video
        self.presentation = presentation
        self.paid_stars_total = paid_stars_total
        self.peer = peer
        self.date = date
        self.source = source

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.muted:
            flags |= (1 << 0)
        if self.left:
            flags |= (1 << 1)
        if self.can_self_unmute:
            flags |= (1 << 2)
        if self.just_joined:
            flags |= (1 << 4)
        if self.versioned:
            flags |= (1 << 5)
        if self.min:
            flags |= (1 << 8)
        if self.muted_by_you:
            flags |= (1 << 9)
        if self.volume_by_admin:
            flags |= (1 << 10)
        if self.self_:
            flags |= (1 << 12)
        if self.video_joined:
            flags |= (1 << 15)
        if self.active_date is not None:
            flags |= (1 << 3)
        if self.volume is not None:
            flags |= (1 << 7)
        if self.about is not None:
            flags |= (1 << 11)
        if self.raise_hand_rating is not None:
            flags |= (1 << 13)
        if self.video is not None:
            flags |= (1 << 6)
        if self.presentation is not None:
            flags |= (1 << 14)
        if self.paid_stars_total is not None:
            flags |= (1 << 16)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.date or 0)
        if self.active_date is not None:
            writer.write_int32(self.active_date or 0)
        writer.write_int32(self.source or 0)
        if self.volume is not None:
            writer.write_int32(self.volume or 0)
        if self.about is not None:
            writer.write_string(self.about or '')
        if self.raise_hand_rating is not None:
            writer.write_int64(self.raise_hand_rating or 0)
        if self.video is not None:
            if self.video is not None and hasattr(self.video, 'write'): self.video.write(writer)
        if self.presentation is not None:
            if self.presentation is not None and hasattr(self.presentation, 'write'): self.presentation.write(writer)
        if self.paid_stars_total is not None:
            writer.write_int64(self.paid_stars_total or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallParticipant':
        flags = reader.read_uint32()
        muted = bool(flags & (1 << 0))
        left = bool(flags & (1 << 1))
        can_self_unmute = bool(flags & (1 << 2))
        just_joined = bool(flags & (1 << 4))
        versioned = bool(flags & (1 << 5))
        min = bool(flags & (1 << 8))
        muted_by_you = bool(flags & (1 << 9))
        volume_by_admin = bool(flags & (1 << 10))
        self_ = bool(flags & (1 << 12))
        video_joined = bool(flags & (1 << 15))
        peer = reader.read_object()
        date = reader.read_int32()
        active_date = reader.read_int32() if (flags & (1 << 3)) else None
        source = reader.read_int32()
        volume = reader.read_int32() if (flags & (1 << 7)) else None
        about = reader.read_string() if (flags & (1 << 11)) else None
        raise_hand_rating = reader.read_int64() if (flags & (1 << 13)) else None
        video = reader.read_object() if (flags & (1 << 6)) else None
        presentation = reader.read_object() if (flags & (1 << 14)) else None
        paid_stars_total = reader.read_int64() if (flags & (1 << 16)) else None
        return cls(muted=muted, left=left, can_self_unmute=can_self_unmute, just_joined=just_joined, versioned=versioned, min=min, muted_by_you=muted_by_you, volume_by_admin=volume_by_admin, self_=self_, video_joined=video_joined, peer=peer, date=date, active_date=active_date, source=source, volume=volume, about=about, raise_hand_rating=raise_hand_rating, video=video, presentation=presentation, paid_stars_total=paid_stars_total)


@register_tl
class PhoneGroupCall(TLObject):
    ID: int = 0x9e727aad

    def __init__(self, call: Any = None, participants: Any = None, participants_next_offset: Any = None, chats: Any = None, users: Any = None) -> None:
        self.call = call
        self.participants = participants
        self.participants_next_offset = participants_next_offset
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_vector(self.participants or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.participants_next_offset or '')
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGroupCall':
        call = reader.read_object()
        participants = reader.read_vector(lambda r: reader.read_object())
        participants_next_offset = reader.read_string()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(call=call, participants=participants, participants_next_offset=participants_next_offset, chats=chats, users=users)


@register_tl
class PhoneGroupParticipants(TLObject):
    ID: int = 0xf47751b6

    def __init__(self, count: Any = None, participants: Any = None, next_offset: Any = None, chats: Any = None, users: Any = None, version: Any = None) -> None:
        self.count = count
        self.participants = participants
        self.next_offset = next_offset
        self.chats = chats
        self.users = users
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.participants or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.next_offset or '')
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGroupParticipants':
        count = reader.read_int32()
        participants = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        version = reader.read_int32()
        return cls(count=count, participants=participants, next_offset=next_offset, chats=chats, users=users, version=version)


@register_tl
class InlineQueryPeerTypeSameBotPM(TLObject):
    ID: int = 0x3081ed9d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineQueryPeerTypeSameBotPM':
        return cls()


@register_tl
class InlineQueryPeerTypePM(TLObject):
    ID: int = 0x833c0fac

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineQueryPeerTypePM':
        return cls()


@register_tl
class InlineQueryPeerTypeChat(TLObject):
    ID: int = 0xd766c50a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineQueryPeerTypeChat':
        return cls()


@register_tl
class InlineQueryPeerTypeMegagroup(TLObject):
    ID: int = 0x5ec4be43

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineQueryPeerTypeMegagroup':
        return cls()


@register_tl
class InlineQueryPeerTypeBroadcast(TLObject):
    ID: int = 0x6334ee9a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineQueryPeerTypeBroadcast':
        return cls()


@register_tl
class InlineQueryPeerTypeBotPM(TLObject):
    ID: int = 0xe3b2d0c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineQueryPeerTypeBotPM':
        return cls()


@register_tl
class MessagesHistoryImport(TLObject):
    ID: int = 0x1662af0b

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesHistoryImport':
        id = reader.read_int64()
        return cls(id=id)


@register_tl
class MessagesHistoryImportParsed(TLObject):
    ID: int = 0x5e0fb7b9

    def __init__(self, pm: bool = False, group: bool = False, title: Any = None) -> None:
        self.pm = pm
        self.group = group
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pm:
            flags |= (1 << 0)
        if self.group:
            flags |= (1 << 1)
        if self.title is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.title is not None:
            writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesHistoryImportParsed':
        flags = reader.read_uint32()
        pm = bool(flags & (1 << 0))
        group = bool(flags & (1 << 1))
        title = reader.read_string() if (flags & (1 << 2)) else None
        return cls(pm=pm, group=group, title=title)


@register_tl
class MessagesAffectedFoundMessages(TLObject):
    ID: int = 0xef8d3e6c

    def __init__(self, pts: Any = None, pts_count: Any = None, offset: Any = None, messages: Any = None) -> None:
        self.pts = pts
        self.pts_count = pts_count
        self.offset = offset
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        writer.write_int32(self.offset or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAffectedFoundMessages':
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        offset = reader.read_int32()
        messages = reader.read_vector(lambda r: r.read_int32())
        return cls(pts=pts, pts_count=pts_count, offset=offset, messages=messages)


@register_tl
class ChatInviteImporter(TLObject):
    ID: int = 0x8c5adfd9

    def __init__(self, requested: bool = False, via_chatlist: bool = False, about: Any = None, approved_by: Any = None, user_id: Any = None, date: Any = None) -> None:
        self.requested = requested
        self.via_chatlist = via_chatlist
        self.about = about
        self.approved_by = approved_by
        self.user_id = user_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.requested:
            flags |= (1 << 0)
        if self.via_chatlist:
            flags |= (1 << 3)
        if self.about is not None:
            flags |= (1 << 2)
        if self.approved_by is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.date or 0)
        if self.about is not None:
            writer.write_string(self.about or '')
        if self.approved_by is not None:
            writer.write_int64(self.approved_by or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatInviteImporter':
        flags = reader.read_uint32()
        requested = bool(flags & (1 << 0))
        via_chatlist = bool(flags & (1 << 3))
        user_id = reader.read_int64()
        date = reader.read_int32()
        about = reader.read_string() if (flags & (1 << 2)) else None
        approved_by = reader.read_int64() if (flags & (1 << 1)) else None
        return cls(requested=requested, via_chatlist=via_chatlist, user_id=user_id, date=date, about=about, approved_by=approved_by)


@register_tl
class MessagesExportedChatInvites(TLObject):
    ID: int = 0xbdc62dcc

    def __init__(self, count: Any = None, invites: Any = None, users: Any = None) -> None:
        self.count = count
        self.invites = invites
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.invites or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesExportedChatInvites':
        count = reader.read_int32()
        invites = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, invites=invites, users=users)


@register_tl
class MessagesExportedChatInvite(TLObject):
    ID: int = 0x1871be50

    def __init__(self, invite: Any = None, users: Any = None) -> None:
        self.invite = invite
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.invite is not None and hasattr(self.invite, 'write'): self.invite.write(writer)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesExportedChatInvite':
        invite = reader.read_object()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(invite=invite, users=users)


@register_tl
class MessagesExportedChatInviteReplaced(TLObject):
    ID: int = 0x222600ef

    def __init__(self, invite: Any = None, new_invite: Any = None, users: Any = None) -> None:
        self.invite = invite
        self.new_invite = new_invite
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.invite is not None and hasattr(self.invite, 'write'): self.invite.write(writer)
        if self.new_invite is not None and hasattr(self.new_invite, 'write'): self.new_invite.write(writer)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesExportedChatInviteReplaced':
        invite = reader.read_object()
        new_invite = reader.read_object()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(invite=invite, new_invite=new_invite, users=users)


@register_tl
class MessagesChatInviteImporters(TLObject):
    ID: int = 0x81b6b00a

    def __init__(self, count: Any = None, importers: Any = None, users: Any = None) -> None:
        self.count = count
        self.importers = importers
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.importers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatInviteImporters':
        count = reader.read_int32()
        importers = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, importers=importers, users=users)


@register_tl
class ChatAdminWithInvites(TLObject):
    ID: int = 0xf2ecef23

    def __init__(self, admin_id: Any = None, invites_count: Any = None, revoked_invites_count: Any = None) -> None:
        self.admin_id = admin_id
        self.invites_count = invites_count
        self.revoked_invites_count = revoked_invites_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.admin_id or 0)
        writer.write_int32(self.invites_count or 0)
        writer.write_int32(self.revoked_invites_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatAdminWithInvites':
        admin_id = reader.read_int64()
        invites_count = reader.read_int32()
        revoked_invites_count = reader.read_int32()
        return cls(admin_id=admin_id, invites_count=invites_count, revoked_invites_count=revoked_invites_count)


@register_tl
class MessagesChatAdminsWithInvites(TLObject):
    ID: int = 0xb69b72d7

    def __init__(self, admins: Any = None, users: Any = None) -> None:
        self.admins = admins
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.admins or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatAdminsWithInvites':
        admins = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(admins=admins, users=users)


@register_tl
class MessagesCheckedHistoryImportPeer(TLObject):
    ID: int = 0xa24de717

    def __init__(self, confirm_text: Any = None) -> None:
        self.confirm_text = confirm_text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.confirm_text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCheckedHistoryImportPeer':
        confirm_text = reader.read_string()
        return cls(confirm_text=confirm_text)


@register_tl
class PhoneJoinAsPeers(TLObject):
    ID: int = 0xafe5623f

    def __init__(self, peers: Any = None, chats: Any = None, users: Any = None) -> None:
        self.peers = peers
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneJoinAsPeers':
        peers = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(peers=peers, chats=chats, users=users)


@register_tl
class PhoneExportedGroupCallInvite(TLObject):
    ID: int = 0x204bd158

    def __init__(self, link: Any = None) -> None:
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.link or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneExportedGroupCallInvite':
        link = reader.read_string()
        return cls(link=link)


@register_tl
class GroupCallParticipantVideoSourceGroup(TLObject):
    ID: int = 0xdcb118b7

    def __init__(self, semantics: Any = None, sources: Any = None) -> None:
        self.semantics = semantics
        self.sources = sources

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.semantics or '')
        writer.write_vector(self.sources or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallParticipantVideoSourceGroup':
        semantics = reader.read_string()
        sources = reader.read_vector(lambda r: r.read_int32())
        return cls(semantics=semantics, sources=sources)


@register_tl
class GroupCallParticipantVideo(TLObject):
    ID: int = 0x67753ac8

    def __init__(self, paused: bool = False, audio_source: Any = None, endpoint: Any = None, source_groups: Any = None) -> None:
        self.paused = paused
        self.audio_source = audio_source
        self.endpoint = endpoint
        self.source_groups = source_groups

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.paused:
            flags |= (1 << 0)
        if self.audio_source is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.endpoint or '')
        writer.write_vector(self.source_groups or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.audio_source is not None:
            writer.write_int32(self.audio_source or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallParticipantVideo':
        flags = reader.read_uint32()
        paused = bool(flags & (1 << 0))
        endpoint = reader.read_string()
        source_groups = reader.read_vector(lambda r: reader.read_object())
        audio_source = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(paused=paused, endpoint=endpoint, source_groups=source_groups, audio_source=audio_source)


@register_tl
class StickersSuggestedShortName(TLObject):
    ID: int = 0x85fea03f

    def __init__(self, short_name: Any = None) -> None:
        self.short_name = short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.short_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersSuggestedShortName':
        short_name = reader.read_string()
        return cls(short_name=short_name)


@register_tl
class BotCommandScopeDefault(TLObject):
    ID: int = 0x2f6cb2ab

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommandScopeDefault':
        return cls()


@register_tl
class BotCommandScopeUsers(TLObject):
    ID: int = 0x3c4f04d8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommandScopeUsers':
        return cls()


@register_tl
class BotCommandScopeChats(TLObject):
    ID: int = 0x6fe1a881

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommandScopeChats':
        return cls()


@register_tl
class BotCommandScopeChatAdmins(TLObject):
    ID: int = 0xb9aa606a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommandScopeChatAdmins':
        return cls()


@register_tl
class BotCommandScopePeer(TLObject):
    ID: int = 0xdb9d897d

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommandScopePeer':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class BotCommandScopePeerAdmins(TLObject):
    ID: int = 0x3fd863d1

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommandScopePeerAdmins':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class BotCommandScopePeerUser(TLObject):
    ID: int = 0xa1321f3

    def __init__(self, peer: Any = None, user_id: Any = None) -> None:
        self.peer = peer
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommandScopePeerUser':
        peer = reader.read_object()
        user_id = reader.read_object()
        return cls(peer=peer, user_id=user_id)


@register_tl
class AccountResetPasswordFailedWait(TLObject):
    ID: int = 0xe3779861

    def __init__(self, retry_date: Any = None) -> None:
        self.retry_date = retry_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.retry_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetPasswordFailedWait':
        retry_date = reader.read_int32()
        return cls(retry_date=retry_date)


@register_tl
class AccountResetPasswordRequestedWait(TLObject):
    ID: int = 0xe9effc7d

    def __init__(self, until_date: Any = None) -> None:
        self.until_date = until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetPasswordRequestedWait':
        until_date = reader.read_int32()
        return cls(until_date=until_date)


@register_tl
class AccountResetPasswordOk(TLObject):
    ID: int = 0xe926d63e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetPasswordOk':
        return cls()


@register_tl
class ChatTheme(TLObject):
    ID: int = 0xc3dffc04

    def __init__(self, emoticon: Any = None) -> None:
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatTheme':
        emoticon = reader.read_string()
        return cls(emoticon=emoticon)


@register_tl
class ChatThemeUniqueGift(TLObject):
    ID: int = 0x3458f9c8

    def __init__(self, gift: Any = None, theme_settings: Any = None) -> None:
        self.gift = gift
        self.theme_settings = theme_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        writer.write_vector(self.theme_settings or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatThemeUniqueGift':
        gift = reader.read_object()
        theme_settings = reader.read_vector(lambda r: reader.read_object())
        return cls(gift=gift, theme_settings=theme_settings)


@register_tl
class AccountChatThemesNotModified(TLObject):
    ID: int = 0xe011e1c4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountChatThemesNotModified':
        return cls()


@register_tl
class AccountChatThemes(TLObject):
    ID: int = 0xbe098173

    def __init__(self, next_offset: Any = None, hash: Any = None, themes: Any = None, chats: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.hash = hash
        self.themes = themes
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.themes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountChatThemes':
        flags = reader.read_uint32()
        hash = reader.read_int64()
        themes = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        return cls(hash=hash, themes=themes, chats=chats, users=users, next_offset=next_offset)


@register_tl
class SponsoredMessage(TLObject):
    ID: int = 0x7dbf8673

    def __init__(self, recommended: bool = False, can_report: bool = False, entities: Any = None, photo: Any = None, media: Any = None, color: Any = None, sponsor_info: Any = None, additional_info: Any = None, min_display_duration: Any = None, max_display_duration: Any = None, random_id: Any = None, url: Any = None, title: Any = None, message: Any = None, button_text: Any = None) -> None:
        self.recommended = recommended
        self.can_report = can_report
        self.entities = entities
        self.photo = photo
        self.media = media
        self.color = color
        self.sponsor_info = sponsor_info
        self.additional_info = additional_info
        self.min_display_duration = min_display_duration
        self.max_display_duration = max_display_duration
        self.random_id = random_id
        self.url = url
        self.title = title
        self.message = message
        self.button_text = button_text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.recommended:
            flags |= (1 << 5)
        if self.can_report:
            flags |= (1 << 12)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.photo is not None:
            flags |= (1 << 6)
        if self.media is not None:
            flags |= (1 << 14)
        if self.color is not None:
            flags |= (1 << 13)
        if self.sponsor_info is not None:
            flags |= (1 << 7)
        if self.additional_info is not None:
            flags |= (1 << 8)
        if self.min_display_duration is not None:
            flags |= (1 << 15)
        if self.max_display_duration is not None:
            flags |= (1 << 15)
        writer.write_uint32(flags)
        writer.write_bytes(self.random_id or b'')
        writer.write_string(self.url or '')
        writer.write_string(self.title or '')
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.color is not None:
            if self.color is not None and hasattr(self.color, 'write'): self.color.write(writer)
        writer.write_string(self.button_text or '')
        if self.sponsor_info is not None:
            writer.write_string(self.sponsor_info or '')
        if self.additional_info is not None:
            writer.write_string(self.additional_info or '')
        if self.min_display_duration is not None:
            writer.write_int32(self.min_display_duration or 0)
        if self.max_display_duration is not None:
            writer.write_int32(self.max_display_duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SponsoredMessage':
        flags = reader.read_uint32()
        recommended = bool(flags & (1 << 5))
        can_report = bool(flags & (1 << 12))
        random_id = reader.read_bytes()
        url = reader.read_string()
        title = reader.read_string()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        photo = reader.read_object() if (flags & (1 << 6)) else None
        media = reader.read_object() if (flags & (1 << 14)) else None
        color = reader.read_object() if (flags & (1 << 13)) else None
        button_text = reader.read_string()
        sponsor_info = reader.read_string() if (flags & (1 << 7)) else None
        additional_info = reader.read_string() if (flags & (1 << 8)) else None
        min_display_duration = reader.read_int32() if (flags & (1 << 15)) else None
        max_display_duration = reader.read_int32() if (flags & (1 << 15)) else None
        return cls(recommended=recommended, can_report=can_report, random_id=random_id, url=url, title=title, message=message, entities=entities, photo=photo, media=media, color=color, button_text=button_text, sponsor_info=sponsor_info, additional_info=additional_info, min_display_duration=min_display_duration, max_display_duration=max_display_duration)


@register_tl
class MessagesSponsoredMessages(TLObject):
    ID: int = 0xffda656d

    def __init__(self, posts_between: Any = None, start_delay: Any = None, between_delay: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.posts_between = posts_between
        self.start_delay = start_delay
        self.between_delay = between_delay
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.posts_between is not None:
            flags |= (1 << 0)
        if self.start_delay is not None:
            flags |= (1 << 1)
        if self.between_delay is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.posts_between is not None:
            writer.write_int32(self.posts_between or 0)
        if self.start_delay is not None:
            writer.write_int32(self.start_delay or 0)
        if self.between_delay is not None:
            writer.write_int32(self.between_delay or 0)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSponsoredMessages':
        flags = reader.read_uint32()
        posts_between = reader.read_int32() if (flags & (1 << 0)) else None
        start_delay = reader.read_int32() if (flags & (1 << 1)) else None
        between_delay = reader.read_int32() if (flags & (1 << 2)) else None
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(posts_between=posts_between, start_delay=start_delay, between_delay=between_delay, messages=messages, chats=chats, users=users)


@register_tl
class MessagesSponsoredMessagesEmpty(TLObject):
    ID: int = 0x1839490f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSponsoredMessagesEmpty':
        return cls()


@register_tl
class SearchResultsCalendarPeriod(TLObject):
    ID: int = 0xc9b0539f

    def __init__(self, date: Any = None, min_msg_id: Any = None, max_msg_id: Any = None, count: Any = None) -> None:
        self.date = date
        self.min_msg_id = min_msg_id
        self.max_msg_id = max_msg_id
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.min_msg_id or 0)
        writer.write_int32(self.max_msg_id or 0)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SearchResultsCalendarPeriod':
        date = reader.read_int32()
        min_msg_id = reader.read_int32()
        max_msg_id = reader.read_int32()
        count = reader.read_int32()
        return cls(date=date, min_msg_id=min_msg_id, max_msg_id=max_msg_id, count=count)


@register_tl
class MessagesSearchResultsCalendar(TLObject):
    ID: int = 0x147ee23c

    def __init__(self, inexact: bool = False, offset_id_offset: Any = None, count: Any = None, min_date: Any = None, min_msg_id: Any = None, periods: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.inexact = inexact
        self.offset_id_offset = offset_id_offset
        self.count = count
        self.min_date = min_date
        self.min_msg_id = min_msg_id
        self.periods = periods
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inexact:
            flags |= (1 << 0)
        if self.offset_id_offset is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_int32(self.min_date or 0)
        writer.write_int32(self.min_msg_id or 0)
        if self.offset_id_offset is not None:
            writer.write_int32(self.offset_id_offset or 0)
        writer.write_vector(self.periods or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchResultsCalendar':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 0))
        count = reader.read_int32()
        min_date = reader.read_int32()
        min_msg_id = reader.read_int32()
        offset_id_offset = reader.read_int32() if (flags & (1 << 1)) else None
        periods = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(inexact=inexact, count=count, min_date=min_date, min_msg_id=min_msg_id, offset_id_offset=offset_id_offset, periods=periods, messages=messages, chats=chats, users=users)


@register_tl
class SearchResultPosition(TLObject):
    ID: int = 0x7f648b67

    def __init__(self, msg_id: Any = None, date: Any = None, offset: Any = None) -> None:
        self.msg_id = msg_id
        self.date = date
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.msg_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SearchResultPosition':
        msg_id = reader.read_int32()
        date = reader.read_int32()
        offset = reader.read_int32()
        return cls(msg_id=msg_id, date=date, offset=offset)


@register_tl
class MessagesSearchResultsPositions(TLObject):
    ID: int = 0x53b22baf

    def __init__(self, count: Any = None, positions: Any = None) -> None:
        self.count = count
        self.positions = positions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.positions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSearchResultsPositions':
        count = reader.read_int32()
        positions = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, positions=positions)


@register_tl
class ChannelsSendAsPeers(TLObject):
    ID: int = 0xf496b0c6

    def __init__(self, peers: Any = None, chats: Any = None, users: Any = None) -> None:
        self.peers = peers
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSendAsPeers':
        peers = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(peers=peers, chats=chats, users=users)


@register_tl
class UsersUserFull(TLObject):
    ID: int = 0x3b6d152e

    def __init__(self, full_user: Any = None, chats: Any = None, users: Any = None) -> None:
        self.full_user = full_user
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.full_user is not None and hasattr(self.full_user, 'write'): self.full_user.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersUserFull':
        full_user = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(full_user=full_user, chats=chats, users=users)


@register_tl
class MessagesPeerSettings(TLObject):
    ID: int = 0x6880b94d

    def __init__(self, settings: Any = None, chats: Any = None, users: Any = None) -> None:
        self.settings = settings
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesPeerSettings':
        settings = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(settings=settings, chats=chats, users=users)


@register_tl
class AuthLoggedOut(TLObject):
    ID: int = 0xc3a2835f

    def __init__(self, future_auth_token: Any = None) -> None:
        self.future_auth_token = future_auth_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.future_auth_token is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.future_auth_token is not None:
            writer.write_bytes(self.future_auth_token or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthLoggedOut':
        flags = reader.read_uint32()
        future_auth_token = reader.read_bytes() if (flags & (1 << 0)) else None
        return cls(future_auth_token=future_auth_token)


@register_tl
class ReactionCount(TLObject):
    ID: int = 0xa3d1cb80

    def __init__(self, chosen_order: Any = None, reaction: Any = None, count: Any = None) -> None:
        self.chosen_order = chosen_order
        self.reaction = reaction
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.chosen_order is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.chosen_order is not None:
            writer.write_int32(self.chosen_order or 0)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionCount':
        flags = reader.read_uint32()
        chosen_order = reader.read_int32() if (flags & (1 << 0)) else None
        reaction = reader.read_object()
        count = reader.read_int32()
        return cls(chosen_order=chosen_order, reaction=reaction, count=count)


@register_tl
class MessageReactions(TLObject):
    ID: int = 0xa339f0b

    def __init__(self, min: bool = False, can_see_list: bool = False, reactions_as_tags: bool = False, recent_reactions: Any = None, top_reactors: Any = None, results: Any = None) -> None:
        self.min = min
        self.can_see_list = can_see_list
        self.reactions_as_tags = reactions_as_tags
        self.recent_reactions = recent_reactions
        self.top_reactors = top_reactors
        self.results = results

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.min:
            flags |= (1 << 0)
        if self.can_see_list:
            flags |= (1 << 2)
        if self.reactions_as_tags:
            flags |= (1 << 3)
        if self.recent_reactions is not None:
            flags |= (1 << 1)
        if self.top_reactors is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_vector(self.results or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.recent_reactions is not None:
            writer.write_vector(self.recent_reactions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.top_reactors is not None:
            writer.write_vector(self.top_reactors or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageReactions':
        flags = reader.read_uint32()
        min = bool(flags & (1 << 0))
        can_see_list = bool(flags & (1 << 2))
        reactions_as_tags = bool(flags & (1 << 3))
        results = reader.read_vector(lambda r: reader.read_object())
        recent_reactions = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        top_reactors = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        return cls(min=min, can_see_list=can_see_list, reactions_as_tags=reactions_as_tags, results=results, recent_reactions=recent_reactions, top_reactors=top_reactors)


@register_tl
class MessagesMessageReactionsList(TLObject):
    ID: int = 0x31bd492d

    def __init__(self, next_offset: Any = None, count: Any = None, reactions: Any = None, chats: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.count = count
        self.reactions = reactions
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.reactions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessageReactionsList':
        flags = reader.read_uint32()
        count = reader.read_int32()
        reactions = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        return cls(count=count, reactions=reactions, chats=chats, users=users, next_offset=next_offset)


@register_tl
class AvailableReaction(TLObject):
    ID: int = 0xc077ec01

    def __init__(self, inactive: bool = False, premium: bool = False, around_animation: Any = None, center_icon: Any = None, reaction: Any = None, title: Any = None, static_icon: Any = None, appear_animation: Any = None, select_animation: Any = None, activate_animation: Any = None, effect_animation: Any = None) -> None:
        self.inactive = inactive
        self.premium = premium
        self.around_animation = around_animation
        self.center_icon = center_icon
        self.reaction = reaction
        self.title = title
        self.static_icon = static_icon
        self.appear_animation = appear_animation
        self.select_animation = select_animation
        self.activate_animation = activate_animation
        self.effect_animation = effect_animation

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inactive:
            flags |= (1 << 0)
        if self.premium:
            flags |= (1 << 2)
        if self.around_animation is not None:
            flags |= (1 << 1)
        if self.center_icon is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.reaction or '')
        writer.write_string(self.title or '')
        if self.static_icon is not None and hasattr(self.static_icon, 'write'): self.static_icon.write(writer)
        if self.appear_animation is not None and hasattr(self.appear_animation, 'write'): self.appear_animation.write(writer)
        if self.select_animation is not None and hasattr(self.select_animation, 'write'): self.select_animation.write(writer)
        if self.activate_animation is not None and hasattr(self.activate_animation, 'write'): self.activate_animation.write(writer)
        if self.effect_animation is not None and hasattr(self.effect_animation, 'write'): self.effect_animation.write(writer)
        if self.around_animation is not None:
            if self.around_animation is not None and hasattr(self.around_animation, 'write'): self.around_animation.write(writer)
        if self.center_icon is not None:
            if self.center_icon is not None and hasattr(self.center_icon, 'write'): self.center_icon.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AvailableReaction':
        flags = reader.read_uint32()
        inactive = bool(flags & (1 << 0))
        premium = bool(flags & (1 << 2))
        reaction = reader.read_string()
        title = reader.read_string()
        static_icon = reader.read_object()
        appear_animation = reader.read_object()
        select_animation = reader.read_object()
        activate_animation = reader.read_object()
        effect_animation = reader.read_object()
        around_animation = reader.read_object() if (flags & (1 << 1)) else None
        center_icon = reader.read_object() if (flags & (1 << 1)) else None
        return cls(inactive=inactive, premium=premium, reaction=reaction, title=title, static_icon=static_icon, appear_animation=appear_animation, select_animation=select_animation, activate_animation=activate_animation, effect_animation=effect_animation, around_animation=around_animation, center_icon=center_icon)


@register_tl
class MessagesAvailableReactionsNotModified(TLObject):
    ID: int = 0x9f071957

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAvailableReactionsNotModified':
        return cls()


@register_tl
class MessagesAvailableReactions(TLObject):
    ID: int = 0x768e3aad

    def __init__(self, hash: Any = None, reactions: Any = None) -> None:
        self.hash = hash
        self.reactions = reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)
        writer.write_vector(self.reactions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAvailableReactions':
        hash = reader.read_int32()
        reactions = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, reactions=reactions)

