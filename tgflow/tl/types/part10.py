from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class MessagePeerReaction(TLObject):
    ID: int = 0x8c79b63c

    def __init__(self, big: bool = False, unread: bool = False, my: bool = False, peer_id: Any = None, date: Any = None, reaction: Any = None) -> None:
        self.big = big
        self.unread = unread
        self.my = my
        self.peer_id = peer_id
        self.date = date
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.big:
            flags |= (1 << 0)
        if self.unread:
            flags |= (1 << 1)
        if self.my:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        writer.write_int32(self.date or 0)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagePeerReaction':
        flags = reader.read_uint32()
        big = bool(flags & (1 << 0))
        unread = bool(flags & (1 << 1))
        my = bool(flags & (1 << 2))
        peer_id = reader.read_object()
        date = reader.read_int32()
        reaction = reader.read_object()
        return cls(big=big, unread=unread, my=my, peer_id=peer_id, date=date, reaction=reaction)


@register_tl
class GroupCallStreamChannel(TLObject):
    ID: int = 0x80eb48af

    def __init__(self, channel: Any = None, scale: Any = None, last_timestamp_ms: Any = None) -> None:
        self.channel = channel
        self.scale = scale
        self.last_timestamp_ms = last_timestamp_ms

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.channel or 0)
        writer.write_int32(self.scale or 0)
        writer.write_int64(self.last_timestamp_ms or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallStreamChannel':
        channel = reader.read_int32()
        scale = reader.read_int32()
        last_timestamp_ms = reader.read_int64()
        return cls(channel=channel, scale=scale, last_timestamp_ms=last_timestamp_ms)


@register_tl
class PhoneGroupCallStreamChannels(TLObject):
    ID: int = 0xd0e482b2

    def __init__(self, channels: Any = None) -> None:
        self.channels = channels

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.channels or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGroupCallStreamChannels':
        channels = reader.read_vector(lambda r: reader.read_object())
        return cls(channels=channels)


@register_tl
class PhoneGroupCallStreamRtmpUrl(TLObject):
    ID: int = 0x2dbf3432

    def __init__(self, url: Any = None, key: Any = None) -> None:
        self.url = url
        self.key = key

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_string(self.key or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGroupCallStreamRtmpUrl':
        url = reader.read_string()
        key = reader.read_string()
        return cls(url=url, key=key)


@register_tl
class AttachMenuBotIconColor(TLObject):
    ID: int = 0x4576f3f0

    def __init__(self, name: Any = None, color: Any = None) -> None:
        self.name = name
        self.color = color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.name or '')
        writer.write_int32(self.color or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuBotIconColor':
        name = reader.read_string()
        color = reader.read_int32()
        return cls(name=name, color=color)


@register_tl
class AttachMenuBotIcon(TLObject):
    ID: int = 0xb2a7386b

    def __init__(self, colors: Any = None, name: Any = None, icon: Any = None) -> None:
        self.colors = colors
        self.name = name
        self.icon = icon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.colors is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.name or '')
        if self.icon is not None and hasattr(self.icon, 'write'): self.icon.write(writer)
        if self.colors is not None:
            writer.write_vector(self.colors or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuBotIcon':
        flags = reader.read_uint32()
        name = reader.read_string()
        icon = reader.read_object()
        colors = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        return cls(name=name, icon=icon, colors=colors)


@register_tl
class AttachMenuBot(TLObject):
    ID: int = 0xd90d8dfe

    def __init__(self, inactive: bool = False, has_settings: bool = False, request_write_access: bool = False, show_in_attach_menu: bool = False, show_in_side_menu: bool = False, side_menu_disclaimer_needed: bool = False, peer_types: Any = None, bot_id: Any = None, short_name: Any = None, icons: Any = None) -> None:
        self.inactive = inactive
        self.has_settings = has_settings
        self.request_write_access = request_write_access
        self.show_in_attach_menu = show_in_attach_menu
        self.show_in_side_menu = show_in_side_menu
        self.side_menu_disclaimer_needed = side_menu_disclaimer_needed
        self.peer_types = peer_types
        self.bot_id = bot_id
        self.short_name = short_name
        self.icons = icons

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inactive:
            flags |= (1 << 0)
        if self.has_settings:
            flags |= (1 << 1)
        if self.request_write_access:
            flags |= (1 << 2)
        if self.show_in_attach_menu:
            flags |= (1 << 3)
        if self.show_in_side_menu:
            flags |= (1 << 4)
        if self.side_menu_disclaimer_needed:
            flags |= (1 << 5)
        if self.peer_types is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int64(self.bot_id or 0)
        writer.write_string(self.short_name or '')
        if self.peer_types is not None:
            writer.write_vector(self.peer_types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.icons or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuBot':
        flags = reader.read_uint32()
        inactive = bool(flags & (1 << 0))
        has_settings = bool(flags & (1 << 1))
        request_write_access = bool(flags & (1 << 2))
        show_in_attach_menu = bool(flags & (1 << 3))
        show_in_side_menu = bool(flags & (1 << 4))
        side_menu_disclaimer_needed = bool(flags & (1 << 5))
        bot_id = reader.read_int64()
        short_name = reader.read_string()
        peer_types = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        icons = reader.read_vector(lambda r: reader.read_object())
        return cls(inactive=inactive, has_settings=has_settings, request_write_access=request_write_access, show_in_attach_menu=show_in_attach_menu, show_in_side_menu=show_in_side_menu, side_menu_disclaimer_needed=side_menu_disclaimer_needed, bot_id=bot_id, short_name=short_name, peer_types=peer_types, icons=icons)


@register_tl
class AttachMenuBotsNotModified(TLObject):
    ID: int = 0xf1d88a5c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuBotsNotModified':
        return cls()


@register_tl
class AttachMenuBots(TLObject):
    ID: int = 0x3c4301c0

    def __init__(self, hash: Any = None, bots: Any = None, users: Any = None) -> None:
        self.hash = hash
        self.bots = bots
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.bots or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuBots':
        hash = reader.read_int64()
        bots = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, bots=bots, users=users)


@register_tl
class AttachMenuBotsBot(TLObject):
    ID: int = 0x93bf667f

    def __init__(self, bot: Any = None, users: Any = None) -> None:
        self.bot = bot
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuBotsBot':
        bot = reader.read_object()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(bot=bot, users=users)


@register_tl
class WebViewResultUrl(TLObject):
    ID: int = 0x4d22ff98

    def __init__(self, fullsize: bool = False, fullscreen: bool = False, query_id: Any = None, url: Any = None) -> None:
        self.fullsize = fullsize
        self.fullscreen = fullscreen
        self.query_id = query_id
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.fullsize:
            flags |= (1 << 1)
        if self.fullscreen:
            flags |= (1 << 2)
        if self.query_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.query_id is not None:
            writer.write_int64(self.query_id or 0)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'WebViewResultUrl':
        flags = reader.read_uint32()
        fullsize = bool(flags & (1 << 1))
        fullscreen = bool(flags & (1 << 2))
        query_id = reader.read_int64() if (flags & (1 << 0)) else None
        url = reader.read_string()
        return cls(fullsize=fullsize, fullscreen=fullscreen, query_id=query_id, url=url)


@register_tl
class WebViewMessageSent(TLObject):
    ID: int = 0xc94511c

    def __init__(self, msg_id: Any = None) -> None:
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.msg_id is not None:
            if self.msg_id is not None and hasattr(self.msg_id, 'write'): self.msg_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebViewMessageSent':
        flags = reader.read_uint32()
        msg_id = reader.read_object() if (flags & (1 << 0)) else None
        return cls(msg_id=msg_id)


@register_tl
class BotMenuButtonDefault(TLObject):
    ID: int = 0x7533a588

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotMenuButtonDefault':
        return cls()


@register_tl
class BotMenuButtonCommands(TLObject):
    ID: int = 0x4258c205

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotMenuButtonCommands':
        return cls()


@register_tl
class BotMenuButton(TLObject):
    ID: int = 0xc7b57ce6

    def __init__(self, text: Any = None, url: Any = None) -> None:
        self.text = text
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotMenuButton':
        text = reader.read_string()
        url = reader.read_string()
        return cls(text=text, url=url)


@register_tl
class AccountSavedRingtonesNotModified(TLObject):
    ID: int = 0xfbf6e8b1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSavedRingtonesNotModified':
        return cls()


@register_tl
class AccountSavedRingtones(TLObject):
    ID: int = 0xc1e92cc5

    def __init__(self, hash: Any = None, ringtones: Any = None) -> None:
        self.hash = hash
        self.ringtones = ringtones

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.ringtones or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSavedRingtones':
        hash = reader.read_int64()
        ringtones = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, ringtones=ringtones)


@register_tl
class NotificationSoundDefault(TLObject):
    ID: int = 0x97e8bebe

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'NotificationSoundDefault':
        return cls()


@register_tl
class NotificationSoundNone(TLObject):
    ID: int = 0x6f0c34df

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'NotificationSoundNone':
        return cls()


@register_tl
class NotificationSoundLocal(TLObject):
    ID: int = 0x830b9ae4

    def __init__(self, title: Any = None, data: Any = None) -> None:
        self.title = title
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_string(self.data or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'NotificationSoundLocal':
        title = reader.read_string()
        data = reader.read_string()
        return cls(title=title, data=data)


@register_tl
class NotificationSoundRingtone(TLObject):
    ID: int = 0xff6c8049

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'NotificationSoundRingtone':
        id = reader.read_int64()
        return cls(id=id)


@register_tl
class AccountSavedRingtone(TLObject):
    ID: int = 0xb7263f6d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSavedRingtone':
        return cls()


@register_tl
class AccountSavedRingtoneConverted(TLObject):
    ID: int = 0x1f307eb7

    def __init__(self, document: Any = None) -> None:
        self.document = document

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSavedRingtoneConverted':
        document = reader.read_object()
        return cls(document=document)


@register_tl
class AttachMenuPeerTypeSameBotPM(TLObject):
    ID: int = 0x7d6be90e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuPeerTypeSameBotPM':
        return cls()


@register_tl
class AttachMenuPeerTypeBotPM(TLObject):
    ID: int = 0xc32bfa1a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuPeerTypeBotPM':
        return cls()


@register_tl
class AttachMenuPeerTypePM(TLObject):
    ID: int = 0xf146d31f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuPeerTypePM':
        return cls()


@register_tl
class AttachMenuPeerTypeChat(TLObject):
    ID: int = 0x509113f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuPeerTypeChat':
        return cls()


@register_tl
class AttachMenuPeerTypeBroadcast(TLObject):
    ID: int = 0x7bfbdefc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AttachMenuPeerTypeBroadcast':
        return cls()


@register_tl
class InputInvoiceMessage(TLObject):
    ID: int = 0xc5b56859

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceMessage':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class InputInvoiceSlug(TLObject):
    ID: int = 0xc326caef

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceSlug':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class InputInvoicePremiumGiftCode(TLObject):
    ID: int = 0x98986c0d

    def __init__(self, purpose: Any = None, option: Any = None) -> None:
        self.purpose = purpose
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)
        if self.option is not None and hasattr(self.option, 'write'): self.option.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoicePremiumGiftCode':
        purpose = reader.read_object()
        option = reader.read_object()
        return cls(purpose=purpose, option=option)


@register_tl
class InputInvoiceStars(TLObject):
    ID: int = 0x65f00ce3

    def __init__(self, purpose: Any = None) -> None:
        self.purpose = purpose

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStars':
        purpose = reader.read_object()
        return cls(purpose=purpose)


@register_tl
class InputInvoiceChatInviteSubscription(TLObject):
    ID: int = 0x34e793f1

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceChatInviteSubscription':
        hash = reader.read_string()
        return cls(hash=hash)


@register_tl
class InputInvoiceStarGift(TLObject):
    ID: int = 0xe8625e92

    def __init__(self, hide_name: bool = False, include_upgrade: bool = False, message: Any = None, peer: Any = None, gift_id: Any = None) -> None:
        self.hide_name = hide_name
        self.include_upgrade = include_upgrade
        self.message = message
        self.peer = peer
        self.gift_id = gift_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.hide_name:
            flags |= (1 << 0)
        if self.include_upgrade:
            flags |= (1 << 2)
        if self.message is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.gift_id or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStarGift':
        flags = reader.read_uint32()
        hide_name = bool(flags & (1 << 0))
        include_upgrade = bool(flags & (1 << 2))
        peer = reader.read_object()
        gift_id = reader.read_int64()
        message = reader.read_object() if (flags & (1 << 1)) else None
        return cls(hide_name=hide_name, include_upgrade=include_upgrade, peer=peer, gift_id=gift_id, message=message)


@register_tl
class InputInvoiceStarGiftUpgrade(TLObject):
    ID: int = 0x4d818d5d

    def __init__(self, keep_original_details: bool = False, stargift: Any = None) -> None:
        self.keep_original_details = keep_original_details
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.keep_original_details:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStarGiftUpgrade':
        flags = reader.read_uint32()
        keep_original_details = bool(flags & (1 << 0))
        stargift = reader.read_object()
        return cls(keep_original_details=keep_original_details, stargift=stargift)


@register_tl
class InputInvoiceStarGiftTransfer(TLObject):
    ID: int = 0x4a5f5bd9

    def __init__(self, stargift: Any = None, to_id: Any = None) -> None:
        self.stargift = stargift
        self.to_id = to_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)
        if self.to_id is not None and hasattr(self.to_id, 'write'): self.to_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStarGiftTransfer':
        stargift = reader.read_object()
        to_id = reader.read_object()
        return cls(stargift=stargift, to_id=to_id)


