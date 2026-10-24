from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class Message(TLObject):
    ID: int = 0x95ef6f2b

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, silent: bool = False, post: bool = False, from_scheduled: bool = False, legacy: bool = False, edit_hide: bool = False, pinned: bool = False, noforwards: bool = False, invert_media: bool = False, offline: bool = False, video_processing_pending: bool = False, paid_suggested_post_stars: bool = False, paid_suggested_post_ton: bool = False, from_id: Any = None, from_boosts_applied: Any = None, from_rank: Any = None, saved_peer_id: Any = None, fwd_from: Any = None, via_bot_id: Any = None, via_business_bot_id: Any = None, guestchat_via_from: Any = None, reply_to: Any = None, media: Any = None, reply_markup: Any = None, entities: Any = None, views: Any = None, forwards: Any = None, replies: Any = None, edit_date: Any = None, post_author: Any = None, grouped_id: Any = None, reactions: Any = None, restriction_reason: Any = None, ttl_period: Any = None, quick_reply_shortcut_id: Any = None, effect: Any = None, factcheck: Any = None, report_delivery_until_date: Any = None, paid_message_stars: Any = None, suggested_post: Any = None, schedule_repeat_period: Any = None, summary_from_language: Any = None, id: Any = None, peer_id: Any = None, date: Any = None, message: Any = None) -> None:
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.silent = silent
        self.post = post
        self.from_scheduled = from_scheduled
        self.legacy = legacy
        self.edit_hide = edit_hide
        self.pinned = pinned
        self.noforwards = noforwards
        self.invert_media = invert_media
        self.offline = offline
        self.video_processing_pending = video_processing_pending
        self.paid_suggested_post_stars = paid_suggested_post_stars
        self.paid_suggested_post_ton = paid_suggested_post_ton
        self.from_id = from_id
        self.from_boosts_applied = from_boosts_applied
        self.from_rank = from_rank
        self.saved_peer_id = saved_peer_id
        self.fwd_from = fwd_from
        self.via_bot_id = via_bot_id
        self.via_business_bot_id = via_business_bot_id
        self.guestchat_via_from = guestchat_via_from
        self.reply_to = reply_to
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities
        self.views = views
        self.forwards = forwards
        self.replies = replies
        self.edit_date = edit_date
        self.post_author = post_author
        self.grouped_id = grouped_id
        self.reactions = reactions
        self.restriction_reason = restriction_reason
        self.ttl_period = ttl_period
        self.quick_reply_shortcut_id = quick_reply_shortcut_id
        self.effect = effect
        self.factcheck = factcheck
        self.report_delivery_until_date = report_delivery_until_date
        self.paid_message_stars = paid_message_stars
        self.suggested_post = suggested_post
        self.schedule_repeat_period = schedule_repeat_period
        self.summary_from_language = summary_from_language
        self.id = id
        self.peer_id = peer_id
        self.date = date
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        flags2 = 0
        if self.out:
            flags |= (1 << 1)
        if self.mentioned:
            flags |= (1 << 4)
        if self.media_unread:
            flags |= (1 << 5)
        if self.silent:
            flags |= (1 << 13)
        if self.post:
            flags |= (1 << 14)
        if self.from_scheduled:
            flags |= (1 << 18)
        if self.legacy:
            flags |= (1 << 19)
        if self.edit_hide:
            flags |= (1 << 21)
        if self.pinned:
            flags |= (1 << 24)
        if self.noforwards:
            flags |= (1 << 26)
        if self.invert_media:
            flags |= (1 << 27)
        if self.offline:
            flags2 |= (1 << 1)
        if self.video_processing_pending:
            flags2 |= (1 << 4)
        if self.paid_suggested_post_stars:
            flags2 |= (1 << 8)
        if self.paid_suggested_post_ton:
            flags2 |= (1 << 9)
        if self.from_id is not None:
            flags |= (1 << 8)
        if self.from_boosts_applied is not None:
            flags |= (1 << 29)
        if self.from_rank is not None:
            flags2 |= (1 << 12)
        if self.saved_peer_id is not None:
            flags |= (1 << 28)
        if self.fwd_from is not None:
            flags |= (1 << 2)
        if self.via_bot_id is not None:
            flags |= (1 << 11)
        if self.via_business_bot_id is not None:
            flags2 |= (1 << 0)
        if self.guestchat_via_from is not None:
            flags2 |= (1 << 19)
        if self.reply_to is not None:
            flags |= (1 << 3)
        if self.media is not None:
            flags |= (1 << 9)
        if self.reply_markup is not None:
            flags |= (1 << 6)
        if self.entities is not None:
            flags |= (1 << 7)
        if self.views is not None:
            flags |= (1 << 10)
        if self.forwards is not None:
            flags |= (1 << 10)
        if self.replies is not None:
            flags |= (1 << 23)
        if self.edit_date is not None:
            flags |= (1 << 15)
        if self.post_author is not None:
            flags |= (1 << 16)
        if self.grouped_id is not None:
            flags |= (1 << 17)
        if self.reactions is not None:
            flags |= (1 << 20)
        if self.restriction_reason is not None:
            flags |= (1 << 22)
        if self.ttl_period is not None:
            flags |= (1 << 25)
        if self.quick_reply_shortcut_id is not None:
            flags |= (1 << 30)
        if self.effect is not None:
            flags2 |= (1 << 2)
        if self.factcheck is not None:
            flags2 |= (1 << 3)
        if self.report_delivery_until_date is not None:
            flags2 |= (1 << 5)
        if self.paid_message_stars is not None:
            flags2 |= (1 << 6)
        if self.suggested_post is not None:
            flags2 |= (1 << 7)
        if self.schedule_repeat_period is not None:
            flags2 |= (1 << 10)
        if self.summary_from_language is not None:
            flags2 |= (1 << 11)
        writer.write_uint32(flags)
        writer.write_uint32(flags2)
        writer.write_int32(self.id or 0)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.from_boosts_applied is not None:
            writer.write_int32(self.from_boosts_applied or 0)
        if self.from_rank is not None:
            writer.write_string(self.from_rank or '')
        if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        if self.fwd_from is not None:
            if self.fwd_from is not None and hasattr(self.fwd_from, 'write'): self.fwd_from.write(writer)
        if self.via_bot_id is not None:
            writer.write_int64(self.via_bot_id or 0)
        if self.via_business_bot_id is not None:
            writer.write_int64(self.via_business_bot_id or 0)
        if self.guestchat_via_from is not None:
            if self.guestchat_via_from is not None and hasattr(self.guestchat_via_from, 'write'): self.guestchat_via_from.write(writer)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        writer.write_int32(self.date or 0)
        writer.write_string(self.message or '')
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.reply_markup is not None:
            if self.reply_markup is not None and hasattr(self.reply_markup, 'write'): self.reply_markup.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.views is not None:
            writer.write_int32(self.views or 0)
        if self.forwards is not None:
            writer.write_int32(self.forwards or 0)
        if self.replies is not None:
            if self.replies is not None and hasattr(self.replies, 'write'): self.replies.write(writer)
        if self.edit_date is not None:
            writer.write_int32(self.edit_date or 0)
        if self.post_author is not None:
            writer.write_string(self.post_author or '')
        if self.grouped_id is not None:
            writer.write_int64(self.grouped_id or 0)
        if self.reactions is not None:
            if self.reactions is not None and hasattr(self.reactions, 'write'): self.reactions.write(writer)
        if self.restriction_reason is not None:
            writer.write_vector(self.restriction_reason or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.quick_reply_shortcut_id is not None:
            writer.write_int32(self.quick_reply_shortcut_id or 0)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.factcheck is not None:
            if self.factcheck is not None and hasattr(self.factcheck, 'write'): self.factcheck.write(writer)
        if self.report_delivery_until_date is not None:
            writer.write_int32(self.report_delivery_until_date or 0)
        if self.paid_message_stars is not None:
            writer.write_int64(self.paid_message_stars or 0)
        if self.suggested_post is not None:
            if self.suggested_post is not None and hasattr(self.suggested_post, 'write'): self.suggested_post.write(writer)
        if self.schedule_repeat_period is not None:
            writer.write_int32(self.schedule_repeat_period or 0)
        if self.summary_from_language is not None:
            writer.write_string(self.summary_from_language or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'Message':
        flags = reader.read_uint32()
        flags2 = reader.read_uint32()
        out = bool(flags & (1 << 1))
        mentioned = bool(flags & (1 << 4))
        media_unread = bool(flags & (1 << 5))
        silent = bool(flags & (1 << 13))
        post = bool(flags & (1 << 14))
        from_scheduled = bool(flags & (1 << 18))
        legacy = bool(flags & (1 << 19))
        edit_hide = bool(flags & (1 << 21))
        pinned = bool(flags & (1 << 24))
        noforwards = bool(flags & (1 << 26))
        invert_media = bool(flags & (1 << 27))
        offline = bool(flags2 & (1 << 1))
        video_processing_pending = bool(flags2 & (1 << 4))
        paid_suggested_post_stars = bool(flags2 & (1 << 8))
        paid_suggested_post_ton = bool(flags2 & (1 << 9))
        id = reader.read_int32()
        from_id = reader.read_object() if (flags & (1 << 8)) else None
        from_boosts_applied = reader.read_int32() if (flags & (1 << 29)) else None
        from_rank = reader.read_string() if (flags2 & (1 << 12)) else None
        peer_id = reader.read_object()
        saved_peer_id = reader.read_object() if (flags & (1 << 28)) else None
        fwd_from = reader.read_object() if (flags & (1 << 2)) else None
        via_bot_id = reader.read_int64() if (flags & (1 << 11)) else None
        via_business_bot_id = reader.read_int64() if (flags2 & (1 << 0)) else None
        guestchat_via_from = reader.read_object() if (flags2 & (1 << 19)) else None
        reply_to = reader.read_object() if (flags & (1 << 3)) else None
        date = reader.read_int32()
        message = reader.read_string()
        media = reader.read_object() if (flags & (1 << 9)) else None
        reply_markup = reader.read_object() if (flags & (1 << 6)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 7)) else None
        views = reader.read_int32() if (flags & (1 << 10)) else None
        forwards = reader.read_int32() if (flags & (1 << 10)) else None
        replies = reader.read_object() if (flags & (1 << 23)) else None
        edit_date = reader.read_int32() if (flags & (1 << 15)) else None
        post_author = reader.read_string() if (flags & (1 << 16)) else None
        grouped_id = reader.read_int64() if (flags & (1 << 17)) else None
        reactions = reader.read_object() if (flags & (1 << 20)) else None
        restriction_reason = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 22)) else None
        ttl_period = reader.read_int32() if (flags & (1 << 25)) else None
        quick_reply_shortcut_id = reader.read_int32() if (flags & (1 << 30)) else None
        effect = reader.read_int64() if (flags2 & (1 << 2)) else None
        factcheck = reader.read_object() if (flags2 & (1 << 3)) else None
        report_delivery_until_date = reader.read_int32() if (flags2 & (1 << 5)) else None
        paid_message_stars = reader.read_int64() if (flags2 & (1 << 6)) else None
        suggested_post = reader.read_object() if (flags2 & (1 << 7)) else None
        schedule_repeat_period = reader.read_int32() if (flags2 & (1 << 10)) else None
        summary_from_language = reader.read_string() if (flags2 & (1 << 11)) else None
        return cls(out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, post=post, from_scheduled=from_scheduled, legacy=legacy, edit_hide=edit_hide, pinned=pinned, noforwards=noforwards, invert_media=invert_media, offline=offline, video_processing_pending=video_processing_pending, paid_suggested_post_stars=paid_suggested_post_stars, paid_suggested_post_ton=paid_suggested_post_ton, id=id, from_id=from_id, from_boosts_applied=from_boosts_applied, from_rank=from_rank, peer_id=peer_id, saved_peer_id=saved_peer_id, fwd_from=fwd_from, via_bot_id=via_bot_id, via_business_bot_id=via_business_bot_id, guestchat_via_from=guestchat_via_from, reply_to=reply_to, date=date, message=message, media=media, reply_markup=reply_markup, entities=entities, views=views, forwards=forwards, replies=replies, edit_date=edit_date, post_author=post_author, grouped_id=grouped_id, reactions=reactions, restriction_reason=restriction_reason, ttl_period=ttl_period, quick_reply_shortcut_id=quick_reply_shortcut_id, effect=effect, factcheck=factcheck, report_delivery_until_date=report_delivery_until_date, paid_message_stars=paid_message_stars, suggested_post=suggested_post, schedule_repeat_period=schedule_repeat_period, summary_from_language=summary_from_language)


