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

        if name in ERROR_MAP:
            exc_cls = ERROR_MAP[name]
            return exc_cls(message=text, code=code, value=val)

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
        if code == 406:
            return NotAcceptable(message=text, code=code, value=val)
        if code >= 500:
            return InternalServerError(message=text, code=code, value=val)
        return RPCError(message=text, code=code, value=val)


class BadRequest(RPCError):
    CODE: int = 400
    NAME: str = "BAD_REQUEST"


class MessageNotModified(BadRequest):
    NAME: str = "MESSAGE_NOT_MODIFIED"


class MessageEmpty(BadRequest):
    NAME: str = "MESSAGE_EMPTY"


class MessageTooLong(BadRequest):
    NAME: str = "MESSAGE_TOO_LONG"


class MediaEmpty(BadRequest):
    NAME: str = "MEDIA_EMPTY"


class MediaInvalid(BadRequest):
    NAME: str = "MEDIA_INVALID"


class PeerIdInvalid(BadRequest):
    NAME: str = "PEER_ID_INVALID"


class ChatAdminRequired(BadRequest):
    NAME: str = "CHAT_ADMIN_REQUIRED"


class UserNotParticipant(BadRequest):
    NAME: str = "USER_NOT_PARTICIPANT"


class ChannelPrivate(BadRequest):
    NAME: str = "CHANNEL_PRIVATE"


class ChannelInvalid(BadRequest):
    NAME: str = "CHANNEL_INVALID"


class UsernameInvalid(BadRequest):
    NAME: str = "USERNAME_INVALID"


class UsernameOccupied(BadRequest):
    NAME: str = "USERNAME_OCCUPIED"


class UsernameNotOccupied(BadRequest):
    NAME: str = "USERNAME_NOT_OCCUPIED"


class PhoneNumberInvalid(BadRequest):
    NAME: str = "PHONE_NUMBER_INVALID"


class PhoneCodeEmpty(BadRequest):
    NAME: str = "PHONE_CODE_EMPTY"


class PhoneCodeExpired(BadRequest):
    NAME: str = "PHONE_CODE_EXPIRED"


class PhoneCodeInvalid(BadRequest):
    NAME: str = "PHONE_CODE_INVALID"


class PasswordHashInvalid(BadRequest):
    NAME: str = "PASSWORD_HASH_INVALID"


class TopicClosed(BadRequest):
    NAME: str = "TOPIC_CLOSED"


class TopicDeleted(BadRequest):
    NAME: str = "TOPIC_DELETED"


class PremiumAccountRequired(BadRequest):
    NAME: str = "PREMIUM_ACCOUNT_REQUIRED"


class BoostsEmpty(BadRequest):
    NAME: str = "BOOSTS_EMPTY"


class StoryNotModified(BadRequest):
    NAME: str = "STORY_NOT_MODIFIED"


class Unauthorized(RPCError):
    CODE: int = 401
    NAME: str = "UNAUTHORIZED"


class AuthKeyUnregistered(Unauthorized):
    NAME: str = "AUTH_KEY_UNREGISTERED"


class AuthKeyInvalid(Unauthorized):
    NAME: str = "AUTH_KEY_INVALID"


class UserDeactivated(Unauthorized):
    NAME: str = "USER_DEACTIVATED"


class SessionRevoked(Unauthorized):
    NAME: str = "SESSION_REVOKED"


class SessionExpired(Unauthorized):
    NAME: str = "SESSION_EXPIRED"


class SessionPasswordNeeded(Unauthorized):
    NAME: str = "SESSION_PASSWORD_NEEDED"


class Forbidden(RPCError):
    CODE: int = 403
    NAME: str = "FORBIDDEN"


class ChatWriteForbidden(Forbidden):
    NAME: str = "CHAT_WRITE_FORBIDDEN"


class ChatSendMediaForbidden(Forbidden):
    NAME: str = "CHAT_SEND_MEDIA_FORBIDDEN"


class ChatSendStickersForbidden(Forbidden):
    NAME: str = "CHAT_SEND_STICKERS_FORBIDDEN"


class ChatSendPollsForbidden(Forbidden):
    NAME: str = "CHAT_SEND_POLLS_FORBIDDEN"


class UserRestricted(Forbidden):
    NAME: str = "USER_RESTRICTED"


class UserBannedInChannel(Forbidden):
    NAME: str = "USER_BANNED_IN_CHANNEL"


class VoiceMessagesForbidden(Forbidden):
    NAME: str = "VOICE_MESSAGES_FORBIDDEN"


