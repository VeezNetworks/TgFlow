from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class StarsTransaction(TLObject):
    ID: int = 0x13659eb0

    def __init__(self, refund: bool = False, pending: bool = False, failed: bool = False, gift: bool = False, reaction: bool = False, stargift_upgrade: bool = False, business_transfer: bool = False, stargift_resale: bool = False, posts_search: bool = False, stargift_prepaid_upgrade: bool = False, stargift_drop_original_details: bool = False, phonegroup_message: bool = False, stargift_auction_bid: bool = False, offer: bool = False, title: Any = None, description: Any = None, photo: Any = None, transaction_date: Any = None, transaction_url: Any = None, bot_payload: Any = None, msg_id: Any = None, extended_media: Any = None, subscription_period: Any = None, giveaway_post_id: Any = None, stargift: Any = None, floodskip_number: Any = None, starref_commission_permille: Any = None, starref_peer: Any = None, starref_amount: Any = None, paid_messages: Any = None, premium_gift_months: Any = None, ads_proceeds_from_date: Any = None, ads_proceeds_to_date: Any = None, id: Any = None, amount: Any = None, date: Any = None, peer: Any = None) -> None:
        self.refund = refund
        self.pending = pending
        self.failed = failed
        self.gift = gift
        self.reaction = reaction
        self.stargift_upgrade = stargift_upgrade
        self.business_transfer = business_transfer
        self.stargift_resale = stargift_resale
        self.posts_search = posts_search
        self.stargift_prepaid_upgrade = stargift_prepaid_upgrade
        self.stargift_drop_original_details = stargift_drop_original_details
        self.phonegroup_message = phonegroup_message
        self.stargift_auction_bid = stargift_auction_bid
        self.offer = offer
        self.title = title
        self.description = description
        self.photo = photo
        self.transaction_date = transaction_date
        self.transaction_url = transaction_url
        self.bot_payload = bot_payload
        self.msg_id = msg_id
        self.extended_media = extended_media
        self.subscription_period = subscription_period
        self.giveaway_post_id = giveaway_post_id
        self.stargift = stargift
        self.floodskip_number = floodskip_number
        self.starref_commission_permille = starref_commission_permille
        self.starref_peer = starref_peer
        self.starref_amount = starref_amount
        self.paid_messages = paid_messages
        self.premium_gift_months = premium_gift_months
        self.ads_proceeds_from_date = ads_proceeds_from_date
        self.ads_proceeds_to_date = ads_proceeds_to_date
        self.id = id
        self.amount = amount
        self.date = date
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.refund:
            flags |= (1 << 3)
        if self.pending:
            flags |= (1 << 4)
        if self.failed:
            flags |= (1 << 6)
        if self.gift:
            flags |= (1 << 10)
        if self.reaction:
            flags |= (1 << 11)
        if self.stargift_upgrade:
            flags |= (1 << 18)
        if self.business_transfer:
            flags |= (1 << 21)
        if self.stargift_resale:
            flags |= (1 << 22)
        if self.posts_search:
            flags |= (1 << 24)
        if self.stargift_prepaid_upgrade:
            flags |= (1 << 25)
        if self.stargift_drop_original_details:
            flags |= (1 << 26)
        if self.phonegroup_message:
            flags |= (1 << 27)
        if self.stargift_auction_bid:
            flags |= (1 << 28)
        if self.offer:
            flags |= (1 << 29)
        if self.title is not None:
            flags |= (1 << 0)
        if self.description is not None:
            flags |= (1 << 1)
        if self.photo is not None:
            flags |= (1 << 2)
        if self.transaction_date is not None:
            flags |= (1 << 5)
        if self.transaction_url is not None:
            flags |= (1 << 5)
        if self.bot_payload is not None:
            flags |= (1 << 7)
        if self.msg_id is not None:
            flags |= (1 << 8)
        if self.extended_media is not None:
            flags |= (1 << 9)
        if self.subscription_period is not None:
            flags |= (1 << 12)
        if self.giveaway_post_id is not None:
            flags |= (1 << 13)
        if self.stargift is not None:
            flags |= (1 << 14)
        if self.floodskip_number is not None:
            flags |= (1 << 15)
        if self.starref_commission_permille is not None:
            flags |= (1 << 16)
        if self.starref_peer is not None:
            flags |= (1 << 17)
        if self.starref_amount is not None:
            flags |= (1 << 17)
        if self.paid_messages is not None:
            flags |= (1 << 19)
        if self.premium_gift_months is not None:
            flags |= (1 << 20)
        if self.ads_proceeds_from_date is not None:
            flags |= (1 << 23)
        if self.ads_proceeds_to_date is not None:
            flags |= (1 << 23)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        if self.amount is not None and hasattr(self.amount, 'write'): self.amount.write(writer)
        writer.write_int32(self.date or 0)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.transaction_date is not None:
            writer.write_int32(self.transaction_date or 0)
        if self.transaction_url is not None:
            writer.write_string(self.transaction_url or '')
        if self.bot_payload is not None:
            writer.write_bytes(self.bot_payload or b'')
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.extended_media is not None:
            writer.write_vector(self.extended_media or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.subscription_period is not None:
            writer.write_int32(self.subscription_period or 0)
        if self.giveaway_post_id is not None:
            writer.write_int32(self.giveaway_post_id or 0)
        if self.stargift is not None:
            if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)
        if self.floodskip_number is not None:
            writer.write_int32(self.floodskip_number or 0)
        if self.starref_commission_permille is not None:
            writer.write_int32(self.starref_commission_permille or 0)
        if self.starref_peer is not None:
            if self.starref_peer is not None and hasattr(self.starref_peer, 'write'): self.starref_peer.write(writer)
        if self.starref_amount is not None:
            if self.starref_amount is not None and hasattr(self.starref_amount, 'write'): self.starref_amount.write(writer)
        if self.paid_messages is not None:
            writer.write_int32(self.paid_messages or 0)
        if self.premium_gift_months is not None:
            writer.write_int32(self.premium_gift_months or 0)
        if self.ads_proceeds_from_date is not None:
            writer.write_int32(self.ads_proceeds_from_date or 0)
        if self.ads_proceeds_to_date is not None:
            writer.write_int32(self.ads_proceeds_to_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTransaction':
        flags = reader.read_uint32()
        refund = bool(flags & (1 << 3))
        pending = bool(flags & (1 << 4))
        failed = bool(flags & (1 << 6))
        gift = bool(flags & (1 << 10))
        reaction = bool(flags & (1 << 11))
        stargift_upgrade = bool(flags & (1 << 18))
        business_transfer = bool(flags & (1 << 21))
        stargift_resale = bool(flags & (1 << 22))
        posts_search = bool(flags & (1 << 24))
        stargift_prepaid_upgrade = bool(flags & (1 << 25))
        stargift_drop_original_details = bool(flags & (1 << 26))
        phonegroup_message = bool(flags & (1 << 27))
        stargift_auction_bid = bool(flags & (1 << 28))
        offer = bool(flags & (1 << 29))
        id = reader.read_string()
        amount = reader.read_object()
        date = reader.read_int32()
        peer = reader.read_object()
        title = reader.read_string() if (flags & (1 << 0)) else None
        description = reader.read_string() if (flags & (1 << 1)) else None
        photo = reader.read_object() if (flags & (1 << 2)) else None
        transaction_date = reader.read_int32() if (flags & (1 << 5)) else None
        transaction_url = reader.read_string() if (flags & (1 << 5)) else None
        bot_payload = reader.read_bytes() if (flags & (1 << 7)) else None
        msg_id = reader.read_int32() if (flags & (1 << 8)) else None
        extended_media = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 9)) else None
        subscription_period = reader.read_int32() if (flags & (1 << 12)) else None
        giveaway_post_id = reader.read_int32() if (flags & (1 << 13)) else None
        stargift = reader.read_object() if (flags & (1 << 14)) else None
        floodskip_number = reader.read_int32() if (flags & (1 << 15)) else None
        starref_commission_permille = reader.read_int32() if (flags & (1 << 16)) else None
        starref_peer = reader.read_object() if (flags & (1 << 17)) else None
        starref_amount = reader.read_object() if (flags & (1 << 17)) else None
        paid_messages = reader.read_int32() if (flags & (1 << 19)) else None
        premium_gift_months = reader.read_int32() if (flags & (1 << 20)) else None
        ads_proceeds_from_date = reader.read_int32() if (flags & (1 << 23)) else None
        ads_proceeds_to_date = reader.read_int32() if (flags & (1 << 23)) else None
        return cls(refund=refund, pending=pending, failed=failed, gift=gift, reaction=reaction, stargift_upgrade=stargift_upgrade, business_transfer=business_transfer, stargift_resale=stargift_resale, posts_search=posts_search, stargift_prepaid_upgrade=stargift_prepaid_upgrade, stargift_drop_original_details=stargift_drop_original_details, phonegroup_message=phonegroup_message, stargift_auction_bid=stargift_auction_bid, offer=offer, id=id, amount=amount, date=date, peer=peer, title=title, description=description, photo=photo, transaction_date=transaction_date, transaction_url=transaction_url, bot_payload=bot_payload, msg_id=msg_id, extended_media=extended_media, subscription_period=subscription_period, giveaway_post_id=giveaway_post_id, stargift=stargift, floodskip_number=floodskip_number, starref_commission_permille=starref_commission_permille, starref_peer=starref_peer, starref_amount=starref_amount, paid_messages=paid_messages, premium_gift_months=premium_gift_months, ads_proceeds_from_date=ads_proceeds_from_date, ads_proceeds_to_date=ads_proceeds_to_date)


