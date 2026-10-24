from typing import Any, Optional
from .user import User


class GroupCall:
    def __init__(
        self,
        id: int,
        access_hash: int,
        participants_count: int = 0,
        title: str | None = None,
        stream_dc_id: int | None = None,
        schedule_date: int | None = None,
        is_active: bool = True,
        is_rtmp: bool = False,
    ) -> None:
        self.id = id
        self.access_hash = access_hash
        self.participants_count = participants_count
        self.title = title
        self.stream_dc_id = stream_dc_id
        self.schedule_date = schedule_date
        self.is_active = is_active
        self.is_rtmp = is_rtmp


class GroupCallParticipant:
    def __init__(
        self,
        peer: Any,
        date: int = 0,
        source: int = 0,
        volume: int = 10000,
        about: str | None = None,
        is_muted: bool = False,
        is_left: bool = False,
        can_self_unmute: bool = True,
        is_video_joined: bool = False,
        is_self: bool = False,
    ) -> None:
        self.peer = peer
        self.date = date
        self.source = source
        self.volume = volume
        self.about = about
        self.is_muted = is_muted
        self.is_left = is_left
        self.can_self_unmute = can_self_unmute
        self.is_video_joined = is_video_joined
        self.is_self = is_self
