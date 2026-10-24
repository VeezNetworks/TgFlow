from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class BotsGetAdminedBots(TLRequest):
    ID: int = 0xb0711d83

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetAdminedBots':
        return cls()


@register_tl
class BotsUpdateStarRefProgram(TLRequest):
    ID: int = 0x778b5ab3

    def __init__(self, duration_months: Any = None, bot: Any = None, commission_permille: Any = None) -> None:
        self.duration_months = duration_months
        self.bot = bot
        self.commission_permille = commission_permille

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.duration_months is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_int32(self.commission_permille or 0)
        if self.duration_months is not None:
            writer.write_int32(self.duration_months or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsUpdateStarRefProgram':
        flags = reader.read_uint32()
        bot = reader.read_object()
        commission_permille = reader.read_int32()
        duration_months = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(bot=bot, commission_permille=commission_permille, duration_months=duration_months)


@register_tl
class BotsSetCustomVerification(TLRequest):
    ID: int = 0x8b89dfbd

    def __init__(self, enabled: bool = False, bot: Any = None, custom_description: Any = None, peer: Any = None) -> None:
        self.enabled = enabled
        self.bot = bot
        self.custom_description = custom_description
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.enabled:
            flags |= (1 << 1)
        if self.bot is not None:
            flags |= (1 << 0)
        if self.custom_description is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.bot is not None:
            if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.custom_description is not None:
            writer.write_string(self.custom_description or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsSetCustomVerification':
        flags = reader.read_uint32()
        enabled = bool(flags & (1 << 1))
        bot = reader.read_object() if (flags & (1 << 0)) else None
        peer = reader.read_object()
        custom_description = reader.read_string() if (flags & (1 << 2)) else None
        return cls(enabled=enabled, bot=bot, peer=peer, custom_description=custom_description)


@register_tl
class BotsGetBotRecommendations(TLRequest):
    ID: int = 0xa1b70815

    def __init__(self, bot: Any = None) -> None:
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetBotRecommendations':
        bot = reader.read_object()
        return cls(bot=bot)


@register_tl
class BotsCheckUsername(TLRequest):
    ID: int = 0x87f2219b

    def __init__(self, username: Any = None) -> None:
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsCheckUsername':
        username = reader.read_string()
        return cls(username=username)


@register_tl
class BotsCreateBot(TLRequest):
    ID: int = 0xe5b17f2b

    def __init__(self, via_deeplink: bool = False, name: Any = None, username: Any = None, manager_id: Any = None) -> None:
        self.via_deeplink = via_deeplink
        self.name = name
        self.username = username
        self.manager_id = manager_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_deeplink:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.name or '')
        writer.write_string(self.username or '')
        if self.manager_id is not None and hasattr(self.manager_id, 'write'): self.manager_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsCreateBot':
        flags = reader.read_uint32()
        via_deeplink = bool(flags & (1 << 0))
        name = reader.read_string()
        username = reader.read_string()
        manager_id = reader.read_object()
        return cls(via_deeplink=via_deeplink, name=name, username=username, manager_id=manager_id)


@register_tl
class BotsExportBotToken(TLRequest):
    ID: int = 0xbd0d99eb

    def __init__(self, bot: Any = None, revoke: Any = None) -> None:
        self.bot = bot
        self.revoke = revoke

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_bool(bool(self.revoke))

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsExportBotToken':
        bot = reader.read_object()
        revoke = reader.read_bool()
        return cls(bot=bot, revoke=revoke)


@register_tl
class BotsRequestWebViewButton(TLRequest):
    ID: int = 0x31a2a35e

    def __init__(self, user_id: Any = None, button: Any = None) -> None:
        self.user_id = user_id
        self.button = button

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        if self.button is not None and hasattr(self.button, 'write'): self.button.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsRequestWebViewButton':
        user_id = reader.read_object()
        button = reader.read_object()
        return cls(user_id=user_id, button=button)


@register_tl
class BotsGetRequestedWebViewButton(TLRequest):
    ID: int = 0xbf25b7f3

    def __init__(self, bot: Any = None, webapp_req_id: Any = None) -> None:
        self.bot = bot
        self.webapp_req_id = webapp_req_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.webapp_req_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetRequestedWebViewButton':
        bot = reader.read_object()
        webapp_req_id = reader.read_string()
        return cls(bot=bot, webapp_req_id=webapp_req_id)


@register_tl
class BotsGetAccessSettings(TLRequest):
    ID: int = 0x213853a3

    def __init__(self, bot: Any = None) -> None:
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetAccessSettings':
        bot = reader.read_object()
        return cls(bot=bot)


@register_tl
class BotsEditAccessSettings(TLRequest):
    ID: int = 0x31813cd8

    def __init__(self, restricted: bool = False, add_users: Any = None, bot: Any = None) -> None:
        self.restricted = restricted
        self.add_users = add_users
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.restricted:
            flags |= (1 << 0)
        if self.add_users is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.add_users is not None:
            writer.write_vector(self.add_users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsEditAccessSettings':
        flags = reader.read_uint32()
        restricted = bool(flags & (1 << 0))
        bot = reader.read_object()
        add_users = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        return cls(restricted=restricted, bot=bot, add_users=add_users)


@register_tl
class PaymentsGetPaymentForm(TLRequest):
    ID: int = 0x37148dbb

    def __init__(self, theme_params: Any = None, invoice: Any = None) -> None:
        self.theme_params = theme_params
        self.invoice = invoice

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.theme_params is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        if self.theme_params is not None:
            if self.theme_params is not None and hasattr(self.theme_params, 'write'): self.theme_params.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetPaymentForm':
        flags = reader.read_uint32()
        invoice = reader.read_object()
        theme_params = reader.read_object() if (flags & (1 << 0)) else None
        return cls(invoice=invoice, theme_params=theme_params)


@register_tl
class PaymentsGetPaymentReceipt(TLRequest):
    ID: int = 0x2478d1cc

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetPaymentReceipt':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class PaymentsValidateRequestedInfo(TLRequest):
    ID: int = 0xb6c8f12b

    def __init__(self, save: bool = False, invoice: Any = None, info: Any = None) -> None:
        self.save = save
        self.invoice = invoice
        self.info = info

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.save:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        if self.info is not None and hasattr(self.info, 'write'): self.info.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsValidateRequestedInfo':
        flags = reader.read_uint32()
        save = bool(flags & (1 << 0))
        invoice = reader.read_object()
        info = reader.read_object()
        return cls(save=save, invoice=invoice, info=info)


@register_tl
class PaymentsSendPaymentForm(TLRequest):
    ID: int = 0x2d03522f

    def __init__(self, requested_info_id: Any = None, shipping_option_id: Any = None, tip_amount: Any = None, form_id: Any = None, invoice: Any = None, credentials: Any = None) -> None:
        self.requested_info_id = requested_info_id
        self.shipping_option_id = shipping_option_id
        self.tip_amount = tip_amount
        self.form_id = form_id
        self.invoice = invoice
        self.credentials = credentials

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.requested_info_id is not None:
            flags |= (1 << 0)
        if self.shipping_option_id is not None:
            flags |= (1 << 1)
        if self.tip_amount is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.form_id or 0)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        if self.requested_info_id is not None:
            writer.write_string(self.requested_info_id or '')
        if self.shipping_option_id is not None:
            writer.write_string(self.shipping_option_id or '')
        if self.credentials is not None and hasattr(self.credentials, 'write'): self.credentials.write(writer)
        if self.tip_amount is not None:
            writer.write_int64(self.tip_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsSendPaymentForm':
        flags = reader.read_uint32()
        form_id = reader.read_int64()
        invoice = reader.read_object()
        requested_info_id = reader.read_string() if (flags & (1 << 0)) else None
        shipping_option_id = reader.read_string() if (flags & (1 << 1)) else None
        credentials = reader.read_object()
        tip_amount = reader.read_int64() if (flags & (1 << 2)) else None
        return cls(form_id=form_id, invoice=invoice, requested_info_id=requested_info_id, shipping_option_id=shipping_option_id, credentials=credentials, tip_amount=tip_amount)


@register_tl
class PaymentsGetSavedInfo(TLRequest):
    ID: int = 0x227d824b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetSavedInfo':
        return cls()


@register_tl
class PaymentsClearSavedInfo(TLRequest):
    ID: int = 0xd83d70c1

    def __init__(self, credentials: bool = False, info: bool = False) -> None:
        self.credentials = credentials
        self.info = info

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.credentials:
            flags |= (1 << 0)
        if self.info:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsClearSavedInfo':
        flags = reader.read_uint32()
        credentials = bool(flags & (1 << 0))
        info = bool(flags & (1 << 1))
        return cls(credentials=credentials, info=info)


@register_tl
class PaymentsGetBankCardData(TLRequest):
    ID: int = 0x2e79d779

    def __init__(self, number: Any = None) -> None:
        self.number = number

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.number or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetBankCardData':
        number = reader.read_string()
        return cls(number=number)


@register_tl
class PaymentsExportInvoice(TLRequest):
    ID: int = 0xf91b065

    def __init__(self, invoice_media: Any = None) -> None:
        self.invoice_media = invoice_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.invoice_media is not None and hasattr(self.invoice_media, 'write'): self.invoice_media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsExportInvoice':
        invoice_media = reader.read_object()
        return cls(invoice_media=invoice_media)


@register_tl
class PaymentsAssignAppStoreTransaction(TLRequest):
    ID: int = 0x80ed747d

    def __init__(self, receipt: Any = None, purpose: Any = None) -> None:
        self.receipt = receipt
        self.purpose = purpose

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.receipt or b'')
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsAssignAppStoreTransaction':
        receipt = reader.read_bytes()
        purpose = reader.read_object()
        return cls(receipt=receipt, purpose=purpose)


@register_tl
class PaymentsAssignPlayMarketTransaction(TLRequest):
    ID: int = 0xdffd50d3

    def __init__(self, receipt: Any = None, purpose: Any = None) -> None:
        self.receipt = receipt
        self.purpose = purpose

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.receipt is not None and hasattr(self.receipt, 'write'): self.receipt.write(writer)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsAssignPlayMarketTransaction':
        receipt = reader.read_object()
        purpose = reader.read_object()
        return cls(receipt=receipt, purpose=purpose)


@register_tl
class PaymentsGetPremiumGiftCodeOptions(TLRequest):
    ID: int = 0x2757ba54

    def __init__(self, boost_peer: Any = None) -> None:
        self.boost_peer = boost_peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.boost_peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.boost_peer is not None:
            if self.boost_peer is not None and hasattr(self.boost_peer, 'write'): self.boost_peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetPremiumGiftCodeOptions':
        flags = reader.read_uint32()
        boost_peer = reader.read_object() if (flags & (1 << 0)) else None
        return cls(boost_peer=boost_peer)


@register_tl
class PaymentsCheckGiftCode(TLRequest):
    ID: int = 0x8e51b4c1

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCheckGiftCode':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class PaymentsApplyGiftCode(TLRequest):
    ID: int = 0xf6e26854

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsApplyGiftCode':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class PaymentsGetGiveawayInfo(TLRequest):
    ID: int = 0xf4239425

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetGiveawayInfo':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class PaymentsLaunchPrepaidGiveaway(TLRequest):
    ID: int = 0x5ff58f20

    def __init__(self, peer: Any = None, giveaway_id: Any = None, purpose: Any = None) -> None:
        self.peer = peer
        self.giveaway_id = giveaway_id
        self.purpose = purpose

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.giveaway_id or 0)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsLaunchPrepaidGiveaway':
        peer = reader.read_object()
        giveaway_id = reader.read_int64()
        purpose = reader.read_object()
        return cls(peer=peer, giveaway_id=giveaway_id, purpose=purpose)


