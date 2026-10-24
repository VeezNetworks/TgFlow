from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl

@register_tl
class ChannelFull(TLObject):
    ID: int = 0xe4e0b29d

    def __init__(self, can_view_participants: bool = False, can_set_username: bool = False, can_set_stickers: bool = False, hidden_prehistory: bool = False, can_set_location: bool = False, has_scheduled: bool = False, can_view_stats: bool = False, blocked: bool = False, can_delete_channel: bool = False, antispam: bool = False, participants_hidden: bool = False, translations_disabled: bool = False, stories_pinned_available: bool = False, view_forum_as_messages: bool = False, restricted_sponsored: bool = False, can_view_revenue: bool = False, paid_media_allowed: bool = False, can_view_stars_revenue: bool = False, paid_reactions_available: bool = False, stargifts_available: bool = False, paid_messages_available: bool = False, id: Any = None, about: Any = None, participants_count: Any = None, admins_count: Any = None, kicked_count: Any = None, banned_count: Any = None, online_count: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, chat_photo: Any = None, notify_settings: Any = None, exported_invite: Any = None, bot_info: Any = None, migrated_from_chat_id: Any = None, migrated_from_max_id: Any = None, pinned_msg_id: Any = None, stickerset: Any = None, available_min_id: Any = None, folder_id: Any = None, linked_chat_id: Any = None, location: Any = None, slowmode_seconds: Any = None, slowmode_next_send_date: Any = None, stats_dc: Any = None, pts: Any = None, call: Any = None, ttl_period: Any = None, pending_suggestions: Any = None, groupcall_default_join_as: Any = None, theme_emoticon: Any = None, requests_pending: Any = None, recent_requesters: Any = None, default_send_as: Any = None, available_reactions: Any = None, reactions_limit: Any = None, stories: Any = None, wallpaper: Any = None, boosts_applied: Any = None, boosts_unrestrict: Any = None, emojiset: Any = None, bot_verification: Any = None, stargifts_count: Any = None, send_paid_messages_stars: Any = None, main_tab: Any = None) -> None:
        self.can_view_participants = can_view_participants
        self.can_set_username = can_set_username
        self.can_set_stickers = can_set_stickers
        self.hidden_prehistory = hidden_prehistory
        self.can_set_location = can_set_location
        self.has_scheduled = has_scheduled
        self.can_view_stats = can_view_stats
        self.blocked = blocked
        self.can_delete_channel = can_delete_channel
        self.antispam = antispam
        self.participants_hidden = participants_hidden
        self.translations_disabled = translations_disabled
        self.stories_pinned_available = stories_pinned_available
        self.view_forum_as_messages = view_forum_as_messages
        self.restricted_sponsored = restricted_sponsored
        self.can_view_revenue = can_view_revenue
        self.paid_media_allowed = paid_media_allowed
        self.can_view_stars_revenue = can_view_stars_revenue
        self.paid_reactions_available = paid_reactions_available
        self.stargifts_available = stargifts_available
        self.paid_messages_available = paid_messages_available
        self.id = id
        self.about = about
        self.participants_count = participants_count
        self.admins_count = admins_count
        self.kicked_count = kicked_count
        self.banned_count = banned_count
        self.online_count = online_count
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
        self.exported_invite = exported_invite
        self.bot_info = bot_info
        self.migrated_from_chat_id = migrated_from_chat_id
        self.migrated_from_max_id = migrated_from_max_id
        self.pinned_msg_id = pinned_msg_id
        self.stickerset = stickerset
        self.available_min_id = available_min_id
        self.folder_id = folder_id
        self.linked_chat_id = linked_chat_id
        self.location = location
        self.slowmode_seconds = slowmode_seconds
        self.slowmode_next_send_date = slowmode_next_send_date
        self.stats_dc = stats_dc
        self.pts = pts
        self.call = call
        self.ttl_period = ttl_period
        self.pending_suggestions = pending_suggestions
        self.groupcall_default_join_as = groupcall_default_join_as
        self.theme_emoticon = theme_emoticon
        self.requests_pending = requests_pending
        self.recent_requesters = recent_requesters
        self.default_send_as = default_send_as
        self.available_reactions = available_reactions
        self.reactions_limit = reactions_limit
        self.stories = stories
        self.wallpaper = wallpaper
        self.boosts_applied = boosts_applied
        self.boosts_unrestrict = boosts_unrestrict
        self.emojiset = emojiset
        self.bot_verification = bot_verification
        self.stargifts_count = stargifts_count
        self.send_paid_messages_stars = send_paid_messages_stars
        self.main_tab = main_tab

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_view_participants:
            flags |= (1 << 3)
        if self.can_set_username:
            flags |= (1 << 6)
        if self.can_set_stickers:
            flags |= (1 << 7)
        if self.hidden_prehistory:
            flags |= (1 << 10)
        if self.can_set_location:
            flags |= (1 << 16)
        if self.has_scheduled:
            flags |= (1 << 19)
        if self.can_view_stats:
            flags |= (1 << 20)
        if self.blocked:
            flags |= (1 << 22)
        if self.can_delete_channel:
            flags |= (1 << 0)
        if self.antispam:
            flags |= (1 << 1)
        if self.participants_hidden:
            flags |= (1 << 2)
        if self.translations_disabled:
            flags |= (1 << 3)
        if self.stories_pinned_available:
            flags |= (1 << 5)
        if self.view_forum_as_messages:
            flags |= (1 << 6)
        if self.restricted_sponsored:
            flags |= (1 << 11)
        if self.can_view_revenue:
            flags |= (1 << 12)
        if self.paid_media_allowed:
            flags |= (1 << 14)
        if self.can_view_stars_revenue:
            flags |= (1 << 15)
        if self.paid_reactions_available:
            flags |= (1 << 16)
        if self.stargifts_available:
            flags |= (1 << 19)
        if self.paid_messages_available:
            flags |= (1 << 20)
        if self.participants_count is not None:
            flags |= (1 << 0)
        if self.admins_count is not None:
            flags |= (1 << 1)
        if self.kicked_count is not None:
            flags |= (1 << 2)
        if self.banned_count is not None:
            flags |= (1 << 2)
        if self.online_count is not None:
            flags |= (1 << 13)
        if self.exported_invite is not None:
            flags |= (1 << 23)
        if self.migrated_from_chat_id is not None:
            flags |= (1 << 4)
        if self.migrated_from_max_id is not None:
            flags |= (1 << 4)
        if self.pinned_msg_id is not None:
            flags |= (1 << 5)
        if self.stickerset is not None:
            flags |= (1 << 8)
        if self.available_min_id is not None:
            flags |= (1 << 9)
        if self.folder_id is not None:
            flags |= (1 << 11)
        if self.linked_chat_id is not None:
            flags |= (1 << 14)
        if self.location is not None:
            flags |= (1 << 15)
        if self.slowmode_seconds is not None:
            flags |= (1 << 17)
        if self.slowmode_next_send_date is not None:
            flags |= (1 << 18)
        if self.stats_dc is not None:
            flags |= (1 << 12)
        if self.call is not None:
            flags |= (1 << 21)
        if self.ttl_period is not None:
            flags |= (1 << 24)
        if self.pending_suggestions is not None:
            flags |= (1 << 25)
        if self.groupcall_default_join_as is not None:
            flags |= (1 << 26)
        if self.theme_emoticon is not None:
            flags |= (1 << 27)
        if self.requests_pending is not None:
            flags |= (1 << 28)
        if self.recent_requesters is not None:
            flags |= (1 << 28)
        if self.default_send_as is not None:
            flags |= (1 << 29)
        if self.available_reactions is not None:
            flags |= (1 << 30)
        if self.reactions_limit is not None:
            flags |= (1 << 13)
        if self.stories is not None:
            flags |= (1 << 4)
        if self.wallpaper is not None:
            flags |= (1 << 7)
        if self.boosts_applied is not None:
            flags |= (1 << 8)
        if self.boosts_unrestrict is not None:
            flags |= (1 << 9)
        if self.emojiset is not None:
            flags |= (1 << 10)
        if self.bot_verification is not None:
            flags |= (1 << 17)
        if self.stargifts_count is not None:
            flags |= (1 << 18)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 21)
        if self.main_tab is not None:
            flags |= (1 << 22)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(str(self.about or ''))
        if self.participants_count is not None:
            writer.write_int32(self.participants_count or 0)
        if self.admins_count is not None:
            writer.write_int32(self.admins_count or 0)
        if self.kicked_count is not None:
            writer.write_int32(self.kicked_count or 0)
        if self.banned_count is not None:
            writer.write_int32(self.banned_count or 0)
        if self.online_count is not None:
            writer.write_int32(self.online_count or 0)
        writer.write_int32(self.read_inbox_max_id or 0)
        writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        if hasattr(self.chat_photo, 'write'):
            self.chat_photo.write(writer)
        else:
            writer.write_bytes(self.chat_photo or b'')
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')
        if self.exported_invite is not None:
            if hasattr(self.exported_invite, 'write'):
                self.exported_invite.write(writer)
            else:
                writer.write_bytes(self.exported_invite or b'')
        writer.write_vector(self.bot_info or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.migrated_from_chat_id is not None:
            writer.write_int64(self.migrated_from_chat_id or 0)
        if self.migrated_from_max_id is not None:
            writer.write_int32(self.migrated_from_max_id or 0)
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        if self.stickerset is not None:
            if hasattr(self.stickerset, 'write'):
                self.stickerset.write(writer)
            else:
                writer.write_bytes(self.stickerset or b'')
        if self.available_min_id is not None:
            writer.write_int32(self.available_min_id or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.linked_chat_id is not None:
            writer.write_int64(self.linked_chat_id or 0)
        if self.location is not None:
            if hasattr(self.location, 'write'):
                self.location.write(writer)
            else:
                writer.write_bytes(self.location or b'')
        if self.slowmode_seconds is not None:
            writer.write_int32(self.slowmode_seconds or 0)
        if self.slowmode_next_send_date is not None:
            writer.write_int32(self.slowmode_next_send_date or 0)
        if self.stats_dc is not None:
            writer.write_int32(self.stats_dc or 0)
        writer.write_int32(self.pts or 0)
        if self.call is not None:
            if hasattr(self.call, 'write'):
                self.call.write(writer)
            else:
                writer.write_bytes(self.call or b'')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.pending_suggestions is not None:
            writer.write_vector(self.pending_suggestions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.groupcall_default_join_as is not None:
            if hasattr(self.groupcall_default_join_as, 'write'):
                self.groupcall_default_join_as.write(writer)
            else:
                writer.write_bytes(self.groupcall_default_join_as or b'')
        if self.theme_emoticon is not None:
            writer.write_string(str(self.theme_emoticon or ''))
        if self.requests_pending is not None:
            writer.write_int32(self.requests_pending or 0)
        if self.recent_requesters is not None:
            writer.write_vector(self.recent_requesters or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.default_send_as is not None:
            if hasattr(self.default_send_as, 'write'):
                self.default_send_as.write(writer)
            else:
                writer.write_bytes(self.default_send_as or b'')
        if self.available_reactions is not None:
            if hasattr(self.available_reactions, 'write'):
                self.available_reactions.write(writer)
            else:
                writer.write_bytes(self.available_reactions or b'')
        if self.reactions_limit is not None:
            writer.write_int32(self.reactions_limit or 0)
        if self.stories is not None:
            if hasattr(self.stories, 'write'):
                self.stories.write(writer)
            else:
                writer.write_bytes(self.stories or b'')
        if self.wallpaper is not None:
            if hasattr(self.wallpaper, 'write'):
                self.wallpaper.write(writer)
            else:
                writer.write_bytes(self.wallpaper or b'')
        if self.boosts_applied is not None:
            writer.write_int32(self.boosts_applied or 0)
        if self.boosts_unrestrict is not None:
            writer.write_int32(self.boosts_unrestrict or 0)
        if self.emojiset is not None:
            if hasattr(self.emojiset, 'write'):
                self.emojiset.write(writer)
            else:
                writer.write_bytes(self.emojiset or b'')
        if self.bot_verification is not None:
            if hasattr(self.bot_verification, 'write'):
                self.bot_verification.write(writer)
            else:
                writer.write_bytes(self.bot_verification or b'')
        if self.stargifts_count is not None:
            writer.write_int32(self.stargifts_count or 0)
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.main_tab is not None:
            if hasattr(self.main_tab, 'write'):
                self.main_tab.write(writer)
            else:
                writer.write_bytes(self.main_tab or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelFull':
        flags = reader.read_uint32()
        can_view_participants = bool(flags & (1 << 3))
        can_set_username = bool(flags & (1 << 6))
        can_set_stickers = bool(flags & (1 << 7))
        hidden_prehistory = bool(flags & (1 << 10))
        can_set_location = bool(flags & (1 << 16))
        has_scheduled = bool(flags & (1 << 19))
        can_view_stats = bool(flags & (1 << 20))
        blocked = bool(flags & (1 << 22))
        can_delete_channel = bool(flags & (1 << 0))
        antispam = bool(flags & (1 << 1))
        participants_hidden = bool(flags & (1 << 2))
        translations_disabled = bool(flags & (1 << 3))
        stories_pinned_available = bool(flags & (1 << 5))
        view_forum_as_messages = bool(flags & (1 << 6))
        restricted_sponsored = bool(flags & (1 << 11))
        can_view_revenue = bool(flags & (1 << 12))
        paid_media_allowed = bool(flags & (1 << 14))
        can_view_stars_revenue = bool(flags & (1 << 15))
        paid_reactions_available = bool(flags & (1 << 16))
        stargifts_available = bool(flags & (1 << 19))
        paid_messages_available = bool(flags & (1 << 20))
        id = reader.read_int64()
        about = reader.read_string()
        participants_count = None
        if flags & (1 << 0):
            participants_count = reader.read_int32()
        admins_count = None
        if flags & (1 << 1):
            admins_count = reader.read_int32()
        kicked_count = None
        if flags & (1 << 2):
            kicked_count = reader.read_int32()
        banned_count = None
        if flags & (1 << 2):
            banned_count = reader.read_int32()
        online_count = None
        if flags & (1 << 13):
            online_count = reader.read_int32()
        read_inbox_max_id = reader.read_int32()
        read_outbox_max_id = reader.read_int32()
        unread_count = reader.read_int32()
        chat_photo = reader.read_object()
        notify_settings = reader.read_object()
        exported_invite = None
        if flags & (1 << 23):
            exported_invite = reader.read_object()
        bot_info = reader.read_vector(lambda r: r.read_object())
        migrated_from_chat_id = None
        if flags & (1 << 4):
            migrated_from_chat_id = reader.read_int64()
        migrated_from_max_id = None
        if flags & (1 << 4):
            migrated_from_max_id = reader.read_int32()
        pinned_msg_id = None
        if flags & (1 << 5):
            pinned_msg_id = reader.read_int32()
        stickerset = None
        if flags & (1 << 8):
            stickerset = reader.read_object()
        available_min_id = None
        if flags & (1 << 9):
            available_min_id = reader.read_int32()
        folder_id = None
        if flags & (1 << 11):
            folder_id = reader.read_int32()
        linked_chat_id = None
        if flags & (1 << 14):
            linked_chat_id = reader.read_int64()
        location = None
        if flags & (1 << 15):
            location = reader.read_object()
        slowmode_seconds = None
        if flags & (1 << 17):
            slowmode_seconds = reader.read_int32()
        slowmode_next_send_date = None
        if flags & (1 << 18):
            slowmode_next_send_date = reader.read_int32()
        stats_dc = None
        if flags & (1 << 12):
            stats_dc = reader.read_int32()
        pts = reader.read_int32()
        call = None
        if flags & (1 << 21):
            call = reader.read_object()
        ttl_period = None
        if flags & (1 << 24):
            ttl_period = reader.read_int32()
        pending_suggestions = None
        if flags & (1 << 25):
            pending_suggestions = reader.read_vector(lambda r: r.read_object())
        groupcall_default_join_as = None
        if flags & (1 << 26):
            groupcall_default_join_as = reader.read_object()
        theme_emoticon = None
        if flags & (1 << 27):
            theme_emoticon = reader.read_string()
        requests_pending = None
        if flags & (1 << 28):
            requests_pending = reader.read_int32()
        recent_requesters = None
        if flags & (1 << 28):
            recent_requesters = reader.read_vector(lambda r: r.read_object())
        default_send_as = None
        if flags & (1 << 29):
            default_send_as = reader.read_object()
        available_reactions = None
        if flags & (1 << 30):
            available_reactions = reader.read_object()
        reactions_limit = None
        if flags & (1 << 13):
            reactions_limit = reader.read_int32()
        stories = None
        if flags & (1 << 4):
            stories = reader.read_object()
        wallpaper = None
        if flags & (1 << 7):
            wallpaper = reader.read_object()
        boosts_applied = None
        if flags & (1 << 8):
            boosts_applied = reader.read_int32()
        boosts_unrestrict = None
        if flags & (1 << 9):
            boosts_unrestrict = reader.read_int32()
        emojiset = None
        if flags & (1 << 10):
            emojiset = reader.read_object()
        bot_verification = None
        if flags & (1 << 17):
            bot_verification = reader.read_object()
        stargifts_count = None
        if flags & (1 << 18):
            stargifts_count = reader.read_int32()
        send_paid_messages_stars = None
        if flags & (1 << 21):
            send_paid_messages_stars = reader.read_int64()
        main_tab = None
        if flags & (1 << 22):
            main_tab = reader.read_object()
        return cls(can_view_participants=can_view_participants, can_set_username=can_set_username, can_set_stickers=can_set_stickers, hidden_prehistory=hidden_prehistory, can_set_location=can_set_location, has_scheduled=has_scheduled, can_view_stats=can_view_stats, blocked=blocked, can_delete_channel=can_delete_channel, antispam=antispam, participants_hidden=participants_hidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, view_forum_as_messages=view_forum_as_messages, restricted_sponsored=restricted_sponsored, can_view_revenue=can_view_revenue, paid_media_allowed=paid_media_allowed, can_view_stars_revenue=can_view_stars_revenue, paid_reactions_available=paid_reactions_available, stargifts_available=stargifts_available, paid_messages_available=paid_messages_available, id=id, about=about, participants_count=participants_count, admins_count=admins_count, kicked_count=kicked_count, banned_count=banned_count, online_count=online_count, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chat_photo=chat_photo, notify_settings=notify_settings, exported_invite=exported_invite, bot_info=bot_info, migrated_from_chat_id=migrated_from_chat_id, migrated_from_max_id=migrated_from_max_id, pinned_msg_id=pinned_msg_id, stickerset=stickerset, available_min_id=available_min_id, folder_id=folder_id, linked_chat_id=linked_chat_id, location=location, slowmode_seconds=slowmode_seconds, slowmode_next_send_date=slowmode_next_send_date, stats_dc=stats_dc, pts=pts, call=call, ttl_period=ttl_period, pending_suggestions=pending_suggestions, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, default_send_as=default_send_as, available_reactions=available_reactions, reactions_limit=reactions_limit, stories=stories, wallpaper=wallpaper, boosts_applied=boosts_applied, boosts_unrestrict=boosts_unrestrict, emojiset=emojiset, bot_verification=bot_verification, stargifts_count=stargifts_count, send_paid_messages_stars=send_paid_messages_stars, main_tab=main_tab)
@register_tl
class ChatParticipant(TLObject):
    ID: int = 0x38e79fde

    def __init__(self, user_id: Any = None, inviter_id: Any = None, date: Any = None, rank: Any = None) -> None:
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        if self.rank is not None:
            writer.write_string(str(self.rank or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipant':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        rank = None
        if flags & (1 << 0):
            rank = reader.read_string()
        return cls(user_id=user_id, inviter_id=inviter_id, date=date, rank=rank)
@register_tl
class ChatParticipantCreator(TLObject):
    ID: int = 0xe1f867b8

    def __init__(self, user_id: Any = None, rank: Any = None) -> None:
        self.user_id = user_id
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.rank is not None:
            writer.write_string(str(self.rank or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantCreator':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        rank = None
        if flags & (1 << 0):
            rank = reader.read_string()
        return cls(user_id=user_id, rank=rank)
@register_tl
class ChatParticipantAdmin(TLObject):
    ID: int = 0x360d5d2

    def __init__(self, user_id: Any = None, inviter_id: Any = None, date: Any = None, rank: Any = None) -> None:
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        if self.rank is not None:
            writer.write_string(str(self.rank or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantAdmin':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        rank = None
        if flags & (1 << 0):
            rank = reader.read_string()
        return cls(user_id=user_id, inviter_id=inviter_id, date=date, rank=rank)
@register_tl
class ChatParticipantsForbidden(TLObject):
    ID: int = 0x8763d3e1

    def __init__(self, chat_id: Any = None, self_participant: Any = None) -> None:
        self.chat_id = chat_id
        self.self_participant = self_participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.self_participant is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.chat_id or 0)
        if self.self_participant is not None:
            if hasattr(self.self_participant, 'write'):
                self.self_participant.write(writer)
            else:
                writer.write_bytes(self.self_participant or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantsForbidden':
        flags = reader.read_uint32()
        chat_id = reader.read_int64()
        self_participant = None
        if flags & (1 << 0):
            self_participant = reader.read_object()
        return cls(chat_id=chat_id, self_participant=self_participant)
@register_tl
class ChatParticipants(TLObject):
    ID: int = 0x3cbc93f8

    def __init__(self, chat_id: Any = None, participants: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.participants = participants
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_vector(self.participants or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipants':
        chat_id = reader.read_int64()
        participants = reader.read_vector(lambda r: r.read_object())
        version = reader.read_int32()
        return cls(chat_id=chat_id, participants=participants, version=version)
@register_tl
class ChatPhotoEmpty(TLObject):
    ID: int = 0x37c1011c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatPhotoEmpty':
        return cls()
@register_tl
class ChatPhoto(TLObject):
    ID: int = 0x1c6e1c11

    def __init__(self, has_video: bool = False, photo_id: Any = None, stripped_thumb: Any = None, dc_id: Any = None) -> None:
        self.has_video = has_video
        self.photo_id = photo_id
        self.stripped_thumb = stripped_thumb
        self.dc_id = dc_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_video:
            flags |= (1 << 0)
        if self.stripped_thumb is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.photo_id or 0)
        if self.stripped_thumb is not None:
            writer.write_bytes(self.stripped_thumb or b'')
        writer.write_int32(self.dc_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatPhoto':
        flags = reader.read_uint32()
        has_video = bool(flags & (1 << 0))
        photo_id = reader.read_int64()
        stripped_thumb = None
        if flags & (1 << 1):
            stripped_thumb = reader.read_bytes()
        dc_id = reader.read_int32()
        return cls(has_video=has_video, photo_id=photo_id, stripped_thumb=stripped_thumb, dc_id=dc_id)
@register_tl
class MessageEmpty(TLObject):
    ID: int = 0x90a6ca84

    def __init__(self, id: Any = None, peer_id: Any = None) -> None:
        self.id = id
        self.peer_id = peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.peer_id is not None:
            if hasattr(self.peer_id, 'write'):
                self.peer_id.write(writer)
            else:
                writer.write_bytes(self.peer_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEmpty':
        flags = reader.read_uint32()
        id = reader.read_int32()
        peer_id = None
        if flags & (1 << 0):
            peer_id = reader.read_object()
        return cls(id=id, peer_id=peer_id)
@register_tl
class Message(TLObject):
    ID: int = 0x95ef6f2b

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, silent: bool = False, post: bool = False, from_scheduled: bool = False, legacy: bool = False, edit_hide: bool = False, pinned: bool = False, noforwards: bool = False, invert_media: bool = False, offline: bool = False, video_processing_pending: bool = False, paid_suggested_post_stars: bool = False, paid_suggested_post_ton: bool = False, id: Any = None, from_id: Any = None, from_boosts_applied: Any = None, from_rank: Any = None, peer_id: Any = None, saved_peer_id: Any = None, fwd_from: Any = None, via_bot_id: Any = None, via_business_bot_id: Any = None, guestchat_via_from: Any = None, reply_to: Any = None, date: Any = None, message: Any = None, media: Any = None, reply_markup: Any = None, entities: Any = None, views: Any = None, forwards: Any = None, replies: Any = None, edit_date: Any = None, post_author: Any = None, grouped_id: Any = None, reactions: Any = None, restriction_reason: Any = None, ttl_period: Any = None, quick_reply_shortcut_id: Any = None, effect: Any = None, factcheck: Any = None, report_delivery_until_date: Any = None, paid_message_stars: Any = None, suggested_post: Any = None, schedule_repeat_period: Any = None, summary_from_language: Any = None) -> None:
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
        self.id = id
        self.from_id = from_id
        self.from_boosts_applied = from_boosts_applied
        self.from_rank = from_rank
        self.peer_id = peer_id
        self.saved_peer_id = saved_peer_id
        self.fwd_from = fwd_from
        self.via_bot_id = via_bot_id
        self.via_business_bot_id = via_business_bot_id
        self.guestchat_via_from = guestchat_via_from
        self.reply_to = reply_to
        self.date = date
        self.message = message
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

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
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
            flags |= (1 << 1)
        if self.video_processing_pending:
            flags |= (1 << 4)
        if self.paid_suggested_post_stars:
            flags |= (1 << 8)
        if self.paid_suggested_post_ton:
            flags |= (1 << 9)
        if self.from_id is not None:
            flags |= (1 << 8)
        if self.from_boosts_applied is not None:
            flags |= (1 << 29)
        if self.from_rank is not None:
            flags |= (1 << 12)
        if self.saved_peer_id is not None:
            flags |= (1 << 28)
        if self.fwd_from is not None:
            flags |= (1 << 2)
        if self.via_bot_id is not None:
            flags |= (1 << 11)
        if self.via_business_bot_id is not None:
            flags |= (1 << 0)
        if self.guestchat_via_from is not None:
            flags |= (1 << 19)
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
            flags |= (1 << 2)
        if self.factcheck is not None:
            flags |= (1 << 3)
        if self.report_delivery_until_date is not None:
            flags |= (1 << 5)
        if self.paid_message_stars is not None:
            flags |= (1 << 6)
        if self.suggested_post is not None:
            flags |= (1 << 7)
        if self.schedule_repeat_period is not None:
            flags |= (1 << 10)
        if self.summary_from_language is not None:
            flags |= (1 << 11)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.from_id is not None:
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if self.from_boosts_applied is not None:
            writer.write_int32(self.from_boosts_applied or 0)
        if self.from_rank is not None:
            writer.write_string(str(self.from_rank or ''))
        if hasattr(self.peer_id, 'write'):
            self.peer_id.write(writer)
        else:
            writer.write_bytes(self.peer_id or b'')
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if self.fwd_from is not None:
            if hasattr(self.fwd_from, 'write'):
                self.fwd_from.write(writer)
            else:
                writer.write_bytes(self.fwd_from or b'')
        if self.via_bot_id is not None:
            writer.write_int64(self.via_bot_id or 0)
        if self.via_business_bot_id is not None:
            writer.write_int64(self.via_business_bot_id or 0)
        if self.guestchat_via_from is not None:
            if hasattr(self.guestchat_via_from, 'write'):
                self.guestchat_via_from.write(writer)
            else:
                writer.write_bytes(self.guestchat_via_from or b'')
        if self.reply_to is not None:
            if hasattr(self.reply_to, 'write'):
                self.reply_to.write(writer)
            else:
                writer.write_bytes(self.reply_to or b'')
        writer.write_int32(self.date or 0)
        writer.write_string(str(self.message or ''))
        if self.media is not None:
            if hasattr(self.media, 'write'):
                self.media.write(writer)
            else:
                writer.write_bytes(self.media or b'')
        if self.reply_markup is not None:
            if hasattr(self.reply_markup, 'write'):
                self.reply_markup.write(writer)
            else:
                writer.write_bytes(self.reply_markup or b'')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.views is not None:
            writer.write_int32(self.views or 0)
        if self.forwards is not None:
            writer.write_int32(self.forwards or 0)
        if self.replies is not None:
            if hasattr(self.replies, 'write'):
                self.replies.write(writer)
            else:
                writer.write_bytes(self.replies or b'')
        if self.edit_date is not None:
            writer.write_int32(self.edit_date or 0)
        if self.post_author is not None:
            writer.write_string(str(self.post_author or ''))
        if self.grouped_id is not None:
            writer.write_int64(self.grouped_id or 0)
        if self.reactions is not None:
            if hasattr(self.reactions, 'write'):
                self.reactions.write(writer)
            else:
                writer.write_bytes(self.reactions or b'')
        if self.restriction_reason is not None:
            writer.write_vector(self.restriction_reason or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.quick_reply_shortcut_id is not None:
            writer.write_int32(self.quick_reply_shortcut_id or 0)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.factcheck is not None:
            if hasattr(self.factcheck, 'write'):
                self.factcheck.write(writer)
            else:
                writer.write_bytes(self.factcheck or b'')
        if self.report_delivery_until_date is not None:
            writer.write_int32(self.report_delivery_until_date or 0)
        if self.paid_message_stars is not None:
            writer.write_int64(self.paid_message_stars or 0)
        if self.suggested_post is not None:
            if hasattr(self.suggested_post, 'write'):
                self.suggested_post.write(writer)
            else:
                writer.write_bytes(self.suggested_post or b'')
        if self.schedule_repeat_period is not None:
            writer.write_int32(self.schedule_repeat_period or 0)
        if self.summary_from_language is not None:
            writer.write_string(str(self.summary_from_language or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'Message':
        flags = reader.read_uint32()
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
        offline = bool(flags & (1 << 1))
        video_processing_pending = bool(flags & (1 << 4))
        paid_suggested_post_stars = bool(flags & (1 << 8))
        paid_suggested_post_ton = bool(flags & (1 << 9))
        id = reader.read_int32()
        from_id = None
        if flags & (1 << 8):
            from_id = reader.read_object()
        from_boosts_applied = None
        if flags & (1 << 29):
            from_boosts_applied = reader.read_int32()
        from_rank = None
        if flags & (1 << 12):
            from_rank = reader.read_string()
        peer_id = reader.read_object()
        saved_peer_id = None
        if flags & (1 << 28):
            saved_peer_id = reader.read_object()
        fwd_from = None
        if flags & (1 << 2):
            fwd_from = reader.read_object()
        via_bot_id = None
        if flags & (1 << 11):
            via_bot_id = reader.read_int64()
        via_business_bot_id = None
        if flags & (1 << 0):
            via_business_bot_id = reader.read_int64()
        guestchat_via_from = None
        if flags & (1 << 19):
            guestchat_via_from = reader.read_object()
        reply_to = None
        if flags & (1 << 3):
            reply_to = reader.read_object()
        date = reader.read_int32()
        message = reader.read_string()
        media = None
        if flags & (1 << 9):
            media = reader.read_object()
        reply_markup = None
        if flags & (1 << 6):
            reply_markup = reader.read_object()
        entities = None
        if flags & (1 << 7):
            entities = reader.read_vector(lambda r: r.read_object())
        views = None
        if flags & (1 << 10):
            views = reader.read_int32()
        forwards = None
        if flags & (1 << 10):
            forwards = reader.read_int32()
        replies = None
        if flags & (1 << 23):
            replies = reader.read_object()
        edit_date = None
        if flags & (1 << 15):
            edit_date = reader.read_int32()
        post_author = None
        if flags & (1 << 16):
            post_author = reader.read_string()
        grouped_id = None
        if flags & (1 << 17):
            grouped_id = reader.read_int64()
        reactions = None
        if flags & (1 << 20):
            reactions = reader.read_object()
        restriction_reason = None
        if flags & (1 << 22):
            restriction_reason = reader.read_vector(lambda r: r.read_object())
        ttl_period = None
        if flags & (1 << 25):
            ttl_period = reader.read_int32()
        quick_reply_shortcut_id = None
        if flags & (1 << 30):
            quick_reply_shortcut_id = reader.read_int32()
        effect = None
        if flags & (1 << 2):
            effect = reader.read_int64()
        factcheck = None
        if flags & (1 << 3):
            factcheck = reader.read_object()
        report_delivery_until_date = None
        if flags & (1 << 5):
            report_delivery_until_date = reader.read_int32()
        paid_message_stars = None
        if flags & (1 << 6):
            paid_message_stars = reader.read_int64()
        suggested_post = None
        if flags & (1 << 7):
            suggested_post = reader.read_object()
        schedule_repeat_period = None
        if flags & (1 << 10):
            schedule_repeat_period = reader.read_int32()
        summary_from_language = None
        if flags & (1 << 11):
            summary_from_language = reader.read_string()
        return cls(out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, post=post, from_scheduled=from_scheduled, legacy=legacy, edit_hide=edit_hide, pinned=pinned, noforwards=noforwards, invert_media=invert_media, offline=offline, video_processing_pending=video_processing_pending, paid_suggested_post_stars=paid_suggested_post_stars, paid_suggested_post_ton=paid_suggested_post_ton, id=id, from_id=from_id, from_boosts_applied=from_boosts_applied, from_rank=from_rank, peer_id=peer_id, saved_peer_id=saved_peer_id, fwd_from=fwd_from, via_bot_id=via_bot_id, via_business_bot_id=via_business_bot_id, guestchat_via_from=guestchat_via_from, reply_to=reply_to, date=date, message=message, media=media, reply_markup=reply_markup, entities=entities, views=views, forwards=forwards, replies=replies, edit_date=edit_date, post_author=post_author, grouped_id=grouped_id, reactions=reactions, restriction_reason=restriction_reason, ttl_period=ttl_period, quick_reply_shortcut_id=quick_reply_shortcut_id, effect=effect, factcheck=factcheck, report_delivery_until_date=report_delivery_until_date, paid_message_stars=paid_message_stars, suggested_post=suggested_post, schedule_repeat_period=schedule_repeat_period, summary_from_language=summary_from_language)
@register_tl
class MessageService(TLObject):
    ID: int = 0x7a800e0a

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, reactions_are_possible: bool = False, silent: bool = False, post: bool = False, legacy: bool = False, id: Any = None, from_id: Any = None, peer_id: Any = None, saved_peer_id: Any = None, reply_to: Any = None, date: Any = None, action: Any = None, reactions: Any = None, ttl_period: Any = None) -> None:
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.reactions_are_possible = reactions_are_possible
        self.silent = silent
        self.post = post
        self.legacy = legacy
        self.id = id
        self.from_id = from_id
        self.peer_id = peer_id
        self.saved_peer_id = saved_peer_id
        self.reply_to = reply_to
        self.date = date
        self.action = action
        self.reactions = reactions
        self.ttl_period = ttl_period

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
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if hasattr(self.peer_id, 'write'):
            self.peer_id.write(writer)
        else:
            writer.write_bytes(self.peer_id or b'')
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if self.reply_to is not None:
            if hasattr(self.reply_to, 'write'):
                self.reply_to.write(writer)
            else:
                writer.write_bytes(self.reply_to or b'')
        writer.write_int32(self.date or 0)
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')
        if self.reactions is not None:
            if hasattr(self.reactions, 'write'):
                self.reactions.write(writer)
            else:
                writer.write_bytes(self.reactions or b'')
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
        from_id = None
        if flags & (1 << 8):
            from_id = reader.read_object()
        peer_id = reader.read_object()
        saved_peer_id = None
        if flags & (1 << 28):
            saved_peer_id = reader.read_object()
        reply_to = None
        if flags & (1 << 3):
            reply_to = reader.read_object()
        date = reader.read_int32()
        action = reader.read_object()
        reactions = None
        if flags & (1 << 20):
            reactions = reader.read_object()
        ttl_period = None
        if flags & (1 << 25):
            ttl_period = reader.read_int32()
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
            if hasattr(self.photo, 'write'):
                self.photo.write(writer)
            else:
                writer.write_bytes(self.photo or b'')
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video is not None:
            if hasattr(self.video, 'write'):
                self.video.write(writer)
            else:
                writer.write_bytes(self.video or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPhoto':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 3))
        live_photo = bool(flags & (1 << 4))
        photo = None
        if flags & (1 << 0):
            photo = reader.read_object()
        ttl_seconds = None
        if flags & (1 << 2):
            ttl_seconds = reader.read_int32()
        video = None
        if flags & (1 << 4):
            video = reader.read_object()
        return cls(spoiler=spoiler, live_photo=live_photo, photo=photo, ttl_seconds=ttl_seconds, video=video)
@register_tl
class MessageMediaGeo(TLObject):
    ID: int = 0x56e0d474

    def __init__(self, geo: Any = None) -> None:
        self.geo = geo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.geo, 'write'):
            self.geo.write(writer)
        else:
            writer.write_bytes(self.geo or b'')

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
        writer.write_string(str(self.phone_number or ''))
        writer.write_string(str(self.first_name or ''))
        writer.write_string(str(self.last_name or ''))
        writer.write_string(str(self.vcard or ''))
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
            if hasattr(self.document, 'write'):
                self.document.write(writer)
            else:
                writer.write_bytes(self.document or b'')
        if self.alt_documents is not None:
            writer.write_vector(self.alt_documents or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.video_cover is not None:
            if hasattr(self.video_cover, 'write'):
                self.video_cover.write(writer)
            else:
                writer.write_bytes(self.video_cover or b'')
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
        document = None
        if flags & (1 << 0):
            document = reader.read_object()
        alt_documents = None
        if flags & (1 << 5):
            alt_documents = reader.read_vector(lambda r: r.read_object())
        video_cover = None
        if flags & (1 << 9):
            video_cover = reader.read_object()
        video_timestamp = None
        if flags & (1 << 10):
            video_timestamp = reader.read_int32()
        ttl_seconds = None
        if flags & (1 << 2):
            ttl_seconds = reader.read_int32()
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
        if hasattr(self.webpage, 'write'):
            self.webpage.write(writer)
        else:
            writer.write_bytes(self.webpage or b'')

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
        if hasattr(self.geo, 'write'):
            self.geo.write(writer)
        else:
            writer.write_bytes(self.geo or b'')
        writer.write_string(str(self.title or ''))
        writer.write_string(str(self.address or ''))
        writer.write_string(str(self.provider or ''))
        writer.write_string(str(self.venue_id or ''))
        writer.write_string(str(self.venue_type or ''))

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
        if hasattr(self.game, 'write'):
            self.game.write(writer)
        else:
            writer.write_bytes(self.game or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGame':
        game = reader.read_object()
        return cls(game=game)
@register_tl
class MessageMediaInvoice(TLObject):
    ID: int = 0xf6a548d3

    def __init__(self, shipping_address_requested: bool = False, test: bool = False, title: Any = None, description: Any = None, photo: Any = None, receipt_msg_id: Any = None, currency: Any = None, total_amount: Any = None, start_param: Any = None, extended_media: Any = None) -> None:
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.title = title
        self.description = description
        self.photo = photo
        self.receipt_msg_id = receipt_msg_id
        self.currency = currency
        self.total_amount = total_amount
        self.start_param = start_param
        self.extended_media = extended_media

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
        writer.write_string(str(self.title or ''))
        writer.write_string(str(self.description or ''))
        if self.photo is not None:
            if hasattr(self.photo, 'write'):
                self.photo.write(writer)
            else:
                writer.write_bytes(self.photo or b'')
        if self.receipt_msg_id is not None:
            writer.write_int32(self.receipt_msg_id or 0)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        writer.write_string(str(self.start_param or ''))
        if self.extended_media is not None:
            if hasattr(self.extended_media, 'write'):
                self.extended_media.write(writer)
            else:
                writer.write_bytes(self.extended_media or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaInvoice':
        flags = reader.read_uint32()
        shipping_address_requested = bool(flags & (1 << 1))
        test = bool(flags & (1 << 3))
        title = reader.read_string()
        description = reader.read_string()
        photo = None
        if flags & (1 << 0):
            photo = reader.read_object()
        receipt_msg_id = None
        if flags & (1 << 2):
            receipt_msg_id = reader.read_int32()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        start_param = reader.read_string()
        extended_media = None
        if flags & (1 << 4):
            extended_media = reader.read_object()
        return cls(shipping_address_requested=shipping_address_requested, test=test, title=title, description=description, photo=photo, receipt_msg_id=receipt_msg_id, currency=currency, total_amount=total_amount, start_param=start_param, extended_media=extended_media)
@register_tl
class MessageMediaGeoLive(TLObject):
    ID: int = 0xb940c666

    def __init__(self, geo: Any = None, heading: Any = None, period: Any = None, proximity_notification_radius: Any = None) -> None:
        self.geo = geo
        self.heading = heading
        self.period = period
        self.proximity_notification_radius = proximity_notification_radius

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.heading is not None:
            flags |= (1 << 0)
        if self.proximity_notification_radius is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.geo, 'write'):
            self.geo.write(writer)
        else:
            writer.write_bytes(self.geo or b'')
        if self.heading is not None:
            writer.write_int32(self.heading or 0)
        writer.write_int32(self.period or 0)
        if self.proximity_notification_radius is not None:
            writer.write_int32(self.proximity_notification_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGeoLive':
        flags = reader.read_uint32()
        geo = reader.read_object()
        heading = None
        if flags & (1 << 0):
            heading = reader.read_int32()
        period = reader.read_int32()
        proximity_notification_radius = None
        if flags & (1 << 1):
            proximity_notification_radius = reader.read_int32()
        return cls(geo=geo, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius)
@register_tl
class MessageMediaPoll(TLObject):
    ID: int = 0x773f4e66

    def __init__(self, poll: Any = None, results: Any = None, attached_media: Any = None) -> None:
        self.poll = poll
        self.results = results
        self.attached_media = attached_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attached_media is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.poll, 'write'):
            self.poll.write(writer)
        else:
            writer.write_bytes(self.poll or b'')
        if hasattr(self.results, 'write'):
            self.results.write(writer)
        else:
            writer.write_bytes(self.results or b'')
        if self.attached_media is not None:
            if hasattr(self.attached_media, 'write'):
                self.attached_media.write(writer)
            else:
                writer.write_bytes(self.attached_media or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPoll':
        flags = reader.read_uint32()
        poll = reader.read_object()
        results = reader.read_object()
        attached_media = None
        if flags & (1 << 0):
            attached_media = reader.read_object()
        return cls(poll=poll, results=results, attached_media=attached_media)
@register_tl
class MessageMediaDice(TLObject):
    ID: int = 0x8cbec07

    def __init__(self, value: Any = None, emoticon: Any = None, game_outcome: Any = None) -> None:
        self.value = value
        self.emoticon = emoticon
        self.game_outcome = game_outcome

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.game_outcome is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.value or 0)
        writer.write_string(str(self.emoticon or ''))
        if self.game_outcome is not None:
            if hasattr(self.game_outcome, 'write'):
                self.game_outcome.write(writer)
            else:
                writer.write_bytes(self.game_outcome or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaDice':
        flags = reader.read_uint32()
        value = reader.read_int32()
        emoticon = reader.read_string()
        game_outcome = None
        if flags & (1 << 0):
            game_outcome = reader.read_object()
        return cls(value=value, emoticon=emoticon, game_outcome=game_outcome)
@register_tl
class MessageMediaStory(TLObject):
    ID: int = 0x68cb6283

    def __init__(self, via_mention: bool = False, peer: Any = None, id: Any = None, story: Any = None) -> None:
        self.via_mention = via_mention
        self.peer = peer
        self.id = id
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_mention:
            flags |= (1 << 1)
        if self.story is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.id or 0)
        if self.story is not None:
            if hasattr(self.story, 'write'):
                self.story.write(writer)
            else:
                writer.write_bytes(self.story or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaStory':
        flags = reader.read_uint32()
        via_mention = bool(flags & (1 << 1))
        peer = reader.read_object()
        id = reader.read_int32()
        story = None
        if flags & (1 << 0):
            story = reader.read_object()
        return cls(via_mention=via_mention, peer=peer, id=id, story=story)
@register_tl
class MessageMediaGiveaway(TLObject):
    ID: int = 0xaa073beb

    def __init__(self, only_new_subscribers: bool = False, winners_are_visible: bool = False, channels: Any = None, countries_iso2: Any = None, prize_description: Any = None, quantity: Any = None, months: Any = None, stars: Any = None, until_date: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.winners_are_visible = winners_are_visible
        self.channels = channels
        self.countries_iso2 = countries_iso2
        self.prize_description = prize_description
        self.quantity = quantity
        self.months = months
        self.stars = stars
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
        writer.write_vector(self.channels or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.countries_iso2 is not None:
            writer.write_vector(self.countries_iso2 or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.prize_description is not None:
            writer.write_string(str(self.prize_description or ''))
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
        channels = reader.read_vector(lambda r: r.read_object())
        countries_iso2 = None
        if flags & (1 << 1):
            countries_iso2 = reader.read_vector(lambda r: r.read_object())
        prize_description = None
        if flags & (1 << 3):
            prize_description = reader.read_string()
        quantity = reader.read_int32()
        months = None
        if flags & (1 << 4):
            months = reader.read_int32()
        stars = None
        if flags & (1 << 5):
            stars = reader.read_int64()
        until_date = reader.read_int32()
        return cls(only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, channels=channels, countries_iso2=countries_iso2, prize_description=prize_description, quantity=quantity, months=months, stars=stars, until_date=until_date)
@register_tl
class MessageMediaGiveawayResults(TLObject):
    ID: int = 0xceaa3ea1

    def __init__(self, only_new_subscribers: bool = False, refunded: bool = False, channel_id: Any = None, additional_peers_count: Any = None, launch_msg_id: Any = None, winners_count: Any = None, unclaimed_count: Any = None, winners: Any = None, months: Any = None, stars: Any = None, prize_description: Any = None, until_date: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.refunded = refunded
        self.channel_id = channel_id
        self.additional_peers_count = additional_peers_count
        self.launch_msg_id = launch_msg_id
        self.winners_count = winners_count
        self.unclaimed_count = unclaimed_count
        self.winners = winners
        self.months = months
        self.stars = stars
        self.prize_description = prize_description
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
        writer.write_vector(self.winners or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.months is not None:
            writer.write_int32(self.months or 0)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)
        if self.prize_description is not None:
            writer.write_string(str(self.prize_description or ''))
        writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGiveawayResults':
        flags = reader.read_uint32()
        only_new_subscribers = bool(flags & (1 << 0))
        refunded = bool(flags & (1 << 2))
        channel_id = reader.read_int64()
        additional_peers_count = None
        if flags & (1 << 3):
            additional_peers_count = reader.read_int32()
        launch_msg_id = reader.read_int32()
        winners_count = reader.read_int32()
        unclaimed_count = reader.read_int32()
        winners = reader.read_vector(lambda r: r.read_object())
        months = None
        if flags & (1 << 4):
            months = reader.read_int32()
        stars = None
        if flags & (1 << 5):
            stars = reader.read_int64()
        prize_description = None
        if flags & (1 << 1):
            prize_description = reader.read_string()
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
        writer.write_vector(self.extended_media or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPaidMedia':
        stars_amount = reader.read_int64()
        extended_media = reader.read_vector(lambda r: r.read_object())
        return cls(stars_amount=stars_amount, extended_media=extended_media)
@register_tl
class MessageMediaToDo(TLObject):
    ID: int = 0x8a53b014

    def __init__(self, todo: Any = None, completions: Any = None) -> None:
        self.todo = todo
        self.completions = completions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.completions is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.todo, 'write'):
            self.todo.write(writer)
        else:
            writer.write_bytes(self.todo or b'')
        if self.completions is not None:
            writer.write_vector(self.completions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaToDo':
        flags = reader.read_uint32()
        todo = reader.read_object()
        completions = None
        if flags & (1 << 0):
            completions = reader.read_vector(lambda r: r.read_object())
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
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')

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
        writer.write_string(str(self.title or ''))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatCreate':
        title = reader.read_string()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(title=title, users=users)
@register_tl
class MessageActionChatEditTitle(TLObject):
    ID: int = 0xb5a1ce5a

    def __init__(self, title: Any = None) -> None:
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.title or ''))

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
        if hasattr(self.photo, 'write'):
            self.photo.write(writer)
        else:
            writer.write_bytes(self.photo or b'')

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
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatAddUser':
        users = reader.read_vector(lambda r: r.read_object())
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
        writer.write_string(str(self.title or ''))

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
        writer.write_string(str(self.title or ''))
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

    def __init__(self, recurring_init: bool = False, recurring_used: bool = False, currency: Any = None, total_amount: Any = None, payload: Any = None, info: Any = None, shipping_option_id: Any = None, charge: Any = None, subscription_until_date: Any = None) -> None:
        self.recurring_init = recurring_init
        self.recurring_used = recurring_used
        self.currency = currency
        self.total_amount = total_amount
        self.payload = payload
        self.info = info
        self.shipping_option_id = shipping_option_id
        self.charge = charge
        self.subscription_until_date = subscription_until_date

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
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        writer.write_bytes(self.payload or b'')
        if self.info is not None:
            if hasattr(self.info, 'write'):
                self.info.write(writer)
            else:
                writer.write_bytes(self.info or b'')
        if self.shipping_option_id is not None:
            writer.write_string(str(self.shipping_option_id or ''))
        if hasattr(self.charge, 'write'):
            self.charge.write(writer)
        else:
            writer.write_bytes(self.charge or b'')
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
        info = None
        if flags & (1 << 0):
            info = reader.read_object()
        shipping_option_id = None
        if flags & (1 << 1):
            shipping_option_id = reader.read_string()
        charge = reader.read_object()
        subscription_until_date = None
        if flags & (1 << 4):
            subscription_until_date = reader.read_int32()
        return cls(recurring_init=recurring_init, recurring_used=recurring_used, currency=currency, total_amount=total_amount, payload=payload, info=info, shipping_option_id=shipping_option_id, charge=charge, subscription_until_date=subscription_until_date)
@register_tl
class MessageActionPaymentSent(TLObject):
    ID: int = 0xc624b16e

    def __init__(self, recurring_init: bool = False, recurring_used: bool = False, currency: Any = None, total_amount: Any = None, invoice_slug: Any = None, subscription_until_date: Any = None) -> None:
        self.recurring_init = recurring_init
        self.recurring_used = recurring_used
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_slug = invoice_slug
        self.subscription_until_date = subscription_until_date

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
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        if self.invoice_slug is not None:
            writer.write_string(str(self.invoice_slug or ''))
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentSent':
        flags = reader.read_uint32()
        recurring_init = bool(flags & (1 << 2))
        recurring_used = bool(flags & (1 << 3))
        currency = reader.read_string()
        total_amount = reader.read_int64()
        invoice_slug = None
        if flags & (1 << 0):
            invoice_slug = reader.read_string()
        subscription_until_date = None
        if flags & (1 << 4):
            subscription_until_date = reader.read_int32()
        return cls(recurring_init=recurring_init, recurring_used=recurring_used, currency=currency, total_amount=total_amount, invoice_slug=invoice_slug, subscription_until_date=subscription_until_date)
@register_tl
class MessageActionPhoneCall(TLObject):
    ID: int = 0x80e11a7f

    def __init__(self, video: bool = False, call_id: Any = None, reason: Any = None, duration: Any = None) -> None:
        self.video = video
        self.call_id = call_id
        self.reason = reason
        self.duration = duration

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
            if hasattr(self.reason, 'write'):
                self.reason.write(writer)
            else:
                writer.write_bytes(self.reason or b'')
        if self.duration is not None:
            writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPhoneCall':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 2))
        call_id = reader.read_int64()
        reason = None
        if flags & (1 << 0):
            reason = reader.read_object()
        duration = None
        if flags & (1 << 1):
            duration = reader.read_int32()
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
        writer.write_string(str(self.message or ''))

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
            writer.write_string(str(self.domain or ''))
        if self.app is not None:
            if hasattr(self.app, 'write'):
                self.app.write(writer)
            else:
                writer.write_bytes(self.app or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionBotAllowed':
        flags = reader.read_uint32()
        attach_menu = bool(flags & (1 << 1))
        from_request = bool(flags & (1 << 3))
        domain = None
        if flags & (1 << 0):
            domain = reader.read_string()
        app = None
        if flags & (1 << 2):
            app = reader.read_object()
        return cls(attach_menu=attach_menu, from_request=from_request, domain=domain, app=app)
@register_tl
class MessageActionSecureValuesSentMe(TLObject):
    ID: int = 0x1b287353

    def __init__(self, values: Any = None, credentials: Any = None) -> None:
        self.values = values
        self.credentials = credentials

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.values or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if hasattr(self.credentials, 'write'):
            self.credentials.write(writer)
        else:
            writer.write_bytes(self.credentials or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSecureValuesSentMe':
        values = reader.read_vector(lambda r: r.read_object())
        credentials = reader.read_object()
        return cls(values=values, credentials=credentials)
@register_tl
class MessageActionSecureValuesSent(TLObject):
    ID: int = 0xd95c6154

    def __init__(self, types: Any = None) -> None:
        self.types = types

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.types or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSecureValuesSent':
        types = reader.read_vector(lambda r: r.read_object())
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
        if hasattr(self.from_id, 'write'):
            self.from_id.write(writer)
        else:
            writer.write_bytes(self.from_id or b'')
        if hasattr(self.to_id, 'write'):
            self.to_id.write(writer)
        else:
            writer.write_bytes(self.to_id or b'')
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

    def __init__(self, call: Any = None, duration: Any = None) -> None:
        self.call = call
        self.duration = duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.duration is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        if self.duration is not None:
            writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGroupCall':
        flags = reader.read_uint32()
        call = reader.read_object()
        duration = None
        if flags & (1 << 0):
            duration = reader.read_int32()
        return cls(call=call, duration=duration)
@register_tl
class MessageActionInviteToGroupCall(TLObject):
    ID: int = 0x502f92f7

    def __init__(self, call: Any = None, users: Any = None) -> None:
        self.call = call
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionInviteToGroupCall':
        call = reader.read_object()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(call=call, users=users)
@register_tl
class MessageActionSetMessagesTTL(TLObject):
    ID: int = 0x3c134d7b

    def __init__(self, period: Any = None, auto_setting_from: Any = None) -> None:
        self.period = period
        self.auto_setting_from = auto_setting_from

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
        auto_setting_from = None
        if flags & (1 << 0):
            auto_setting_from = reader.read_int64()
        return cls(period=period, auto_setting_from=auto_setting_from)
@register_tl
class MessageActionGroupCallScheduled(TLObject):
    ID: int = 0xb3a07661

    def __init__(self, call: Any = None, schedule_date: Any = None) -> None:
        self.call = call
        self.schedule_date = schedule_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
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
        if hasattr(self.theme, 'write'):
            self.theme.write(writer)
        else:
            writer.write_bytes(self.theme or b'')

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
        writer.write_string(str(self.text or ''))
        writer.write_string(str(self.data or ''))

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
        writer.write_string(str(self.text or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionWebViewDataSent':
        text = reader.read_string()
        return cls(text=text)
@register_tl
class MessageActionGiftPremium(TLObject):
    ID: int = 0x48e91302

    def __init__(self, currency: Any = None, amount: Any = None, days: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, message: Any = None) -> None:
        self.currency = currency
        self.amount = amount
        self.days = days
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.message = message

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
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)
        writer.write_int32(self.days or 0)
        if self.crypto_currency is not None:
            writer.write_string(str(self.crypto_currency or ''))
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.message is not None:
            if hasattr(self.message, 'write'):
                self.message.write(writer)
            else:
                writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftPremium':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        days = reader.read_int32()
        crypto_currency = None
        if flags & (1 << 0):
            crypto_currency = reader.read_string()
        crypto_amount = None
        if flags & (1 << 0):
            crypto_amount = reader.read_int64()
        message = None
        if flags & (1 << 1):
            message = reader.read_object()
        return cls(currency=currency, amount=amount, days=days, crypto_currency=crypto_currency, crypto_amount=crypto_amount, message=message)
@register_tl
class MessageActionTopicCreate(TLObject):
    ID: int = 0xd999256

    def __init__(self, title_missing: bool = False, title: Any = None, icon_color: Any = None, icon_emoji_id: Any = None) -> None:
        self.title_missing = title_missing
        self.title = title
        self.icon_color = icon_color
        self.icon_emoji_id = icon_emoji_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title_missing:
            flags |= (1 << 1)
        if self.icon_emoji_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.title or ''))
        writer.write_int32(self.icon_color or 0)
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTopicCreate':
        flags = reader.read_uint32()
        title_missing = bool(flags & (1 << 1))
        title = reader.read_string()
        icon_color = reader.read_int32()
        icon_emoji_id = None
        if flags & (1 << 0):
            icon_emoji_id = reader.read_int64()
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
            writer.write_string(str(self.title or ''))
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)
        if self.closed is not None:
            writer.write_bool(bool(self.closed))
        if self.hidden is not None:
            writer.write_bool(bool(self.hidden))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTopicEdit':
        flags = reader.read_uint32()
        title = None
        if flags & (1 << 0):
            title = reader.read_string()
        icon_emoji_id = None
        if flags & (1 << 1):
            icon_emoji_id = reader.read_int64()
        closed = None
        if flags & (1 << 2):
            closed = reader.read_bool()
        hidden = None
        if flags & (1 << 3):
            hidden = reader.read_bool()
        return cls(title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)
@register_tl
class MessageActionSuggestProfilePhoto(TLObject):
    ID: int = 0x57de635e

    def __init__(self, photo: Any = None) -> None:
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.photo, 'write'):
            self.photo.write(writer)
        else:
            writer.write_bytes(self.photo or b'')

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
        writer.write_vector(self.peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionRequestedPeer':
        button_id = reader.read_int32()
        peers = reader.read_vector(lambda r: r.read_object())
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
        if hasattr(self.wallpaper, 'write'):
            self.wallpaper.write(writer)
        else:
            writer.write_bytes(self.wallpaper or b'')

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

    def __init__(self, via_giveaway: bool = False, unclaimed: bool = False, boost_peer: Any = None, days: Any = None, slug: Any = None, currency: Any = None, amount: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, message: Any = None) -> None:
        self.via_giveaway = via_giveaway
        self.unclaimed = unclaimed
        self.boost_peer = boost_peer
        self.days = days
        self.slug = slug
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.message = message

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
            if hasattr(self.boost_peer, 'write'):
                self.boost_peer.write(writer)
            else:
                writer.write_bytes(self.boost_peer or b'')
        writer.write_int32(self.days or 0)
        writer.write_string(str(self.slug or ''))
        if self.currency is not None:
            writer.write_string(str(self.currency or ''))
        if self.amount is not None:
            writer.write_int64(self.amount or 0)
        if self.crypto_currency is not None:
            writer.write_string(str(self.crypto_currency or ''))
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.message is not None:
            if hasattr(self.message, 'write'):
                self.message.write(writer)
            else:
                writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftCode':
        flags = reader.read_uint32()
        via_giveaway = bool(flags & (1 << 0))
        unclaimed = bool(flags & (1 << 5))
        boost_peer = None
        if flags & (1 << 1):
            boost_peer = reader.read_object()
        days = reader.read_int32()
        slug = reader.read_string()
        currency = None
        if flags & (1 << 2):
            currency = reader.read_string()
        amount = None
        if flags & (1 << 2):
            amount = reader.read_int64()
        crypto_currency = None
        if flags & (1 << 3):
            crypto_currency = reader.read_string()
        crypto_amount = None
        if flags & (1 << 3):
            crypto_amount = reader.read_int64()
        message = None
        if flags & (1 << 4):
            message = reader.read_object()
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
        stars = None
        if flags & (1 << 0):
            stars = reader.read_int64()
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
        writer.write_vector(self.peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionRequestedPeerSentMe':
        button_id = reader.read_int32()
        peers = reader.read_vector(lambda r: r.read_object())
        return cls(button_id=button_id, peers=peers)
@register_tl
class MessageActionPaymentRefunded(TLObject):
    ID: int = 0x41b3e202

    def __init__(self, peer: Any = None, currency: Any = None, total_amount: Any = None, payload: Any = None, charge: Any = None) -> None:
        self.peer = peer
        self.currency = currency
        self.total_amount = total_amount
        self.payload = payload
        self.charge = charge

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.payload is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        if self.payload is not None:
            writer.write_bytes(self.payload or b'')
        if hasattr(self.charge, 'write'):
            self.charge.write(writer)
        else:
            writer.write_bytes(self.charge or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentRefunded':
        flags = reader.read_uint32()
        peer = reader.read_object()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        payload = None
        if flags & (1 << 0):
            payload = reader.read_bytes()
        charge = reader.read_object()
        return cls(peer=peer, currency=currency, total_amount=total_amount, payload=payload, charge=charge)
@register_tl
class MessageActionGiftStars(TLObject):
    ID: int = 0x45d5b021

    def __init__(self, currency: Any = None, amount: Any = None, stars: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, transaction_id: Any = None) -> None:
        self.currency = currency
        self.amount = amount
        self.stars = stars
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.transaction_id = transaction_id

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
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)
        writer.write_int64(self.stars or 0)
        if self.crypto_currency is not None:
            writer.write_string(str(self.crypto_currency or ''))
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.transaction_id is not None:
            writer.write_string(str(self.transaction_id or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftStars':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        stars = reader.read_int64()
        crypto_currency = None
        if flags & (1 << 0):
            crypto_currency = reader.read_string()
        crypto_amount = None
        if flags & (1 << 0):
            crypto_amount = reader.read_int64()
        transaction_id = None
        if flags & (1 << 1):
            transaction_id = reader.read_string()
        return cls(currency=currency, amount=amount, stars=stars, crypto_currency=crypto_currency, crypto_amount=crypto_amount, transaction_id=transaction_id)