@register_tl
class MessageService(TLObject):
    ID: int = 0x7a800e0a

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, reactions_are_possible: bool = False, silent: bool = False, post: bool = False, legacy: bool = False, from_id: Any = None, saved_peer_id: Any = None, reply_to: Any = None, reactions: Any = None, ttl_period: Any = None, id: Any = None, peer_id: Any = None, date: Any = None, action: Any = None) -> None:
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.reactions_are_possible = reactions_are_possible
        self.silent = silent
        self.post = post
        self.legacy = legacy
        self.from_id = from_id
        self.saved_peer_id = saved_peer_id
        self.reply_to = reply_to
        self.reactions = reactions
        self.ttl_period = ttl_period
        self.id = id
        self.peer_id = peer_id
        self.date = date
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.out:
            flags |= (1 << 1)
        if self.mentioned:
            flags |= (1 << 4)
        if self.media_unread:
            flags |= (1 << 5)
        if self.reactions_are_possible:
            flags |= (1 << 9)
        if self.silent:
            flags |= (1 << 13)
        if self.post:
            flags |= (1 << 14)
        if self.legacy:
            flags |= (1 << 19)
        if self.from_id is not None:
            flags |= (1 << 8)
        if self.saved_peer_id is not None:
            flags |= (1 << 28)
        if self.reply_to is not None:
            flags |= (1 << 3)
        if self.reactions is not None:
            flags |= (1 << 20)
        if self.ttl_period is not None:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        if self.reply_to is not None:
            if self.reply_to is not None and hasattr(self.reply_to, 'write'): self.reply_to.write(writer)
        writer.write_int32(self.date or 0)
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)
        if self.reactions is not None:
            if self.reactions is not None and hasattr(self.reactions, 'write'): self.reactions.write(writer)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageService':
        flags = reader.read_uint32()
        out = bool(flags & (1 << 1))
        mentioned = bool(flags & (1 << 4))
        media_unread = bool(flags & (1 << 5))
        reactions_are_possible = bool(flags & (1 << 9))
        silent = bool(flags & (1 << 13))
        post = bool(flags & (1 << 14))
        legacy = bool(flags & (1 << 19))
        id = reader.read_int32()
        from_id = reader.read_object() if (flags & (1 << 8)) else None
        peer_id = reader.read_object()
        saved_peer_id = reader.read_object() if (flags & (1 << 28)) else None
        reply_to = reader.read_object() if (flags & (1 << 3)) else None
        date = reader.read_int32()
        action = reader.read_object()
        reactions = reader.read_object() if (flags & (1 << 20)) else None
        ttl_period = reader.read_int32() if (flags & (1 << 25)) else None
        return cls(out=out, mentioned=mentioned, media_unread=media_unread, reactions_are_possible=reactions_are_possible, silent=silent, post=post, legacy=legacy, id=id, from_id=from_id, peer_id=peer_id, saved_peer_id=saved_peer_id, reply_to=reply_to, date=date, action=action, reactions=reactions, ttl_period=ttl_period)


@register_tl
class MessageMediaEmpty(TLObject):
    ID: int = 0x3ded6320

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaEmpty':
        return cls()


@register_tl
class MessageMediaPhoto(TLObject):
    ID: int = 0xe216eb63

    def __init__(self, spoiler: bool = False, live_photo: bool = False, photo: Any = None, ttl_seconds: Any = None, video: Any = None) -> None:
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.photo = photo
        self.ttl_seconds = ttl_seconds
        self.video = video

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 3)
        if self.live_photo:
            flags |= (1 << 4)
        if self.photo is not None:
            flags |= (1 << 0)
        if self.ttl_seconds is not None:
            flags |= (1 << 2)
        if self.video is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video is not None:
            if self.video is not None and hasattr(self.video, 'write'): self.video.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPhoto':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 3))
        live_photo = bool(flags & (1 << 4))
        photo = reader.read_object() if (flags & (1 << 0)) else None
        ttl_seconds = reader.read_int32() if (flags & (1 << 2)) else None
        video = reader.read_object() if (flags & (1 << 4)) else None
        return cls(spoiler=spoiler, live_photo=live_photo, photo=photo, ttl_seconds=ttl_seconds, video=video)


@register_tl
class MessageMediaGeo(TLObject):
    ID: int = 0x56e0d474

    def __init__(self, geo: Any = None) -> None:
        self.geo = geo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGeo':
        geo = reader.read_object()
        return cls(geo=geo)


@register_tl
class MessageMediaContact(TLObject):
    ID: int = 0x70322949

    def __init__(self, phone_number: Any = None, first_name: Any = None, last_name: Any = None, vcard: Any = None, user_id: Any = None) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_string(self.vcard or '')
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaContact':
        phone_number = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        vcard = reader.read_string()
        user_id = reader.read_int64()
        return cls(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard, user_id=user_id)


@register_tl
class MessageMediaUnsupported(TLObject):
    ID: int = 0x9f84f49e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaUnsupported':
        return cls()


