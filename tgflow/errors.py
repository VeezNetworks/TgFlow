import re


class RPCError(Exception):
    CODE: int = 0
    NAME: str = "RPC_ERROR"

    def __init__(self, message: str = "", code: int = 0, value: int | None = None) -> None:
        self.message = message or self.NAME
        self.code = code or self.CODE
        self.value = value
        super().__init__(f"[{self.code} {self.message}]" + (f" (value={self.value})" if self.value else ""))

    @classmethod
    def from_rpc_error(cls, code: int, text: str) -> "RPCError":
        match = re.match(r"^([A-Z0-9_]+?)(?:_(\d+))?$", text)
        name = match.group(1) if match else text
        val = int(match.group(2)) if match and match.group(2) else None

        if code == 420 or "FLOOD_WAIT" in text:
            return FloodWait(message=text, code=code, value=val or 1)
        if code == 400:
            return BadRequest(message=text, code=code, value=val)
        if code == 401:
            return Unauthorized(message=text, code=code, value=val)
        if code == 403:
            return Forbidden(message=text, code=code, value=val)
        if code == 404:
            return NotFound(message=text, code=code, value=val)
        if code >= 500:
            return InternalServerError(message=text, code=code, value=val)
        return RPCError(message=text, code=code, value=val)


class BadRequest(RPCError):
    CODE: int = 400
    NAME: str = "BAD_REQUEST"


class Unauthorized(RPCError):
    CODE: int = 401
    NAME: str = "UNAUTHORIZED"


class Forbidden(RPCError):
    CODE: int = 403
    NAME: str = "FORBIDDEN"


class NotFound(RPCError):
    CODE: int = 404
    NAME: str = "NOT_FOUND"


class FloodWait(RPCError):
    CODE: int = 420
    NAME: str = "FLOOD_WAIT"

    def __init__(self, message: str = "", code: int = 420, value: int = 1) -> None:
        super().__init__(message=message, code=code, value=value)


class InternalServerError(RPCError):
    CODE: int = 500
    NAME: str = "INTERNAL_SERVER_ERROR"


class SecurityError(Exception):
    pass


class ConnectionError(Exception):
    pass
