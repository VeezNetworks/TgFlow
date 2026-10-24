import re
from typing import Any, Callable, Sequence, Union


class Filter:
    def __call__(self, client: Any, update: Any) -> bool:
        raise NotImplementedError

    def __and__(self, other: "Filter") -> "Filter":
        return AndFilter(self, other)

    def __or__(self, other: "Filter") -> "Filter":
        return OrFilter(self, other)

    def __invert__(self) -> "Filter":
        return InvertFilter(self)


class AndFilter(Filter):
    def __init__(self, f1: Filter, f2: Filter) -> None:
        self.f1 = f1
        self.f2 = f2

    def __call__(self, client: Any, update: Any) -> bool:
        return bool(self.f1(client, update) and self.f2(client, update))


class OrFilter(Filter):
    def __init__(self, f1: Filter, f2: Filter) -> None:
        self.f1 = f1
        self.f2 = f2

    def __call__(self, client: Any, update: Any) -> bool:
        return bool(self.f1(client, update) or self.f2(client, update))


class InvertFilter(Filter):
    def __init__(self, f: Filter) -> None:
        self.f = f

    def __call__(self, client: Any, update: Any) -> bool:
        return not bool(self.f(client, update))


class CustomFilter(Filter):
    def __init__(self, func: Callable[[Any, Any], bool]) -> None:
        self.func = func

    def __call__(self, client: Any, update: Any) -> bool:
        try:
            return bool(self.func(client, update))
        except TypeError:
            return bool(self.func(update))


def create(func: Callable[..., bool]) -> Filter:
    return CustomFilter(func)


class AllFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return True


class TextFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        text = getattr(update, "text", None) or getattr(update, "message", None)
        return bool(text and isinstance(text, str) and len(text.strip()) > 0)


class PrivateFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        chat = getattr(update, "chat", None)
        if not chat:
            return False
        return getattr(chat, "type", "") == "private"


class GroupFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        chat = getattr(update, "chat", None)
        if not chat:
            return False
        return getattr(chat, "type", "") in ("group", "supergroup")


class ChannelFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        chat = getattr(update, "chat", None)
        if not chat:
            return False
        return getattr(chat, "type", "") == "channel"


class BotFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        from_user = getattr(update, "from_user", None)
        if not from_user:
            return False
        return bool(getattr(from_user, "is_bot", False))


class ReplyFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "reply_to_message", None) is not None or getattr(update, "reply_to_message_id", None) is not None


class ForwardedFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "forward_from", None) is not None or getattr(update, "forward_date", None) is not None


class MediaFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return any(
            getattr(update, attr, None) is not None
            for attr in ("photo", "video", "document", "audio", "voice", "animation", "sticker")
        )


class PhotoFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "photo", None) is not None


class DocumentFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "document", None) is not None


class CommandFilter(Filter):
    def __init__(self, commands: Union[str, Sequence[str]], prefixes: Union[str, Sequence[str]] = "/") -> None:
        if isinstance(commands, str):
            self.commands = [commands.lower()]
        else:
            self.commands = [c.lower() for c in commands]
        self.prefixes = set(prefixes if not isinstance(prefixes, str) else [prefixes])

    def __call__(self, client: Any, update: Any) -> bool:
        text = getattr(update, "text", "") or ""
        if not text:
            return False
        for prefix in self.prefixes:
            if text.startswith(prefix):
                parts = text[len(prefix):].split()
                if not parts:
                    continue
                cmd = parts[0].split("@")[0].lower()
                if cmd in self.commands:
                    update.command = [cmd] + parts[1:]
                    return True
        return False


class RegexFilter(Filter):
    def __init__(self, pattern: Union[str, re.Pattern]) -> None:
        self.pattern = re.compile(pattern) if isinstance(pattern, str) else pattern

    def __call__(self, client: Any, update: Any) -> bool:
        text = getattr(update, "text", "") or getattr(update, "data", "") or ""
        match = self.pattern.search(str(text))
        if match:
            update.matches = [match]
            return True
        return False


class UserFilter(Filter):
    def __init__(self, users: Union[int, str, Sequence[Union[int, str]]]) -> None:
        user_list = [users] if isinstance(users, (int, str)) else list(users)
        self.user_ids = {u for u in user_list if isinstance(u, int)}
        self.usernames = {u.lower().lstrip("@") for u in user_list if isinstance(u, str)}

    def __call__(self, client: Any, update: Any) -> bool:
        from_user = getattr(update, "from_user", None)
        if not from_user:
            return False
        uid = getattr(from_user, "id", None)
        uname = (getattr(from_user, "username", "") or "").lower().lstrip("@")
        return uid in self.user_ids or uname in self.usernames


class ChatFilter(Filter):
    def __init__(self, chats: Union[int, str, Sequence[Union[int, str]]]) -> None:
        chat_list = [chats] if isinstance(chats, (int, str)) else list(chats)
        self.chat_ids = {c for c in chat_list if isinstance(c, int)}
        self.usernames = {c.lower().lstrip("@") for c in chat_list if isinstance(c, str)}

    def __call__(self, client: Any, update: Any) -> bool:
        chat = getattr(update, "chat", None)
        if not chat:
            return False
        cid = getattr(chat, "id", None)
        cname = (getattr(chat, "username", "") or "").lower().lstrip("@")
        return cid in self.chat_ids or cname in self.usernames


all = AllFilter()
text = TextFilter()
private = PrivateFilter()
group = GroupFilter()
channel = ChannelFilter()
bot = BotFilter()
reply = ReplyFilter()
forwarded = ForwardedFilter()
media = MediaFilter()
photo = PhotoFilter()
document = DocumentFilter()
command = CommandFilter
regex = RegexFilter
user = UserFilter
chat = ChatFilter