@register_tl
class MessageMediaDocument(TLObject):
    ID: int = 0x52d8ccd9

    def __init__(self, nopremium: bool = False, spoiler: bool = False, video: bool = False, round: bool = False, voice: bool = False, document: Any = None, alt_documents: Any = None, video_cover: Any = None, video_timestamp: Any = None, ttl_seconds: Any = None) -> None:
        self.nopremium = nopremium
        self.spoiler = spoiler
        self.video = video
        self.round = round
        self.voice = voice
        self.document = document
        self.alt_documents = alt_documents
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp
        self.ttl_seconds = ttl_seconds

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.nopremium:
            flags |= (1 << 3)
        if self.spoiler:
            flags |= (1 << 4)
        if self.video:
            flags |= (1 << 6)
        if self.round:
            flags |= (1 << 7)
        if self.voice:
            flags |= (1 << 8)
        if self.document is not None:
            flags |= (1 << 0)
        if self.alt_documents is not None:
            flags |= (1 << 5)
        if self.video_cover is not None:
            flags |= (1 << 9)
        if self.video_timestamp is not None:
            flags |= (1 << 10)
        if self.ttl_seconds is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.alt_documents is not None:
            writer.write_vector(self.alt_documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.video_cover is not None:
            if self.video_cover is not None and hasattr(self.video_cover, 'write'): self.video_cover.write(writer)
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaDocument':
        flags = reader.read_uint32()
        nopremium = bool(flags & (1 << 3))
        spoiler = bool(flags & (1 << 4))
        video = bool(flags & (1 << 6))
        round = bool(flags & (1 << 7))
        voice = bool(flags & (1 << 8))
        document = reader.read_object() if (flags & (1 << 0)) else None
        alt_documents = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 5)) else None
        video_cover = reader.read_object() if (flags & (1 << 9)) else None
        video_timestamp = reader.read_int32() if (flags & (1 << 10)) else None
        ttl_seconds = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(nopremium=nopremium, spoiler=spoiler, video=video, round=round, voice=voice, document=document, alt_documents=alt_documents, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds)


@register_tl
class MessageMediaWebPage(TLObject):
    ID: int = 0xddf10c3b

    def __init__(self, force_large_media: bool = False, force_small_media: bool = False, manual: bool = False, safe: bool = False, webpage: Any = None) -> None:
        self.force_large_media = force_large_media
        self.force_small_media = force_small_media
        self.manual = manual
        self.safe = safe
        self.webpage = webpage

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.force_large_media:
            flags |= (1 << 0)
        if self.force_small_media:
            flags |= (1 << 1)
        if self.manual:
            flags |= (1 << 3)
        if self.safe:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.webpage is not None and hasattr(self.webpage, 'write'): self.webpage.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaWebPage':
        flags = reader.read_uint32()
        force_large_media = bool(flags & (1 << 0))
        force_small_media = bool(flags & (1 << 1))
        manual = bool(flags & (1 << 3))
        safe = bool(flags & (1 << 4))
        webpage = reader.read_object()
        return cls(force_large_media=force_large_media, force_small_media=force_small_media, manual=manual, safe=safe, webpage=webpage)


@register_tl
class MessageMediaVenue(TLObject):
    ID: int = 0x2ec0533f

    def __init__(self, geo: Any = None, title: Any = None, address: Any = None, provider: Any = None, venue_id: Any = None, venue_type: Any = None) -> None:
        self.geo = geo
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        writer.write_string(self.title or '')
        writer.write_string(self.address or '')
        writer.write_string(self.provider or '')
        writer.write_string(self.venue_id or '')
        writer.write_string(self.venue_type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaVenue':
        geo = reader.read_object()
        title = reader.read_string()
        address = reader.read_string()
        provider = reader.read_string()
        venue_id = reader.read_string()
        venue_type = reader.read_string()
        return cls(geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)


@register_tl
class MessageMediaGame(TLObject):
    ID: int = 0xfdb19008

    def __init__(self, game: Any = None) -> None:
        self.game = game

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.game is not None and hasattr(self.game, 'write'): self.game.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGame':
        game = reader.read_object()
        return cls(game=game)


@register_tl
class MessageMediaInvoice(TLObject):
    ID: int = 0xf6a548d3

    def __init__(self, shipping_address_requested: bool = False, test: bool = False, photo: Any = None, receipt_msg_id: Any = None, extended_media: Any = None, title: Any = None, description: Any = None, currency: Any = None, total_amount: Any = None, start_param: Any = None) -> None:
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.photo = photo
        self.receipt_msg_id = receipt_msg_id
        self.extended_media = extended_media
        self.title = title
        self.description = description
        self.currency = currency
        self.total_amount = total_amount
        self.start_param = start_param

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.shipping_address_requested:
            flags |= (1 << 1)
        if self.test:
            flags |= (1 << 3)
        if self.photo is not None:
            flags |= (1 << 0)
        if self.receipt_msg_id is not None:
            flags |= (1 << 2)
        if self.extended_media is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.receipt_msg_id is not None:
            writer.write_int32(self.receipt_msg_id or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)
        writer.write_string(self.start_param or '')
        if self.extended_media is not None:
            if self.extended_media is not None and hasattr(self.extended_media, 'write'): self.extended_media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaInvoice':
        flags = reader.read_uint32()
        shipping_address_requested = bool(flags & (1 << 1))
        test = bool(flags & (1 << 3))
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 0)) else None
        receipt_msg_id = reader.read_int32() if (flags & (1 << 2)) else None
        currency = reader.read_string()
        total_amount = reader.read_int64()
        start_param = reader.read_string()
        extended_media = reader.read_object() if (flags & (1 << 4)) else None
        return cls(shipping_address_requested=shipping_address_requested, test=test, title=title, description=description, photo=photo, receipt_msg_id=receipt_msg_id, currency=currency, total_amount=total_amount, start_param=start_param, extended_media=extended_media)


@register_tl
class MessageMediaGeoLive(TLObject):
    ID: int = 0xb940c666

    def __init__(self, heading: Any = None, proximity_notification_radius: Any = None, geo: Any = None, period: Any = None) -> None:
        self.heading = heading
        self.proximity_notification_radius = proximity_notification_radius
        self.geo = geo
        self.period = period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.heading is not None:
            flags |= (1 << 0)
        if self.proximity_notification_radius is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        if self.heading is not None:
            writer.write_int32(self.heading or 0)
        writer.write_int32(self.period or 0)
        if self.proximity_notification_radius is not None:
            writer.write_int32(self.proximity_notification_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGeoLive':
        flags = reader.read_uint32()
        geo = reader.read_object()
        heading = reader.read_int32() if (flags & (1 << 0)) else None
        period = reader.read_int32()
        proximity_notification_radius = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(geo=geo, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius)


@register_tl
class MessageMediaPoll(TLObject):
    ID: int = 0x773f4e66

    def __init__(self, attached_media: Any = None, poll: Any = None, results: Any = None) -> None:
        self.attached_media = attached_media
        self.poll = poll
        self.results = results

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attached_media is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.poll is not None and hasattr(self.poll, 'write'): self.poll.write(writer)
        if self.results is not None and hasattr(self.results, 'write'): self.results.write(writer)
        if self.attached_media is not None:
            if self.attached_media is not None and hasattr(self.attached_media, 'write'): self.attached_media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPoll':
        flags = reader.read_uint32()
        poll = reader.read_object()
        results = reader.read_object()
        attached_media = reader.read_object() if (flags & (1 << 0)) else None
        return cls(poll=poll, results=results, attached_media=attached_media)


@register_tl
class MessageMediaDice(TLObject):
    ID: int = 0x8cbec07

    def __init__(self, game_outcome: Any = None, value: Any = None, emoticon: Any = None) -> None:
        self.game_outcome = game_outcome
        self.value = value
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.game_outcome is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.value or 0)
        writer.write_string(self.emoticon or '')
        if self.game_outcome is not None:
            if self.game_outcome is not None and hasattr(self.game_outcome, 'write'): self.game_outcome.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaDice':
        flags = reader.read_uint32()
        value = reader.read_int32()
        emoticon = reader.read_string()
        game_outcome = reader.read_object() if (flags & (1 << 0)) else None
        return cls(value=value, emoticon=emoticon, game_outcome=game_outcome)


@register_tl
class MessageMediaStory(TLObject):
    ID: int = 0x68cb6283

    def __init__(self, via_mention: bool = False, story: Any = None, peer: Any = None, id: Any = None) -> None:
        self.via_mention = via_mention
        self.story = story
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_mention:
            flags |= (1 << 1)
        if self.story is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.story is not None:
            if self.story is not None and hasattr(self.story, 'write'): self.story.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaStory':
        flags = reader.read_uint32()
        via_mention = bool(flags & (1 << 1))
        peer = reader.read_object()
        id = reader.read_int32()
        story = reader.read_object() if (flags & (1 << 0)) else None
        return cls(via_mention=via_mention, peer=peer, id=id, story=story)