@register_tl
class PaymentsStarsStatus(TLObject):
    ID: int = 0x6c9ce8ed

    def __init__(self, subscriptions: Any = None, subscriptions_next_offset: Any = None, subscriptions_missing_balance: Any = None, history: Any = None, next_offset: Any = None, balance: Any = None, chats: Any = None, users: Any = None) -> None:
        self.subscriptions = subscriptions
        self.subscriptions_next_offset = subscriptions_next_offset
        self.subscriptions_missing_balance = subscriptions_missing_balance
        self.history = history
        self.next_offset = next_offset
        self.balance = balance
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.subscriptions is not None:
            flags |= (1 << 1)
        if self.subscriptions_next_offset is not None:
            flags |= (1 << 2)
        if self.subscriptions_missing_balance is not None:
            flags |= (1 << 4)
        if self.history is not None:
            flags |= (1 << 3)
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.balance is not None and hasattr(self.balance, 'write'): self.balance.write(writer)
        if self.subscriptions is not None:
            writer.write_vector(self.subscriptions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.subscriptions_next_offset is not None:
            writer.write_string(self.subscriptions_next_offset or '')
        if self.subscriptions_missing_balance is not None:
            writer.write_int64(self.subscriptions_missing_balance or 0)
        if self.history is not None:
            writer.write_vector(self.history or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarsStatus':
        flags = reader.read_uint32()
        balance = reader.read_object()
        subscriptions = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        subscriptions_next_offset = reader.read_string() if (flags & (1 << 2)) else None
        subscriptions_missing_balance = reader.read_int64() if (flags & (1 << 4)) else None
        history = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(balance=balance, subscriptions=subscriptions, subscriptions_next_offset=subscriptions_next_offset, subscriptions_missing_balance=subscriptions_missing_balance, history=history, next_offset=next_offset, chats=chats, users=users)


@register_tl
class FoundStory(TLObject):
    ID: int = 0xe87acbc0

    def __init__(self, peer: Any = None, story: Any = None) -> None:
        self.peer = peer
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.story is not None and hasattr(self.story, 'write'): self.story.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'FoundStory':
        peer = reader.read_object()
        story = reader.read_object()
        return cls(peer=peer, story=story)


@register_tl
class StoriesFoundStories(TLObject):
    ID: int = 0xe2de7737

    def __init__(self, next_offset: Any = None, count: Any = None, stories: Any = None, chats: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.count = count
        self.stories = stories
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.stories or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesFoundStories':
        flags = reader.read_uint32()
        count = reader.read_int32()
        stories = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, stories=stories, next_offset=next_offset, chats=chats, users=users)


@register_tl
class GeoPointAddress(TLObject):
    ID: int = 0xde4c5d93

    def __init__(self, state: Any = None, city: Any = None, street: Any = None, country_iso2: Any = None) -> None:
        self.state = state
        self.city = city
        self.street = street
        self.country_iso2 = country_iso2

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.state is not None:
            flags |= (1 << 0)
        if self.city is not None:
            flags |= (1 << 1)
        if self.street is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.country_iso2 or '')
        if self.state is not None:
            writer.write_string(self.state or '')
        if self.city is not None:
            writer.write_string(self.city or '')
        if self.street is not None:
            writer.write_string(self.street or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'GeoPointAddress':
        flags = reader.read_uint32()
        country_iso2 = reader.read_string()
        state = reader.read_string() if (flags & (1 << 0)) else None
        city = reader.read_string() if (flags & (1 << 1)) else None
        street = reader.read_string() if (flags & (1 << 2)) else None
        return cls(country_iso2=country_iso2, state=state, city=city, street=street)


@register_tl
class StarsRevenueStatus(TLObject):
    ID: int = 0xfebe5491

    def __init__(self, withdrawal_enabled: bool = False, next_withdrawal_at: Any = None, current_balance: Any = None, available_balance: Any = None, overall_revenue: Any = None) -> None:
        self.withdrawal_enabled = withdrawal_enabled
        self.next_withdrawal_at = next_withdrawal_at
        self.current_balance = current_balance
        self.available_balance = available_balance
        self.overall_revenue = overall_revenue

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.withdrawal_enabled:
            flags |= (1 << 0)
        if self.next_withdrawal_at is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.current_balance is not None and hasattr(self.current_balance, 'write'): self.current_balance.write(writer)
        if self.available_balance is not None and hasattr(self.available_balance, 'write'): self.available_balance.write(writer)
        if self.overall_revenue is not None and hasattr(self.overall_revenue, 'write'): self.overall_revenue.write(writer)
        if self.next_withdrawal_at is not None:
            writer.write_int32(self.next_withdrawal_at or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsRevenueStatus':
        flags = reader.read_uint32()
        withdrawal_enabled = bool(flags & (1 << 0))
        current_balance = reader.read_object()
        available_balance = reader.read_object()
        overall_revenue = reader.read_object()
        next_withdrawal_at = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(withdrawal_enabled=withdrawal_enabled, current_balance=current_balance, available_balance=available_balance, overall_revenue=overall_revenue, next_withdrawal_at=next_withdrawal_at)


@register_tl
class PaymentsStarsRevenueStats(TLObject):
    ID: int = 0x6c207376

    def __init__(self, top_hours_graph: Any = None, revenue_graph: Any = None, status: Any = None, usd_rate: Any = None) -> None:
        self.top_hours_graph = top_hours_graph
        self.revenue_graph = revenue_graph
        self.status = status
        self.usd_rate = usd_rate

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_hours_graph is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.top_hours_graph is not None:
            if self.top_hours_graph is not None and hasattr(self.top_hours_graph, 'write'): self.top_hours_graph.write(writer)
        if self.revenue_graph is not None and hasattr(self.revenue_graph, 'write'): self.revenue_graph.write(writer)
        if self.status is not None and hasattr(self.status, 'write'): self.status.write(writer)
        writer.write_double(self.usd_rate or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarsRevenueStats':
        flags = reader.read_uint32()
        top_hours_graph = reader.read_object() if (flags & (1 << 0)) else None
        revenue_graph = reader.read_object()
        status = reader.read_object()
        usd_rate = reader.read_double()
        return cls(top_hours_graph=top_hours_graph, revenue_graph=revenue_graph, status=status, usd_rate=usd_rate)


@register_tl
class PaymentsStarsRevenueWithdrawalUrl(TLObject):
    ID: int = 0x1dab80b7

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarsRevenueWithdrawalUrl':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class PaymentsStarsRevenueAdsAccountUrl(TLObject):
    ID: int = 0x394e7f21

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarsRevenueAdsAccountUrl':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class InputStarsTransaction(TLObject):
    ID: int = 0x206ae6d1

    def __init__(self, refund: bool = False, id: Any = None) -> None:
        self.refund = refund
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.refund:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStarsTransaction':
        flags = reader.read_uint32()
        refund = bool(flags & (1 << 0))
        id = reader.read_string()
        return cls(refund=refund, id=id)


@register_tl
class StarsGiftOption(TLObject):
    ID: int = 0x5e0589f1

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
    def read(cls, reader: TLReader) -> 'StarsGiftOption':
        flags = reader.read_uint32()
        extended = bool(flags & (1 << 1))
        stars = reader.read_int64()
        store_product = reader.read_string() if (flags & (1 << 0)) else None
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(extended=extended, stars=stars, store_product=store_product, currency=currency, amount=amount)


@register_tl
class BotsPopularAppBots(TLObject):
    ID: int = 0x1991b13b

    def __init__(self, next_offset: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsPopularAppBots':
        flags = reader.read_uint32()
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(next_offset=next_offset, users=users)


@register_tl
class BotPreviewMedia(TLObject):
    ID: int = 0x23e91ba3

    def __init__(self, date: Any = None, media: Any = None) -> None:
        self.date = date
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.date or 0)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotPreviewMedia':
        date = reader.read_int32()
        media = reader.read_object()
        return cls(date=date, media=media)


@register_tl
class BotsPreviewInfo(TLObject):
    ID: int = 0xca71d64

    def __init__(self, media: Any = None, lang_codes: Any = None) -> None:
        self.media = media
        self.lang_codes = lang_codes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.media or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.lang_codes or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsPreviewInfo':
        media = reader.read_vector(lambda r: reader.read_object())
        lang_codes = reader.read_vector(lambda r: r.read_string())
        return cls(media=media, lang_codes=lang_codes)


@register_tl
class StarsSubscriptionPricing(TLObject):
    ID: int = 0x5416d58

    def __init__(self, period: Any = None, amount: Any = None) -> None:
        self.period = period
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.period or 0)
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsSubscriptionPricing':
        period = reader.read_int32()
        amount = reader.read_int64()
        return cls(period=period, amount=amount)


@register_tl
class StarsSubscription(TLObject):
    ID: int = 0x2e6eab1a

    def __init__(self, canceled: bool = False, can_refulfill: bool = False, missing_balance: bool = False, bot_canceled: bool = False, chat_invite_hash: Any = None, title: Any = None, photo: Any = None, invoice_slug: Any = None, id: Any = None, peer: Any = None, until_date: Any = None, pricing: Any = None) -> None:
        self.canceled = canceled
        self.can_refulfill = can_refulfill
        self.missing_balance = missing_balance
        self.bot_canceled = bot_canceled
        self.chat_invite_hash = chat_invite_hash
        self.title = title
        self.photo = photo
        self.invoice_slug = invoice_slug
        self.id = id
        self.peer = peer
        self.until_date = until_date
        self.pricing = pricing

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.canceled:
            flags |= (1 << 0)
        if self.can_refulfill:
            flags |= (1 << 1)
        if self.missing_balance:
            flags |= (1 << 2)
        if self.bot_canceled:
            flags |= (1 << 7)
        if self.chat_invite_hash is not None:
            flags |= (1 << 3)
        if self.title is not None:
            flags |= (1 << 4)
        if self.photo is not None:
            flags |= (1 << 5)
        if self.invoice_slug is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.until_date or 0)
        if self.pricing is not None and hasattr(self.pricing, 'write'): self.pricing.write(writer)
        if self.chat_invite_hash is not None:
            writer.write_string(self.chat_invite_hash or '')
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.invoice_slug is not None:
            writer.write_string(self.invoice_slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsSubscription':
        flags = reader.read_uint32()
        canceled = bool(flags & (1 << 0))
        can_refulfill = bool(flags & (1 << 1))
        missing_balance = bool(flags & (1 << 2))
        bot_canceled = bool(flags & (1 << 7))
        id = reader.read_string()
        peer = reader.read_object()
        until_date = reader.read_int32()
        pricing = reader.read_object()
        chat_invite_hash = reader.read_string() if (flags & (1 << 3)) else None
        title = reader.read_string() if (flags & (1 << 4)) else None
        photo = reader.read_object() if (flags & (1 << 5)) else None
        invoice_slug = reader.read_string() if (flags & (1 << 6)) else None
        return cls(canceled=canceled, can_refulfill=can_refulfill, missing_balance=missing_balance, bot_canceled=bot_canceled, id=id, peer=peer, until_date=until_date, pricing=pricing, chat_invite_hash=chat_invite_hash, title=title, photo=photo, invoice_slug=invoice_slug)


@register_tl
class MessageReactor(TLObject):
    ID: int = 0x4ba3a95a

    def __init__(self, top: bool = False, my: bool = False, anonymous: bool = False, peer_id: Any = None, count: Any = None) -> None:
        self.top = top
        self.my = my
        self.anonymous = anonymous
        self.peer_id = peer_id
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top:
            flags |= (1 << 0)
        if self.my:
            flags |= (1 << 1)
        if self.anonymous:
            flags |= (1 << 2)
        if self.peer_id is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.peer_id is not None:
            if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageReactor':
        flags = reader.read_uint32()
        top = bool(flags & (1 << 0))
        my = bool(flags & (1 << 1))
        anonymous = bool(flags & (1 << 2))
        peer_id = reader.read_object() if (flags & (1 << 3)) else None
        count = reader.read_int32()
        return cls(top=top, my=my, anonymous=anonymous, peer_id=peer_id, count=count)


@register_tl
class StarsGiveawayOption(TLObject):
    ID: int = 0x94ce852a

    def __init__(self, extended: bool = False, default: bool = False, store_product: Any = None, stars: Any = None, yearly_boosts: Any = None, currency: Any = None, amount: Any = None, winners: Any = None) -> None:
        self.extended = extended
        self.default = default
        self.store_product = store_product
        self.stars = stars
        self.yearly_boosts = yearly_boosts
        self.currency = currency
        self.amount = amount
        self.winners = winners

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.extended:
            flags |= (1 << 0)
        if self.default:
            flags |= (1 << 1)
        if self.store_product is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)
        writer.write_int32(self.yearly_boosts or 0)
        if self.store_product is not None:
            writer.write_string(self.store_product or '')
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        writer.write_vector(self.winners or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsGiveawayOption':
        flags = reader.read_uint32()
        extended = bool(flags & (1 << 0))
        default = bool(flags & (1 << 1))
        stars = reader.read_int64()
        yearly_boosts = reader.read_int32()
        store_product = reader.read_string() if (flags & (1 << 2)) else None
        currency = reader.read_string()
        amount = reader.read_int64()
        winners = reader.read_vector(lambda r: reader.read_object())
        return cls(extended=extended, default=default, stars=stars, yearly_boosts=yearly_boosts, store_product=store_product, currency=currency, amount=amount, winners=winners)


@register_tl
class StarsGiveawayWinnersOption(TLObject):
    ID: int = 0x54236209

    def __init__(self, default: bool = False, users: Any = None, per_user_stars: Any = None) -> None:
        self.default = default
        self.users = users
        self.per_user_stars = per_user_stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.default:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.users or 0)
        writer.write_int64(self.per_user_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsGiveawayWinnersOption':
        flags = reader.read_uint32()
        default = bool(flags & (1 << 0))
        users = reader.read_int32()
        per_user_stars = reader.read_int64()
        return cls(default=default, users=users, per_user_stars=per_user_stars)


@register_tl
class StarGift(TLObject):
    ID: int = 0x313a9547

    def __init__(self, limited: bool = False, sold_out: bool = False, birthday: bool = False, require_premium: bool = False, limited_per_user: bool = False, peer_color_available: bool = False, auction: bool = False, availability_remains: Any = None, availability_total: Any = None, availability_resale: Any = None, first_sale_date: Any = None, last_sale_date: Any = None, upgrade_stars: Any = None, resell_min_stars: Any = None, title: Any = None, released_by: Any = None, per_user_total: Any = None, per_user_remains: Any = None, locked_until_date: Any = None, auction_slug: Any = None, gifts_per_round: Any = None, auction_start_date: Any = None, upgrade_variants: Any = None, background: Any = None, id: Any = None, sticker: Any = None, stars: Any = None, convert_stars: Any = None) -> None:
        self.limited = limited
        self.sold_out = sold_out
        self.birthday = birthday
        self.require_premium = require_premium
        self.limited_per_user = limited_per_user
        self.peer_color_available = peer_color_available
        self.auction = auction
        self.availability_remains = availability_remains
        self.availability_total = availability_total
        self.availability_resale = availability_resale
        self.first_sale_date = first_sale_date
        self.last_sale_date = last_sale_date
        self.upgrade_stars = upgrade_stars
        self.resell_min_stars = resell_min_stars
        self.title = title
        self.released_by = released_by
        self.per_user_total = per_user_total
        self.per_user_remains = per_user_remains
        self.locked_until_date = locked_until_date
        self.auction_slug = auction_slug
        self.gifts_per_round = gifts_per_round
        self.auction_start_date = auction_start_date
        self.upgrade_variants = upgrade_variants
        self.background = background
        self.id = id
        self.sticker = sticker
        self.stars = stars
        self.convert_stars = convert_stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.limited:
            flags |= (1 << 0)
        if self.sold_out:
            flags |= (1 << 1)
        if self.birthday:
            flags |= (1 << 2)
        if self.require_premium:
            flags |= (1 << 7)
        if self.limited_per_user:
            flags |= (1 << 8)
        if self.peer_color_available:
            flags |= (1 << 10)
        if self.auction:
            flags |= (1 << 11)
        if self.availability_remains is not None:
            flags |= (1 << 0)
        if self.availability_total is not None:
            flags |= (1 << 0)
        if self.availability_resale is not None:
            flags |= (1 << 4)
        if self.first_sale_date is not None:
            flags |= (1 << 1)
        if self.last_sale_date is not None:
            flags |= (1 << 1)
        if self.upgrade_stars is not None:
            flags |= (1 << 3)
        if self.resell_min_stars is not None:
            flags |= (1 << 4)
        if self.title is not None:
            flags |= (1 << 5)
        if self.released_by is not None:
            flags |= (1 << 6)
        if self.per_user_total is not None:
            flags |= (1 << 8)
        if self.per_user_remains is not None:
            flags |= (1 << 8)
        if self.locked_until_date is not None:
            flags |= (1 << 9)
        if self.auction_slug is not None:
            flags |= (1 << 11)
        if self.gifts_per_round is not None:
            flags |= (1 << 11)
        if self.auction_start_date is not None:
            flags |= (1 << 11)
        if self.upgrade_variants is not None:
            flags |= (1 << 12)
        if self.background is not None:
            flags |= (1 << 13)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)
        writer.write_int64(self.stars or 0)
        if self.availability_remains is not None:
            writer.write_int32(self.availability_remains or 0)
        if self.availability_total is not None:
            writer.write_int32(self.availability_total or 0)
        if self.availability_resale is not None:
            writer.write_int64(self.availability_resale or 0)
        writer.write_int64(self.convert_stars or 0)
        if self.first_sale_date is not None:
            writer.write_int32(self.first_sale_date or 0)
        if self.last_sale_date is not None:
            writer.write_int32(self.last_sale_date or 0)
        if self.upgrade_stars is not None:
            writer.write_int64(self.upgrade_stars or 0)
        if self.resell_min_stars is not None:
            writer.write_int64(self.resell_min_stars or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.released_by is not None:
            if self.released_by is not None and hasattr(self.released_by, 'write'): self.released_by.write(writer)
        if self.per_user_total is not None:
            writer.write_int32(self.per_user_total or 0)
        if self.per_user_remains is not None:
            writer.write_int32(self.per_user_remains or 0)
        if self.locked_until_date is not None:
            writer.write_int32(self.locked_until_date or 0)
        if self.auction_slug is not None:
            writer.write_string(self.auction_slug or '')
        if self.gifts_per_round is not None:
            writer.write_int32(self.gifts_per_round or 0)
        if self.auction_start_date is not None:
            writer.write_int32(self.auction_start_date or 0)
        if self.upgrade_variants is not None:
            writer.write_int32(self.upgrade_variants or 0)
        if self.background is not None:
            if self.background is not None and hasattr(self.background, 'write'): self.background.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGift':
        flags = reader.read_uint32()
        limited = bool(flags & (1 << 0))
        sold_out = bool(flags & (1 << 1))
        birthday = bool(flags & (1 << 2))
        require_premium = bool(flags & (1 << 7))
        limited_per_user = bool(flags & (1 << 8))
        peer_color_available = bool(flags & (1 << 10))
        auction = bool(flags & (1 << 11))
        id = reader.read_int64()
        sticker = reader.read_object()
        stars = reader.read_int64()
        availability_remains = reader.read_int32() if (flags & (1 << 0)) else None
        availability_total = reader.read_int32() if (flags & (1 << 0)) else None
        availability_resale = reader.read_int64() if (flags & (1 << 4)) else None
        convert_stars = reader.read_int64()
        first_sale_date = reader.read_int32() if (flags & (1 << 1)) else None
        last_sale_date = reader.read_int32() if (flags & (1 << 1)) else None
        upgrade_stars = reader.read_int64() if (flags & (1 << 3)) else None
        resell_min_stars = reader.read_int64() if (flags & (1 << 4)) else None
        title = reader.read_string() if (flags & (1 << 5)) else None
        released_by = reader.read_object() if (flags & (1 << 6)) else None
        per_user_total = reader.read_int32() if (flags & (1 << 8)) else None
        per_user_remains = reader.read_int32() if (flags & (1 << 8)) else None
        locked_until_date = reader.read_int32() if (flags & (1 << 9)) else None
        auction_slug = reader.read_string() if (flags & (1 << 11)) else None
        gifts_per_round = reader.read_int32() if (flags & (1 << 11)) else None
        auction_start_date = reader.read_int32() if (flags & (1 << 11)) else None
        upgrade_variants = reader.read_int32() if (flags & (1 << 12)) else None
        background = reader.read_object() if (flags & (1 << 13)) else None
        return cls(limited=limited, sold_out=sold_out, birthday=birthday, require_premium=require_premium, limited_per_user=limited_per_user, peer_color_available=peer_color_available, auction=auction, id=id, sticker=sticker, stars=stars, availability_remains=availability_remains, availability_total=availability_total, availability_resale=availability_resale, convert_stars=convert_stars, first_sale_date=first_sale_date, last_sale_date=last_sale_date, upgrade_stars=upgrade_stars, resell_min_stars=resell_min_stars, title=title, released_by=released_by, per_user_total=per_user_total, per_user_remains=per_user_remains, locked_until_date=locked_until_date, auction_slug=auction_slug, gifts_per_round=gifts_per_round, auction_start_date=auction_start_date, upgrade_variants=upgrade_variants, background=background)


@register_tl
class StarGiftUnique(TLObject):
    ID: int = 0x85f0a9cd

    def __init__(self, require_premium: bool = False, resale_ton_only: bool = False, theme_available: bool = False, burned: bool = False, crafted: bool = False, owner_id: Any = None, owner_name: Any = None, owner_address: Any = None, gift_address: Any = None, resell_amount: Any = None, released_by: Any = None, value_amount: Any = None, value_currency: Any = None, value_usd_amount: Any = None, theme_peer: Any = None, peer_color: Any = None, host_id: Any = None, offer_min_stars: Any = None, craft_chance_permille: Any = None, id: Any = None, gift_id: Any = None, title: Any = None, slug: Any = None, num: Any = None, attributes: Any = None, availability_issued: Any = None, availability_total: Any = None) -> None:
        self.require_premium = require_premium
        self.resale_ton_only = resale_ton_only
        self.theme_available = theme_available
        self.burned = burned
        self.crafted = crafted
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.gift_address = gift_address
        self.resell_amount = resell_amount
        self.released_by = released_by
        self.value_amount = value_amount
        self.value_currency = value_currency
        self.value_usd_amount = value_usd_amount
        self.theme_peer = theme_peer
        self.peer_color = peer_color
        self.host_id = host_id
        self.offer_min_stars = offer_min_stars
        self.craft_chance_permille = craft_chance_permille
        self.id = id
        self.gift_id = gift_id
        self.title = title
        self.slug = slug
        self.num = num
        self.attributes = attributes
        self.availability_issued = availability_issued
        self.availability_total = availability_total

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.require_premium:
            flags |= (1 << 6)
        if self.resale_ton_only:
            flags |= (1 << 7)
        if self.theme_available:
            flags |= (1 << 9)
        if self.burned:
            flags |= (1 << 14)
        if self.crafted:
            flags |= (1 << 15)
        if self.owner_id is not None:
            flags |= (1 << 0)
        if self.owner_name is not None:
            flags |= (1 << 1)
        if self.owner_address is not None:
            flags |= (1 << 2)
        if self.gift_address is not None:
            flags |= (1 << 3)
        if self.resell_amount is not None:
            flags |= (1 << 4)
        if self.released_by is not None:
            flags |= (1 << 5)
        if self.value_amount is not None:
            flags |= (1 << 8)
        if self.value_currency is not None:
            flags |= (1 << 8)
        if self.value_usd_amount is not None:
            flags |= (1 << 8)
        if self.theme_peer is not None:
            flags |= (1 << 10)
        if self.peer_color is not None:
            flags |= (1 << 11)
        if self.host_id is not None:
            flags |= (1 << 12)
        if self.offer_min_stars is not None:
            flags |= (1 << 13)
        if self.craft_chance_permille is not None:
            flags |= (1 << 16)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.gift_id or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.slug or '')
        writer.write_int32(self.num or 0)
        if self.owner_id is not None:
            if self.owner_id is not None and hasattr(self.owner_id, 'write'): self.owner_id.write(writer)
        if self.owner_name is not None:
            writer.write_string(self.owner_name or '')
        if self.owner_address is not None:
            writer.write_string(self.owner_address or '')
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.availability_issued or 0)
        writer.write_int32(self.availability_total or 0)
        if self.gift_address is not None:
            writer.write_string(self.gift_address or '')
        if self.resell_amount is not None:
            writer.write_vector(self.resell_amount or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.released_by is not None:
            if self.released_by is not None and hasattr(self.released_by, 'write'): self.released_by.write(writer)
        if self.value_amount is not None:
            writer.write_int64(self.value_amount or 0)
        if self.value_currency is not None:
            writer.write_string(self.value_currency or '')
        if self.value_usd_amount is not None:
            writer.write_int64(self.value_usd_amount or 0)
        if self.theme_peer is not None:
            if self.theme_peer is not None and hasattr(self.theme_peer, 'write'): self.theme_peer.write(writer)
        if self.peer_color is not None:
            if self.peer_color is not None and hasattr(self.peer_color, 'write'): self.peer_color.write(writer)
        if self.host_id is not None:
            if self.host_id is not None and hasattr(self.host_id, 'write'): self.host_id.write(writer)
        if self.offer_min_stars is not None:
            writer.write_int32(self.offer_min_stars or 0)
        if self.craft_chance_permille is not None:
            writer.write_int32(self.craft_chance_permille or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftUnique':
        flags = reader.read_uint32()
        require_premium = bool(flags & (1 << 6))
        resale_ton_only = bool(flags & (1 << 7))
        theme_available = bool(flags & (1 << 9))
        burned = bool(flags & (1 << 14))
        crafted = bool(flags & (1 << 15))
        id = reader.read_int64()
        gift_id = reader.read_int64()
        title = reader.read_string()
        slug = reader.read_string()
        num = reader.read_int32()
        owner_id = reader.read_object() if (flags & (1 << 0)) else None
        owner_name = reader.read_string() if (flags & (1 << 1)) else None
        owner_address = reader.read_string() if (flags & (1 << 2)) else None
        attributes = reader.read_vector(lambda r: reader.read_object())
        availability_issued = reader.read_int32()
        availability_total = reader.read_int32()
        gift_address = reader.read_string() if (flags & (1 << 3)) else None
        resell_amount = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        released_by = reader.read_object() if (flags & (1 << 5)) else None
        value_amount = reader.read_int64() if (flags & (1 << 8)) else None
        value_currency = reader.read_string() if (flags & (1 << 8)) else None
        value_usd_amount = reader.read_int64() if (flags & (1 << 8)) else None
        theme_peer = reader.read_object() if (flags & (1 << 10)) else None
        peer_color = reader.read_object() if (flags & (1 << 11)) else None
        host_id = reader.read_object() if (flags & (1 << 12)) else None
        offer_min_stars = reader.read_int32() if (flags & (1 << 13)) else None
        craft_chance_permille = reader.read_int32() if (flags & (1 << 16)) else None
        return cls(require_premium=require_premium, resale_ton_only=resale_ton_only, theme_available=theme_available, burned=burned, crafted=crafted, id=id, gift_id=gift_id, title=title, slug=slug, num=num, owner_id=owner_id, owner_name=owner_name, owner_address=owner_address, attributes=attributes, availability_issued=availability_issued, availability_total=availability_total, gift_address=gift_address, resell_amount=resell_amount, released_by=released_by, value_amount=value_amount, value_currency=value_currency, value_usd_amount=value_usd_amount, theme_peer=theme_peer, peer_color=peer_color, host_id=host_id, offer_min_stars=offer_min_stars, craft_chance_permille=craft_chance_permille)


@register_tl
class PaymentsStarGiftsNotModified(TLObject):
    ID: int = 0xa388a368

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftsNotModified':
        return cls()


@register_tl
class PaymentsStarGifts(TLObject):
    ID: int = 0x2ed82995

    def __init__(self, hash: Any = None, gifts: Any = None, chats: Any = None, users: Any = None) -> None:
        self.hash = hash
        self.gifts = gifts
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)
        writer.write_vector(self.gifts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGifts':
        hash = reader.read_int32()
        gifts = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, gifts=gifts, chats=chats, users=users)


@register_tl
class MessageReportOption(TLObject):
    ID: int = 0x7903e3d9

    def __init__(self, text: Any = None, option: Any = None) -> None:
        self.text = text
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_bytes(self.option or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageReportOption':
        text = reader.read_string()
        option = reader.read_bytes()
        return cls(text=text, option=option)


@register_tl
class ReportResultChooseOption(TLObject):
    ID: int = 0xf0e4e0b6

    def __init__(self, title: Any = None, options: Any = None) -> None:
        self.title = title
        self.options = options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_vector(self.options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReportResultChooseOption':
        title = reader.read_string()
        options = reader.read_vector(lambda r: reader.read_object())
        return cls(title=title, options=options)


@register_tl
class ReportResultAddComment(TLObject):
    ID: int = 0x6f09ac31

    def __init__(self, optional: bool = False, option: Any = None) -> None:
        self.optional = optional
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.optional:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_bytes(self.option or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ReportResultAddComment':
        flags = reader.read_uint32()
        optional = bool(flags & (1 << 0))
        option = reader.read_bytes()
        return cls(optional=optional, option=option)


@register_tl
class ReportResultReported(TLObject):
    ID: int = 0x8db33c4b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReportResultReported':
        return cls()


@register_tl
class MessagesBotPreparedInlineMessage(TLObject):
    ID: int = 0x8ecf0511

    def __init__(self, id: Any = None, expire_date: Any = None) -> None:
        self.id = id
        self.expire_date = expire_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_int32(self.expire_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesBotPreparedInlineMessage':
        id = reader.read_string()
        expire_date = reader.read_int32()
        return cls(id=id, expire_date=expire_date)


@register_tl
class MessagesPreparedInlineMessage(TLObject):
    ID: int = 0xff57708d

    def __init__(self, query_id: Any = None, result: Any = None, peer_types: Any = None, cache_time: Any = None, users: Any = None) -> None:
        self.query_id = query_id
        self.result = result
        self.peer_types = peer_types
        self.cache_time = cache_time
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        if self.result is not None and hasattr(self.result, 'write'): self.result.write(writer)
        writer.write_vector(self.peer_types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.cache_time or 0)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesPreparedInlineMessage':
        query_id = reader.read_int64()
        result = reader.read_object()
        peer_types = reader.read_vector(lambda r: reader.read_object())
        cache_time = reader.read_int32()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(query_id=query_id, result=result, peer_types=peer_types, cache_time=cache_time, users=users)


@register_tl
class BotAppSettings(TLObject):
    ID: int = 0xc99b1950

    def __init__(self, placeholder_path: Any = None, background_color: Any = None, background_dark_color: Any = None, header_color: Any = None, header_dark_color: Any = None) -> None:
        self.placeholder_path = placeholder_path
        self.background_color = background_color
        self.background_dark_color = background_dark_color
        self.header_color = header_color
        self.header_dark_color = header_dark_color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.placeholder_path is not None:
            flags |= (1 << 0)
        if self.background_color is not None:
            flags |= (1 << 1)
        if self.background_dark_color is not None:
            flags |= (1 << 2)
        if self.header_color is not None:
            flags |= (1 << 3)
        if self.header_dark_color is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.placeholder_path is not None:
            writer.write_bytes(self.placeholder_path or b'')
        if self.background_color is not None:
            writer.write_int32(self.background_color or 0)
        if self.background_dark_color is not None:
            writer.write_int32(self.background_dark_color or 0)
        if self.header_color is not None:
            writer.write_int32(self.header_color or 0)
        if self.header_dark_color is not None:
            writer.write_int32(self.header_dark_color or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotAppSettings':
        flags = reader.read_uint32()
        placeholder_path = reader.read_bytes() if (flags & (1 << 0)) else None
        background_color = reader.read_int32() if (flags & (1 << 1)) else None
        background_dark_color = reader.read_int32() if (flags & (1 << 2)) else None
        header_color = reader.read_int32() if (flags & (1 << 3)) else None
        header_dark_color = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(placeholder_path=placeholder_path, background_color=background_color, background_dark_color=background_dark_color, header_color=header_color, header_dark_color=header_dark_color)


@register_tl
class StarRefProgram(TLObject):
    ID: int = 0xdd0c66f2

    def __init__(self, duration_months: Any = None, end_date: Any = None, daily_revenue_per_user: Any = None, bot_id: Any = None, commission_permille: Any = None) -> None:
        self.duration_months = duration_months
        self.end_date = end_date
        self.daily_revenue_per_user = daily_revenue_per_user
        self.bot_id = bot_id
        self.commission_permille = commission_permille

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.duration_months is not None:
            flags |= (1 << 0)
        if self.end_date is not None:
            flags |= (1 << 1)
        if self.daily_revenue_per_user is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.bot_id or 0)
        writer.write_int32(self.commission_permille or 0)
        if self.duration_months is not None:
            writer.write_int32(self.duration_months or 0)
        if self.end_date is not None:
            writer.write_int32(self.end_date or 0)
        if self.daily_revenue_per_user is not None:
            if self.daily_revenue_per_user is not None and hasattr(self.daily_revenue_per_user, 'write'): self.daily_revenue_per_user.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarRefProgram':
        flags = reader.read_uint32()
        bot_id = reader.read_int64()
        commission_permille = reader.read_int32()
        duration_months = reader.read_int32() if (flags & (1 << 0)) else None
        end_date = reader.read_int32() if (flags & (1 << 1)) else None
        daily_revenue_per_user = reader.read_object() if (flags & (1 << 2)) else None
        return cls(bot_id=bot_id, commission_permille=commission_permille, duration_months=duration_months, end_date=end_date, daily_revenue_per_user=daily_revenue_per_user)


@register_tl
class ConnectedBotStarRef(TLObject):
    ID: int = 0x19a13f71

    def __init__(self, revoked: bool = False, duration_months: Any = None, url: Any = None, date: Any = None, bot_id: Any = None, commission_permille: Any = None, participants: Any = None, revenue: Any = None) -> None:
        self.revoked = revoked
        self.duration_months = duration_months
        self.url = url
        self.date = date
        self.bot_id = bot_id
        self.commission_permille = commission_permille
        self.participants = participants
        self.revenue = revenue

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoked:
            flags |= (1 << 1)
        if self.duration_months is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.url or '')
        writer.write_int32(self.date or 0)
        writer.write_int64(self.bot_id or 0)
        writer.write_int32(self.commission_permille or 0)
        if self.duration_months is not None:
            writer.write_int32(self.duration_months or 0)
        writer.write_int64(self.participants or 0)
        writer.write_int64(self.revenue or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ConnectedBotStarRef':
        flags = reader.read_uint32()
        revoked = bool(flags & (1 << 1))
        url = reader.read_string()
        date = reader.read_int32()
        bot_id = reader.read_int64()
        commission_permille = reader.read_int32()
        duration_months = reader.read_int32() if (flags & (1 << 0)) else None
        participants = reader.read_int64()
        revenue = reader.read_int64()
        return cls(revoked=revoked, url=url, date=date, bot_id=bot_id, commission_permille=commission_permille, duration_months=duration_months, participants=participants, revenue=revenue)


@register_tl
class PaymentsConnectedStarRefBots(TLObject):
    ID: int = 0x98d5ea1d

    def __init__(self, count: Any = None, connected_bots: Any = None, users: Any = None) -> None:
        self.count = count
        self.connected_bots = connected_bots
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.connected_bots or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsConnectedStarRefBots':
        count = reader.read_int32()
        connected_bots = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, connected_bots=connected_bots, users=users)


@register_tl
class PaymentsSuggestedStarRefBots(TLObject):
    ID: int = 0xb4d5d859

    def __init__(self, next_offset: Any = None, count: Any = None, suggested_bots: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.count = count
        self.suggested_bots = suggested_bots
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.suggested_bots or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsSuggestedStarRefBots':
        flags = reader.read_uint32()
        count = reader.read_int32()
        suggested_bots = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        return cls(count=count, suggested_bots=suggested_bots, users=users, next_offset=next_offset)


@register_tl
class StarsAmount(TLObject):
    ID: int = 0xbbb6b4a3

    def __init__(self, amount: Any = None, nanos: Any = None) -> None:
        self.amount = amount
        self.nanos = nanos

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.amount or 0)
        writer.write_int32(self.nanos or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsAmount':
        amount = reader.read_int64()
        nanos = reader.read_int32()
        return cls(amount=amount, nanos=nanos)


@register_tl
class StarsTonAmount(TLObject):
    ID: int = 0x74aee3e0

    def __init__(self, amount: Any = None) -> None:
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsTonAmount':
        amount = reader.read_int64()
        return cls(amount=amount)


@register_tl
class MessagesFoundStickersNotModified(TLObject):
    ID: int = 0x6010c534

    def __init__(self, next_offset: Any = None) -> None:
        self.next_offset = next_offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.next_offset is not None:
            writer.write_int32(self.next_offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFoundStickersNotModified':
        flags = reader.read_uint32()
        next_offset = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(next_offset=next_offset)


@register_tl
class MessagesFoundStickers(TLObject):
    ID: int = 0x82c9e290

    def __init__(self, next_offset: Any = None, hash: Any = None, stickers: Any = None) -> None:
        self.next_offset = next_offset
        self.hash = hash
        self.stickers = stickers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.next_offset is not None:
            writer.write_int32(self.next_offset or 0)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesFoundStickers':
        flags = reader.read_uint32()
        next_offset = reader.read_int32() if (flags & (1 << 0)) else None
        hash = reader.read_int64()
        stickers = reader.read_vector(lambda r: reader.read_object())
        return cls(next_offset=next_offset, hash=hash, stickers=stickers)


@register_tl
class BotVerifierSettings(TLObject):
    ID: int = 0xb0cd6617

    def __init__(self, can_modify_custom_description: bool = False, custom_description: Any = None, icon: Any = None, company: Any = None) -> None:
        self.can_modify_custom_description = can_modify_custom_description
        self.custom_description = custom_description
        self.icon = icon
        self.company = company

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_modify_custom_description:
            flags |= (1 << 1)
        if self.custom_description is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.icon or 0)
        writer.write_string(self.company or '')
        if self.custom_description is not None:
            writer.write_string(self.custom_description or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotVerifierSettings':
        flags = reader.read_uint32()
        can_modify_custom_description = bool(flags & (1 << 1))
        icon = reader.read_int64()
        company = reader.read_string()
        custom_description = reader.read_string() if (flags & (1 << 0)) else None
        return cls(can_modify_custom_description=can_modify_custom_description, icon=icon, company=company, custom_description=custom_description)


@register_tl
class BotVerification(TLObject):
    ID: int = 0xf93cd45c

    def __init__(self, bot_id: Any = None, icon: Any = None, description: Any = None) -> None:
        self.bot_id = bot_id
        self.icon = icon
        self.description = description

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bot_id or 0)
        writer.write_int64(self.icon or 0)
        writer.write_string(self.description or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotVerification':
        bot_id = reader.read_int64()
        icon = reader.read_int64()
        description = reader.read_string()
        return cls(bot_id=bot_id, icon=icon, description=description)


@register_tl
class StarGiftAttributeModel(TLObject):
    ID: int = 0x565251e2

    def __init__(self, crafted: bool = False, name: Any = None, document: Any = None, rarity: Any = None) -> None:
        self.crafted = crafted
        self.name = name
        self.document = document
        self.rarity = rarity

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.crafted:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.name or '')
        if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.rarity is not None and hasattr(self.rarity, 'write'): self.rarity.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeModel':
        flags = reader.read_uint32()
        crafted = bool(flags & (1 << 0))
        name = reader.read_string()
        document = reader.read_object()
        rarity = reader.read_object()
        return cls(crafted=crafted, name=name, document=document, rarity=rarity)


@register_tl
class StarGiftAttributePattern(TLObject):
    ID: int = 0x4e7085ea

    def __init__(self, name: Any = None, document: Any = None, rarity: Any = None) -> None:
        self.name = name
        self.document = document
        self.rarity = rarity

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.name or '')
        if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.rarity is not None and hasattr(self.rarity, 'write'): self.rarity.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributePattern':
        name = reader.read_string()
        document = reader.read_object()
        rarity = reader.read_object()
        return cls(name=name, document=document, rarity=rarity)


@register_tl
class StarGiftAttributeBackdrop(TLObject):
    ID: int = 0x9f2504e4

    def __init__(self, name: Any = None, backdrop_id: Any = None, center_color: Any = None, edge_color: Any = None, pattern_color: Any = None, text_color: Any = None, rarity: Any = None) -> None:
        self.name = name
        self.backdrop_id = backdrop_id
        self.center_color = center_color
        self.edge_color = edge_color
        self.pattern_color = pattern_color
        self.text_color = text_color
        self.rarity = rarity

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.name or '')
        writer.write_int32(self.backdrop_id or 0)
        writer.write_int32(self.center_color or 0)
        writer.write_int32(self.edge_color or 0)
        writer.write_int32(self.pattern_color or 0)
        writer.write_int32(self.text_color or 0)
        if self.rarity is not None and hasattr(self.rarity, 'write'): self.rarity.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeBackdrop':
        name = reader.read_string()
        backdrop_id = reader.read_int32()
        center_color = reader.read_int32()
        edge_color = reader.read_int32()
        pattern_color = reader.read_int32()
        text_color = reader.read_int32()
        rarity = reader.read_object()
        return cls(name=name, backdrop_id=backdrop_id, center_color=center_color, edge_color=edge_color, pattern_color=pattern_color, text_color=text_color, rarity=rarity)


@register_tl
class StarGiftAttributeOriginalDetails(TLObject):
    ID: int = 0xe0bff26c

    def __init__(self, sender_id: Any = None, message: Any = None, recipient_id: Any = None, date: Any = None) -> None:
        self.sender_id = sender_id
        self.message = message
        self.recipient_id = recipient_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sender_id is not None:
            flags |= (1 << 0)
        if self.message is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.sender_id is not None:
            if self.sender_id is not None and hasattr(self.sender_id, 'write'): self.sender_id.write(writer)
        if self.recipient_id is not None and hasattr(self.recipient_id, 'write'): self.recipient_id.write(writer)
        writer.write_int32(self.date or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeOriginalDetails':
        flags = reader.read_uint32()
        sender_id = reader.read_object() if (flags & (1 << 0)) else None
        recipient_id = reader.read_object()
        date = reader.read_int32()
        message = reader.read_object() if (flags & (1 << 1)) else None
        return cls(sender_id=sender_id, recipient_id=recipient_id, date=date, message=message)


@register_tl
class PaymentsStarGiftUpgradePreview(TLObject):
    ID: int = 0x3de1dfed

    def __init__(self, sample_attributes: Any = None, prices: Any = None, next_prices: Any = None) -> None:
        self.sample_attributes = sample_attributes
        self.prices = prices
        self.next_prices = next_prices

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.sample_attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.prices or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.next_prices or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftUpgradePreview':
        sample_attributes = reader.read_vector(lambda r: reader.read_object())
        prices = reader.read_vector(lambda r: reader.read_object())
        next_prices = reader.read_vector(lambda r: reader.read_object())
        return cls(sample_attributes=sample_attributes, prices=prices, next_prices=next_prices)


@register_tl
class UsersUsers(TLObject):
    ID: int = 0x62d706b8

    def __init__(self, users: Any = None) -> None:
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersUsers':
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(users=users)


@register_tl
class UsersUsersSlice(TLObject):
    ID: int = 0x315a4974

    def __init__(self, count: Any = None, users: Any = None) -> None:
        self.count = count
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersUsersSlice':
        count = reader.read_int32()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, users=users)


@register_tl
class PaymentsUniqueStarGift(TLObject):
    ID: int = 0x416c56e8

    def __init__(self, gift: Any = None, chats: Any = None, users: Any = None) -> None:
        self.gift = gift
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsUniqueStarGift':
        gift = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(gift=gift, chats=chats, users=users)


@register_tl
class MessagesWebPagePreview(TLObject):
    ID: int = 0x8c9a88ac

    def __init__(self, media: Any = None, chats: Any = None, users: Any = None) -> None:
        self.media = media
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesWebPagePreview':
        media = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(media=media, chats=chats, users=users)


@register_tl
class SavedStarGift(TLObject):
    ID: int = 0x41df43fc

    def __init__(self, name_hidden: bool = False, unsaved: bool = False, refunded: bool = False, can_upgrade: bool = False, pinned_to_top: bool = False, upgrade_separate: bool = False, from_id: Any = None, message: Any = None, msg_id: Any = None, saved_id: Any = None, convert_stars: Any = None, upgrade_stars: Any = None, can_export_at: Any = None, transfer_stars: Any = None, can_transfer_at: Any = None, can_resell_at: Any = None, collection_id: Any = None, prepaid_upgrade_hash: Any = None, drop_original_details_stars: Any = None, gift_num: Any = None, can_craft_at: Any = None, date: Any = None, gift: Any = None) -> None:
        self.name_hidden = name_hidden
        self.unsaved = unsaved
        self.refunded = refunded
        self.can_upgrade = can_upgrade
        self.pinned_to_top = pinned_to_top
        self.upgrade_separate = upgrade_separate
        self.from_id = from_id
        self.message = message
        self.msg_id = msg_id
        self.saved_id = saved_id
        self.convert_stars = convert_stars
        self.upgrade_stars = upgrade_stars
        self.can_export_at = can_export_at
        self.transfer_stars = transfer_stars
        self.can_transfer_at = can_transfer_at
        self.can_resell_at = can_resell_at
        self.collection_id = collection_id
        self.prepaid_upgrade_hash = prepaid_upgrade_hash
        self.drop_original_details_stars = drop_original_details_stars
        self.gift_num = gift_num
        self.can_craft_at = can_craft_at
        self.date = date
        self.gift = gift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.name_hidden:
            flags |= (1 << 0)
        if self.unsaved:
            flags |= (1 << 5)
        if self.refunded:
            flags |= (1 << 9)
        if self.can_upgrade:
            flags |= (1 << 10)
        if self.pinned_to_top:
            flags |= (1 << 12)
        if self.upgrade_separate:
            flags |= (1 << 17)
        if self.from_id is not None:
            flags |= (1 << 1)
        if self.message is not None:
            flags |= (1 << 2)
        if self.msg_id is not None:
            flags |= (1 << 3)
        if self.saved_id is not None:
            flags |= (1 << 11)
        if self.convert_stars is not None:
            flags |= (1 << 4)
        if self.upgrade_stars is not None:
            flags |= (1 << 6)
        if self.can_export_at is not None:
            flags |= (1 << 7)
        if self.transfer_stars is not None:
            flags |= (1 << 8)
        if self.can_transfer_at is not None:
            flags |= (1 << 13)
        if self.can_resell_at is not None:
            flags |= (1 << 14)
        if self.collection_id is not None:
            flags |= (1 << 15)
        if self.prepaid_upgrade_hash is not None:
            flags |= (1 << 16)
        if self.drop_original_details_stars is not None:
            flags |= (1 << 18)
        if self.gift_num is not None:
            flags |= (1 << 19)
        if self.can_craft_at is not None:
            flags |= (1 << 20)
        writer.write_uint32(flags)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        writer.write_int32(self.date or 0)
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.saved_id is not None:
            writer.write_int64(self.saved_id or 0)
        if self.convert_stars is not None:
            writer.write_int64(self.convert_stars or 0)
        if self.upgrade_stars is not None:
            writer.write_int64(self.upgrade_stars or 0)
        if self.can_export_at is not None:
            writer.write_int32(self.can_export_at or 0)
        if self.transfer_stars is not None:
            writer.write_int64(self.transfer_stars or 0)
        if self.can_transfer_at is not None:
            writer.write_int32(self.can_transfer_at or 0)
        if self.can_resell_at is not None:
            writer.write_int32(self.can_resell_at or 0)
        if self.collection_id is not None:
            writer.write_vector(self.collection_id or [], lambda w, x: w.write_int32(x))
        if self.prepaid_upgrade_hash is not None:
            writer.write_string(self.prepaid_upgrade_hash or '')
        if self.drop_original_details_stars is not None:
            writer.write_int64(self.drop_original_details_stars or 0)
        if self.gift_num is not None:
            writer.write_int32(self.gift_num or 0)
        if self.can_craft_at is not None:
            writer.write_int32(self.can_craft_at or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SavedStarGift':
        flags = reader.read_uint32()
        name_hidden = bool(flags & (1 << 0))
        unsaved = bool(flags & (1 << 5))
        refunded = bool(flags & (1 << 9))
        can_upgrade = bool(flags & (1 << 10))
        pinned_to_top = bool(flags & (1 << 12))
        upgrade_separate = bool(flags & (1 << 17))
        from_id = reader.read_object() if (flags & (1 << 1)) else None
        date = reader.read_int32()
        gift = reader.read_object()
        message = reader.read_object() if (flags & (1 << 2)) else None
        msg_id = reader.read_int32() if (flags & (1 << 3)) else None
        saved_id = reader.read_int64() if (flags & (1 << 11)) else None
        convert_stars = reader.read_int64() if (flags & (1 << 4)) else None
        upgrade_stars = reader.read_int64() if (flags & (1 << 6)) else None
        can_export_at = reader.read_int32() if (flags & (1 << 7)) else None
        transfer_stars = reader.read_int64() if (flags & (1 << 8)) else None
        can_transfer_at = reader.read_int32() if (flags & (1 << 13)) else None
        can_resell_at = reader.read_int32() if (flags & (1 << 14)) else None
        collection_id = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 15)) else None
        prepaid_upgrade_hash = reader.read_string() if (flags & (1 << 16)) else None
        drop_original_details_stars = reader.read_int64() if (flags & (1 << 18)) else None
        gift_num = reader.read_int32() if (flags & (1 << 19)) else None
        can_craft_at = reader.read_int32() if (flags & (1 << 20)) else None
        return cls(name_hidden=name_hidden, unsaved=unsaved, refunded=refunded, can_upgrade=can_upgrade, pinned_to_top=pinned_to_top, upgrade_separate=upgrade_separate, from_id=from_id, date=date, gift=gift, message=message, msg_id=msg_id, saved_id=saved_id, convert_stars=convert_stars, upgrade_stars=upgrade_stars, can_export_at=can_export_at, transfer_stars=transfer_stars, can_transfer_at=can_transfer_at, can_resell_at=can_resell_at, collection_id=collection_id, prepaid_upgrade_hash=prepaid_upgrade_hash, drop_original_details_stars=drop_original_details_stars, gift_num=gift_num, can_craft_at=can_craft_at)


@register_tl
class PaymentsSavedStarGifts(TLObject):
    ID: int = 0x95f389b1

    def __init__(self, chat_notifications_enabled: Any = None, next_offset: Any = None, count: Any = None, gifts: Any = None, chats: Any = None, users: Any = None) -> None:
        self.chat_notifications_enabled = chat_notifications_enabled
        self.next_offset = next_offset
        self.count = count
        self.gifts = gifts
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.chat_notifications_enabled is not None:
            flags |= (1 << 1)
        if self.next_offset is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        if self.chat_notifications_enabled is not None:
            writer.write_bool(bool(self.chat_notifications_enabled))
        writer.write_vector(self.gifts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsSavedStarGifts':
        flags = reader.read_uint32()
        count = reader.read_int32()
        chat_notifications_enabled = reader.read_bool() if (flags & (1 << 1)) else None
        gifts = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, chat_notifications_enabled=chat_notifications_enabled, gifts=gifts, next_offset=next_offset, chats=chats, users=users)


@register_tl
class InputSavedStarGiftUser(TLObject):
    ID: int = 0x69279795

    def __init__(self, msg_id: Any = None) -> None:
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSavedStarGiftUser':
        msg_id = reader.read_int32()
        return cls(msg_id=msg_id)


@register_tl
class InputSavedStarGiftChat(TLObject):
    ID: int = 0xf101aa7f

    def __init__(self, peer: Any = None, saved_id: Any = None) -> None:
        self.peer = peer
        self.saved_id = saved_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.saved_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSavedStarGiftChat':
        peer = reader.read_object()
        saved_id = reader.read_int64()
        return cls(peer=peer, saved_id=saved_id)


@register_tl
class InputSavedStarGiftSlug(TLObject):
    ID: int = 0x2085c238

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSavedStarGiftSlug':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class PaymentsStarGiftWithdrawalUrl(TLObject):
    ID: int = 0x84aa3a9c

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftWithdrawalUrl':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class PaidReactionPrivacyDefault(TLObject):
    ID: int = 0x206ad49e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaidReactionPrivacyDefault':
        return cls()


@register_tl
class PaidReactionPrivacyAnonymous(TLObject):
    ID: int = 0x1f0c1ad9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaidReactionPrivacyAnonymous':
        return cls()


@register_tl
class PaidReactionPrivacyPeer(TLObject):
    ID: int = 0xdc6cfcf0

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaidReactionPrivacyPeer':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class AccountPaidMessagesRevenue(TLObject):
    ID: int = 0x1e109708

    def __init__(self, stars_amount: Any = None) -> None:
        self.stars_amount = stars_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.stars_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPaidMessagesRevenue':
        stars_amount = reader.read_int64()
        return cls(stars_amount=stars_amount)


@register_tl
class RequirementToContactEmpty(TLObject):
    ID: int = 0x50a9839

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequirementToContactEmpty':
        return cls()


@register_tl
class RequirementToContactPremium(TLObject):
    ID: int = 0xe581e4e9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequirementToContactPremium':
        return cls()


@register_tl
class RequirementToContactPaidMessages(TLObject):
    ID: int = 0xb4f67e93

    def __init__(self, stars_amount: Any = None) -> None:
        self.stars_amount = stars_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.stars_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'RequirementToContactPaidMessages':
        stars_amount = reader.read_int64()
        return cls(stars_amount=stars_amount)


@register_tl
class BusinessBotRights(TLObject):
    ID: int = 0xa0624cf7

    def __init__(self, reply: bool = False, read_messages: bool = False, delete_sent_messages: bool = False, delete_received_messages: bool = False, edit_name: bool = False, edit_bio: bool = False, edit_profile_photo: bool = False, edit_username: bool = False, view_gifts: bool = False, sell_gifts: bool = False, change_gift_settings: bool = False, transfer_and_upgrade_gifts: bool = False, transfer_stars: bool = False, manage_stories: bool = False) -> None:
        self.reply = reply
        self.read_messages = read_messages
        self.delete_sent_messages = delete_sent_messages
        self.delete_received_messages = delete_received_messages
        self.edit_name = edit_name
        self.edit_bio = edit_bio
        self.edit_profile_photo = edit_profile_photo
        self.edit_username = edit_username
        self.view_gifts = view_gifts
        self.sell_gifts = sell_gifts
        self.change_gift_settings = change_gift_settings
        self.transfer_and_upgrade_gifts = transfer_and_upgrade_gifts
        self.transfer_stars = transfer_stars
        self.manage_stories = manage_stories

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply:
            flags |= (1 << 0)
        if self.read_messages:
            flags |= (1 << 1)
        if self.delete_sent_messages:
            flags |= (1 << 2)
        if self.delete_received_messages:
            flags |= (1 << 3)
        if self.edit_name:
            flags |= (1 << 4)
        if self.edit_bio:
            flags |= (1 << 5)
        if self.edit_profile_photo:
            flags |= (1 << 6)
        if self.edit_username:
            flags |= (1 << 7)
        if self.view_gifts:
            flags |= (1 << 8)
        if self.sell_gifts:
            flags |= (1 << 9)
        if self.change_gift_settings:
            flags |= (1 << 10)
        if self.transfer_and_upgrade_gifts:
            flags |= (1 << 11)
        if self.transfer_stars:
            flags |= (1 << 12)
        if self.manage_stories:
            flags |= (1 << 13)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'BusinessBotRights':
        flags = reader.read_uint32()
        reply = bool(flags & (1 << 0))
        read_messages = bool(flags & (1 << 1))
        delete_sent_messages = bool(flags & (1 << 2))
        delete_received_messages = bool(flags & (1 << 3))
        edit_name = bool(flags & (1 << 4))
        edit_bio = bool(flags & (1 << 5))
        edit_profile_photo = bool(flags & (1 << 6))
        edit_username = bool(flags & (1 << 7))
        view_gifts = bool(flags & (1 << 8))
        sell_gifts = bool(flags & (1 << 9))
        change_gift_settings = bool(flags & (1 << 10))
        transfer_and_upgrade_gifts = bool(flags & (1 << 11))
        transfer_stars = bool(flags & (1 << 12))
        manage_stories = bool(flags & (1 << 13))
        return cls(reply=reply, read_messages=read_messages, delete_sent_messages=delete_sent_messages, delete_received_messages=delete_received_messages, edit_name=edit_name, edit_bio=edit_bio, edit_profile_photo=edit_profile_photo, edit_username=edit_username, view_gifts=view_gifts, sell_gifts=sell_gifts, change_gift_settings=change_gift_settings, transfer_and_upgrade_gifts=transfer_and_upgrade_gifts, transfer_stars=transfer_stars, manage_stories=manage_stories)


@register_tl
class DisallowedGiftsSettings(TLObject):
    ID: int = 0x71f276c4

    def __init__(self, disallow_unlimited_stargifts: bool = False, disallow_limited_stargifts: bool = False, disallow_unique_stargifts: bool = False, disallow_premium_gifts: bool = False, disallow_stargifts_from_channels: bool = False) -> None:
        self.disallow_unlimited_stargifts = disallow_unlimited_stargifts
        self.disallow_limited_stargifts = disallow_limited_stargifts
        self.disallow_unique_stargifts = disallow_unique_stargifts
        self.disallow_premium_gifts = disallow_premium_gifts
        self.disallow_stargifts_from_channels = disallow_stargifts_from_channels

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.disallow_unlimited_stargifts:
            flags |= (1 << 0)
        if self.disallow_limited_stargifts:
            flags |= (1 << 1)
        if self.disallow_unique_stargifts:
            flags |= (1 << 2)
        if self.disallow_premium_gifts:
            flags |= (1 << 3)
        if self.disallow_stargifts_from_channels:
            flags |= (1 << 4)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'DisallowedGiftsSettings':
        flags = reader.read_uint32()
        disallow_unlimited_stargifts = bool(flags & (1 << 0))
        disallow_limited_stargifts = bool(flags & (1 << 1))
        disallow_unique_stargifts = bool(flags & (1 << 2))
        disallow_premium_gifts = bool(flags & (1 << 3))
        disallow_stargifts_from_channels = bool(flags & (1 << 4))
        return cls(disallow_unlimited_stargifts=disallow_unlimited_stargifts, disallow_limited_stargifts=disallow_limited_stargifts, disallow_unique_stargifts=disallow_unique_stargifts, disallow_premium_gifts=disallow_premium_gifts, disallow_stargifts_from_channels=disallow_stargifts_from_channels)


@register_tl
class SponsoredPeer(TLObject):
    ID: int = 0xc69708d3

    def __init__(self, sponsor_info: Any = None, additional_info: Any = None, random_id: Any = None, peer: Any = None) -> None:
        self.sponsor_info = sponsor_info
        self.additional_info = additional_info
        self.random_id = random_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sponsor_info is not None:
            flags |= (1 << 0)
        if self.additional_info is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_bytes(self.random_id or b'')
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.sponsor_info is not None:
            writer.write_string(self.sponsor_info or '')
        if self.additional_info is not None:
            writer.write_string(self.additional_info or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'SponsoredPeer':
        flags = reader.read_uint32()
        random_id = reader.read_bytes()
        peer = reader.read_object()
        sponsor_info = reader.read_string() if (flags & (1 << 0)) else None
        additional_info = reader.read_string() if (flags & (1 << 1)) else None
        return cls(random_id=random_id, peer=peer, sponsor_info=sponsor_info, additional_info=additional_info)


@register_tl
class ContactsSponsoredPeersEmpty(TLObject):
    ID: int = 0xea32b4b1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsSponsoredPeersEmpty':
        return cls()


@register_tl
class ContactsSponsoredPeers(TLObject):
    ID: int = 0xeb032884

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
    def read(cls, reader: TLReader) -> 'ContactsSponsoredPeers':
        peers = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(peers=peers, chats=chats, users=users)


@register_tl
class StarGiftAttributeIdModel(TLObject):
    ID: int = 0x48aaae3c

    def __init__(self, document_id: Any = None) -> None:
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.document_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeIdModel':
        document_id = reader.read_int64()
        return cls(document_id=document_id)


@register_tl
class StarGiftAttributeIdPattern(TLObject):
    ID: int = 0x4a162433

    def __init__(self, document_id: Any = None) -> None:
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.document_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeIdPattern':
        document_id = reader.read_int64()
        return cls(document_id=document_id)


@register_tl
class StarGiftAttributeIdBackdrop(TLObject):
    ID: int = 0x1f01c757

    def __init__(self, backdrop_id: Any = None) -> None:
        self.backdrop_id = backdrop_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.backdrop_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeIdBackdrop':
        backdrop_id = reader.read_int32()
        return cls(backdrop_id=backdrop_id)


@register_tl
class StarGiftAttributeCounter(TLObject):
    ID: int = 0x2eb1b658

    def __init__(self, attribute: Any = None, count: Any = None) -> None:
        self.attribute = attribute
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.attribute is not None and hasattr(self.attribute, 'write'): self.attribute.write(writer)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeCounter':
        attribute = reader.read_object()
        count = reader.read_int32()
        return cls(attribute=attribute, count=count)


@register_tl
class PaymentsResaleStarGifts(TLObject):
    ID: int = 0x947a12df

    def __init__(self, next_offset: Any = None, attributes: Any = None, attributes_hash: Any = None, counters: Any = None, count: Any = None, gifts: Any = None, chats: Any = None, users: Any = None) -> None:
        self.next_offset = next_offset
        self.attributes = attributes
        self.attributes_hash = attributes_hash
        self.counters = counters
        self.count = count
        self.gifts = gifts
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_offset is not None:
            flags |= (1 << 0)
        if self.attributes is not None:
            flags |= (1 << 1)
        if self.attributes_hash is not None:
            flags |= (1 << 1)
        if self.counters is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.gifts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.next_offset is not None:
            writer.write_string(self.next_offset or '')
        if self.attributes is not None:
            writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.attributes_hash is not None:
            writer.write_int64(self.attributes_hash or 0)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.counters is not None:
            writer.write_vector(self.counters or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsResaleStarGifts':
        flags = reader.read_uint32()
        count = reader.read_int32()
        gifts = reader.read_vector(lambda r: reader.read_object())
        next_offset = reader.read_string() if (flags & (1 << 0)) else None
        attributes = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        attributes_hash = reader.read_int64() if (flags & (1 << 1)) else None
        chats = reader.read_vector(lambda r: reader.read_object())
        counters = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 2)) else None
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, gifts=gifts, next_offset=next_offset, attributes=attributes, attributes_hash=attributes_hash, chats=chats, counters=counters, users=users)


@register_tl
class StoriesCanSendStoryCount(TLObject):
    ID: int = 0xc387c04e

    def __init__(self, count_remains: Any = None) -> None:
        self.count_remains = count_remains

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count_remains or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesCanSendStoryCount':
        count_remains = reader.read_int32()
        return cls(count_remains=count_remains)


@register_tl
class PendingSuggestion(TLObject):
    ID: int = 0xe7e82e12

    def __init__(self, suggestion: Any = None, title: Any = None, description: Any = None, url: Any = None) -> None:
        self.suggestion = suggestion
        self.title = title
        self.description = description
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.suggestion or '')
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)
        if self.description is not None and hasattr(self.description, 'write'): self.description.write(writer)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PendingSuggestion':
        suggestion = reader.read_string()
        title = reader.read_object()
        description = reader.read_object()
        url = reader.read_string()
        return cls(suggestion=suggestion, title=title, description=description, url=url)


