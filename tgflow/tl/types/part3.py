from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl

@register_tl
class MessageActionPrizeStars(TLObject):
    ID: int = 0xb00c47a2

    def __init__(self, unclaimed: bool = False, stars: Any = None, transaction_id: Any = None, boost_peer: Any = None, giveaway_msg_id: Any = None) -> None:
        self.unclaimed = unclaimed
        self.stars = stars
        self.transaction_id = transaction_id
        self.boost_peer = boost_peer
        self.giveaway_msg_id = giveaway_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unclaimed:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)
        writer.write_string(str(self.transaction_id or ''))
        if hasattr(self.boost_peer, 'write'):
            self.boost_peer.write(writer)
        else:
            writer.write_bytes(self.boost_peer or b'')
        writer.write_int32(self.giveaway_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPrizeStars':
        flags = reader.read_uint32()
        unclaimed = bool(flags & (1 << 0))
        stars = reader.read_int64()
        transaction_id = reader.read_string()
        boost_peer = reader.read_object()
        giveaway_msg_id = reader.read_int32()
        return cls(unclaimed=unclaimed, stars=stars, transaction_id=transaction_id, boost_peer=boost_peer, giveaway_msg_id=giveaway_msg_id)
@register_tl
class MessageActionStarGift(TLObject):
    ID: int = 0xea2c31d3

    def __init__(self, name_hidden: bool = False, saved: bool = False, converted: bool = False, upgraded: bool = False, refunded: bool = False, can_upgrade: bool = False, prepaid_upgrade: bool = False, upgrade_separate: bool = False, auction_acquired: bool = False, gift: Any = None, message: Any = None, convert_stars: Any = None, upgrade_msg_id: Any = None, upgrade_stars: Any = None, from_id: Any = None, peer: Any = None, saved_id: Any = None, prepaid_upgrade_hash: Any = None, gift_msg_id: Any = None, to_id: Any = None, gift_num: Any = None) -> None:
        self.name_hidden = name_hidden
        self.saved = saved
        self.converted = converted
        self.upgraded = upgraded
        self.refunded = refunded
        self.can_upgrade = can_upgrade
        self.prepaid_upgrade = prepaid_upgrade
        self.upgrade_separate = upgrade_separate
        self.auction_acquired = auction_acquired
        self.gift = gift
        self.message = message
        self.convert_stars = convert_stars
        self.upgrade_msg_id = upgrade_msg_id
        self.upgrade_stars = upgrade_stars
        self.from_id = from_id
        self.peer = peer
        self.saved_id = saved_id
        self.prepaid_upgrade_hash = prepaid_upgrade_hash
        self.gift_msg_id = gift_msg_id
        self.to_id = to_id
        self.gift_num = gift_num

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.name_hidden:
            flags |= (1 << 0)
        if self.saved:
            flags |= (1 << 2)
        if self.converted:
            flags |= (1 << 3)
        if self.upgraded:
            flags |= (1 << 5)
        if self.refunded:
            flags |= (1 << 9)
        if self.can_upgrade:
            flags |= (1 << 10)
        if self.prepaid_upgrade:
            flags |= (1 << 13)
        if self.upgrade_separate:
            flags |= (1 << 16)
        if self.auction_acquired:
            flags |= (1 << 17)
        if self.message is not None:
            flags |= (1 << 1)
        if self.convert_stars is not None:
            flags |= (1 << 4)
        if self.upgrade_msg_id is not None:
            flags |= (1 << 5)
        if self.upgrade_stars is not None:
            flags |= (1 << 8)
        if self.from_id is not None:
            flags |= (1 << 11)
        if self.peer is not None:
            flags |= (1 << 12)
        if self.saved_id is not None:
            flags |= (1 << 12)
        if self.prepaid_upgrade_hash is not None:
            flags |= (1 << 14)
        if self.gift_msg_id is not None:
            flags |= (1 << 15)
        if self.to_id is not None:
            flags |= (1 << 18)
        if self.gift_num is not None:
            flags |= (1 << 19)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if self.message is not None:
            if hasattr(self.message, 'write'):
                self.message.write(writer)
            else:
                writer.write_bytes(self.message or b'')
        if self.convert_stars is not None:
            writer.write_int64(self.convert_stars or 0)
        if self.upgrade_msg_id is not None:
            writer.write_int32(self.upgrade_msg_id or 0)
        if self.upgrade_stars is not None:
            writer.write_int64(self.upgrade_stars or 0)
        if self.from_id is not None:
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if self.saved_id is not None:
            writer.write_int64(self.saved_id or 0)
        if self.prepaid_upgrade_hash is not None:
            writer.write_string(str(self.prepaid_upgrade_hash or ''))
        if self.gift_msg_id is not None:
            writer.write_int32(self.gift_msg_id or 0)
        if self.to_id is not None:
            if hasattr(self.to_id, 'write'):
                self.to_id.write(writer)
            else:
                writer.write_bytes(self.to_id or b'')
        if self.gift_num is not None:
            writer.write_int32(self.gift_num or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGift':
        flags = reader.read_uint32()
        name_hidden = bool(flags & (1 << 0))
        saved = bool(flags & (1 << 2))
        converted = bool(flags & (1 << 3))
        upgraded = bool(flags & (1 << 5))
        refunded = bool(flags & (1 << 9))
        can_upgrade = bool(flags & (1 << 10))
        prepaid_upgrade = bool(flags & (1 << 13))
        upgrade_separate = bool(flags & (1 << 16))
        auction_acquired = bool(flags & (1 << 17))
        gift = reader.read_object()
        message = None
        if flags & (1 << 1):
            message = reader.read_object()
        convert_stars = None
        if flags & (1 << 4):
            convert_stars = reader.read_int64()
        upgrade_msg_id = None
        if flags & (1 << 5):
            upgrade_msg_id = reader.read_int32()
        upgrade_stars = None
        if flags & (1 << 8):
            upgrade_stars = reader.read_int64()
        from_id = None
        if flags & (1 << 11):
            from_id = reader.read_object()
        peer = None
        if flags & (1 << 12):
            peer = reader.read_object()
        saved_id = None
        if flags & (1 << 12):
            saved_id = reader.read_int64()
        prepaid_upgrade_hash = None
        if flags & (1 << 14):
            prepaid_upgrade_hash = reader.read_string()
        gift_msg_id = None
        if flags & (1 << 15):
            gift_msg_id = reader.read_int32()
        to_id = None
        if flags & (1 << 18):
            to_id = reader.read_object()
        gift_num = None
        if flags & (1 << 19):
            gift_num = reader.read_int32()
        return cls(name_hidden=name_hidden, saved=saved, converted=converted, upgraded=upgraded, refunded=refunded, can_upgrade=can_upgrade, prepaid_upgrade=prepaid_upgrade, upgrade_separate=upgrade_separate, auction_acquired=auction_acquired, gift=gift, message=message, convert_stars=convert_stars, upgrade_msg_id=upgrade_msg_id, upgrade_stars=upgrade_stars, from_id=from_id, peer=peer, saved_id=saved_id, prepaid_upgrade_hash=prepaid_upgrade_hash, gift_msg_id=gift_msg_id, to_id=to_id, gift_num=gift_num)
@register_tl
class MessageActionStarGiftUnique(TLObject):
    ID: int = 0xe6c31522

    def __init__(self, upgrade: bool = False, transferred: bool = False, saved: bool = False, refunded: bool = False, prepaid_upgrade: bool = False, assigned: bool = False, from_offer: bool = False, craft: bool = False, gift: Any = None, can_export_at: Any = None, transfer_stars: Any = None, from_id: Any = None, peer: Any = None, saved_id: Any = None, resale_amount: Any = None, can_transfer_at: Any = None, can_resell_at: Any = None, drop_original_details_stars: Any = None, can_craft_at: Any = None) -> None:
        self.upgrade = upgrade
        self.transferred = transferred
        self.saved = saved
        self.refunded = refunded
        self.prepaid_upgrade = prepaid_upgrade
        self.assigned = assigned
        self.from_offer = from_offer
        self.craft = craft
        self.gift = gift
        self.can_export_at = can_export_at
        self.transfer_stars = transfer_stars
        self.from_id = from_id
        self.peer = peer
        self.saved_id = saved_id
        self.resale_amount = resale_amount
        self.can_transfer_at = can_transfer_at
        self.can_resell_at = can_resell_at
        self.drop_original_details_stars = drop_original_details_stars
        self.can_craft_at = can_craft_at

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.upgrade:
            flags |= (1 << 0)
        if self.transferred:
            flags |= (1 << 1)
        if self.saved:
            flags |= (1 << 2)
        if self.refunded:
            flags |= (1 << 5)
        if self.prepaid_upgrade:
            flags |= (1 << 11)
        if self.assigned:
            flags |= (1 << 13)
        if self.from_offer:
            flags |= (1 << 14)
        if self.craft:
            flags |= (1 << 16)
        if self.can_export_at is not None:
            flags |= (1 << 3)
        if self.transfer_stars is not None:
            flags |= (1 << 4)
        if self.from_id is not None:
            flags |= (1 << 6)
        if self.peer is not None:
            flags |= (1 << 7)
        if self.saved_id is not None:
            flags |= (1 << 7)
        if self.resale_amount is not None:
            flags |= (1 << 8)
        if self.can_transfer_at is not None:
            flags |= (1 << 9)
        if self.can_resell_at is not None:
            flags |= (1 << 10)
        if self.drop_original_details_stars is not None:
            flags |= (1 << 12)
        if self.can_craft_at is not None:
            flags |= (1 << 15)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if self.can_export_at is not None:
            writer.write_int32(self.can_export_at or 0)
        if self.transfer_stars is not None:
            writer.write_int64(self.transfer_stars or 0)
        if self.from_id is not None:
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if self.saved_id is not None:
            writer.write_int64(self.saved_id or 0)
        if self.resale_amount is not None:
            if hasattr(self.resale_amount, 'write'):
                self.resale_amount.write(writer)
            else:
                writer.write_bytes(self.resale_amount or b'')
        if self.can_transfer_at is not None:
            writer.write_int32(self.can_transfer_at or 0)
        if self.can_resell_at is not None:
            writer.write_int32(self.can_resell_at or 0)
        if self.drop_original_details_stars is not None:
            writer.write_int64(self.drop_original_details_stars or 0)
        if self.can_craft_at is not None:
            writer.write_int32(self.can_craft_at or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGiftUnique':
        flags = reader.read_uint32()
        upgrade = bool(flags & (1 << 0))
        transferred = bool(flags & (1 << 1))
        saved = bool(flags & (1 << 2))
        refunded = bool(flags & (1 << 5))
        prepaid_upgrade = bool(flags & (1 << 11))
        assigned = bool(flags & (1 << 13))
        from_offer = bool(flags & (1 << 14))
        craft = bool(flags & (1 << 16))
        gift = reader.read_object()
        can_export_at = None
        if flags & (1 << 3):
            can_export_at = reader.read_int32()
        transfer_stars = None
        if flags & (1 << 4):
            transfer_stars = reader.read_int64()
        from_id = None
        if flags & (1 << 6):
            from_id = reader.read_object()
        peer = None
        if flags & (1 << 7):
            peer = reader.read_object()
        saved_id = None
        if flags & (1 << 7):
            saved_id = reader.read_int64()
        resale_amount = None
        if flags & (1 << 8):
            resale_amount = reader.read_object()
        can_transfer_at = None
        if flags & (1 << 9):
            can_transfer_at = reader.read_int32()
        can_resell_at = None
        if flags & (1 << 10):
            can_resell_at = reader.read_int32()
        drop_original_details_stars = None
        if flags & (1 << 12):
            drop_original_details_stars = reader.read_int64()
        can_craft_at = None
        if flags & (1 << 15):
            can_craft_at = reader.read_int32()
        return cls(upgrade=upgrade, transferred=transferred, saved=saved, refunded=refunded, prepaid_upgrade=prepaid_upgrade, assigned=assigned, from_offer=from_offer, craft=craft, gift=gift, can_export_at=can_export_at, transfer_stars=transfer_stars, from_id=from_id, peer=peer, saved_id=saved_id, resale_amount=resale_amount, can_transfer_at=can_transfer_at, can_resell_at=can_resell_at, drop_original_details_stars=drop_original_details_stars, can_craft_at=can_craft_at)
@register_tl
class MessageActionPaidMessagesRefunded(TLObject):
    ID: int = 0xac1f1fcd

    def __init__(self, count: Any = None, stars: Any = None) -> None:
        self.count = count
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaidMessagesRefunded':
        count = reader.read_int32()
        stars = reader.read_int64()
        return cls(count=count, stars=stars)
@register_tl
class MessageActionPaidMessagesPrice(TLObject):
    ID: int = 0x84b88578

    def __init__(self, broadcast_messages_allowed: bool = False, stars: Any = None) -> None:
        self.broadcast_messages_allowed = broadcast_messages_allowed
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast_messages_allowed:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaidMessagesPrice':
        flags = reader.read_uint32()
        broadcast_messages_allowed = bool(flags & (1 << 0))
        stars = reader.read_int64()
        return cls(broadcast_messages_allowed=broadcast_messages_allowed, stars=stars)
@register_tl
class MessageActionConferenceCall(TLObject):
    ID: int = 0x2ffe2f7a

    def __init__(self, missed: bool = False, active: bool = False, video: bool = False, call_id: Any = None, duration: Any = None, other_participants: Any = None) -> None:
        self.missed = missed
        self.active = active
        self.video = video
        self.call_id = call_id
        self.duration = duration
        self.other_participants = other_participants

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.missed:
            flags |= (1 << 0)
        if self.active:
            flags |= (1 << 1)
        if self.video:
            flags |= (1 << 4)
        if self.duration is not None:
            flags |= (1 << 2)
        if self.other_participants is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int64(self.call_id or 0)
        if self.duration is not None:
            writer.write_int32(self.duration or 0)
        if self.other_participants is not None:
            writer.write_vector(self.other_participants or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionConferenceCall':
        flags = reader.read_uint32()
        missed = bool(flags & (1 << 0))
        active = bool(flags & (1 << 1))
        video = bool(flags & (1 << 4))
        call_id = reader.read_int64()
        duration = None
        if flags & (1 << 2):
            duration = reader.read_int32()
        other_participants = None
        if flags & (1 << 3):
            other_participants = reader.read_vector(lambda r: r.read_object())
        return cls(missed=missed, active=active, video=video, call_id=call_id, duration=duration, other_participants=other_participants)
@register_tl
class MessageActionTodoCompletions(TLObject):
    ID: int = 0xcc7c5c89

    def __init__(self, completed: Any = None, incompleted: Any = None) -> None:
        self.completed = completed
        self.incompleted = incompleted

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.completed or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.incompleted or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTodoCompletions':
        completed = reader.read_vector(lambda r: r.read_object())
        incompleted = reader.read_vector(lambda r: r.read_object())
        return cls(completed=completed, incompleted=incompleted)
@register_tl
class MessageActionTodoAppendTasks(TLObject):
    ID: int = 0xc7edbc83

    def __init__(self, list: Any = None) -> None:
        self.list = list

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.list or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTodoAppendTasks':
        list = reader.read_vector(lambda r: r.read_object())
        return cls(list=list)
@register_tl
class MessageActionSuggestedPostApproval(TLObject):
    ID: int = 0xee7a1596

    def __init__(self, rejected: bool = False, balance_too_low: bool = False, reject_comment: Any = None, schedule_date: Any = None, price: Any = None) -> None:
        self.rejected = rejected
        self.balance_too_low = balance_too_low
        self.reject_comment = reject_comment
        self.schedule_date = schedule_date
        self.price = price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rejected:
            flags |= (1 << 0)
        if self.balance_too_low:
            flags |= (1 << 1)
        if self.reject_comment is not None:
            flags |= (1 << 2)
        if self.schedule_date is not None:
            flags |= (1 << 3)
        if self.price is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.reject_comment is not None:
            writer.write_string(str(self.reject_comment or ''))
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.price is not None:
            if hasattr(self.price, 'write'):
                self.price.write(writer)
            else:
                writer.write_bytes(self.price or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestedPostApproval':
        flags = reader.read_uint32()
        rejected = bool(flags & (1 << 0))
        balance_too_low = bool(flags & (1 << 1))
        reject_comment = None
        if flags & (1 << 2):
            reject_comment = reader.read_string()
        schedule_date = None
        if flags & (1 << 3):
            schedule_date = reader.read_int32()
        price = None
        if flags & (1 << 4):
            price = reader.read_object()
        return cls(rejected=rejected, balance_too_low=balance_too_low, reject_comment=reject_comment, schedule_date=schedule_date, price=price)
@register_tl
class MessageActionSuggestedPostSuccess(TLObject):
    ID: int = 0x95ddcf69

    def __init__(self, price: Any = None) -> None:
        self.price = price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.price, 'write'):
            self.price.write(writer)
        else:
            writer.write_bytes(self.price or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestedPostSuccess':
        price = reader.read_object()
        return cls(price=price)
@register_tl
class MessageActionSuggestedPostRefund(TLObject):
    ID: int = 0x69f916f8

    def __init__(self, payer_initiated: bool = False) -> None:
        self.payer_initiated = payer_initiated

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.payer_initiated:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestedPostRefund':
        flags = reader.read_uint32()
        payer_initiated = bool(flags & (1 << 0))
        return cls(payer_initiated=payer_initiated)
@register_tl
class MessageActionGiftTon(TLObject):
    ID: int = 0xa8a3c699

    def __init__(self, currency: Any = None, amount: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, transaction_id: Any = None) -> None:
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.transaction_id = transaction_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.transaction_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)
        writer.write_string(str(self.crypto_currency or ''))
        writer.write_int64(self.crypto_amount or 0)
        if self.transaction_id is not None:
            writer.write_string(str(self.transaction_id or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftTon':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        crypto_currency = reader.read_string()
        crypto_amount = reader.read_int64()
        transaction_id = None
        if flags & (1 << 0):
            transaction_id = reader.read_string()
        return cls(currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, transaction_id=transaction_id)
@register_tl
class MessageActionSuggestBirthday(TLObject):
    ID: int = 0x2c8f2a25

    def __init__(self, birthday: Any = None) -> None:
        self.birthday = birthday

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.birthday, 'write'):
            self.birthday.write(writer)
        else:
            writer.write_bytes(self.birthday or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestBirthday':
        birthday = reader.read_object()
        return cls(birthday=birthday)
@register_tl
class MessageActionStarGiftPurchaseOffer(TLObject):
    ID: int = 0x774278d4

    def __init__(self, accepted: bool = False, declined: bool = False, gift: Any = None, price: Any = None, expires_at: Any = None) -> None:
        self.accepted = accepted
        self.declined = declined
        self.gift = gift
        self.price = price
        self.expires_at = expires_at

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accepted:
            flags |= (1 << 0)
        if self.declined:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if hasattr(self.price, 'write'):
            self.price.write(writer)
        else:
            writer.write_bytes(self.price or b'')
        writer.write_int32(self.expires_at or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGiftPurchaseOffer':
        flags = reader.read_uint32()
        accepted = bool(flags & (1 << 0))
        declined = bool(flags & (1 << 1))
        gift = reader.read_object()
        price = reader.read_object()
        expires_at = reader.read_int32()
        return cls(accepted=accepted, declined=declined, gift=gift, price=price, expires_at=expires_at)
@register_tl
class MessageActionStarGiftPurchaseOfferDeclined(TLObject):
    ID: int = 0x73ada76b

    def __init__(self, expired: bool = False, gift: Any = None, price: Any = None) -> None:
        self.expired = expired
        self.gift = gift
        self.price = price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.expired:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if hasattr(self.price, 'write'):
            self.price.write(writer)
        else:
            writer.write_bytes(self.price or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGiftPurchaseOfferDeclined':
        flags = reader.read_uint32()
        expired = bool(flags & (1 << 0))
        gift = reader.read_object()
        price = reader.read_object()
        return cls(expired=expired, gift=gift, price=price)
@register_tl
class MessageActionNewCreatorPending(TLObject):
    ID: int = 0xb07ed085

    def __init__(self, new_creator_id: Any = None) -> None:
        self.new_creator_id = new_creator_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.new_creator_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionNewCreatorPending':
        new_creator_id = reader.read_int64()
        return cls(new_creator_id=new_creator_id)
@register_tl
class MessageActionChangeCreator(TLObject):
    ID: int = 0xe188503b

    def __init__(self, new_creator_id: Any = None) -> None:
        self.new_creator_id = new_creator_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.new_creator_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChangeCreator':
        new_creator_id = reader.read_int64()
        return cls(new_creator_id=new_creator_id)
@register_tl
class MessageActionNoForwardsToggle(TLObject):
    ID: int = 0xbf7d6572

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.prev_value))
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionNoForwardsToggle':
        prev_value = reader.read_bool()
        new_value = reader.read_bool()
        return cls(prev_value=prev_value, new_value=new_value)
@register_tl
class MessageActionNoForwardsRequest(TLObject):
    ID: int = 0x3e2793ba

    def __init__(self, expired: bool = False, prev_value: Any = None, new_value: Any = None) -> None:
        self.expired = expired
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.expired:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_bool(bool(self.prev_value))
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionNoForwardsRequest':
        flags = reader.read_uint32()
        expired = bool(flags & (1 << 0))
        prev_value = reader.read_bool()
        new_value = reader.read_bool()
        return cls(expired=expired, prev_value=prev_value, new_value=new_value)
@register_tl
class MessageActionPollAppendAnswer(TLObject):
    ID: int = 0x9da1cd6c

    def __init__(self, answer: Any = None) -> None:
        self.answer = answer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.answer, 'write'):
            self.answer.write(writer)
        else:
            writer.write_bytes(self.answer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPollAppendAnswer':
        answer = reader.read_object()
        return cls(answer=answer)
@register_tl
class MessageActionPollDeleteAnswer(TLObject):
    ID: int = 0x399674dc

    def __init__(self, answer: Any = None) -> None:
        self.answer = answer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.answer, 'write'):
            self.answer.write(writer)
        else:
            writer.write_bytes(self.answer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPollDeleteAnswer':
        answer = reader.read_object()
        return cls(answer=answer)
@register_tl
class MessageActionManagedBotCreated(TLObject):
    ID: int = 0x16605e3e

    def __init__(self, bot_id: Any = None) -> None:
        self.bot_id = bot_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bot_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionManagedBotCreated':
        bot_id = reader.read_int64()
        return cls(bot_id=bot_id)
@register_tl
class Dialog(TLObject):
    ID: int = 0xfc89f7f3

    def __init__(self, pinned: bool = False, unread_mark: bool = False, view_forum_as_messages: bool = False, peer: Any = None, top_message: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, unread_mentions_count: Any = None, unread_reactions_count: Any = None, unread_poll_votes_count: Any = None, notify_settings: Any = None, pts: Any = None, draft: Any = None, folder_id: Any = None, ttl_period: Any = None) -> None:
        self.pinned = pinned
        self.unread_mark = unread_mark
        self.view_forum_as_messages = view_forum_as_messages
        self.peer = peer
        self.top_message = top_message
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_reactions_count = unread_reactions_count
        self.unread_poll_votes_count = unread_poll_votes_count
        self.notify_settings = notify_settings
        self.pts = pts
        self.draft = draft
        self.folder_id = folder_id
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 2)
        if self.unread_mark:
            flags |= (1 << 3)
        if self.view_forum_as_messages:
            flags |= (1 << 6)
        if self.pts is not None:
            flags |= (1 << 0)
        if self.draft is not None:
            flags |= (1 << 1)
        if self.folder_id is not None:
            flags |= (1 << 4)
        if self.ttl_period is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.read_inbox_max_id or 0)
        writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        writer.write_int32(self.unread_mentions_count or 0)
        writer.write_int32(self.unread_reactions_count or 0)
        writer.write_int32(self.unread_poll_votes_count or 0)
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')
        if self.pts is not None:
            writer.write_int32(self.pts or 0)
        if self.draft is not None:
            if hasattr(self.draft, 'write'):
                self.draft.write(writer)
            else:
                writer.write_bytes(self.draft or b'')
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Dialog':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 2))
        unread_mark = bool(flags & (1 << 3))
        view_forum_as_messages = bool(flags & (1 << 6))
        peer = reader.read_object()
        top_message = reader.read_int32()
        read_inbox_max_id = reader.read_int32()
        read_outbox_max_id = reader.read_int32()
        unread_count = reader.read_int32()
        unread_mentions_count = reader.read_int32()
        unread_reactions_count = reader.read_int32()
        unread_poll_votes_count = reader.read_int32()
        notify_settings = reader.read_object()
        pts = None
        if flags & (1 << 0):
            pts = reader.read_int32()
        draft = None
        if flags & (1 << 1):
            draft = reader.read_object()
        folder_id = None
        if flags & (1 << 4):
            folder_id = reader.read_int32()
        ttl_period = None
        if flags & (1 << 5):
            ttl_period = reader.read_int32()
        return cls(pinned=pinned, unread_mark=unread_mark, view_forum_as_messages=view_forum_as_messages, peer=peer, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, unread_poll_votes_count=unread_poll_votes_count, notify_settings=notify_settings, pts=pts, draft=draft, folder_id=folder_id, ttl_period=ttl_period)
@register_tl
class DialogFolder(TLObject):
    ID: int = 0x71bd134c

    def __init__(self, pinned: bool = False, folder: Any = None, peer: Any = None, top_message: Any = None, unread_muted_peers_count: Any = None, unread_unmuted_peers_count: Any = None, unread_muted_messages_count: Any = None, unread_unmuted_messages_count: Any = None) -> None:
        self.pinned = pinned
        self.folder = folder
        self.peer = peer
        self.top_message = top_message
        self.unread_muted_peers_count = unread_muted_peers_count
        self.unread_unmuted_peers_count = unread_unmuted_peers_count
        self.unread_muted_messages_count = unread_muted_messages_count
        self.unread_unmuted_messages_count = unread_unmuted_messages_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if hasattr(self.folder, 'write'):
            self.folder.write(writer)
        else:
            writer.write_bytes(self.folder or b'')
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.unread_muted_peers_count or 0)
        writer.write_int32(self.unread_unmuted_peers_count or 0)
        writer.write_int32(self.unread_muted_messages_count or 0)
        writer.write_int32(self.unread_unmuted_messages_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogFolder':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 2))
        folder = reader.read_object()
        peer = reader.read_object()
        top_message = reader.read_int32()
        unread_muted_peers_count = reader.read_int32()
        unread_unmuted_peers_count = reader.read_int32()
        unread_muted_messages_count = reader.read_int32()
        unread_unmuted_messages_count = reader.read_int32()
        return cls(pinned=pinned, folder=folder, peer=peer, top_message=top_message, unread_muted_peers_count=unread_muted_peers_count, unread_unmuted_peers_count=unread_unmuted_peers_count, unread_muted_messages_count=unread_muted_messages_count, unread_unmuted_messages_count=unread_unmuted_messages_count)
@register_tl
class PhotoEmpty(TLObject):
    ID: int = 0x2331b22d

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoEmpty':
        id = reader.read_int64()
        return cls(id=id)
@register_tl
class Photo(TLObject):
    ID: int = 0xfb197a65

    def __init__(self, has_stickers: bool = False, id: Any = None, access_hash: Any = None, file_reference: Any = None, date: Any = None, sizes: Any = None, video_sizes: Any = None, dc_id: Any = None) -> None:
        self.has_stickers = has_stickers
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.date = date
        self.sizes = sizes
        self.video_sizes = video_sizes
        self.dc_id = dc_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_stickers:
            flags |= (1 << 0)
        if self.video_sizes is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_bytes(self.file_reference or b'')
        writer.write_int32(self.date or 0)
        writer.write_vector(self.sizes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.video_sizes is not None:
            writer.write_vector(self.video_sizes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.dc_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Photo':
        flags = reader.read_uint32()
        has_stickers = bool(flags & (1 << 0))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        date = reader.read_int32()
        sizes = reader.read_vector(lambda r: r.read_object())
        video_sizes = None
        if flags & (1 << 1):
            video_sizes = reader.read_vector(lambda r: r.read_object())
        dc_id = reader.read_int32()
        return cls(has_stickers=has_stickers, id=id, access_hash=access_hash, file_reference=file_reference, date=date, sizes=sizes, video_sizes=video_sizes, dc_id=dc_id)
@register_tl
class PhotoSizeEmpty(TLObject):
    ID: int = 0xe17e23c

    def __init__(self, type: Any = None) -> None:
        self.type = type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSizeEmpty':
        type = reader.read_string()
        return cls(type=type)
@register_tl
class PhotoSize(TLObject):
    ID: int = 0x75c78e60

    def __init__(self, type: Any = None, w: Any = None, h: Any = None, size: Any = None) -> None:
        self.type = type
        self.w = w
        self.h = h
        self.size = size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSize':
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        return cls(type=type, w=w, h=h, size=size)
@register_tl
class PhotoCachedSize(TLObject):
    ID: int = 0x21e1ad6

    def __init__(self, type: Any = None, w: Any = None, h: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.w = w
        self.h = h
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoCachedSize':
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(type=type, w=w, h=h, bytes=bytes)
@register_tl
class PhotoStrippedSize(TLObject):
    ID: int = 0xe0b0bc2e

    def __init__(self, type: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoStrippedSize':
        type = reader.read_string()
        bytes = reader.read_bytes()
        return cls(type=type, bytes=bytes)
@register_tl
class PhotoSizeProgressive(TLObject):
    ID: int = 0xfa3efb95

    def __init__(self, type: Any = None, w: Any = None, h: Any = None, sizes: Any = None) -> None:
        self.type = type
        self.w = w
        self.h = h
        self.sizes = sizes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_vector(self.sizes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSizeProgressive':
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        sizes = reader.read_vector(lambda r: r.read_object())
        return cls(type=type, w=w, h=h, sizes=sizes)
@register_tl
class PhotoPathSize(TLObject):
    ID: int = 0xd8214d41

    def __init__(self, type: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoPathSize':
        type = reader.read_string()
        bytes = reader.read_bytes()
        return cls(type=type, bytes=bytes)
@register_tl
class GeoPointEmpty(TLObject):
    ID: int = 0x1117dd5f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'GeoPointEmpty':
        return cls()
@register_tl
class GeoPoint(TLObject):
    ID: int = 0xb2a2f663

    def __init__(self, long: Any = None, lat: Any = None, access_hash: Any = None, accuracy_radius: Any = None) -> None:
        self.long = long
        self.lat = lat
        self.access_hash = access_hash
        self.accuracy_radius = accuracy_radius

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accuracy_radius is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_double(float(self.long or 0.0))
        writer.write_double(float(self.lat or 0.0))
        writer.write_int64(self.access_hash or 0)
        if self.accuracy_radius is not None:
            writer.write_int32(self.accuracy_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GeoPoint':
        flags = reader.read_uint32()
        long = reader.read_double()
        lat = reader.read_double()
        access_hash = reader.read_int64()
        accuracy_radius = None
        if flags & (1 << 0):
            accuracy_radius = reader.read_int32()
        return cls(long=long, lat=lat, access_hash=access_hash, accuracy_radius=accuracy_radius)
@register_tl
class AuthSentCode(TLObject):
    ID: int = 0x5e002502

    def __init__(self, type: Any = None, phone_code_hash: Any = None, next_type: Any = None, timeout: Any = None) -> None:
        self.type = type
        self.phone_code_hash = phone_code_hash
        self.next_type = next_type
        self.timeout = timeout

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_type is not None:
            flags |= (1 << 1)
        if self.timeout is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if hasattr(self.type, 'write'):
            self.type.write(writer)
        else:
            writer.write_bytes(self.type or b'')
        writer.write_string(str(self.phone_code_hash or ''))
        if self.next_type is not None:
            if hasattr(self.next_type, 'write'):
                self.next_type.write(writer)
            else:
                writer.write_bytes(self.next_type or b'')
        if self.timeout is not None:
            writer.write_int32(self.timeout or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCode':
        flags = reader.read_uint32()
        type = reader.read_object()
        phone_code_hash = reader.read_string()
        next_type = None
        if flags & (1 << 1):
            next_type = reader.read_object()
        timeout = None
        if flags & (1 << 2):
            timeout = reader.read_int32()
        return cls(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)
@register_tl
class AuthSentCodeSuccess(TLObject):
    ID: int = 0x2390fe44

    def __init__(self, authorization: Any = None) -> None:
        self.authorization = authorization

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.authorization, 'write'):
            self.authorization.write(writer)
        else:
            writer.write_bytes(self.authorization or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeSuccess':
        authorization = reader.read_object()
        return cls(authorization=authorization)
@register_tl
class AuthSentCodePaymentRequired(TLObject):
    ID: int = 0xf8827ebf

    def __init__(self, store_product: Any = None, phone_code_hash: Any = None, support_email_address: Any = None, support_email_subject: Any = None, premium_days: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.store_product = store_product
        self.phone_code_hash = phone_code_hash
        self.support_email_address = support_email_address
        self.support_email_subject = support_email_subject
        self.premium_days = premium_days
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.store_product or ''))
        writer.write_string(str(self.phone_code_hash or ''))
        writer.write_string(str(self.support_email_address or ''))
        writer.write_string(str(self.support_email_subject or ''))
        writer.write_int32(self.premium_days or 0)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodePaymentRequired':
        store_product = reader.read_string()
        phone_code_hash = reader.read_string()
        support_email_address = reader.read_string()
        support_email_subject = reader.read_string()
        premium_days = reader.read_int32()
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(store_product=store_product, phone_code_hash=phone_code_hash, support_email_address=support_email_address, support_email_subject=support_email_subject, premium_days=premium_days, currency=currency, amount=amount)
@register_tl
class AuthAuthorization(TLObject):
    ID: int = 0x2ea2c0d4

    def __init__(self, setup_password_required: bool = False, otherwise_relogin_days: Any = None, tmp_sessions: Any = None, future_auth_token: Any = None, user: Any = None) -> None:
        self.setup_password_required = setup_password_required
        self.otherwise_relogin_days = otherwise_relogin_days
        self.tmp_sessions = tmp_sessions
        self.future_auth_token = future_auth_token
        self.user = user

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.setup_password_required:
            flags |= (1 << 1)
        if self.otherwise_relogin_days is not None:
            flags |= (1 << 1)
        if self.tmp_sessions is not None:
            flags |= (1 << 0)
        if self.future_auth_token is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.otherwise_relogin_days is not None:
            writer.write_int32(self.otherwise_relogin_days or 0)
        if self.tmp_sessions is not None:
            writer.write_int32(self.tmp_sessions or 0)
        if self.future_auth_token is not None:
            writer.write_bytes(self.future_auth_token or b'')
        if hasattr(self.user, 'write'):
            self.user.write(writer)
        else:
            writer.write_bytes(self.user or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthAuthorization':
        flags = reader.read_uint32()
        setup_password_required = bool(flags & (1 << 1))
        otherwise_relogin_days = None
        if flags & (1 << 1):
            otherwise_relogin_days = reader.read_int32()
        tmp_sessions = None
        if flags & (1 << 0):
            tmp_sessions = reader.read_int32()
        future_auth_token = None
        if flags & (1 << 2):
            future_auth_token = reader.read_bytes()
        user = reader.read_object()
        return cls(setup_password_required=setup_password_required, otherwise_relogin_days=otherwise_relogin_days, tmp_sessions=tmp_sessions, future_auth_token=future_auth_token, user=user)
@register_tl
class AuthAuthorizationSignUpRequired(TLObject):
    ID: int = 0x44747e9a

    def __init__(self, terms_of_service: Any = None) -> None:
        self.terms_of_service = terms_of_service

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.terms_of_service is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.terms_of_service is not None:
            if hasattr(self.terms_of_service, 'write'):
                self.terms_of_service.write(writer)
            else:
                writer.write_bytes(self.terms_of_service or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthAuthorizationSignUpRequired':
        flags = reader.read_uint32()
        terms_of_service = None
        if flags & (1 << 0):
            terms_of_service = reader.read_object()
        return cls(terms_of_service=terms_of_service)
@register_tl
class AuthExportedAuthorization(TLObject):
    ID: int = 0xb434e2b8

    def __init__(self, id: Any = None, bytes: Any = None) -> None:
        self.id = id
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthExportedAuthorization':
        id = reader.read_int64()
        bytes = reader.read_bytes()
        return cls(id=id, bytes=bytes)
@register_tl
class InputNotifyPeer(TLObject):
    ID: int = 0xb8bc5b0c

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyPeer':
        peer = reader.read_object()
        return cls(peer=peer)
@register_tl
class InputNotifyUsers(TLObject):
    ID: int = 0x193b4417

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyUsers':
        return cls()
@register_tl
class InputNotifyChats(TLObject):
    ID: int = 0x4a95e84e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyChats':
        return cls()
@register_tl
class InputNotifyBroadcasts(TLObject):
    ID: int = 0xb1db7c7e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyBroadcasts':
        return cls()
@register_tl
class InputNotifyForumTopic(TLObject):
    ID: int = 0x5c467992

    def __init__(self, peer: Any = None, top_msg_id: Any = None) -> None:
        self.peer = peer
        self.top_msg_id = top_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.top_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyForumTopic':
        peer = reader.read_object()
        top_msg_id = reader.read_int32()
        return cls(peer=peer, top_msg_id=top_msg_id)
@register_tl
class InputPeerNotifySettings(TLObject):
    ID: int = 0xcacb6ae2

    def __init__(self, show_previews: Any = None, silent: Any = None, mute_until: Any = None, sound: Any = None, stories_muted: Any = None, stories_hide_sender: Any = None, stories_sound: Any = None) -> None:
        self.show_previews = show_previews
        self.silent = silent
        self.mute_until = mute_until
        self.sound = sound
        self.stories_muted = stories_muted
        self.stories_hide_sender = stories_hide_sender
        self.stories_sound = stories_sound

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.show_previews is not None:
            flags |= (1 << 0)
        if self.silent is not None:
            flags |= (1 << 1)
        if self.mute_until is not None:
            flags |= (1 << 2)
        if self.sound is not None:
            flags |= (1 << 3)
        if self.stories_muted is not None:
            flags |= (1 << 6)
        if self.stories_hide_sender is not None:
            flags |= (1 << 7)
        if self.stories_sound is not None:
            flags |= (1 << 8)
        writer.write_uint32(flags)
        if self.show_previews is not None:
            writer.write_bool(bool(self.show_previews))
        if self.silent is not None:
            writer.write_bool(bool(self.silent))
        if self.mute_until is not None:
            writer.write_int32(self.mute_until or 0)
        if self.sound is not None:
            if hasattr(self.sound, 'write'):
                self.sound.write(writer)
            else:
                writer.write_bytes(self.sound or b'')
        if self.stories_muted is not None:
            writer.write_bool(bool(self.stories_muted))
        if self.stories_hide_sender is not None:
            writer.write_bool(bool(self.stories_hide_sender))
        if self.stories_sound is not None:
            if hasattr(self.stories_sound, 'write'):
                self.stories_sound.write(writer)
            else:
                writer.write_bytes(self.stories_sound or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerNotifySettings':
        flags = reader.read_uint32()
        show_previews = None
        if flags & (1 << 0):
            show_previews = reader.read_bool()
        silent = None
        if flags & (1 << 1):
            silent = reader.read_bool()
        mute_until = None
        if flags & (1 << 2):
            mute_until = reader.read_int32()
        sound = None
        if flags & (1 << 3):
            sound = reader.read_object()
        stories_muted = None
        if flags & (1 << 6):
            stories_muted = reader.read_bool()
        stories_hide_sender = None
        if flags & (1 << 7):
            stories_hide_sender = reader.read_bool()
        stories_sound = None
        if flags & (1 << 8):
            stories_sound = reader.read_object()
        return cls(show_previews=show_previews, silent=silent, mute_until=mute_until, sound=sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_sound=stories_sound)
@register_tl
class PeerNotifySettings(TLObject):
    ID: int = 0x99622c0c

    def __init__(self, show_previews: Any = None, silent: Any = None, mute_until: Any = None, ios_sound: Any = None, android_sound: Any = None, other_sound: Any = None, stories_muted: Any = None, stories_hide_sender: Any = None, stories_ios_sound: Any = None, stories_android_sound: Any = None, stories_other_sound: Any = None) -> None:
        self.show_previews = show_previews
        self.silent = silent
        self.mute_until = mute_until
        self.ios_sound = ios_sound
        self.android_sound = android_sound
        self.other_sound = other_sound
        self.stories_muted = stories_muted
        self.stories_hide_sender = stories_hide_sender
        self.stories_ios_sound = stories_ios_sound
        self.stories_android_sound = stories_android_sound
        self.stories_other_sound = stories_other_sound

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.show_previews is not None:
            flags |= (1 << 0)
        if self.silent is not None:
            flags |= (1 << 1)
        if self.mute_until is not None:
            flags |= (1 << 2)
        if self.ios_sound is not None:
            flags |= (1 << 3)
        if self.android_sound is not None:
            flags |= (1 << 4)
        if self.other_sound is not None:
            flags |= (1 << 5)
        if self.stories_muted is not None:
            flags |= (1 << 6)
        if self.stories_hide_sender is not None:
            flags |= (1 << 7)
        if self.stories_ios_sound is not None:
            flags |= (1 << 8)
        if self.stories_android_sound is not None:
            flags |= (1 << 9)
        if self.stories_other_sound is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.show_previews is not None:
            writer.write_bool(bool(self.show_previews))
        if self.silent is not None:
            writer.write_bool(bool(self.silent))
        if self.mute_until is not None:
            writer.write_int32(self.mute_until or 0)
        if self.ios_sound is not None:
            if hasattr(self.ios_sound, 'write'):
                self.ios_sound.write(writer)
            else:
                writer.write_bytes(self.ios_sound or b'')
        if self.android_sound is not None:
            if hasattr(self.android_sound, 'write'):
                self.android_sound.write(writer)
            else:
                writer.write_bytes(self.android_sound or b'')
        if self.other_sound is not None:
            if hasattr(self.other_sound, 'write'):
                self.other_sound.write(writer)
            else:
                writer.write_bytes(self.other_sound or b'')
        if self.stories_muted is not None:
            writer.write_bool(bool(self.stories_muted))
        if self.stories_hide_sender is not None:
            writer.write_bool(bool(self.stories_hide_sender))
        if self.stories_ios_sound is not None:
            if hasattr(self.stories_ios_sound, 'write'):
                self.stories_ios_sound.write(writer)
            else:
                writer.write_bytes(self.stories_ios_sound or b'')
        if self.stories_android_sound is not None:
            if hasattr(self.stories_android_sound, 'write'):
                self.stories_android_sound.write(writer)
            else:
                writer.write_bytes(self.stories_android_sound or b'')
        if self.stories_other_sound is not None:
            if hasattr(self.stories_other_sound, 'write'):
                self.stories_other_sound.write(writer)
            else:
                writer.write_bytes(self.stories_other_sound or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerNotifySettings':
        flags = reader.read_uint32()
        show_previews = None
        if flags & (1 << 0):
            show_previews = reader.read_bool()
        silent = None
        if flags & (1 << 1):
            silent = reader.read_bool()
        mute_until = None
        if flags & (1 << 2):
            mute_until = reader.read_int32()
        ios_sound = None
        if flags & (1 << 3):
            ios_sound = reader.read_object()
        android_sound = None
        if flags & (1 << 4):
            android_sound = reader.read_object()
        other_sound = None
        if flags & (1 << 5):
            other_sound = reader.read_object()
        stories_muted = None
        if flags & (1 << 6):
            stories_muted = reader.read_bool()
        stories_hide_sender = None
        if flags & (1 << 7):
            stories_hide_sender = reader.read_bool()
        stories_ios_sound = None
        if flags & (1 << 8):
            stories_ios_sound = reader.read_object()
        stories_android_sound = None
        if flags & (1 << 9):
            stories_android_sound = reader.read_object()
        stories_other_sound = None
        if flags & (1 << 10):
            stories_other_sound = reader.read_object()
        return cls(show_previews=show_previews, silent=silent, mute_until=mute_until, ios_sound=ios_sound, android_sound=android_sound, other_sound=other_sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_ios_sound=stories_ios_sound, stories_android_sound=stories_android_sound, stories_other_sound=stories_other_sound)
@register_tl
class PeerSettings(TLObject):
    ID: int = 0xf47741f7

    def __init__(self, report_spam: bool = False, add_contact: bool = False, block_contact: bool = False, share_contact: bool = False, need_contacts_exception: bool = False, report_geo: bool = False, autoarchived: bool = False, invite_members: bool = False, request_chat_broadcast: bool = False, business_bot_paused: bool = False, business_bot_can_reply: bool = False, geo_distance: Any = None, request_chat_title: Any = None, request_chat_date: Any = None, business_bot_id: Any = None, business_bot_manage_url: Any = None, charge_paid_message_stars: Any = None, registration_month: Any = None, phone_country: Any = None, name_change_date: Any = None, photo_change_date: Any = None) -> None:
        self.report_spam = report_spam
        self.add_contact = add_contact
        self.block_contact = block_contact
        self.share_contact = share_contact
        self.need_contacts_exception = need_contacts_exception
        self.report_geo = report_geo
        self.autoarchived = autoarchived
        self.invite_members = invite_members
        self.request_chat_broadcast = request_chat_broadcast
        self.business_bot_paused = business_bot_paused
        self.business_bot_can_reply = business_bot_can_reply
        self.geo_distance = geo_distance
        self.request_chat_title = request_chat_title
        self.request_chat_date = request_chat_date
        self.business_bot_id = business_bot_id
        self.business_bot_manage_url = business_bot_manage_url
        self.charge_paid_message_stars = charge_paid_message_stars
        self.registration_month = registration_month
        self.phone_country = phone_country
        self.name_change_date = name_change_date
        self.photo_change_date = photo_change_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.report_spam:
            flags |= (1 << 0)
        if self.add_contact:
            flags |= (1 << 1)
        if self.block_contact:
            flags |= (1 << 2)
        if self.share_contact:
            flags |= (1 << 3)
        if self.need_contacts_exception:
            flags |= (1 << 4)
        if self.report_geo:
            flags |= (1 << 5)
        if self.autoarchived:
            flags |= (1 << 7)
        if self.invite_members:
            flags |= (1 << 8)
        if self.request_chat_broadcast:
            flags |= (1 << 10)
        if self.business_bot_paused:
            flags |= (1 << 11)
        if self.business_bot_can_reply:
            flags |= (1 << 12)
        if self.geo_distance is not None:
            flags |= (1 << 6)
        if self.request_chat_title is not None:
            flags |= (1 << 9)
        if self.request_chat_date is not None:
            flags |= (1 << 9)
        if self.business_bot_id is not None:
            flags |= (1 << 13)
        if self.business_bot_manage_url is not None:
            flags |= (1 << 13)
        if self.charge_paid_message_stars is not None:
            flags |= (1 << 14)
        if self.registration_month is not None:
            flags |= (1 << 15)
        if self.phone_country is not None:
            flags |= (1 << 16)
        if self.name_change_date is not None:
            flags |= (1 << 17)
        if self.photo_change_date is not None:
            flags |= (1 << 18)
        writer.write_uint32(flags)
        if self.geo_distance is not None:
            writer.write_int32(self.geo_distance or 0)
        if self.request_chat_title is not None:
            writer.write_string(str(self.request_chat_title or ''))
        if self.request_chat_date is not None:
            writer.write_int32(self.request_chat_date or 0)
        if self.business_bot_id is not None:
            writer.write_int64(self.business_bot_id or 0)
        if self.business_bot_manage_url is not None:
            writer.write_string(str(self.business_bot_manage_url or ''))
        if self.charge_paid_message_stars is not None:
            writer.write_int64(self.charge_paid_message_stars or 0)
        if self.registration_month is not None:
            writer.write_string(str(self.registration_month or ''))
        if self.phone_country is not None:
            writer.write_string(str(self.phone_country or ''))
        if self.name_change_date is not None:
            writer.write_int32(self.name_change_date or 0)
        if self.photo_change_date is not None:
            writer.write_int32(self.photo_change_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerSettings':
        flags = reader.read_uint32()
        report_spam = bool(flags & (1 << 0))
        add_contact = bool(flags & (1 << 1))
        block_contact = bool(flags & (1 << 2))
        share_contact = bool(flags & (1 << 3))
        need_contacts_exception = bool(flags & (1 << 4))
        report_geo = bool(flags & (1 << 5))
        autoarchived = bool(flags & (1 << 7))
        invite_members = bool(flags & (1 << 8))
        request_chat_broadcast = bool(flags & (1 << 10))
        business_bot_paused = bool(flags & (1 << 11))
        business_bot_can_reply = bool(flags & (1 << 12))
        geo_distance = None
        if flags & (1 << 6):
            geo_distance = reader.read_int32()
        request_chat_title = None
        if flags & (1 << 9):
            request_chat_title = reader.read_string()
        request_chat_date = None
        if flags & (1 << 9):
            request_chat_date = reader.read_int32()
        business_bot_id = None
        if flags & (1 << 13):
            business_bot_id = reader.read_int64()
        business_bot_manage_url = None
        if flags & (1 << 13):
            business_bot_manage_url = reader.read_string()
        charge_paid_message_stars = None
        if flags & (1 << 14):
            charge_paid_message_stars = reader.read_int64()
        registration_month = None
        if flags & (1 << 15):
            registration_month = reader.read_string()
        phone_country = None
        if flags & (1 << 16):
            phone_country = reader.read_string()
        name_change_date = None
        if flags & (1 << 17):
            name_change_date = reader.read_int32()
        photo_change_date = None
        if flags & (1 << 18):
            photo_change_date = reader.read_int32()
        return cls(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact, share_contact=share_contact, need_contacts_exception=need_contacts_exception, report_geo=report_geo, autoarchived=autoarchived, invite_members=invite_members, request_chat_broadcast=request_chat_broadcast, business_bot_paused=business_bot_paused, business_bot_can_reply=business_bot_can_reply, geo_distance=geo_distance, request_chat_title=request_chat_title, request_chat_date=request_chat_date, business_bot_id=business_bot_id, business_bot_manage_url=business_bot_manage_url, charge_paid_message_stars=charge_paid_message_stars, registration_month=registration_month, phone_country=phone_country, name_change_date=name_change_date, photo_change_date=photo_change_date)
@register_tl
class WallPaper(TLObject):
    ID: int = 0xa437c3ed

    def __init__(self, id: Any = None, creator: bool = False, default: bool = False, pattern: bool = False, dark: bool = False, access_hash: Any = None, slug: Any = None, document: Any = None, settings: Any = None) -> None:
        self.id = id
        self.creator = creator
        self.default = default
        self.pattern = pattern
        self.dark = dark
        self.access_hash = access_hash
        self.slug = slug
        self.document = document
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.creator:
            flags |= (1 << 0)
        if self.default:
            flags |= (1 << 1)
        if self.pattern:
            flags |= (1 << 3)
        if self.dark:
            flags |= (1 << 4)
        if self.settings is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_string(str(self.slug or ''))
        if hasattr(self.document, 'write'):
            self.document.write(writer)
        else:
            writer.write_bytes(self.document or b'')
        if self.settings is not None:
            if hasattr(self.settings, 'write'):
                self.settings.write(writer)
            else:
                writer.write_bytes(self.settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'WallPaper':
        flags = reader.read_uint32()
        id = reader.read_int64()
        creator = bool(flags & (1 << 0))
        default = bool(flags & (1 << 1))
        pattern = bool(flags & (1 << 3))
        dark = bool(flags & (1 << 4))
        access_hash = reader.read_int64()
        slug = reader.read_string()
        document = reader.read_object()
        settings = None
        if flags & (1 << 2):
            settings = reader.read_object()
        return cls(id=id, creator=creator, default=default, pattern=pattern, dark=dark, access_hash=access_hash, slug=slug, document=document, settings=settings)
@register_tl
class WallPaperNoFile(TLObject):
    ID: int = 0xe0804116

    def __init__(self, id: Any = None, default: bool = False, dark: bool = False, settings: Any = None) -> None:
        self.id = id
        self.default = default
        self.dark = dark
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.default:
            flags |= (1 << 1)
        if self.dark:
            flags |= (1 << 4)
        if self.settings is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.settings is not None:
            if hasattr(self.settings, 'write'):
                self.settings.write(writer)
            else:
                writer.write_bytes(self.settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'WallPaperNoFile':
        flags = reader.read_uint32()
        id = reader.read_int64()
        default = bool(flags & (1 << 1))
        dark = bool(flags & (1 << 4))
        settings = None
        if flags & (1 << 2):
            settings = reader.read_object()
        return cls(id=id, default=default, dark=dark, settings=settings)
@register_tl
class InputReportReasonSpam(TLObject):
    ID: int = 0x58dbcab8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonSpam':
        return cls()
@register_tl
class InputReportReasonViolence(TLObject):
    ID: int = 0x1e22c78d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonViolence':
        return cls()
@register_tl
class InputReportReasonPornography(TLObject):
    ID: int = 0x2e59d922

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonPornography':
        return cls()
@register_tl
class InputReportReasonChildAbuse(TLObject):
    ID: int = 0xadf44ee3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonChildAbuse':
        return cls()
@register_tl
class InputReportReasonOther(TLObject):
    ID: int = 0xc1e4a2b1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonOther':
        return cls()
@register_tl
class InputReportReasonCopyright(TLObject):
    ID: int = 0x9b89f93a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonCopyright':
        return cls()
@register_tl
class InputReportReasonGeoIrrelevant(TLObject):
    ID: int = 0xdbd4feed

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonGeoIrrelevant':
        return cls()
@register_tl
class InputReportReasonFake(TLObject):
    ID: int = 0xf5ddd6e7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonFake':
        return cls()
@register_tl
class InputReportReasonIllegalDrugs(TLObject):
    ID: int = 0xa8eb2be

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonIllegalDrugs':
        return cls()
@register_tl
class InputReportReasonPersonalDetails(TLObject):
    ID: int = 0x9ec7863d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonPersonalDetails':
        return cls()
@register_tl
class UserFull(TLObject):
    ID: int = 0x6cbe645

    def __init__(self, blocked: bool = False, phone_calls_available: bool = False, phone_calls_private: bool = False, can_pin_message: bool = False, has_scheduled: bool = False, video_calls_available: bool = False, voice_messages_forbidden: bool = False, translations_disabled: bool = False, stories_pinned_available: bool = False, blocked_my_stories_from: bool = False, wallpaper_overridden: bool = False, contact_require_premium: bool = False, read_dates_private: bool = False, sponsored_enabled: bool = False, can_view_revenue: bool = False, bot_can_manage_emoji_status: bool = False, display_gifts_button: bool = False, noforwards_my_enabled: bool = False, noforwards_peer_enabled: bool = False, unofficial_security_risk: bool = False, id: Any = None, about: Any = None, settings: Any = None, personal_photo: Any = None, profile_photo: Any = None, fallback_photo: Any = None, notify_settings: Any = None, bot_info: Any = None, pinned_msg_id: Any = None, common_chats_count: Any = None, folder_id: Any = None, ttl_period: Any = None, theme: Any = None, private_forward_name: Any = None, bot_group_admin_rights: Any = None, bot_broadcast_admin_rights: Any = None, wallpaper: Any = None, stories: Any = None, business_work_hours: Any = None, business_location: Any = None, business_greeting_message: Any = None, business_away_message: Any = None, business_intro: Any = None, birthday: Any = None, personal_channel_id: Any = None, personal_channel_message: Any = None, stargifts_count: Any = None, starref_program: Any = None, bot_verification: Any = None, send_paid_messages_stars: Any = None, disallowed_gifts: Any = None, stars_rating: Any = None, stars_my_pending_rating: Any = None, stars_my_pending_rating_date: Any = None, main_tab: Any = None, saved_music: Any = None, note: Any = None, bot_manager_id: Any = None) -> None:
        self.blocked = blocked
        self.phone_calls_available = phone_calls_available
        self.phone_calls_private = phone_calls_private
        self.can_pin_message = can_pin_message
        self.has_scheduled = has_scheduled
        self.video_calls_available = video_calls_available
        self.voice_messages_forbidden = voice_messages_forbidden
        self.translations_disabled = translations_disabled
        self.stories_pinned_available = stories_pinned_available
        self.blocked_my_stories_from = blocked_my_stories_from
        self.wallpaper_overridden = wallpaper_overridden
        self.contact_require_premium = contact_require_premium
        self.read_dates_private = read_dates_private
        self.sponsored_enabled = sponsored_enabled
        self.can_view_revenue = can_view_revenue
        self.bot_can_manage_emoji_status = bot_can_manage_emoji_status
        self.display_gifts_button = display_gifts_button
        self.noforwards_my_enabled = noforwards_my_enabled
        self.noforwards_peer_enabled = noforwards_peer_enabled
        self.unofficial_security_risk = unofficial_security_risk
        self.id = id
        self.about = about
        self.settings = settings
        self.personal_photo = personal_photo
        self.profile_photo = profile_photo
        self.fallback_photo = fallback_photo
        self.notify_settings = notify_settings
        self.bot_info = bot_info
        self.pinned_msg_id = pinned_msg_id
        self.common_chats_count = common_chats_count
        self.folder_id = folder_id
        self.ttl_period = ttl_period
        self.theme = theme
        self.private_forward_name = private_forward_name
        self.bot_group_admin_rights = bot_group_admin_rights
        self.bot_broadcast_admin_rights = bot_broadcast_admin_rights
        self.wallpaper = wallpaper
        self.stories = stories
        self.business_work_hours = business_work_hours
        self.business_location = business_location
        self.business_greeting_message = business_greeting_message
        self.business_away_message = business_away_message
        self.business_intro = business_intro
        self.birthday = birthday
        self.personal_channel_id = personal_channel_id
        self.personal_channel_message = personal_channel_message
        self.stargifts_count = stargifts_count
        self.starref_program = starref_program
        self.bot_verification = bot_verification
        self.send_paid_messages_stars = send_paid_messages_stars
        self.disallowed_gifts = disallowed_gifts
        self.stars_rating = stars_rating
        self.stars_my_pending_rating = stars_my_pending_rating
        self.stars_my_pending_rating_date = stars_my_pending_rating_date
        self.main_tab = main_tab
        self.saved_music = saved_music
        self.note = note
        self.bot_manager_id = bot_manager_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blocked:
            flags |= (1 << 0)
        if self.phone_calls_available:
            flags |= (1 << 4)
        if self.phone_calls_private:
            flags |= (1 << 5)
        if self.can_pin_message:
            flags |= (1 << 7)
        if self.has_scheduled:
            flags |= (1 << 12)
        if self.video_calls_available:
            flags |= (1 << 13)
        if self.voice_messages_forbidden:
            flags |= (1 << 20)
        if self.translations_disabled:
            flags |= (1 << 23)
        if self.stories_pinned_available:
            flags |= (1 << 26)
        if self.blocked_my_stories_from:
            flags |= (1 << 27)
        if self.wallpaper_overridden:
            flags |= (1 << 28)
        if self.contact_require_premium:
            flags |= (1 << 29)
        if self.read_dates_private:
            flags |= (1 << 30)
        if self.sponsored_enabled:
            flags |= (1 << 7)
        if self.can_view_revenue:
            flags |= (1 << 9)
        if self.bot_can_manage_emoji_status:
            flags |= (1 << 10)
        if self.display_gifts_button:
            flags |= (1 << 16)
        if self.noforwards_my_enabled:
            flags |= (1 << 23)
        if self.noforwards_peer_enabled:
            flags |= (1 << 24)
        if self.unofficial_security_risk:
            flags |= (1 << 26)
        if self.about is not None:
            flags |= (1 << 1)
        if self.personal_photo is not None:
            flags |= (1 << 21)
        if self.profile_photo is not None:
            flags |= (1 << 2)
        if self.fallback_photo is not None:
            flags |= (1 << 22)
        if self.bot_info is not None:
            flags |= (1 << 3)
        if self.pinned_msg_id is not None:
            flags |= (1 << 6)
        if self.folder_id is not None:
            flags |= (1 << 11)
        if self.ttl_period is not None:
            flags |= (1 << 14)
        if self.theme is not None:
            flags |= (1 << 15)
        if self.private_forward_name is not None:
            flags |= (1 << 16)
        if self.bot_group_admin_rights is not None:
            flags |= (1 << 17)
        if self.bot_broadcast_admin_rights is not None:
            flags |= (1 << 18)
        if self.wallpaper is not None:
            flags |= (1 << 24)
        if self.stories is not None:
            flags |= (1 << 25)
        if self.business_work_hours is not None:
            flags |= (1 << 0)
        if self.business_location is not None:
            flags |= (1 << 1)
        if self.business_greeting_message is not None:
            flags |= (1 << 2)
        if self.business_away_message is not None:
            flags |= (1 << 3)
        if self.business_intro is not None:
            flags |= (1 << 4)
        if self.birthday is not None:
            flags |= (1 << 5)
        if self.personal_channel_id is not None:
            flags |= (1 << 6)
        if self.personal_channel_message is not None:
            flags |= (1 << 6)
        if self.stargifts_count is not None:
            flags |= (1 << 8)
        if self.starref_program is not None:
            flags |= (1 << 11)
        if self.bot_verification is not None:
            flags |= (1 << 12)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 14)
        if self.disallowed_gifts is not None:
            flags |= (1 << 15)
        if self.stars_rating is not None:
            flags |= (1 << 17)
        if self.stars_my_pending_rating is not None:
            flags |= (1 << 18)
        if self.stars_my_pending_rating_date is not None:
            flags |= (1 << 18)
        if self.main_tab is not None:
            flags |= (1 << 20)
        if self.saved_music is not None:
            flags |= (1 << 21)
        if self.note is not None:
            flags |= (1 << 22)
        if self.bot_manager_id is not None:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.about is not None:
            writer.write_string(str(self.about or ''))
        if hasattr(self.settings, 'write'):
            self.settings.write(writer)
        else:
            writer.write_bytes(self.settings or b'')
        if self.personal_photo is not None:
            if hasattr(self.personal_photo, 'write'):
                self.personal_photo.write(writer)
            else:
                writer.write_bytes(self.personal_photo or b'')
        if self.profile_photo is not None:
            if hasattr(self.profile_photo, 'write'):
                self.profile_photo.write(writer)
            else:
                writer.write_bytes(self.profile_photo or b'')
        if self.fallback_photo is not None:
            if hasattr(self.fallback_photo, 'write'):
                self.fallback_photo.write(writer)
            else:
                writer.write_bytes(self.fallback_photo or b'')
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')
        if self.bot_info is not None:
            if hasattr(self.bot_info, 'write'):
                self.bot_info.write(writer)
            else:
                writer.write_bytes(self.bot_info or b'')
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        writer.write_int32(self.common_chats_count or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.theme is not None:
            if hasattr(self.theme, 'write'):
                self.theme.write(writer)
            else:
                writer.write_bytes(self.theme or b'')
        if self.private_forward_name is not None:
            writer.write_string(str(self.private_forward_name or ''))
        if self.bot_group_admin_rights is not None:
            if hasattr(self.bot_group_admin_rights, 'write'):
                self.bot_group_admin_rights.write(writer)
            else:
                writer.write_bytes(self.bot_group_admin_rights or b'')
        if self.bot_broadcast_admin_rights is not None:
            if hasattr(self.bot_broadcast_admin_rights, 'write'):
                self.bot_broadcast_admin_rights.write(writer)
            else:
                writer.write_bytes(self.bot_broadcast_admin_rights or b'')
        if self.wallpaper is not None:
            if hasattr(self.wallpaper, 'write'):
                self.wallpaper.write(writer)
            else:
                writer.write_bytes(self.wallpaper or b'')
        if self.stories is not None:
            if hasattr(self.stories, 'write'):
                self.stories.write(writer)
            else:
                writer.write_bytes(self.stories or b'')
        if self.business_work_hours is not None:
            if hasattr(self.business_work_hours, 'write'):
                self.business_work_hours.write(writer)
            else:
                writer.write_bytes(self.business_work_hours or b'')
        if self.business_location is not None:
            if hasattr(self.business_location, 'write'):
                self.business_location.write(writer)
            else:
                writer.write_bytes(self.business_location or b'')
        if self.business_greeting_message is not None:
            if hasattr(self.business_greeting_message, 'write'):
                self.business_greeting_message.write(writer)
            else:
                writer.write_bytes(self.business_greeting_message or b'')
        if self.business_away_message is not None:
            if hasattr(self.business_away_message, 'write'):
                self.business_away_message.write(writer)
            else:
                writer.write_bytes(self.business_away_message or b'')
        if self.business_intro is not None:
            if hasattr(self.business_intro, 'write'):
                self.business_intro.write(writer)
            else:
                writer.write_bytes(self.business_intro or b'')
        if self.birthday is not None:
            if hasattr(self.birthday, 'write'):
                self.birthday.write(writer)
            else:
                writer.write_bytes(self.birthday or b'')
        if self.personal_channel_id is not None:
            writer.write_int64(self.personal_channel_id or 0)
        if self.personal_channel_message is not None:
            writer.write_int32(self.personal_channel_message or 0)
        if self.stargifts_count is not None:
            writer.write_int32(self.stargifts_count or 0)
        if self.starref_program is not None:
            if hasattr(self.starref_program, 'write'):
                self.starref_program.write(writer)
            else:
                writer.write_bytes(self.starref_program or b'')
        if self.bot_verification is not None:
            if hasattr(self.bot_verification, 'write'):
                self.bot_verification.write(writer)
            else:
                writer.write_bytes(self.bot_verification or b'')
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.disallowed_gifts is not None:
            if hasattr(self.disallowed_gifts, 'write'):
                self.disallowed_gifts.write(writer)
            else:
                writer.write_bytes(self.disallowed_gifts or b'')
        if self.stars_rating is not None:
            if hasattr(self.stars_rating, 'write'):
                self.stars_rating.write(writer)
            else:
                writer.write_bytes(self.stars_rating or b'')
        if self.stars_my_pending_rating is not None:
            if hasattr(self.stars_my_pending_rating, 'write'):
                self.stars_my_pending_rating.write(writer)
            else:
                writer.write_bytes(self.stars_my_pending_rating or b'')
        if self.stars_my_pending_rating_date is not None:
            writer.write_int32(self.stars_my_pending_rating_date or 0)
        if self.main_tab is not None:
            if hasattr(self.main_tab, 'write'):
                self.main_tab.write(writer)
            else:
                writer.write_bytes(self.main_tab or b'')
        if self.saved_music is not None:
            if hasattr(self.saved_music, 'write'):
                self.saved_music.write(writer)
            else:
                writer.write_bytes(self.saved_music or b'')
        if self.note is not None:
            if hasattr(self.note, 'write'):
                self.note.write(writer)
            else:
                writer.write_bytes(self.note or b'')
        if self.bot_manager_id is not None:
            writer.write_int64(self.bot_manager_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserFull':
        flags = reader.read_uint32()
        blocked = bool(flags & (1 << 0))
        phone_calls_available = bool(flags & (1 << 4))
        phone_calls_private = bool(flags & (1 << 5))
        can_pin_message = bool(flags & (1 << 7))
        has_scheduled = bool(flags & (1 << 12))
        video_calls_available = bool(flags & (1 << 13))
        voice_messages_forbidden = bool(flags & (1 << 20))
        translations_disabled = bool(flags & (1 << 23))
        stories_pinned_available = bool(flags & (1 << 26))
        blocked_my_stories_from = bool(flags & (1 << 27))
        wallpaper_overridden = bool(flags & (1 << 28))
        contact_require_premium = bool(flags & (1 << 29))
        read_dates_private = bool(flags & (1 << 30))
        sponsored_enabled = bool(flags & (1 << 7))
        can_view_revenue = bool(flags & (1 << 9))
        bot_can_manage_emoji_status = bool(flags & (1 << 10))
        display_gifts_button = bool(flags & (1 << 16))
        noforwards_my_enabled = bool(flags & (1 << 23))
        noforwards_peer_enabled = bool(flags & (1 << 24))
        unofficial_security_risk = bool(flags & (1 << 26))
        id = reader.read_int64()
        about = None
        if flags & (1 << 1):
            about = reader.read_string()
        settings = reader.read_object()
        personal_photo = None
        if flags & (1 << 21):
            personal_photo = reader.read_object()
        profile_photo = None
        if flags & (1 << 2):
            profile_photo = reader.read_object()
        fallback_photo = None
        if flags & (1 << 22):
            fallback_photo = reader.read_object()
        notify_settings = reader.read_object()
        bot_info = None
        if flags & (1 << 3):
            bot_info = reader.read_object()
        pinned_msg_id = None
        if flags & (1 << 6):
            pinned_msg_id = reader.read_int32()
        common_chats_count = reader.read_int32()
        folder_id = None
        if flags & (1 << 11):
            folder_id = reader.read_int32()
        ttl_period = None
        if flags & (1 << 14):
            ttl_period = reader.read_int32()
        theme = None
        if flags & (1 << 15):
            theme = reader.read_object()
        private_forward_name = None
        if flags & (1 << 16):
            private_forward_name = reader.read_string()
        bot_group_admin_rights = None
        if flags & (1 << 17):
            bot_group_admin_rights = reader.read_object()
        bot_broadcast_admin_rights = None
        if flags & (1 << 18):
            bot_broadcast_admin_rights = reader.read_object()
        wallpaper = None
        if flags & (1 << 24):
            wallpaper = reader.read_object()
        stories = None
        if flags & (1 << 25):
            stories = reader.read_object()
        business_work_hours = None
        if flags & (1 << 0):
            business_work_hours = reader.read_object()
        business_location = None
        if flags & (1 << 1):
            business_location = reader.read_object()
        business_greeting_message = None
        if flags & (1 << 2):
            business_greeting_message = reader.read_object()
        business_away_message = None
        if flags & (1 << 3):
            business_away_message = reader.read_object()
        business_intro = None
        if flags & (1 << 4):
            business_intro = reader.read_object()
        birthday = None
        if flags & (1 << 5):
            birthday = reader.read_object()
        personal_channel_id = None
        if flags & (1 << 6):
            personal_channel_id = reader.read_int64()
        personal_channel_message = None
        if flags & (1 << 6):
            personal_channel_message = reader.read_int32()
        stargifts_count = None
        if flags & (1 << 8):
            stargifts_count = reader.read_int32()
        starref_program = None
        if flags & (1 << 11):
            starref_program = reader.read_object()
        bot_verification = None
        if flags & (1 << 12):
            bot_verification = reader.read_object()
        send_paid_messages_stars = None
        if flags & (1 << 14):
            send_paid_messages_stars = reader.read_int64()
        disallowed_gifts = None
        if flags & (1 << 15):
            disallowed_gifts = reader.read_object()
        stars_rating = None
        if flags & (1 << 17):
            stars_rating = reader.read_object()
        stars_my_pending_rating = None
        if flags & (1 << 18):
            stars_my_pending_rating = reader.read_object()
        stars_my_pending_rating_date = None
        if flags & (1 << 18):
            stars_my_pending_rating_date = reader.read_int32()
        main_tab = None
        if flags & (1 << 20):
            main_tab = reader.read_object()
        saved_music = None
        if flags & (1 << 21):
            saved_music = reader.read_object()
        note = None
        if flags & (1 << 22):
            note = reader.read_object()
        bot_manager_id = None
        if flags & (1 << 25):
            bot_manager_id = reader.read_int64()
        return cls(blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, video_calls_available=video_calls_available, voice_messages_forbidden=voice_messages_forbidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, blocked_my_stories_from=blocked_my_stories_from, wallpaper_overridden=wallpaper_overridden, contact_require_premium=contact_require_premium, read_dates_private=read_dates_private, sponsored_enabled=sponsored_enabled, can_view_revenue=can_view_revenue, bot_can_manage_emoji_status=bot_can_manage_emoji_status, display_gifts_button=display_gifts_button, noforwards_my_enabled=noforwards_my_enabled, noforwards_peer_enabled=noforwards_peer_enabled, unofficial_security_risk=unofficial_security_risk, id=id, about=about, settings=settings, personal_photo=personal_photo, profile_photo=profile_photo, fallback_photo=fallback_photo, notify_settings=notify_settings, bot_info=bot_info, pinned_msg_id=pinned_msg_id, common_chats_count=common_chats_count, folder_id=folder_id, ttl_period=ttl_period, theme=theme, private_forward_name=private_forward_name, bot_group_admin_rights=bot_group_admin_rights, bot_broadcast_admin_rights=bot_broadcast_admin_rights, wallpaper=wallpaper, stories=stories, business_work_hours=business_work_hours, business_location=business_location, business_greeting_message=business_greeting_message, business_away_message=business_away_message, business_intro=business_intro, birthday=birthday, personal_channel_id=personal_channel_id, personal_channel_message=personal_channel_message, stargifts_count=stargifts_count, starref_program=starref_program, bot_verification=bot_verification, send_paid_messages_stars=send_paid_messages_stars, disallowed_gifts=disallowed_gifts, stars_rating=stars_rating, stars_my_pending_rating=stars_my_pending_rating, stars_my_pending_rating_date=stars_my_pending_rating_date, main_tab=main_tab, saved_music=saved_music, note=note, bot_manager_id=bot_manager_id)
@register_tl
class Contact(TLObject):
    ID: int = 0x145ade0b

    def __init__(self, user_id: Any = None, mutual: Any = None) -> None:
        self.user_id = user_id
        self.mutual = mutual

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_bool(bool(self.mutual))

    @classmethod
    def read(cls, reader: TLReader) -> 'Contact':
        user_id = reader.read_int64()
        mutual = reader.read_bool()
        return cls(user_id=user_id, mutual=mutual)
@register_tl
class ImportedContact(TLObject):
    ID: int = 0xc13e3c50

    def __init__(self, user_id: Any = None, client_id: Any = None) -> None:
        self.user_id = user_id
        self.client_id = client_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.client_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ImportedContact':
        user_id = reader.read_int64()
        client_id = reader.read_int64()
        return cls(user_id=user_id, client_id=client_id)
@register_tl
class ContactStatus(TLObject):
    ID: int = 0x16d9703b

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
    def read(cls, reader: TLReader) -> 'ContactStatus':
        user_id = reader.read_int64()
        status = reader.read_object()
        return cls(user_id=user_id, status=status)
@register_tl
class ContactsContactsNotModified(TLObject):
    ID: int = 0xb74ba9d2

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsContactsNotModified':
        return cls()
@register_tl
class ContactsContacts(TLObject):
    ID: int = 0xeae87e42

    def __init__(self, contacts: Any = None, saved_count: Any = None, users: Any = None) -> None:
        self.contacts = contacts
        self.saved_count = saved_count
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.contacts or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.saved_count or 0)
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsContacts':
        contacts = reader.read_vector(lambda r: r.read_object())
        saved_count = reader.read_int32()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(contacts=contacts, saved_count=saved_count, users=users)
@register_tl
class ContactsImportedContacts(TLObject):
    ID: int = 0x77d01c3b

    def __init__(self, imported: Any = None, popular_invites: Any = None, retry_contacts: Any = None, users: Any = None) -> None:
        self.imported = imported
        self.popular_invites = popular_invites
        self.retry_contacts = retry_contacts
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.imported or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.popular_invites or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.retry_contacts or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsImportedContacts':
        imported = reader.read_vector(lambda r: r.read_object())
        popular_invites = reader.read_vector(lambda r: r.read_object())
        retry_contacts = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(imported=imported, popular_invites=popular_invites, retry_contacts=retry_contacts, users=users)
@register_tl
class ContactsBlocked(TLObject):
    ID: int = 0xade1591

    def __init__(self, blocked: Any = None, chats: Any = None, users: Any = None) -> None:
        self.blocked = blocked
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.blocked or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlocked':
        blocked = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(blocked=blocked, chats=chats, users=users)
@register_tl
class ContactsBlockedSlice(TLObject):
    ID: int = 0xe1664194

    def __init__(self, count: Any = None, blocked: Any = None, chats: Any = None, users: Any = None) -> None:
        self.count = count
        self.blocked = blocked
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.blocked or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlockedSlice':
        count = reader.read_int32()
        blocked = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, blocked=blocked, chats=chats, users=users)
@register_tl
class MessagesDialogs(TLObject):
    ID: int = 0x15ba6c40

    def __init__(self, dialogs: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dialogs or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogs':
        dialogs = reader.read_vector(lambda r: r.read_object())
        messages = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(dialogs=dialogs, messages=messages, chats=chats, users=users)
@register_tl
class MessagesDialogsSlice(TLObject):
    ID: int = 0x71e094f3

    def __init__(self, count: Any = None, dialogs: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.count = count
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.dialogs or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogsSlice':
        count = reader.read_int32()
        dialogs = reader.read_vector(lambda r: r.read_object())
        messages = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, dialogs=dialogs, messages=messages, chats=chats, users=users)
@register_tl
class MessagesDialogsNotModified(TLObject):
    ID: int = 0xf0e3e596

    def __init__(self, count: Any = None) -> None:
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogsNotModified':
        count = reader.read_int32()
        return cls(count=count)
@register_tl
class MessagesMessages(TLObject):
    ID: int = 0x1d73e7ea

    def __init__(self, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.topics or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessages':
        messages = reader.read_vector(lambda r: r.read_object())
        topics = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(messages=messages, topics=topics, chats=chats, users=users)
@register_tl
class MessagesMessagesSlice(TLObject):
    ID: int = 0x5f206716

    def __init__(self, inexact: bool = False, count: Any = None, next_rate: Any = None, offset_id_offset: Any = None, search_flood: Any = None, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.inexact = inexact
        self.count = count
        self.next_rate = next_rate
        self.offset_id_offset = offset_id_offset
        self.search_flood = search_flood
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inexact:
            flags |= (1 << 1)
        if self.next_rate is not None:
            flags |= (1 << 0)
        if self.offset_id_offset is not None:
            flags |= (1 << 2)
        if self.search_flood is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        if self.next_rate is not None:
            writer.write_int32(self.next_rate or 0)
        if self.offset_id_offset is not None:
            writer.write_int32(self.offset_id_offset or 0)
        if self.search_flood is not None:
            if hasattr(self.search_flood, 'write'):
                self.search_flood.write(writer)
            else:
                writer.write_bytes(self.search_flood or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.topics or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessagesSlice':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 1))
        count = reader.read_int32()
        next_rate = None
        if flags & (1 << 0):
            next_rate = reader.read_int32()
        offset_id_offset = None
        if flags & (1 << 2):
            offset_id_offset = reader.read_int32()
        search_flood = None
        if flags & (1 << 3):
            search_flood = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        topics = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(inexact=inexact, count=count, next_rate=next_rate, offset_id_offset=offset_id_offset, search_flood=search_flood, messages=messages, topics=topics, chats=chats, users=users)
@register_tl
class MessagesChannelMessages(TLObject):
    ID: int = 0xc776ba4e

    def __init__(self, inexact: bool = False, pts: Any = None, count: Any = None, offset_id_offset: Any = None, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.inexact = inexact
        self.pts = pts
        self.count = count
        self.offset_id_offset = offset_id_offset
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inexact:
            flags |= (1 << 1)
        if self.offset_id_offset is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.count or 0)
        if self.offset_id_offset is not None:
            writer.write_int32(self.offset_id_offset or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.topics or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChannelMessages':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 1))
        pts = reader.read_int32()
        count = reader.read_int32()
        offset_id_offset = None
        if flags & (1 << 2):
            offset_id_offset = reader.read_int32()
        messages = reader.read_vector(lambda r: r.read_object())
        topics = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(inexact=inexact, pts=pts, count=count, offset_id_offset=offset_id_offset, messages=messages, topics=topics, chats=chats, users=users)
@register_tl
class MessagesMessagesNotModified(TLObject):
    ID: int = 0x74535f21

    def __init__(self, count: Any = None) -> None:
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessagesNotModified':
        count = reader.read_int32()
        return cls(count=count)
@register_tl
class MessagesChats(TLObject):
    ID: int = 0x64ff9fd5

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChats':
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(chats=chats)
@register_tl
class MessagesChatsSlice(TLObject):
    ID: int = 0x9cd81144

    def __init__(self, count: Any = None, chats: Any = None) -> None:
        self.count = count
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatsSlice':
        count = reader.read_int32()
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, chats=chats)
@register_tl
class MessagesChatFull(TLObject):
    ID: int = 0xe5d7d19c

    def __init__(self, full_chat: Any = None, chats: Any = None, users: Any = None) -> None:
        self.full_chat = full_chat
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.full_chat, 'write'):
            self.full_chat.write(writer)
        else:
            writer.write_bytes(self.full_chat or b'')
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatFull':
        full_chat = reader.read_object()
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(full_chat=full_chat, chats=chats, users=users)
@register_tl
class MessagesAffectedHistory(TLObject):
    ID: int = 0xb45c69d1

    def __init__(self, pts: Any = None, pts_count: Any = None, offset: Any = None) -> None:
        self.pts = pts
        self.pts_count = pts_count
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        writer.write_int32(self.offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAffectedHistory':
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        offset = reader.read_int32()
        return cls(pts=pts, pts_count=pts_count, offset=offset)
@register_tl
class InputMessagesFilterEmpty(TLObject):
    ID: int = 0x57e2f66c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterEmpty':
        return cls()
@register_tl
class InputMessagesFilterPhotos(TLObject):
    ID: int = 0x9609a51c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPhotos':
        return cls()
@register_tl
class InputMessagesFilterVideo(TLObject):
    ID: int = 0x9fc00e65

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterVideo':
        return cls()
@register_tl
class InputMessagesFilterPhotoVideo(TLObject):
    ID: int = 0x56e9f0e4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPhotoVideo':
        return cls()
@register_tl
class InputMessagesFilterDocument(TLObject):
    ID: int = 0x9eddf188

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterDocument':
        return cls()
@register_tl
class InputMessagesFilterUrl(TLObject):
    ID: int = 0x7ef0dd87

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterUrl':
        return cls()
@register_tl
class InputMessagesFilterGif(TLObject):
    ID: int = 0xffc86587

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterGif':
        return cls()
@register_tl
class InputMessagesFilterVoice(TLObject):
    ID: int = 0x50f5c392

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterVoice':
        return cls()
@register_tl
class InputMessagesFilterMusic(TLObject):
    ID: int = 0x3751b49e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterMusic':
        return cls()