@register_tl
class MessageMediaGiveaway(TLObject):
    ID: int = 0xaa073beb

    def __init__(self, only_new_subscribers: bool = False, winners_are_visible: bool = False, countries_iso2: Any = None, prize_description: Any = None, months: Any = None, stars: Any = None, channels: Any = None, quantity: Any = None, until_date: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.winners_are_visible = winners_are_visible
        self.countries_iso2 = countries_iso2
        self.prize_description = prize_description
        self.months = months
        self.stars = stars
        self.channels = channels
        self.quantity = quantity
        self.until_date = until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.only_new_subscribers:
            flags |= (1 << 0)
        if self.winners_are_visible:
            flags |= (1 << 2)
        if self.countries_iso2 is not None:
            flags |= (1 << 1)
        if self.prize_description is not None:
            flags |= (1 << 3)
        if self.months is not None:
            flags |= (1 << 4)
        if self.stars is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_vector(self.channels or [], lambda w, x: w.write_int64(x))
        if self.countries_iso2 is not None:
            writer.write_vector(self.countries_iso2 or [], lambda w, x: w.write_string(x))
        if self.prize_description is not None:
            writer.write_string(self.prize_description or '')
        writer.write_int32(self.quantity or 0)
        if self.months is not None:
            writer.write_int32(self.months or 0)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)
        writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGiveaway':
        flags = reader.read_uint32()
        only_new_subscribers = bool(flags & (1 << 0))
        winners_are_visible = bool(flags & (1 << 2))
        channels = reader.read_vector(lambda r: r.read_int64())
        countries_iso2 = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 1)) else None
        prize_description = reader.read_string() if (flags & (1 << 3)) else None
        quantity = reader.read_int32()
        months = reader.read_int32() if (flags & (1 << 4)) else None
        stars = reader.read_int64() if (flags & (1 << 5)) else None
        until_date = reader.read_int32()
        return cls(only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, channels=channels, countries_iso2=countries_iso2, prize_description=prize_description, quantity=quantity, months=months, stars=stars, until_date=until_date)


@register_tl
class MessageMediaGiveawayResults(TLObject):
    ID: int = 0xceaa3ea1

    def __init__(self, only_new_subscribers: bool = False, refunded: bool = False, additional_peers_count: Any = None, months: Any = None, stars: Any = None, prize_description: Any = None, channel_id: Any = None, launch_msg_id: Any = None, winners_count: Any = None, unclaimed_count: Any = None, winners: Any = None, until_date: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.refunded = refunded
        self.additional_peers_count = additional_peers_count
        self.months = months
        self.stars = stars
        self.prize_description = prize_description
        self.channel_id = channel_id
        self.launch_msg_id = launch_msg_id
        self.winners_count = winners_count
        self.unclaimed_count = unclaimed_count
        self.winners = winners
        self.until_date = until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.only_new_subscribers:
            flags |= (1 << 0)
        if self.refunded:
            flags |= (1 << 2)
        if self.additional_peers_count is not None:
            flags |= (1 << 3)
        if self.months is not None:
            flags |= (1 << 4)
        if self.stars is not None:
            flags |= (1 << 5)
        if self.prize_description is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.additional_peers_count is not None:
            writer.write_int32(self.additional_peers_count or 0)
        writer.write_int32(self.launch_msg_id or 0)
        writer.write_int32(self.winners_count or 0)
        writer.write_int32(self.unclaimed_count or 0)
        writer.write_vector(self.winners or [], lambda w, x: w.write_int64(x))
        if self.months is not None:
            writer.write_int32(self.months or 0)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)
        if self.prize_description is not None:
            writer.write_string(self.prize_description or '')
        writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGiveawayResults':
        flags = reader.read_uint32()
        only_new_subscribers = bool(flags & (1 << 0))
        refunded = bool(flags & (1 << 2))
        channel_id = reader.read_int64()
        additional_peers_count = reader.read_int32() if (flags & (1 << 3)) else None
        launch_msg_id = reader.read_int32()
        winners_count = reader.read_int32()
        unclaimed_count = reader.read_int32()
        winners = reader.read_vector(lambda r: r.read_int64())
        months = reader.read_int32() if (flags & (1 << 4)) else None
        stars = reader.read_int64() if (flags & (1 << 5)) else None
        prize_description = reader.read_string() if (flags & (1 << 1)) else None
        until_date = reader.read_int32()
        return cls(only_new_subscribers=only_new_subscribers, refunded=refunded, channel_id=channel_id, additional_peers_count=additional_peers_count, launch_msg_id=launch_msg_id, winners_count=winners_count, unclaimed_count=unclaimed_count, winners=winners, months=months, stars=stars, prize_description=prize_description, until_date=until_date)


