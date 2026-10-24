from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class InputNotifyForumTopic(TLObject):
    ID: int = 0x5c467992

    def __init__(self, peer: Any = None, top_msg_id: Any = None) -> None:
        self.peer = peer
        self.top_msg_id = top_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
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
            if self.sound is not None and hasattr(self.sound, 'write'): self.sound.write(writer)
        if self.stories_muted is not None:
            writer.write_bool(bool(self.stories_muted))
        if self.stories_hide_sender is not None:
            writer.write_bool(bool(self.stories_hide_sender))
        if self.stories_sound is not None:
            if self.stories_sound is not None and hasattr(self.stories_sound, 'write'): self.stories_sound.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerNotifySettings':
        flags = reader.read_uint32()
        show_previews = reader.read_bool() if (flags & (1 << 0)) else None
        silent = reader.read_bool() if (flags & (1 << 1)) else None
        mute_until = reader.read_int32() if (flags & (1 << 2)) else None
        sound = reader.read_object() if (flags & (1 << 3)) else None
        stories_muted = reader.read_bool() if (flags & (1 << 6)) else None
        stories_hide_sender = reader.read_bool() if (flags & (1 << 7)) else None
        stories_sound = reader.read_object() if (flags & (1 << 8)) else None
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
            if self.ios_sound is not None and hasattr(self.ios_sound, 'write'): self.ios_sound.write(writer)
        if self.android_sound is not None:
            if self.android_sound is not None and hasattr(self.android_sound, 'write'): self.android_sound.write(writer)
        if self.other_sound is not None:
            if self.other_sound is not None and hasattr(self.other_sound, 'write'): self.other_sound.write(writer)
        if self.stories_muted is not None:
            writer.write_bool(bool(self.stories_muted))
        if self.stories_hide_sender is not None:
            writer.write_bool(bool(self.stories_hide_sender))
        if self.stories_ios_sound is not None:
            if self.stories_ios_sound is not None and hasattr(self.stories_ios_sound, 'write'): self.stories_ios_sound.write(writer)
        if self.stories_android_sound is not None:
            if self.stories_android_sound is not None and hasattr(self.stories_android_sound, 'write'): self.stories_android_sound.write(writer)
        if self.stories_other_sound is not None:
            if self.stories_other_sound is not None and hasattr(self.stories_other_sound, 'write'): self.stories_other_sound.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerNotifySettings':
        flags = reader.read_uint32()
        show_previews = reader.read_bool() if (flags & (1 << 0)) else None
        silent = reader.read_bool() if (flags & (1 << 1)) else None
        mute_until = reader.read_int32() if (flags & (1 << 2)) else None
        ios_sound = reader.read_object() if (flags & (1 << 3)) else None
        android_sound = reader.read_object() if (flags & (1 << 4)) else None
        other_sound = reader.read_object() if (flags & (1 << 5)) else None
        stories_muted = reader.read_bool() if (flags & (1 << 6)) else None
        stories_hide_sender = reader.read_bool() if (flags & (1 << 7)) else None
        stories_ios_sound = reader.read_object() if (flags & (1 << 8)) else None
        stories_android_sound = reader.read_object() if (flags & (1 << 9)) else None
        stories_other_sound = reader.read_object() if (flags & (1 << 10)) else None
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
            writer.write_string(self.request_chat_title or '')
        if self.request_chat_date is not None:
            writer.write_int32(self.request_chat_date or 0)
        if self.business_bot_id is not None:
            writer.write_int64(self.business_bot_id or 0)
        if self.business_bot_manage_url is not None:
            writer.write_string(self.business_bot_manage_url or '')
        if self.charge_paid_message_stars is not None:
            writer.write_int64(self.charge_paid_message_stars or 0)
        if self.registration_month is not None:
            writer.write_string(self.registration_month or '')
        if self.phone_country is not None:
            writer.write_string(self.phone_country or '')
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
        geo_distance = reader.read_int32() if (flags & (1 << 6)) else None
        request_chat_title = reader.read_string() if (flags & (1 << 9)) else None
        request_chat_date = reader.read_int32() if (flags & (1 << 9)) else None
        business_bot_id = reader.read_int64() if (flags & (1 << 13)) else None
        business_bot_manage_url = reader.read_string() if (flags & (1 << 13)) else None
        charge_paid_message_stars = reader.read_int64() if (flags & (1 << 14)) else None
        registration_month = reader.read_string() if (flags & (1 << 15)) else None
        phone_country = reader.read_string() if (flags & (1 << 16)) else None
        name_change_date = reader.read_int32() if (flags & (1 << 17)) else None
        photo_change_date = reader.read_int32() if (flags & (1 << 18)) else None
        return cls(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact, share_contact=share_contact, need_contacts_exception=need_contacts_exception, report_geo=report_geo, autoarchived=autoarchived, invite_members=invite_members, request_chat_broadcast=request_chat_broadcast, business_bot_paused=business_bot_paused, business_bot_can_reply=business_bot_can_reply, geo_distance=geo_distance, request_chat_title=request_chat_title, request_chat_date=request_chat_date, business_bot_id=business_bot_id, business_bot_manage_url=business_bot_manage_url, charge_paid_message_stars=charge_paid_message_stars, registration_month=registration_month, phone_country=phone_country, name_change_date=name_change_date, photo_change_date=photo_change_date)


@register_tl
class WallPaper(TLObject):
    ID: int = 0xa437c3ed

    def __init__(self, creator: bool = False, default: bool = False, pattern: bool = False, dark: bool = False, settings: Any = None, id: Any = None, access_hash: Any = None, slug: Any = None, document: Any = None) -> None:
        self.creator = creator
        self.default = default
        self.pattern = pattern
        self.dark = dark
        self.settings = settings
        self.id = id
        self.access_hash = access_hash
        self.slug = slug
        self.document = document

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
        writer.write_string(self.slug or '')
        if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.settings is not None:
            if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

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
        settings = reader.read_object() if (flags & (1 << 2)) else None
        return cls(id=id, creator=creator, default=default, pattern=pattern, dark=dark, access_hash=access_hash, slug=slug, document=document, settings=settings)


