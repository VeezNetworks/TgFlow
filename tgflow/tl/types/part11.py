from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class StoriesStoryViewsList(TLObject):
    ID: int = 0x59d78fc5

    def __init__(self, next_offset: Any = None, count: Any = None, views_count: Any = None, forwards_count: Any = None, reactions_count: Any = None, views: Any = None, chats: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.count = count
        self.views_count = views_count
        self.forwards_count = forwards_count
        self.reactions_count = reactions_count
        self.views = views
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_int32(self.views_count or 0)
        writer.write_int32(self.forwards_count or 0)
        writer.write_int32(self.reactions_count or 0)
        writer.write_vector(self.views or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesStoryViewsList':
        flags = reader.read_uint32()
        count = reader.read_int32()
        views_count = reader.read_int32()
        forwards_count = reader.read_int32()
        reactions_count = reader.read_int32()
        views = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        return cls(count=count, views_count=views_count, forwards_count=forwards_count, reactions_count=reactions_count, views=views, chats=chats, users=users, next_offset=next_offset)


@register_tl
class StoriesStoryViews(TLObject):
    ID: int = 0xde9eed1d

    def __init__(self, views: Any = None, users: Any = None) -> None:
        self.views = views
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.views or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesStoryViews':
        views = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(views=views, users=users)


@register_tl
class InputReplyToMessage(TLObject):
    ID: int = 0x3bd4b7c2

    def __init__(self, top_msg_id: Any = None, reply_to_peer_id: Any = None, quote_text: Any = None, quote_entities: Any = None, quote_offset: Any = None, monoforum_peer_id: Any = None, todo_item_id: Any = None, poll_option: Any = None, reply_to_msg_id: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.reply_to_peer_id = reply_to_peer_id
        self.quote_text = quote_text
        self.quote_entities = quote_entities
        self.quote_offset = quote_offset
        self.monoforum_peer_id = monoforum_peer_id
        self.todo_item_id = todo_item_id
        self.poll_option = poll_option
        self.reply_to_msg_id = reply_to_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.reply_to_peer_id is not None:
            flags |= (1 << 1)
        if self.quote_text is not None:
            flags |= (1 << 2)
        if self.quote_entities is not None:
            flags |= (1 << 3)
        if self.quote_offset is not None:
            flags |= (1 << 4)
        if self.monoforum_peer_id is not None:
            flags |= (1 << 5)
        if self.todo_item_id is not None:
            flags |= (1 << 6)
        if self.poll_option is not None:
            flags |= (1 << 7)
        writer.write_uint32(flags)
        writer.write_int32(self.reply_to_msg_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.reply_to_peer_id is not None:
            if self.reply_to_peer_id is not None and hasattr(self.reply_to_peer_id, 'write'): self.reply_to_peer_id.write(writer)
        if self.quote_text is not None:
            writer.write_string(self.quote_text or '')
        if self.quote_entities is not None:
            writer.write_vector(self.quote_entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.quote_offset is not None:
            writer.write_int32(self.quote_offset or 0)
        if self.monoforum_peer_id is not None:
            if self.monoforum_peer_id is not None and hasattr(self.monoforum_peer_id, 'write'): self.monoforum_peer_id.write(writer)
        if self.todo_item_id is not None:
            writer.write_int32(self.todo_item_id or 0)
        if self.poll_option is not None:
            writer.write_bytes(self.poll_option or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReplyToMessage':
        flags = reader.read_uint32()
        reply_to_msg_id = reader.read_int32()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        reply_to_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        quote_text = reader.read_string() if (flags & (1 << 2)) else None
        quote_entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        quote_offset = reader.read_int32() if (flags & (1 << 4)) else None
        monoforum_peer_id = reader.read_object() if (flags & (1 << 5)) else None
        todo_item_id = reader.read_int32() if (flags & (1 << 6)) else None
        poll_option = reader.read_bytes() if (flags & (1 << 7)) else None
        return cls(reply_to_msg_id=reply_to_msg_id, top_msg_id=top_msg_id, reply_to_peer_id=reply_to_peer_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset, monoforum_peer_id=monoforum_peer_id, todo_item_id=todo_item_id, poll_option=poll_option)


@register_tl
class InputReplyToStory(TLObject):
    ID: int = 0x5881323a

    def __init__(self, peer: Any = None, story_id: Any = None) -> None:
        self.peer = peer
        self.story_id = story_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.story_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReplyToStory':
        peer = reader.read_object()
        story_id = reader.read_int32()
        return cls(peer=peer, story_id=story_id)


@register_tl
class InputReplyToMonoForum(TLObject):
    ID: int = 0x69d66c45

    def __init__(self, monoforum_peer_id: Any = None) -> None:
        self.monoforum_peer_id = monoforum_peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.monoforum_peer_id is not None and hasattr(self.monoforum_peer_id, 'write'): self.monoforum_peer_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReplyToMonoForum':
        monoforum_peer_id = reader.read_object()
        return cls(monoforum_peer_id=monoforum_peer_id)


@register_tl
class ExportedStoryLink(TLObject):
    ID: int = 0x3fc9053b

    def __init__(self, link: Any = None) -> None:
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.link or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ExportedStoryLink':
        link = reader.read_string()
        return cls(link=link)


@register_tl
class StoriesStealthMode(TLObject):
    ID: int = 0x712e27fd

    def __init__(self, active_until_date: Any = None, cooldown_until_date: Any = None) -> None:
        self.active_until_date = active_until_date
        self.cooldown_until_date = cooldown_until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.active_until_date is not None:
            flags |= (1 << 0)
        if self.cooldown_until_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.active_until_date is not None:
            writer.write_int32(self.active_until_date or 0)
        if self.cooldown_until_date is not None:
            writer.write_int32(self.cooldown_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesStealthMode':
        flags = reader.read_uint32()
        active_until_date = reader.read_int32() if (flags & (1 << 0)) else None
        cooldown_until_date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(active_until_date=active_until_date, cooldown_until_date=cooldown_until_date)


@register_tl
class MediaAreaCoordinates(TLObject):
    ID: int = 0xcfc9e002

    def __init__(self, radius: Any = None, x: Any = None, y: Any = None, w: Any = None, h: Any = None, rotation: Any = None) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rotation = rotation

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.radius is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_double(self.x or 0.0)
        writer.write_double(self.y or 0.0)
        writer.write_double(self.w or 0.0)
        writer.write_double(self.h or 0.0)
        writer.write_double(self.rotation or 0.0)
        if self.radius is not None:
            writer.write_double(self.radius or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaCoordinates':
        flags = reader.read_uint32()
        x = reader.read_double()
        y = reader.read_double()
        w = reader.read_double()
        h = reader.read_double()
        rotation = reader.read_double()
        radius = reader.read_double() if (flags & (1 << 0)) else None
        return cls(x=x, y=y, w=w, h=h, rotation=rotation, radius=radius)


@register_tl
class MediaAreaVenue(TLObject):
    ID: int = 0xbe82db9c

    def __init__(self, coordinates: Any = None, geo: Any = None, title: Any = None, address: Any = None, provider: Any = None, venue_id: Any = None, venue_type: Any = None) -> None:
        self.coordinates = coordinates
        self.geo = geo
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        writer.write_string(self.title or '')
        writer.write_string(self.address or '')
        writer.write_string(self.provider or '')
        writer.write_string(self.venue_id or '')
        writer.write_string(self.venue_type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaVenue':
        coordinates = reader.read_object()
        geo = reader.read_object()
        title = reader.read_string()
        address = reader.read_string()
        provider = reader.read_string()
        venue_id = reader.read_string()
        venue_type = reader.read_string()
        return cls(coordinates=coordinates, geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)


@register_tl
class InputMediaAreaVenue(TLObject):
    ID: int = 0xb282217f

    def __init__(self, coordinates: Any = None, query_id: Any = None, result_id: Any = None) -> None:
        self.coordinates = coordinates
        self.query_id = query_id
        self.result_id = result_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        writer.write_int64(self.query_id or 0)
        writer.write_string(self.result_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaAreaVenue':
        coordinates = reader.read_object()
        query_id = reader.read_int64()
        result_id = reader.read_string()
        return cls(coordinates=coordinates, query_id=query_id, result_id=result_id)


@register_tl
class MediaAreaGeoPoint(TLObject):
    ID: int = 0xcad5452d

    def __init__(self, address: Any = None, coordinates: Any = None, geo: Any = None) -> None:
        self.address = address
        self.coordinates = coordinates
        self.geo = geo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.address is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        if self.address is not None:
            if self.address is not None and hasattr(self.address, 'write'): self.address.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaGeoPoint':
        flags = reader.read_uint32()
        coordinates = reader.read_object()
        geo = reader.read_object()
        address = reader.read_object() if (flags & (1 << 0)) else None
        return cls(coordinates=coordinates, geo=geo, address=address)


@register_tl
class MediaAreaSuggestedReaction(TLObject):
    ID: int = 0x14455871

    def __init__(self, dark: bool = False, flipped: bool = False, coordinates: Any = None, reaction: Any = None) -> None:
        self.dark = dark
        self.flipped = flipped
        self.coordinates = coordinates
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        if self.flipped:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaSuggestedReaction':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        flipped = bool(flags & (1 << 1))
        coordinates = reader.read_object()
        reaction = reader.read_object()
        return cls(dark=dark, flipped=flipped, coordinates=coordinates, reaction=reaction)


@register_tl
class MediaAreaChannelPost(TLObject):
    ID: int = 0x770416af

    def __init__(self, coordinates: Any = None, channel_id: Any = None, msg_id: Any = None) -> None:
        self.coordinates = coordinates
        self.channel_id = channel_id
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaChannelPost':
        coordinates = reader.read_object()
        channel_id = reader.read_int64()
        msg_id = reader.read_int32()
        return cls(coordinates=coordinates, channel_id=channel_id, msg_id=msg_id)


@register_tl
class InputMediaAreaChannelPost(TLObject):
    ID: int = 0x2271f2bf

    def __init__(self, coordinates: Any = None, channel: Any = None, msg_id: Any = None) -> None:
        self.coordinates = coordinates
        self.channel = channel
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaAreaChannelPost':
        coordinates = reader.read_object()
        channel = reader.read_object()
        msg_id = reader.read_int32()
        return cls(coordinates=coordinates, channel=channel, msg_id=msg_id)


@register_tl
class MediaAreaUrl(TLObject):
    ID: int = 0x37381085

    def __init__(self, coordinates: Any = None, url: Any = None) -> None:
        self.coordinates = coordinates
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaUrl':
        coordinates = reader.read_object()
        url = reader.read_string()
        return cls(coordinates=coordinates, url=url)


@register_tl
class MediaAreaWeather(TLObject):
    ID: int = 0x49a6549c

    def __init__(self, coordinates: Any = None, emoji: Any = None, temperature_c: Any = None, color: Any = None) -> None:
        self.coordinates = coordinates
        self.emoji = emoji
        self.temperature_c = temperature_c
        self.color = color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        writer.write_string(self.emoji or '')
        writer.write_double(self.temperature_c or 0.0)
        writer.write_int32(self.color or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaWeather':
        coordinates = reader.read_object()
        emoji = reader.read_string()
        temperature_c = reader.read_double()
        color = reader.read_int32()
        return cls(coordinates=coordinates, emoji=emoji, temperature_c=temperature_c, color=color)


@register_tl
class MediaAreaStarGift(TLObject):
    ID: int = 0x5787686d

    def __init__(self, coordinates: Any = None, slug: Any = None) -> None:
        self.coordinates = coordinates
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.coordinates is not None and hasattr(self.coordinates, 'write'): self.coordinates.write(writer)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MediaAreaStarGift':
        coordinates = reader.read_object()
        slug = reader.read_string()
        return cls(coordinates=coordinates, slug=slug)


@register_tl
class PeerStories(TLObject):
    ID: int = 0x9a35e999

    def __init__(self, max_read_id: Any = None, peer: Any = None, stories: Any = None) -> None:
        self.max_read_id = max_read_id
        self.peer = peer
        self.stories = stories

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.max_read_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.max_read_id is not None:
            writer.write_int32(self.max_read_id or 0)
        writer.write_vector(self.stories or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerStories':
        flags = reader.read_uint32()
        peer = reader.read_object()
        max_read_id = reader.read_int32() if (flags & (1 << 0)) else None
        stories = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, max_read_id=max_read_id, stories=stories)


@register_tl
class StoriesPeerStories(TLObject):
    ID: int = 0xcae68768

    def __init__(self, stories: Any = None, chats: Any = None, users: Any = None) -> None:
        self.stories = stories
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stories is not None and hasattr(self.stories, 'write'): self.stories.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesPeerStories':
        stories = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(stories=stories, chats=chats, users=users)


@register_tl
class MessagesWebPage(TLObject):
    ID: int = 0xfd5e12bd

    def __init__(self, webpage: Any = None, chats: Any = None, users: Any = None) -> None:
        self.webpage = webpage
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.webpage is not None and hasattr(self.webpage, 'write'): self.webpage.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesWebPage':
        webpage = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(webpage=webpage, chats=chats, users=users)


@register_tl
class PremiumGiftCodeOption(TLObject):
    ID: int = 0x257e962b

    def __init__(self, store_product: Any = None, store_quantity: Any = None, users: Any = None, months: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.store_product = store_product
        self.store_quantity = store_quantity
        self.users = users
        self.months = months
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.store_product is not None:
            flags |= (1 << 0)
        if self.store_quantity is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.users or 0)
        writer.write_int32(self.months or 0)
        if self.store_product is not None:
            writer.write_string(self.store_product or '')
        if self.store_quantity is not None:
            writer.write_int32(self.store_quantity or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumGiftCodeOption':
        flags = reader.read_uint32()
        users = reader.read_int32()
        months = reader.read_int32()
        store_product = reader.read_string() if (flags & (1 << 0)) else None
        store_quantity = reader.read_int32() if (flags & (1 << 1)) else None
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(users=users, months=months, store_product=store_product, store_quantity=store_quantity, currency=currency, amount=amount)


@register_tl
class PaymentsCheckedGiftCode(TLObject):
    ID: int = 0xeb983f8f

    def __init__(self, via_giveaway: bool = False, from_id: Any = None, giveaway_msg_id: Any = None, to_id: Any = None, used_date: Any = None, date: Any = None, days: Any = None, chats: Any = None, users: Any = None) -> None:
        self.via_giveaway = via_giveaway
        self.from_id = from_id
        self.giveaway_msg_id = giveaway_msg_id
        self.to_id = to_id
        self.used_date = used_date
        self.date = date
        self.days = days
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_giveaway:
            flags |= (1 << 2)
        if self.from_id is not None:
            flags |= (1 << 4)
        if self.giveaway_msg_id is not None:
            flags |= (1 << 3)
        if self.to_id is not None:
            flags |= (1 << 0)
        if self.used_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.giveaway_msg_id is not None:
            writer.write_int32(self.giveaway_msg_id or 0)
        if self.to_id is not None:
            writer.write_int64(self.to_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.days or 0)
        if self.used_date is not None:
            writer.write_int32(self.used_date or 0)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCheckedGiftCode':
        flags = reader.read_uint32()
        via_giveaway = bool(flags & (1 << 2))
        from_id = reader.read_object() if (flags & (1 << 4)) else None
        giveaway_msg_id = reader.read_int32() if (flags & (1 << 3)) else None
        to_id = reader.read_int64() if (flags & (1 << 0)) else None
        date = reader.read_int32()
        days = reader.read_int32()
        used_date = reader.read_int32() if (flags & (1 << 1)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(via_giveaway=via_giveaway, from_id=from_id, giveaway_msg_id=giveaway_msg_id, to_id=to_id, date=date, days=days, used_date=used_date, chats=chats, users=users)


@register_tl
class PaymentsGiveawayInfo(TLObject):
    ID: int = 0x4367daa0

    def __init__(self, participating: bool = False, preparing_results: bool = False, joined_too_early_date: Any = None, admin_disallowed_chat_id: Any = None, disallowed_country: Any = None, start_date: Any = None) -> None:
        self.participating = participating
        self.preparing_results = preparing_results
        self.joined_too_early_date = joined_too_early_date
        self.admin_disallowed_chat_id = admin_disallowed_chat_id
        self.disallowed_country = disallowed_country
        self.start_date = start_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.participating:
            flags |= (1 << 0)
        if self.preparing_results:
            flags |= (1 << 3)
        if self.joined_too_early_date is not None:
            flags |= (1 << 1)
        if self.admin_disallowed_chat_id is not None:
            flags |= (1 << 2)
        if self.disallowed_country is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int32(self.start_date or 0)
        if self.joined_too_early_date is not None:
            writer.write_int32(self.joined_too_early_date or 0)
        if self.admin_disallowed_chat_id is not None:
            writer.write_int64(self.admin_disallowed_chat_id or 0)
        if self.disallowed_country is not None:
            writer.write_string(self.disallowed_country or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGiveawayInfo':
        flags = reader.read_uint32()
        participating = bool(flags & (1 << 0))
        preparing_results = bool(flags & (1 << 3))
        start_date = reader.read_int32()
        joined_too_early_date = reader.read_int32() if (flags & (1 << 1)) else None
        admin_disallowed_chat_id = reader.read_int64() if (flags & (1 << 2)) else None
        disallowed_country = reader.read_string() if (flags & (1 << 4)) else None
        return cls(participating=participating, preparing_results=preparing_results, start_date=start_date, joined_too_early_date=joined_too_early_date, admin_disallowed_chat_id=admin_disallowed_chat_id, disallowed_country=disallowed_country)


@register_tl
class PaymentsGiveawayInfoResults(TLObject):
    ID: int = 0xe175e66f

    def __init__(self, winner: bool = False, refunded: bool = False, gift_code_slug: Any = None, stars_prize: Any = None, activated_count: Any = None, start_date: Any = None, finish_date: Any = None, winners_count: Any = None) -> None:
        self.winner = winner
        self.refunded = refunded
        self.gift_code_slug = gift_code_slug
        self.stars_prize = stars_prize
        self.activated_count = activated_count
        self.start_date = start_date
        self.finish_date = finish_date
        self.winners_count = winners_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.winner:
            flags |= (1 << 0)
        if self.refunded:
            flags |= (1 << 1)
        if self.gift_code_slug is not None:
            flags |= (1 << 3)
        if self.stars_prize is not None:
            flags |= (1 << 4)
        if self.activated_count is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.start_date or 0)
        if self.gift_code_slug is not None:
            writer.write_string(self.gift_code_slug or '')
        if self.stars_prize is not None:
            writer.write_int64(self.stars_prize or 0)
        writer.write_int32(self.finish_date or 0)
        writer.write_int32(self.winners_count or 0)
        if self.activated_count is not None:
            writer.write_int32(self.activated_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGiveawayInfoResults':
        flags = reader.read_uint32()
        winner = bool(flags & (1 << 0))
        refunded = bool(flags & (1 << 1))
        start_date = reader.read_int32()
        gift_code_slug = reader.read_string() if (flags & (1 << 3)) else None
        stars_prize = reader.read_int64() if (flags & (1 << 4)) else None
        finish_date = reader.read_int32()
        winners_count = reader.read_int32()
        activated_count = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(winner=winner, refunded=refunded, start_date=start_date, gift_code_slug=gift_code_slug, stars_prize=stars_prize, finish_date=finish_date, winners_count=winners_count, activated_count=activated_count)


@register_tl
class PrepaidGiveaway(TLObject):
    ID: int = 0xb2539d54

    def __init__(self, id: Any = None, months: Any = None, quantity: Any = None, date: Any = None) -> None:
        self.id = id
        self.months = months
        self.quantity = quantity
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int32(self.months or 0)
        writer.write_int32(self.quantity or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrepaidGiveaway':
        id = reader.read_int64()
        months = reader.read_int32()
        quantity = reader.read_int32()
        date = reader.read_int32()
        return cls(id=id, months=months, quantity=quantity, date=date)


@register_tl
class PrepaidStarsGiveaway(TLObject):
    ID: int = 0x9a9d77e0

    def __init__(self, id: Any = None, stars: Any = None, quantity: Any = None, boosts: Any = None, date: Any = None) -> None:
        self.id = id
        self.stars = stars
        self.quantity = quantity
        self.boosts = boosts
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.stars or 0)
        writer.write_int32(self.quantity or 0)
        writer.write_int32(self.boosts or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrepaidStarsGiveaway':
        id = reader.read_int64()
        stars = reader.read_int64()
        quantity = reader.read_int32()
        boosts = reader.read_int32()
        date = reader.read_int32()
        return cls(id=id, stars=stars, quantity=quantity, boosts=boosts, date=date)


@register_tl
class Boost(TLObject):
    ID: int = 0x4b3e14d6

    def __init__(self, gift: bool = False, giveaway: bool = False, unclaimed: bool = False, user_id: Any = None, giveaway_msg_id: Any = None, used_gift_slug: Any = None, multiplier: Any = None, stars: Any = None, id: Any = None, date: Any = None, expires: Any = None) -> None:
        self.gift = gift
        self.giveaway = giveaway
        self.unclaimed = unclaimed
        self.user_id = user_id
        self.giveaway_msg_id = giveaway_msg_id
        self.used_gift_slug = used_gift_slug
        self.multiplier = multiplier
        self.stars = stars
        self.id = id
        self.date = date
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.gift:
            flags |= (1 << 1)
        if self.giveaway:
            flags |= (1 << 2)
        if self.unclaimed:
            flags |= (1 << 3)
        if self.user_id is not None:
            flags |= (1 << 0)
        if self.giveaway_msg_id is not None:
            flags |= (1 << 2)
        if self.used_gift_slug is not None:
            flags |= (1 << 4)
        if self.multiplier is not None:
            flags |= (1 << 5)
        if self.stars is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        if self.user_id is not None:
            writer.write_int64(self.user_id or 0)
        if self.giveaway_msg_id is not None:
            writer.write_int32(self.giveaway_msg_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.expires or 0)
        if self.used_gift_slug is not None:
            writer.write_string(self.used_gift_slug or '')
        if self.multiplier is not None:
            writer.write_int32(self.multiplier or 0)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Boost':
        flags = reader.read_uint32()
        gift = bool(flags & (1 << 1))
        giveaway = bool(flags & (1 << 2))
        unclaimed = bool(flags & (1 << 3))
        id = reader.read_string()
        user_id = reader.read_int64() if (flags & (1 << 0)) else None
        giveaway_msg_id = reader.read_int32() if (flags & (1 << 2)) else None
        date = reader.read_int32()
        expires = reader.read_int32()
        used_gift_slug = reader.read_string() if (flags & (1 << 4)) else None
        multiplier = reader.read_int32() if (flags & (1 << 5)) else None
        stars = reader.read_int64() if (flags & (1 << 6)) else None
        return cls(gift=gift, giveaway=giveaway, unclaimed=unclaimed, id=id, user_id=user_id, giveaway_msg_id=giveaway_msg_id, date=date, expires=expires, used_gift_slug=used_gift_slug, multiplier=multiplier, stars=stars)


@register_tl
class PremiumBoostsList(TLObject):
    ID: int = 0x86f8613c

    def __init__(self, next_offset: Any = None, count: Any = None, boosts: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.count = count
        self.boosts = boosts
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.boosts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumBoostsList':
        flags = reader.read_uint32()
        count = reader.read_int32()
        boosts = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, boosts=boosts, next_offset=next_offset, users=users)


@register_tl
class MyBoost(TLObject):
    ID: int = 0xc448415c

    def __init__(self, peer: Any = None, cooldown_until_date: Any = None, slot: Any = None, date: Any = None, expires: Any = None) -> None:
        self.peer = peer
        self.cooldown_until_date = cooldown_until_date
        self.slot = slot
        self.date = date
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer is not None:
            flags |= (1 << 0)
        if self.cooldown_until_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.slot or 0)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.expires or 0)
        if self.cooldown_until_date is not None:
            writer.write_int32(self.cooldown_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MyBoost':
        flags = reader.read_uint32()
        slot = reader.read_int32()
        peer = reader.read_object() if (flags & (1 << 0)) else None
        date = reader.read_int32()
        expires = reader.read_int32()
        cooldown_until_date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(slot=slot, peer=peer, date=date, expires=expires, cooldown_until_date=cooldown_until_date)


@register_tl
class PremiumMyBoosts(TLObject):
    ID: int = 0x9ae228e2

    def __init__(self, my_boosts: Any = None, chats: Any = None, users: Any = None) -> None:
        self.my_boosts = my_boosts
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.my_boosts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumMyBoosts':
        my_boosts = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(my_boosts=my_boosts, chats=chats, users=users)


@register_tl
class PremiumBoostsStatus(TLObject):
    ID: int = 0x4959427a

    def __init__(self, my_boost: bool = False, gift_boosts: Any = None, next_level_boosts: Any = None, premium_audience: Any = None, prepaid_giveaways: Any = None, my_boost_slots: Any = None, level: Any = None, current_level_boosts: Any = None, boosts: Any = None, boost_url: Any = None) -> None:
        self.my_boost = my_boost
        self.gift_boosts = gift_boosts
        self.next_level_boosts = next_level_boosts
        self.premium_audience = premium_audience
        self.prepaid_giveaways = prepaid_giveaways
        self.my_boost_slots = my_boost_slots
        self.level = level
        self.current_level_boosts = current_level_boosts
        self.boosts = boosts
        self.boost_url = boost_url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.my_boost:
            flags |= (1 << 2)
        if self.gift_boosts is not None:
            flags |= (1 << 4)
        if self.next_level_boosts is not None:
            flags |= (1 << 0)
        if self.premium_audience is not None:
            flags |= (1 << 1)
        if self.prepaid_giveaways is not None:
            flags |= (1 << 3)
        if self.my_boost_slots is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.level or 0)
        writer.write_int32(self.current_level_boosts or 0)
        writer.write_int32(self.boosts or 0)
        if self.gift_boosts is not None:
            writer.write_int32(self.gift_boosts or 0)
        if self.next_level_boosts is not None:
            writer.write_int32(self.next_level_boosts or 0)
        if self.premium_audience is not None:
            if self.premium_audience is not None and hasattr(self.premium_audience, 'write'): self.premium_audience.write(writer)
        writer.write_string(self.boost_url or '')
        if self.prepaid_giveaways is not None:
            writer.write_vector(self.prepaid_giveaways or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.my_boost_slots is not None:
            writer.write_vector(self.my_boost_slots or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PremiumBoostsStatus':
        flags = reader.read_uint32()
        my_boost = bool(flags & (1 << 2))
        level = reader.read_int32()
        current_level_boosts = reader.read_int32()
        boosts = reader.read_int32()
        gift_boosts = reader.read_int32() if (flags & (1 << 4)) else None
        next_level_boosts = reader.read_int32() if (flags & (1 << 0)) else None
        premium_audience = reader.read_object() if (flags & (1 << 1)) else None
        boost_url = reader.read_string()
        prepaid_giveaways = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        my_boost_slots = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 2)) else None
        return cls(my_boost=my_boost, level=level, current_level_boosts=current_level_boosts, boosts=boosts, gift_boosts=gift_boosts, next_level_boosts=next_level_boosts, premium_audience=premium_audience, boost_url=boost_url, prepaid_giveaways=prepaid_giveaways, my_boost_slots=my_boost_slots)


@register_tl
class StoryFwdHeader(TLObject):
    ID: int = 0xb826e150

    def __init__(self, modified: bool = False, from_: Any = None, from_name: Any = None, story_id: Any = None) -> None:
        self.modified = modified
        self.from_ = from_
        self.from_name = from_name
        self.story_id = story_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.modified:
            flags |= (1 << 3)
        if self.from_ is not None:
            flags |= (1 << 0)
        if self.from_name is not None:
            flags |= (1 << 1)
        if self.story_id is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.from_ is not None:
            if self.from_ is not None and hasattr(self.from_, 'write'): self.from_.write(writer)
        if self.from_name is not None:
            writer.write_string(self.from_name or '')
        if self.story_id is not None:
            writer.write_int32(self.story_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryFwdHeader':
        flags = reader.read_uint32()
        modified = bool(flags & (1 << 3))
        from_ = reader.read_object() if (flags & (1 << 0)) else None
        from_name = reader.read_string() if (flags & (1 << 1)) else None
        story_id = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(modified=modified, from_=from_, from_name=from_name, story_id=story_id)


@register_tl
class PostInteractionCountersMessage(TLObject):
    ID: int = 0xe7058e7f

    def __init__(self, msg_id: Any = None, views: Any = None, forwards: Any = None, reactions: Any = None) -> None:
        self.msg_id = msg_id
        self.views = views
        self.forwards = forwards
        self.reactions = reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.msg_id or 0)
        writer.write_int32(self.views or 0)
        writer.write_int32(self.forwards or 0)
        writer.write_int32(self.reactions or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PostInteractionCountersMessage':
        msg_id = reader.read_int32()
        views = reader.read_int32()
        forwards = reader.read_int32()
        reactions = reader.read_int32()
        return cls(msg_id=msg_id, views=views, forwards=forwards, reactions=reactions)


@register_tl
class PostInteractionCountersStory(TLObject):
    ID: int = 0x8a480e27

    def __init__(self, story_id: Any = None, views: Any = None, forwards: Any = None, reactions: Any = None) -> None:
        self.story_id = story_id
        self.views = views
        self.forwards = forwards
        self.reactions = reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.story_id or 0)
        writer.write_int32(self.views or 0)
        writer.write_int32(self.forwards or 0)
        writer.write_int32(self.reactions or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PostInteractionCountersStory':
        story_id = reader.read_int32()
        views = reader.read_int32()
        forwards = reader.read_int32()
        reactions = reader.read_int32()
        return cls(story_id=story_id, views=views, forwards=forwards, reactions=reactions)


@register_tl
class StatsStoryStats(TLObject):
    ID: int = 0x50cd067c

    def __init__(self, views_graph: Any = None, reactions_by_emotion_graph: Any = None) -> None:
        self.views_graph = views_graph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.views_graph is not None and hasattr(self.views_graph, 'write'): self.views_graph.write(writer)
        if self.reactions_by_emotion_graph is not None and hasattr(self.reactions_by_emotion_graph, 'write'): self.reactions_by_emotion_graph.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsStoryStats':
        views_graph = reader.read_object()
        reactions_by_emotion_graph = reader.read_object()
        return cls(views_graph=views_graph, reactions_by_emotion_graph=reactions_by_emotion_graph)


@register_tl
class PublicForwardMessage(TLObject):
    ID: int = 0x1f2bf4a

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PublicForwardMessage':
        message = reader.read_object()
        return cls(message=message)


@register_tl
class PublicForwardStory(TLObject):
    ID: int = 0xedf3add0

    def __init__(self, peer: Any = None, story: Any = None) -> None:
        self.peer = peer
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.story is not None and hasattr(self.story, 'write'): self.story.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PublicForwardStory':
        peer = reader.read_object()
        story = reader.read_object()
        return cls(peer=peer, story=story)


@register_tl
class StatsPublicForwards(TLObject):
    ID: int = 0x93037e20

    def __init__(self, next_offset: Any = None, count: Any = None, forwards: Any = None, chats: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.count = count
        self.forwards = forwards
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.forwards or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsPublicForwards':
        flags = reader.read_uint32()
        count = reader.read_int32()
        forwards = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, forwards=forwards, next_offset=next_offset, chats=chats, users=users)


@register_tl
class PeerColor(TLObject):
    ID: int = 0xb54b5acf

    def __init__(self, color: Any = None, background_emoji_id: Any = None) -> None:
        self.color = color
        self.background_emoji_id = background_emoji_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.color is not None:
            flags |= (1 << 0)
        if self.background_emoji_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.color is not None:
            writer.write_int32(self.color or 0)
        if self.background_emoji_id is not None:
            writer.write_int64(self.background_emoji_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerColor':
        flags = reader.read_uint32()
        color = reader.read_int32() if (flags & (1 << 0)) else None
        background_emoji_id = reader.read_int64() if (flags & (1 << 1)) else None
        return cls(color=color, background_emoji_id=background_emoji_id)


@register_tl
class PeerColorCollectible(TLObject):
    ID: int = 0xb9c0639a

    def __init__(self, dark_accent_color: Any = None, dark_colors: Any = None, collectible_id: Any = None, gift_emoji_id: Any = None, background_emoji_id: Any = None, accent_color: Any = None, colors: Any = None) -> None:
        self.dark_accent_color = dark_accent_color
        self.dark_colors = dark_colors
        self.collectible_id = collectible_id
        self.gift_emoji_id = gift_emoji_id
        self.background_emoji_id = background_emoji_id
        self.accent_color = accent_color
        self.colors = colors

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark_accent_color is not None:
            flags |= (1 << 0)
        if self.dark_colors is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.collectible_id or 0)
        writer.write_int64(self.gift_emoji_id or 0)
        writer.write_int64(self.background_emoji_id or 0)
        writer.write_int32(self.accent_color or 0)
        writer.write_vector(self.colors or [], lambda w, x: w.write_int32(x))
        if self.dark_accent_color is not None:
            writer.write_int32(self.dark_accent_color or 0)
        if self.dark_colors is not None:
            writer.write_vector(self.dark_colors or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerColorCollectible':
        flags = reader.read_uint32()
        collectible_id = reader.read_int64()
        gift_emoji_id = reader.read_int64()
        background_emoji_id = reader.read_int64()
        accent_color = reader.read_int32()
        colors = reader.read_vector(lambda r: r.read_int32())
        dark_accent_color = reader.read_int32() if (flags & (1 << 0)) else None
        dark_colors = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 1)) else None
        return cls(collectible_id=collectible_id, gift_emoji_id=gift_emoji_id, background_emoji_id=background_emoji_id, accent_color=accent_color, colors=colors, dark_accent_color=dark_accent_color, dark_colors=dark_colors)


@register_tl
class InputPeerColorCollectible(TLObject):
    ID: int = 0xb8ea86a9

    def __init__(self, collectible_id: Any = None) -> None:
        self.collectible_id = collectible_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.collectible_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerColorCollectible':
        collectible_id = reader.read_int64()
        return cls(collectible_id=collectible_id)


@register_tl
class HelpPeerColorSet(TLObject):
    ID: int = 0x26219a58

    def __init__(self, colors: Any = None) -> None:
        self.colors = colors

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.colors or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPeerColorSet':
        colors = reader.read_vector(lambda r: r.read_int32())
        return cls(colors=colors)


@register_tl
class HelpPeerColorProfileSet(TLObject):
    ID: int = 0x767d61eb

    def __init__(self, palette_colors: Any = None, bg_colors: Any = None, story_colors: Any = None) -> None:
        self.palette_colors = palette_colors
        self.bg_colors = bg_colors
        self.story_colors = story_colors

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.palette_colors or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.bg_colors or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.story_colors or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPeerColorProfileSet':
        palette_colors = reader.read_vector(lambda r: r.read_int32())
        bg_colors = reader.read_vector(lambda r: r.read_int32())
        story_colors = reader.read_vector(lambda r: r.read_int32())
        return cls(palette_colors=palette_colors, bg_colors=bg_colors, story_colors=story_colors)


@register_tl
class HelpPeerColorOption(TLObject):
    ID: int = 0xadec6ebe

    def __init__(self, hidden: bool = False, colors: Any = None, dark_colors: Any = None, channel_min_level: Any = None, group_min_level: Any = None, color_id: Any = None) -> None:
        self.hidden = hidden
        self.colors = colors
        self.dark_colors = dark_colors
        self.channel_min_level = channel_min_level
        self.group_min_level = group_min_level
        self.color_id = color_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.hidden:
            flags |= (1 << 0)
        if self.colors is not None:
            flags |= (1 << 1)
        if self.dark_colors is not None:
            flags |= (1 << 2)
        if self.channel_min_level is not None:
            flags |= (1 << 3)
        if self.group_min_level is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_int32(self.color_id or 0)
        if self.colors is not None:
            if self.colors is not None and hasattr(self.colors, 'write'): self.colors.write(writer)
        if self.dark_colors is not None:
            if self.dark_colors is not None and hasattr(self.dark_colors, 'write'): self.dark_colors.write(writer)
        if self.channel_min_level is not None:
            writer.write_int32(self.channel_min_level or 0)
        if self.group_min_level is not None:
            writer.write_int32(self.group_min_level or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPeerColorOption':
        flags = reader.read_uint32()
        hidden = bool(flags & (1 << 0))
        color_id = reader.read_int32()
        colors = reader.read_object() if (flags & (1 << 1)) else None
        dark_colors = reader.read_object() if (flags & (1 << 2)) else None
        channel_min_level = reader.read_int32() if (flags & (1 << 3)) else None
        group_min_level = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(hidden=hidden, color_id=color_id, colors=colors, dark_colors=dark_colors, channel_min_level=channel_min_level, group_min_level=group_min_level)


@register_tl
class HelpPeerColorsNotModified(TLObject):
    ID: int = 0x2ba1f5ce

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPeerColorsNotModified':
        return cls()


@register_tl
class HelpPeerColors(TLObject):
    ID: int = 0xf8ed08

    def __init__(self, hash: Any = None, colors: Any = None) -> None:
        self.hash = hash
        self.colors = colors

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)
        writer.write_vector(self.colors or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpPeerColors':
        hash = reader.read_int32()
        colors = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, colors=colors)


@register_tl
class StoryReaction(TLObject):
    ID: int = 0x6090d6d5

    def __init__(self, peer_id: Any = None, date: Any = None, reaction: Any = None) -> None:
        self.peer_id = peer_id
        self.date = date
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        writer.write_int32(self.date or 0)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryReaction':
        peer_id = reader.read_object()
        date = reader.read_int32()
        reaction = reader.read_object()
        return cls(peer_id=peer_id, date=date, reaction=reaction)


@register_tl
class StoryReactionPublicForward(TLObject):
    ID: int = 0xbbab2643

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryReactionPublicForward':
        message = reader.read_object()
        return cls(message=message)


@register_tl
class StoryReactionPublicRepost(TLObject):
    ID: int = 0xcfcd0f13

    def __init__(self, peer_id: Any = None, story: Any = None) -> None:
        self.peer_id = peer_id
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        if self.story is not None and hasattr(self.story, 'write'): self.story.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryReactionPublicRepost':
        peer_id = reader.read_object()
        story = reader.read_object()
        return cls(peer_id=peer_id, story=story)


@register_tl
class StoriesStoryReactionsList(TLObject):
    ID: int = 0xaa5f789c

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
    def read(cls, reader: TLReader) -> 'StoriesStoryReactionsList':
        flags = reader.read_uint32()
        count = reader.read_int32()
        reactions = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        return cls(count=count, reactions=reactions, chats=chats, users=users, next_offset=next_offset)


@register_tl
class SavedDialog(TLObject):
    ID: int = 0xbd87cb6c

    def __init__(self, pinned: bool = False, peer: Any = None, top_message: Any = None) -> None:
        self.pinned = pinned
        self.peer = peer
        self.top_message = top_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.top_message or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SavedDialog':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 2))
        peer = reader.read_object()
        top_message = reader.read_int32()
        return cls(pinned=pinned, peer=peer, top_message=top_message)


@register_tl
class MonoForumDialog(TLObject):
    ID: int = 0x64407ea7

    def __init__(self, unread_mark: bool = False, nopaid_messages_exception: bool = False, draft: Any = None, peer: Any = None, top_message: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, unread_reactions_count: Any = None) -> None:
        self.unread_mark = unread_mark
        self.nopaid_messages_exception = nopaid_messages_exception
        self.draft = draft
        self.peer = peer
        self.top_message = top_message
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.unread_reactions_count = unread_reactions_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unread_mark:
            flags |= (1 << 3)
        if self.nopaid_messages_exception:
            flags |= (1 << 4)
        if self.draft is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.read_inbox_max_id or 0)
        writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        writer.write_int32(self.unread_reactions_count or 0)
        if self.draft is not None:
            if self.draft is not None and hasattr(self.draft, 'write'): self.draft.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MonoForumDialog':
        flags = reader.read_uint32()
        unread_mark = bool(flags & (1 << 3))
        nopaid_messages_exception = bool(flags & (1 << 4))
        peer = reader.read_object()
        top_message = reader.read_int32()
        read_inbox_max_id = reader.read_int32()
        read_outbox_max_id = reader.read_int32()
        unread_count = reader.read_int32()
        unread_reactions_count = reader.read_int32()
        draft = reader.read_object() if (flags & (1 << 1)) else None
        return cls(unread_mark=unread_mark, nopaid_messages_exception=nopaid_messages_exception, peer=peer, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_reactions_count=unread_reactions_count, draft=draft)


@register_tl
class MessagesSavedDialogs(TLObject):
    ID: int = 0xf83ae221

    def __init__(self, dialogs: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dialogs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavedDialogs':
        dialogs = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(dialogs=dialogs, messages=messages, chats=chats, users=users)


@register_tl
class MessagesSavedDialogsSlice(TLObject):
    ID: int = 0x44ba9dd9

    def __init__(self, count: Any = None, dialogs: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.count = count
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.dialogs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavedDialogsSlice':
        count = reader.read_int32()
        dialogs = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, dialogs=dialogs, messages=messages, chats=chats, users=users)


@register_tl
class MessagesSavedDialogsNotModified(TLObject):
    ID: int = 0xc01f6fe8

    def __init__(self, count: Any = None) -> None:
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavedDialogsNotModified':
        count = reader.read_int32()
        return cls(count=count)


@register_tl
class SavedReactionTag(TLObject):
    ID: int = 0xcb6ff828

    def __init__(self, title: Any = None, reaction: Any = None, count: Any = None) -> None:
        self.title = title
        self.reaction = reaction
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.reaction is not None and hasattr(self.reaction, 'write'): self.reaction.write(writer)
        if self.title is not None:
            writer.write_string(self.title or '')
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SavedReactionTag':
        flags = reader.read_uint32()
        reaction = reader.read_object()
        title = reader.read_string() if (flags & (1 << 0)) else None
        count = reader.read_int32()
        return cls(reaction=reaction, title=title, count=count)


@register_tl
class MessagesSavedReactionTagsNotModified(TLObject):
    ID: int = 0x889b59ef

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavedReactionTagsNotModified':
        return cls()


@register_tl
class MessagesSavedReactionTags(TLObject):
    ID: int = 0x3259950a

    def __init__(self, tags: Any = None, hash: Any = None) -> None:
        self.tags = tags
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.tags or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSavedReactionTags':
        tags = reader.read_vector(lambda r: reader.read_object())
        hash = reader.read_int64()
        return cls(tags=tags, hash=hash)


@register_tl
class OutboxReadDate(TLObject):
    ID: int = 0x3bb842ac

    def __init__(self, date: Any = None) -> None:
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'OutboxReadDate':
        date = reader.read_int32()
        return cls(date=date)


@register_tl
class SmsjobsEligibleToJoin(TLObject):
    ID: int = 0xdc8b44cf

    def __init__(self, terms_url: Any = None, monthly_sent_sms: Any = None) -> None:
        self.terms_url = terms_url
        self.monthly_sent_sms = monthly_sent_sms

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.terms_url or '')
        writer.write_int32(self.monthly_sent_sms or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsEligibleToJoin':
        terms_url = reader.read_string()
        monthly_sent_sms = reader.read_int32()
        return cls(terms_url=terms_url, monthly_sent_sms=monthly_sent_sms)


@register_tl
class SmsjobsStatus(TLObject):
    ID: int = 0x2aee9191

    def __init__(self, allow_international: bool = False, last_gift_slug: Any = None, recent_sent: Any = None, recent_since: Any = None, recent_remains: Any = None, total_sent: Any = None, total_since: Any = None, terms_url: Any = None) -> None:
        self.allow_international = allow_international
        self.last_gift_slug = last_gift_slug
        self.recent_sent = recent_sent
        self.recent_since = recent_since
        self.recent_remains = recent_remains
        self.total_sent = total_sent
        self.total_since = total_since
        self.terms_url = terms_url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.allow_international:
            flags |= (1 << 0)
        if self.last_gift_slug is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.recent_sent or 0)
        writer.write_int32(self.recent_since or 0)
        writer.write_int32(self.recent_remains or 0)
        writer.write_int32(self.total_sent or 0)
        writer.write_int32(self.total_since or 0)
        if self.last_gift_slug is not None:
            writer.write_string(self.last_gift_slug or '')
        writer.write_string(self.terms_url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsjobsStatus':
        flags = reader.read_uint32()
        allow_international = bool(flags & (1 << 0))
        recent_sent = reader.read_int32()
        recent_since = reader.read_int32()
        recent_remains = reader.read_int32()
        total_sent = reader.read_int32()
        total_since = reader.read_int32()
        last_gift_slug = reader.read_string() if (flags & (1 << 1)) else None
        terms_url = reader.read_string()
        return cls(allow_international=allow_international, recent_sent=recent_sent, recent_since=recent_since, recent_remains=recent_remains, total_sent=total_sent, total_since=total_since, last_gift_slug=last_gift_slug, terms_url=terms_url)


@register_tl
class SmsJob(TLObject):
    ID: int = 0xe6a1eeb8

    def __init__(self, job_id: Any = None, phone_number: Any = None, text: Any = None) -> None:
        self.job_id = job_id
        self.phone_number = phone_number
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.job_id or '')
        writer.write_string(self.phone_number or '')
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SmsJob':
        job_id = reader.read_string()
        phone_number = reader.read_string()
        text = reader.read_string()
        return cls(job_id=job_id, phone_number=phone_number, text=text)


@register_tl
class BusinessWeeklyOpen(TLObject):
    ID: int = 0x120b1ab9

    def __init__(self, start_minute: Any = None, end_minute: Any = None) -> None:
        self.start_minute = start_minute
        self.end_minute = end_minute

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.start_minute or 0)
        writer.write_int32(self.end_minute or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessWeeklyOpen':
        start_minute = reader.read_int32()
        end_minute = reader.read_int32()
        return cls(start_minute=start_minute, end_minute=end_minute)


@register_tl
class BusinessWorkHours(TLObject):
    ID: int = 0x8c92b098

    def __init__(self, open_now: bool = False, timezone_id: Any = None, weekly_open: Any = None) -> None:
        self.open_now = open_now
        self.timezone_id = timezone_id
        self.weekly_open = weekly_open

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.open_now:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.timezone_id or '')
        writer.write_vector(self.weekly_open or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessWorkHours':
        flags = reader.read_uint32()
        open_now = bool(flags & (1 << 0))
        timezone_id = reader.read_string()
        weekly_open = reader.read_vector(lambda r: reader.read_object())
        return cls(open_now=open_now, timezone_id=timezone_id, weekly_open=weekly_open)


@register_tl
class BusinessLocation(TLObject):
    ID: int = 0xac5c1af7

    def __init__(self, geo_point: Any = None, address: Any = None) -> None:
        self.geo_point = geo_point
        self.address = address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo_point is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.geo_point is not None:
            if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        writer.write_string(self.address or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessLocation':
        flags = reader.read_uint32()
        geo_point = reader.read_object() if (flags & (1 << 0)) else None
        address = reader.read_string()
        return cls(geo_point=geo_point, address=address)


@register_tl
class InputBusinessRecipients(TLObject):
    ID: int = 0x6f8b32aa

    def __init__(self, existing_chats: bool = False, new_chats: bool = False, contacts: bool = False, non_contacts: bool = False, exclude_selected: bool = False, users: Any = None) -> None:
        self.existing_chats = existing_chats
        self.new_chats = new_chats
        self.contacts = contacts
        self.non_contacts = non_contacts
        self.exclude_selected = exclude_selected
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.existing_chats:
            flags |= (1 << 0)
        if self.new_chats:
            flags |= (1 << 1)
        if self.contacts:
            flags |= (1 << 2)
        if self.non_contacts:
            flags |= (1 << 3)
        if self.exclude_selected:
            flags |= (1 << 5)
        if self.users is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.users is not None:
            writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBusinessRecipients':
        flags = reader.read_uint32()
        existing_chats = bool(flags & (1 << 0))
        new_chats = bool(flags & (1 << 1))
        contacts = bool(flags & (1 << 2))
        non_contacts = bool(flags & (1 << 3))
        exclude_selected = bool(flags & (1 << 5))
        users = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        return cls(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users)


@register_tl
class BusinessRecipients(TLObject):
    ID: int = 0x21108ff7

    def __init__(self, existing_chats: bool = False, new_chats: bool = False, contacts: bool = False, non_contacts: bool = False, exclude_selected: bool = False, users: Any = None) -> None:
        self.existing_chats = existing_chats
        self.new_chats = new_chats
        self.contacts = contacts
        self.non_contacts = non_contacts
        self.exclude_selected = exclude_selected
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.existing_chats:
            flags |= (1 << 0)
        if self.new_chats:
            flags |= (1 << 1)
        if self.contacts:
            flags |= (1 << 2)
        if self.non_contacts:
            flags |= (1 << 3)
        if self.exclude_selected:
            flags |= (1 << 5)
        if self.users is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.users is not None:
            writer.write_vector(self.users or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessRecipients':
        flags = reader.read_uint32()
        existing_chats = bool(flags & (1 << 0))
        new_chats = bool(flags & (1 << 1))
        contacts = bool(flags & (1 << 2))
        non_contacts = bool(flags & (1 << 3))
        exclude_selected = bool(flags & (1 << 5))
        users = reader.read_vector(lambda r: r.read_int64()) if (flags & (1 << 4)) else None
        return cls(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users)


@register_tl
class BusinessAwayMessageScheduleAlways(TLObject):
    ID: int = 0xc9b9e2b9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessAwayMessageScheduleAlways':
        return cls()


@register_tl
class BusinessAwayMessageScheduleOutsideWorkHours(TLObject):
    ID: int = 0xc3f2f501

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessAwayMessageScheduleOutsideWorkHours':
        return cls()


@register_tl
class BusinessAwayMessageScheduleCustom(TLObject):
    ID: int = 0xcc4d9ecc

    def __init__(self, start_date: Any = None, end_date: Any = None) -> None:
        self.start_date = start_date
        self.end_date = end_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.start_date or 0)
        writer.write_int32(self.end_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessAwayMessageScheduleCustom':
        start_date = reader.read_int32()
        end_date = reader.read_int32()
        return cls(start_date=start_date, end_date=end_date)


@register_tl
class InputBusinessGreetingMessage(TLObject):
    ID: int = 0x194cb3b

    def __init__(self, shortcut_id: Any = None, recipients: Any = None, no_activity_days: Any = None) -> None:
        self.shortcut_id = shortcut_id
        self.recipients = recipients
        self.no_activity_days = no_activity_days

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)
        if self.recipients is not None and hasattr(self.recipients, 'write'): self.recipients.write(writer)
        writer.write_int32(self.no_activity_days or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBusinessGreetingMessage':
        shortcut_id = reader.read_int32()
        recipients = reader.read_object()
        no_activity_days = reader.read_int32()
        return cls(shortcut_id=shortcut_id, recipients=recipients, no_activity_days=no_activity_days)


@register_tl
class BusinessGreetingMessage(TLObject):
    ID: int = 0xe519abab

    def __init__(self, shortcut_id: Any = None, recipients: Any = None, no_activity_days: Any = None) -> None:
        self.shortcut_id = shortcut_id
        self.recipients = recipients
        self.no_activity_days = no_activity_days

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)
        if self.recipients is not None and hasattr(self.recipients, 'write'): self.recipients.write(writer)
        writer.write_int32(self.no_activity_days or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessGreetingMessage':
        shortcut_id = reader.read_int32()
        recipients = reader.read_object()
        no_activity_days = reader.read_int32()
        return cls(shortcut_id=shortcut_id, recipients=recipients, no_activity_days=no_activity_days)


@register_tl
class InputBusinessAwayMessage(TLObject):
    ID: int = 0x832175e0

    def __init__(self, offline_only: bool = False, shortcut_id: Any = None, schedule: Any = None, recipients: Any = None) -> None:
        self.offline_only = offline_only
        self.shortcut_id = shortcut_id
        self.schedule = schedule
        self.recipients = recipients

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.offline_only:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.shortcut_id or 0)
        if self.schedule is not None and hasattr(self.schedule, 'write'): self.schedule.write(writer)
        if self.recipients is not None and hasattr(self.recipients, 'write'): self.recipients.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBusinessAwayMessage':
        flags = reader.read_uint32()
        offline_only = bool(flags & (1 << 0))
        shortcut_id = reader.read_int32()
        schedule = reader.read_object()
        recipients = reader.read_object()
        return cls(offline_only=offline_only, shortcut_id=shortcut_id, schedule=schedule, recipients=recipients)


@register_tl
class BusinessAwayMessage(TLObject):
    ID: int = 0xef156a5c

    def __init__(self, offline_only: bool = False, shortcut_id: Any = None, schedule: Any = None, recipients: Any = None) -> None:
        self.offline_only = offline_only
        self.shortcut_id = shortcut_id
        self.schedule = schedule
        self.recipients = recipients

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.offline_only:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.shortcut_id or 0)
        if self.schedule is not None and hasattr(self.schedule, 'write'): self.schedule.write(writer)
        if self.recipients is not None and hasattr(self.recipients, 'write'): self.recipients.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessAwayMessage':
        flags = reader.read_uint32()
        offline_only = bool(flags & (1 << 0))
        shortcut_id = reader.read_int32()
        schedule = reader.read_object()
        recipients = reader.read_object()
        return cls(offline_only=offline_only, shortcut_id=shortcut_id, schedule=schedule, recipients=recipients)


@register_tl
class Timezone(TLObject):
    ID: int = 0xff9289f5

    def __init__(self, id: Any = None, name: Any = None, utc_offset: Any = None) -> None:
        self.id = id
        self.name = name
        self.utc_offset = utc_offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_string(self.name or '')
        writer.write_int32(self.utc_offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Timezone':
        id = reader.read_string()
        name = reader.read_string()
        utc_offset = reader.read_int32()
        return cls(id=id, name=name, utc_offset=utc_offset)


@register_tl
class HelpTimezonesListNotModified(TLObject):
    ID: int = 0x970708cc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpTimezonesListNotModified':
        return cls()


@register_tl
class HelpTimezonesList(TLObject):
    ID: int = 0x7b74ed71

    def __init__(self, timezones: Any = None, hash: Any = None) -> None:
        self.timezones = timezones
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.timezones or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpTimezonesList':
        timezones = reader.read_vector(lambda r: reader.read_object())
        hash = reader.read_int32()
        return cls(timezones=timezones, hash=hash)


@register_tl
class QuickReply(TLObject):
    ID: int = 0x697102b

    def __init__(self, shortcut_id: Any = None, shortcut: Any = None, top_message: Any = None, count: Any = None) -> None:
        self.shortcut_id = shortcut_id
        self.shortcut = shortcut
        self.top_message = top_message
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)
        writer.write_string(self.shortcut or '')
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'QuickReply':
        shortcut_id = reader.read_int32()
        shortcut = reader.read_string()
        top_message = reader.read_int32()
        count = reader.read_int32()
        return cls(shortcut_id=shortcut_id, shortcut=shortcut, top_message=top_message, count=count)


@register_tl
class InputQuickReplyShortcut(TLObject):
    ID: int = 0x24596d41

    def __init__(self, shortcut: Any = None) -> None:
        self.shortcut = shortcut

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.shortcut or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputQuickReplyShortcut':
        shortcut = reader.read_string()
        return cls(shortcut=shortcut)


@register_tl
class InputQuickReplyShortcutId(TLObject):
    ID: int = 0x1190cf1

    def __init__(self, shortcut_id: Any = None) -> None:
        self.shortcut_id = shortcut_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputQuickReplyShortcutId':
        shortcut_id = reader.read_int32()
        return cls(shortcut_id=shortcut_id)


@register_tl
class MessagesQuickReplies(TLObject):
    ID: int = 0xc68d6695

    def __init__(self, quick_replies: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.quick_replies = quick_replies
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.quick_replies or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesQuickReplies':
        quick_replies = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(quick_replies=quick_replies, messages=messages, chats=chats, users=users)


@register_tl
class MessagesQuickRepliesNotModified(TLObject):
    ID: int = 0x5f91eb5b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesQuickRepliesNotModified':
        return cls()


@register_tl
class ConnectedBot(TLObject):
    ID: int = 0xcd64636c

    def __init__(self, bot_id: Any = None, recipients: Any = None, rights: Any = None) -> None:
        self.bot_id = bot_id
        self.recipients = recipients
        self.rights = rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        writer.write_uint32(flags)
        writer.write_int64(self.bot_id or 0)
        if self.recipients is not None and hasattr(self.recipients, 'write'): self.recipients.write(writer)
        if self.rights is not None and hasattr(self.rights, 'write'): self.rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ConnectedBot':
        flags = reader.read_uint32()
        bot_id = reader.read_int64()
        recipients = reader.read_object()
        rights = reader.read_object()
        return cls(bot_id=bot_id, recipients=recipients, rights=rights)


@register_tl
class AccountConnectedBots(TLObject):
    ID: int = 0x17d7f87b

    def __init__(self, connected_bots: Any = None, users: Any = None) -> None:
        self.connected_bots = connected_bots
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.connected_bots or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountConnectedBots':
        connected_bots = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(connected_bots=connected_bots, users=users)


@register_tl
class MessagesDialogFilters(TLObject):
    ID: int = 0x2ad93719

    def __init__(self, tags_enabled: bool = False, filters: Any = None) -> None:
        self.tags_enabled = tags_enabled
        self.filters = filters

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.tags_enabled:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.filters or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogFilters':
        flags = reader.read_uint32()
        tags_enabled = bool(flags & (1 << 0))
        filters = reader.read_vector(lambda r: reader.read_object())
        return cls(tags_enabled=tags_enabled, filters=filters)


@register_tl
class Birthday(TLObject):
    ID: int = 0x6c8e1e06

    def __init__(self, year: Any = None, day: Any = None, month: Any = None) -> None:
        self.year = year
        self.day = day
        self.month = month

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.year is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.day or 0)
        writer.write_int32(self.month or 0)
        if self.year is not None:
            writer.write_int32(self.year or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Birthday':
        flags = reader.read_uint32()
        day = reader.read_int32()
        month = reader.read_int32()
        year = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(day=day, month=month, year=year)


@register_tl
class BotBusinessConnection(TLObject):
    ID: int = 0x8f34b2f5

    def __init__(self, disabled: bool = False, rights: Any = None, connection_id: Any = None, user_id: Any = None, dc_id: Any = None, date: Any = None) -> None:
        self.disabled = disabled
        self.rights = rights
        self.connection_id = connection_id
        self.user_id = user_id
        self.dc_id = dc_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.disabled:
            flags |= (1 << 1)
        if self.rights is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.connection_id or '')
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.dc_id or 0)
        writer.write_int32(self.date or 0)
        if self.rights is not None:
            if self.rights is not None and hasattr(self.rights, 'write'): self.rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotBusinessConnection':
        flags = reader.read_uint32()
        disabled = bool(flags & (1 << 1))
        connection_id = reader.read_string()
        user_id = reader.read_int64()
        dc_id = reader.read_int32()
        date = reader.read_int32()
        rights = reader.read_object() if (flags & (1 << 2)) else None
        return cls(disabled=disabled, connection_id=connection_id, user_id=user_id, dc_id=dc_id, date=date, rights=rights)


@register_tl
class InputBusinessIntro(TLObject):
    ID: int = 0x9c469cd

    def __init__(self, sticker: Any = None, title: Any = None, description: Any = None) -> None:
        self.sticker = sticker
        self.title = title
        self.description = description

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sticker is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.sticker is not None:
            if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBusinessIntro':
        flags = reader.read_uint32()
        title = reader.read_string()
        description = reader.read_string()
        sticker = reader.read_object() if (flags & (1 << 0)) else None
        return cls(title=title, description=description, sticker=sticker)


@register_tl
class BusinessIntro(TLObject):
    ID: int = 0x5a0a066d

    def __init__(self, sticker: Any = None, title: Any = None, description: Any = None) -> None:
        self.sticker = sticker
        self.title = title
        self.description = description

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sticker is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.sticker is not None:
            if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessIntro':
        flags = reader.read_uint32()
        title = reader.read_string()
        description = reader.read_string()
        sticker = reader.read_object() if (flags & (1 << 0)) else None
        return cls(title=title, description=description, sticker=sticker)


@register_tl
class MessagesMyStickers(TLObject):
    ID: int = 0xfaff629d

    def __init__(self, count: Any = None, sets: Any = None) -> None:
        self.count = count
        self.sets = sets

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.sets or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMyStickers':
        count = reader.read_int32()
        sets = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, sets=sets)


@register_tl
class InputCollectibleUsername(TLObject):
    ID: int = 0xe39460a9

    def __init__(self, username: Any = None) -> None:
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputCollectibleUsername':
        username = reader.read_string()
        return cls(username=username)


@register_tl
class InputCollectiblePhone(TLObject):
    ID: int = 0xa2e214a4

    def __init__(self, phone: Any = None) -> None:
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputCollectiblePhone':
        phone = reader.read_string()
        return cls(phone=phone)


@register_tl
class FragmentCollectibleInfo(TLObject):
    ID: int = 0x6ebdff91

    def __init__(self, purchase_date: Any = None, currency: Any = None, amount: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, url: Any = None) -> None:
        self.purchase_date = purchase_date
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.purchase_date or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        writer.write_string(self.crypto_currency or '')
        writer.write_int64(self.crypto_amount or 0)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'FragmentCollectibleInfo':
        purchase_date = reader.read_int32()
        currency = reader.read_string()
        amount = reader.read_int64()
        crypto_currency = reader.read_string()
        crypto_amount = reader.read_int64()
        url = reader.read_string()
        return cls(purchase_date=purchase_date, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, url=url)


@register_tl
class InputBusinessBotRecipients(TLObject):
    ID: int = 0xc4e5921e

    def __init__(self, existing_chats: bool = False, new_chats: bool = False, contacts: bool = False, non_contacts: bool = False, exclude_selected: bool = False, users: Any = None, exclude_users: Any = None) -> None:
        self.existing_chats = existing_chats
        self.new_chats = new_chats
        self.contacts = contacts
        self.non_contacts = non_contacts
        self.exclude_selected = exclude_selected
        self.users = users
        self.exclude_users = exclude_users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.existing_chats:
            flags |= (1 << 0)
        if self.new_chats:
            flags |= (1 << 1)
        if self.contacts:
            flags |= (1 << 2)
        if self.non_contacts:
            flags |= (1 << 3)
        if self.exclude_selected:
            flags |= (1 << 5)
        if self.users is not None:
            flags |= (1 << 4)
        if self.exclude_users is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        if self.users is not None:
            writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.exclude_users is not None:
            writer.write_vector(self.exclude_users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBusinessBotRecipients':
        flags = reader.read_uint32()
        existing_chats = bool(flags & (1 << 0))
        new_chats = bool(flags & (1 << 1))
        contacts = bool(flags & (1 << 2))
        non_contacts = bool(flags & (1 << 3))
        exclude_selected = bool(flags & (1 << 5))
        users = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        exclude_users = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 6)) else None
        return cls(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users, exclude_users=exclude_users)


@register_tl
class BusinessBotRecipients(TLObject):
    ID: int = 0xb88cf373

    def __init__(self, existing_chats: bool = False, new_chats: bool = False, contacts: bool = False, non_contacts: bool = False, exclude_selected: bool = False, users: Any = None, exclude_users: Any = None) -> None:
        self.existing_chats = existing_chats
        self.new_chats = new_chats
        self.contacts = contacts
        self.non_contacts = non_contacts
        self.exclude_selected = exclude_selected
        self.users = users
        self.exclude_users = exclude_users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.existing_chats:
            flags |= (1 << 0)
        if self.new_chats:
            flags |= (1 << 1)
        if self.contacts:
            flags |= (1 << 2)
        if self.non_contacts:
            flags |= (1 << 3)
        if self.exclude_selected:
            flags |= (1 << 5)
        if self.users is not None:
            flags |= (1 << 4)
        if self.exclude_users is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        if self.users is not None:
            writer.write_vector(self.users or [], lambda w, x: w.write_int64(x))
        if self.exclude_users is not None:
            writer.write_vector(self.exclude_users or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessBotRecipients':
        flags = reader.read_uint32()
        existing_chats = bool(flags & (1 << 0))
        new_chats = bool(flags & (1 << 1))
        contacts = bool(flags & (1 << 2))
        non_contacts = bool(flags & (1 << 3))
        exclude_selected = bool(flags & (1 << 5))
        users = reader.read_vector(lambda r: r.read_int64()) if (flags & (1 << 4)) else None
        exclude_users = reader.read_vector(lambda r: r.read_int64()) if (flags & (1 << 6)) else None
        return cls(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users, exclude_users=exclude_users)


@register_tl
class ContactBirthday(TLObject):
    ID: int = 0x1d998733

    def __init__(self, contact_id: Any = None, birthday: Any = None) -> None:
        self.contact_id = contact_id
        self.birthday = birthday

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.contact_id or 0)
        if self.birthday is not None and hasattr(self.birthday, 'write'): self.birthday.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactBirthday':
        contact_id = reader.read_int64()
        birthday = reader.read_object()
        return cls(contact_id=contact_id, birthday=birthday)


@register_tl
class ContactsContactBirthdays(TLObject):
    ID: int = 0x114ff30d

    def __init__(self, contacts: Any = None, users: Any = None) -> None:
        self.contacts = contacts
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.contacts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsContactBirthdays':
        contacts = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(contacts=contacts, users=users)


@register_tl
class MissingInvitee(TLObject):
    ID: int = 0x628c9224

    def __init__(self, premium_would_allow_invite: bool = False, premium_required_for_pm: bool = False, user_id: Any = None) -> None:
        self.premium_would_allow_invite = premium_would_allow_invite
        self.premium_required_for_pm = premium_required_for_pm
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.premium_would_allow_invite:
            flags |= (1 << 0)
        if self.premium_required_for_pm:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MissingInvitee':
        flags = reader.read_uint32()
        premium_would_allow_invite = bool(flags & (1 << 0))
        premium_required_for_pm = bool(flags & (1 << 1))
        user_id = reader.read_int64()
        return cls(premium_would_allow_invite=premium_would_allow_invite, premium_required_for_pm=premium_required_for_pm, user_id=user_id)


@register_tl
class MessagesInvitedUsers(TLObject):
    ID: int = 0x7f5defa6

    def __init__(self, updates: Any = None, missing_invitees: Any = None) -> None:
        self.updates = updates
        self.missing_invitees = missing_invitees

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.updates is not None and hasattr(self.updates, 'write'): self.updates.write(writer)
        writer.write_vector(self.missing_invitees or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesInvitedUsers':
        updates = reader.read_object()
        missing_invitees = reader.read_vector(lambda r: reader.read_object())
        return cls(updates=updates, missing_invitees=missing_invitees)


@register_tl
class InputBusinessChatLink(TLObject):
    ID: int = 0x11679fa7

    def __init__(self, entities: Any = None, title: Any = None, message: Any = None) -> None:
        self.entities = entities
        self.title = title
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.entities is not None:
            flags |= (1 << 0)
        if self.title is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.title is not None:
            writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputBusinessChatLink':
        flags = reader.read_uint32()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        title = reader.read_string() if (flags & (1 << 1)) else None
        return cls(message=message, entities=entities, title=title)


@register_tl
class BusinessChatLink(TLObject):
    ID: int = 0xb4ae666f

    def __init__(self, entities: Any = None, title: Any = None, link: Any = None, message: Any = None, views: Any = None) -> None:
        self.entities = entities
        self.title = title
        self.link = link
        self.message = message
        self.views = views

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.entities is not None:
            flags |= (1 << 0)
        if self.title is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.link or '')
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.title is not None:
            writer.write_string(self.title or '')
        writer.write_int32(self.views or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessChatLink':
        flags = reader.read_uint32()
        link = reader.read_string()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        title = reader.read_string() if (flags & (1 << 1)) else None
        views = reader.read_int32()
        return cls(link=link, message=message, entities=entities, title=title, views=views)


@register_tl
class AccountBusinessChatLinks(TLObject):
    ID: int = 0xec43a2d1

    def __init__(self, links: Any = None, chats: Any = None, users: Any = None) -> None:
        self.links = links
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.links or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountBusinessChatLinks':
        links = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(links=links, chats=chats, users=users)


@register_tl
class AccountResolvedBusinessChatLinks(TLObject):
    ID: int = 0x9a23af21

    def __init__(self, entities: Any = None, peer: Any = None, message: Any = None, chats: Any = None, users: Any = None) -> None:
        self.entities = entities
        self.peer = peer
        self.message = message
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.entities is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.message or '')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResolvedBusinessChatLinks':
        flags = reader.read_uint32()
        peer = reader.read_object()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, message=message, entities=entities, chats=chats, users=users)


@register_tl
class RequestedPeerUser(TLObject):
    ID: int = 0xd62ff46a

    def __init__(self, first_name: Any = None, last_name: Any = None, username: Any = None, photo: Any = None, user_id: Any = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.first_name is not None:
            flags |= (1 << 0)
        if self.last_name is not None:
            flags |= (1 << 0)
        if self.username is not None:
            flags |= (1 << 1)
        if self.photo is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.first_name is not None:
            writer.write_string(self.first_name or '')
        if self.last_name is not None:
            writer.write_string(self.last_name or '')
        if self.username is not None:
            writer.write_string(self.username or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequestedPeerUser':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        first_name = reader.read_string() if (flags & (1 << 0)) else None
        last_name = reader.read_string() if (flags & (1 << 0)) else None
        username = reader.read_string() if (flags & (1 << 1)) else None
        photo = reader.read_object() if (flags & (1 << 2)) else None
        return cls(user_id=user_id, first_name=first_name, last_name=last_name, username=username, photo=photo)


@register_tl
class RequestedPeerChat(TLObject):
    ID: int = 0x7307544f

    def __init__(self, title: Any = None, photo: Any = None, chat_id: Any = None) -> None:
        self.title = title
        self.photo = photo
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        if self.photo is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.chat_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequestedPeerChat':
        flags = reader.read_uint32()
        chat_id = reader.read_int64()
        title = reader.read_string() if (flags & (1 << 0)) else None
        photo = reader.read_object() if (flags & (1 << 2)) else None
        return cls(chat_id=chat_id, title=title, photo=photo)


@register_tl
class RequestedPeerChannel(TLObject):
    ID: int = 0x8ba403e4

    def __init__(self, title: Any = None, username: Any = None, photo: Any = None, channel_id: Any = None) -> None:
        self.title = title
        self.username = username
        self.photo = photo
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        if self.username is not None:
            flags |= (1 << 1)
        if self.photo is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.username is not None:
            writer.write_string(self.username or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequestedPeerChannel':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        title = reader.read_string() if (flags & (1 << 0)) else None
        username = reader.read_string() if (flags & (1 << 1)) else None
        photo = reader.read_object() if (flags & (1 << 2)) else None
        return cls(channel_id=channel_id, title=title, username=username, photo=photo)


@register_tl
class SponsoredMessageReportOption(TLObject):
    ID: int = 0x430d3150

    def __init__(self, text: Any = None, option: Any = None) -> None:
        self.text = text
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_bytes(self.option or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SponsoredMessageReportOption':
        text = reader.read_string()
        option = reader.read_bytes()
        return cls(text=text, option=option)


@register_tl
class ChannelsSponsoredMessageReportResultChooseOption(TLObject):
    ID: int = 0x846f9e42

    def __init__(self, title: Any = None, options: Any = None) -> None:
        self.title = title
        self.options = options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_vector(self.options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSponsoredMessageReportResultChooseOption':
        title = reader.read_string()
        options = reader.read_vector(lambda r: reader.read_object())
        return cls(title=title, options=options)


@register_tl
class ChannelsSponsoredMessageReportResultAdsHidden(TLObject):
    ID: int = 0x3e3bcf2f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSponsoredMessageReportResultAdsHidden':
        return cls()


@register_tl
class ChannelsSponsoredMessageReportResultReported(TLObject):
    ID: int = 0xad798849

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSponsoredMessageReportResultReported':
        return cls()


@register_tl
class ReactionNotificationsFromContacts(TLObject):
    ID: int = 0xbac3a61a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionNotificationsFromContacts':
        return cls()


@register_tl
class ReactionNotificationsFromAll(TLObject):
    ID: int = 0x4b9e22a0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionNotificationsFromAll':
        return cls()


@register_tl
class ReactionsNotifySettings(TLObject):
    ID: int = 0x71e4ea58

    def __init__(self, messages_notify_from: Any = None, stories_notify_from: Any = None, poll_votes_notify_from: Any = None, sound: Any = None, show_previews: Any = None) -> None:
        self.messages_notify_from = messages_notify_from
        self.stories_notify_from = stories_notify_from
        self.poll_votes_notify_from = poll_votes_notify_from
        self.sound = sound
        self.show_previews = show_previews

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.messages_notify_from is not None:
            flags |= (1 << 0)
        if self.stories_notify_from is not None:
            flags |= (1 << 1)
        if self.poll_votes_notify_from is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.messages_notify_from is not None:
            if self.messages_notify_from is not None and hasattr(self.messages_notify_from, 'write'): self.messages_notify_from.write(writer)
        if self.stories_notify_from is not None:
            if self.stories_notify_from is not None and hasattr(self.stories_notify_from, 'write'): self.stories_notify_from.write(writer)
        if self.poll_votes_notify_from is not None:
            if self.poll_votes_notify_from is not None and hasattr(self.poll_votes_notify_from, 'write'): self.poll_votes_notify_from.write(writer)
        if self.sound is not None and hasattr(self.sound, 'write'): self.sound.write(writer)
        writer.write_bool(bool(self.show_previews))

    @classmethod
    def read(cls, reader: TLReader) -> 'ReactionsNotifySettings':
        flags = reader.read_uint32()
        messages_notify_from = reader.read_object() if (flags & (1 << 0)) else None
        stories_notify_from = reader.read_object() if (flags & (1 << 1)) else None
        poll_votes_notify_from = reader.read_object() if (flags & (1 << 2)) else None
        sound = reader.read_object()
        show_previews = reader.read_bool()
        return cls(messages_notify_from=messages_notify_from, stories_notify_from=stories_notify_from, poll_votes_notify_from=poll_votes_notify_from, sound=sound, show_previews=show_previews)


@register_tl
class AvailableEffect(TLObject):
    ID: int = 0x93c3e27e

    def __init__(self, premium_required: bool = False, static_icon_id: Any = None, effect_animation_id: Any = None, id: Any = None, emoticon: Any = None, effect_sticker_id: Any = None) -> None:
        self.premium_required = premium_required
        self.static_icon_id = static_icon_id
        self.effect_animation_id = effect_animation_id
        self.id = id
        self.emoticon = emoticon
        self.effect_sticker_id = effect_sticker_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.premium_required:
            flags |= (1 << 2)
        if self.static_icon_id is not None:
            flags |= (1 << 0)
        if self.effect_animation_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(self.emoticon or '')
        if self.static_icon_id is not None:
            writer.write_int64(self.static_icon_id or 0)
        writer.write_int64(self.effect_sticker_id or 0)
        if self.effect_animation_id is not None:
            writer.write_int64(self.effect_animation_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AvailableEffect':
        flags = reader.read_uint32()
        premium_required = bool(flags & (1 << 2))
        id = reader.read_int64()
        emoticon = reader.read_string()
        static_icon_id = reader.read_int64() if (flags & (1 << 0)) else None
        effect_sticker_id = reader.read_int64()
        effect_animation_id = reader.read_int64() if (flags & (1 << 1)) else None
        return cls(premium_required=premium_required, id=id, emoticon=emoticon, static_icon_id=static_icon_id, effect_sticker_id=effect_sticker_id, effect_animation_id=effect_animation_id)


@register_tl
class MessagesAvailableEffectsNotModified(TLObject):
    ID: int = 0xd1ed9a5b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAvailableEffectsNotModified':
        return cls()


@register_tl
class MessagesAvailableEffects(TLObject):
    ID: int = 0xbddb616e

    def __init__(self, hash: Any = None, effects: Any = None, documents: Any = None) -> None:
        self.hash = hash
        self.effects = effects
        self.documents = documents

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)
        writer.write_vector(self.effects or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAvailableEffects':
        hash = reader.read_int32()
        effects = reader.read_vector(lambda r: reader.read_object())
        documents = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, effects=effects, documents=documents)


@register_tl
class FactCheck(TLObject):
    ID: int = 0xb89bfccf

    def __init__(self, need_check: bool = False, country: Any = None, text: Any = None, hash: Any = None) -> None:
        self.need_check = need_check
        self.country = country
        self.text = text
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.need_check:
            flags |= (1 << 0)
        if self.country is not None:
            flags |= (1 << 1)
        if self.text is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.country is not None:
            writer.write_string(self.country or '')
        if self.text is not None:
            if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'FactCheck':
        flags = reader.read_uint32()
        need_check = bool(flags & (1 << 0))
        country = reader.read_string() if (flags & (1 << 1)) else None
        text = reader.read_object() if (flags & (1 << 1)) else None
        hash = reader.read_int64()
        return cls(need_check=need_check, country=country, text=text, hash=hash)


@register_tl
class StarsTransactionPeerUnsupported(TLObject):
    ID: int = 0x95f2bfe4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeerUnsupported':
        return cls()


@register_tl
class StarsTransactionPeerAppStore(TLObject):
    ID: int = 0xb457b375

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeerAppStore':
        return cls()


@register_tl
class StarsTransactionPeerPlayMarket(TLObject):
    ID: int = 0x7b560a0b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeerPlayMarket':
        return cls()


@register_tl
class StarsTransactionPeerPremiumBot(TLObject):
    ID: int = 0x250dbaf8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeerPremiumBot':
        return cls()


@register_tl
class StarsTransactionPeerFragment(TLObject):
    ID: int = 0xe92fd902

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeerFragment':
        return cls()


@register_tl
class StarsTransactionPeer(TLObject):
    ID: int = 0xd80da15d

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeer':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class StarsTransactionPeerAds(TLObject):
    ID: int = 0x60682812

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeerAds':
        return cls()


@register_tl
class StarsTransactionPeerAPI(TLObject):
    ID: int = 0xf9677aad

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransactionPeerAPI':
        return cls()


@register_tl
class StarsTopupOption(TLObject):
    ID: int = 0xbd915c0

    def __init__(self, extended: bool = False, store_product: Any = None, stars: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.extended = extended
        self.store_product = store_product
        self.stars = stars
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.extended:
            flags |= (1 << 1)
        if self.store_product is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)
        if self.store_product is not None:
            writer.write_string(self.store_product or '')
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTopupOption':
        flags = reader.read_uint32()
        extended = bool(flags & (1 << 1))
        stars = reader.read_int64()
        store_product = reader.read_string() if (flags & (1 << 0)) else None
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(extended=extended, stars=stars, store_product=store_product, currency=currency, amount=amount)