@register_tl
class MessageMediaPaidMedia(TLObject):
    ID: int = 0xa8852491

    def __init__(self, stars_amount: Any = None, extended_media: Any = None) -> None:
        self.stars_amount = stars_amount
        self.extended_media = extended_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.stars_amount or 0)
        writer.write_vector(self.extended_media or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPaidMedia':
        stars_amount = reader.read_int64()
        extended_media = reader.read_vector(lambda r: reader.read_object())
        return cls(stars_amount=stars_amount, extended_media=extended_media)


@register_tl
class MessageMediaToDo(TLObject):
    ID: int = 0x8a53b014

    def __init__(self, completions: Any = None, todo: Any = None) -> None:
        self.completions = completions
        self.todo = todo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.completions is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.todo is not None and hasattr(self.todo, 'write'): self.todo.write(writer)
        if self.completions is not None:
            writer.write_vector(self.completions or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaToDo':
        flags = reader.read_uint32()
        todo = reader.read_object()
        completions = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        return cls(todo=todo, completions=completions)


@register_tl
class MessageMediaVideoStream(TLObject):
    ID: int = 0xca5cab89

    def __init__(self, rtmp_stream: bool = False, call: Any = None) -> None:
        self.rtmp_stream = rtmp_stream
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rtmp_stream:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaVideoStream':
        flags = reader.read_uint32()
        rtmp_stream = bool(flags & (1 << 0))
        call = reader.read_object()
        return cls(rtmp_stream=rtmp_stream, call=call)


@register_tl
class MessageActionEmpty(TLObject):
    ID: int = 0xb6aef7b0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionEmpty':
        return cls()


@register_tl
class MessageActionChatCreate(TLObject):
    ID: int = 0xbd47cbad

    def __init__(self, title: Any = None, users: Any = None) -> None:
        self.title = title
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_vector(self.users or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatCreate':
        title = reader.read_string()
        users = reader.read_vector(lambda r: r.read_int64())
        return cls(title=title, users=users)


@register_tl
class MessageActionChatEditTitle(TLObject):
    ID: int = 0xb5a1ce5a

    def __init__(self, title: Any = None) -> None:
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatEditTitle':
        title = reader.read_string()
        return cls(title=title)


@register_tl
class MessageActionChatEditPhoto(TLObject):
    ID: int = 0x7fcb13a8

    def __init__(self, photo: Any = None) -> None:
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatEditPhoto':
        photo = reader.read_object()
        return cls(photo=photo)


@register_tl
class MessageActionChatDeletePhoto(TLObject):
    ID: int = 0x95e3fbef

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatDeletePhoto':
        return cls()


@register_tl
class MessageActionChatAddUser(TLObject):
    ID: int = 0x15cefd00

    def __init__(self, users: Any = None) -> None:
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.users or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatAddUser':
        users = reader.read_vector(lambda r: r.read_int64())
        return cls(users=users)


@register_tl
class MessageActionChatDeleteUser(TLObject):
    ID: int = 0xa43f30cc

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatDeleteUser':
        user_id = reader.read_int64()
        return cls(user_id=user_id)


@register_tl
class MessageActionChatJoinedByLink(TLObject):
    ID: int = 0x31224c3

    def __init__(self, inviter_id: Any = None) -> None:
        self.inviter_id = inviter_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.inviter_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatJoinedByLink':
        inviter_id = reader.read_int64()
        return cls(inviter_id=inviter_id)


@register_tl
class MessageActionChannelCreate(TLObject):
    ID: int = 0x95d2ac92

    def __init__(self, title: Any = None) -> None:
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChannelCreate':
        title = reader.read_string()
        return cls(title=title)


@register_tl
class MessageActionChatMigrateTo(TLObject):
    ID: int = 0xe1037f92

    def __init__(self, channel_id: Any = None) -> None:
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatMigrateTo':
        channel_id = reader.read_int64()
        return cls(channel_id=channel_id)


@register_tl
class MessageActionChannelMigrateFrom(TLObject):
    ID: int = 0xea3948e9

    def __init__(self, title: Any = None, chat_id: Any = None) -> None:
        self.title = title
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.title or '')
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChannelMigrateFrom':
        title = reader.read_string()
        chat_id = reader.read_int64()
        return cls(title=title, chat_id=chat_id)


@register_tl
class MessageActionPinMessage(TLObject):
    ID: int = 0x94bd38ed

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPinMessage':
        return cls()


@register_tl
class MessageActionHistoryClear(TLObject):
    ID: int = 0x9fbab604

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionHistoryClear':
        return cls()


@register_tl
class MessageActionGameScore(TLObject):
    ID: int = 0x92a72876

    def __init__(self, game_id: Any = None, score: Any = None) -> None:
        self.game_id = game_id
        self.score = score

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.game_id or 0)
        writer.write_int32(self.score or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGameScore':
        game_id = reader.read_int64()
        score = reader.read_int32()
        return cls(game_id=game_id, score=score)


@register_tl
class MessageActionPaymentSentMe(TLObject):
    ID: int = 0xffa00ccc

    def __init__(self, recurring_init: bool = False, recurring_used: bool = False, info: Any = None, shipping_option_id: Any = None, subscription_until_date: Any = None, currency: Any = None, total_amount: Any = None, payload: Any = None, charge: Any = None) -> None:
        self.recurring_init = recurring_init
        self.recurring_used = recurring_used
        self.info = info
        self.shipping_option_id = shipping_option_id
        self.subscription_until_date = subscription_until_date
        self.currency = currency
        self.total_amount = total_amount
        self.payload = payload
        self.charge = charge

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.recurring_init:
            flags |= (1 << 2)
        if self.recurring_used:
            flags |= (1 << 3)
        if self.info is not None:
            flags |= (1 << 0)
        if self.shipping_option_id is not None:
            flags |= (1 << 1)
        if self.subscription_until_date is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)
        writer.write_bytes(self.payload or b'')
        if self.info is not None:
            if self.info is not None and hasattr(self.info, 'write'): self.info.write(writer)
        if self.shipping_option_id is not None:
            writer.write_string(self.shipping_option_id or '')
        if self.charge is not None and hasattr(self.charge, 'write'): self.charge.write(writer)
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentSentMe':
        flags = reader.read_uint32()
        recurring_init = bool(flags & (1 << 2))
        recurring_used = bool(flags & (1 << 3))
        currency = reader.read_string()
        total_amount = reader.read_int64()
        payload = reader.read_bytes()
        info = reader.read_object() if (flags & (1 << 0)) else None
        shipping_option_id = reader.read_string() if (flags & (1 << 1)) else None
        charge = reader.read_object()
        subscription_until_date = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(recurring_init=recurring_init, recurring_used=recurring_used, currency=currency, total_amount=total_amount, payload=payload, info=info, shipping_option_id=shipping_option_id, charge=charge, subscription_until_date=subscription_until_date)


@register_tl
class MessageActionPaymentSent(TLObject):
    ID: int = 0xc624b16e

    def __init__(self, recurring_init: bool = False, recurring_used: bool = False, invoice_slug: Any = None, subscription_until_date: Any = None, currency: Any = None, total_amount: Any = None) -> None:
        self.recurring_init = recurring_init
        self.recurring_used = recurring_used
        self.invoice_slug = invoice_slug
        self.subscription_until_date = subscription_until_date
        self.currency = currency
        self.total_amount = total_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.recurring_init:
            flags |= (1 << 2)
        if self.recurring_used:
            flags |= (1 << 3)
        if self.invoice_slug is not None:
            flags |= (1 << 0)
        if self.subscription_until_date is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)
        if self.invoice_slug is not None:
            writer.write_string(self.invoice_slug or '')
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentSent':
        flags = reader.read_uint32()
        recurring_init = bool(flags & (1 << 2))
        recurring_used = bool(flags & (1 << 3))
        currency = reader.read_string()
        total_amount = reader.read_int64()
        invoice_slug = reader.read_string() if (flags & (1 << 0)) else None
        subscription_until_date = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(recurring_init=recurring_init, recurring_used=recurring_used, currency=currency, total_amount=total_amount, invoice_slug=invoice_slug, subscription_until_date=subscription_until_date)


@register_tl
class MessageActionPhoneCall(TLObject):
    ID: int = 0x80e11a7f

    def __init__(self, video: bool = False, reason: Any = None, duration: Any = None, call_id: Any = None) -> None:
        self.video = video
        self.reason = reason
        self.duration = duration
        self.call_id = call_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 2)
        if self.reason is not None:
            flags |= (1 << 0)
        if self.duration is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.call_id or 0)
        if self.reason is not None:
            if self.reason is not None and hasattr(self.reason, 'write'): self.reason.write(writer)
        if self.duration is not None:
            writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPhoneCall':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 2))
        call_id = reader.read_int64()
        reason = reader.read_object() if (flags & (1 << 0)) else None
        duration = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(video=video, call_id=call_id, reason=reason, duration=duration)


@register_tl
class MessageActionScreenshotTaken(TLObject):
    ID: int = 0x4792929b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionScreenshotTaken':
        return cls()


@register_tl
class MessageActionCustomAction(TLObject):
    ID: int = 0xfae69f56

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.message or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionCustomAction':
        message = reader.read_string()
        return cls(message=message)


@register_tl
class MessageActionBotAllowed(TLObject):
    ID: int = 0xc516d679

    def __init__(self, attach_menu: bool = False, from_request: bool = False, domain: Any = None, app: Any = None) -> None:
        self.attach_menu = attach_menu
        self.from_request = from_request
        self.domain = domain
        self.app = app

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attach_menu:
            flags |= (1 << 1)
        if self.from_request:
            flags |= (1 << 3)
        if self.domain is not None:
            flags |= (1 << 0)
        if self.app is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.domain is not None:
            writer.write_string(self.domain or '')
        if self.app is not None:
            if self.app is not None and hasattr(self.app, 'write'): self.app.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionBotAllowed':
        flags = reader.read_uint32()
        attach_menu = bool(flags & (1 << 1))
        from_request = bool(flags & (1 << 3))
        domain = reader.read_string() if (flags & (1 << 0)) else None
        app = reader.read_object() if (flags & (1 << 2)) else None
        return cls(attach_menu=attach_menu, from_request=from_request, domain=domain, app=app)


@register_tl
class MessageActionSecureValuesSentMe(TLObject):
    ID: int = 0x1b287353

    def __init__(self, values: Any = None, credentials: Any = None) -> None:
        self.values = values
        self.credentials = credentials

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.values or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.credentials is not None and hasattr(self.credentials, 'write'): self.credentials.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSecureValuesSentMe':
        values = reader.read_vector(lambda r: reader.read_object())
        credentials = reader.read_object()
        return cls(values=values, credentials=credentials)


@register_tl
class MessageActionSecureValuesSent(TLObject):
    ID: int = 0xd95c6154

    def __init__(self, types: Any = None) -> None:
        self.types = types

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSecureValuesSent':
        types = reader.read_vector(lambda r: reader.read_object())
        return cls(types=types)


@register_tl
class MessageActionContactSignUp(TLObject):
    ID: int = 0xf3f25f76

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionContactSignUp':
        return cls()


