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
    def __init__(self, func: Callable[..., bool]) -> None:
        self.func = func

    def __call__(self, client: Any, update: Any) -> bool:
        return bool(self.func(client, update))


class AllFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return True


class TextFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return bool(getattr(update, "text", None))


class PrivateFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        chat = getattr(update, "chat", None)
        return bool(chat and getattr(chat, "type", "") == "private")


class GroupFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        chat = getattr(update, "chat", None)
        return bool(chat and getattr(chat, "type", "") in ("group", "supergroup"))


class ChannelFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        chat = getattr(update, "chat", None)
        return bool(chat and getattr(chat, "type", "") == "channel")


class BotFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        user = getattr(update, "from_user", None)
        return bool(user and getattr(user, "is_bot", False))


class ReplyFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return bool(getattr(update, "reply_to_message_id", None) or getattr(update, "reply_to_message", None))


class ForwardedFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return bool(getattr(update, "forward_from", None) or getattr(update, "forward_date", None))


class PhotoFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "photo", None) is not None


class VideoFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "video", None) is not None


class AudioFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "audio", None) is not None


class DocumentFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "document", None) is not None


class VoiceFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "voice", None) is not None


class AnimationFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "animation", None) is not None


class StickerFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "sticker", None) is not None


class PollFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return getattr(update, "poll", None) is not None


class MediaFilter(Filter):
    def __call__(self, client: Any, update: Any) -> bool:
        return any(
            getattr(update, attr, None) is not None
            for attr in ("photo", "video", "document", "audio", "voice", "animation", "sticker")
        )


class CommandContext:
    def __init__(self, client: Any, message: Any, command: str, args: str, kwargs: dict[str, Any]) -> None:
        self.client = client
        self.message = message
        self.command = command
        self.args = args
        self.kwargs = kwargs
        self.chat = getattr(message, "chat", None)
        self.from_user = getattr(message, "from_user", None)

    async def reply(self, text: str, **kwargs: Any) -> Any:
        return await self.message.reply(text, **kwargs)

    async def reply_text(self, text: str, **kwargs: Any) -> Any:
        return await self.message.reply(text, **kwargs)


class FlowCommand:
    def __init__(
        self,
        name: str,
        description: str = "",
        prefixes: Union[str, Sequence[str]] = "/",
        when: Filter | None = None,
        aliases: Sequence[str] | None = None,
        case_sensitive: bool = False,
    ) -> None:
        self.name = name
        self.description = description
        self.prefixes = prefixes
        self.when_filter = when
        self.aliases = list(aliases) if aliases else []
        self.case_sensitive = case_sensitive

    def desc(self, description: str) -> "FlowCommand":
        self.description = description
        return self

    def prefix(self, prefixes: Union[str, Sequence[str]]) -> "FlowCommand":
        self.prefixes = prefixes
        return self

    def when(self, filter_obj: Filter) -> "FlowCommand":
        self.when_filter = (self.when_filter & filter_obj) if self.when_filter else filter_obj
        return self

    def alias(self, *aliases: str) -> "FlowCommand":
        self.aliases.extend(aliases)
        return self

    def build_filter(self) -> Filter:
        cmds = [self.name] + self.aliases
        f = CommandFilter(cmds, prefixes=self.prefixes, case_sensitive=self.case_sensitive)
        if self.when_filter:
            return f & self.when_filter
        return f


Command = FlowCommand


