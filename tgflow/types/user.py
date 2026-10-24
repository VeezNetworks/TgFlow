from typing import Any


class User:
    def __init__(
        self,
        id: int,
        first_name: str = "",
        last_name: str | None = None,
        username: str | None = None,
        is_bot: bool = False,
        is_premium: bool = False,
        phone_number: str | None = None,
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.is_bot = is_bot
        self.is_premium = is_premium
        self.phone_number = phone_number

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

    @classmethod
    def from_tl(cls, tl_user: Any) -> "User":
        return cls(
            id=getattr(tl_user, "id", 0),
            first_name=getattr(tl_user, "first_name", "") or "",
            last_name=getattr(tl_user, "last_name", None),
            username=getattr(tl_user, "username", None),
            is_bot=bool(getattr(tl_user, "bot", False)),
            is_premium=bool(getattr(tl_user, "premium", False)),
            phone_number=getattr(tl_user, "phone", None),
        )