@register_tl
class MessageActionGeoProximityReached(TLObject):
    ID: int = 0x98e0d697

    def __init__(self, from_id: Any = None, to_id: Any = None, distance: Any = None) -> None:
        self.from_id = from_id
        self.to_id = to_id
        self.distance = distance

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.to_id is not None and hasattr(self.to_id, 'write'): self.to_id.write(writer)
        writer.write_int32(self.distance or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGeoProximityReached':
        from_id = reader.read_object()
        to_id = reader.read_object()
        distance = reader.read_int32()
        return cls(from_id=from_id, to_id=to_id, distance=distance)


@register_tl
class MessageActionGroupCall(TLObject):
    ID: int = 0x7a0d7f42

    def __init__(self, duration: Any = None, call: Any = None) -> None:
        self.duration = duration
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.duration is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.duration is not None:
            writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGroupCall':
        flags = reader.read_uint32()
        call = reader.read_object()
        duration = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(call=call, duration=duration)


@register_tl
class MessageActionInviteToGroupCall(TLObject):
    ID: int = 0x502f92f7

    def __init__(self, call: Any = None, users: Any = None) -> None:
        self.call = call
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_vector(self.users or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionInviteToGroupCall':
        call = reader.read_object()
        users = reader.read_vector(lambda r: r.read_int64())
        return cls(call=call, users=users)


@register_tl
class MessageActionSetMessagesTTL(TLObject):
    ID: int = 0x3c134d7b

    def __init__(self, auto_setting_from: Any = None, period: Any = None) -> None:
        self.auto_setting_from = auto_setting_from
        self.period = period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.auto_setting_from is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.period or 0)
        if self.auto_setting_from is not None:
            writer.write_int64(self.auto_setting_from or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSetMessagesTTL':
        flags = reader.read_uint32()
        period = reader.read_int32()
        auto_setting_from = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(period=period, auto_setting_from=auto_setting_from)


@register_tl
class MessageActionGroupCallScheduled(TLObject):
    ID: int = 0xb3a07661

    def __init__(self, call: Any = None, schedule_date: Any = None) -> None:
        self.call = call
        self.schedule_date = schedule_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_int32(self.schedule_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGroupCallScheduled':
        call = reader.read_object()
        schedule_date = reader.read_int32()
        return cls(call=call, schedule_date=schedule_date)


@register_tl
class MessageActionSetChatTheme(TLObject):
    ID: int = 0xb91bbd3a

    def __init__(self, theme: Any = None) -> None:
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSetChatTheme':
        theme = reader.read_object()
        return cls(theme=theme)


@register_tl
class MessageActionChatJoinedByRequest(TLObject):
    ID: int = 0xebbca3cb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatJoinedByRequest':
        return cls()


@register_tl
class MessageActionWebViewDataSentMe(TLObject):
    ID: int = 0x47dd8079

    def __init__(self, text: Any = None, data: Any = None) -> None:
        self.text = text
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_string(self.data or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionWebViewDataSentMe':
        text = reader.read_string()
        data = reader.read_string()
        return cls(text=text, data=data)


@register_tl
class MessageActionWebViewDataSent(TLObject):
    ID: int = 0xb4c38cb5

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionWebViewDataSent':
        text = reader.read_string()
        return cls(text=text)


@register_tl
class MessageActionGiftPremium(TLObject):
    ID: int = 0x48e91302

    def __init__(self, crypto_currency: Any = None, crypto_amount: Any = None, message: Any = None, currency: Any = None, amount: Any = None, days: Any = None) -> None:
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.message = message
        self.currency = currency
        self.amount = amount
        self.days = days

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.crypto_currency is not None:
            flags |= (1 << 0)
        if self.crypto_amount is not None:
            flags |= (1 << 0)
        if self.message is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        writer.write_int32(self.days or 0)
        if self.crypto_currency is not None:
            writer.write_string(self.crypto_currency or '')
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftPremium':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        days = reader.read_int32()
        crypto_currency = reader.read_string() if (flags & (1 << 0)) else None
        crypto_amount = reader.read_int64() if (flags & (1 << 0)) else None
        message = reader.read_object() if (flags & (1 << 1)) else None
        return cls(currency=currency, amount=amount, days=days, crypto_currency=crypto_currency, crypto_amount=crypto_amount, message=message)


@register_tl
class MessageActionTopicCreate(TLObject):
    ID: int = 0xd999256

    def __init__(self, title_missing: bool = False, icon_emoji_id: Any = None, title: Any = None, icon_color: Any = None) -> None:
        self.title_missing = title_missing
        self.icon_emoji_id = icon_emoji_id
        self.title = title
        self.icon_color = icon_color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title_missing:
            flags |= (1 << 1)
        if self.icon_emoji_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_int32(self.icon_color or 0)
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTopicCreate':
        flags = reader.read_uint32()
        title_missing = bool(flags & (1 << 1))
        title = reader.read_string()
        icon_color = reader.read_int32()
        icon_emoji_id = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(title_missing=title_missing, title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id)


@register_tl
class MessageActionTopicEdit(TLObject):
    ID: int = 0xc0944820

    def __init__(self, title: Any = None, icon_emoji_id: Any = None, closed: Any = None, hidden: Any = None) -> None:
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.closed = closed
        self.hidden = hidden

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        if self.icon_emoji_id is not None:
            flags |= (1 << 1)
        if self.closed is not None:
            flags |= (1 << 2)
        if self.hidden is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)
        if self.closed is not None:
            writer.write_bool(bool(self.closed))
        if self.hidden is not None:
            writer.write_bool(bool(self.hidden))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTopicEdit':
        flags = reader.read_uint32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        icon_emoji_id = reader.read_int64() if (flags & (1 << 1)) else None
        closed = reader.read_bool() if (flags & (1 << 2)) else None
        hidden = reader.read_bool() if (flags & (1 << 3)) else None
        return cls(title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)


@register_tl
class MessageActionSuggestProfilePhoto(TLObject):
    ID: int = 0x57de635e

    def __init__(self, photo: Any = None) -> None:
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestProfilePhoto':
        photo = reader.read_object()
        return cls(photo=photo)


@register_tl
class MessageActionRequestedPeer(TLObject):
    ID: int = 0x31518e9b

    def __init__(self, button_id: Any = None, peers: Any = None) -> None:
        self.button_id = button_id
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.button_id or 0)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionRequestedPeer':
        button_id = reader.read_int32()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(button_id=button_id, peers=peers)


@register_tl
class MessageActionSetChatWallPaper(TLObject):
    ID: int = 0x5060a3f4

    def __init__(self, same: bool = False, for_both: bool = False, wallpaper: Any = None) -> None:
        self.same = same
        self.for_both = for_both
        self.wallpaper = wallpaper

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.same:
            flags |= (1 << 0)
        if self.for_both:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSetChatWallPaper':
        flags = reader.read_uint32()
        same = bool(flags & (1 << 0))
        for_both = bool(flags & (1 << 1))
        wallpaper = reader.read_object()
        return cls(same=same, for_both=for_both, wallpaper=wallpaper)


@register_tl
class MessageActionGiftCode(TLObject):
    ID: int = 0x31c48347

    def __init__(self, via_giveaway: bool = False, unclaimed: bool = False, boost_peer: Any = None, currency: Any = None, amount: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, message: Any = None, days: Any = None, slug: Any = None) -> None:
        self.via_giveaway = via_giveaway
        self.unclaimed = unclaimed
        self.boost_peer = boost_peer
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.message = message
        self.days = days
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_giveaway:
            flags |= (1 << 0)
        if self.unclaimed:
            flags |= (1 << 5)
        if self.boost_peer is not None:
            flags |= (1 << 1)
        if self.currency is not None:
            flags |= (1 << 2)
        if self.amount is not None:
            flags |= (1 << 2)
        if self.crypto_currency is not None:
            flags |= (1 << 3)
        if self.crypto_amount is not None:
            flags |= (1 << 3)
        if self.message is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.boost_peer is not None:
            if self.boost_peer is not None and hasattr(self.boost_peer, 'write'): self.boost_peer.write(writer)
        writer.write_int32(self.days or 0)
        writer.write_string(self.slug or '')
        if self.currency is not None:
            writer.write_string(self.currency or '')
        if self.amount is not None:
            writer.write_int64(self.amount or 0)
        if self.crypto_currency is not None:
            writer.write_string(self.crypto_currency or '')
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftCode':
        flags = reader.read_uint32()
        via_giveaway = bool(flags & (1 << 0))
        unclaimed = bool(flags & (1 << 5))
        boost_peer = reader.read_object() if (flags & (1 << 1)) else None
        days = reader.read_int32()
        slug = reader.read_string()
        currency = reader.read_string() if (flags & (1 << 2)) else None
        amount = reader.read_int64() if (flags & (1 << 2)) else None
        crypto_currency = reader.read_string() if (flags & (1 << 3)) else None
        crypto_amount = reader.read_int64() if (flags & (1 << 3)) else None
        message = reader.read_object() if (flags & (1 << 4)) else None
        return cls(via_giveaway=via_giveaway, unclaimed=unclaimed, boost_peer=boost_peer, days=days, slug=slug, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, message=message)


@register_tl
class MessageActionGiveawayLaunch(TLObject):
    ID: int = 0xa80f51e4

    def __init__(self, stars: Any = None) -> None:
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.stars is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiveawayLaunch':
        flags = reader.read_uint32()
        stars = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(stars=stars)


@register_tl
class MessageActionGiveawayResults(TLObject):
    ID: int = 0x87e2f155

    def __init__(self, stars: bool = False, winners_count: Any = None, unclaimed_count: Any = None) -> None:
        self.stars = stars
        self.winners_count = winners_count
        self.unclaimed_count = unclaimed_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.stars:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.winners_count or 0)
        writer.write_int32(self.unclaimed_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiveawayResults':
        flags = reader.read_uint32()
        stars = bool(flags & (1 << 0))
        winners_count = reader.read_int32()
        unclaimed_count = reader.read_int32()
        return cls(stars=stars, winners_count=winners_count, unclaimed_count=unclaimed_count)


@register_tl
class MessageActionBoostApply(TLObject):
    ID: int = 0xcc02aa6d

    def __init__(self, boosts: Any = None) -> None:
        self.boosts = boosts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.boosts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionBoostApply':
        boosts = reader.read_int32()
        return cls(boosts=boosts)


@register_tl
class MessageActionRequestedPeerSentMe(TLObject):
    ID: int = 0x93b31848

    def __init__(self, button_id: Any = None, peers: Any = None) -> None:
        self.button_id = button_id
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.button_id or 0)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionRequestedPeerSentMe':
        button_id = reader.read_int32()
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(button_id=button_id, peers=peers)


@register_tl
class MessageActionPaymentRefunded(TLObject):
    ID: int = 0x41b3e202

    def __init__(self, payload: Any = None, peer: Any = None, currency: Any = None, total_amount: Any = None, charge: Any = None) -> None:
        self.payload = payload
        self.peer = peer
        self.currency = currency
        self.total_amount = total_amount
        self.charge = charge

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.payload is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)
        if self.payload is not None:
            writer.write_bytes(self.payload or b'')
        if self.charge is not None and hasattr(self.charge, 'write'): self.charge.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentRefunded':
        flags = reader.read_uint32()
        peer = reader.read_object()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        payload = reader.read_bytes() if (flags & (1 << 0)) else None
        charge = reader.read_object()
        return cls(peer=peer, currency=currency, total_amount=total_amount, payload=payload, charge=charge)


