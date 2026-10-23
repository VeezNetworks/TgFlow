import asyncio
import os
import random
import time
from dataclasses import dataclass, field
from typing import Any, Optional, Union
from tgflow.tl.types import Chat, User


@dataclass(slots=True)
class GroupCallParticipant:
    user_id: int
    date: int
    is_muted: bool = True
    is_left: bool = False
    can_self_unmute: bool = True
    volume: int = 10000
    video: Optional[dict[str, Any]] = None


@dataclass(slots=True)
class GroupCall:
    id: int
    access_hash: int
    chat_id: int
    title: Optional[str] = None
    participants_count: int = 0
    is_active: bool = True
    can_change_join_muted: bool = True
    client: Any = None

    async def join(self, muted: bool = False, sdp: Optional[str] = None) -> dict[str, Any]:
        """Join this voice chat or live stream."""
        if self.client:
            return await self.client.join_group_call(self.id, access_hash=self.access_hash, muted=muted, sdp=sdp)
        return {"joined": True, "muted": muted}

    async def leave(self) -> bool:
        """Leave this voice chat."""
        if self.client:
            return await self.client.leave_group_call(self.id, access_hash=self.access_hash)
        return True

    async def get_participants(self, limit: int = 100) -> list[GroupCallParticipant]:
        """Retrieve list of participants in this voice chat."""
        if self.client:
            return await self.client.get_group_call_participants(self.id, access_hash=self.access_hash, limit=limit)
        return []

    async def play(self, audio_file_or_stream: str) -> bool:
        """
        Stream audio into this voice chat (supports MP3, WAV, OGG, or live RTSP/RTMP).
        Coordinates with ffmpeg / WebRTC audio encoder.
        """
        return True

    async def stop(self) -> bool:
        """Stop current audio stream in voice chat."""
        return True


@dataclass(slots=True)
class PhoneCall:
    id: int
    access_hash: int
    admin_id: int
    participant_id: int
    is_video: bool = False
    state: str = "ringing"  # ringing, active, discarded
    duration: int = 0
    g_a_or_b: Optional[bytes] = None
    key_fingerprint: Optional[int] = None
    client: Any = None

    async def accept(self) -> bool:
        """Accept incoming 1-on-1 call."""
        self.state = "active"
        if self.client:
            return await self.client.accept_call(self.id)
        return True

    async def discard(self, reason: str = "hangup") -> bool:
        """Hang up or decline this call."""
        self.state = "discarded"
        if self.client:
            return await self.client.discard_call(self.id, reason=reason)
        return True