@register_tl
class InputInvoicePremiumGiftStars(TLObject):
    ID: int = 0xdabab2ef

    def __init__(self, message: Any = None, user_id: Any = None, months: Any = None) -> None:
        self.message = message
        self.user_id = user_id
        self.months = months

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.message is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.months or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoicePremiumGiftStars':
        flags = reader.read_uint32()
        user_id = reader.read_object()
        months = reader.read_int32()
        message = reader.read_object() if (flags & (1 << 0)) else None
        return cls(user_id=user_id, months=months, message=message)


@register_tl
class InputInvoiceBusinessBotTransferStars(TLObject):
    ID: int = 0xf4997e42

    def __init__(self, bot: Any = None, stars: Any = None) -> None:
        self.bot = bot
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceBusinessBotTransferStars':
        bot = reader.read_object()
        stars = reader.read_int64()
        return cls(bot=bot, stars=stars)


@register_tl
class InputInvoiceStarGiftResale(TLObject):
    ID: int = 0xc39f5324

    def __init__(self, ton: bool = False, slug: Any = None, to_id: Any = None) -> None:
        self.ton = ton
        self.slug = slug
        self.to_id = to_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ton:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.slug or '')
        if self.to_id is not None and hasattr(self.to_id, 'write'): self.to_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStarGiftResale':
        flags = reader.read_uint32()
        ton = bool(flags & (1 << 0))
        slug = reader.read_string()
        to_id = reader.read_object()
        return cls(ton=ton, slug=slug, to_id=to_id)