@register_tl
class TodoItem(TLObject):
    ID: int = 0xcba9a52f

    def __init__(self, id: Any = None, title: Any = None) -> None:
        self.id = id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TodoItem':
        id = reader.read_int32()
        title = reader.read_object()
        return cls(id=id, title=title)


@register_tl
class TodoList(TLObject):
    ID: int = 0x49b92a26

    def __init__(self, others_can_append: bool = False, others_can_complete: bool = False, title: Any = None, list: Any = None) -> None:
        self.others_can_append = others_can_append
        self.others_can_complete = others_can_complete
        self.title = title
        self.list = list

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.others_can_append:
            flags |= (1 << 0)
        if self.others_can_complete:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)
        writer.write_vector(self.list or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'TodoList':
        flags = reader.read_uint32()
        others_can_append = bool(flags & (1 << 0))
        others_can_complete = bool(flags & (1 << 1))
        title = reader.read_object()
        list = reader.read_vector(lambda r: reader.read_object())
        return cls(others_can_append=others_can_append, others_can_complete=others_can_complete, title=title, list=list)


@register_tl
class TodoCompletion(TLObject):
    ID: int = 0x221bb5e4

    def __init__(self, id: Any = None, completed_by: Any = None, date: Any = None) -> None:
        self.id = id
        self.completed_by = completed_by
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        if self.completed_by is not None and hasattr(self.completed_by, 'write'): self.completed_by.write(writer)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'TodoCompletion':
        id = reader.read_int32()
        completed_by = reader.read_object()
        date = reader.read_int32()
        return cls(id=id, completed_by=completed_by, date=date)


@register_tl
class SuggestedPost(TLObject):
    ID: int = 0xe8e37e5

    def __init__(self, accepted: bool = False, rejected: bool = False, price: Any = None, schedule_date: Any = None) -> None:
        self.accepted = accepted
        self.rejected = rejected
        self.price = price
        self.schedule_date = schedule_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accepted:
            flags |= (1 << 1)
        if self.rejected:
            flags |= (1 << 2)
        if self.price is not None:
            flags |= (1 << 3)
        if self.schedule_date is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.price is not None:
            if self.price is not None and hasattr(self.price, 'write'): self.price.write(writer)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SuggestedPost':
        flags = reader.read_uint32()
        accepted = bool(flags & (1 << 1))
        rejected = bool(flags & (1 << 2))
        price = reader.read_object() if (flags & (1 << 3)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(accepted=accepted, rejected=rejected, price=price, schedule_date=schedule_date)


@register_tl
class StarsRating(TLObject):
    ID: int = 0x1b0e4f07

    def __init__(self, next_level_stars: Any = None, level: Any = None, current_level_stars: Any = None, stars: Any = None) -> None:
        self.next_level_stars = next_level_stars
        self.level = level
        self.current_level_stars = current_level_stars
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_level_stars is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.level or 0)
        writer.write_int64(self.current_level_stars or 0)
        writer.write_int64(self.stars or 0)
        if self.next_level_stars is not None:
            writer.write_int64(self.next_level_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarsRating':
        flags = reader.read_uint32()
        level = reader.read_int32()
        current_level_stars = reader.read_int64()
        stars = reader.read_int64()
        next_level_stars = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(level=level, current_level_stars=current_level_stars, stars=stars, next_level_stars=next_level_stars)


@register_tl
class StarGiftCollection(TLObject):
    ID: int = 0x9d6b13b0

    def __init__(self, icon: Any = None, collection_id: Any = None, title: Any = None, gifts_count: Any = None, hash: Any = None) -> None:
        self.icon = icon
        self.collection_id = collection_id
        self.title = title
        self.gifts_count = gifts_count
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.icon is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.collection_id or 0)
        writer.write_string(self.title or '')
        if self.icon is not None:
            if self.icon is not None and hasattr(self.icon, 'write'): self.icon.write(writer)
        writer.write_int32(self.gifts_count or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftCollection':
        flags = reader.read_uint32()
        collection_id = reader.read_int32()
        title = reader.read_string()
        icon = reader.read_object() if (flags & (1 << 0)) else None
        gifts_count = reader.read_int32()
        hash = reader.read_int64()
        return cls(collection_id=collection_id, title=title, icon=icon, gifts_count=gifts_count, hash=hash)


@register_tl
class PaymentsStarGiftCollectionsNotModified(TLObject):
    ID: int = 0xa0ba4f17

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftCollectionsNotModified':
        return cls()


@register_tl
class PaymentsStarGiftCollections(TLObject):
    ID: int = 0x8a2932f3

    def __init__(self, collections: Any = None) -> None:
        self.collections = collections

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.collections or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftCollections':
        collections = reader.read_vector(lambda r: reader.read_object())
        return cls(collections=collections)


@register_tl
class StoryAlbum(TLObject):
    ID: int = 0x9325705a

    def __init__(self, icon_photo: Any = None, icon_video: Any = None, album_id: Any = None, title: Any = None) -> None:
        self.icon_photo = icon_photo
        self.icon_video = icon_video
        self.album_id = album_id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.icon_photo is not None:
            flags |= (1 << 0)
        if self.icon_video is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.album_id or 0)
        writer.write_string(self.title or '')
        if self.icon_photo is not None:
            if self.icon_photo is not None and hasattr(self.icon_photo, 'write'): self.icon_photo.write(writer)
        if self.icon_video is not None:
            if self.icon_video is not None and hasattr(self.icon_video, 'write'): self.icon_video.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoryAlbum':
        flags = reader.read_uint32()
        album_id = reader.read_int32()
        title = reader.read_string()
        icon_photo = reader.read_object() if (flags & (1 << 0)) else None
        icon_video = reader.read_object() if (flags & (1 << 1)) else None
        return cls(album_id=album_id, title=title, icon_photo=icon_photo, icon_video=icon_video)


@register_tl
class StoriesAlbumsNotModified(TLObject):
    ID: int = 0x564edaeb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesAlbumsNotModified':
        return cls()


@register_tl
class StoriesAlbums(TLObject):
    ID: int = 0xc3987a3a

    def __init__(self, hash: Any = None, albums: Any = None) -> None:
        self.hash = hash
        self.albums = albums

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.albums or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StoriesAlbums':
        hash = reader.read_int64()
        albums = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, albums=albums)


