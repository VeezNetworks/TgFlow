from typing import Any, Optional
from .user import User


class ChatPermissions:
    def __init__(
        self,
        can_send_messages: bool = True,
        can_send_audios: bool = True,
        can_send_documents: bool = True,
        can_send_photos: bool = True,
        can_send_videos: bool = True,
        can_send_video_notes: bool = True,
        can_send_voice_notes: bool = True,
        can_send_polls: bool = True,
        can_send_other_messages: bool = True,
        can_add_web_page_previews: bool = True,
        can_change_info: bool = False,
        can_invite_users: bool = False,
        can_pin_messages: bool = False,
        can_manage_topics: bool = False,
    ) -> None:
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics


class ChatMember:
    def __init__(
        self,
        status: str,
        user: User,
        custom_title: str | None = None,
        is_anonymous: bool = False,
        until_date: int = 0,
        can_be_edited: bool = False,
        can_manage_chat: bool = False,
        can_delete_messages: bool = False,
        can_manage_video_chats: bool = False,
        can_restrict_members: bool = False,
        can_promote_members: bool = False,
        can_change_info: bool = False,
        can_invite_users: bool = False,
        can_post_messages: bool = False,
        can_edit_messages: bool = False,
        can_pin_messages: bool = False,
        can_manage_topics: bool = False,
    ) -> None:
        self.status = status
        self.user = user
        self.custom_title = custom_title
        self.is_anonymous = is_anonymous
        self.until_date = until_date
        self.can_be_edited = can_be_edited
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics


class ChatInviteLink:
    def __init__(
        self,
        invite_link: str,
        creator: User,
        creates_join_request: bool = False,
        is_primary: bool = False,
        is_revoked: bool = False,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        pending_join_request_count: int | None = None,
    ) -> None:
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count
