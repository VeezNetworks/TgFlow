from typing import Any


class Chat:
    def __init__(
        self,
        id: int,
        type: str = "private",
        title: str | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
    ) -> None:
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_tl(cls, tl_chat: Any) -> "Chat":
        cid = getattr(tl_chat, "id", 0)
        cname = tl_chat.__class__.__name__
        if cname in ("Channel", "ChannelForbidden"):
            ctype = "channel" if getattr(tl_chat, "broadcast", False) else "supergroup"
            return cls(id=cid, type=ctype, title=getattr(tl_chat, "title", None), username=getattr(tl_chat, "username", None))
        if cname in ("Chat", "ChatForbidden"):
            return cls(id=cid, type="group", title=getattr(tl_chat, "title", None))
        return cls(
            id=cid,
            type="private",
            first_name=getattr(tl_chat, "first_name", None),
            last_name=getattr(tl_chat, "last_name", None),
            username=getattr(tl_chat, "username", None),
        )
