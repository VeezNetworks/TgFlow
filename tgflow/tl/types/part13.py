from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class StarGiftAuctionStateFinished(TLObject):
    ID: int = 0x972dabbf

    def __init__(self, listed_count: Any = None, fragment_listed_count: Any = None, fragment_listed_url: Any = None, start_date: Any = None, end_date: Any = None, average_price: Any = None) -> None:
        self.listed_count = listed_count
        self.fragment_listed_count = fragment_listed_count
        self.fragment_listed_url = fragment_listed_url
        self.start_date = start_date
        self.end_date = end_date
        self.average_price = average_price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.listed_count is not None:
            flags |= (1 << 0)
        if self.fragment_listed_count is not None:
            flags |= (1 << 1)
        if self.fragment_listed_url is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.start_date or 0)
        writer.write_int32(self.end_date or 0)
        writer.write_int64(self.average_price or 0)
        if self.listed_count is not None:
            writer.write_int32(self.listed_count or 0)
        if self.fragment_listed_count is not None:
            writer.write_int32(self.fragment_listed_count or 0)
        if self.fragment_listed_url is not None:
            writer.write_string(self.fragment_listed_url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAuctionStateFinished':
        flags = reader.read_uint32()
        start_date = reader.read_int32()
        end_date = reader.read_int32()
        average_price = reader.read_int64()
        listed_count = reader.read_int32() if (flags & (1 << 0)) else None
        fragment_listed_count = reader.read_int32() if (flags & (1 << 1)) else None
        fragment_listed_url = reader.read_string() if (flags & (1 << 1)) else None
        return cls(start_date=start_date, end_date=end_date, average_price=average_price, listed_count=listed_count, fragment_listed_count=fragment_listed_count, fragment_listed_url=fragment_listed_url)


@register_tl
class StarGiftAuctionUserState(TLObject):
    ID: int = 0x2eeed1c4

    def __init__(self, returned: bool = False, bid_amount: Any = None, bid_date: Any = None, min_bid_amount: Any = None, bid_peer: Any = None, acquired_count: Any = None) -> None:
        self.returned = returned
        self.bid_amount = bid_amount
        self.bid_date = bid_date
        self.min_bid_amount = min_bid_amount
        self.bid_peer = bid_peer
        self.acquired_count = acquired_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.returned:
            flags |= (1 << 1)
        if self.bid_amount is not None:
            flags |= (1 << 0)
        if self.bid_date is not None:
            flags |= (1 << 0)
        if self.min_bid_amount is not None:
            flags |= (1 << 0)
        if self.bid_peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.bid_amount is not None:
            writer.write_int64(self.bid_amount or 0)
        if self.bid_date is not None:
            writer.write_int32(self.bid_date or 0)
        if self.min_bid_amount is not None:
            writer.write_int64(self.min_bid_amount or 0)
        if self.bid_peer is not None:
            if self.bid_peer is not None and hasattr(self.bid_peer, 'write'): self.bid_peer.write(writer)
        writer.write_int32(self.acquired_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAuctionUserState':
        flags = reader.read_uint32()
        returned = bool(flags & (1 << 1))
        bid_amount = reader.read_int64() if (flags & (1 << 0)) else None
        bid_date = reader.read_int32() if (flags & (1 << 0)) else None
        min_bid_amount = reader.read_int64() if (flags & (1 << 0)) else None
        bid_peer = reader.read_object() if (flags & (1 << 0)) else None
        acquired_count = reader.read_int32()
        return cls(returned=returned, bid_amount=bid_amount, bid_date=bid_date, min_bid_amount=min_bid_amount, bid_peer=bid_peer, acquired_count=acquired_count)


@register_tl
class PaymentsStarGiftAuctionState(TLObject):
    ID: int = 0x6b39f4ec

    def __init__(self, gift: Any = None, state: Any = None, user_state: Any = None, timeout: Any = None, users: Any = None, chats: Any = None) -> None:
        self.gift = gift
        self.state = state
        self.user_state = user_state
        self.timeout = timeout
        self.users = users
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        if self.state is not None and hasattr(self.state, 'write'): self.state.write(writer)
        if self.user_state is not None and hasattr(self.user_state, 'write'): self.user_state.write(writer)
        writer.write_int32(self.timeout or 0)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftAuctionState':
        gift = reader.read_object()
        state = reader.read_object()
        user_state = reader.read_object()
        timeout = reader.read_int32()
        users = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        return cls(gift=gift, state=state, user_state=user_state, timeout=timeout, users=users, chats=chats)


@register_tl
class StarGiftAuctionAcquiredGift(TLObject):
    ID: int = 0x42b00348

    def __init__(self, name_hidden: bool = False, message: Any = None, gift_num: Any = None, peer: Any = None, date: Any = None, bid_amount: Any = None, round: Any = None, pos: Any = None) -> None:
        self.name_hidden = name_hidden
        self.message = message
        self.gift_num = gift_num
        self.peer = peer
        self.date = date
        self.bid_amount = bid_amount
        self.round = round
        self.pos = pos

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.name_hidden:
            flags |= (1 << 0)
        if self.message is not None:
            flags |= (1 << 1)
        if self.gift_num is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.bid_amount or 0)
        writer.write_int32(self.round or 0)
        writer.write_int32(self.pos or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        if self.gift_num is not None:
            writer.write_int32(self.gift_num or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAuctionAcquiredGift':
        flags = reader.read_uint32()
        name_hidden = bool(flags & (1 << 0))
        peer = reader.read_object()
        date = reader.read_int32()
        bid_amount = reader.read_int64()
        round = reader.read_int32()
        pos = reader.read_int32()
        message = reader.read_object() if (flags & (1 << 1)) else None
        gift_num = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(name_hidden=name_hidden, peer=peer, date=date, bid_amount=bid_amount, round=round, pos=pos, message=message, gift_num=gift_num)


@register_tl
class PaymentsStarGiftAuctionAcquiredGifts(TLObject):
    ID: int = 0x7d5bd1f0

    def __init__(self, gifts: Any = None, users: Any = None, chats: Any = None) -> None:
        self.gifts = gifts
        self.users = users
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.gifts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftAuctionAcquiredGifts':
        gifts = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        return cls(gifts=gifts, users=users, chats=chats)


@register_tl
class StarGiftActiveAuctionState(TLObject):
    ID: int = 0xd31bc45d

    def __init__(self, gift: Any = None, state: Any = None, user_state: Any = None) -> None:
        self.gift = gift
        self.state = state
        self.user_state = user_state

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        if self.state is not None and hasattr(self.state, 'write'): self.state.write(writer)
        if self.user_state is not None and hasattr(self.user_state, 'write'): self.user_state.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftActiveAuctionState':
        gift = reader.read_object()
        state = reader.read_object()
        user_state = reader.read_object()
        return cls(gift=gift, state=state, user_state=user_state)


@register_tl
class PaymentsStarGiftActiveAuctionsNotModified(TLObject):
    ID: int = 0xdb33dad0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftActiveAuctionsNotModified':
        return cls()


@register_tl
class PaymentsStarGiftActiveAuctions(TLObject):
    ID: int = 0xaef6abbc

    def __init__(self, auctions: Any = None, users: Any = None, chats: Any = None) -> None:
        self.auctions = auctions
        self.users = users
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.auctions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftActiveAuctions':
        auctions = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        return cls(auctions=auctions, users=users, chats=chats)


@register_tl
class InputStarGiftAuction(TLObject):
    ID: int = 0x2e16c98

    def __init__(self, gift_id: Any = None) -> None:
        self.gift_id = gift_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStarGiftAuction':
        gift_id = reader.read_int64()
        return cls(gift_id=gift_id)


@register_tl
class InputStarGiftAuctionSlug(TLObject):
    ID: int = 0x7ab58308

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStarGiftAuctionSlug':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class Passkey(TLObject):
    ID: int = 0x98613ebf

    def __init__(self, software_emoji_id: Any = None, last_usage_date: Any = None, id: Any = None, name: Any = None, date: Any = None) -> None:
        self.software_emoji_id = software_emoji_id
        self.last_usage_date = last_usage_date
        self.id = id
        self.name = name
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.software_emoji_id is not None:
            flags |= (1 << 0)
        if self.last_usage_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.id or '')
        writer.write_string(self.name or '')
        writer.write_int32(self.date or 0)
        if self.software_emoji_id is not None:
            writer.write_int64(self.software_emoji_id or 0)
        if self.last_usage_date is not None:
            writer.write_int32(self.last_usage_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Passkey':
        flags = reader.read_uint32()
        id = reader.read_string()
        name = reader.read_string()
        date = reader.read_int32()
        software_emoji_id = reader.read_int64() if (flags & (1 << 0)) else None
        last_usage_date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(id=id, name=name, date=date, software_emoji_id=software_emoji_id, last_usage_date=last_usage_date)


@register_tl
class AccountPasskeys(TLObject):
    ID: int = 0xf8e0aa1c

    def __init__(self, passkeys: Any = None) -> None:
        self.passkeys = passkeys

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.passkeys or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPasskeys':
        passkeys = reader.read_vector(lambda r: reader.read_object())
        return cls(passkeys=passkeys)


@register_tl
class AccountPasskeyRegistrationOptions(TLObject):
    ID: int = 0xe16b5ce1

    def __init__(self, options: Any = None) -> None:
        self.options = options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.options is not None and hasattr(self.options, 'write'): self.options.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPasskeyRegistrationOptions':
        options = reader.read_object()
        return cls(options=options)


@register_tl
class AuthPasskeyLoginOptions(TLObject):
    ID: int = 0xe2037789

    def __init__(self, options: Any = None) -> None:
        self.options = options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.options is not None and hasattr(self.options, 'write'): self.options.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthPasskeyLoginOptions':
        options = reader.read_object()
        return cls(options=options)


@register_tl
class InputPasskeyResponseRegister(TLObject):
    ID: int = 0x3e63935c

    def __init__(self, client_data: Any = None, attestation_data: Any = None) -> None:
        self.client_data = client_data
        self.attestation_data = attestation_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.client_data is not None and hasattr(self.client_data, 'write'): self.client_data.write(writer)
        writer.write_bytes(self.attestation_data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPasskeyResponseRegister':
        client_data = reader.read_object()
        attestation_data = reader.read_bytes()
        return cls(client_data=client_data, attestation_data=attestation_data)


@register_tl
class InputPasskeyResponseLogin(TLObject):
    ID: int = 0xc31fc14a

    def __init__(self, client_data: Any = None, authenticator_data: Any = None, signature: Any = None, user_handle: Any = None) -> None:
        self.client_data = client_data
        self.authenticator_data = authenticator_data
        self.signature = signature
        self.user_handle = user_handle

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.client_data is not None and hasattr(self.client_data, 'write'): self.client_data.write(writer)
        writer.write_bytes(self.authenticator_data or b'')
        writer.write_bytes(self.signature or b'')
        writer.write_string(self.user_handle or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPasskeyResponseLogin':
        client_data = reader.read_object()
        authenticator_data = reader.read_bytes()
        signature = reader.read_bytes()
        user_handle = reader.read_string()
        return cls(client_data=client_data, authenticator_data=authenticator_data, signature=signature, user_handle=user_handle)


@register_tl
class InputPasskeyCredentialPublicKey(TLObject):
    ID: int = 0x3c27b78f

    def __init__(self, id: Any = None, raw_id: Any = None, response: Any = None) -> None:
        self.id = id
        self.raw_id = raw_id
        self.response = response

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_string(self.raw_id or '')
        if self.response is not None and hasattr(self.response, 'write'): self.response.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPasskeyCredentialPublicKey':
        id = reader.read_string()
        raw_id = reader.read_string()
        response = reader.read_object()
        return cls(id=id, raw_id=raw_id, response=response)


@register_tl
class StarGiftBackground(TLObject):
    ID: int = 0xaff56398

    def __init__(self, center_color: Any = None, edge_color: Any = None, text_color: Any = None) -> None:
        self.center_color = center_color
        self.edge_color = edge_color
        self.text_color = text_color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.center_color or 0)
        writer.write_int32(self.edge_color or 0)
        writer.write_int32(self.text_color or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftBackground':
        center_color = reader.read_int32()
        edge_color = reader.read_int32()
        text_color = reader.read_int32()
        return cls(center_color=center_color, edge_color=edge_color, text_color=text_color)


@register_tl
class StarGiftAuctionRound(TLObject):
    ID: int = 0x3aae0528

    def __init__(self, num: Any = None, duration: Any = None) -> None:
        self.num = num
        self.duration = duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.num or 0)
        writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAuctionRound':
        num = reader.read_int32()
        duration = reader.read_int32()
        return cls(num=num, duration=duration)


@register_tl
class StarGiftAuctionRoundExtendable(TLObject):
    ID: int = 0xaa021e5

    def __init__(self, num: Any = None, duration: Any = None, extend_top: Any = None, extend_window: Any = None) -> None:
        self.num = num
        self.duration = duration
        self.extend_top = extend_top
        self.extend_window = extend_window

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.num or 0)
        writer.write_int32(self.duration or 0)
        writer.write_int32(self.extend_top or 0)
        writer.write_int32(self.extend_window or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAuctionRoundExtendable':
        num = reader.read_int32()
        duration = reader.read_int32()
        extend_top = reader.read_int32()
        extend_window = reader.read_int32()
        return cls(num=num, duration=duration, extend_top=extend_top, extend_window=extend_window)


@register_tl
class PaymentsStarGiftUpgradeAttributes(TLObject):
    ID: int = 0x46c6e36f

    def __init__(self, attributes: Any = None) -> None:
        self.attributes = attributes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsStarGiftUpgradeAttributes':
        attributes = reader.read_vector(lambda r: reader.read_object())
        return cls(attributes=attributes)


@register_tl
class MessagesEmojiGameOutcome(TLObject):
    ID: int = 0xda2ad647

    def __init__(self, seed: Any = None, stake_ton_amount: Any = None, ton_amount: Any = None) -> None:
        self.seed = seed
        self.stake_ton_amount = stake_ton_amount
        self.ton_amount = ton_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.seed or b'')
        writer.write_int64(self.stake_ton_amount or 0)
        writer.write_int64(self.ton_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEmojiGameOutcome':
        seed = reader.read_bytes()
        stake_ton_amount = reader.read_int64()
        ton_amount = reader.read_int64()
        return cls(seed=seed, stake_ton_amount=stake_ton_amount, ton_amount=ton_amount)


@register_tl
class MessagesEmojiGameUnavailable(TLObject):
    ID: int = 0x59e65335

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEmojiGameUnavailable':
        return cls()


@register_tl
class MessagesEmojiGameDiceInfo(TLObject):
    ID: int = 0x44e56023

    def __init__(self, plays_left: Any = None, game_hash: Any = None, prev_stake: Any = None, current_streak: Any = None, params: Any = None) -> None:
        self.plays_left = plays_left
        self.game_hash = game_hash
        self.prev_stake = prev_stake
        self.current_streak = current_streak
        self.params = params

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.plays_left is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.game_hash or '')
        writer.write_int64(self.prev_stake or 0)
        writer.write_int32(self.current_streak or 0)
        writer.write_vector(self.params or [], lambda w, x: w.write_int32(x))
        if self.plays_left is not None:
            writer.write_int32(self.plays_left or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEmojiGameDiceInfo':
        flags = reader.read_uint32()
        game_hash = reader.read_string()
        prev_stake = reader.read_int64()
        current_streak = reader.read_int32()
        params = reader.read_vector(lambda r: r.read_int32())
        plays_left = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(game_hash=game_hash, prev_stake=prev_stake, current_streak=current_streak, params=params, plays_left=plays_left)


@register_tl
class StarGiftAttributeRarity(TLObject):
    ID: int = 0x36437737

    def __init__(self, permille: Any = None) -> None:
        self.permille = permille

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.permille or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeRarity':
        permille = reader.read_int32()
        return cls(permille=permille)


@register_tl
class StarGiftAttributeRarityUncommon(TLObject):
    ID: int = 0xdbce6389

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeRarityUncommon':
        return cls()


@register_tl
class StarGiftAttributeRarityRare(TLObject):
    ID: int = 0xf08d516b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeRarityRare':
        return cls()


@register_tl
class StarGiftAttributeRarityEpic(TLObject):
    ID: int = 0x78fbf3a8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeRarityEpic':
        return cls()


@register_tl
class StarGiftAttributeRarityLegendary(TLObject):
    ID: int = 0xcef7e7a8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StarGiftAttributeRarityLegendary':
        return cls()


@register_tl
class KeyboardButtonStyle(TLObject):
    ID: int = 0x4fdd3430

    def __init__(self, bg_primary: bool = False, bg_danger: bool = False, bg_success: bool = False, icon: Any = None) -> None:
        self.bg_primary = bg_primary
        self.bg_danger = bg_danger
        self.bg_success = bg_success
        self.icon = icon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.bg_primary:
            flags |= (1 << 0)
        if self.bg_danger:
            flags |= (1 << 1)
        if self.bg_success:
            flags |= (1 << 2)
        if self.icon is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.icon is not None:
            writer.write_int64(self.icon or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonStyle':
        flags = reader.read_uint32()
        bg_primary = bool(flags & (1 << 0))
        bg_danger = bool(flags & (1 << 1))
        bg_success = bool(flags & (1 << 2))
        icon = reader.read_int64() if (flags & (1 << 3)) else None
        return cls(bg_primary=bg_primary, bg_danger=bg_danger, bg_success=bg_success, icon=icon)


@register_tl
class InputMessageReadMetric(TLObject):
    ID: int = 0x402b4495

    def __init__(self, msg_id: Any = None, view_id: Any = None, time_in_view_ms: Any = None, active_time_in_view_ms: Any = None, height_to_viewport_ratio_permille: Any = None, seen_range_ratio_permille: Any = None) -> None:
        self.msg_id = msg_id
        self.view_id = view_id
        self.time_in_view_ms = time_in_view_ms
        self.active_time_in_view_ms = active_time_in_view_ms
        self.height_to_viewport_ratio_permille = height_to_viewport_ratio_permille
        self.seen_range_ratio_permille = seen_range_ratio_permille

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.view_id or 0)
        writer.write_int32(self.time_in_view_ms or 0)
        writer.write_int32(self.active_time_in_view_ms or 0)
        writer.write_int32(self.height_to_viewport_ratio_permille or 0)
        writer.write_int32(self.seen_range_ratio_permille or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessageReadMetric':
        msg_id = reader.read_int32()
        view_id = reader.read_int64()
        time_in_view_ms = reader.read_int32()
        active_time_in_view_ms = reader.read_int32()
        height_to_viewport_ratio_permille = reader.read_int32()
        seen_range_ratio_permille = reader.read_int32()
        return cls(msg_id=msg_id, view_id=view_id, time_in_view_ms=time_in_view_ms, active_time_in_view_ms=active_time_in_view_ms, height_to_viewport_ratio_permille=height_to_viewport_ratio_permille, seen_range_ratio_permille=seen_range_ratio_permille)


@register_tl
class BotsExportedBotToken(TLObject):
    ID: int = 0x3c60b621

    def __init__(self, token: Any = None) -> None:
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsExportedBotToken':
        token = reader.read_string()
        return cls(token=token)


@register_tl
class BotsRequestedButton(TLObject):
    ID: int = 0xf13bbcd7

    def __init__(self, webapp_req_id: Any = None) -> None:
        self.webapp_req_id = webapp_req_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.webapp_req_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsRequestedButton':
        webapp_req_id = reader.read_string()
        return cls(webapp_req_id=webapp_req_id)


@register_tl
class MessagesComposedMessageWithAI(TLObject):
    ID: int = 0x90d7adfa

    def __init__(self, diff_text: Any = None, result_text: Any = None) -> None:
        self.diff_text = diff_text
        self.result_text = result_text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.diff_text is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.result_text is not None and hasattr(self.result_text, 'write'): self.result_text.write(writer)
        if self.diff_text is not None:
            if self.diff_text is not None and hasattr(self.diff_text, 'write'): self.diff_text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesComposedMessageWithAI':
        flags = reader.read_uint32()
        result_text = reader.read_object()
        diff_text = reader.read_object() if (flags & (1 << 0)) else None
        return cls(result_text=result_text, diff_text=diff_text)


@register_tl
class StatsPollStats(TLObject):
    ID: int = 0x2999beed

    def __init__(self, votes_graph: Any = None) -> None:
        self.votes_graph = votes_graph

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.votes_graph is not None and hasattr(self.votes_graph, 'write'): self.votes_graph.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsPollStats':
        votes_graph = reader.read_object()
        return cls(votes_graph=votes_graph)


@register_tl
class InputAiComposeToneDefault(TLObject):
    ID: int = 0x1fe9a9bf

    def __init__(self, tone: Any = None) -> None:
        self.tone = tone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.tone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputAiComposeToneDefault':
        tone = reader.read_string()
        return cls(tone=tone)


@register_tl
class InputAiComposeToneID(TLObject):
    ID: int = 0x773c080

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputAiComposeToneID':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputAiComposeToneSlug(TLObject):
    ID: int = 0x1fa01357

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputAiComposeToneSlug':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class AiComposeTone(TLObject):
    ID: int = 0xcff63ea9

    def __init__(self, creator: bool = False, emoji_id: Any = None, prompt: Any = None, installs_count: Any = None, author_id: Any = None, example_english: Any = None, id: Any = None, access_hash: Any = None, slug: Any = None, title: Any = None) -> None:
        self.creator = creator
        self.emoji_id = emoji_id
        self.prompt = prompt
        self.installs_count = installs_count
        self.author_id = author_id
        self.example_english = example_english
        self.id = id
        self.access_hash = access_hash
        self.slug = slug
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.creator:
            flags |= (1 << 0)
        if self.emoji_id is not None:
            flags |= (1 << 1)
        if self.prompt is not None:
            flags |= (1 << 4)
        if self.installs_count is not None:
            flags |= (1 << 2)
        if self.author_id is not None:
            flags |= (1 << 3)
        if self.example_english is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_string(self.slug or '')
        writer.write_string(self.title or '')
        if self.emoji_id is not None:
            writer.write_int64(self.emoji_id or 0)
        if self.prompt is not None:
            writer.write_string(self.prompt or '')
        if self.installs_count is not None:
            writer.write_int32(self.installs_count or 0)
        if self.author_id is not None:
            writer.write_int64(self.author_id or 0)
        if self.example_english is not None:
            if self.example_english is not None and hasattr(self.example_english, 'write'): self.example_english.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AiComposeTone':
        flags = reader.read_uint32()
        creator = bool(flags & (1 << 0))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        slug = reader.read_string()
        title = reader.read_string()
        emoji_id = reader.read_int64() if (flags & (1 << 1)) else None
        prompt = reader.read_string() if (flags & (1 << 4)) else None
        installs_count = reader.read_int32() if (flags & (1 << 2)) else None
        author_id = reader.read_int64() if (flags & (1 << 3)) else None
        example_english = reader.read_object() if (flags & (1 << 5)) else None
        return cls(creator=creator, id=id, access_hash=access_hash, slug=slug, title=title, emoji_id=emoji_id, prompt=prompt, installs_count=installs_count, author_id=author_id, example_english=example_english)


@register_tl
class AiComposeToneDefault(TLObject):
    ID: int = 0x9bad6414

    def __init__(self, tone: Any = None, emoji_id: Any = None, title: Any = None) -> None:
        self.tone = tone
        self.emoji_id = emoji_id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.tone or '')
        writer.write_int64(self.emoji_id or 0)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AiComposeToneDefault':
        tone = reader.read_string()
        emoji_id = reader.read_int64()
        title = reader.read_string()
        return cls(tone=tone, emoji_id=emoji_id, title=title)


@register_tl
class AicomposeTonesNotModified(TLObject):
    ID: int = 0xc1f46103

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeTonesNotModified':
        return cls()


@register_tl
class AicomposeTones(TLObject):
    ID: int = 0x6c9d0efe

    def __init__(self, hash: Any = None, tones: Any = None, users: Any = None) -> None:
        self.hash = hash
        self.tones = tones
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.tones or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AicomposeTones':
        hash = reader.read_int64()
        tones = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, tones=tones, users=users)


@register_tl
class AiComposeToneExample(TLObject):
    ID: int = 0xf1d628ec

    def __init__(self, from_: Any = None, to: Any = None) -> None:
        self.from_ = from_
        self.to = to

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.from_ is not None and hasattr(self.from_, 'write'): self.from_.write(writer)
        if self.to is not None and hasattr(self.to, 'write'): self.to.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AiComposeToneExample':
        from_ = reader.read_object()
        to = reader.read_object()
        return cls(from_=from_, to=to)


@register_tl
class BotsAccessSettings(TLObject):
    ID: int = 0xdd1fbf93

    def __init__(self, restricted: bool = False, add_users: Any = None) -> None:
        self.restricted = restricted
        self.add_users = add_users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.restricted:
            flags |= (1 << 0)
        if self.add_users is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.add_users is not None:
            writer.write_vector(self.add_users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsAccessSettings':
        flags = reader.read_uint32()
        restricted = bool(flags & (1 << 0))
        add_users = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        return cls(restricted=restricted, add_users=add_users)