@register_tl
class PaymentsGetStarsTopupOptions(TLRequest):
    ID: int = 0xc00ec7d3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsTopupOptions':
        return cls()


@register_tl
class PaymentsGetStarsStatus(TLRequest):
    ID: int = 0x4ea9b3bf

    def __init__(self, ton: bool = False, peer: Any = None) -> None:
        self.ton = ton
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ton:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsStatus':
        flags = reader.read_uint32()
        ton = bool(flags & (1 << 0))
        peer = reader.read_object()
        return cls(ton=ton, peer=peer)


@register_tl
class PaymentsGetStarsTransactions(TLRequest):
    ID: int = 0x69da4557

    def __init__(self, inbound: bool = False, outbound: bool = False, ascending: bool = False, ton: bool = False, subscription_id: Any = None, peer: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.inbound = inbound
        self.outbound = outbound
        self.ascending = ascending
        self.ton = ton
        self.subscription_id = subscription_id
        self.peer = peer
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inbound:
            flags |= (1 << 0)
        if self.outbound:
            flags |= (1 << 1)
        if self.ascending:
            flags |= (1 << 2)
        if self.ton:
            flags |= (1 << 4)
        if self.subscription_id is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.subscription_id is not None:
            writer.write_string(self.subscription_id or '')
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsTransactions':
        flags = reader.read_uint32()
        inbound = bool(flags & (1 << 0))
        outbound = bool(flags & (1 << 1))
        ascending = bool(flags & (1 << 2))
        ton = bool(flags & (1 << 4))
        subscription_id = reader.read_string() if (flags & (1 << 3)) else None
        peer = reader.read_object()
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(inbound=inbound, outbound=outbound, ascending=ascending, ton=ton, subscription_id=subscription_id, peer=peer, offset=offset, limit=limit)


@register_tl
class PaymentsSendStarsForm(TLRequest):
    ID: int = 0x7998c914

    def __init__(self, form_id: Any = None, invoice: Any = None) -> None:
        self.form_id = form_id
        self.invoice = invoice

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.form_id or 0)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsSendStarsForm':
        form_id = reader.read_int64()
        invoice = reader.read_object()
        return cls(form_id=form_id, invoice=invoice)


@register_tl
class PaymentsRefundStarsCharge(TLRequest):
    ID: int = 0x25ae8f4a

    def __init__(self, user_id: Any = None, charge_id: Any = None) -> None:
        self.user_id = user_id
        self.charge_id = charge_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_string(self.charge_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsRefundStarsCharge':
        user_id = reader.read_object()
        charge_id = reader.read_string()
        return cls(user_id=user_id, charge_id=charge_id)


@register_tl
class PaymentsGetStarsRevenueStats(TLRequest):
    ID: int = 0xd91ffad6

    def __init__(self, dark: bool = False, ton: bool = False, peer: Any = None) -> None:
        self.dark = dark
        self.ton = ton
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        if self.ton:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsRevenueStats':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        ton = bool(flags & (1 << 1))
        peer = reader.read_object()
        return cls(dark=dark, ton=ton, peer=peer)


@register_tl
class PaymentsGetStarsRevenueWithdrawalUrl(TLRequest):
    ID: int = 0x2433dc92

    def __init__(self, ton: bool = False, amount: Any = None, peer: Any = None, password: Any = None) -> None:
        self.ton = ton
        self.amount = amount
        self.peer = peer
        self.password = password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ton:
            flags |= (1 << 0)
        if self.amount is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.amount is not None:
            writer.write_int64(self.amount or 0)
        if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsRevenueWithdrawalUrl':
        flags = reader.read_uint32()
        ton = bool(flags & (1 << 0))
        peer = reader.read_object()
        amount = reader.read_int64() if (flags & (1 << 1)) else None
        password = reader.read_object()
        return cls(ton=ton, peer=peer, amount=amount, password=password)


@register_tl
class PaymentsGetStarsRevenueAdsAccountUrl(TLRequest):
    ID: int = 0xd1d7efc5

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsRevenueAdsAccountUrl':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class PaymentsGetStarsTransactionsByID(TLRequest):
    ID: int = 0x2dca16b8

    def __init__(self, ton: bool = False, peer: Any = None, id: Any = None) -> None:
        self.ton = ton
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ton:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsTransactionsByID':
        flags = reader.read_uint32()
        ton = bool(flags & (1 << 0))
        peer = reader.read_object()
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(ton=ton, peer=peer, id=id)


@register_tl
class PaymentsGetStarsGiftOptions(TLRequest):
    ID: int = 0xd3c96bc8

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.user_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.user_id is not None:
            if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsGiftOptions':
        flags = reader.read_uint32()
        user_id = reader.read_object() if (flags & (1 << 0)) else None
        return cls(user_id=user_id)


@register_tl
class PaymentsGetStarsSubscriptions(TLRequest):
    ID: int = 0x32512c5

    def __init__(self, missing_balance: bool = False, peer: Any = None, offset: Any = None) -> None:
        self.missing_balance = missing_balance
        self.peer = peer
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.missing_balance:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsSubscriptions':
        flags = reader.read_uint32()
        missing_balance = bool(flags & (1 << 0))
        peer = reader.read_object()
        offset = reader.read_string()
        return cls(missing_balance=missing_balance, peer=peer, offset=offset)


@register_tl
class PaymentsChangeStarsSubscription(TLRequest):
    ID: int = 0xc7770878

    def __init__(self, canceled: Any = None, peer: Any = None, subscription_id: Any = None) -> None:
        self.canceled = canceled
        self.peer = peer
        self.subscription_id = subscription_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.canceled is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.subscription_id or '')
        if self.canceled is not None:
            writer.write_bool(bool(self.canceled))

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsChangeStarsSubscription':
        flags = reader.read_uint32()
        peer = reader.read_object()
        subscription_id = reader.read_string()
        canceled = reader.read_bool() if (flags & (1 << 0)) else None
        return cls(peer=peer, subscription_id=subscription_id, canceled=canceled)


@register_tl
class PaymentsFulfillStarsSubscription(TLRequest):
    ID: int = 0xcc5bebb3

    def __init__(self, peer: Any = None, subscription_id: Any = None) -> None:
        self.peer = peer
        self.subscription_id = subscription_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.subscription_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsFulfillStarsSubscription':
        peer = reader.read_object()
        subscription_id = reader.read_string()
        return cls(peer=peer, subscription_id=subscription_id)