class NotFound(RPCError):
    CODE: int = 404
    NAME: str = "NOT_FOUND"


class NotAcceptable(RPCError):
    CODE: int = 406
    NAME: str = "NOT_ACCEPTABLE"


class AuthKeyDuplicated(NotAcceptable):
    NAME: str = "AUTH_KEY_DUPLICATED"


class FilerefUpgradeNeeded(NotAcceptable):
    NAME: str = "FILEREF_UPGRADE_NEEDED"


class FloodWait(RPCError):
    CODE: int = 420
    NAME: str = "FLOOD_WAIT"

    def __init__(self, message: str = "", code: int = 420, value: int = 1) -> None:
        super().__init__(message=message, code=code, value=value)
        self.seconds = value


class SlowmodeWait(FloodWait):
    NAME: str = "SLOWMODE_WAIT"


class FloodPremiumWait(FloodWait):
    NAME: str = "FLOOD_PREMIUM_WAIT"


class InternalServerError(RPCError):
    CODE: int = 500
    NAME: str = "INTERNAL_SERVER_ERROR"


class RpcCallFail(InternalServerError):
    NAME: str = "RPC_CALL_FAIL"


class InterDcCallError(InternalServerError):
    NAME: str = "INTERDC_CALL_ERROR"


class SecurityError(Exception):
    pass


class ConnectionError(Exception):
    pass


ERROR_MAP: dict[str, type[RPCError]] = {
    "MESSAGE_NOT_MODIFIED": MessageNotModified,
    "MESSAGE_EMPTY": MessageEmpty,
    "MESSAGE_TOO_LONG": MessageTooLong,
    "MEDIA_EMPTY": MediaEmpty,
    "MEDIA_INVALID": MediaInvalid,
    "PEER_ID_INVALID": PeerIdInvalid,
    "CHAT_ADMIN_REQUIRED": ChatAdminRequired,
    "USER_NOT_PARTICIPANT": UserNotParticipant,
    "CHANNEL_PRIVATE": ChannelPrivate,
    "CHANNEL_INVALID": ChannelInvalid,
    "USERNAME_INVALID": UsernameInvalid,
    "USERNAME_OCCUPIED": UsernameOccupied,
    "USERNAME_NOT_OCCUPIED": UsernameNotOccupied,
    "PHONE_NUMBER_INVALID": PhoneNumberInvalid,
    "PHONE_CODE_EMPTY": PhoneCodeEmpty,
    "PHONE_CODE_EXPIRED": PhoneCodeExpired,
    "PHONE_CODE_INVALID": PhoneCodeInvalid,
    "PASSWORD_HASH_INVALID": PasswordHashInvalid,
    "TOPIC_CLOSED": TopicClosed,
    "TOPIC_DELETED": TopicDeleted,
    "PREMIUM_ACCOUNT_REQUIRED": PremiumAccountRequired,
    "BOOSTS_EMPTY": BoostsEmpty,
    "STORY_NOT_MODIFIED": StoryNotModified,
    "AUTH_KEY_UNREGISTERED": AuthKeyUnregistered,
    "AUTH_KEY_INVALID": AuthKeyInvalid,
    "USER_DEACTIVATED": UserDeactivated,
    "SESSION_REVOKED": SessionRevoked,
    "SESSION_EXPIRED": SessionExpired,
    "SESSION_PASSWORD_NEEDED": SessionPasswordNeeded,
    "CHAT_WRITE_FORBIDDEN": ChatWriteForbidden,
    "CHAT_SEND_MEDIA_FORBIDDEN": ChatSendMediaForbidden,
    "CHAT_SEND_STICKERS_FORBIDDEN": ChatSendStickersForbidden,
    "CHAT_SEND_POLLS_FORBIDDEN": ChatSendPollsForbidden,
    "USER_RESTRICTED": UserRestricted,
    "USER_BANNED_IN_CHANNEL": UserBannedInChannel,
    "VOICE_MESSAGES_FORBIDDEN": VoiceMessagesForbidden,
    "AUTH_KEY_DUPLICATED": AuthKeyDuplicated,
    "FILEREF_UPGRADE_NEEDED": FilerefUpgradeNeeded,
    "FLOOD_WAIT": FloodWait,
    "SLOWMODE_WAIT": SlowmodeWait,
    "FLOOD_PREMIUM_WAIT": FloodPremiumWait,
    "RPC_CALL_FAIL": RpcCallFail,
}