class CommandFilter(Filter):
    def __init__(
        self,
        commands: Union[str, Sequence[str], FlowCommand],
        prefixes: Union[str, Sequence[str]] = "/",
        case_sensitive: bool = False,
    ) -> None:
        self.case_sensitive = case_sensitive
        prefix_list = [prefixes] if isinstance(prefixes, str) else list(prefixes)
        self.prefixes = set(prefix_list)
        self.arg_specs: list[tuple[str, type, bool]] = []

        raw_candidates: list[str] = []
        if isinstance(commands, FlowCommand):
            raw_candidates = [commands.name] + commands.aliases
        elif isinstance(commands, str):
            raw_candidates = [commands]
        else:
            raw_candidates = list(commands)

        raw_cmds: list[str] = []
        for idx, item in enumerate(raw_candidates):
            tokens = item.strip().split()
            if tokens:
                raw_cmds.append(tokens[0])
                if idx == 0 and len(tokens) > 1 and not self.arg_specs:
                    for tok in tokens[1:]:
                        is_opt = tok.startswith("[") and tok.endswith("]")
                        clean_tok = tok.strip("<>[]")
                        typ = str
                        name = clean_tok
                        if ":" in clean_tok:
                            name, t_name = clean_tok.split(":", 1)
                            if t_name.lower() in ("int", "integer"):
                                typ = int
                            elif t_name.lower() in ("float", "double"):
                                typ = float
                            elif t_name.lower() in ("bool", "boolean"):
                                typ = bool
                        self.arg_specs.append((name, typ, is_opt))

        self.commands: set[str] = set()
        for c in raw_cmds:
            clean_c = c
            for p in self.prefixes:
                if clean_c.startswith(p):
                    clean_c = clean_c[len(p):]
                    break
            if not self.case_sensitive:
                clean_c = clean_c.lower()
            self.commands.add(clean_c)

    def __call__(self, client: Any, update: Any) -> bool:
        text = getattr(update, "text", "") or ""
        if not text:
            return False
        for prefix in self.prefixes:
            if prefix == "" or text.startswith(prefix):
                rem = text[len(prefix):] if prefix else text
                parts = rem.split()
                if not parts:
                    continue
                raw_token = parts[0].split("@")[0]
                cmd = raw_token if self.case_sensitive else raw_token.lower()
                if cmd in self.commands:
                    args_list = parts[1:]
                    args_str = rem[len(parts[0]):].strip()
                    update.command = [cmd] + args_list
                    update.command_name = cmd
                    update.command_args = args_str
                    update.command_args_list = args_list
                    update.args = args_str

                    parsed_kwargs = {}
                    for idx, spec in enumerate(self.arg_specs):
                        name, typ, is_opt = spec
                        if idx < len(args_list):
                            val = args_list[idx]
                            try:
                                if typ is bool:
                                    parsed_kwargs[name] = val.lower() in ("1", "true", "yes", "on")
                                else:
                                    parsed_kwargs[name] = typ(val)
                            except (ValueError, TypeError):
                                parsed_kwargs[name] = val
                        elif not is_opt:
                            parsed_kwargs[name] = None
                        else:
                            parsed_kwargs[name] = None
                    update.command_kwargs = parsed_kwargs
                    update.command_context = CommandContext(client, update, cmd, args_str, parsed_kwargs)
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
        user = getattr(update, "from_user", None)
        if not user:
            return False
        uid = getattr(user, "id", None)
        uname = (getattr(user, "username", "") or "").lower().lstrip("@")
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


class DataFilter(Filter):
    def __init__(self, data: Union[str, Sequence[str]]) -> None:
        self.allowed = {data} if isinstance(data, str) else set(data)

    def __call__(self, client: Any, update: Any) -> bool:
        val = getattr(update, "data", None)
        return val in self.allowed


class WhenRegistry:
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
    video = VideoFilter()
    audio = AudioFilter()
    document = DocumentFilter()
    voice = VoiceFilter()
    animation = AnimationFilter()
    sticker = StickerFilter()
    poll = PollFilter()

    @staticmethod
    def command(
        commands: Union[str, Sequence[str], FlowCommand],
        prefixes: Union[str, Sequence[str]] = "/",
        case_sensitive: bool = False,
    ) -> CommandFilter:
        return CommandFilter(commands, prefixes, case_sensitive=case_sensitive)

    @staticmethod
    def regex(pattern: Union[str, re.Pattern]) -> RegexFilter:
        return RegexFilter(pattern)

    @staticmethod
    def user(users: Union[int, str, Sequence[Union[int, str]]]) -> UserFilter:
        return UserFilter(users)

    @staticmethod
    def chat(chats: Union[int, str, Sequence[Union[int, str]]]) -> ChatFilter:
        return ChatFilter(chats)

    @staticmethod
    def data(data: Union[str, Sequence[str]]) -> DataFilter:
        return DataFilter(data)

    @staticmethod
    def custom(func: Callable[..., bool]) -> CustomFilter:
        return CustomFilter(func)


When = WhenRegistry
F = WhenRegistry

all = When.all
text = When.text
private = When.private
group = When.group
channel = When.channel
bot = When.bot
reply = When.reply
forwarded = When.forwarded
media = When.media
photo = When.photo
video = When.video
audio = When.audio
document = When.document
voice = When.voice
animation = When.animation
sticker = When.sticker
poll = When.poll
command = When.command
regex = When.regex
user = When.user
chat = When.chat
data = When.data
custom = When.custom
create = When.custom