@register_tl
class MessageActionGiftStars(TLObject):
    ID: int = 0x45d5b021

    def __init__(self, crypto_currency: Any = None, crypto_amount: Any = None, transaction_id: Any = None, currency: Any = None, amount: Any = None, stars: Any = None) -> None:
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.transaction_id = transaction_id
        self.currency = currency
        self.amount = amount
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.crypto_currency is not None:
            flags |= (1 << 0)
        if self.crypto_amount is not None:
            flags |= (1 << 0)
        if self.transaction_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        writer.write_int64(self.stars or 0)
        if self.crypto_currency is not None:
            writer.write_string(self.crypto_currency or '')
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.transaction_id is not None:
            writer.write_string(self.transaction_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftStars':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        stars = reader.read_int64()
        crypto_currency = reader.read_string() if (flags & (1 << 0)) else None
        crypto_amount = reader.read_int64() if (flags & (1 << 0)) else None
        transaction_id = reader.read_string() if (flags & (1 << 1)) else None
        return cls(currency=currency, amount=amount, stars=stars, crypto_currency=crypto_currency, crypto_amount=crypto_amount, transaction_id=transaction_id)


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
        writer.write_string(self.transaction_id or '')
        if self.boost_peer is not None and hasattr(self.boost_peer, 'write'): self.boost_peer.write(writer)
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

    def __init__(self, name_hidden: bool = False, saved: bool = False, converted: bool = False, upgraded: bool = False, refunded: bool = False, can_upgrade: bool = False, prepaid_upgrade: bool = False, upgrade_separate: bool = False, auction_acquired: bool = False, message: Any = None, convert_stars: Any = None, upgrade_msg_id: Any = None, upgrade_stars: Any = None, from_id: Any = None, peer: Any = None, saved_id: Any = None, prepaid_upgrade_hash: Any = None, gift_msg_id: Any = None, to_id: Any = None, gift_num: Any = None, gift: Any = None) -> None:
        self.name_hidden = name_hidden
        self.saved = saved
        self.converted = converted
        self.upgraded = upgraded
        self.refunded = refunded
        self.can_upgrade = can_upgrade
        self.prepaid_upgrade = prepaid_upgrade
        self.upgrade_separate = upgrade_separate
        self.auction_acquired = auction_acquired
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
        self.gift = gift

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
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        if self.convert_stars is not None:
            writer.write_int64(self.convert_stars or 0)
        if self.upgrade_msg_id is not None:
            writer.write_int32(self.upgrade_msg_id or 0)
        if self.upgrade_stars is not None:
            writer.write_int64(self.upgrade_stars or 0)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.saved_id is not None:
            writer.write_int64(self.saved_id or 0)
        if self.prepaid_upgrade_hash is not None:
            writer.write_string(self.prepaid_upgrade_hash or '')
        if self.gift_msg_id is not None:
            writer.write_int32(self.gift_msg_id or 0)
        if self.to_id is not None:
            if self.to_id is not None and hasattr(self.to_id, 'write'): self.to_id.write(writer)
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
        message = reader.read_object() if (flags & (1 << 1)) else None
        convert_stars = reader.read_int64() if (flags & (1 << 4)) else None
        upgrade_msg_id = reader.read_int32() if (flags & (1 << 5)) else None
        upgrade_stars = reader.read_int64() if (flags & (1 << 8)) else None
        from_id = reader.read_object() if (flags & (1 << 11)) else None
        peer = reader.read_object() if (flags & (1 << 12)) else None
        saved_id = reader.read_int64() if (flags & (1 << 12)) else None
        prepaid_upgrade_hash = reader.read_string() if (flags & (1 << 14)) else None
        gift_msg_id = reader.read_int32() if (flags & (1 << 15)) else None
        to_id = reader.read_object() if (flags & (1 << 18)) else None
        gift_num = reader.read_int32() if (flags & (1 << 19)) else None
        return cls(name_hidden=name_hidden, saved=saved, converted=converted, upgraded=upgraded, refunded=refunded, can_upgrade=can_upgrade, prepaid_upgrade=prepaid_upgrade, upgrade_separate=upgrade_separate, auction_acquired=auction_acquired, gift=gift, message=message, convert_stars=convert_stars, upgrade_msg_id=upgrade_msg_id, upgrade_stars=upgrade_stars, from_id=from_id, peer=peer, saved_id=saved_id, prepaid_upgrade_hash=prepaid_upgrade_hash, gift_msg_id=gift_msg_id, to_id=to_id, gift_num=gift_num)


@register_tl
class MessageActionStarGiftUnique(TLObject):
    ID: int = 0xe6c31522

    def __init__(self, upgrade: bool = False, transferred: bool = False, saved: bool = False, refunded: bool = False, prepaid_upgrade: bool = False, assigned: bool = False, from_offer: bool = False, craft: bool = False, can_export_at: Any = None, transfer_stars: Any = None, from_id: Any = None, peer: Any = None, saved_id: Any = None, resale_amount: Any = None, can_transfer_at: Any = None, can_resell_at: Any = None, drop_original_details_stars: Any = None, can_craft_at: Any = None, gift: Any = None) -> None:
        self.upgrade = upgrade
        self.transferred = transferred
        self.saved = saved
        self.refunded = refunded
        self.prepaid_upgrade = prepaid_upgrade
        self.assigned = assigned
        self.from_offer = from_offer
        self.craft = craft
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
        self.gift = gift

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
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        if self.can_export_at is not None:
            writer.write_int32(self.can_export_at or 0)
        if self.transfer_stars is not None:
            writer.write_int64(self.transfer_stars or 0)
        if self.from_id is not None:
            if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.saved_id is not None:
            writer.write_int64(self.saved_id or 0)
        if self.resale_amount is not None:
            if self.resale_amount is not None and hasattr(self.resale_amount, 'write'): self.resale_amount.write(writer)
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
        can_export_at = reader.read_int32() if (flags & (1 << 3)) else None
        transfer_stars = reader.read_int64() if (flags & (1 << 4)) else None
        from_id = reader.read_object() if (flags & (1 << 6)) else None
        peer = reader.read_object() if (flags & (1 << 7)) else None
        saved_id = reader.read_int64() if (flags & (1 << 7)) else None
        resale_amount = reader.read_object() if (flags & (1 << 8)) else None
        can_transfer_at = reader.read_int32() if (flags & (1 << 9)) else None
        can_resell_at = reader.read_int32() if (flags & (1 << 10)) else None
        drop_original_details_stars = reader.read_int64() if (flags & (1 << 12)) else None
        can_craft_at = reader.read_int32() if (flags & (1 << 15)) else None
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

    def __init__(self, missed: bool = False, active: bool = False, video: bool = False, duration: Any = None, other_participants: Any = None, call_id: Any = None) -> None:
        self.missed = missed
        self.active = active
        self.video = video
        self.duration = duration
        self.other_participants = other_participants
        self.call_id = call_id

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
            writer.write_vector(self.other_participants or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionConferenceCall':
        flags = reader.read_uint32()
        missed = bool(flags & (1 << 0))
        active = bool(flags & (1 << 1))
        video = bool(flags & (1 << 4))
        call_id = reader.read_int64()
        duration = reader.read_int32() if (flags & (1 << 2)) else None
        other_participants = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        return cls(missed=missed, active=active, video=video, call_id=call_id, duration=duration, other_participants=other_participants)


@register_tl
class MessageActionTodoCompletions(TLObject):
    ID: int = 0xcc7c5c89

    def __init__(self, completed: Any = None, incompleted: Any = None) -> None:
        self.completed = completed
        self.incompleted = incompleted

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.completed or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.incompleted or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTodoCompletions':
        completed = reader.read_vector(lambda r: r.read_int32())
        incompleted = reader.read_vector(lambda r: r.read_int32())
        return cls(completed=completed, incompleted=incompleted)


@register_tl
class MessageActionTodoAppendTasks(TLObject):
    ID: int = 0xc7edbc83

    def __init__(self, list: Any = None) -> None:
        self.list = list

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.list or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTodoAppendTasks':
        list = reader.read_vector(lambda r: reader.read_object())
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
            writer.write_string(self.reject_comment or '')
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.price is not None:
            if self.price is not None and hasattr(self.price, 'write'): self.price.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestedPostApproval':
        flags = reader.read_uint32()
        rejected = bool(flags & (1 << 0))
        balance_too_low = bool(flags & (1 << 1))
        reject_comment = reader.read_string() if (flags & (1 << 2)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 3)) else None
        price = reader.read_object() if (flags & (1 << 4)) else None
        return cls(rejected=rejected, balance_too_low=balance_too_low, reject_comment=reject_comment, schedule_date=schedule_date, price=price)


@register_tl
class MessageActionSuggestedPostSuccess(TLObject):
    ID: int = 0x95ddcf69

    def __init__(self, price: Any = None) -> None:
        self.price = price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.price is not None and hasattr(self.price, 'write'): self.price.write(writer)

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

    def __init__(self, transaction_id: Any = None, currency: Any = None, amount: Any = None, crypto_currency: Any = None, crypto_amount: Any = None) -> None:
        self.transaction_id = transaction_id
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.transaction_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.currency or '')
        writer.write_int64(self.amount or 0)
        writer.write_string(self.crypto_currency or '')
        writer.write_int64(self.crypto_amount or 0)
        if self.transaction_id is not None:
            writer.write_string(self.transaction_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftTon':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        crypto_currency = reader.read_string()
        crypto_amount = reader.read_int64()
        transaction_id = reader.read_string() if (flags & (1 << 0)) else None
        return cls(currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, transaction_id=transaction_id)


@register_tl
class MessageActionSuggestBirthday(TLObject):
    ID: int = 0x2c8f2a25

    def __init__(self, birthday: Any = None) -> None:
        self.birthday = birthday

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.birthday is not None and hasattr(self.birthday, 'write'): self.birthday.write(writer)

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
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        if self.price is not None and hasattr(self.price, 'write'): self.price.write(writer)
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
        if self.gift is not None and hasattr(self.gift, 'write'): self.gift.write(writer)
        if self.price is not None and hasattr(self.price, 'write'): self.price.write(writer)

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
        if self.answer is not None and hasattr(self.answer, 'write'): self.answer.write(writer)

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
        if self.answer is not None and hasattr(self.answer, 'write'): self.answer.write(writer)

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

    def __init__(self, pinned: bool = False, unread_mark: bool = False, view_forum_as_messages: bool = False, pts: Any = None, draft: Any = None, folder_id: Any = None, ttl_period: Any = None, peer: Any = None, top_message: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, unread_mentions_count: Any = None, unread_reactions_count: Any = None, unread_poll_votes_count: Any = None, notify_settings: Any = None) -> None:
        self.pinned = pinned
        self.unread_mark = unread_mark
        self.view_forum_as_messages = view_forum_as_messages
        self.pts = pts
        self.draft = draft
        self.folder_id = folder_id
        self.ttl_period = ttl_period
        self.peer = peer
        self.top_message = top_message
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_reactions_count = unread_reactions_count
        self.unread_poll_votes_count = unread_poll_votes_count
        self.notify_settings = notify_settings

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
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.read_inbox_max_id or 0)
        writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        writer.write_int32(self.unread_mentions_count or 0)
        writer.write_int32(self.unread_reactions_count or 0)
        writer.write_int32(self.unread_poll_votes_count or 0)
        if self.notify_settings is not None and hasattr(self.notify_settings, 'write'): self.notify_settings.write(writer)
        if self.pts is not None:
            writer.write_int32(self.pts or 0)
        if self.draft is not None:
            if self.draft is not None and hasattr(self.draft, 'write'): self.draft.write(writer)
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
        pts = reader.read_int32() if (flags & (1 << 0)) else None
        draft = reader.read_object() if (flags & (1 << 1)) else None
        folder_id = reader.read_int32() if (flags & (1 << 4)) else None
        ttl_period = reader.read_int32() if (flags & (1 << 5)) else None
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
        if self.folder is not None and hasattr(self.folder, 'write'): self.folder.write(writer)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
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

    def __init__(self, has_stickers: bool = False, video_sizes: Any = None, id: Any = None, access_hash: Any = None, file_reference: Any = None, date: Any = None, sizes: Any = None, dc_id: Any = None) -> None:
        self.has_stickers = has_stickers
        self.video_sizes = video_sizes
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.date = date
        self.sizes = sizes
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
        writer.write_vector(self.sizes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.video_sizes is not None:
            writer.write_vector(self.video_sizes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.dc_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Photo':
        flags = reader.read_uint32()
        has_stickers = bool(flags & (1 << 0))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        date = reader.read_int32()
        sizes = reader.read_vector(lambda r: reader.read_object())
        video_sizes = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        dc_id = reader.read_int32()
        return cls(has_stickers=has_stickers, id=id, access_hash=access_hash, file_reference=file_reference, date=date, sizes=sizes, video_sizes=video_sizes, dc_id=dc_id)


@register_tl
class PhotoSizeEmpty(TLObject):
    ID: int = 0xe17e23c

    def __init__(self, type: Any = None) -> None:
        self.type = type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.type or '')

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
        writer.write_string(self.type or '')
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
        writer.write_string(self.type or '')
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
        writer.write_string(self.type or '')
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
        writer.write_string(self.type or '')
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_vector(self.sizes or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSizeProgressive':
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        sizes = reader.read_vector(lambda r: r.read_int32())
        return cls(type=type, w=w, h=h, sizes=sizes)


@register_tl
class PhotoPathSize(TLObject):
    ID: int = 0xd8214d41

    def __init__(self, type: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.type or '')
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

    def __init__(self, accuracy_radius: Any = None, long: Any = None, lat: Any = None, access_hash: Any = None) -> None:
        self.accuracy_radius = accuracy_radius
        self.long = long
        self.lat = lat
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accuracy_radius is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_double(self.long or 0.0)
        writer.write_double(self.lat or 0.0)
        writer.write_int64(self.access_hash or 0)
        if self.accuracy_radius is not None:
            writer.write_int32(self.accuracy_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GeoPoint':
        flags = reader.read_uint32()
        long = reader.read_double()
        lat = reader.read_double()
        access_hash = reader.read_int64()
        accuracy_radius = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(long=long, lat=lat, access_hash=access_hash, accuracy_radius=accuracy_radius)


@register_tl
class AuthSentCode(TLObject):
    ID: int = 0x5e002502

    def __init__(self, next_type: Any = None, timeout: Any = None, type: Any = None, phone_code_hash: Any = None) -> None:
        self.next_type = next_type
        self.timeout = timeout
        self.type = type
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_type is not None:
            flags |= (1 << 1)
        if self.timeout is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.type is not None and hasattr(self.type, 'write'): self.type.write(writer)
        writer.write_string(self.phone_code_hash or '')
        if self.next_type is not None:
            if self.next_type is not None and hasattr(self.next_type, 'write'): self.next_type.write(writer)
        if self.timeout is not None:
            writer.write_int32(self.timeout or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCode':
        flags = reader.read_uint32()
        type = reader.read_object()
        phone_code_hash = reader.read_string()
        next_type = reader.read_object() if (flags & (1 << 1)) else None
        timeout = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)


@register_tl
class AuthSentCodeSuccess(TLObject):
    ID: int = 0x2390fe44

    def __init__(self, authorization: Any = None) -> None:
        self.authorization = authorization

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.authorization is not None and hasattr(self.authorization, 'write'): self.authorization.write(writer)

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
        writer.write_string(self.store_product or '')
        writer.write_string(self.phone_code_hash or '')
        writer.write_string(self.support_email_address or '')
        writer.write_string(self.support_email_subject or '')
        writer.write_int32(self.premium_days or 0)
        writer.write_string(self.currency or '')
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
        if self.user is not None and hasattr(self.user, 'write'): self.user.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthAuthorization':
        flags = reader.read_uint32()
        setup_password_required = bool(flags & (1 << 1))
        otherwise_relogin_days = reader.read_int32() if (flags & (1 << 1)) else None
        tmp_sessions = reader.read_int32() if (flags & (1 << 0)) else None
        future_auth_token = reader.read_bytes() if (flags & (1 << 2)) else None
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
            if self.terms_of_service is not None and hasattr(self.terms_of_service, 'write'): self.terms_of_service.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthAuthorizationSignUpRequired':
        flags = reader.read_uint32()
        terms_of_service = reader.read_object() if (flags & (1 << 0)) else None
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
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

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