@register_tl
class PaymentsGetStarsGiveawayOptions(TLRequest):
    ID: int = 0xbd1efd3e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarsGiveawayOptions':
        return cls()


@register_tl
class PaymentsGetStarGifts(TLRequest):
    ID: int = 0xc4563590

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGifts':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class PaymentsSaveStarGift(TLRequest):
    ID: int = 0x2a2a697c

    def __init__(self, unsave: bool = False, stargift: Any = None) -> None:
        self.unsave = unsave
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unsave:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsSaveStarGift':
        flags = reader.read_uint32()
        unsave = bool(flags & (1 << 0))
        stargift = reader.read_object()
        return cls(unsave=unsave, stargift=stargift)


@register_tl
class PaymentsConvertStarGift(TLRequest):
    ID: int = 0x74bf076b

    def __init__(self, stargift: Any = None) -> None:
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsConvertStarGift':
        stargift = reader.read_object()
        return cls(stargift=stargift)


@register_tl
class PaymentsBotCancelStarsSubscription(TLRequest):
    ID: int = 0x6dfa0622

    def __init__(self, restore: bool = False, user_id: Any = None, charge_id: Any = None) -> None:
        self.restore = restore
        self.user_id = user_id
        self.charge_id = charge_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.restore:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_string(self.charge_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsBotCancelStarsSubscription':
        flags = reader.read_uint32()
        restore = bool(flags & (1 << 0))
        user_id = reader.read_object()
        charge_id = reader.read_string()
        return cls(restore=restore, user_id=user_id, charge_id=charge_id)


@register_tl
class PaymentsGetConnectedStarRefBots(TLRequest):
    ID: int = 0x5869a553

    def __init__(self, offset_date: Any = None, offset_link: Any = None, peer: Any = None, limit: Any = None) -> None:
        self.offset_date = offset_date
        self.offset_link = offset_link
        self.peer = peer
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.offset_date is not None:
            flags |= (1 << 2)
        if self.offset_link is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.offset_date is not None:
            writer.write_int32(self.offset_date or 0)
        if self.offset_link is not None:
            writer.write_string(self.offset_link or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetConnectedStarRefBots':
        flags = reader.read_uint32()
        peer = reader.read_object()
        offset_date = reader.read_int32() if (flags & (1 << 2)) else None
        offset_link = reader.read_string() if (flags & (1 << 2)) else None
        limit = reader.read_int32()
        return cls(peer=peer, offset_date=offset_date, offset_link=offset_link, limit=limit)


@register_tl
class PaymentsGetConnectedStarRefBot(TLRequest):
    ID: int = 0xb7d998f0

    def __init__(self, peer: Any = None, bot: Any = None) -> None:
        self.peer = peer
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetConnectedStarRefBot':
        peer = reader.read_object()
        bot = reader.read_object()
        return cls(peer=peer, bot=bot)


@register_tl
class PaymentsGetSuggestedStarRefBots(TLRequest):
    ID: int = 0xd6b48f7

    def __init__(self, order_by_revenue: bool = False, order_by_date: bool = False, peer: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.order_by_revenue = order_by_revenue
        self.order_by_date = order_by_date
        self.peer = peer
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.order_by_revenue:
            flags |= (1 << 0)
        if self.order_by_date:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetSuggestedStarRefBots':
        flags = reader.read_uint32()
        order_by_revenue = bool(flags & (1 << 0))
        order_by_date = bool(flags & (1 << 1))
        peer = reader.read_object()
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(order_by_revenue=order_by_revenue, order_by_date=order_by_date, peer=peer, offset=offset, limit=limit)


@register_tl
class PaymentsConnectStarRefBot(TLRequest):
    ID: int = 0x7ed5348a

    def __init__(self, peer: Any = None, bot: Any = None) -> None:
        self.peer = peer
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsConnectStarRefBot':
        peer = reader.read_object()
        bot = reader.read_object()
        return cls(peer=peer, bot=bot)


@register_tl
class PaymentsEditConnectedStarRefBot(TLRequest):
    ID: int = 0xe4fca4a3

    def __init__(self, revoked: bool = False, peer: Any = None, link: Any = None) -> None:
        self.revoked = revoked
        self.peer = peer
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoked:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.link or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsEditConnectedStarRefBot':
        flags = reader.read_uint32()
        revoked = bool(flags & (1 << 0))
        peer = reader.read_object()
        link = reader.read_string()
        return cls(revoked=revoked, peer=peer, link=link)


@register_tl
class PaymentsGetStarGiftUpgradePreview(TLRequest):
    ID: int = 0x9c9abcb1

    def __init__(self, gift_id: Any = None) -> None:
        self.gift_id = gift_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGiftUpgradePreview':
        gift_id = reader.read_int64()
        return cls(gift_id=gift_id)


@register_tl
class PaymentsUpgradeStarGift(TLRequest):
    ID: int = 0xaed6e4f5

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
    def read(cls, reader: TLReader) -> 'PaymentsUpgradeStarGift':
        flags = reader.read_uint32()
        keep_original_details = bool(flags & (1 << 0))
        stargift = reader.read_object()
        return cls(keep_original_details=keep_original_details, stargift=stargift)


@register_tl
class PaymentsTransferStarGift(TLRequest):
    ID: int = 0x7f18176a

    def __init__(self, stargift: Any = None, to_id: Any = None) -> None:
        self.stargift = stargift
        self.to_id = to_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)
        if self.to_id is not None and hasattr(self.to_id, 'write'): self.to_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsTransferStarGift':
        stargift = reader.read_object()
        to_id = reader.read_object()
        return cls(stargift=stargift, to_id=to_id)


@register_tl
class PaymentsGetUniqueStarGift(TLRequest):
    ID: int = 0xa1974d72

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetUniqueStarGift':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class PaymentsGetSavedStarGifts(TLRequest):
    ID: int = 0xa319e569

    def __init__(self, exclude_unsaved: bool = False, exclude_saved: bool = False, exclude_unlimited: bool = False, exclude_unique: bool = False, sort_by_value: bool = False, exclude_upgradable: bool = False, exclude_unupgradable: bool = False, peer_color_available: bool = False, exclude_hosted: bool = False, collection_id: Any = None, peer: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.exclude_unsaved = exclude_unsaved
        self.exclude_saved = exclude_saved
        self.exclude_unlimited = exclude_unlimited
        self.exclude_unique = exclude_unique
        self.sort_by_value = sort_by_value
        self.exclude_upgradable = exclude_upgradable
        self.exclude_unupgradable = exclude_unupgradable
        self.peer_color_available = peer_color_available
        self.exclude_hosted = exclude_hosted
        self.collection_id = collection_id
        self.peer = peer
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.exclude_unsaved:
            flags |= (1 << 0)
        if self.exclude_saved:
            flags |= (1 << 1)
        if self.exclude_unlimited:
            flags |= (1 << 2)
        if self.exclude_unique:
            flags |= (1 << 4)
        if self.sort_by_value:
            flags |= (1 << 5)
        if self.exclude_upgradable:
            flags |= (1 << 7)
        if self.exclude_unupgradable:
            flags |= (1 << 8)
        if self.peer_color_available:
            flags |= (1 << 9)
        if self.exclude_hosted:
            flags |= (1 << 10)
        if self.collection_id is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.collection_id is not None:
            writer.write_int32(self.collection_id or 0)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetSavedStarGifts':
        flags = reader.read_uint32()
        exclude_unsaved = bool(flags & (1 << 0))
        exclude_saved = bool(flags & (1 << 1))
        exclude_unlimited = bool(flags & (1 << 2))
        exclude_unique = bool(flags & (1 << 4))
        sort_by_value = bool(flags & (1 << 5))
        exclude_upgradable = bool(flags & (1 << 7))
        exclude_unupgradable = bool(flags & (1 << 8))
        peer_color_available = bool(flags & (1 << 9))
        exclude_hosted = bool(flags & (1 << 10))
        peer = reader.read_object()
        collection_id = reader.read_int32() if (flags & (1 << 6)) else None
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(exclude_unsaved=exclude_unsaved, exclude_saved=exclude_saved, exclude_unlimited=exclude_unlimited, exclude_unique=exclude_unique, sort_by_value=sort_by_value, exclude_upgradable=exclude_upgradable, exclude_unupgradable=exclude_unupgradable, peer_color_available=peer_color_available, exclude_hosted=exclude_hosted, peer=peer, collection_id=collection_id, offset=offset, limit=limit)


@register_tl
class PaymentsGetSavedStarGift(TLRequest):
    ID: int = 0xb455a106

    def __init__(self, stargift: Any = None) -> None:
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.stargift or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetSavedStarGift':
        stargift = reader.read_vector(lambda r: reader.read_object())
        return cls(stargift=stargift)


@register_tl
class PaymentsGetStarGiftWithdrawalUrl(TLRequest):
    ID: int = 0xd06e93a8

    def __init__(self, stargift: Any = None, password: Any = None) -> None:
        self.stargift = stargift
        self.password = password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)
        if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGiftWithdrawalUrl':
        stargift = reader.read_object()
        password = reader.read_object()
        return cls(stargift=stargift, password=password)


@register_tl
class PaymentsToggleChatStarGiftNotifications(TLRequest):
    ID: int = 0x60eaefa1

    def __init__(self, enabled: bool = False, peer: Any = None) -> None:
        self.enabled = enabled
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.enabled:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsToggleChatStarGiftNotifications':
        flags = reader.read_uint32()
        enabled = bool(flags & (1 << 0))
        peer = reader.read_object()
        return cls(enabled=enabled, peer=peer)


@register_tl
class PaymentsToggleStarGiftsPinnedToTop(TLRequest):
    ID: int = 0x1513e7b0

    def __init__(self, peer: Any = None, stargift: Any = None) -> None:
        self.peer = peer
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.stargift or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsToggleStarGiftsPinnedToTop':
        peer = reader.read_object()
        stargift = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, stargift=stargift)


@register_tl
class PaymentsCanPurchaseStore(TLRequest):
    ID: int = 0x4fdc5ea7

    def __init__(self, purpose: Any = None) -> None:
        self.purpose = purpose

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCanPurchaseStore':
        purpose = reader.read_object()
        return cls(purpose=purpose)


@register_tl
class PaymentsGetResaleStarGifts(TLRequest):
    ID: int = 0x7a5fa236

    def __init__(self, sort_by_price: bool = False, sort_by_num: bool = False, for_craft: bool = False, stars_only: bool = False, attributes_hash: Any = None, attributes: Any = None, gift_id: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.sort_by_price = sort_by_price
        self.sort_by_num = sort_by_num
        self.for_craft = for_craft
        self.stars_only = stars_only
        self.attributes_hash = attributes_hash
        self.attributes = attributes
        self.gift_id = gift_id
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sort_by_price:
            flags |= (1 << 1)
        if self.sort_by_num:
            flags |= (1 << 2)
        if self.for_craft:
            flags |= (1 << 4)
        if self.stars_only:
            flags |= (1 << 5)
        if self.attributes_hash is not None:
            flags |= (1 << 0)
        if self.attributes is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.attributes_hash is not None:
            writer.write_int64(self.attributes_hash or 0)
        writer.write_int64(self.gift_id or 0)
        if self.attributes is not None:
            writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetResaleStarGifts':
        flags = reader.read_uint32()
        sort_by_price = bool(flags & (1 << 1))
        sort_by_num = bool(flags & (1 << 2))
        for_craft = bool(flags & (1 << 4))
        stars_only = bool(flags & (1 << 5))
        attributes_hash = reader.read_int64() if (flags & (1 << 0)) else None
        gift_id = reader.read_int64()
        attributes = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(sort_by_price=sort_by_price, sort_by_num=sort_by_num, for_craft=for_craft, stars_only=stars_only, attributes_hash=attributes_hash, gift_id=gift_id, attributes=attributes, offset=offset, limit=limit)


@register_tl
class PaymentsUpdateStarGiftPrice(TLRequest):
    ID: int = 0xedbe6ccb

    def __init__(self, stargift: Any = None, resell_amount: Any = None) -> None:
        self.stargift = stargift
        self.resell_amount = resell_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stargift is not None and hasattr(self.stargift, 'write'): self.stargift.write(writer)
        if self.resell_amount is not None and hasattr(self.resell_amount, 'write'): self.resell_amount.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsUpdateStarGiftPrice':
        stargift = reader.read_object()
        resell_amount = reader.read_object()
        return cls(stargift=stargift, resell_amount=resell_amount)


@register_tl
class PaymentsCreateStarGiftCollection(TLRequest):
    ID: int = 0x1f4a0e87

    def __init__(self, peer: Any = None, title: Any = None, stargift: Any = None) -> None:
        self.peer = peer
        self.title = title
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.title or '')
        writer.write_vector(self.stargift or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCreateStarGiftCollection':
        peer = reader.read_object()
        title = reader.read_string()
        stargift = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, title=title, stargift=stargift)


@register_tl
class PaymentsUpdateStarGiftCollection(TLRequest):
    ID: int = 0x4fddbee7

    def __init__(self, title: Any = None, delete_stargift: Any = None, add_stargift: Any = None, order: Any = None, peer: Any = None, collection_id: Any = None) -> None:
        self.title = title
        self.delete_stargift = delete_stargift
        self.add_stargift = add_stargift
        self.order = order
        self.peer = peer
        self.collection_id = collection_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        if self.delete_stargift is not None:
            flags |= (1 << 1)
        if self.add_stargift is not None:
            flags |= (1 << 2)
        if self.order is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.collection_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.delete_stargift is not None:
            writer.write_vector(self.delete_stargift or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.add_stargift is not None:
            writer.write_vector(self.add_stargift or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.order is not None:
            writer.write_vector(self.order or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsUpdateStarGiftCollection':
        flags = reader.read_uint32()
        peer = reader.read_object()
        collection_id = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        delete_stargift = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        add_stargift = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 2)) else None
        order = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        return cls(peer=peer, collection_id=collection_id, title=title, delete_stargift=delete_stargift, add_stargift=add_stargift, order=order)


@register_tl
class PaymentsReorderStarGiftCollections(TLRequest):
    ID: int = 0xc32af4cc

    def __init__(self, peer: Any = None, order: Any = None) -> None:
        self.peer = peer
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.order or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsReorderStarGiftCollections':
        peer = reader.read_object()
        order = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, order=order)


@register_tl
class PaymentsDeleteStarGiftCollection(TLRequest):
    ID: int = 0xad5648e8

    def __init__(self, peer: Any = None, collection_id: Any = None) -> None:
        self.peer = peer
        self.collection_id = collection_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.collection_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsDeleteStarGiftCollection':
        peer = reader.read_object()
        collection_id = reader.read_int32()
        return cls(peer=peer, collection_id=collection_id)


@register_tl
class PaymentsGetStarGiftCollections(TLRequest):
    ID: int = 0x981b91dd

    def __init__(self, peer: Any = None, hash: Any = None) -> None:
        self.peer = peer
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGiftCollections':
        peer = reader.read_object()
        hash = reader.read_int64()
        return cls(peer=peer, hash=hash)


@register_tl
class PaymentsGetUniqueStarGiftValueInfo(TLRequest):
    ID: int = 0x4365af6b

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetUniqueStarGiftValueInfo':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class PaymentsCheckCanSendGift(TLRequest):
    ID: int = 0xc0c4edc9

    def __init__(self, gift_id: Any = None) -> None:
        self.gift_id = gift_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCheckCanSendGift':
        gift_id = reader.read_int64()
        return cls(gift_id=gift_id)


@register_tl
class PaymentsGetStarGiftAuctionState(TLRequest):
    ID: int = 0x5c9ff4d6

    def __init__(self, auction: Any = None, version: Any = None) -> None:
        self.auction = auction
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.auction is not None and hasattr(self.auction, 'write'): self.auction.write(writer)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGiftAuctionState':
        auction = reader.read_object()
        version = reader.read_int32()
        return cls(auction=auction, version=version)


@register_tl
class PaymentsGetStarGiftAuctionAcquiredGifts(TLRequest):
    ID: int = 0x6ba2cbec

    def __init__(self, gift_id: Any = None) -> None:
        self.gift_id = gift_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGiftAuctionAcquiredGifts':
        gift_id = reader.read_int64()
        return cls(gift_id=gift_id)


@register_tl
class PaymentsGetStarGiftActiveAuctions(TLRequest):
    ID: int = 0xa5d0514d

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGiftActiveAuctions':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class PaymentsResolveStarGiftOffer(TLRequest):
    ID: int = 0xe9ce781c

    def __init__(self, decline: bool = False, offer_msg_id: Any = None) -> None:
        self.decline = decline
        self.offer_msg_id = offer_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.decline:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.offer_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsResolveStarGiftOffer':
        flags = reader.read_uint32()
        decline = bool(flags & (1 << 0))
        offer_msg_id = reader.read_int32()
        return cls(decline=decline, offer_msg_id=offer_msg_id)


@register_tl
class PaymentsSendStarGiftOffer(TLRequest):
    ID: int = 0x8fb86b41

    def __init__(self, allow_paid_stars: Any = None, peer: Any = None, slug: Any = None, price: Any = None, duration: Any = None, random_id: Any = None) -> None:
        self.allow_paid_stars = allow_paid_stars
        self.peer = peer
        self.slug = slug
        self.price = price
        self.duration = duration
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.allow_paid_stars is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.slug or '')
        if self.price is not None and hasattr(self.price, 'write'): self.price.write(writer)
        writer.write_int32(self.duration or 0)
        writer.write_int64(self.random_id or 0)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsSendStarGiftOffer':
        flags = reader.read_uint32()
        peer = reader.read_object()
        slug = reader.read_string()
        price = reader.read_object()
        duration = reader.read_int32()
        random_id = reader.read_int64()
        allow_paid_stars = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(peer=peer, slug=slug, price=price, duration=duration, random_id=random_id, allow_paid_stars=allow_paid_stars)