@register_tl
class WallPaperNoFile(TLObject):
    ID: int = 0xe0804116

    def __init__(self, default: bool = False, dark: bool = False, settings: Any = None, id: Any = None) -> None:
        self.default = default
        self.dark = dark
        self.settings = settings
        self.id = id

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
            if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'WallPaperNoFile':
        flags = reader.read_uint32()
        id = reader.read_int64()
        default = bool(flags & (1 << 1))
        dark = bool(flags & (1 << 4))
        settings = reader.read_object() if (flags & (1 << 2)) else None
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

    def __init__(self, blocked: bool = False, phone_calls_available: bool = False, phone_calls_private: bool = False, can_pin_message: bool = False, has_scheduled: bool = False, video_calls_available: bool = False, voice_messages_forbidden: bool = False, translations_disabled: bool = False, stories_pinned_available: bool = False, blocked_my_stories_from: bool = False, wallpaper_overridden: bool = False, contact_require_premium: bool = False, read_dates_private: bool = False, sponsored_enabled: bool = False, can_view_revenue: bool = False, bot_can_manage_emoji_status: bool = False, display_gifts_button: bool = False, noforwards_my_enabled: bool = False, noforwards_peer_enabled: bool = False, unofficial_security_risk: bool = False, about: Any = None, personal_photo: Any = None, profile_photo: Any = None, fallback_photo: Any = None, bot_info: Any = None, pinned_msg_id: Any = None, folder_id: Any = None, ttl_period: Any = None, theme: Any = None, private_forward_name: Any = None, bot_group_admin_rights: Any = None, bot_broadcast_admin_rights: Any = None, wallpaper: Any = None, stories: Any = None, business_work_hours: Any = None, business_location: Any = None, business_greeting_message: Any = None, business_away_message: Any = None, business_intro: Any = None, birthday: Any = None, personal_channel_id: Any = None, personal_channel_message: Any = None, stargifts_count: Any = None, starref_program: Any = None, bot_verification: Any = None, send_paid_messages_stars: Any = None, disallowed_gifts: Any = None, stars_rating: Any = None, stars_my_pending_rating: Any = None, stars_my_pending_rating_date: Any = None, main_tab: Any = None, saved_music: Any = None, note: Any = None, bot_manager_id: Any = None, id: Any = None, settings: Any = None, notify_settings: Any = None, common_chats_count: Any = None) -> None:
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
        self.about = about
        self.personal_photo = personal_photo
        self.profile_photo = profile_photo
        self.fallback_photo = fallback_photo
        self.bot_info = bot_info
        self.pinned_msg_id = pinned_msg_id
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
        self.id = id
        self.settings = settings
        self.notify_settings = notify_settings
        self.common_chats_count = common_chats_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        flags2 = 0
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
            flags2 |= (1 << 7)
        if self.can_view_revenue:
            flags2 |= (1 << 9)
        if self.bot_can_manage_emoji_status:
            flags2 |= (1 << 10)
        if self.display_gifts_button:
            flags2 |= (1 << 16)
        if self.noforwards_my_enabled:
            flags2 |= (1 << 23)
        if self.noforwards_peer_enabled:
            flags2 |= (1 << 24)
        if self.unofficial_security_risk:
            flags2 |= (1 << 26)
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
            flags2 |= (1 << 0)
        if self.business_location is not None:
            flags2 |= (1 << 1)
        if self.business_greeting_message is not None:
            flags2 |= (1 << 2)
        if self.business_away_message is not None:
            flags2 |= (1 << 3)
        if self.business_intro is not None:
            flags2 |= (1 << 4)
        if self.birthday is not None:
            flags2 |= (1 << 5)
        if self.personal_channel_id is not None:
            flags2 |= (1 << 6)
        if self.personal_channel_message is not None:
            flags2 |= (1 << 6)
        if self.stargifts_count is not None:
            flags2 |= (1 << 8)
        if self.starref_program is not None:
            flags2 |= (1 << 11)
        if self.bot_verification is not None:
            flags2 |= (1 << 12)
        if self.send_paid_messages_stars is not None:
            flags2 |= (1 << 14)
        if self.disallowed_gifts is not None:
            flags2 |= (1 << 15)
        if self.stars_rating is not None:
            flags2 |= (1 << 17)
        if self.stars_my_pending_rating is not None:
            flags2 |= (1 << 18)
        if self.stars_my_pending_rating_date is not None:
            flags2 |= (1 << 18)
        if self.main_tab is not None:
            flags2 |= (1 << 20)
        if self.saved_music is not None:
            flags2 |= (1 << 21)
        if self.note is not None:
            flags2 |= (1 << 22)
        if self.bot_manager_id is not None:
            flags2 |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_uint32(flags2)
        writer.write_int64(self.id or 0)
        if self.about is not None:
            writer.write_string(self.about or '')
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)
        if self.personal_photo is not None:
            if self.personal_photo is not None and hasattr(self.personal_photo, 'write'): self.personal_photo.write(writer)
        if self.profile_photo is not None:
            if self.profile_photo is not None and hasattr(self.profile_photo, 'write'): self.profile_photo.write(writer)
        if self.fallback_photo is not None:
            if self.fallback_photo is not None and hasattr(self.fallback_photo, 'write'): self.fallback_photo.write(writer)
        if self.notify_settings is not None and hasattr(self.notify_settings, 'write'): self.notify_settings.write(writer)
        if self.bot_info is not None:
            if self.bot_info is not None and hasattr(self.bot_info, 'write'): self.bot_info.write(writer)
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        writer.write_int32(self.common_chats_count or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.theme is not None:
            if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)
        if self.private_forward_name is not None:
            writer.write_string(self.private_forward_name or '')
        if self.bot_group_admin_rights is not None:
            if self.bot_group_admin_rights is not None and hasattr(self.bot_group_admin_rights, 'write'): self.bot_group_admin_rights.write(writer)
        if self.bot_broadcast_admin_rights is not None:
            if self.bot_broadcast_admin_rights is not None and hasattr(self.bot_broadcast_admin_rights, 'write'): self.bot_broadcast_admin_rights.write(writer)
        if self.wallpaper is not None:
            if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)
        if self.stories is not None:
            if self.stories is not None and hasattr(self.stories, 'write'): self.stories.write(writer)
        if self.business_work_hours is not None:
            if self.business_work_hours is not None and hasattr(self.business_work_hours, 'write'): self.business_work_hours.write(writer)
        if self.business_location is not None:
            if self.business_location is not None and hasattr(self.business_location, 'write'): self.business_location.write(writer)
        if self.business_greeting_message is not None:
            if self.business_greeting_message is not None and hasattr(self.business_greeting_message, 'write'): self.business_greeting_message.write(writer)
        if self.business_away_message is not None:
            if self.business_away_message is not None and hasattr(self.business_away_message, 'write'): self.business_away_message.write(writer)
        if self.business_intro is not None:
            if self.business_intro is not None and hasattr(self.business_intro, 'write'): self.business_intro.write(writer)
        if self.birthday is not None:
            if self.birthday is not None and hasattr(self.birthday, 'write'): self.birthday.write(writer)
        if self.personal_channel_id is not None:
            writer.write_int64(self.personal_channel_id or 0)
        if self.personal_channel_message is not None:
            writer.write_int32(self.personal_channel_message or 0)
        if self.stargifts_count is not None:
            writer.write_int32(self.stargifts_count or 0)
        if self.starref_program is not None:
            if self.starref_program is not None and hasattr(self.starref_program, 'write'): self.starref_program.write(writer)
        if self.bot_verification is not None:
            if self.bot_verification is not None and hasattr(self.bot_verification, 'write'): self.bot_verification.write(writer)
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.disallowed_gifts is not None:
            if self.disallowed_gifts is not None and hasattr(self.disallowed_gifts, 'write'): self.disallowed_gifts.write(writer)
        if self.stars_rating is not None:
            if self.stars_rating is not None and hasattr(self.stars_rating, 'write'): self.stars_rating.write(writer)
        if self.stars_my_pending_rating is not None:
            if self.stars_my_pending_rating is not None and hasattr(self.stars_my_pending_rating, 'write'): self.stars_my_pending_rating.write(writer)
        if self.stars_my_pending_rating_date is not None:
            writer.write_int32(self.stars_my_pending_rating_date or 0)
        if self.main_tab is not None:
            if self.main_tab is not None and hasattr(self.main_tab, 'write'): self.main_tab.write(writer)
        if self.saved_music is not None:
            if self.saved_music is not None and hasattr(self.saved_music, 'write'): self.saved_music.write(writer)
        if self.note is not None:
            if self.note is not None and hasattr(self.note, 'write'): self.note.write(writer)
        if self.bot_manager_id is not None:
            writer.write_int64(self.bot_manager_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserFull':
        flags = reader.read_uint32()
        flags2 = reader.read_uint32()
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
        sponsored_enabled = bool(flags2 & (1 << 7))
        can_view_revenue = bool(flags2 & (1 << 9))
        bot_can_manage_emoji_status = bool(flags2 & (1 << 10))
        display_gifts_button = bool(flags2 & (1 << 16))
        noforwards_my_enabled = bool(flags2 & (1 << 23))
        noforwards_peer_enabled = bool(flags2 & (1 << 24))
        unofficial_security_risk = bool(flags2 & (1 << 26))
        id = reader.read_int64()
        about = reader.read_string() if (flags & (1 << 1)) else None
        settings = reader.read_object()
        personal_photo = reader.read_object() if (flags & (1 << 21)) else None
        profile_photo = reader.read_object() if (flags & (1 << 2)) else None
        fallback_photo = reader.read_object() if (flags & (1 << 22)) else None
        notify_settings = reader.read_object()
        bot_info = reader.read_object() if (flags & (1 << 3)) else None
        pinned_msg_id = reader.read_int32() if (flags & (1 << 6)) else None
        common_chats_count = reader.read_int32()
        folder_id = reader.read_int32() if (flags & (1 << 11)) else None
        ttl_period = reader.read_int32() if (flags & (1 << 14)) else None
        theme = reader.read_object() if (flags & (1 << 15)) else None
        private_forward_name = reader.read_string() if (flags & (1 << 16)) else None
        bot_group_admin_rights = reader.read_object() if (flags & (1 << 17)) else None
        bot_broadcast_admin_rights = reader.read_object() if (flags & (1 << 18)) else None
        wallpaper = reader.read_object() if (flags & (1 << 24)) else None
        stories = reader.read_object() if (flags & (1 << 25)) else None
        business_work_hours = reader.read_object() if (flags2 & (1 << 0)) else None
        business_location = reader.read_object() if (flags2 & (1 << 1)) else None
        business_greeting_message = reader.read_object() if (flags2 & (1 << 2)) else None
        business_away_message = reader.read_object() if (flags2 & (1 << 3)) else None
        business_intro = reader.read_object() if (flags2 & (1 << 4)) else None
        birthday = reader.read_object() if (flags2 & (1 << 5)) else None
        personal_channel_id = reader.read_int64() if (flags2 & (1 << 6)) else None
        personal_channel_message = reader.read_int32() if (flags2 & (1 << 6)) else None
        stargifts_count = reader.read_int32() if (flags2 & (1 << 8)) else None
        starref_program = reader.read_object() if (flags2 & (1 << 11)) else None
        bot_verification = reader.read_object() if (flags2 & (1 << 12)) else None
        send_paid_messages_stars = reader.read_int64() if (flags2 & (1 << 14)) else None
        disallowed_gifts = reader.read_object() if (flags2 & (1 << 15)) else None
        stars_rating = reader.read_object() if (flags2 & (1 << 17)) else None
        stars_my_pending_rating = reader.read_object() if (flags2 & (1 << 18)) else None
        stars_my_pending_rating_date = reader.read_int32() if (flags2 & (1 << 18)) else None
        main_tab = reader.read_object() if (flags2 & (1 << 20)) else None
        saved_music = reader.read_object() if (flags2 & (1 << 21)) else None
        note = reader.read_object() if (flags2 & (1 << 22)) else None
        bot_manager_id = reader.read_int64() if (flags2 & (1 << 25)) else None
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
        if self.status is not None and hasattr(self.status, 'write'): self.status.write(writer)

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
        writer.write_vector(self.contacts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.saved_count or 0)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsContacts':
        contacts = reader.read_vector(lambda r: reader.read_object())
        saved_count = reader.read_int32()
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.imported or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.popular_invites or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.retry_contacts or [], lambda w, x: w.write_int64(x))
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsImportedContacts':
        imported = reader.read_vector(lambda r: reader.read_object())
        popular_invites = reader.read_vector(lambda r: reader.read_object())
        retry_contacts = reader.read_vector(lambda r: r.read_int64())
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.blocked or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlocked':
        blocked = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.blocked or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlockedSlice':
        count = reader.read_int32()
        blocked = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.dialogs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogs':
        dialogs = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.dialogs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogsSlice':
        count = reader.read_int32()
        dialogs = reader.read_vector(lambda r: reader.read_object())
        messages = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.topics or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessages':
        messages = reader.read_vector(lambda r: reader.read_object())
        topics = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(messages=messages, topics=topics, chats=chats, users=users)


