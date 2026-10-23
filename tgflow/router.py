import inspect
import re
from typing import Any, Callable, Optional, Union
from tgflow.filters import Filter


class RouteSegment:
    def __init__(self, name: str, param_type: type = str, default: Any = None, is_catchall: bool = False):
        self.name = name
        self.param_type = param_type
        self.default = default
        self.is_catchall = is_catchall


class RouteTemplate:
    PARAM_PATTERN = re.compile(r"<([a-zA-Z_][a-zA-Z0-9_]*)(?::(int|str))?(?:=([^>]+))?(\*)?>")

    def __init__(self, template: str):
        self.template = template
        self.command = ""
        self.segments: list[RouteSegment] = []
        self._parse()

    def _parse(self) -> None:
        parts = self.template.strip().split()
        if not parts:
            return

        self.command = parts[0].lower()

        for part in parts[1:]:
            match = self.PARAM_PATTERN.match(part)
            if not match:
                self.segments.append(RouteSegment(name=part, default=part))
                continue

            name = match.group(1)
            raw_type = match.group(2) or "str"
            raw_default = match.group(3)
            is_catchall = bool(match.group(4))

            param_type = int if raw_type == "int" else str
            default_val = None
            if raw_default is not None:
                default_val = param_type(raw_default)

            self.segments.append(RouteSegment(name=name, param_type=param_type, default=default_val, is_catchall=is_catchall))

    def match(self, text: str, reply_to: Any = None) -> Optional[dict[str, Any]]:
        parts = text.strip().split()
        if not parts:
            return None

        cmd = parts[0].lower()
        if cmd != self.command:
            return None

        args = parts[1:]
        extracted: dict[str, Any] = {}
        arg_idx = 0

        for seg in self.segments:
            if seg.name == "target":
                if reply_to and reply_to.sender:
                    extracted["target"] = reply_to.sender
                    continue
                elif arg_idx < len(args):
                    extracted["target"] = args[arg_idx]
                    arg_idx += 1
                    continue
                elif seg.default is not None:
                    extracted["target"] = seg.default
                    continue
                else:
                    return None

            if seg.is_catchall:
                if arg_idx < len(args):
                    extracted[seg.name] = " ".join(args[arg_idx:])
                else:
                    extracted[seg.name] = seg.default
                arg_idx = len(args)
                break

            if arg_idx < len(args):
                raw = args[arg_idx]
                try:
                    extracted[seg.name] = seg.param_type(raw)
                except ValueError:
                    return None
                arg_idx += 1
            elif seg.default is not None:
                extracted[seg.name] = seg.default
            else:
                return None

        return extracted


class HandlerEntry:
    def __init__(
        self,
        handler: Callable,
        template: Optional[RouteTemplate] = None,
        filter_obj: Optional[Filter] = None,
        regex_pattern: Optional[re.Pattern] = None,
    ):
        self.handler = handler
        self.template = template
        self.filter = filter_obj
        self.regex = regex_pattern


class Router:
    def __init__(self):
        self.entries: list[HandlerEntry] = []

    def on(self, target: Union[str, Filter, Callable], filter_obj: Optional[Filter] = None):
        template = None
        current_filter = filter_obj

        if isinstance(target, str):
            template = RouteTemplate(target)
        elif isinstance(target, Filter):
            current_filter = target if current_filter is None else (current_filter & target)

        def decorator(func: Callable):
            self.entries.append(
                HandlerEntry(
                    handler=func,
                    template=template,
                    filter_obj=current_filter,
                )
            )
            return func

        if callable(target) and not isinstance(target, Filter):
            return decorator(target)

        return decorator

    def regex(self, pattern: Union[str, re.Pattern], filter_obj: Optional[Filter] = None):
        compiled = re.compile(pattern) if isinstance(pattern, str) else pattern

        def decorator(func: Callable):
            self.entries.append(
                HandlerEntry(
                    handler=func,
                    regex_pattern=compiled,
                    filter_obj=filter_obj,
                )
            )
            return func

        return decorator

    def respond(self, command: str, text_response: str) -> None:
        template = RouteTemplate(command)

        async def _static_responder(ctx):
            await ctx.reply(text_response)

        self.entries.append(HandlerEntry(handler=_static_responder, template=template))

    async def dispatch(self, ctx: Any) -> bool:
        message = getattr(ctx, "message", ctx)
        client = getattr(ctx, "client", None)
        text = getattr(message, "text", None) or getattr(message, "caption", None)

        for entry in self.entries:
            if entry.filter is not None:
                passed = await entry.filter(client, message)
                if not passed:
                    continue

            if entry.template is not None:
                if not text:
                    continue
                reply_to = getattr(message, "reply_to", None)
                params = entry.template.match(text, reply_to=reply_to)
                if params is None:
                    continue

                sig = inspect.signature(entry.handler)
                if len(sig.parameters) <= 1:
                    await entry.handler(ctx)
                else:
                    await entry.handler(ctx, **params)
                return True

            elif entry.regex is not None:
                if not text:
                    continue
                match = entry.regex.match(text)
                if match:
                    kwargs = match.groupdict()
                    if kwargs:
                        await entry.handler(ctx, **kwargs)
                    else:
                        await entry.handler(ctx, *match.groups())
                    return True

            elif entry.filter is not None:
                await entry.handler(ctx)
                return True

        return False