@register_tl
class PaymentsGetStarGiftUpgradeAttributes(TLRequest):
    ID: int = 0x6d038b58

    def __init__(self, gift_id: Any = None) -> None:
        self.gift_id = gift_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetStarGiftUpgradeAttributes':
        gift_id = reader.read_int64()
        return cls(gift_id=gift_id)


@register_tl
class PaymentsGetCraftStarGifts(TLRequest):
    ID: int = 0xfd05dd00

    def __init__(self, gift_id: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.gift_id = gift_id
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsGetCraftStarGifts':
        gift_id = reader.read_int64()
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(gift_id=gift_id, offset=offset, limit=limit)


@register_tl
class PaymentsCraftStarGift(TLRequest):
    ID: int = 0xb0f9684f

    def __init__(self, stargift: Any = None) -> None:
        self.stargift = stargift

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.stargift or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsCraftStarGift':
        stargift = reader.read_vector(lambda r: reader.read_object())
        return cls(stargift=stargift)


@register_tl
class StickersCreateStickerSet(TLRequest):
    ID: int = 0x9021ab67

    def __init__(self, masks: bool = False, emojis: bool = False, text_color: bool = False, thumb: Any = None, software: Any = None, user_id: Any = None, title: Any = None, short_name: Any = None, stickers: Any = None) -> None:
        self.masks = masks
        self.emojis = emojis
        self.text_color = text_color
        self.thumb = thumb
        self.software = software
        self.user_id = user_id
        self.title = title
        self.short_name = short_name
        self.stickers = stickers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 5)
        if self.text_color:
            flags |= (1 << 6)
        if self.thumb is not None:
            flags |= (1 << 2)
        if self.software is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_string(self.title or '')
        writer.write_string(self.short_name or '')
        if self.thumb is not None:
            if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.software is not None:
            writer.write_string(self.software or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersCreateStickerSet':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 5))
        text_color = bool(flags & (1 << 6))
        user_id = reader.read_object()
        title = reader.read_string()
        short_name = reader.read_string()
        thumb = reader.read_object() if (flags & (1 << 2)) else None
        stickers = reader.read_vector(lambda r: reader.read_object())
        software = reader.read_string() if (flags & (1 << 3)) else None
        return cls(masks=masks, emojis=emojis, text_color=text_color, user_id=user_id, title=title, short_name=short_name, thumb=thumb, stickers=stickers, software=software)


@register_tl
class StickersRemoveStickerFromSet(TLRequest):
    ID: int = 0xf7760f51

    def __init__(self, sticker: Any = None) -> None:
        self.sticker = sticker

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersRemoveStickerFromSet':
        sticker = reader.read_object()
        return cls(sticker=sticker)


@register_tl
class StickersChangeStickerPosition(TLRequest):
    ID: int = 0xffb6d4ca

    def __init__(self, sticker: Any = None, position: Any = None) -> None:
        self.sticker = sticker
        self.position = position

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)
        writer.write_int32(self.position or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersChangeStickerPosition':
        sticker = reader.read_object()
        position = reader.read_int32()
        return cls(sticker=sticker, position=position)


@register_tl
class StickersAddStickerToSet(TLRequest):
    ID: int = 0x8653febe

    def __init__(self, stickerset: Any = None, sticker: Any = None) -> None:
        self.stickerset = stickerset
        self.sticker = sticker

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersAddStickerToSet':
        stickerset = reader.read_object()
        sticker = reader.read_object()
        return cls(stickerset=stickerset, sticker=sticker)


@register_tl
class StickersSetStickerSetThumb(TLRequest):
    ID: int = 0xa76a5392

    def __init__(self, thumb: Any = None, thumb_document_id: Any = None, stickerset: Any = None) -> None:
        self.thumb = thumb
        self.thumb_document_id = thumb_document_id
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.thumb is not None:
            flags |= (1 << 0)
        if self.thumb_document_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        if self.thumb is not None:
            if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        if self.thumb_document_id is not None:
            writer.write_int64(self.thumb_document_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersSetStickerSetThumb':
        flags = reader.read_uint32()
        stickerset = reader.read_object()
        thumb = reader.read_object() if (flags & (1 << 0)) else None
        thumb_document_id = reader.read_int64() if (flags & (1 << 1)) else None
        return cls(stickerset=stickerset, thumb=thumb, thumb_document_id=thumb_document_id)


@register_tl
class StickersCheckShortName(TLRequest):
    ID: int = 0x284b3639

    def __init__(self, short_name: Any = None) -> None:
        self.short_name = short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.short_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersCheckShortName':
        short_name = reader.read_string()
        return cls(short_name=short_name)


@register_tl
class StickersSuggestShortName(TLRequest):
    ID: int = 0x4dafc503

    def __init__(self, title: Any = None) -> None:
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersSuggestShortName':
        title = reader.read_string()
        return cls(title=title)


@register_tl
class StickersChangeSticker(TLRequest):
    ID: int = 0xf5537ebc

    def __init__(self, emoji: Any = None, mask_coords: Any = None, keywords: Any = None, sticker: Any = None) -> None:
        self.emoji = emoji
        self.mask_coords = mask_coords
        self.keywords = keywords
        self.sticker = sticker

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.emoji is not None:
            flags |= (1 << 0)
        if self.mask_coords is not None:
            flags |= (1 << 1)
        if self.keywords is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)
        if self.emoji is not None:
            writer.write_string(self.emoji or '')
        if self.mask_coords is not None:
            if self.mask_coords is not None and hasattr(self.mask_coords, 'write'): self.mask_coords.write(writer)
        if self.keywords is not None:
            writer.write_string(self.keywords or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersChangeSticker':
        flags = reader.read_uint32()
        sticker = reader.read_object()
        emoji = reader.read_string() if (flags & (1 << 0)) else None
        mask_coords = reader.read_object() if (flags & (1 << 1)) else None
        keywords = reader.read_string() if (flags & (1 << 2)) else None
        return cls(sticker=sticker, emoji=emoji, mask_coords=mask_coords, keywords=keywords)


@register_tl
class StickersRenameStickerSet(TLRequest):
    ID: int = 0x124b1c00

    def __init__(self, stickerset: Any = None, title: Any = None) -> None:
        self.stickerset = stickerset
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersRenameStickerSet':
        stickerset = reader.read_object()
        title = reader.read_string()
        return cls(stickerset=stickerset, title=title)


@register_tl
class StickersDeleteStickerSet(TLRequest):
    ID: int = 0x87704394

    def __init__(self, stickerset: Any = None) -> None:
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersDeleteStickerSet':
        stickerset = reader.read_object()
        return cls(stickerset=stickerset)


@register_tl
class StickersReplaceSticker(TLRequest):
    ID: int = 0x4696459a

    def __init__(self, sticker: Any = None, new_sticker: Any = None) -> None:
        self.sticker = sticker
        self.new_sticker = new_sticker

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.sticker is not None and hasattr(self.sticker, 'write'): self.sticker.write(writer)
        if self.new_sticker is not None and hasattr(self.new_sticker, 'write'): self.new_sticker.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickersReplaceSticker':
        sticker = reader.read_object()
        new_sticker = reader.read_object()
        return cls(sticker=sticker, new_sticker=new_sticker)


@register_tl
class PhoneGetCallConfig(TLRequest):
    ID: int = 0x55451fa9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetCallConfig':
        return cls()


@register_tl
class PhoneRequestCall(TLRequest):
    ID: int = 0x42ff96ed

    def __init__(self, video: bool = False, user_id: Any = None, random_id: Any = None, g_a_hash: Any = None, protocol: Any = None) -> None:
        self.video = video
        self.user_id = user_id
        self.random_id = random_id
        self.g_a_hash = g_a_hash
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.random_id or 0)
        writer.write_bytes(self.g_a_hash or b'')
        if self.protocol is not None and hasattr(self.protocol, 'write'): self.protocol.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneRequestCall':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        user_id = reader.read_object()
        random_id = reader.read_int32()
        g_a_hash = reader.read_bytes()
        protocol = reader.read_object()
        return cls(video=video, user_id=user_id, random_id=random_id, g_a_hash=g_a_hash, protocol=protocol)


@register_tl
class PhoneAcceptCall(TLRequest):
    ID: int = 0x3bd2b4a0

    def __init__(self, peer: Any = None, g_b: Any = None, protocol: Any = None) -> None:
        self.peer = peer
        self.g_b = g_b
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bytes(self.g_b or b'')
        if self.protocol is not None and hasattr(self.protocol, 'write'): self.protocol.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneAcceptCall':
        peer = reader.read_object()
        g_b = reader.read_bytes()
        protocol = reader.read_object()
        return cls(peer=peer, g_b=g_b, protocol=protocol)


@register_tl
class PhoneConfirmCall(TLRequest):
    ID: int = 0x2efe1722

    def __init__(self, peer: Any = None, g_a: Any = None, key_fingerprint: Any = None, protocol: Any = None) -> None:
        self.peer = peer
        self.g_a = g_a
        self.key_fingerprint = key_fingerprint
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bytes(self.g_a or b'')
        writer.write_int64(self.key_fingerprint or 0)
        if self.protocol is not None and hasattr(self.protocol, 'write'): self.protocol.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneConfirmCall':
        peer = reader.read_object()
        g_a = reader.read_bytes()
        key_fingerprint = reader.read_int64()
        protocol = reader.read_object()
        return cls(peer=peer, g_a=g_a, key_fingerprint=key_fingerprint, protocol=protocol)


@register_tl
class PhoneReceivedCall(TLRequest):
    ID: int = 0x17d54f61

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneReceivedCall':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class PhoneDiscardCall(TLRequest):
    ID: int = 0xb2cbc1c0

    def __init__(self, video: bool = False, peer: Any = None, duration: Any = None, reason: Any = None, connection_id: Any = None) -> None:
        self.video = video
        self.peer = peer
        self.duration = duration
        self.reason = reason
        self.connection_id = connection_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.duration or 0)
        if self.reason is not None and hasattr(self.reason, 'write'): self.reason.write(writer)
        writer.write_int64(self.connection_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneDiscardCall':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        peer = reader.read_object()
        duration = reader.read_int32()
        reason = reader.read_object()
        connection_id = reader.read_int64()
        return cls(video=video, peer=peer, duration=duration, reason=reason, connection_id=connection_id)


@register_tl
class PhoneSetCallRating(TLRequest):
    ID: int = 0x59ead627

    def __init__(self, user_initiative: bool = False, peer: Any = None, rating: Any = None, comment: Any = None) -> None:
        self.user_initiative = user_initiative
        self.peer = peer
        self.rating = rating
        self.comment = comment

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.user_initiative:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.rating or 0)
        writer.write_string(self.comment or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSetCallRating':
        flags = reader.read_uint32()
        user_initiative = bool(flags & (1 << 0))
        peer = reader.read_object()
        rating = reader.read_int32()
        comment = reader.read_string()
        return cls(user_initiative=user_initiative, peer=peer, rating=rating, comment=comment)


@register_tl
class PhoneSaveCallDebug(TLRequest):
    ID: int = 0x277add7e

    def __init__(self, peer: Any = None, debug: Any = None) -> None:
        self.peer = peer
        self.debug = debug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.debug is not None and hasattr(self.debug, 'write'): self.debug.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSaveCallDebug':
        peer = reader.read_object()
        debug = reader.read_object()
        return cls(peer=peer, debug=debug)


@register_tl
class PhoneSendSignalingData(TLRequest):
    ID: int = 0xff7a9383

    def __init__(self, peer: Any = None, data: Any = None) -> None:
        self.peer = peer
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSendSignalingData':
        peer = reader.read_object()
        data = reader.read_bytes()
        return cls(peer=peer, data=data)


@register_tl
class PhoneCreateGroupCall(TLRequest):
    ID: int = 0x48cdc6d8

    def __init__(self, rtmp_stream: bool = False, title: Any = None, schedule_date: Any = None, peer: Any = None, random_id: Any = None) -> None:
        self.rtmp_stream = rtmp_stream
        self.title = title
        self.schedule_date = schedule_date
        self.peer = peer
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rtmp_stream:
            flags |= (1 << 2)
        if self.title is not None:
            flags |= (1 << 0)
        if self.schedule_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.random_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCreateGroupCall':
        flags = reader.read_uint32()
        rtmp_stream = bool(flags & (1 << 2))
        peer = reader.read_object()
        random_id = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(rtmp_stream=rtmp_stream, peer=peer, random_id=random_id, title=title, schedule_date=schedule_date)


@register_tl
class PhoneJoinGroupCall(TLRequest):
    ID: int = 0x8fb53057

    def __init__(self, muted: bool = False, video_stopped: bool = False, invite_hash: Any = None, public_key: Any = None, block: Any = None, call: Any = None, join_as: Any = None, params: Any = None) -> None:
        self.muted = muted
        self.video_stopped = video_stopped
        self.invite_hash = invite_hash
        self.public_key = public_key
        self.block = block
        self.call = call
        self.join_as = join_as
        self.params = params

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.muted:
            flags |= (1 << 0)
        if self.video_stopped:
            flags |= (1 << 2)
        if self.invite_hash is not None:
            flags |= (1 << 1)
        if self.public_key is not None:
            flags |= (1 << 3)
        if self.block is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.join_as is not None and hasattr(self.join_as, 'write'): self.join_as.write(writer)
        if self.invite_hash is not None:
            writer.write_string(self.invite_hash or '')
        if self.public_key is not None:
            writer.write_int256(self.public_key or 0)
        if self.block is not None:
            writer.write_bytes(self.block or b'')
        if self.params is not None and hasattr(self.params, 'write'): self.params.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneJoinGroupCall':
        flags = reader.read_uint32()
        muted = bool(flags & (1 << 0))
        video_stopped = bool(flags & (1 << 2))
        call = reader.read_object()
        join_as = reader.read_object()
        invite_hash = reader.read_string() if (flags & (1 << 1)) else None
        public_key = reader.read_int256() if (flags & (1 << 3)) else None
        block = reader.read_bytes() if (flags & (1 << 3)) else None
        params = reader.read_object()
        return cls(muted=muted, video_stopped=video_stopped, call=call, join_as=join_as, invite_hash=invite_hash, public_key=public_key, block=block, params=params)


@register_tl
class PhoneLeaveGroupCall(TLRequest):
    ID: int = 0x500377f9

    def __init__(self, call: Any = None, source: Any = None) -> None:
        self.call = call
        self.source = source

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_int32(self.source or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneLeaveGroupCall':
        call = reader.read_object()
        source = reader.read_int32()
        return cls(call=call, source=source)


@register_tl
class PhoneInviteToGroupCall(TLRequest):
    ID: int = 0x7b393160

    def __init__(self, call: Any = None, users: Any = None) -> None:
        self.call = call
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneInviteToGroupCall':
        call = reader.read_object()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(call=call, users=users)


@register_tl
class PhoneDiscardGroupCall(TLRequest):
    ID: int = 0x7a777135

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneDiscardGroupCall':
        call = reader.read_object()
        return cls(call=call)


@register_tl
class PhoneToggleGroupCallSettings(TLRequest):
    ID: int = 0x974392f2

    def __init__(self, reset_invite_hash: bool = False, join_muted: Any = None, messages_enabled: Any = None, send_paid_messages_stars: Any = None, call: Any = None) -> None:
        self.reset_invite_hash = reset_invite_hash
        self.join_muted = join_muted
        self.messages_enabled = messages_enabled
        self.send_paid_messages_stars = send_paid_messages_stars
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reset_invite_hash:
            flags |= (1 << 1)
        if self.join_muted is not None:
            flags |= (1 << 0)
        if self.messages_enabled is not None:
            flags |= (1 << 2)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.join_muted is not None:
            writer.write_bool(bool(self.join_muted))
        if self.messages_enabled is not None:
            writer.write_bool(bool(self.messages_enabled))
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneToggleGroupCallSettings':
        flags = reader.read_uint32()
        reset_invite_hash = bool(flags & (1 << 1))
        call = reader.read_object()
        join_muted = reader.read_bool() if (flags & (1 << 0)) else None
        messages_enabled = reader.read_bool() if (flags & (1 << 2)) else None
        send_paid_messages_stars = reader.read_int64() if (flags & (1 << 3)) else None
        return cls(reset_invite_hash=reset_invite_hash, call=call, join_muted=join_muted, messages_enabled=messages_enabled, send_paid_messages_stars=send_paid_messages_stars)


@register_tl
class PhoneGetGroupCall(TLRequest):
    ID: int = 0x41845db

    def __init__(self, call: Any = None, limit: Any = None) -> None:
        self.call = call
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetGroupCall':
        call = reader.read_object()
        limit = reader.read_int32()
        return cls(call=call, limit=limit)


@register_tl
class PhoneGetGroupParticipants(TLRequest):
    ID: int = 0xc558d8ab

    def __init__(self, call: Any = None, ids: Any = None, sources: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.call = call
        self.ids = ids
        self.sources = sources
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_vector(self.ids or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.sources or [], lambda w, x: w.write_int32(x))
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetGroupParticipants':
        call = reader.read_object()
        ids = reader.read_vector(lambda r: reader.read_object())
        sources = reader.read_vector(lambda r: r.read_int32())
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(call=call, ids=ids, sources=sources, offset=offset, limit=limit)


@register_tl
class PhoneCheckGroupCall(TLRequest):
    ID: int = 0xb59cf977

    def __init__(self, call: Any = None, sources: Any = None) -> None:
        self.call = call
        self.sources = sources

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_vector(self.sources or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCheckGroupCall':
        call = reader.read_object()
        sources = reader.read_vector(lambda r: r.read_int32())
        return cls(call=call, sources=sources)


@register_tl
class PhoneToggleGroupCallRecord(TLRequest):
    ID: int = 0xf128c708

    def __init__(self, start: bool = False, video: bool = False, title: Any = None, video_portrait: Any = None, call: Any = None) -> None:
        self.start = start
        self.video = video
        self.title = title
        self.video_portrait = video_portrait
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.start:
            flags |= (1 << 0)
        if self.video:
            flags |= (1 << 2)
        if self.title is not None:
            flags |= (1 << 1)
        if self.video_portrait is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.video_portrait is not None:
            writer.write_bool(bool(self.video_portrait))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneToggleGroupCallRecord':
        flags = reader.read_uint32()
        start = bool(flags & (1 << 0))
        video = bool(flags & (1 << 2))
        call = reader.read_object()
        title = reader.read_string() if (flags & (1 << 1)) else None
        video_portrait = reader.read_bool() if (flags & (1 << 2)) else None
        return cls(start=start, video=video, call=call, title=title, video_portrait=video_portrait)


@register_tl
class PhoneEditGroupCallParticipant(TLRequest):
    ID: int = 0xa5273abf

    def __init__(self, muted: Any = None, volume: Any = None, raise_hand: Any = None, video_stopped: Any = None, video_paused: Any = None, presentation_paused: Any = None, call: Any = None, participant: Any = None) -> None:
        self.muted = muted
        self.volume = volume
        self.raise_hand = raise_hand
        self.video_stopped = video_stopped
        self.video_paused = video_paused
        self.presentation_paused = presentation_paused
        self.call = call
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.muted is not None:
            flags |= (1 << 0)
        if self.volume is not None:
            flags |= (1 << 1)
        if self.raise_hand is not None:
            flags |= (1 << 2)
        if self.video_stopped is not None:
            flags |= (1 << 3)
        if self.video_paused is not None:
            flags |= (1 << 4)
        if self.presentation_paused is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)
        if self.muted is not None:
            writer.write_bool(bool(self.muted))
        if self.volume is not None:
            writer.write_int32(self.volume or 0)
        if self.raise_hand is not None:
            writer.write_bool(bool(self.raise_hand))
        if self.video_stopped is not None:
            writer.write_bool(bool(self.video_stopped))
        if self.video_paused is not None:
            writer.write_bool(bool(self.video_paused))
        if self.presentation_paused is not None:
            writer.write_bool(bool(self.presentation_paused))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneEditGroupCallParticipant':
        flags = reader.read_uint32()
        call = reader.read_object()
        participant = reader.read_object()
        muted = reader.read_bool() if (flags & (1 << 0)) else None
        volume = reader.read_int32() if (flags & (1 << 1)) else None
        raise_hand = reader.read_bool() if (flags & (1 << 2)) else None
        video_stopped = reader.read_bool() if (flags & (1 << 3)) else None
        video_paused = reader.read_bool() if (flags & (1 << 4)) else None
        presentation_paused = reader.read_bool() if (flags & (1 << 5)) else None
        return cls(call=call, participant=participant, muted=muted, volume=volume, raise_hand=raise_hand, video_stopped=video_stopped, video_paused=video_paused, presentation_paused=presentation_paused)


@register_tl
class PhoneEditGroupCallTitle(TLRequest):
    ID: int = 0x1ca6ac0a

    def __init__(self, call: Any = None, title: Any = None) -> None:
        self.call = call
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneEditGroupCallTitle':
        call = reader.read_object()
        title = reader.read_string()
        return cls(call=call, title=title)


@register_tl
class PhoneGetGroupCallJoinAs(TLRequest):
    ID: int = 0xef7c213a

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetGroupCallJoinAs':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class PhoneExportGroupCallInvite(TLRequest):
    ID: int = 0xe6aa647f

    def __init__(self, can_self_unmute: bool = False, call: Any = None) -> None:
        self.can_self_unmute = can_self_unmute
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_self_unmute:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneExportGroupCallInvite':
        flags = reader.read_uint32()
        can_self_unmute = bool(flags & (1 << 0))
        call = reader.read_object()
        return cls(can_self_unmute=can_self_unmute, call=call)


@register_tl
class PhoneToggleGroupCallStartSubscription(TLRequest):
    ID: int = 0x219c34e6

    def __init__(self, call: Any = None, subscribed: Any = None) -> None:
        self.call = call
        self.subscribed = subscribed

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_bool(bool(self.subscribed))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneToggleGroupCallStartSubscription':
        call = reader.read_object()
        subscribed = reader.read_bool()
        return cls(call=call, subscribed=subscribed)


@register_tl
class PhoneStartScheduledGroupCall(TLRequest):
    ID: int = 0x5680e342

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneStartScheduledGroupCall':
        call = reader.read_object()
        return cls(call=call)


@register_tl
class PhoneSaveDefaultGroupCallJoinAs(TLRequest):
    ID: int = 0x575e1f8c

    def __init__(self, peer: Any = None, join_as: Any = None) -> None:
        self.peer = peer
        self.join_as = join_as

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.join_as is not None and hasattr(self.join_as, 'write'): self.join_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSaveDefaultGroupCallJoinAs':
        peer = reader.read_object()
        join_as = reader.read_object()
        return cls(peer=peer, join_as=join_as)


@register_tl
class PhoneJoinGroupCallPresentation(TLRequest):
    ID: int = 0xcbea6bc4

    def __init__(self, call: Any = None, params: Any = None) -> None:
        self.call = call
        self.params = params

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.params is not None and hasattr(self.params, 'write'): self.params.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneJoinGroupCallPresentation':
        call = reader.read_object()
        params = reader.read_object()
        return cls(call=call, params=params)


@register_tl
class PhoneLeaveGroupCallPresentation(TLRequest):
    ID: int = 0x1c50d144

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneLeaveGroupCallPresentation':
        call = reader.read_object()
        return cls(call=call)


@register_tl
class PhoneGetGroupCallStreamChannels(TLRequest):
    ID: int = 0x1ab21940

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetGroupCallStreamChannels':
        call = reader.read_object()
        return cls(call=call)


@register_tl
class PhoneGetGroupCallStreamRtmpUrl(TLRequest):
    ID: int = 0x5af4c73a

    def __init__(self, live_story: bool = False, peer: Any = None, revoke: Any = None) -> None:
        self.live_story = live_story
        self.peer = peer
        self.revoke = revoke

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.live_story:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bool(bool(self.revoke))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetGroupCallStreamRtmpUrl':
        flags = reader.read_uint32()
        live_story = bool(flags & (1 << 0))
        peer = reader.read_object()
        revoke = reader.read_bool()
        return cls(live_story=live_story, peer=peer, revoke=revoke)


@register_tl
class PhoneSaveCallLog(TLRequest):
    ID: int = 0x41248786

    def __init__(self, peer: Any = None, file: Any = None) -> None:
        self.peer = peer
        self.file = file

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSaveCallLog':
        peer = reader.read_object()
        file = reader.read_object()
        return cls(peer=peer, file=file)


@register_tl
class PhoneCreateConferenceCall(TLRequest):
    ID: int = 0x7d0444bb

    def __init__(self, muted: bool = False, video_stopped: bool = False, join: bool = False, public_key: Any = None, block: Any = None, params: Any = None, random_id: Any = None) -> None:
        self.muted = muted
        self.video_stopped = video_stopped
        self.join = join
        self.public_key = public_key
        self.block = block
        self.params = params
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.muted:
            flags |= (1 << 0)
        if self.video_stopped:
            flags |= (1 << 2)
        if self.join:
            flags |= (1 << 3)
        if self.public_key is not None:
            flags |= (1 << 3)
        if self.block is not None:
            flags |= (1 << 3)
        if self.params is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int32(self.random_id or 0)
        if self.public_key is not None:
            writer.write_int256(self.public_key or 0)
        if self.block is not None:
            writer.write_bytes(self.block or b'')
        if self.params is not None:
            if self.params is not None and hasattr(self.params, 'write'): self.params.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCreateConferenceCall':
        flags = reader.read_uint32()
        muted = bool(flags & (1 << 0))
        video_stopped = bool(flags & (1 << 2))
        join = bool(flags & (1 << 3))
        random_id = reader.read_int32()
        public_key = reader.read_int256() if (flags & (1 << 3)) else None
        block = reader.read_bytes() if (flags & (1 << 3)) else None
        params = reader.read_object() if (flags & (1 << 3)) else None
        return cls(muted=muted, video_stopped=video_stopped, join=join, random_id=random_id, public_key=public_key, block=block, params=params)


@register_tl
class PhoneDeleteConferenceCallParticipants(TLRequest):
    ID: int = 0x8ca60525

    def __init__(self, only_left: bool = False, kick: bool = False, call: Any = None, ids: Any = None, block: Any = None) -> None:
        self.only_left = only_left
        self.kick = kick
        self.call = call
        self.ids = ids
        self.block = block

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.only_left:
            flags |= (1 << 0)
        if self.kick:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_vector(self.ids or [], lambda w, x: w.write_int64(x))
        writer.write_bytes(self.block or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneDeleteConferenceCallParticipants':
        flags = reader.read_uint32()
        only_left = bool(flags & (1 << 0))
        kick = bool(flags & (1 << 1))
        call = reader.read_object()
        ids = reader.read_vector(lambda r: r.read_int64())
        block = reader.read_bytes()
        return cls(only_left=only_left, kick=kick, call=call, ids=ids, block=block)


@register_tl
class PhoneSendConferenceCallBroadcast(TLRequest):
    ID: int = 0xc6701900

    def __init__(self, call: Any = None, block: Any = None) -> None:
        self.call = call
        self.block = block

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_bytes(self.block or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSendConferenceCallBroadcast':
        call = reader.read_object()
        block = reader.read_bytes()
        return cls(call=call, block=block)


@register_tl
class PhoneInviteConferenceCallParticipant(TLRequest):
    ID: int = 0xbcf22685

    def __init__(self, video: bool = False, call: Any = None, user_id: Any = None) -> None:
        self.video = video
        self.call = call
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneInviteConferenceCallParticipant':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        call = reader.read_object()
        user_id = reader.read_object()
        return cls(video=video, call=call, user_id=user_id)


@register_tl
class PhoneDeclineConferenceCallInvite(TLRequest):
    ID: int = 0x3c479971

    def __init__(self, msg_id: Any = None) -> None:
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneDeclineConferenceCallInvite':
        msg_id = reader.read_int32()
        return cls(msg_id=msg_id)


@register_tl
class PhoneGetGroupCallChainBlocks(TLRequest):
    ID: int = 0xee9f88a6

    def __init__(self, call: Any = None, sub_chain_id: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.call = call
        self.sub_chain_id = sub_chain_id
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_int32(self.sub_chain_id or 0)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetGroupCallChainBlocks':
        call = reader.read_object()
        sub_chain_id = reader.read_int32()
        offset = reader.read_int32()
        limit = reader.read_int32()
        return cls(call=call, sub_chain_id=sub_chain_id, offset=offset, limit=limit)


@register_tl
class PhoneSendGroupCallMessage(TLRequest):
    ID: int = 0xb1d11410

    def __init__(self, allow_paid_stars: Any = None, send_as: Any = None, call: Any = None, random_id: Any = None, message: Any = None) -> None:
        self.allow_paid_stars = allow_paid_stars
        self.send_as = send_as
        self.call = call
        self.random_id = random_id
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.allow_paid_stars is not None:
            flags |= (1 << 0)
        if self.send_as is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_int64(self.random_id or 0)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSendGroupCallMessage':
        flags = reader.read_uint32()
        call = reader.read_object()
        random_id = reader.read_int64()
        message = reader.read_object()
        allow_paid_stars = reader.read_int64() if (flags & (1 << 0)) else None
        send_as = reader.read_object() if (flags & (1 << 1)) else None
        return cls(call=call, random_id=random_id, message=message, allow_paid_stars=allow_paid_stars, send_as=send_as)


@register_tl
class PhoneSendGroupCallEncryptedMessage(TLRequest):
    ID: int = 0xe5afa56d

    def __init__(self, call: Any = None, encrypted_message: Any = None) -> None:
        self.call = call
        self.encrypted_message = encrypted_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_bytes(self.encrypted_message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSendGroupCallEncryptedMessage':
        call = reader.read_object()
        encrypted_message = reader.read_bytes()
        return cls(call=call, encrypted_message=encrypted_message)


@register_tl
class PhoneDeleteGroupCallMessages(TLRequest):
    ID: int = 0xf64f54f7

    def __init__(self, report_spam: bool = False, call: Any = None, messages: Any = None) -> None:
        self.report_spam = report_spam
        self.call = call
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.report_spam:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_vector(self.messages or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneDeleteGroupCallMessages':
        flags = reader.read_uint32()
        report_spam = bool(flags & (1 << 0))
        call = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_int32())
        return cls(report_spam=report_spam, call=call, messages=messages)


@register_tl
class PhoneDeleteGroupCallParticipantMessages(TLRequest):
    ID: int = 0x1dbfeca0

    def __init__(self, report_spam: bool = False, call: Any = None, participant: Any = None) -> None:
        self.report_spam = report_spam
        self.call = call
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.report_spam:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneDeleteGroupCallParticipantMessages':
        flags = reader.read_uint32()
        report_spam = bool(flags & (1 << 0))
        call = reader.read_object()
        participant = reader.read_object()
        return cls(report_spam=report_spam, call=call, participant=participant)


@register_tl
class PhoneGetGroupCallStars(TLRequest):
    ID: int = 0x6f636302

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneGetGroupCallStars':
        call = reader.read_object()
        return cls(call=call)


@register_tl
class PhoneSaveDefaultSendAs(TLRequest):
    ID: int = 0x4167add1

    def __init__(self, call: Any = None, send_as: Any = None) -> None:
        self.call = call
        self.send_as = send_as

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneSaveDefaultSendAs':
        call = reader.read_object()
        send_as = reader.read_object()
        return cls(call=call, send_as=send_as)


@register_tl
class LangpackGetLangPack(TLRequest):
    ID: int = 0xf2f2330a

    def __init__(self, lang_pack: Any = None, lang_code: Any = None) -> None:
        self.lang_pack = lang_pack
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_pack or '')
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'LangpackGetLangPack':
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        return cls(lang_pack=lang_pack, lang_code=lang_code)


@register_tl
class LangpackGetStrings(TLRequest):
    ID: int = 0xefea3803

    def __init__(self, lang_pack: Any = None, lang_code: Any = None, keys: Any = None) -> None:
        self.lang_pack = lang_pack
        self.lang_code = lang_code
        self.keys = keys

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_pack or '')
        writer.write_string(self.lang_code or '')
        writer.write_vector(self.keys or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'LangpackGetStrings':
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        keys = reader.read_vector(lambda r: r.read_string())
        return cls(lang_pack=lang_pack, lang_code=lang_code, keys=keys)


@register_tl
class LangpackGetDifference(TLRequest):
    ID: int = 0xcd984aa5

    def __init__(self, lang_pack: Any = None, lang_code: Any = None, from_version: Any = None) -> None:
        self.lang_pack = lang_pack
        self.lang_code = lang_code
        self.from_version = from_version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_pack or '')
        writer.write_string(self.lang_code or '')
        writer.write_int32(self.from_version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'LangpackGetDifference':
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        from_version = reader.read_int32()
        return cls(lang_pack=lang_pack, lang_code=lang_code, from_version=from_version)


@register_tl
class LangpackGetLanguages(TLRequest):
    ID: int = 0x42c6978f

    def __init__(self, lang_pack: Any = None) -> None:
        self.lang_pack = lang_pack

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_pack or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'LangpackGetLanguages':
        lang_pack = reader.read_string()
        return cls(lang_pack=lang_pack)


@register_tl
class LangpackGetLanguage(TLRequest):
    ID: int = 0x6a596502

    def __init__(self, lang_pack: Any = None, lang_code: Any = None) -> None:
        self.lang_pack = lang_pack
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_pack or '')
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'LangpackGetLanguage':
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        return cls(lang_pack=lang_pack, lang_code=lang_code)


@register_tl
class FoldersEditPeerFolders(TLRequest):
    ID: int = 0x6847d0ab

    def __init__(self, folder_peers: Any = None) -> None:
        self.folder_peers = folder_peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.folder_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'FoldersEditPeerFolders':
        folder_peers = reader.read_vector(lambda r: reader.read_object())
        return cls(folder_peers=folder_peers)


@register_tl
class StatsGetBroadcastStats(TLRequest):
    ID: int = 0xab42441a

    def __init__(self, dark: bool = False, channel: Any = None) -> None:
        self.dark = dark
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGetBroadcastStats':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        channel = reader.read_object()
        return cls(dark=dark, channel=channel)


@register_tl
class StatsLoadAsyncGraph(TLRequest):
    ID: int = 0x621d5fa0

    def __init__(self, x: Any = None, token: Any = None) -> None:
        self.x = x
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.x is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.token or '')
        if self.x is not None:
            writer.write_int64(self.x or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsLoadAsyncGraph':
        flags = reader.read_uint32()
        token = reader.read_string()
        x = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(token=token, x=x)


@register_tl
class StatsGetMegagroupStats(TLRequest):
    ID: int = 0xdcdf8607

    def __init__(self, dark: bool = False, channel: Any = None) -> None:
        self.dark = dark
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGetMegagroupStats':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        channel = reader.read_object()
        return cls(dark=dark, channel=channel)


@register_tl
class StatsGetMessagePublicForwards(TLRequest):
    ID: int = 0x5f150144

    def __init__(self, channel: Any = None, msg_id: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.channel = channel
        self.msg_id = msg_id
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGetMessagePublicForwards':
        channel = reader.read_object()
        msg_id = reader.read_int32()
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(channel=channel, msg_id=msg_id, offset=offset, limit=limit)


@register_tl
class StatsGetMessageStats(TLRequest):
    ID: int = 0xb6e0a3f5

    def __init__(self, dark: bool = False, channel: Any = None, msg_id: Any = None) -> None:
        self.dark = dark
        self.channel = channel
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGetMessageStats':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        channel = reader.read_object()
        msg_id = reader.read_int32()
        return cls(dark=dark, channel=channel, msg_id=msg_id)


@register_tl
class StatsGetStoryStats(TLRequest):
    ID: int = 0x374fef40

    def __init__(self, dark: bool = False, peer: Any = None, id: Any = None) -> None:
        self.dark = dark
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StatsGetStoryStats':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        peer = reader.read_object()
        id = reader.read_int32()
        return cls(dark=dark, peer=peer, id=id)