@register_tl
class SearchPostsFlood(TLObject):
    ID: int = 0x3e0b5b6a

    def __init__(self, query_is_free: bool = False, wait_till: Any = None, total_daily: Any = None, remains: Any = None, stars_amount: Any = None) -> None:
        self.query_is_free = query_is_free
        self.wait_till = wait_till
        self.total_daily = total_daily
        self.remains = remains
        self.stars_amount = stars_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.query_is_free:
            flags |= (1 << 0)
        if self.wait_till is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.total_daily or 0)
        writer.write_int32(self.remains or 0)
        if self.wait_till is not None:
            writer.write_int32(self.wait_till or 0)
        writer.write_int64(self.stars_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SearchPostsFlood':
        flags = reader.read_uint32()
        query_is_free = bool(flags & (1 << 0))
        total_daily = reader.read_int32()
        remains = reader.read_int32()
        wait_till = reader.read_int32() if (flags & (1 << 1)) else None
        stars_amount = reader.read_int64()
        return cls(query_is_free=query_is_free, total_daily=total_daily, remains=remains, wait_till=wait_till, stars_amount=stars_amount)


@register_tl
class PaymentsUniqueStarGiftValueInfo(TLObject):
    ID: int = 0x512fe446

    def __init__(self, last_sale_on_fragment: bool = False, value_is_average: bool = False, last_sale_date: Any = None, last_sale_price: Any = None, floor_price: Any = None, average_price: Any = None, listed_count: Any = None, fragment_listed_count: Any = None, fragment_listed_url: Any = None, currency: Any = None, value: Any = None, initial_sale_date: Any = None, initial_sale_stars: Any = None, initial_sale_price: Any = None) -> None:
        self.last_sale_on_fragment = last_sale_on_fragment
        self.value_is_average = value_is_average
        self.last_sale_date = last_sale_date
        self.last_sale_price = last_sale_price
        self.floor_price = floor_price
        self.average_price = average_price
        self.listed_count = listed_count
        self.fragment_listed_count = fragment_listed_count
        self.fragment_listed_url = fragment_listed_url
        self.currency = currency
        self.value = value
        self.initial_sale_date = initial_sale_date
        self.initial_sale_stars = initial_sale_stars
        self.initial_sale_price = initial_sale_price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.last_sale_on_fragment:
            flags |= (1 << 1)
        if self.value_is_average:
            flags |= (1 << 6)
        if self.last_sale_date is not None:
            flags |= (1 << 0)
        if self.last_sale_price is not None:
            flags |= (1 << 0)
        if self.floor_price is not None:
            flags |= (1 << 2)
        if self.average_price is not None:
            flags |= (1 << 3)
        if self.listed_count is not None:
            flags |= (1 << 4)
        if self.fragment_listed_count is not None:
            flags |= (1 << 5)
        if self.fragment_listed_url is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_string(self.currency or '')
        writer.write_int64(self.value or 0)
        writer.write_int32(self.initial_sale_date or 0)
        writer.write_int64(self.initial_sale_stars or 0)
        writer.write_int64(self.initial_sale_price or 0)
        if self.last_sale_date is not None:
            writer.write_int32(self.last_sale_date or 0)
        if self.last_sale_price is not None:
            writer.write_int64(self.last_sale_price or 0)
        if self.floor_price is not None:
            writer.write_int64(self.floor_price or 0)
        if self.average_price is not None:
            writer.write_int64(self.average_price or 0)
        if self.listed_count is not None:
            writer.write_int32(self.listed_count or 0)
        if self.fragment_listed_count is not None:
            writer.write_int32(self.fragment_listed_count or 0)
        if self.fragment_listed_url is not None:
            writer.write_string(self.fragment_listed_url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsUniqueStarGiftValueInfo':
        flags = reader.read_uint32()
        last_sale_on_fragment = bool(flags & (1 << 1))
        value_is_average = bool(flags & (1 << 6))
        currency = reader.read_string()
        value = reader.read_int64()
        initial_sale_date = reader.read_int32()
        initial_sale_stars = reader.read_int64()
        initial_sale_price = reader.read_int64()
        last_sale_date = reader.read_int32() if (flags & (1 << 0)) else None
        last_sale_price = reader.read_int64() if (flags & (1 << 0)) else None
        floor_price = reader.read_int64() if (flags & (1 << 2)) else None
        average_price = reader.read_int64() if (flags & (1 << 3)) else None
        listed_count = reader.read_int32() if (flags & (1 << 4)) else None
        fragment_listed_count = reader.read_int32() if (flags & (1 << 5)) else None
        fragment_listed_url = reader.read_string() if (flags & (1 << 5)) else None
        return cls(last_sale_on_fragment=last_sale_on_fragment, value_is_average=value_is_average, currency=currency, value=value, initial_sale_date=initial_sale_date, initial_sale_stars=initial_sale_stars, initial_sale_price=initial_sale_price, last_sale_date=last_sale_date, last_sale_price=last_sale_price, floor_price=floor_price, average_price=average_price, listed_count=listed_count, fragment_listed_count=fragment_listed_count, fragment_listed_url=fragment_listed_url)


@register_tl
class ProfileTabPosts(TLObject):
    ID: int = 0xb98cd696

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabPosts':
        return cls()


@register_tl
class ProfileTabGifts(TLObject):
    ID: int = 0x4d4bd46a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabGifts':
        return cls()


@register_tl
class ProfileTabMedia(TLObject):
    ID: int = 0x72c64955

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabMedia':
        return cls()


@register_tl
class ProfileTabFiles(TLObject):
    ID: int = 0xab339c00

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabFiles':
        return cls()


@register_tl
class ProfileTabMusic(TLObject):
    ID: int = 0x9f27d26e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabMusic':
        return cls()


@register_tl
class ProfileTabVoice(TLObject):
    ID: int = 0xe477092e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabVoice':
        return cls()


@register_tl
class ProfileTabLinks(TLObject):
    ID: int = 0xd3656499

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabLinks':
        return cls()


@register_tl
class ProfileTabGifs(TLObject):
    ID: int = 0xa2c0f695

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ProfileTabGifs':
        return cls()


@register_tl
class UsersSavedMusicNotModified(TLObject):
    ID: int = 0xe3878aa4

    def __init__(self, count: Any = None) -> None:
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersSavedMusicNotModified':
        count = reader.read_int32()
        return cls(count=count)


@register_tl
class UsersSavedMusic(TLObject):
    ID: int = 0x34a2f297

    def __init__(self, count: Any = None, documents: Any = None) -> None:
        self.count = count
        self.documents = documents

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersSavedMusic':
        count = reader.read_int32()
        documents = reader.read_vector(lambda r: reader.read_object())
        return cls(count=count, documents=documents)


@register_tl
class AccountSavedMusicIdsNotModified(TLObject):
    ID: int = 0x4fc81d6e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSavedMusicIdsNotModified':
        return cls()


@register_tl
class AccountSavedMusicIds(TLObject):
    ID: int = 0x998d6636

    def __init__(self, ids: Any = None) -> None:
        self.ids = ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSavedMusicIds':
        ids = reader.read_vector(lambda r: r.read_int64())
        return cls(ids=ids)


@register_tl
class PaymentsCheckCanSendGiftResultOk(TLObject):
    ID: int = 0x374fa7ad

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCheckCanSendGiftResultOk':
        return cls()


@register_tl
class PaymentsCheckCanSendGiftResultFail(TLObject):
    ID: int = 0xd5e58274

    def __init__(self, reason: Any = None) -> None:
        self.reason = reason

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.reason is not None and hasattr(self.reason, 'write'): self.reason.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCheckCanSendGiftResultFail':
        reason = reader.read_object()
        return cls(reason=reason)


@register_tl
class InputChatThemeEmpty(TLObject):
    ID: int = 0x83268483

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatThemeEmpty':
        return cls()


@register_tl
class InputChatTheme(TLObject):
    ID: int = 0xc93de95c

    def __init__(self, emoticon: Any = None) -> None:
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatTheme':
        emoticon = reader.read_string()
        return cls(emoticon=emoticon)


@register_tl
class InputChatThemeUniqueGift(TLObject):
    ID: int = 0x87e5dfe4

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatThemeUniqueGift':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class StarGiftUpgradePrice(TLObject):
    ID: int = 0x99ea331d

    def __init__(self, date: Any = None, upgrade_stars: Any = None) -> None:
        self.date = date
        self.upgrade_stars = upgrade_stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.upgrade_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftUpgradePrice':
        date = reader.read_int32()
        upgrade_stars = reader.read_int64()
        return cls(date=date, upgrade_stars=upgrade_stars)


@register_tl
class GroupCallMessage(TLObject):
    ID: int = 0x1a8afc7e

    def __init__(self, from_admin: bool = False, paid_message_stars: Any = None, id: Any = None, from_id: Any = None, date: Any = None, message: Any = None) -> None:
        self.from_admin = from_admin
        self.paid_message_stars = paid_message_stars
        self.id = id
        self.from_id = from_id
        self.date = date
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.from_admin:
            flags |= (1 << 1)
        if self.paid_message_stars is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        writer.write_int32(self.date or 0)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        if self.paid_message_stars is not None:
            writer.write_int64(self.paid_message_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallMessage':
        flags = reader.read_uint32()
        from_admin = bool(flags & (1 << 1))
        id = reader.read_int32()
        from_id = reader.read_object()
        date = reader.read_int32()
        message = reader.read_object()
        paid_message_stars = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(from_admin=from_admin, id=id, from_id=from_id, date=date, message=message, paid_message_stars=paid_message_stars)


@register_tl
class GroupCallDonor(TLObject):
    ID: int = 0xee430c85

    def __init__(self, top: bool = False, my: bool = False, peer_id: Any = None, stars: Any = None) -> None:
        self.top = top
        self.my = my
        self.peer_id = peer_id
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top:
            flags |= (1 << 0)
        if self.my:
            flags |= (1 << 1)
        if self.peer_id is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.peer_id is not None:
            if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallDonor':
        flags = reader.read_uint32()
        top = bool(flags & (1 << 0))
        my = bool(flags & (1 << 1))
        peer_id = reader.read_object() if (flags & (1 << 3)) else None
        stars = reader.read_int64()
        return cls(top=top, my=my, peer_id=peer_id, stars=stars)


@register_tl
class PhoneGroupCallStars(TLObject):
    ID: int = 0x9d1dbd26

    def __init__(self, total_stars: Any = None, top_donors: Any = None, chats: Any = None, users: Any = None) -> None:
        self.total_stars = total_stars
        self.top_donors = top_donors
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.total_stars or 0)
        writer.write_vector(self.top_donors or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGroupCallStars':
        total_stars = reader.read_int64()
        top_donors = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(total_stars=total_stars, top_donors=top_donors, chats=chats, users=users)


@register_tl
class RecentStory(TLObject):
    ID: int = 0x711d692d

    def __init__(self, live: bool = False, max_id: Any = None) -> None:
        self.live = live
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.live:
            flags |= (1 << 0)
        if self.max_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.max_id is not None:
            writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'RecentStory':
        flags = reader.read_uint32()
        live = bool(flags & (1 << 0))
        max_id = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(live=live, max_id=max_id)


@register_tl
class AuctionBidLevel(TLObject):
    ID: int = 0x310240cc

    def __init__(self, pos: Any = None, amount: Any = None, date: Any = None) -> None:
        self.pos = pos
        self.amount = amount
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pos or 0)
        writer.write_int64(self.amount or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuctionBidLevel':
        pos = reader.read_int32()
        amount = reader.read_int64()
        date = reader.read_int32()
        return cls(pos=pos, amount=amount, date=date)


@register_tl
class StarGiftAuctionStateNotModified(TLObject):
    ID: int = 0xfe333952

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAuctionStateNotModified':
        return cls()


@register_tl
class StarGiftAuctionState(TLObject):
    ID: int = 0x771a4e66

    def __init__(self, version: Any = None, start_date: Any = None, end_date: Any = None, min_bid_amount: Any = None, bid_levels: Any = None, top_bidders: Any = None, next_round_at: Any = None, last_gift_num: Any = None, gifts_left: Any = None, current_round: Any = None, total_rounds: Any = None, rounds: Any = None) -> None:
        self.version = version
        self.start_date = start_date
        self.end_date = end_date
        self.min_bid_amount = min_bid_amount
        self.bid_levels = bid_levels
        self.top_bidders = top_bidders
        self.next_round_at = next_round_at
        self.last_gift_num = last_gift_num
        self.gifts_left = gifts_left
        self.current_round = current_round
        self.total_rounds = total_rounds
        self.rounds = rounds

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.version or 0)
        writer.write_int32(self.start_date or 0)
        writer.write_int32(self.end_date or 0)
        writer.write_int64(self.min_bid_amount or 0)
        writer.write_vector(self.bid_levels or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.top_bidders or [], lambda w, x: w.write_int64(x))
        writer.write_int32(self.next_round_at or 0)
        writer.write_int32(self.last_gift_num or 0)
        writer.write_int32(self.gifts_left or 0)
        writer.write_int32(self.current_round or 0)
        writer.write_int32(self.total_rounds or 0)
        writer.write_vector(self.rounds or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAuctionState':
        version = reader.read_int32()
        start_date = reader.read_int32()
        end_date = reader.read_int32()
        min_bid_amount = reader.read_int64()
        bid_levels = reader.read_vector(lambda r: reader.read_object())
        top_bidders = reader.read_vector(lambda r: r.read_int64())
        next_round_at = reader.read_int32()
        last_gift_num = reader.read_int32()
        gifts_left = reader.read_int32()
        current_round = reader.read_int32()
        total_rounds = reader.read_int32()
        rounds = reader.read_vector(lambda r: reader.read_object())
        return cls(version=version, start_date=start_date, end_date=end_date, min_bid_amount=min_bid_amount, bid_levels=bid_levels, top_bidders=top_bidders, next_round_at=next_round_at, last_gift_num=last_gift_num, gifts_left=gifts_left, current_round=current_round, total_rounds=total_rounds, rounds=rounds)

