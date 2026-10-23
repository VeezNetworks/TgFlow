class TgFlowError(Exception):
    pass


class RPCError(TgFlowError):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")


class FloodWait(RPCError):
    def __init__(self, seconds: int):
        self.seconds = seconds
        super().__init__(420, f"FLOOD_WAIT_{seconds}")


class Unauthorized(RPCError):
    def __init__(self, message: str = "SESSION_PASSWORD_NEEDED"):
        super().__init__(401, message)


class BadMessageError(TgFlowError):
    def __init__(self, error_code: int):
        self.error_code = error_code
        super().__init__(f"Bad server message error code: {error_code}")


class ConnectionClosed(TgFlowError):
    pass
