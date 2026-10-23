from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass(slots=True)
class User:
    id: int
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    phone: Optional[str] = None
    is_bot: bool = False
    is_premium: bool = False

    @property
    def full_name(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name

    @property
    def mention(self) -> str:
        if self.username:
            return f"@{self.username}"
        return self.full_name


@dataclass(slots=True)
class Chat:
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None
    is_forum: bool = False


@dataclass(slots=True)
class Message:
    id: int
    chat: Chat
    sender: Optional[User] = None
    text: Optional[str] = None
    reply_to: Optional["Message"] = None
    date: int = 0
    raw: dict[str, Any] = field(default_factory=dict)

    @property
    def chat_id(self) -> int:
        return self.chat.id

    @property
    def sender_id(self) -> Optional[int]:
        return self.sender.id if self.sender else None


@dataclass(slots=True)
class BusinessConnection:
    id: str
    user_id: int
    dc_id: int
    can_reply: bool = True
    is_disabled: bool = False


@dataclass(slots=True)
class StoryItem:
    id: int
    peer_id: int
    date: int
    caption: Optional[str] = None
    views_count: int = 0


@dataclass(slots=True)
class PaidMedia:
    stars_amount: int
    media_type: str
    payload: Optional[bytes] = None


@dataclass(slots=True)
class ForumTopic:
    id: int
    title: str
    icon_color: int
    is_closed: bool = False


@dataclass(slots=True)
class Gift:
    id: str
    stars_cost: int
    slug: str