@register_tl
class InputInvoiceStarGiftPrepaidUpgrade(TLObject):
    ID: int = 0x9a0b48b8

    def __init__(self, peer: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStarGiftPrepaidUpgrade':
        peer = reader.read_object()
        hash = reader.read_string()
        return cls(peer=peer, hash=hash)


@register_tl
class InputInvoicePremiumAuthCode(TLObject):
    ID: int = 0x3e77f614

    def __init__(self, purpose: Any = None) -> None:
        self.purpose = purpose

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoicePremiumAuthCode':
        purpose = reader.read_object()
        return cls(purpose=purpose)


@register_tl
class InputInvoiceStarGiftDropOriginalDetails(TLObject):
    ID: int = 0x923d8d1

    def __init__(self, stargift: Any = None) -> None:
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStarGiftDropOriginalDetails':
        stargift = reader.read_object()
        return cls(stargift=stargift)


@register_tl
class InputInvoiceStarGiftAuctionBid(TLObject):
    ID: int = 0x1ecafa10

    def __init__(self, hide_name: bool = False, update_bid: bool = False, peer: Any = None, message: Any = None, gift_id: Any = None, bid_amount: Any = None) -> None:
        self.hide_name = hide_name
        self.update_bid = update_bid
        self.peer = peer
        self.message = message
        self.gift_id = gift_id
        self.bid_amount = bid_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.hide_name:
            flags |= (1 << 0)
        if self.update_bid:
            flags |= (1 << 2)
        if self.peer is not None:
            flags |= (1 << 3)
        if self.message is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.gift_id or 0)
        writer.write_int64(self.bid_amount or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputInvoiceStarGiftAuctionBid':
        flags = reader.read_uint32()
        hide_name = bool(flags & (1 << 0))
        update_bid = bool(flags & (1 << 2))
        peer = reader.read_object() if (flags & (1 << 3)) else None
        gift_id = reader.read_int64()
        bid_amount = reader.read_int64()
        message = reader.read_object() if (flags & (1 << 1)) else None
        return cls(hide_name=hide_name, update_bid=update_bid, peer=peer, gift_id=gift_id, bid_amount=bid_amount, message=message)


@register_tl
class PaymentsExportedInvoice(TLObject):
    ID: int = 0xaed0cbd9

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsExportedInvoice':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class MessagesTranscribedAudio(TLObject):
    ID: int = 0xcfb9d957

    def __init__(self, pending: bool = False, trial_remains_num: Any = None, trial_remains_until_date: Any = None, transcription_id: Any = None, text: Any = None) -> None:
        self.pending = pending
        self.trial_remains_num = trial_remains_num
        self.trial_remains_until_date = trial_remains_until_date
        self.transcription_id = transcription_id
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pending:
            flags |= (1 << 0)
        if self.trial_remains_num is not None:
            flags |= (1 << 1)
        if self.trial_remains_until_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.transcription_id or 0)
        writer.write_string(self.text or '')
        if self.trial_remains_num is not None:
            writer.write_int32(self.trial_remains_num or 0)
        if self.trial_remains_until_date is not None:
            writer.write_int32(self.trial_remains_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesTranscribedAudio':
        flags = reader.read_uint32()
        pending = bool(flags & (1 << 0))
        transcription_id = reader.read_int64()
        text = reader.read_string()
        trial_remains_num = reader.read_int32() if (flags & (1 << 1)) else None
        trial_remains_until_date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(pending=pending, transcription_id=transcription_id, text=text, trial_remains_num=trial_remains_num, trial_remains_until_date=trial_remains_until_date)


@register_tl
class HelpPremiumPromo(TLObject):
    ID: int = 0x5334759c

    def __init__(self, status_text: Any = None, status_entities: Any = None, video_sections: Any = None, videos: Any = None, period_options: Any = None, users: Any = None) -> None:
        self.status_text = status_text
        self.status_entities = status_entities
        self.video_sections = video_sections
        self.videos = videos
        self.period_options = period_options
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.status_text or '')
        writer.write_vector(self.status_entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.video_sections or [], lambda w, x: w.write_string(x))
        writer.write_vector(self.videos or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.period_options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPremiumPromo':
        status_text = reader.read_string()
        status_entities = reader.read_vector(lambda r: reader.read_object())
        video_sections = reader.read_vector(lambda r: r.read_string())
        videos = reader.read_vector(lambda r: reader.read_object())
        period_options = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(status_text=status_text, status_entities=status_entities, video_sections=video_sections, videos=videos, period_options=period_options, users=users)


@register_tl
class InputStorePaymentPremiumSubscription(TLObject):
    ID: int = 0xa6751e66

    def __init__(self, restore: bool = False, upgrade: bool = False) -> None:
        self.restore = restore
        self.upgrade = upgrade

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.restore:
            flags |= (1 << 0)
        if self.upgrade:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentPremiumSubscription':
        flags = reader.read_uint32()
        restore = bool(flags & (1 << 0))
        upgrade = bool(flags & (1 << 1))
        return cls(restore=restore, upgrade=upgrade)


@register_tl
class InputStorePaymentGiftPremium(TLObject):
    ID: int = 0x616f7fe8

    def __init__(self, user_id: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.user_id = user_id
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentGiftPremium':
        user_id = reader.read_object()
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(user_id=user_id, currency=currency, amount=amount)


@register_tl
class InputStorePaymentPremiumGiftCode(TLObject):
    ID: int = 0xfb790393

    def __init__(self, boost_peer: Any = None, message: Any = None, users: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.boost_peer = boost_peer
        self.message = message
        self.users = users
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.boost_peer is not None:
            flags |= (1 << 0)
        if self.message is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.boost_peer is not None:
            if self.boost_peer is not None and hasattr(self.boost_peer, 'write'): self.boost_peer.write(writer)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentPremiumGiftCode':
        flags = reader.read_uint32()
        users = reader.read_vector(lambda r: reader.read_object())
        boost_peer = reader.read_object() if (flags & (1 << 0)) else None
        currency = reader.read_string()
        amount = reader.read_int64()
        message = reader.read_object() if (flags & (1 << 1)) else None
        return cls(users=users, boost_peer=boost_peer, currency=currency, amount=amount, message=message)


@register_tl
class InputStorePaymentPremiumGiveaway(TLObject):
    ID: int = 0x160544ca

    def __init__(self, only_new_subscribers: bool = False, winners_are_visible: bool = False, additional_peers: Any = None, countries_iso2: Any = None, prize_description: Any = None, boost_peer: Any = None, random_id: Any = None, until_date: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.winners_are_visible = winners_are_visible
        self.additional_peers = additional_peers
        self.countries_iso2 = countries_iso2
        self.prize_description = prize_description
        self.boost_peer = boost_peer
        self.random_id = random_id
        self.until_date = until_date
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.only_new_subscribers:
            flags |= (1 << 0)
        if self.winners_are_visible:
            flags |= (1 << 3)
        if self.additional_peers is not None:
            flags |= (1 << 1)
        if self.countries_iso2 is not None:
            flags |= (1 << 2)
        if self.prize_description is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.boost_peer is not None and hasattr(self.boost_peer, 'write'): self.boost_peer.write(writer)
        if self.additional_peers is not None:
            writer.write_vector(self.additional_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.countries_iso2 is not None:
            writer.write_vector(self.countries_iso2 or [], lambda w, x: w.write_string(x))
        if self.prize_description is not None:
            writer.write_string(self.prize_description or '')
        writer.write_int64(self.random_id or 0)
        writer.write_int32(self.until_date or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentPremiumGiveaway':
        flags = reader.read_uint32()
        only_new_subscribers = bool(flags & (1 << 0))
        winners_are_visible = bool(flags & (1 << 3))
        boost_peer = reader.read_object()
        additional_peers = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        countries_iso2 = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 2)) else None
        prize_description = reader.read_string() if (flags & (1 << 4)) else None
        random_id = reader.read_int64()
        until_date = reader.read_int32()
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, boost_peer=boost_peer, additional_peers=additional_peers, countries_iso2=countries_iso2, prize_description=prize_description, random_id=random_id, until_date=until_date, currency=currency, amount=amount)


@register_tl
class InputStorePaymentStarsTopup(TLObject):
    ID: int = 0xf9a2a6cb

    def __init__(self, spend_purpose_peer: Any = None, stars: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.spend_purpose_peer = spend_purpose_peer
        self.stars = stars
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spend_purpose_peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        if self.spend_purpose_peer is not None:
            if self.spend_purpose_peer is not None and hasattr(self.spend_purpose_peer, 'write'): self.spend_purpose_peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentStarsTopup':
        flags = reader.read_uint32()
        stars = reader.read_int64()
        currency = reader.read_string()
        amount = reader.read_int64()
        spend_purpose_peer = reader.read_object() if (flags & (1 << 0)) else None
        return cls(stars=stars, currency=currency, amount=amount, spend_purpose_peer=spend_purpose_peer)


@register_tl
class InputStorePaymentStarsGift(TLObject):
    ID: int = 0x1d741ef7

    def __init__(self, user_id: Any = None, stars: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.user_id = user_id
        self.stars = stars
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int64(self.stars or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentStarsGift':
        user_id = reader.read_object()
        stars = reader.read_int64()
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(user_id=user_id, stars=stars, currency=currency, amount=amount)


@register_tl
class InputStorePaymentStarsGiveaway(TLObject):
    ID: int = 0x751f08fa

    def __init__(self, only_new_subscribers: bool = False, winners_are_visible: bool = False, additional_peers: Any = None, countries_iso2: Any = None, prize_description: Any = None, stars: Any = None, boost_peer: Any = None, random_id: Any = None, until_date: Any = None, currency: Any = None, amount: Any = None, users: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.winners_are_visible = winners_are_visible
        self.additional_peers = additional_peers
        self.countries_iso2 = countries_iso2
        self.prize_description = prize_description
        self.stars = stars
        self.boost_peer = boost_peer
        self.random_id = random_id
        self.until_date = until_date
        self.currency = currency
        self.amount = amount
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.only_new_subscribers:
            flags |= (1 << 0)
        if self.winners_are_visible:
            flags |= (1 << 3)
        if self.additional_peers is not None:
            flags |= (1 << 1)
        if self.countries_iso2 is not None:
            flags |= (1 << 2)
        if self.prize_description is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)
        if self.boost_peer is not None and hasattr(self.boost_peer, 'write'): self.boost_peer.write(writer)
        if self.additional_peers is not None:
            writer.write_vector(self.additional_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.countries_iso2 is not None:
            writer.write_vector(self.countries_iso2 or [], lambda w, x: w.write_string(x))
        if self.prize_description is not None:
            writer.write_string(self.prize_description or '')
        writer.write_int64(self.random_id or 0)
        writer.write_int32(self.until_date or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        writer.write_int32(self.users or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentStarsGiveaway':
        flags = reader.read_uint32()
        only_new_subscribers = bool(flags & (1 << 0))
        winners_are_visible = bool(flags & (1 << 3))
        stars = reader.read_int64()
        boost_peer = reader.read_object()
        additional_peers = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        countries_iso2 = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 2)) else None
        prize_description = reader.read_string() if (flags & (1 << 4)) else None
        random_id = reader.read_int64()
        until_date = reader.read_int32()
        currency = reader.read_string()
        amount = reader.read_int64()
        users = reader.read_int32()
        return cls(only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, stars=stars, boost_peer=boost_peer, additional_peers=additional_peers, countries_iso2=countries_iso2, prize_description=prize_description, random_id=random_id, until_date=until_date, currency=currency, amount=amount, users=users)


@register_tl
class InputStorePaymentAuthCode(TLObject):
    ID: int = 0x3fc18057

    def __init__(self, restore: bool = False, phone_number: Any = None, phone_code_hash: Any = None, premium_days: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.restore = restore
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.premium_days = premium_days
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.restore:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        writer.write_int32(self.premium_days or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStorePaymentAuthCode':
        flags = reader.read_uint32()
        restore = bool(flags & (1 << 0))
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        premium_days = reader.read_int32()
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(restore=restore, phone_number=phone_number, phone_code_hash=phone_code_hash, premium_days=premium_days, currency=currency, amount=amount)


@register_tl
class PaymentFormMethod(TLObject):
    ID: int = 0x88f8f21b

    def __init__(self, url: Any = None, title: Any = None) -> None:
        self.url = url
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentFormMethod':
        url = reader.read_string()
        title = reader.read_string()
        return cls(url=url, title=title)


@register_tl
class EmojiStatusEmpty(TLObject):
    ID: int = 0x2de11aae

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiStatusEmpty':
        return cls()


@register_tl
class EmojiStatus(TLObject):
    ID: int = 0xe7ff068a

    def __init__(self, until: Any = None, document_id: Any = None) -> None:
        self.until = until
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.until is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.document_id or 0)
        if self.until is not None:
            writer.write_int32(self.until or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiStatus':
        flags = reader.read_uint32()
        document_id = reader.read_int64()
        until = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(document_id=document_id, until=until)


@register_tl
class EmojiStatusCollectible(TLObject):
    ID: int = 0x7184603b

    def __init__(self, until: Any = None, collectible_id: Any = None, document_id: Any = None, title: Any = None, slug: Any = None, pattern_document_id: Any = None, center_color: Any = None, edge_color: Any = None, pattern_color: Any = None, text_color: Any = None) -> None:
        self.until = until
        self.collectible_id = collectible_id
        self.document_id = document_id
        self.title = title
        self.slug = slug
        self.pattern_document_id = pattern_document_id
        self.center_color = center_color
        self.edge_color = edge_color
        self.pattern_color = pattern_color
        self.text_color = text_color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.until is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.collectible_id or 0)
        writer.write_int64(self.document_id or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.slug or '')
        writer.write_int64(self.pattern_document_id or 0)
        writer.write_int32(self.center_color or 0)
        writer.write_int32(self.edge_color or 0)
        writer.write_int32(self.pattern_color or 0)
        writer.write_int32(self.text_color or 0)
        if self.until is not None:
            writer.write_int32(self.until or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiStatusCollectible':
        flags = reader.read_uint32()
        collectible_id = reader.read_int64()
        document_id = reader.read_int64()
        title = reader.read_string()
        slug = reader.read_string()
        pattern_document_id = reader.read_int64()
        center_color = reader.read_int32()
        edge_color = reader.read_int32()
        pattern_color = reader.read_int32()
        text_color = reader.read_int32()
        until = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(collectible_id=collectible_id, document_id=document_id, title=title, slug=slug, pattern_document_id=pattern_document_id, center_color=center_color, edge_color=edge_color, pattern_color=pattern_color, text_color=text_color, until=until)


@register_tl
class InputEmojiStatusCollectible(TLObject):
    ID: int = 0x7141dbf

    def __init__(self, until: Any = None, collectible_id: Any = None) -> None:
        self.until = until
        self.collectible_id = collectible_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.until is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.collectible_id or 0)
        if self.until is not None:
            writer.write_int32(self.until or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputEmojiStatusCollectible':
        flags = reader.read_uint32()
        collectible_id = reader.read_int64()
        until = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(collectible_id=collectible_id, until=until)


@register_tl
class AccountEmojiStatusesNotModified(TLObject):
    ID: int = 0xd08ce645

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountEmojiStatusesNotModified':
        return cls()


@register_tl
class AccountEmojiStatuses(TLObject):
    ID: int = 0x90c467d1

    def __init__(self, hash: Any = None, statuses: Any = None) -> None:
        self.hash = hash
        self.statuses = statuses

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.statuses or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountEmojiStatuses':
        hash = reader.read_int64()
        statuses = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, statuses=statuses)


@register_tl
class ReactionEmpty(TLObject):
    ID: int = 0x79f5d419

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionEmpty':
        return cls()


@register_tl
class ReactionEmoji(TLObject):
    ID: int = 0x1b2286b8

    def __init__(self, emoticon: Any = None) -> None:
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionEmoji':
        emoticon = reader.read_string()
        return cls(emoticon=emoticon)


@register_tl
class ReactionCustomEmoji(TLObject):
    ID: int = 0x8935fc73

    def __init__(self, document_id: Any = None) -> None:
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.document_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionCustomEmoji':
        document_id = reader.read_int64()
        return cls(document_id=document_id)


@register_tl
class ReactionPaid(TLObject):
    ID: int = 0x523da4eb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionPaid':
        return cls()


@register_tl
class ChatReactionsNone(TLObject):
    ID: int = 0xeafc32bc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatReactionsNone':
        return cls()


@register_tl
class ChatReactionsAll(TLObject):
    ID: int = 0x52928bca

    def __init__(self, allow_custom: bool = False) -> None:
        self.allow_custom = allow_custom

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.allow_custom:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatReactionsAll':
        flags = reader.read_uint32()
        allow_custom = bool(flags & (1 << 0))
        return cls(allow_custom=allow_custom)


@register_tl
class ChatReactionsSome(TLObject):
    ID: int = 0x661d4037

    def __init__(self, reactions: Any = None) -> None:
        self.reactions = reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.reactions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatReactionsSome':
        reactions = reader.read_vector(lambda r: reader.read_object())
        return cls(reactions=reactions)


@register_tl
class MessagesReactionsNotModified(TLObject):
    ID: int = 0xb06fdbdf

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReactionsNotModified':
        return cls()


@register_tl
class MessagesReactions(TLObject):
    ID: int = 0xeafdf716

    def __init__(self, hash: Any = None, reactions: Any = None) -> None:
        self.hash = hash
        self.reactions = reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.reactions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReactions':
        hash = reader.read_int64()
        reactions = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, reactions=reactions)


@register_tl
class EmailVerifyPurposeLoginSetup(TLObject):
    ID: int = 0x4345be73

    def __init__(self, phone_number: Any = None, phone_code_hash: Any = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'EmailVerifyPurposeLoginSetup':
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash)


@register_tl
class EmailVerifyPurposeLoginChange(TLObject):
    ID: int = 0x527d22eb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmailVerifyPurposeLoginChange':
        return cls()


@register_tl
class EmailVerifyPurposePassport(TLObject):
    ID: int = 0xbbf51685

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmailVerifyPurposePassport':
        return cls()


@register_tl
class EmailVerificationCode(TLObject):
    ID: int = 0x922e55a9

    def __init__(self, code: Any = None) -> None:
        self.code = code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'EmailVerificationCode':
        code = reader.read_string()
        return cls(code=code)


@register_tl
class EmailVerificationGoogle(TLObject):
    ID: int = 0xdb909ec2

    def __init__(self, token: Any = None) -> None:
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'EmailVerificationGoogle':
        token = reader.read_string()
        return cls(token=token)


@register_tl
class EmailVerificationApple(TLObject):
    ID: int = 0x96d074fd

    def __init__(self, token: Any = None) -> None:
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'EmailVerificationApple':
        token = reader.read_string()
        return cls(token=token)


@register_tl
class AccountEmailVerified(TLObject):
    ID: int = 0x2b96cd1b

    def __init__(self, email: Any = None) -> None:
        self.email = email

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.email or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountEmailVerified':
        email = reader.read_string()
        return cls(email=email)


@register_tl
class AccountEmailVerifiedLogin(TLObject):
    ID: int = 0xe1bb0d61

    def __init__(self, email: Any = None, sent_code: Any = None) -> None:
        self.email = email
        self.sent_code = sent_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.email or '')
        if self.sent_code is not None and hasattr(self.sent_code, 'write'): self.sent_code.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountEmailVerifiedLogin':
        email = reader.read_string()
        sent_code = reader.read_object()
        return cls(email=email, sent_code=sent_code)


@register_tl
class PremiumSubscriptionOption(TLObject):
    ID: int = 0x5f2d1df2

    def __init__(self, current: bool = False, can_purchase_upgrade: bool = False, transaction: Any = None, store_product: Any = None, months: Any = None, currency: Any = None, amount: Any = None, bot_url: Any = None) -> None:
        self.current = current
        self.can_purchase_upgrade = can_purchase_upgrade
        self.transaction = transaction
        self.store_product = store_product
        self.months = months
        self.currency = currency
        self.amount = amount
        self.bot_url = bot_url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.current:
            flags |= (1 << 1)
        if self.can_purchase_upgrade:
            flags |= (1 << 2)
        if self.transaction is not None:
            flags |= (1 << 3)
        if self.store_product is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.transaction is not None:
            writer.write_string(self.transaction or '')
        writer.write_int32(self.months or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        writer.write_string(self.bot_url or '')
        if self.store_product is not None:
            writer.write_string(self.store_product or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumSubscriptionOption':
        flags = reader.read_uint32()
        current = bool(flags & (1 << 1))
        can_purchase_upgrade = bool(flags & (1 << 2))
        transaction = reader.read_string() if (flags & (1 << 3)) else None
        months = reader.read_int32()
        currency = reader.read_string()
        amount = reader.read_int64()
        bot_url = reader.read_string()
        store_product = reader.read_string() if (flags & (1 << 0)) else None
        return cls(current=current, can_purchase_upgrade=can_purchase_upgrade, transaction=transaction, months=months, currency=currency, amount=amount, bot_url=bot_url, store_product=store_product)


@register_tl
class SendAsPeer(TLObject):
    ID: int = 0xb81c7034

    def __init__(self, premium_required: bool = False, peer: Any = None) -> None:
        self.premium_required = premium_required
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.premium_required:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendAsPeer':
        flags = reader.read_uint32()
        premium_required = bool(flags & (1 << 0))
        peer = reader.read_object()
        return cls(premium_required=premium_required, peer=peer)


@register_tl
class MessageExtendedMediaPreview(TLObject):
    ID: int = 0xad628cc8

    def __init__(self, w: Any = None, h: Any = None, thumb: Any = None, video_duration: Any = None) -> None:
        self.w = w
        self.h = h
        self.thumb = thumb
        self.video_duration = video_duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.w is not None:
            flags |= (1 << 0)
        if self.h is not None:
            flags |= (1 << 0)
        if self.thumb is not None:
            flags |= (1 << 1)
        if self.video_duration is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.w is not None:
            writer.write_int32(self.w or 0)
        if self.h is not None:
            writer.write_int32(self.h or 0)
        if self.thumb is not None:
            if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        if self.video_duration is not None:
            writer.write_int32(self.video_duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageExtendedMediaPreview':
        flags = reader.read_uint32()
        w = reader.read_int32() if (flags & (1 << 0)) else None
        h = reader.read_int32() if (flags & (1 << 0)) else None
        thumb = reader.read_object() if (flags & (1 << 1)) else None
        video_duration = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(w=w, h=h, thumb=thumb, video_duration=video_duration)


@register_tl
class MessageExtendedMedia(TLObject):
    ID: int = 0xee479c64

    def __init__(self, media: Any = None) -> None:
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageExtendedMedia':
        media = reader.read_object()
        return cls(media=media)


@register_tl
class StickerKeyword(TLObject):
    ID: int = 0xfcfeb29c

    def __init__(self, document_id: Any = None, keyword: Any = None) -> None:
        self.document_id = document_id
        self.keyword = keyword

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.document_id or 0)
        writer.write_vector(self.keyword or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StickerKeyword':
        document_id = reader.read_int64()
        keyword = reader.read_vector(lambda r: r.read_string())
        return cls(document_id=document_id, keyword=keyword)


@register_tl
class Username(TLObject):
    ID: int = 0xb4073647

    def __init__(self, editable: bool = False, active: bool = False, username: Any = None) -> None:
        self.editable = editable
        self.active = active
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.editable:
            flags |= (1 << 0)
        if self.active:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'Username':
        flags = reader.read_uint32()
        editable = bool(flags & (1 << 0))
        active = bool(flags & (1 << 1))
        username = reader.read_string()
        return cls(editable=editable, active=active, username=username)


@register_tl
class ForumTopicDeleted(TLObject):
    ID: int = 0x23f109b

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ForumTopicDeleted':
        id = reader.read_int32()
        return cls(id=id)


@register_tl
class ForumTopic(TLObject):
    ID: int = 0xfcdad815

    def __init__(self, my: bool = False, closed: bool = False, pinned: bool = False, short: bool = False, hidden: bool = False, title_missing: bool = False, icon_emoji_id: Any = None, draft: Any = None, id: Any = None, date: Any = None, peer: Any = None, title: Any = None, icon_color: Any = None, top_message: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, unread_mentions_count: Any = None, unread_reactions_count: Any = None, unread_poll_votes_count: Any = None, from_id: Any = None, notify_settings: Any = None) -> None:
        self.my = my
        self.closed = closed
        self.pinned = pinned
        self.short = short
        self.hidden = hidden
        self.title_missing = title_missing
        self.icon_emoji_id = icon_emoji_id
        self.draft = draft
        self.id = id
        self.date = date
        self.peer = peer
        self.title = title
        self.icon_color = icon_color
        self.top_message = top_message
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_reactions_count = unread_reactions_count
        self.unread_poll_votes_count = unread_poll_votes_count
        self.from_id = from_id
        self.notify_settings = notify_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.my:
            flags |= (1 << 1)
        if self.closed:
            flags |= (1 << 2)
        if self.pinned:
            flags |= (1 << 3)
        if self.short:
            flags |= (1 << 5)
        if self.hidden:
            flags |= (1 << 6)
        if self.title_missing:
            flags |= (1 << 7)
        if self.icon_emoji_id is not None:
            flags |= (1 << 0)
        if self.draft is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.date or 0)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.title or '')
        writer.write_int32(self.icon_color or 0)
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.read_inbox_max_id or 0)
        writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        writer.write_int32(self.unread_mentions_count or 0)
        writer.write_int32(self.unread_reactions_count or 0)
        writer.write_int32(self.unread_poll_votes_count or 0)
        if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.notify_settings is not None and hasattr(self.notify_settings, 'write'): self.notify_settings.write(writer)
        if self.draft is not None:
            if self.draft is not None and hasattr(self.draft, 'write'): self.draft.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ForumTopic':
        flags = reader.read_uint32()
        my = bool(flags & (1 << 1))
        closed = bool(flags & (1 << 2))
        pinned = bool(flags & (1 << 3))
        short = bool(flags & (1 << 5))
        hidden = bool(flags & (1 << 6))
        title_missing = bool(flags & (1 << 7))
        id = reader.read_int32()
        date = reader.read_int32()
        peer = reader.read_object()
        title = reader.read_string()
        icon_color = reader.read_int32()
        icon_emoji_id = reader.read_int64() if (flags & (1 << 0)) else None
        top_message = reader.read_int32()
        read_inbox_max_id = reader.read_int32()
        read_outbox_max_id = reader.read_int32()
        unread_count = reader.read_int32()
        unread_mentions_count = reader.read_int32()
        unread_reactions_count = reader.read_int32()
        unread_poll_votes_count = reader.read_int32()
        from_id = reader.read_object()
        notify_settings = reader.read_object()
        draft = reader.read_object() if (flags & (1 << 4)) else None
        return cls(my=my, closed=closed, pinned=pinned, short=short, hidden=hidden, title_missing=title_missing, id=id, date=date, peer=peer, title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, unread_poll_votes_count=unread_poll_votes_count, from_id=from_id, notify_settings=notify_settings, draft=draft)


@register_tl
class MessagesForumTopics(TLObject):
    ID: int = 0x367617d3

    def __init__(self, order_by_create_date: bool = False, count: Any = None, topics: Any = None, messages: Any = None, chats: Any = None, users: Any = None, pts: Any = None) -> None:
        self.order_by_create_date = order_by_create_date
        self.count = count
        self.topics = topics
        self.messages = messages
        self.chats = chats
        self.users = users
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.order_by_create_date:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.topics or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesForumTopics':
        flags = reader.read_uint32()
        order_by_create_date = bool(flags & (1 << 0))
        count = reader.read_int32()
        topics = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        pts = reader.read_int32()
        return cls(order_by_create_date=order_by_create_date, count=count, topics=topics, messages=messages, chats=chats, users=users, pts=pts)


@register_tl
class DefaultHistoryTTL(TLObject):
    ID: int = 0x43b46b20

    def __init__(self, period: Any = None) -> None:
        self.period = period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DefaultHistoryTTL':
        period = reader.read_int32()
        return cls(period=period)


@register_tl
class ExportedContactToken(TLObject):
    ID: int = 0x41bf109b

    def __init__(self, url: Any = None, expires: Any = None) -> None:
        self.url = url
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int32(self.expires or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ExportedContactToken':
        url = reader.read_string()
        expires = reader.read_int32()
        return cls(url=url, expires=expires)


@register_tl
class RequestPeerTypeUser(TLObject):
    ID: int = 0x5f3b8a00

    def __init__(self, bot: Any = None, premium: Any = None) -> None:
        self.bot = bot
        self.premium = premium

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.bot is not None:
            flags |= (1 << 0)
        if self.premium is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.bot is not None:
            writer.write_bool(bool(self.bot))
        if self.premium is not None:
            writer.write_bool(bool(self.premium))

    @classmethod
    def read(cls, reader: TLReader) -> 'RequestPeerTypeUser':
        flags = reader.read_uint32()
        bot = reader.read_bool() if (flags & (1 << 0)) else None
        premium = reader.read_bool() if (flags & (1 << 1)) else None
        return cls(bot=bot, premium=premium)


@register_tl
class RequestPeerTypeChat(TLObject):
    ID: int = 0xc9f06e1b

    def __init__(self, creator: bool = False, bot_participant: bool = False, has_username: Any = None, forum: Any = None, user_admin_rights: Any = None, bot_admin_rights: Any = None) -> None:
        self.creator = creator
        self.bot_participant = bot_participant
        self.has_username = has_username
        self.forum = forum
        self.user_admin_rights = user_admin_rights
        self.bot_admin_rights = bot_admin_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.creator:
            flags |= (1 << 0)
        if self.bot_participant:
            flags |= (1 << 5)
        if self.has_username is not None:
            flags |= (1 << 3)
        if self.forum is not None:
            flags |= (1 << 4)
        if self.user_admin_rights is not None:
            flags |= (1 << 1)
        if self.bot_admin_rights is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.has_username is not None:
            writer.write_bool(bool(self.has_username))
        if self.forum is not None:
            writer.write_bool(bool(self.forum))
        if self.user_admin_rights is not None:
            if self.user_admin_rights is not None and hasattr(self.user_admin_rights, 'write'): self.user_admin_rights.write(writer)
        if self.bot_admin_rights is not None:
            if self.bot_admin_rights is not None and hasattr(self.bot_admin_rights, 'write'): self.bot_admin_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequestPeerTypeChat':
        flags = reader.read_uint32()
        creator = bool(flags & (1 << 0))
        bot_participant = bool(flags & (1 << 5))
        has_username = reader.read_bool() if (flags & (1 << 3)) else None
        forum = reader.read_bool() if (flags & (1 << 4)) else None
        user_admin_rights = reader.read_object() if (flags & (1 << 1)) else None
        bot_admin_rights = reader.read_object() if (flags & (1 << 2)) else None
        return cls(creator=creator, bot_participant=bot_participant, has_username=has_username, forum=forum, user_admin_rights=user_admin_rights, bot_admin_rights=bot_admin_rights)


@register_tl
class RequestPeerTypeBroadcast(TLObject):
    ID: int = 0x339bef6c

    def __init__(self, creator: bool = False, has_username: Any = None, user_admin_rights: Any = None, bot_admin_rights: Any = None) -> None:
        self.creator = creator
        self.has_username = has_username
        self.user_admin_rights = user_admin_rights
        self.bot_admin_rights = bot_admin_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.creator:
            flags |= (1 << 0)
        if self.has_username is not None:
            flags |= (1 << 3)
        if self.user_admin_rights is not None:
            flags |= (1 << 1)
        if self.bot_admin_rights is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.has_username is not None:
            writer.write_bool(bool(self.has_username))
        if self.user_admin_rights is not None:
            if self.user_admin_rights is not None and hasattr(self.user_admin_rights, 'write'): self.user_admin_rights.write(writer)
        if self.bot_admin_rights is not None:
            if self.bot_admin_rights is not None and hasattr(self.bot_admin_rights, 'write'): self.bot_admin_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequestPeerTypeBroadcast':
        flags = reader.read_uint32()
        creator = bool(flags & (1 << 0))
        has_username = reader.read_bool() if (flags & (1 << 3)) else None
        user_admin_rights = reader.read_object() if (flags & (1 << 1)) else None
        bot_admin_rights = reader.read_object() if (flags & (1 << 2)) else None
        return cls(creator=creator, has_username=has_username, user_admin_rights=user_admin_rights, bot_admin_rights=bot_admin_rights)


@register_tl
class RequestPeerTypeCreateBot(TLObject):
    ID: int = 0x3e81e078

    def __init__(self, bot_managed: bool = False, suggested_name: Any = None, suggested_username: Any = None) -> None:
        self.bot_managed = bot_managed
        self.suggested_name = suggested_name
        self.suggested_username = suggested_username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.bot_managed:
            flags |= (1 << 0)
        if self.suggested_name is not None:
            flags |= (1 << 1)
        if self.suggested_username is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.suggested_name is not None:
            writer.write_string(self.suggested_name or '')
        if self.suggested_username is not None:
            writer.write_string(self.suggested_username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'RequestPeerTypeCreateBot':
        flags = reader.read_uint32()
        bot_managed = bool(flags & (1 << 0))
        suggested_name = reader.read_string() if (flags & (1 << 1)) else None
        suggested_username = reader.read_string() if (flags & (1 << 2)) else None
        return cls(bot_managed=bot_managed, suggested_name=suggested_name, suggested_username=suggested_username)


@register_tl
class EmojiListNotModified(TLObject):
    ID: int = 0x481eadfa

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiListNotModified':
        return cls()


@register_tl
class EmojiList(TLObject):
    ID: int = 0x7a1e11d1

    def __init__(self, hash: Any = None, document_id: Any = None) -> None:
        self.hash = hash
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.document_id or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiList':
        hash = reader.read_int64()
        document_id = reader.read_vector(lambda r: r.read_int64())
        return cls(hash=hash, document_id=document_id)


@register_tl
class EmojiGroup(TLObject):
    ID: int = 0x7a9abda9

    def __init__(self, title: Any = None, icon_emoji_id: Any = None, emoticons: Any = None) -> None:
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.emoticons = emoticons

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_int64(self.icon_emoji_id or 0)
        writer.write_vector(self.emoticons or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiGroup':
        title = reader.read_string()
        icon_emoji_id = reader.read_int64()
        emoticons = reader.read_vector(lambda r: r.read_string())
        return cls(title=title, icon_emoji_id=icon_emoji_id, emoticons=emoticons)


@register_tl
class EmojiGroupGreeting(TLObject):
    ID: int = 0x80d26cc7

    def __init__(self, title: Any = None, icon_emoji_id: Any = None, emoticons: Any = None) -> None:
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.emoticons = emoticons

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_int64(self.icon_emoji_id or 0)
        writer.write_vector(self.emoticons or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiGroupGreeting':
        title = reader.read_string()
        icon_emoji_id = reader.read_int64()
        emoticons = reader.read_vector(lambda r: r.read_string())
        return cls(title=title, icon_emoji_id=icon_emoji_id, emoticons=emoticons)


@register_tl
class EmojiGroupPremium(TLObject):
    ID: int = 0x93bcf34

    def __init__(self, title: Any = None, icon_emoji_id: Any = None) -> None:
        self.title = title
        self.icon_emoji_id = icon_emoji_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_int64(self.icon_emoji_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EmojiGroupPremium':
        title = reader.read_string()
        icon_emoji_id = reader.read_int64()
        return cls(title=title, icon_emoji_id=icon_emoji_id)


@register_tl
class MessagesEmojiGroupsNotModified(TLObject):
    ID: int = 0x6fb4ad87

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEmojiGroupsNotModified':
        return cls()


@register_tl
class MessagesEmojiGroups(TLObject):
    ID: int = 0x881fb94b

    def __init__(self, hash: Any = None, groups: Any = None) -> None:
        self.hash = hash
        self.groups = groups

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)
        writer.write_vector(self.groups or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEmojiGroups':
        hash = reader.read_int32()
        groups = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, groups=groups)


@register_tl
class TextWithEntities(TLObject):
    ID: int = 0x751f3146

    def __init__(self, text: Any = None, entities: Any = None) -> None:
        self.text = text
        self.entities = entities

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextWithEntities':
        text = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object())
        return cls(text=text, entities=entities)


@register_tl
class MessagesTranslateResult(TLObject):
    ID: int = 0x33db32f8

    def __init__(self, result: Any = None) -> None:
        self.result = result

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.result or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesTranslateResult':
        result = reader.read_vector(lambda r: reader.read_object())
        return cls(result=result)


@register_tl
class AutoSaveSettings(TLObject):
    ID: int = 0xc84834ce

    def __init__(self, photos: bool = False, videos: bool = False, video_max_size: Any = None) -> None:
        self.photos = photos
        self.videos = videos
        self.video_max_size = video_max_size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.photos:
            flags |= (1 << 0)
        if self.videos:
            flags |= (1 << 1)
        if self.video_max_size is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.video_max_size is not None:
            writer.write_int64(self.video_max_size or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AutoSaveSettings':
        flags = reader.read_uint32()
        photos = bool(flags & (1 << 0))
        videos = bool(flags & (1 << 1))
        video_max_size = reader.read_int64() if (flags & (1 << 2)) else None
        return cls(photos=photos, videos=videos, video_max_size=video_max_size)


@register_tl
class AutoSaveException(TLObject):
    ID: int = 0x81602d47

    def __init__(self, peer: Any = None, settings: Any = None) -> None:
        self.peer = peer
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AutoSaveException':
        peer = reader.read_object()
        settings = reader.read_object()
        return cls(peer=peer, settings=settings)


@register_tl
class AccountAutoSaveSettings(TLObject):
    ID: int = 0x4c3e069d

    def __init__(self, users_settings: Any = None, chats_settings: Any = None, broadcasts_settings: Any = None, exceptions: Any = None, chats: Any = None, users: Any = None) -> None:
        self.users_settings = users_settings
        self.chats_settings = chats_settings
        self.broadcasts_settings = broadcasts_settings
        self.exceptions = exceptions
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.users_settings is not None and hasattr(self.users_settings, 'write'): self.users_settings.write(writer)
        if self.chats_settings is not None and hasattr(self.chats_settings, 'write'): self.chats_settings.write(writer)
        if self.broadcasts_settings is not None and hasattr(self.broadcasts_settings, 'write'): self.broadcasts_settings.write(writer)
        writer.write_vector(self.exceptions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountAutoSaveSettings':
        users_settings = reader.read_object()
        chats_settings = reader.read_object()
        broadcasts_settings = reader.read_object()
        exceptions = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(users_settings=users_settings, chats_settings=chats_settings, broadcasts_settings=broadcasts_settings, exceptions=exceptions, chats=chats, users=users)


@register_tl
class HelpAppConfigNotModified(TLObject):
    ID: int = 0x7cde641d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpAppConfigNotModified':
        return cls()


@register_tl
class HelpAppConfig(TLObject):
    ID: int = 0xdd18782e

    def __init__(self, hash: Any = None, config: Any = None) -> None:
        self.hash = hash
        self.config = config

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)
        if self.config is not None and hasattr(self.config, 'write'): self.config.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpAppConfig':
        hash = reader.read_int32()
        config = reader.read_object()
        return cls(hash=hash, config=config)


@register_tl
class InputBotAppID(TLObject):
    ID: int = 0xa920bd7a

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotAppID':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputBotAppShortName(TLObject):
    ID: int = 0x908c0407

    def __init__(self, bot_id: Any = None, short_name: Any = None) -> None:
        self.bot_id = bot_id
        self.short_name = short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot_id is not None and hasattr(self.bot_id, 'write'): self.bot_id.write(writer)
        writer.write_string(self.short_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBotAppShortName':
        bot_id = reader.read_object()
        short_name = reader.read_string()
        return cls(bot_id=bot_id, short_name=short_name)


@register_tl
class BotAppNotModified(TLObject):
    ID: int = 0x5da674b7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotAppNotModified':
        return cls()


@register_tl
class BotApp(TLObject):
    ID: int = 0x95fcd1d6

    def __init__(self, document: Any = None, id: Any = None, access_hash: Any = None, short_name: Any = None, title: Any = None, description: Any = None, photo: Any = None, hash: Any = None) -> None:
        self.document = document
        self.id = id
        self.access_hash = access_hash
        self.short_name = short_name
        self.title = title
        self.description = description
        self.photo = photo
        self.hash = hash

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
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotApp':
        flags = reader.read_uint32()
        id = reader.read_int64()
        access_hash = reader.read_int64()
        short_name = reader.read_string()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object()
        document = reader.read_object() if (flags & (1 << 0)) else None
        hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash, short_name=short_name, title=title, description=description, photo=photo, document=document, hash=hash)


@register_tl
class MessagesBotApp(TLObject):
    ID: int = 0xeb50adf5

    def __init__(self, inactive: bool = False, request_write_access: bool = False, has_settings: bool = False, app: Any = None) -> None:
        self.inactive = inactive
        self.request_write_access = request_write_access
        self.has_settings = has_settings
        self.app = app

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inactive:
            flags |= (1 << 0)
        if self.request_write_access:
            flags |= (1 << 1)
        if self.has_settings:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.app is not None and hasattr(self.app, 'write'): self.app.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesBotApp':
        flags = reader.read_uint32()
        inactive = bool(flags & (1 << 0))
        request_write_access = bool(flags & (1 << 1))
        has_settings = bool(flags & (1 << 2))
        app = reader.read_object()
        return cls(inactive=inactive, request_write_access=request_write_access, has_settings=has_settings, app=app)


@register_tl
class InlineBotWebView(TLObject):
    ID: int = 0xb57295d5

    def __init__(self, text: Any = None, url: Any = None) -> None:
        self.text = text
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InlineBotWebView':
        text = reader.read_string()
        url = reader.read_string()
        return cls(text=text, url=url)


@register_tl
class ReadParticipantDate(TLObject):
    ID: int = 0x4a4ff172

    def __init__(self, user_id: Any = None, date: Any = None) -> None:
        self.user_id = user_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReadParticipantDate':
        user_id = reader.read_int64()
        date = reader.read_int32()
        return cls(user_id=user_id, date=date)


@register_tl
class InputChatlistDialogFilter(TLObject):
    ID: int = 0xf3e0da33

    def __init__(self, filter_id: Any = None) -> None:
        self.filter_id = filter_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.filter_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatlistDialogFilter':
        filter_id = reader.read_int32()
        return cls(filter_id=filter_id)


@register_tl
class ExportedChatlistInvite(TLObject):
    ID: int = 0xc5181ac

    def __init__(self, title: Any = None, url: Any = None, peers: Any = None) -> None:
        self.title = title
        self.url = url
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.url or '')
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ExportedChatlistInvite':
        flags = reader.read_uint32()
        title = reader.read_string()
        url = reader.read_string()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(title=title, url=url, peers=peers)


@register_tl
class ChatlistsExportedChatlistInvite(TLObject):
    ID: int = 0x10e6e3a6

    def __init__(self, filter: Any = None, invite: Any = None) -> None:
        self.filter = filter
        self.invite = invite

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        if self.invite is not None and hasattr(self.invite, 'write'): self.invite.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsExportedChatlistInvite':
        filter = reader.read_object()
        invite = reader.read_object()
        return cls(filter=filter, invite=invite)


@register_tl
class ChatlistsExportedInvites(TLObject):
    ID: int = 0x10ab6dc7

    def __init__(self, invites: Any = None, chats: Any = None, users: Any = None) -> None:
        self.invites = invites
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.invites or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsExportedInvites':
        invites = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(invites=invites, chats=chats, users=users)


@register_tl
class ChatlistsChatlistInviteAlready(TLObject):
    ID: int = 0xfa87f659

    def __init__(self, filter_id: Any = None, missing_peers: Any = None, already_peers: Any = None, chats: Any = None, users: Any = None) -> None:
        self.filter_id = filter_id
        self.missing_peers = missing_peers
        self.already_peers = already_peers
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.filter_id or 0)
        writer.write_vector(self.missing_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.already_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsChatlistInviteAlready':
        filter_id = reader.read_int32()
        missing_peers = reader.read_vector(lambda r: reader.read_object())
        already_peers = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(filter_id=filter_id, missing_peers=missing_peers, already_peers=already_peers, chats=chats, users=users)


@register_tl
class ChatlistsChatlistInvite(TLObject):
    ID: int = 0xf10ece2f

    def __init__(self, title_noanimate: bool = False, emoticon: Any = None, title: Any = None, peers: Any = None, chats: Any = None, users: Any = None) -> None:
        self.title_noanimate = title_noanimate
        self.emoticon = emoticon
        self.title = title
        self.peers = peers
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title_noanimate:
            flags |= (1 << 1)
        if self.emoticon is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)
        if self.emoticon is not None:
            writer.write_string(self.emoticon or '')
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsChatlistInvite':
        flags = reader.read_uint32()
        title_noanimate = bool(flags & (1 << 1))
        title = reader.read_object()
        emoticon = reader.read_string() if (flags & (1 << 0)) else None
        peers = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(title_noanimate=title_noanimate, title=title, emoticon=emoticon, peers=peers, chats=chats, users=users)


@register_tl
class ChatlistsChatlistUpdates(TLObject):
    ID: int = 0x93bd878d

    def __init__(self, missing_peers: Any = None, chats: Any = None, users: Any = None) -> None:
        self.missing_peers = missing_peers
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.missing_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatlistsChatlistUpdates':
        missing_peers = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(missing_peers=missing_peers, chats=chats, users=users)


@register_tl
class BotsBotInfo(TLObject):
    ID: int = 0xe8a775b0

    def __init__(self, name: Any = None, about: Any = None, description: Any = None) -> None:
        self.name = name
        self.about = about
        self.description = description

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.name or '')
        writer.write_string(self.about or '')
        writer.write_string(self.description or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsBotInfo':
        name = reader.read_string()
        about = reader.read_string()
        description = reader.read_string()
        return cls(name=name, about=about, description=description)


@register_tl
class MessagePeerVote(TLObject):
    ID: int = 0xb6cc2d5c

    def __init__(self, peer: Any = None, option: Any = None, date: Any = None) -> None:
        self.peer = peer
        self.option = option
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bytes(self.option or b'')
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagePeerVote':
        peer = reader.read_object()
        option = reader.read_bytes()
        date = reader.read_int32()
        return cls(peer=peer, option=option, date=date)


@register_tl
class MessagePeerVoteInputOption(TLObject):
    ID: int = 0x74cda504

    def __init__(self, peer: Any = None, date: Any = None) -> None:
        self.peer = peer
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagePeerVoteInputOption':
        peer = reader.read_object()
        date = reader.read_int32()
        return cls(peer=peer, date=date)


@register_tl
class MessagePeerVoteMultiple(TLObject):
    ID: int = 0x4628f6e6

    def __init__(self, peer: Any = None, options: Any = None, date: Any = None) -> None:
        self.peer = peer
        self.options = options
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagePeerVoteMultiple':
        peer = reader.read_object()
        options = reader.read_vector(lambda r: reader.read_object())
        date = reader.read_int32()
        return cls(peer=peer, options=options, date=date)


@register_tl
class StoryViews(TLObject):
    ID: int = 0x8d595cd6

    def __init__(self, has_viewers: bool = False, forwards_count: Any = None, reactions: Any = None, reactions_count: Any = None, recent_viewers: Any = None, views_count: Any = None) -> None:
        self.has_viewers = has_viewers
        self.forwards_count = forwards_count
        self.reactions = reactions
        self.reactions_count = reactions_count
        self.recent_viewers = recent_viewers
        self.views_count = views_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_viewers:
            flags |= (1 << 1)
        if self.forwards_count is not None:
            flags |= (1 << 2)
        if self.reactions is not None:
            flags |= (1 << 3)
        if self.reactions_count is not None:
            flags |= (1 << 4)
        if self.recent_viewers is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.views_count or 0)
        if self.forwards_count is not None:
            writer.write_int32(self.forwards_count or 0)
        if self.reactions is not None:
            writer.write_vector(self.reactions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.reactions_count is not None:
            writer.write_int32(self.reactions_count or 0)
        if self.recent_viewers is not None:
            writer.write_vector(self.recent_viewers or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryViews':
        flags = reader.read_uint32()
        has_viewers = bool(flags & (1 << 1))
        views_count = reader.read_int32()
        forwards_count = reader.read_int32() if (flags & (1 << 2)) else None
        reactions = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        reactions_count = reader.read_int32() if (flags & (1 << 4)) else None
        recent_viewers = reader.read_vector(lambda r: r.read_int64()) if (flags & (1 << 0)) else None
        return cls(has_viewers=has_viewers, views_count=views_count, forwards_count=forwards_count, reactions=reactions, reactions_count=reactions_count, recent_viewers=recent_viewers)


@register_tl
class StoryItemDeleted(TLObject):
    ID: int = 0x51e6ee4f

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryItemDeleted':
        id = reader.read_int32()
        return cls(id=id)


@register_tl
class StoryItemSkipped(TLObject):
    ID: int = 0xffadc913

    def __init__(self, close_friends: bool = False, live: bool = False, id: Any = None, date: Any = None, expire_date: Any = None) -> None:
        self.close_friends = close_friends
        self.live = live
        self.id = id
        self.date = date
        self.expire_date = expire_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.close_friends:
            flags |= (1 << 8)
        if self.live:
            flags |= (1 << 9)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.expire_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryItemSkipped':
        flags = reader.read_uint32()
        close_friends = bool(flags & (1 << 8))
        live = bool(flags & (1 << 9))
        id = reader.read_int32()
        date = reader.read_int32()
        expire_date = reader.read_int32()
        return cls(close_friends=close_friends, live=live, id=id, date=date, expire_date=expire_date)


@register_tl
class StoryItem(TLObject):
    ID: int = 0x16a4b93c

    def __init__(self, pinned: bool = False, public: bool = False, close_friends: bool = False, min: bool = False, noforwards: bool = False, edited: bool = False, contacts: bool = False, selected_contacts: bool = False, out: bool = False, from_id: Any = None, fwd_from: Any = None, caption: Any = None, entities: Any = None, media_areas: Any = None, privacy: Any = None, views: Any = None, sent_reaction: Any = None, albums: Any = None, music: Any = None, id: Any = None, date: Any = None, expire_date: Any = None, media: Any = None) -> None:
        self.pinned = pinned
        self.public = public
        self.close_friends = close_friends
        self.min = min
        self.noforwards = noforwards
        self.edited = edited
        self.contacts = contacts
        self.selected_contacts = selected_contacts
        self.out = out
        self.from_id = from_id
        self.fwd_from = fwd_from
        self.caption = caption
        self.entities = entities
        self.media_areas = media_areas
        self.privacy = privacy
        self.views = views
        self.sent_reaction = sent_reaction
        self.albums = albums
        self.music = music
        self.id = id
        self.date = date
        self.expire_date = expire_date
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 5)
        if self.public:
            flags |= (1 << 7)
        if self.close_friends:
            flags |= (1 << 8)
        if self.min:
            flags |= (1 << 9)
        if self.noforwards:
            flags |= (1 << 10)
        if self.edited:
            flags |= (1 << 11)
        if self.contacts:
            flags |= (1 << 12)
        if self.selected_contacts:
            flags |= (1 << 13)
        if self.out:
            flags |= (1 << 16)
        if self.from_id is not None:
            flags |= (1 << 18)
        if self.fwd_from is not None:
            flags |= (1 << 17)
        if self.caption is not None:
            flags |= (1 << 0)
        if self.entities is not None:
            flags |= (1 << 1)
        if self.media_areas is not None:
            flags |= (1 << 14)
        if self.privacy is not None:
            flags |= (1 << 2)
        if self.views is not None:
            flags |= (1 << 3)
        if self.sent_reaction is not None:
            flags |= (1 << 15)
        if self.albums is not None:
            flags |= (1 << 19)
        if self.music is not None:
            flags |= (1 << 20)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.date or 0)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.fwd_from is not None:
            if self.fwd_from is not None and hasattr(self.fwd_from, 'write'): self.fwd_from.write(writer)
        writer.write_int32(self.expire_date or 0)
        if self.caption is not None:
            writer.write_string(self.caption or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.media_areas is not None:
            writer.write_vector(self.media_areas or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.privacy is not None:
            writer.write_vector(self.privacy or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.views is not None:
            if self.views is not None and hasattr(self.views, 'write'): self.views.write(writer)
        if self.sent_reaction is not None:
            if self.sent_reaction is not None and hasattr(self.sent_reaction, 'write'): self.sent_reaction.write(writer)
        if self.albums is not None:
            writer.write_vector(self.albums or [], lambda w, x: w.write_int32(x))
        if self.music is not None:
            if self.music is not None and hasattr(self.music, 'write'): self.music.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryItem':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 5))
        public = bool(flags & (1 << 7))
        close_friends = bool(flags & (1 << 8))
        min = bool(flags & (1 << 9))
        noforwards = bool(flags & (1 << 10))
        edited = bool(flags & (1 << 11))
        contacts = bool(flags & (1 << 12))
        selected_contacts = bool(flags & (1 << 13))
        out = bool(flags & (1 << 16))
        id = reader.read_int32()
        date = reader.read_int32()
        from_id = reader.read_object() if (flags & (1 << 18)) else None
        fwd_from = reader.read_object() if (flags & (1 << 17)) else None
        expire_date = reader.read_int32()
        caption = reader.read_string() if (flags & (1 << 0)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        media = reader.read_object()
        media_areas = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 14)) else None
        privacy = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 2)) else None
        views = reader.read_object() if (flags & (1 << 3)) else None
        sent_reaction = reader.read_object() if (flags & (1 << 15)) else None
        albums = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 19)) else None
        music = reader.read_object() if (flags & (1 << 20)) else None
        return cls(pinned=pinned, public=public, close_friends=close_friends, min=min, noforwards=noforwards, edited=edited, contacts=contacts, selected_contacts=selected_contacts, out=out, id=id, date=date, from_id=from_id, fwd_from=fwd_from, expire_date=expire_date, caption=caption, entities=entities, media=media, media_areas=media_areas, privacy=privacy, views=views, sent_reaction=sent_reaction, albums=albums, music=music)


@register_tl
class StoriesAllStoriesNotModified(TLObject):
    ID: int = 0x1158fe3e

    def __init__(self, state: Any = None, stealth_mode: Any = None) -> None:
        self.state = state
        self.stealth_mode = stealth_mode

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        writer.write_uint32(flags)
        writer.write_string(self.state or '')
        if self.stealth_mode is not None and hasattr(self.stealth_mode, 'write'): self.stealth_mode.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesAllStoriesNotModified':
        flags = reader.read_uint32()
        state = reader.read_string()
        stealth_mode = reader.read_object()
        return cls(state=state, stealth_mode=stealth_mode)


@register_tl
class StoriesAllStories(TLObject):
    ID: int = 0x6efc5e81

    def __init__(self, has_more: bool = False, count: Any = None, state: Any = None, peer_stories: Any = None, chats: Any = None, users: Any = None, stealth_mode: Any = None) -> None:
        self.has_more = has_more
        self.count = count
        self.state = state
        self.peer_stories = peer_stories
        self.chats = chats
        self.users = users
        self.stealth_mode = stealth_mode

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_more:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_string(self.state or '')
        writer.write_vector(self.peer_stories or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.stealth_mode is not None and hasattr(self.stealth_mode, 'write'): self.stealth_mode.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesAllStories':
        flags = reader.read_uint32()
        has_more = bool(flags & (1 << 0))
        count = reader.read_int32()
        state = reader.read_string()
        peer_stories = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        stealth_mode = reader.read_object()
        return cls(has_more=has_more, count=count, state=state, peer_stories=peer_stories, chats=chats, users=users, stealth_mode=stealth_mode)


@register_tl
class StoriesStories(TLObject):
    ID: int = 0x63c3dd0a

    def __init__(self, pinned_to_top: Any = None, count: Any = None, stories: Any = None, chats: Any = None, users: Any = None) -> None:
        self.pinned_to_top = pinned_to_top
        self.count = count
        self.stories = stories
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned_to_top is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.stories or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.pinned_to_top is not None:
            writer.write_vector(self.pinned_to_top or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesStories':
        flags = reader.read_uint32()
        count = reader.read_int32()
        stories = reader.read_vector(lambda r: reader.read_object())
        pinned_to_top = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, stories=stories, pinned_to_top=pinned_to_top, chats=chats, users=users)


@register_tl
class StoryView(TLObject):
    ID: int = 0xb0bdeac5

    def __init__(self, blocked: bool = False, blocked_my_stories_from: bool = False, reaction: Any = None, user_id: Any = None, date: Any = None) -> None:
        self.blocked = blocked
        self.blocked_my_stories_from = blocked_my_stories_from
        self.reaction = reaction
        self.user_id = user_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blocked:
            flags |= (1 << 0)
        if self.blocked_my_stories_from:
            flags |= (1 << 1)
        if self.reaction is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.date or 0)
        if self.reaction is not None:
            if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryView':
        flags = reader.read_uint32()
        blocked = bool(flags & (1 << 0))
        blocked_my_stories_from = bool(flags & (1 << 1))
        user_id = reader.read_int64()
        date = reader.read_int32()
        reaction = reader.read_object() if (flags & (1 << 2)) else None
        return cls(blocked=blocked, blocked_my_stories_from=blocked_my_stories_from, user_id=user_id, date=date, reaction=reaction)


@register_tl
class StoryViewPublicForward(TLObject):
    ID: int = 0x9083670b

    def __init__(self, blocked: bool = False, blocked_my_stories_from: bool = False, message: Any = None) -> None:
        self.blocked = blocked
        self.blocked_my_stories_from = blocked_my_stories_from
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blocked:
            flags |= (1 << 0)
        if self.blocked_my_stories_from:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryViewPublicForward':
        flags = reader.read_uint32()
        blocked = bool(flags & (1 << 0))
        blocked_my_stories_from = bool(flags & (1 << 1))
        message = reader.read_object()
        return cls(blocked=blocked, blocked_my_stories_from=blocked_my_stories_from, message=message)


@register_tl
class StoryViewPublicRepost(TLObject):
    ID: int = 0xbd74cf49

    def __init__(self, blocked: bool = False, blocked_my_stories_from: bool = False, peer_id: Any = None, story: Any = None) -> None:
        self.blocked = blocked
        self.blocked_my_stories_from = blocked_my_stories_from
        self.peer_id = peer_id
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blocked:
            flags |= (1 << 0)
        if self.blocked_my_stories_from:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        if self.story is not None and hasattr(self.story, 'write'): self.story.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryViewPublicRepost':
        flags = reader.read_uint32()
        blocked = bool(flags & (1 << 0))
        blocked_my_stories_from = bool(flags & (1 << 1))
        peer_id = reader.read_object()
        story = reader.read_object()
        return cls(blocked=blocked, blocked_my_stories_from=blocked_my_stories_from, peer_id=peer_id, story=story)

