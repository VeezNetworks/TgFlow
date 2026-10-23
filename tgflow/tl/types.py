from dataclasses import dataclass, field
from typing import Any, Optional

# Active Telegram Schema Layer
LAYER: int = 225


@dataclass(slots=True)
class User:
    id: int
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    is_bot: bool = False
    is_premium: bool = False
    phone: Optional[str] = None

    @property
    def full_name(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name


@dataclass(slots=True)
class Chat:
    id: int
    type: str  # private, group, supergroup, channel
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


# ==========================================================
# Telegram Layer 225 Modern Schema Models
# ==========================================================

# Telegram Business 2.0 (Layer 200–225)
@dataclass(slots=True)
class BusinessConnection:
    id: str
    user_id: int
    dc_id: int
    can_reply: bool = True
    is_disabled: bool = False


@dataclass(slots=True)
class BusinessIntro:
    title: str = ""
    description: str = ""
    sticker: Optional[str] = None


@dataclass(slots=True)
class BusinessLocation:
    address: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass(slots=True)
class QuickReplyShortcut:
    id: int
    shortcut: str
    message_count: int = 1


# Stories 2.0 (Layer 200–225)
@dataclass(slots=True)
class StoryItem:
    id: int
    peer_id: int
    date: int
    caption: Optional[str] = None
    views_count: int = 0
    reactions_count: int = 0
    is_pinned: bool = False


# Telegram Stars & Subscriptions (Layer 200–225)
@dataclass(slots=True)
class PaidMedia:
    stars_amount: int
    media_type: str = "photo"
    payload: Optional[bytes] = None


@dataclass(slots=True)
class PaidReaction:
    stars_count: int
    is_anonymous: bool = False


@dataclass(slots=True)
class StarSubscription:
    id: str
    period_seconds: int
    stars_amount: int
    is_canceled: bool = False


@dataclass(slots=True)
class StarGiveaway:
    stars_amount: int
    winners_count: int
    prize_description: Optional[str] = None


@dataclass(slots=True)
class StarsRevenueStatus:
    current_balance: int
    available_balance: int
    overall_revenue: int
    can_withdraw: bool = False
    withdrawal_url: Optional[str] = None


# Collectible Unique & Upgraded Gifts (Layer 215–225)
@dataclass(slots=True)
class Gift:
    id: str
    stars_cost: int
    slug: str
    total_count: Optional[int] = None
    remaining_count: Optional[int] = None
    is_limited: bool = False
    is_upgraded: bool = False
    gift_number: Optional[int] = None


# Forum Topics 2.0 (Layer 200–225)
@dataclass(slots=True)
class ForumTopic:
    id: int
    title: str
    icon_color: int
    icon_emoji_id: Optional[str] = None
    is_closed: bool = False
    is_pinned: bool = False
    is_hidden: bool = False


# Bot Verification & Affiliates (Layer 220–225)
@dataclass(slots=True)
class BotVerification:
    bot_id: int
    icon_custom_emoji_id: str
    description: str = ""


@dataclass(slots=True)
class AffiliateProgram:
    commission_permille: int
    revenue_stars: int = 0
