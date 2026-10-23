import inspect
import re
from typing import Any, Callable, Coroutine, Union


class Filter:
    def __init__(self, func: Callable[[Any, Any], Union[bool, Coroutine[Any, Any, bool]]], name: str = ""):
        self.func = func
        self.name = name or getattr(func, "__name__", "custom_filter")

    async def __call__(self, client: Any, update: Any) -> bool:
        if inspect.iscoroutinefunction(self.func):
            return await self.func(client, update)
        res = self.func(client, update)
        if inspect.isawaitable(res):
            return await res
        return bool(res)

    def __and__(self, other: "Filter") -> "Filter":
        async def _and_filter(client: Any, update: Any) -> bool:
            return (await self(client, update)) and (await other(client, update))

        return Filter(_and_filter, f"({self.name} & {other.name})")

    def __or__(self, other: "Filter") -> "Filter":
        async def _or_filter(client: Any, update: Any) -> bool:
            return (await self(client, update)) or (await other(client, update))

        return Filter(_or_filter, f"({self.name} | {other.name})")

    def __invert__(self) -> "Filter":
        async def _not_filter(client: Any, update: Any) -> bool:
            return not (await self(client, update))

        return Filter(_not_filter, f"(~{self.name})")


def create(func: Callable[[Any, Any], Union[bool, Coroutine[Any, Any, bool]]], name: str = "") -> Filter:
    return Filter(func, name=name)


# Basic Content Filters
text = Filter(lambda _, u: bool(getattr(u, "text", None)), "text")
caption = Filter(lambda _, u: bool(getattr(u, "caption", None)), "caption")
reply = Filter(lambda _, u: getattr(u, "reply_to", None) is not None, "reply")
forwarded = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("forward_date")), "forwarded")
pinned = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("pinned_message")), "pinned")

# Chat Type Filters
private = Filter(lambda _, u: getattr(getattr(u, "chat", None), "type", "") == "private", "private")
group = Filter(lambda _, u: getattr(getattr(u, "chat", None), "type", "") in ("group", "supergroup"), "group")
channel = Filter(lambda _, u: getattr(getattr(u, "chat", None), "type", "") == "channel", "channel")
supergroup = Filter(lambda _, u: getattr(getattr(u, "chat", None), "type", "") == "supergroup", "supergroup")
forum = Filter(lambda _, u: bool(getattr(getattr(u, "chat", None), "is_forum", False)), "forum")

# Sender & Identity Filters
bot = Filter(lambda _, u: bool(getattr(getattr(u, "sender", None), "is_bot", False)), "bot")
me = Filter(lambda c, u: bool(getattr(u, "sender_id", None) and getattr(u, "sender_id", None) == getattr(c, "me_id", 0)), "me")
incoming = Filter(lambda _, u: not bool(getattr(u, "raw", {}).get("out", False)), "incoming")
outgoing = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("out", False)), "outgoing")


def user(users: Union[int, str, list[Union[int, str]]]) -> Filter:
    user_set = {users} if isinstance(users, (int, str)) else set(users)

    def _user_filter(_, u: Any) -> bool:
        sender = getattr(u, "sender", None)
        if not sender:
            return False
        return sender.id in user_set or (sender.username and sender.username.lower() in {str(x).lower().lstrip("@") for x in user_set})

    return Filter(_user_filter, f"user({users})")


def chat(chats: Union[int, str, list[Union[int, str]]]) -> Filter:
    chat_set = {chats} if isinstance(chats, (int, str)) else set(chats)

    def _chat_filter(_, u: Any) -> bool:
        ch = getattr(u, "chat", None)
        if not ch:
            return False
        return ch.id in chat_set or (ch.username and ch.username.lower() in {str(x).lower().lstrip("@") for x in chat_set})

    return Filter(_chat_filter, f"chat({chats})")


# Commands & Regex
def command(commands: Union[str, list[str]], prefixes: Union[str, list[str]] = "/") -> Filter:
    cmds = [commands] if isinstance(commands, str) else list(commands)
    cmds = [c.lower().lstrip("/!") for c in cmds]
    prefs = [prefixes] if isinstance(prefixes, str) else list(prefixes)

    def _command_filter(_, u: Any) -> bool:
        t = getattr(u, "text", None) or getattr(u, "caption", None)
        if not t:
            return False
        parts = t.strip().split()
        if not parts:
            return False
        first = parts[0]
        for p in prefs:
            if first.startswith(p):
                clean_cmd = first[len(p) :].split("@")[0].lower()
                return clean_cmd in cmds
        return False

    return Filter(_command_filter, f"command({commands})")


def regex(pattern: Union[str, re.Pattern]) -> Filter:
    compiled = re.compile(pattern) if isinstance(pattern, str) else pattern

    def _regex_filter(_, u: Any) -> bool:
        t = getattr(u, "text", None) or getattr(u, "caption", None)
        if not t:
            return False
        return bool(compiled.search(t))

    return Filter(_regex_filter, f"regex({pattern})")


# Media Type Filters
photo = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("photo")), "photo")
video = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("video")), "video")
audio = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("audio")), "audio")
voice = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("voice")), "voice")
document = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("document")), "document")
sticker = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("sticker")), "sticker")
animation = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("animation")), "animation")
dice = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("dice")), "dice")
media = photo | video | audio | voice | document | sticker | animation

# Modern Layer 225 Filters
story = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("story")), "story")
business = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("business_connection_id")), "business")
paid_media = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("paid_media")), "paid_media")
gift = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("gift")), "gift")
topic = Filter(lambda _, u: bool(getattr(u, "raw", {}).get("message_thread_id")), "topic")
quote = Filter(lambda _, u: bool(getattr(u, "quote", None)), "quote")
ephemeral = Filter(lambda _, u: bool(getattr(u, "is_ephemeral", False)), "ephemeral")


class _FilterTypography:
    """Fluent, expressive typography for routing conditions."""

    # Content
    text = Text = text
    caption = Caption = caption
    reply = Reply = reply
    forwarded = Forwarded = forwarded
    pinned = Pinned = pinned
    quote = Quote = quote
    ephemeral = Ephemeral = ephemeral

    # Chat
    private = Private = private
    group = Group = group
    channel = Channel = channel
    supergroup = Supergroup = supergroup
    forum = Forum = forum

    # Senders
    bot = Bot = bot
    me = Me = me
    incoming = Incoming = incoming
    outgoing = Outgoing = outgoing

    # Media
    media = Media = media
    photo = Photo = photo
    video = Video = video
    audio = Audio = audio
    voice = Voice = voice
    document = Document = document
    sticker = Sticker = sticker
    animation = Animation = animation
    dice = Dice = dice

    # Modern features
    story = Story = story
    business = Business = business
    paid_media = PaidMedia = paid_media
    stars = Stars = paid_media
    gift = Gift = gift
    topic = Topic = topic

    # Factory methods
    command = Command = staticmethod(command)
    regex = Regex = staticmethod(regex)
    user = User = staticmethod(user)
    chat = Chat = staticmethod(chat)
    create = Create = staticmethod(create)


When = _FilterTypography()
F = _FilterTypography()