@register_tl
class MessagesMessagesSlice(TLObject):
    ID: int = 0x5f206716

    def __init__(self, inexact: bool = False, next_rate: Any = None, offset_id_offset: Any = None, search_flood: Any = None, count: Any = None, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.inexact = inexact
        self.next_rate = next_rate
        self.offset_id_offset = offset_id_offset
        self.search_flood = search_flood
        self.count = count
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
            if self.search_flood is not None and hasattr(self.search_flood, 'write'): self.search_flood.write(writer)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.topics or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessagesSlice':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 1))
        count = reader.read_int32()
        next_rate = reader.read_int32() if (flags & (1 << 0)) else None
        offset_id_offset = reader.read_int32() if (flags & (1 << 2)) else None
        search_flood = reader.read_object() if (flags & (1 << 3)) else None
        messages = reader.read_vector(lambda r: reader.read_object())
        topics = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(inexact=inexact, count=count, next_rate=next_rate, offset_id_offset=offset_id_offset, search_flood=search_flood, messages=messages, topics=topics, chats=chats, users=users)


@register_tl
class MessagesChannelMessages(TLObject):
    ID: int = 0xc776ba4e

    def __init__(self, inexact: bool = False, offset_id_offset: Any = None, pts: Any = None, count: Any = None, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.inexact = inexact
        self.offset_id_offset = offset_id_offset
        self.pts = pts
        self.count = count
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
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.topics or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChannelMessages':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 1))
        pts = reader.read_int32()
        count = reader.read_int32()
        offset_id_offset = reader.read_int32() if (flags & (1 << 2)) else None
        messages = reader.read_vector(lambda r: reader.read_object())
        topics = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChats':
        chats = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatsSlice':
        count = reader.read_int32()
        chats = reader.read_vector(lambda r: reader.read_object())
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
        if self.full_chat is not None and hasattr(self.full_chat, 'write'): self.full_chat.write(writer)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatFull':
        full_chat = reader.read_object()
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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


@register_tl
class InputMessagesFilterChatPhotos(TLObject):
    ID: int = 0x3a20ecb8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterChatPhotos':
        return cls()


@register_tl
class InputMessagesFilterPhoneCalls(TLObject):
    ID: int = 0x80c99768

    def __init__(self, missed: bool = False) -> None:
        self.missed = missed

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.missed:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPhoneCalls':
        flags = reader.read_uint32()
        missed = bool(flags & (1 << 0))
        return cls(missed=missed)


@register_tl
class InputMessagesFilterRoundVoice(TLObject):
    ID: int = 0x7a7c17a4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterRoundVoice':
        return cls()


@register_tl
class InputMessagesFilterRoundVideo(TLObject):
    ID: int = 0xb549da53

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterRoundVideo':
        return cls()


@register_tl
class InputMessagesFilterMyMentions(TLObject):
    ID: int = 0xc1f8e69a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterMyMentions':
        return cls()


@register_tl
class InputMessagesFilterGeo(TLObject):
    ID: int = 0xe7026d0d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterGeo':
        return cls()


@register_tl
class InputMessagesFilterContacts(TLObject):
    ID: int = 0xe062db83

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterContacts':
        return cls()


@register_tl
class InputMessagesFilterPinned(TLObject):
    ID: int = 0x1bb00451

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPinned':
        return cls()


@register_tl
class InputMessagesFilterPoll(TLObject):
    ID: int = 0xfa2bc90a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPoll':
        return cls()


@register_tl
class UpdateNewMessage(TLObject):
    ID: int = 0x1f2b0afd

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)


@register_tl
class UpdateMessageID(TLObject):
    ID: int = 0x4e90bfd6

    def __init__(self, id: Any = None, random_id: Any = None) -> None:
        self.id = id
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.random_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessageID':
        id = reader.read_int32()
        random_id = reader.read_int64()
        return cls(id=id, random_id=random_id)


@register_tl
class UpdateDeleteMessages(TLObject):
    ID: int = 0xa20db0e5

    def __init__(self, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.messages or [], lambda w, x: w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteMessages':
        messages = reader.read_vector(lambda r: r.read_int32())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(messages=messages, pts=pts, pts_count=pts_count)


@register_tl
class UpdateUserTyping(TLObject):
    ID: int = 0x2a17bf5c

    def __init__(self, top_msg_id: Any = None, user_id: Any = None, action: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.user_id = user_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserTyping':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        action = reader.read_object()
        return cls(user_id=user_id, top_msg_id=top_msg_id, action=action)


@register_tl
class UpdateChatUserTyping(TLObject):
    ID: int = 0x83487af0

    def __init__(self, chat_id: Any = None, from_id: Any = None, action: Any = None) -> None:
        self.chat_id = chat_id
        self.from_id = from_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        if self.from_id is not None and hasattr(self.from_id, 'write'): self.from_id.write(writer)
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatUserTyping':
        chat_id = reader.read_int64()
        from_id = reader.read_object()
        action = reader.read_object()
        return cls(chat_id=chat_id, from_id=from_id, action=action)


@register_tl
class UpdateChatParticipants(TLObject):
    ID: int = 0x7761198

    def __init__(self, participants: Any = None) -> None:
        self.participants = participants

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.participants is not None and hasattr(self.participants, 'write'): self.participants.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipants':
        participants = reader.read_object()
        return cls(participants=participants)


@register_tl
class UpdateUserStatus(TLObject):
    ID: int = 0xe5bdf8de

    def __init__(self, user_id: Any = None, status: Any = None) -> None:
        self.user_id = user_id
        self.status = status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        if self.status is not None and hasattr(self.status, 'write'): self.status.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserStatus':
        user_id = reader.read_int64()
        status = reader.read_object()
        return cls(user_id=user_id, status=status)


@register_tl
class UpdateUserName(TLObject):
    ID: int = 0xa7848924

    def __init__(self, user_id: Any = None, first_name: Any = None, last_name: Any = None, usernames: Any = None) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.usernames = usernames

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_vector(self.usernames or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserName':
        user_id = reader.read_int64()
        first_name = reader.read_string()
        last_name = reader.read_string()
        usernames = reader.read_vector(lambda r: reader.read_object())
        return cls(user_id=user_id, first_name=first_name, last_name=last_name, usernames=usernames)


@register_tl
class UpdateNewAuthorization(TLObject):
    ID: int = 0x8951abef

    def __init__(self, unconfirmed: bool = False, date: Any = None, device: Any = None, location: Any = None, hash: Any = None) -> None:
        self.unconfirmed = unconfirmed
        self.date = date
        self.device = device
        self.location = location
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unconfirmed:
            flags |= (1 << 0)
        if self.date is not None:
            flags |= (1 << 0)
        if self.device is not None:
            flags |= (1 << 0)
        if self.location is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)
        if self.date is not None:
            writer.write_int32(self.date or 0)
        if self.device is not None:
            writer.write_string(self.device or '')
        if self.location is not None:
            writer.write_string(self.location or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewAuthorization':
        flags = reader.read_uint32()
        unconfirmed = bool(flags & (1 << 0))
        hash = reader.read_int64()
        date = reader.read_int32() if (flags & (1 << 0)) else None
        device = reader.read_string() if (flags & (1 << 0)) else None
        location = reader.read_string() if (flags & (1 << 0)) else None
        return cls(unconfirmed=unconfirmed, hash=hash, date=date, device=device, location=location)


@register_tl
class UpdateNewEncryptedMessage(TLObject):
    ID: int = 0x12bcbd9a

    def __init__(self, message: Any = None, qts: Any = None) -> None:
        self.message = message
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewEncryptedMessage':
        message = reader.read_object()
        qts = reader.read_int32()
        return cls(message=message, qts=qts)


@register_tl
class UpdateEncryptedChatTyping(TLObject):
    ID: int = 0x1710f156

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryptedChatTyping':
        chat_id = reader.read_int32()
        return cls(chat_id=chat_id)


@register_tl
class UpdateEncryption(TLObject):
    ID: int = 0xb4a2e88d

    def __init__(self, chat: Any = None, date: Any = None) -> None:
        self.chat = chat
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chat is not None and hasattr(self.chat, 'write'): self.chat.write(writer)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryption':
        chat = reader.read_object()
        date = reader.read_int32()
        return cls(chat=chat, date=date)


@register_tl
class UpdateEncryptedMessagesRead(TLObject):
    ID: int = 0x38fe25b7

    def __init__(self, chat_id: Any = None, max_date: Any = None, date: Any = None) -> None:
        self.chat_id = chat_id
        self.max_date = max_date
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.chat_id or 0)
        writer.write_int32(self.max_date or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryptedMessagesRead':
        chat_id = reader.read_int32()
        max_date = reader.read_int32()
        date = reader.read_int32()
        return cls(chat_id=chat_id, max_date=max_date, date=date)


@register_tl
class UpdateChatParticipantAdd(TLObject):
    ID: int = 0x3dda5451

    def __init__(self, chat_id: Any = None, user_id: Any = None, inviter_id: Any = None, date: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantAdd':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, inviter_id=inviter_id, date=date, version=version)


@register_tl
class UpdateChatParticipantDelete(TLObject):
    ID: int = 0xe32f3d77

    def __init__(self, chat_id: Any = None, user_id: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantDelete':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, version=version)


@register_tl
class UpdateDcOptions(TLObject):
    ID: int = 0x8e5e9873

    def __init__(self, dc_options: Any = None) -> None:
        self.dc_options = dc_options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dc_options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDcOptions':
        dc_options = reader.read_vector(lambda r: reader.read_object())
        return cls(dc_options=dc_options)


@register_tl
class UpdateNotifySettings(TLObject):
    ID: int = 0xbec268ef

    def __init__(self, peer: Any = None, notify_settings: Any = None) -> None:
        self.peer = peer
        self.notify_settings = notify_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.notify_settings is not None and hasattr(self.notify_settings, 'write'): self.notify_settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNotifySettings':
        peer = reader.read_object()
        notify_settings = reader.read_object()
        return cls(peer=peer, notify_settings=notify_settings)


@register_tl
class UpdateServiceNotification(TLObject):
    ID: int = 0xebe46819

    def __init__(self, popup: bool = False, invert_media: bool = False, inbox_date: Any = None, type: Any = None, message: Any = None, media: Any = None, entities: Any = None) -> None:
        self.popup = popup
        self.invert_media = invert_media
        self.inbox_date = inbox_date
        self.type = type
        self.message = message
        self.media = media
        self.entities = entities

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.popup:
            flags |= (1 << 0)
        if self.invert_media:
            flags |= (1 << 2)
        if self.inbox_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.inbox_date is not None:
            writer.write_int32(self.inbox_date or 0)
        writer.write_string(self.type or '')
        writer.write_string(self.message or '')
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateServiceNotification':
        flags = reader.read_uint32()
        popup = bool(flags & (1 << 0))
        invert_media = bool(flags & (1 << 2))
        inbox_date = reader.read_int32() if (flags & (1 << 1)) else None
        type = reader.read_string()
        message = reader.read_string()
        media = reader.read_object()
        entities = reader.read_vector(lambda r: reader.read_object())
        return cls(popup=popup, invert_media=invert_media, inbox_date=inbox_date, type=type, message=message, media=media, entities=entities)


@register_tl
class UpdatePrivacy(TLObject):
    ID: int = 0xee3b272a

    def __init__(self, key: Any = None, rules: Any = None) -> None:
        self.key = key
        self.rules = rules

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.key is not None and hasattr(self.key, 'write'): self.key.write(writer)
        writer.write_vector(self.rules or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePrivacy':
        key = reader.read_object()
        rules = reader.read_vector(lambda r: reader.read_object())
        return cls(key=key, rules=rules)


@register_tl
class UpdateUserPhone(TLObject):
    ID: int = 0x5492a13

    def __init__(self, user_id: Any = None, phone: Any = None) -> None:
        self.user_id = user_id
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(self.phone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserPhone':
        user_id = reader.read_int64()
        phone = reader.read_string()
        return cls(user_id=user_id, phone=phone)


@register_tl
class UpdateReadHistoryInbox(TLObject):
    ID: int = 0x9e84bc99

    def __init__(self, folder_id: Any = None, top_msg_id: Any = None, peer: Any = None, max_id: Any = None, still_unread_count: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.folder_id = folder_id
        self.top_msg_id = top_msg_id
        self.peer = peer
        self.max_id = max_id
        self.still_unread_count = still_unread_count
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 0)
        if self.top_msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.still_unread_count or 0)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadHistoryInbox':
        flags = reader.read_uint32()
        folder_id = reader.read_int32() if (flags & (1 << 0)) else None
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 1)) else None
        max_id = reader.read_int32()
        still_unread_count = reader.read_int32()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(folder_id=folder_id, peer=peer, top_msg_id=top_msg_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts, pts_count=pts_count)


@register_tl
class UpdateReadHistoryOutbox(TLObject):
    ID: int = 0x2f2f21bf

    def __init__(self, peer: Any = None, max_id: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.peer = peer
        self.max_id = max_id
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadHistoryOutbox':
        peer = reader.read_object()
        max_id = reader.read_int32()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(peer=peer, max_id=max_id, pts=pts, pts_count=pts_count)


@register_tl
class UpdateWebPage(TLObject):
    ID: int = 0x7f891213

    def __init__(self, webpage: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.webpage is not None and hasattr(self.webpage, 'write'): self.webpage.write(writer)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateWebPage':
        webpage = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(webpage=webpage, pts=pts, pts_count=pts_count)


@register_tl
class UpdateReadMessagesContents(TLObject):
    ID: int = 0xf8227181

    def __init__(self, date: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.date = date
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.date is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.messages or [], lambda w, x: w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        if self.date is not None:
            writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadMessagesContents':
        flags = reader.read_uint32()
        messages = reader.read_vector(lambda r: r.read_int32())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        date = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(messages=messages, pts=pts, pts_count=pts_count, date=date)


@register_tl
class UpdateChannelTooLong(TLObject):
    ID: int = 0x108d941f

    def __init__(self, pts: Any = None, channel_id: Any = None) -> None:
        self.pts = pts
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pts is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.pts is not None:
            writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelTooLong':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        pts = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(channel_id=channel_id, pts=pts)


@register_tl
class UpdateChannel(TLObject):
    ID: int = 0x635b4c09

    def __init__(self, channel_id: Any = None) -> None:
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannel':
        channel_id = reader.read_int64()
        return cls(channel_id=channel_id)


@register_tl
class UpdateNewChannelMessage(TLObject):
    ID: int = 0x62ba04d9

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewChannelMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)


@register_tl
class UpdateReadChannelInbox(TLObject):
    ID: int = 0x922e6e10

    def __init__(self, folder_id: Any = None, channel_id: Any = None, max_id: Any = None, still_unread_count: Any = None, pts: Any = None) -> None:
        self.folder_id = folder_id
        self.channel_id = channel_id
        self.max_id = max_id
        self.still_unread_count = still_unread_count
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.still_unread_count or 0)
        writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelInbox':
        flags = reader.read_uint32()
        folder_id = reader.read_int32() if (flags & (1 << 0)) else None
        channel_id = reader.read_int64()
        max_id = reader.read_int32()
        still_unread_count = reader.read_int32()
        pts = reader.read_int32()
        return cls(folder_id=folder_id, channel_id=channel_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts)


@register_tl
class UpdateDeleteChannelMessages(TLObject):
    ID: int = 0xc32d5b12

    def __init__(self, channel_id: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.channel_id = channel_id
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteChannelMessages':
        channel_id = reader.read_int64()
        messages = reader.read_vector(lambda r: r.read_int32())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count)


@register_tl
class UpdateChannelMessageViews(TLObject):
    ID: int = 0xf226ac08

    def __init__(self, channel_id: Any = None, id: Any = None, views: Any = None) -> None:
        self.channel_id = channel_id
        self.id = id
        self.views = views

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.views or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelMessageViews':
        channel_id = reader.read_int64()
        id = reader.read_int32()
        views = reader.read_int32()
        return cls(channel_id=channel_id, id=id, views=views)


@register_tl
class UpdateChatParticipantAdmin(TLObject):
    ID: int = 0xd7ca61a2

    def __init__(self, chat_id: Any = None, user_id: Any = None, is_admin: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bool(bool(self.is_admin))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantAdmin':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        is_admin = reader.read_bool()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, is_admin=is_admin, version=version)


@register_tl
class UpdateNewStickerSet(TLObject):
    ID: int = 0x688a30aa

    def __init__(self, stickerset: Any = None) -> None:
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewStickerSet':
        stickerset = reader.read_object()
        return cls(stickerset=stickerset)


@register_tl
class UpdateStickerSetsOrder(TLObject):
    ID: int = 0xbb2d201

    def __init__(self, masks: bool = False, emojis: bool = False, order: Any = None) -> None:
        self.masks = masks
        self.emojis = emojis
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_vector(self.order or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStickerSetsOrder':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        order = reader.read_vector(lambda r: r.read_int64())
        return cls(masks=masks, emojis=emojis, order=order)


@register_tl
class UpdateStickerSets(TLObject):
    ID: int = 0x31c24808

    def __init__(self, masks: bool = False, emojis: bool = False) -> None:
        self.masks = masks
        self.emojis = emojis

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStickerSets':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        return cls(masks=masks, emojis=emojis)


@register_tl
class UpdateSavedGifs(TLObject):
    ID: int = 0x9375341e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSavedGifs':
        return cls()


@register_tl
class UpdateBotInlineQuery(TLObject):
    ID: int = 0x496f379c

    def __init__(self, geo: Any = None, peer_type: Any = None, query_id: Any = None, user_id: Any = None, query: Any = None, offset: Any = None) -> None:
        self.geo = geo
        self.peer_type = peer_type
        self.query_id = query_id
        self.user_id = user_id
        self.query = query
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo is not None:
            flags |= (1 << 0)
        if self.peer_type is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(self.query or '')
        if self.geo is not None:
            if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        if self.peer_type is not None:
            if self.peer_type is not None and hasattr(self.peer_type, 'write'): self.peer_type.write(writer)
        writer.write_string(self.offset or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotInlineQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        query = reader.read_string()
        geo = reader.read_object() if (flags & (1 << 0)) else None
        peer_type = reader.read_object() if (flags & (1 << 1)) else None
        offset = reader.read_string()
        return cls(query_id=query_id, user_id=user_id, query=query, geo=geo, peer_type=peer_type, offset=offset)


@register_tl
class UpdateBotInlineSend(TLObject):
    ID: int = 0x12f12a07

    def __init__(self, geo: Any = None, msg_id: Any = None, user_id: Any = None, query: Any = None, id: Any = None) -> None:
        self.geo = geo
        self.msg_id = msg_id
        self.user_id = user_id
        self.query = query
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo is not None:
            flags |= (1 << 0)
        if self.msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_string(self.query or '')
        if self.geo is not None:
            if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        writer.write_string(self.id or '')
        if self.msg_id is not None:
            if self.msg_id is not None and hasattr(self.msg_id, 'write'): self.msg_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotInlineSend':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        query = reader.read_string()
        geo = reader.read_object() if (flags & (1 << 0)) else None
        id = reader.read_string()
        msg_id = reader.read_object() if (flags & (1 << 1)) else None
        return cls(user_id=user_id, query=query, geo=geo, id=id, msg_id=msg_id)


@register_tl
class UpdateEditChannelMessage(TLObject):
    ID: int = 0x1b3f4df7

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEditChannelMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)


@register_tl
class UpdateBotCallbackQuery(TLObject):
    ID: int = 0xb9cfc48d

    def __init__(self, data: Any = None, game_short_name: Any = None, query_id: Any = None, user_id: Any = None, peer: Any = None, msg_id: Any = None, chat_instance: Any = None) -> None:
        self.data = data
        self.game_short_name = game_short_name
        self.query_id = query_id
        self.user_id = user_id
        self.peer = peer
        self.msg_id = msg_id
        self.chat_instance = chat_instance

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.game_short_name is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.chat_instance or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')
        if self.game_short_name is not None:
            writer.write_string(self.game_short_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotCallbackQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        peer = reader.read_object()
        msg_id = reader.read_int32()
        chat_instance = reader.read_int64()
        data = reader.read_bytes() if (flags & (1 << 0)) else None
        game_short_name = reader.read_string() if (flags & (1 << 1)) else None
        return cls(query_id=query_id, user_id=user_id, peer=peer, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)


@register_tl
class UpdateEditMessage(TLObject):
    ID: int = 0xe40370a3

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEditMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)


@register_tl
class UpdateInlineBotCallbackQuery(TLObject):
    ID: int = 0x691e9052

    def __init__(self, data: Any = None, game_short_name: Any = None, query_id: Any = None, user_id: Any = None, msg_id: Any = None, chat_instance: Any = None) -> None:
        self.data = data
        self.game_short_name = game_short_name
        self.query_id = query_id
        self.user_id = user_id
        self.msg_id = msg_id
        self.chat_instance = chat_instance

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.game_short_name is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        if self.msg_id is not None and hasattr(self.msg_id, 'write'): self.msg_id.write(writer)
        writer.write_int64(self.chat_instance or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')
        if self.game_short_name is not None:
            writer.write_string(self.game_short_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateInlineBotCallbackQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        msg_id = reader.read_object()
        chat_instance = reader.read_int64()
        data = reader.read_bytes() if (flags & (1 << 0)) else None
        game_short_name = reader.read_string() if (flags & (1 << 1)) else None
        return cls(query_id=query_id, user_id=user_id, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)


@register_tl
class UpdateReadChannelOutbox(TLObject):
    ID: int = 0xb75f99a9

    def __init__(self, channel_id: Any = None, max_id: Any = None) -> None:
        self.channel_id = channel_id
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelOutbox':
        channel_id = reader.read_int64()
        max_id = reader.read_int32()
        return cls(channel_id=channel_id, max_id=max_id)


@register_tl
class UpdateDraftMessage(TLObject):
    ID: int = 0xedfc111e

    def __init__(self, top_msg_id: Any = None, saved_peer_id: Any = None, peer: Any = None, draft: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.peer = peer
        self.draft = draft

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        if self.draft is not None and hasattr(self.draft, 'write'): self.draft.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDraftMessage':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        saved_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        draft = reader.read_object()
        return cls(peer=peer, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, draft=draft)


@register_tl
class UpdateReadFeaturedStickers(TLObject):
    ID: int = 0x571d2742

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadFeaturedStickers':
        return cls()


@register_tl
class UpdateRecentStickers(TLObject):
    ID: int = 0x9a422c20

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateRecentStickers':
        return cls()


@register_tl
class UpdateConfig(TLObject):
    ID: int = 0xa229dd06

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateConfig':
        return cls()


@register_tl
class UpdatePtsChanged(TLObject):
    ID: int = 0x3354678f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePtsChanged':
        return cls()


@register_tl
class UpdateChannelWebPage(TLObject):
    ID: int = 0x2f2ba99f

    def __init__(self, channel_id: Any = None, webpage: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.channel_id = channel_id
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        if self.webpage is not None and hasattr(self.webpage, 'write'): self.webpage.write(writer)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelWebPage':
        channel_id = reader.read_int64()
        webpage = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(channel_id=channel_id, webpage=webpage, pts=pts, pts_count=pts_count)


@register_tl
class UpdateDialogPinned(TLObject):
    ID: int = 0x6e6fe51c

    def __init__(self, pinned: bool = False, folder_id: Any = None, peer: Any = None) -> None:
        self.pinned = pinned
        self.folder_id = folder_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        if self.folder_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogPinned':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        folder_id = reader.read_int32() if (flags & (1 << 1)) else None
        peer = reader.read_object()
        return cls(pinned=pinned, folder_id=folder_id, peer=peer)


@register_tl
class UpdatePinnedDialogs(TLObject):
    ID: int = 0xfa0f3ca2

    def __init__(self, folder_id: Any = None, order: Any = None) -> None:
        self.folder_id = folder_id
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 1)
        if self.order is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.order is not None:
            writer.write_vector(self.order or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedDialogs':
        flags = reader.read_uint32()
        folder_id = reader.read_int32() if (flags & (1 << 1)) else None
        order = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        return cls(folder_id=folder_id, order=order)


@register_tl
class UpdateBotWebhookJSON(TLObject):
    ID: int = 0x8317c0c3

    def __init__(self, data: Any = None) -> None:
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.data is not None and hasattr(self.data, 'write'): self.data.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotWebhookJSON':
        data = reader.read_object()
        return cls(data=data)


@register_tl
class UpdateBotWebhookJSONQuery(TLObject):
    ID: int = 0x9b9240a6

    def __init__(self, query_id: Any = None, data: Any = None, timeout: Any = None) -> None:
        self.query_id = query_id
        self.data = data
        self.timeout = timeout

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        if self.data is not None and hasattr(self.data, 'write'): self.data.write(writer)
        writer.write_int32(self.timeout or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotWebhookJSONQuery':
        query_id = reader.read_int64()
        data = reader.read_object()
        timeout = reader.read_int32()
        return cls(query_id=query_id, data=data, timeout=timeout)


@register_tl
class UpdateBotShippingQuery(TLObject):
    ID: int = 0xb5aefd7d

    def __init__(self, query_id: Any = None, user_id: Any = None, payload: Any = None, shipping_address: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.payload = payload
        self.shipping_address = shipping_address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bytes(self.payload or b'')
        if self.shipping_address is not None and hasattr(self.shipping_address, 'write'): self.shipping_address.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotShippingQuery':
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        payload = reader.read_bytes()
        shipping_address = reader.read_object()
        return cls(query_id=query_id, user_id=user_id, payload=payload, shipping_address=shipping_address)


@register_tl
class UpdateBotPrecheckoutQuery(TLObject):
    ID: int = 0x8caa9a96

    def __init__(self, info: Any = None, shipping_option_id: Any = None, query_id: Any = None, user_id: Any = None, payload: Any = None, currency: Any = None, total_amount: Any = None) -> None:
        self.info = info
        self.shipping_option_id = shipping_option_id
        self.query_id = query_id
        self.user_id = user_id
        self.payload = payload
        self.currency = currency
        self.total_amount = total_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.info is not None:
            flags |= (1 << 0)
        if self.shipping_option_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bytes(self.payload or b'')
        if self.info is not None:
            if self.info is not None and hasattr(self.info, 'write'): self.info.write(writer)
        if self.shipping_option_id is not None:
            writer.write_string(self.shipping_option_id or '')
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotPrecheckoutQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        payload = reader.read_bytes()
        info = reader.read_object() if (flags & (1 << 0)) else None
        shipping_option_id = reader.read_string() if (flags & (1 << 1)) else None
        currency = reader.read_string()
        total_amount = reader.read_int64()
        return cls(query_id=query_id, user_id=user_id, payload=payload, info=info, shipping_option_id=shipping_option_id, currency=currency, total_amount=total_amount)


@register_tl
class UpdatePhoneCall(TLObject):
    ID: int = 0xab0f6b1e

    def __init__(self, phone_call: Any = None) -> None:
        self.phone_call = phone_call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.phone_call is not None and hasattr(self.phone_call, 'write'): self.phone_call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePhoneCall':
        phone_call = reader.read_object()
        return cls(phone_call=phone_call)


@register_tl
class UpdateLangPackTooLong(TLObject):
    ID: int = 0x46560264

    def __init__(self, lang_code: Any = None) -> None:
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLangPackTooLong':
        lang_code = reader.read_string()
        return cls(lang_code=lang_code)


@register_tl
class UpdateLangPack(TLObject):
    ID: int = 0x56022f4d

    def __init__(self, difference: Any = None) -> None:
        self.difference = difference

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.difference is not None and hasattr(self.difference, 'write'): self.difference.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLangPack':
        difference = reader.read_object()
        return cls(difference=difference)


@register_tl
class UpdateFavedStickers(TLObject):
    ID: int = 0xe511996d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateFavedStickers':
        return cls()


@register_tl
class UpdateChannelReadMessagesContents(TLObject):
    ID: int = 0x25f324f7

    def __init__(self, top_msg_id: Any = None, saved_peer_id: Any = None, channel_id: Any = None, messages: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.channel_id = channel_id
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)
        writer.write_vector(self.messages or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelReadMessagesContents':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        saved_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        messages = reader.read_vector(lambda r: r.read_int32())
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, messages=messages)


@register_tl
class UpdateContactsReset(TLObject):
    ID: int = 0x7084a7be

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateContactsReset':
        return cls()


@register_tl
class UpdateChannelAvailableMessages(TLObject):
    ID: int = 0xb23fc698

    def __init__(self, channel_id: Any = None, available_min_id: Any = None) -> None:
        self.channel_id = channel_id
        self.available_min_id = available_min_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.available_min_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelAvailableMessages':
        channel_id = reader.read_int64()
        available_min_id = reader.read_int32()
        return cls(channel_id=channel_id, available_min_id=available_min_id)


@register_tl
class UpdateDialogUnreadMark(TLObject):
    ID: int = 0xb658f23e

    def __init__(self, unread: bool = False, saved_peer_id: Any = None, peer: Any = None) -> None:
        self.unread = unread
        self.saved_peer_id = saved_peer_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unread:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.saved_peer_id is not None:
            if self.saved_peer_id is not None and hasattr(self.saved_peer_id, 'write'): self.saved_peer_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogUnreadMark':
        flags = reader.read_uint32()
        unread = bool(flags & (1 << 0))
        peer = reader.read_object()
        saved_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        return cls(unread=unread, peer=peer, saved_peer_id=saved_peer_id)


@register_tl
class UpdateMessagePoll(TLObject):
    ID: int = 0xd64c522b

    def __init__(self, peer: Any = None, msg_id: Any = None, top_msg_id: Any = None, poll: Any = None, poll_id: Any = None, results: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.top_msg_id = top_msg_id
        self.poll = poll
        self.poll_id = poll_id
        self.results = results

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer is not None:
            flags |= (1 << 1)
        if self.msg_id is not None:
            flags |= (1 << 1)
        if self.top_msg_id is not None:
            flags |= (1 << 2)
        if self.poll is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int64(self.poll_id or 0)
        if self.poll is not None:
            if self.poll is not None and hasattr(self.poll, 'write'): self.poll.write(writer)
        if self.results is not None and hasattr(self.results, 'write'): self.results.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessagePoll':
        flags = reader.read_uint32()
        peer = reader.read_object() if (flags & (1 << 1)) else None
        msg_id = reader.read_int32() if (flags & (1 << 1)) else None
        top_msg_id = reader.read_int32() if (flags & (1 << 2)) else None
        poll_id = reader.read_int64()
        poll = reader.read_object() if (flags & (1 << 0)) else None
        results = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, top_msg_id=top_msg_id, poll_id=poll_id, poll=poll, results=results)


@register_tl
class UpdateChatDefaultBannedRights(TLObject):
    ID: int = 0x54c01850

    def __init__(self, peer: Any = None, default_banned_rights: Any = None, version: Any = None) -> None:
        self.peer = peer
        self.default_banned_rights = default_banned_rights
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.default_banned_rights is not None and hasattr(self.default_banned_rights, 'write'): self.default_banned_rights.write(writer)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatDefaultBannedRights':
        peer = reader.read_object()
        default_banned_rights = reader.read_object()
        version = reader.read_int32()
        return cls(peer=peer, default_banned_rights=default_banned_rights, version=version)


@register_tl
class UpdateFolderPeers(TLObject):
    ID: int = 0x19360dc0

    def __init__(self, folder_peers: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.folder_peers = folder_peers
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.folder_peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateFolderPeers':
        folder_peers = reader.read_vector(lambda r: reader.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(folder_peers=folder_peers, pts=pts, pts_count=pts_count)


@register_tl
class UpdatePeerSettings(TLObject):
    ID: int = 0x6a7e7366

    def __init__(self, peer: Any = None, settings: Any = None) -> None:
        self.peer = peer
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerSettings':
        peer = reader.read_object()
        settings = reader.read_object()
        return cls(peer=peer, settings=settings)


@register_tl
class UpdatePeerLocated(TLObject):
    ID: int = 0xb4afcfb0

    def __init__(self, peers: Any = None) -> None:
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.peers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerLocated':
        peers = reader.read_vector(lambda r: reader.read_object())
        return cls(peers=peers)


@register_tl
class UpdateNewScheduledMessage(TLObject):
    ID: int = 0x39a51dfb

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewScheduledMessage':
        message = reader.read_object()
        return cls(message=message)


@register_tl
class UpdateDeleteScheduledMessages(TLObject):
    ID: int = 0xf2a71983

    def __init__(self, sent_messages: Any = None, peer: Any = None, messages: Any = None) -> None:
        self.sent_messages = sent_messages
        self.peer = peer
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sent_messages is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.messages or [], lambda w, x: w.write_int32(x))
        if self.sent_messages is not None:
            writer.write_vector(self.sent_messages or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteScheduledMessages':
        flags = reader.read_uint32()
        peer = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_int32())
        sent_messages = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        return cls(peer=peer, messages=messages, sent_messages=sent_messages)


@register_tl
class UpdateTheme(TLObject):
    ID: int = 0x8216fba3

    def __init__(self, theme: Any = None) -> None:
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateTheme':
        theme = reader.read_object()
        return cls(theme=theme)


@register_tl
class UpdateGeoLiveViewed(TLObject):
    ID: int = 0x871fb939

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGeoLiveViewed':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)


@register_tl
class UpdateLoginToken(TLObject):
    ID: int = 0x564fe691

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLoginToken':
        return cls()


@register_tl
class UpdateMessagePollVote(TLObject):
    ID: int = 0x7699f014

    def __init__(self, poll_id: Any = None, peer: Any = None, options: Any = None, positions: Any = None, qts: Any = None) -> None:
        self.poll_id = poll_id
        self.peer = peer
        self.options = options
        self.positions = positions
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.poll_id or 0)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.positions or [], lambda w, x: w.write_int32(x))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessagePollVote':
        poll_id = reader.read_int64()
        peer = reader.read_object()
        options = reader.read_vector(lambda r: reader.read_object())
        positions = reader.read_vector(lambda r: r.read_int32())
        qts = reader.read_int32()
        return cls(poll_id=poll_id, peer=peer, options=options, positions=positions, qts=qts)


@register_tl
class UpdateDialogFilter(TLObject):
    ID: int = 0x26ffde7d

    def __init__(self, filter: Any = None, id: Any = None) -> None:
        self.filter = filter
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.filter is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.filter is not None:
            if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilter':
        flags = reader.read_uint32()
        id = reader.read_int32()
        filter = reader.read_object() if (flags & (1 << 0)) else None
        return cls(id=id, filter=filter)


@register_tl
class UpdateDialogFilterOrder(TLObject):
    ID: int = 0xa5d72105

    def __init__(self, order: Any = None) -> None:
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.order or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilterOrder':
        order = reader.read_vector(lambda r: r.read_int32())
        return cls(order=order)


@register_tl
class UpdateDialogFilters(TLObject):
    ID: int = 0x3504914f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilters':
        return cls()


@register_tl
class UpdatePhoneCallSignalingData(TLObject):
    ID: int = 0x2661bf09

    def __init__(self, phone_call_id: Any = None, data: Any = None) -> None:
        self.phone_call_id = phone_call_id
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.phone_call_id or 0)
        writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePhoneCallSignalingData':
        phone_call_id = reader.read_int64()
        data = reader.read_bytes()
        return cls(phone_call_id=phone_call_id, data=data)

