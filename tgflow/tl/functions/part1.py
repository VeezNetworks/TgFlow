from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class InvokeAfterMsg(TLRequest):
    ID: int = 0xcb9f372d

    def __init__(self, X: Any = None, msg_id: Any = None) -> None:
        self.X = X
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_int64(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeAfterMsg':
        X = reader.read_object()
        msg_id = reader.read_int64()
        return cls(X=X, msg_id=msg_id)


@register_tl
class InvokeAfterMsgs(TLRequest):
    ID: int = 0x3dc4b4f0

    def __init__(self, X: Any = None, msg_ids: Any = None) -> None:
        self.X = X
        self.msg_ids = msg_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_vector(self.msg_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeAfterMsgs':
        X = reader.read_object()
        msg_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(X=X, msg_ids=msg_ids)


@register_tl
class InitConnection(TLRequest):
    ID: int = 0xc1cd5ea9

    def __init__(self, proxy: Any = None, params: Any = None, X: Any = None, api_id: Any = None, device_model: Any = None, system_version: Any = None, app_version: Any = None, system_lang_code: Any = None, lang_pack: Any = None, lang_code: Any = None) -> None:
        self.proxy = proxy
        self.params = params
        self.X = X
        self.api_id = api_id
        self.device_model = device_model
        self.system_version = system_version
        self.app_version = app_version
        self.system_lang_code = system_lang_code
        self.lang_pack = lang_pack
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.proxy is not None:
            flags |= (1 << 0)
        if self.params is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_int32(self.api_id or 0)
        writer.write_string(self.device_model or '')
        writer.write_string(self.system_version or '')
        writer.write_string(self.app_version or '')
        writer.write_string(self.system_lang_code or '')
        writer.write_string(self.lang_pack or '')
        writer.write_string(self.lang_code or '')
        if self.proxy is not None:
            if self.proxy is not None and hasattr(self.proxy, 'write'): self.proxy.write(writer)
        if self.params is not None:
            if self.params is not None and hasattr(self.params, 'write'): self.params.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InitConnection':
        flags = reader.read_uint32()
        X = reader.read_object()
        api_id = reader.read_int32()
        device_model = reader.read_string()
        system_version = reader.read_string()
        app_version = reader.read_string()
        system_lang_code = reader.read_string()
        lang_pack = reader.read_string()
        lang_code = reader.read_string()
        proxy = reader.read_object() if (flags & (1 << 0)) else None
        params = reader.read_object() if (flags & (1 << 1)) else None
        return cls(X=X, api_id=api_id, device_model=device_model, system_version=system_version, app_version=app_version, system_lang_code=system_lang_code, lang_pack=lang_pack, lang_code=lang_code, proxy=proxy, params=params)


@register_tl
class InvokeWithLayer(TLRequest):
    ID: int = 0xda9b0d0d

    def __init__(self, X: Any = None, layer: Any = None) -> None:
        self.X = X
        self.layer = layer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_int32(self.layer or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithLayer':
        X = reader.read_object()
        layer = reader.read_int32()
        return cls(X=X, layer=layer)


@register_tl
class InvokeWithoutUpdates(TLRequest):
    ID: int = 0xbf9459b7

    def __init__(self, X: Any = None) -> None:
        self.X = X

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithoutUpdates':
        X = reader.read_object()
        return cls(X=X)


@register_tl
class InvokeWithMessagesRange(TLRequest):
    ID: int = 0x365275f2

    def __init__(self, X: Any = None, range: Any = None) -> None:
        self.X = X
        self.range = range

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        if self.range is not None and hasattr(self.range, 'write'): self.range.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithMessagesRange':
        X = reader.read_object()
        range = reader.read_object()
        return cls(X=X, range=range)


@register_tl
class InvokeWithTakeout(TLRequest):
    ID: int = 0xaca9fd2e

    def __init__(self, X: Any = None, takeout_id: Any = None) -> None:
        self.X = X
        self.takeout_id = takeout_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_int64(self.takeout_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithTakeout':
        X = reader.read_object()
        takeout_id = reader.read_int64()
        return cls(X=X, takeout_id=takeout_id)


@register_tl
class InvokeWithBusinessConnection(TLRequest):
    ID: int = 0xdd289f8e

    def __init__(self, X: Any = None, connection_id: Any = None) -> None:
        self.X = X
        self.connection_id = connection_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_string(self.connection_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithBusinessConnection':
        X = reader.read_object()
        connection_id = reader.read_string()
        return cls(X=X, connection_id=connection_id)


@register_tl
class InvokeWithGooglePlayIntegrity(TLRequest):
    ID: int = 0x1df92984

    def __init__(self, X: Any = None, nonce: Any = None, token: Any = None) -> None:
        self.X = X
        self.nonce = nonce
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_string(self.nonce or '')
        writer.write_string(self.token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithGooglePlayIntegrity':
        X = reader.read_object()
        nonce = reader.read_string()
        token = reader.read_string()
        return cls(X=X, nonce=nonce, token=token)


@register_tl
class InvokeWithApnsSecret(TLRequest):
    ID: int = 0xdae54f8

    def __init__(self, X: Any = None, nonce: Any = None, secret: Any = None) -> None:
        self.X = X
        self.nonce = nonce
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_string(self.nonce or '')
        writer.write_string(self.secret or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithApnsSecret':
        X = reader.read_object()
        nonce = reader.read_string()
        secret = reader.read_string()
        return cls(X=X, nonce=nonce, secret=secret)


@register_tl
class InvokeWithReCaptcha(TLRequest):
    ID: int = 0xadbb0f94

    def __init__(self, X: Any = None, token: Any = None) -> None:
        self.X = X
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.X is not None and hasattr(self.X, 'write'): self.X.write(writer)
        writer.write_string(self.token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InvokeWithReCaptcha':
        X = reader.read_object()
        token = reader.read_string()
        return cls(X=X, token=token)


@register_tl
class AuthSendCode(TLRequest):
    ID: int = 0xa677244f

    def __init__(self, phone_number: Any = None, api_id: Any = None, api_hash: Any = None, settings: Any = None) -> None:
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_int32(self.api_id or 0)
        writer.write_string(self.api_hash or '')
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSendCode':
        phone_number = reader.read_string()
        api_id = reader.read_int32()
        api_hash = reader.read_string()
        settings = reader.read_object()
        return cls(phone_number=phone_number, api_id=api_id, api_hash=api_hash, settings=settings)


@register_tl
class AuthSignUp(TLRequest):
    ID: int = 0xaac7b717

    def __init__(self, no_joined_notifications: bool = False, phone_number: Any = None, phone_code_hash: Any = None, first_name: Any = None, last_name: Any = None) -> None:
        self.no_joined_notifications = no_joined_notifications
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.first_name = first_name
        self.last_name = last_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_joined_notifications:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSignUp':
        flags = reader.read_uint32()
        no_joined_notifications = bool(flags & (1 << 0))
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        return cls(no_joined_notifications=no_joined_notifications, phone_number=phone_number, phone_code_hash=phone_code_hash, first_name=first_name, last_name=last_name)


@register_tl
class AuthSignIn(TLRequest):
    ID: int = 0x8d52a951

    def __init__(self, phone_code: Any = None, email_verification: Any = None, phone_number: Any = None, phone_code_hash: Any = None) -> None:
        self.phone_code = phone_code
        self.email_verification = email_verification
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.phone_code is not None:
            flags |= (1 << 0)
        if self.email_verification is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        if self.phone_code is not None:
            writer.write_string(self.phone_code or '')
        if self.email_verification is not None:
            if self.email_verification is not None and hasattr(self.email_verification, 'write'): self.email_verification.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSignIn':
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string() if (flags & (1 << 0)) else None
        email_verification = reader.read_object() if (flags & (1 << 1)) else None
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code, email_verification=email_verification)


@register_tl
class AuthLogOut(TLRequest):
    ID: int = 0x3e72ba19

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthLogOut':
        return cls()


@register_tl
class AuthResetAuthorizations(TLRequest):
    ID: int = 0x9fab0d1a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthResetAuthorizations':
        return cls()


@register_tl
class AuthExportAuthorization(TLRequest):
    ID: int = 0xe5bfffcd

    def __init__(self, dc_id: Any = None) -> None:
        self.dc_id = dc_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthExportAuthorization':
        dc_id = reader.read_int32()
        return cls(dc_id=dc_id)


@register_tl
class AuthImportAuthorization(TLRequest):
    ID: int = 0xa57a7dad

    def __init__(self, id: Any = None, bytes: Any = None) -> None:
        self.id = id
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthImportAuthorization':
        id = reader.read_int64()
        bytes = reader.read_bytes()
        return cls(id=id, bytes=bytes)


@register_tl
class AuthBindTempAuthKey(TLRequest):
    ID: int = 0xcdd42a05

    def __init__(self, perm_auth_key_id: Any = None, nonce: Any = None, expires_at: Any = None, encrypted_message: Any = None) -> None:
        self.perm_auth_key_id = perm_auth_key_id
        self.nonce = nonce
        self.expires_at = expires_at
        self.encrypted_message = encrypted_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.perm_auth_key_id or 0)
        writer.write_int64(self.nonce or 0)
        writer.write_int32(self.expires_at or 0)
        writer.write_bytes(self.encrypted_message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthBindTempAuthKey':
        perm_auth_key_id = reader.read_int64()
        nonce = reader.read_int64()
        expires_at = reader.read_int32()
        encrypted_message = reader.read_bytes()
        return cls(perm_auth_key_id=perm_auth_key_id, nonce=nonce, expires_at=expires_at, encrypted_message=encrypted_message)


@register_tl
class AuthImportBotAuthorization(TLRequest):
    ID: int = 0x67a3ff2c

    def __init__(self, flags: Any = None, api_id: Any = None, api_hash: Any = None, bot_auth_token: Any = None) -> None:
        self.flags = flags
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_auth_token = bot_auth_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.flags or 0)
        writer.write_int32(self.api_id or 0)
        writer.write_string(self.api_hash or '')
        writer.write_string(self.bot_auth_token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthImportBotAuthorization':
        flags = reader.read_int32()
        api_id = reader.read_int32()
        api_hash = reader.read_string()
        bot_auth_token = reader.read_string()
        return cls(flags=flags, api_id=api_id, api_hash=api_hash, bot_auth_token=bot_auth_token)


@register_tl
class AuthCheckPassword(TLRequest):
    ID: int = 0xd18b4d16

    def __init__(self, password: Any = None) -> None:
        self.password = password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCheckPassword':
        password = reader.read_object()
        return cls(password=password)


@register_tl
class AuthRequestPasswordRecovery(TLRequest):
    ID: int = 0xd897bc66

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthRequestPasswordRecovery':
        return cls()


@register_tl
class AuthRecoverPassword(TLRequest):
    ID: int = 0x37096c70

    def __init__(self, new_settings: Any = None, code: Any = None) -> None:
        self.new_settings = new_settings
        self.code = code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.new_settings is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.code or '')
        if self.new_settings is not None:
            if self.new_settings is not None and hasattr(self.new_settings, 'write'): self.new_settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthRecoverPassword':
        flags = reader.read_uint32()
        code = reader.read_string()
        new_settings = reader.read_object() if (flags & (1 << 0)) else None
        return cls(code=code, new_settings=new_settings)


@register_tl
class AuthResendCode(TLRequest):
    ID: int = 0xcae47523

    def __init__(self, reason: Any = None, phone_number: Any = None, phone_code_hash: Any = None) -> None:
        self.reason = reason
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reason is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        if self.reason is not None:
            writer.write_string(self.reason or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthResendCode':
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        reason = reader.read_string() if (flags & (1 << 0)) else None
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, reason=reason)


@register_tl
class AuthCancelCode(TLRequest):
    ID: int = 0x1f040578

    def __init__(self, phone_number: Any = None, phone_code_hash: Any = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCancelCode':
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash)


@register_tl
class AuthDropTempAuthKeys(TLRequest):
    ID: int = 0x8e48a188

    def __init__(self, except_auth_keys: Any = None) -> None:
        self.except_auth_keys = except_auth_keys

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.except_auth_keys or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthDropTempAuthKeys':
        except_auth_keys = reader.read_vector(lambda r: r.read_int64())
        return cls(except_auth_keys=except_auth_keys)


@register_tl
class AuthExportLoginToken(TLRequest):
    ID: int = 0xb7e085fe

    def __init__(self, api_id: Any = None, api_hash: Any = None, except_ids: Any = None) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.except_ids = except_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.api_id or 0)
        writer.write_string(self.api_hash or '')
        writer.write_vector(self.except_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthExportLoginToken':
        api_id = reader.read_int32()
        api_hash = reader.read_string()
        except_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(api_id=api_id, api_hash=api_hash, except_ids=except_ids)


@register_tl
class AuthImportLoginToken(TLRequest):
    ID: int = 0x95ac5ce4

    def __init__(self, token: Any = None) -> None:
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.token or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthImportLoginToken':
        token = reader.read_bytes()
        return cls(token=token)


@register_tl
class AuthAcceptLoginToken(TLRequest):
    ID: int = 0xe894ad4d

    def __init__(self, token: Any = None) -> None:
        self.token = token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.token or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthAcceptLoginToken':
        token = reader.read_bytes()
        return cls(token=token)


@register_tl
class AuthCheckRecoveryPassword(TLRequest):
    ID: int = 0xd36bf79

    def __init__(self, code: Any = None) -> None:
        self.code = code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCheckRecoveryPassword':
        code = reader.read_string()
        return cls(code=code)


@register_tl
class AuthImportWebTokenAuthorization(TLRequest):
    ID: int = 0x2db873a9

    def __init__(self, api_id: Any = None, api_hash: Any = None, web_auth_token: Any = None) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.web_auth_token = web_auth_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.api_id or 0)
        writer.write_string(self.api_hash or '')
        writer.write_string(self.web_auth_token or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthImportWebTokenAuthorization':
        api_id = reader.read_int32()
        api_hash = reader.read_string()
        web_auth_token = reader.read_string()
        return cls(api_id=api_id, api_hash=api_hash, web_auth_token=web_auth_token)


@register_tl
class AuthRequestFirebaseSms(TLRequest):
    ID: int = 0x8e39261e

    def __init__(self, safety_net_token: Any = None, play_integrity_token: Any = None, ios_push_secret: Any = None, phone_number: Any = None, phone_code_hash: Any = None) -> None:
        self.safety_net_token = safety_net_token
        self.play_integrity_token = play_integrity_token
        self.ios_push_secret = ios_push_secret
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.safety_net_token is not None:
            flags |= (1 << 0)
        if self.play_integrity_token is not None:
            flags |= (1 << 2)
        if self.ios_push_secret is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        if self.safety_net_token is not None:
            writer.write_string(self.safety_net_token or '')
        if self.play_integrity_token is not None:
            writer.write_string(self.play_integrity_token or '')
        if self.ios_push_secret is not None:
            writer.write_string(self.ios_push_secret or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthRequestFirebaseSms':
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        safety_net_token = reader.read_string() if (flags & (1 << 0)) else None
        play_integrity_token = reader.read_string() if (flags & (1 << 2)) else None
        ios_push_secret = reader.read_string() if (flags & (1 << 1)) else None
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, safety_net_token=safety_net_token, play_integrity_token=play_integrity_token, ios_push_secret=ios_push_secret)


@register_tl
class AuthResetLoginEmail(TLRequest):
    ID: int = 0x7e960193

    def __init__(self, phone_number: Any = None, phone_code_hash: Any = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthResetLoginEmail':
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash)


@register_tl
class AuthReportMissingCode(TLRequest):
    ID: int = 0xcb9deff6

    def __init__(self, phone_number: Any = None, phone_code_hash: Any = None, mnc: Any = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.mnc = mnc

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        writer.write_string(self.mnc or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthReportMissingCode':
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        mnc = reader.read_string()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, mnc=mnc)


@register_tl
class AuthCheckPaidAuth(TLRequest):
    ID: int = 0x56e59f9c

    def __init__(self, phone_number: Any = None, phone_code_hash: Any = None, form_id: Any = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.form_id = form_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        writer.write_int64(self.form_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthCheckPaidAuth':
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        form_id = reader.read_int64()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, form_id=form_id)


@register_tl
class AuthInitPasskeyLogin(TLRequest):
    ID: int = 0x518ad0b7

    def __init__(self, api_id: Any = None, api_hash: Any = None) -> None:
        self.api_id = api_id
        self.api_hash = api_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.api_id or 0)
        writer.write_string(self.api_hash or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthInitPasskeyLogin':
        api_id = reader.read_int32()
        api_hash = reader.read_string()
        return cls(api_id=api_id, api_hash=api_hash)


@register_tl
class AuthFinishPasskeyLogin(TLRequest):
    ID: int = 0x9857ad07

    def __init__(self, from_dc_id: Any = None, from_auth_key_id: Any = None, credential: Any = None) -> None:
        self.from_dc_id = from_dc_id
        self.from_auth_key_id = from_auth_key_id
        self.credential = credential

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.from_dc_id is not None:
            flags |= (1 << 0)
        if self.from_auth_key_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.credential is not None and hasattr(self.credential, 'write'): self.credential.write(writer)
        if self.from_dc_id is not None:
            writer.write_int32(self.from_dc_id or 0)
        if self.from_auth_key_id is not None:
            writer.write_int64(self.from_auth_key_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthFinishPasskeyLogin':
        flags = reader.read_uint32()
        credential = reader.read_object()
        from_dc_id = reader.read_int32() if (flags & (1 << 0)) else None
        from_auth_key_id = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(credential=credential, from_dc_id=from_dc_id, from_auth_key_id=from_auth_key_id)


@register_tl
class AccountRegisterDevice(TLRequest):
    ID: int = 0xec86017a

    def __init__(self, no_muted: bool = False, token_type: Any = None, token: Any = None, app_sandbox: Any = None, secret: Any = None, other_uids: Any = None) -> None:
        self.no_muted = no_muted
        self.token_type = token_type
        self.token = token
        self.app_sandbox = app_sandbox
        self.secret = secret
        self.other_uids = other_uids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_muted:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.token_type or 0)
        writer.write_string(self.token or '')
        writer.write_bool(bool(self.app_sandbox))
        writer.write_bytes(self.secret or b'')
        writer.write_vector(self.other_uids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountRegisterDevice':
        flags = reader.read_uint32()
        no_muted = bool(flags & (1 << 0))
        token_type = reader.read_int32()
        token = reader.read_string()
        app_sandbox = reader.read_bool()
        secret = reader.read_bytes()
        other_uids = reader.read_vector(lambda r: r.read_int64())
        return cls(no_muted=no_muted, token_type=token_type, token=token, app_sandbox=app_sandbox, secret=secret, other_uids=other_uids)


@register_tl
class AccountUnregisterDevice(TLRequest):
    ID: int = 0x6a0d3206

    def __init__(self, token_type: Any = None, token: Any = None, other_uids: Any = None) -> None:
        self.token_type = token_type
        self.token = token
        self.other_uids = other_uids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.token_type or 0)
        writer.write_string(self.token or '')
        writer.write_vector(self.other_uids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUnregisterDevice':
        token_type = reader.read_int32()
        token = reader.read_string()
        other_uids = reader.read_vector(lambda r: r.read_int64())
        return cls(token_type=token_type, token=token, other_uids=other_uids)


@register_tl
class AccountUpdateNotifySettings(TLRequest):
    ID: int = 0x84be5b93

    def __init__(self, peer: Any = None, settings: Any = None) -> None:
        self.peer = peer
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateNotifySettings':
        peer = reader.read_object()
        settings = reader.read_object()
        return cls(peer=peer, settings=settings)


@register_tl
class AccountGetNotifySettings(TLRequest):
    ID: int = 0x12b3ad31

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetNotifySettings':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class AccountResetNotifySettings(TLRequest):
    ID: int = 0xdb7e1747

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetNotifySettings':
        return cls()


@register_tl
class AccountUpdateProfile(TLRequest):
    ID: int = 0x78515775

    def __init__(self, first_name: Any = None, last_name: Any = None, about: Any = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.about = about

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.first_name is not None:
            flags |= (1 << 0)
        if self.last_name is not None:
            flags |= (1 << 1)
        if self.about is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.first_name is not None:
            writer.write_string(self.first_name or '')
        if self.last_name is not None:
            writer.write_string(self.last_name or '')
        if self.about is not None:
            writer.write_string(self.about or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateProfile':
        flags = reader.read_uint32()
        first_name = reader.read_string() if (flags & (1 << 0)) else None
        last_name = reader.read_string() if (flags & (1 << 1)) else None
        about = reader.read_string() if (flags & (1 << 2)) else None
        return cls(first_name=first_name, last_name=last_name, about=about)


@register_tl
class AccountUpdateStatus(TLRequest):
    ID: int = 0x6628562c

    def __init__(self, offline: Any = None) -> None:
        self.offline = offline

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.offline))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateStatus':
        offline = reader.read_bool()
        return cls(offline=offline)


@register_tl
class AccountGetWallPapers(TLRequest):
    ID: int = 0x7967d36

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetWallPapers':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountReportPeer(TLRequest):
    ID: int = 0xc5ba3d86

    def __init__(self, peer: Any = None, reason: Any = None, message: Any = None) -> None:
        self.peer = peer
        self.reason = reason
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.reason is not None and hasattr(self.reason, 'write'): self.reason.write(writer)
        writer.write_string(self.message or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountReportPeer':
        peer = reader.read_object()
        reason = reader.read_object()
        message = reader.read_string()
        return cls(peer=peer, reason=reason, message=message)


@register_tl
class AccountCheckUsername(TLRequest):
    ID: int = 0x2714d86c

    def __init__(self, username: Any = None) -> None:
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountCheckUsername':
        username = reader.read_string()
        return cls(username=username)


@register_tl
class AccountUpdateUsername(TLRequest):
    ID: int = 0x3e0bdd7c

    def __init__(self, username: Any = None) -> None:
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateUsername':
        username = reader.read_string()
        return cls(username=username)


@register_tl
class AccountGetPrivacy(TLRequest):
    ID: int = 0xdadbc950

    def __init__(self, key: Any = None) -> None:
        self.key = key

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.key is not None and hasattr(self.key, 'write'): self.key.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetPrivacy':
        key = reader.read_object()
        return cls(key=key)


@register_tl
class AccountSetPrivacy(TLRequest):
    ID: int = 0xc9f81ce8

    def __init__(self, key: Any = None, rules: Any = None) -> None:
        self.key = key
        self.rules = rules

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.key is not None and hasattr(self.key, 'write'): self.key.write(writer)
        writer.write_vector(self.rules or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetPrivacy':
        key = reader.read_object()
        rules = reader.read_vector(lambda r: reader.read_object())
        return cls(key=key, rules=rules)


@register_tl
class AccountDeleteAccount(TLRequest):
    ID: int = 0xa2c0cf74

    def __init__(self, password: Any = None, reason: Any = None) -> None:
        self.password = password
        self.reason = reason

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.password is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.reason or '')
        if self.password is not None:
            if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDeleteAccount':
        flags = reader.read_uint32()
        reason = reader.read_string()
        password = reader.read_object() if (flags & (1 << 0)) else None
        return cls(reason=reason, password=password)


@register_tl
class AccountGetAccountTTL(TLRequest):
    ID: int = 0x8fc711d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetAccountTTL':
        return cls()


@register_tl
class AccountSetAccountTTL(TLRequest):
    ID: int = 0x2442485e

    def __init__(self, ttl: Any = None) -> None:
        self.ttl = ttl

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.ttl is not None and hasattr(self.ttl, 'write'): self.ttl.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetAccountTTL':
        ttl = reader.read_object()
        return cls(ttl=ttl)


@register_tl
class AccountSendChangePhoneCode(TLRequest):
    ID: int = 0x82574ae5

    def __init__(self, phone_number: Any = None, settings: Any = None) -> None:
        self.phone_number = phone_number
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSendChangePhoneCode':
        phone_number = reader.read_string()
        settings = reader.read_object()
        return cls(phone_number=phone_number, settings=settings)


@register_tl
class AccountChangePhone(TLRequest):
    ID: int = 0x70c32edb

    def __init__(self, phone_number: Any = None, phone_code_hash: Any = None, phone_code: Any = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        writer.write_string(self.phone_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountChangePhone':
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code)


@register_tl
class AccountUpdateDeviceLocked(TLRequest):
    ID: int = 0x38df3532

    def __init__(self, period: Any = None) -> None:
        self.period = period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateDeviceLocked':
        period = reader.read_int32()
        return cls(period=period)


@register_tl
class AccountGetAuthorizations(TLRequest):
    ID: int = 0xe320c158

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetAuthorizations':
        return cls()


@register_tl
class AccountResetAuthorization(TLRequest):
    ID: int = 0xdf77f3bc

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetAuthorization':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetPassword(TLRequest):
    ID: int = 0x548a30f5

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetPassword':
        return cls()


@register_tl
class AccountGetPasswordSettings(TLRequest):
    ID: int = 0x9cd4eaf9

    def __init__(self, password: Any = None) -> None:
        self.password = password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetPasswordSettings':
        password = reader.read_object()
        return cls(password=password)


@register_tl
class AccountUpdatePasswordSettings(TLRequest):
    ID: int = 0xa59b102f

    def __init__(self, password: Any = None, new_settings: Any = None) -> None:
        self.password = password
        self.new_settings = new_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)
        if self.new_settings is not None and hasattr(self.new_settings, 'write'): self.new_settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdatePasswordSettings':
        password = reader.read_object()
        new_settings = reader.read_object()
        return cls(password=password, new_settings=new_settings)


@register_tl
class AccountSendConfirmPhoneCode(TLRequest):
    ID: int = 0x1b3faa88

    def __init__(self, hash: Any = None, settings: Any = None) -> None:
        self.hash = hash
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.hash or '')
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSendConfirmPhoneCode':
        hash = reader.read_string()
        settings = reader.read_object()
        return cls(hash=hash, settings=settings)


@register_tl
class AccountConfirmPhone(TLRequest):
    ID: int = 0x5f2178c3

    def __init__(self, phone_code_hash: Any = None, phone_code: Any = None) -> None:
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_code_hash or '')
        writer.write_string(self.phone_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountConfirmPhone':
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string()
        return cls(phone_code_hash=phone_code_hash, phone_code=phone_code)


@register_tl
class AccountGetTmpPassword(TLRequest):
    ID: int = 0x449e0b51

    def __init__(self, password: Any = None, period: Any = None) -> None:
        self.password = password
        self.period = period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)
        writer.write_int32(self.period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetTmpPassword':
        password = reader.read_object()
        period = reader.read_int32()
        return cls(password=password, period=period)


@register_tl
class AccountGetWebAuthorizations(TLRequest):
    ID: int = 0x182e6d6f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetWebAuthorizations':
        return cls()


@register_tl
class AccountResetWebAuthorization(TLRequest):
    ID: int = 0x2d01b9ef

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetWebAuthorization':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountResetWebAuthorizations(TLRequest):
    ID: int = 0x682d2594

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetWebAuthorizations':
        return cls()


@register_tl
class AccountGetAllSecureValues(TLRequest):
    ID: int = 0xb288bc7d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetAllSecureValues':
        return cls()


@register_tl
class AccountGetSecureValue(TLRequest):
    ID: int = 0x73665bc2

    def __init__(self, types: Any = None) -> None:
        self.types = types

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetSecureValue':
        types = reader.read_vector(lambda r: reader.read_object())
        return cls(types=types)


@register_tl
class AccountSaveSecureValue(TLRequest):
    ID: int = 0x899fe31d

    def __init__(self, value: Any = None, secure_secret_id: Any = None) -> None:
        self.value = value
        self.secure_secret_id = secure_secret_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.value is not None and hasattr(self.value, 'write'): self.value.write(writer)
        writer.write_int64(self.secure_secret_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSaveSecureValue':
        value = reader.read_object()
        secure_secret_id = reader.read_int64()
        return cls(value=value, secure_secret_id=secure_secret_id)


@register_tl
class AccountDeleteSecureValue(TLRequest):
    ID: int = 0xb880bc4b

    def __init__(self, types: Any = None) -> None:
        self.types = types

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDeleteSecureValue':
        types = reader.read_vector(lambda r: reader.read_object())
        return cls(types=types)


@register_tl
class AccountGetAuthorizationForm(TLRequest):
    ID: int = 0xa929597a

    def __init__(self, bot_id: Any = None, scope: Any = None, public_key: Any = None) -> None:
        self.bot_id = bot_id
        self.scope = scope
        self.public_key = public_key

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bot_id or 0)
        writer.write_string(self.scope or '')
        writer.write_string(self.public_key or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetAuthorizationForm':
        bot_id = reader.read_int64()
        scope = reader.read_string()
        public_key = reader.read_string()
        return cls(bot_id=bot_id, scope=scope, public_key=public_key)


@register_tl
class AccountAcceptAuthorization(TLRequest):
    ID: int = 0xf3ed4c73

    def __init__(self, bot_id: Any = None, scope: Any = None, public_key: Any = None, value_hashes: Any = None, credentials: Any = None) -> None:
        self.bot_id = bot_id
        self.scope = scope
        self.public_key = public_key
        self.value_hashes = value_hashes
        self.credentials = credentials

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bot_id or 0)
        writer.write_string(self.scope or '')
        writer.write_string(self.public_key or '')
        writer.write_vector(self.value_hashes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.credentials is not None and hasattr(self.credentials, 'write'): self.credentials.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountAcceptAuthorization':
        bot_id = reader.read_int64()
        scope = reader.read_string()
        public_key = reader.read_string()
        value_hashes = reader.read_vector(lambda r: reader.read_object())
        credentials = reader.read_object()
        return cls(bot_id=bot_id, scope=scope, public_key=public_key, value_hashes=value_hashes, credentials=credentials)


@register_tl
class AccountSendVerifyPhoneCode(TLRequest):
    ID: int = 0xa5a356f9

    def __init__(self, phone_number: Any = None, settings: Any = None) -> None:
        self.phone_number = phone_number
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSendVerifyPhoneCode':
        phone_number = reader.read_string()
        settings = reader.read_object()
        return cls(phone_number=phone_number, settings=settings)


@register_tl
class AccountVerifyPhone(TLRequest):
    ID: int = 0x4dd3a7f6

    def __init__(self, phone_number: Any = None, phone_code_hash: Any = None, phone_code: Any = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.phone_code_hash or '')
        writer.write_string(self.phone_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountVerifyPhone':
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code)


@register_tl
class AccountSendVerifyEmailCode(TLRequest):
    ID: int = 0x98e037bb

    def __init__(self, purpose: Any = None, email: Any = None) -> None:
        self.purpose = purpose
        self.email = email

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)
        writer.write_string(self.email or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSendVerifyEmailCode':
        purpose = reader.read_object()
        email = reader.read_string()
        return cls(purpose=purpose, email=email)


@register_tl
class AccountVerifyEmail(TLRequest):
    ID: int = 0x32da4cf

    def __init__(self, purpose: Any = None, verification: Any = None) -> None:
        self.purpose = purpose
        self.verification = verification

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.purpose is not None and hasattr(self.purpose, 'write'): self.purpose.write(writer)
        if self.verification is not None and hasattr(self.verification, 'write'): self.verification.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountVerifyEmail':
        purpose = reader.read_object()
        verification = reader.read_object()
        return cls(purpose=purpose, verification=verification)


@register_tl
class AccountInitTakeoutSession(TLRequest):
    ID: int = 0x8ef3eab0

    def __init__(self, contacts: bool = False, message_users: bool = False, message_chats: bool = False, message_megagroups: bool = False, message_channels: bool = False, files: bool = False, file_max_size: Any = None) -> None:
        self.contacts = contacts
        self.message_users = message_users
        self.message_chats = message_chats
        self.message_megagroups = message_megagroups
        self.message_channels = message_channels
        self.files = files
        self.file_max_size = file_max_size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.contacts:
            flags |= (1 << 0)
        if self.message_users:
            flags |= (1 << 1)
        if self.message_chats:
            flags |= (1 << 2)
        if self.message_megagroups:
            flags |= (1 << 3)
        if self.message_channels:
            flags |= (1 << 4)
        if self.files:
            flags |= (1 << 5)
        if self.file_max_size is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.file_max_size is not None:
            writer.write_int64(self.file_max_size or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountInitTakeoutSession':
        flags = reader.read_uint32()
        contacts = bool(flags & (1 << 0))
        message_users = bool(flags & (1 << 1))
        message_chats = bool(flags & (1 << 2))
        message_megagroups = bool(flags & (1 << 3))
        message_channels = bool(flags & (1 << 4))
        files = bool(flags & (1 << 5))
        file_max_size = reader.read_int64() if (flags & (1 << 5)) else None
        return cls(contacts=contacts, message_users=message_users, message_chats=message_chats, message_megagroups=message_megagroups, message_channels=message_channels, files=files, file_max_size=file_max_size)


@register_tl
class AccountFinishTakeoutSession(TLRequest):
    ID: int = 0x1d2652ee

    def __init__(self, success: bool = False) -> None:
        self.success = success

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.success:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountFinishTakeoutSession':
        flags = reader.read_uint32()
        success = bool(flags & (1 << 0))
        return cls(success=success)


@register_tl
class AccountConfirmPasswordEmail(TLRequest):
    ID: int = 0x8fdf1920

    def __init__(self, code: Any = None) -> None:
        self.code = code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountConfirmPasswordEmail':
        code = reader.read_string()
        return cls(code=code)


@register_tl
class AccountResendPasswordEmail(TLRequest):
    ID: int = 0x7a7f2a15

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResendPasswordEmail':
        return cls()


@register_tl
class AccountCancelPasswordEmail(TLRequest):
    ID: int = 0xc1cbd5b6

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountCancelPasswordEmail':
        return cls()


@register_tl
class AccountGetContactSignUpNotification(TLRequest):
    ID: int = 0x9f07c728

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetContactSignUpNotification':
        return cls()


@register_tl
class AccountSetContactSignUpNotification(TLRequest):
    ID: int = 0xcff43f61

    def __init__(self, silent: Any = None) -> None:
        self.silent = silent

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.silent))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetContactSignUpNotification':
        silent = reader.read_bool()
        return cls(silent=silent)


@register_tl
class AccountGetNotifyExceptions(TLRequest):
    ID: int = 0x53577479

    def __init__(self, compare_sound: bool = False, compare_stories: bool = False, peer: Any = None) -> None:
        self.compare_sound = compare_sound
        self.compare_stories = compare_stories
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.compare_sound:
            flags |= (1 << 1)
        if self.compare_stories:
            flags |= (1 << 2)
        if self.peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetNotifyExceptions':
        flags = reader.read_uint32()
        compare_sound = bool(flags & (1 << 1))
        compare_stories = bool(flags & (1 << 2))
        peer = reader.read_object() if (flags & (1 << 0)) else None
        return cls(compare_sound=compare_sound, compare_stories=compare_stories, peer=peer)


@register_tl
class AccountGetWallPaper(TLRequest):
    ID: int = 0xfc8ddbea

    def __init__(self, wallpaper: Any = None) -> None:
        self.wallpaper = wallpaper

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetWallPaper':
        wallpaper = reader.read_object()
        return cls(wallpaper=wallpaper)


@register_tl
class AccountUploadWallPaper(TLRequest):
    ID: int = 0xe39a8f03

    def __init__(self, for_chat: bool = False, file: Any = None, mime_type: Any = None, settings: Any = None) -> None:
        self.for_chat = for_chat
        self.file = file
        self.mime_type = mime_type
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.for_chat:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        writer.write_string(self.mime_type or '')
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUploadWallPaper':
        flags = reader.read_uint32()
        for_chat = bool(flags & (1 << 0))
        file = reader.read_object()
        mime_type = reader.read_string()
        settings = reader.read_object()
        return cls(for_chat=for_chat, file=file, mime_type=mime_type, settings=settings)


@register_tl
class AccountSaveWallPaper(TLRequest):
    ID: int = 0x6c5a5b37

    def __init__(self, wallpaper: Any = None, unsave: Any = None, settings: Any = None) -> None:
        self.wallpaper = wallpaper
        self.unsave = unsave
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)
        writer.write_bool(bool(self.unsave))
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSaveWallPaper':
        wallpaper = reader.read_object()
        unsave = reader.read_bool()
        settings = reader.read_object()
        return cls(wallpaper=wallpaper, unsave=unsave, settings=settings)


@register_tl
class AccountInstallWallPaper(TLRequest):
    ID: int = 0xfeed5769

    def __init__(self, wallpaper: Any = None, settings: Any = None) -> None:
        self.wallpaper = wallpaper
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountInstallWallPaper':
        wallpaper = reader.read_object()
        settings = reader.read_object()
        return cls(wallpaper=wallpaper, settings=settings)


@register_tl
class AccountResetWallPapers(TLRequest):
    ID: int = 0xbb3b9804

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetWallPapers':
        return cls()


@register_tl
class AccountGetAutoDownloadSettings(TLRequest):
    ID: int = 0x56da0b3f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetAutoDownloadSettings':
        return cls()


@register_tl
class AccountSaveAutoDownloadSettings(TLRequest):
    ID: int = 0x76f36233

    def __init__(self, low: bool = False, high: bool = False, settings: Any = None) -> None:
        self.low = low
        self.high = high
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.low:
            flags |= (1 << 0)
        if self.high:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSaveAutoDownloadSettings':
        flags = reader.read_uint32()
        low = bool(flags & (1 << 0))
        high = bool(flags & (1 << 1))
        settings = reader.read_object()
        return cls(low=low, high=high, settings=settings)


@register_tl
class AccountUploadTheme(TLRequest):
    ID: int = 0x1c3db333

    def __init__(self, thumb: Any = None, file: Any = None, file_name: Any = None, mime_type: Any = None) -> None:
        self.thumb = thumb
        self.file = file
        self.file_name = file_name
        self.mime_type = mime_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.thumb is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        if self.thumb is not None:
            if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        writer.write_string(self.file_name or '')
        writer.write_string(self.mime_type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUploadTheme':
        flags = reader.read_uint32()
        file = reader.read_object()
        thumb = reader.read_object() if (flags & (1 << 0)) else None
        file_name = reader.read_string()
        mime_type = reader.read_string()
        return cls(file=file, thumb=thumb, file_name=file_name, mime_type=mime_type)


@register_tl
class AccountCreateTheme(TLRequest):
    ID: int = 0x652e4400

    def __init__(self, document: Any = None, settings: Any = None, slug: Any = None, title: Any = None) -> None:
        self.document = document
        self.settings = settings
        self.slug = slug
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.document is not None:
            flags |= (1 << 2)
        if self.settings is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_string(self.slug or '')
        writer.write_string(self.title or '')
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.settings is not None:
            writer.write_vector(self.settings or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountCreateTheme':
        flags = reader.read_uint32()
        slug = reader.read_string()
        title = reader.read_string()
        document = reader.read_object() if (flags & (1 << 2)) else None
        settings = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        return cls(slug=slug, title=title, document=document, settings=settings)


@register_tl
class AccountUpdateTheme(TLRequest):
    ID: int = 0x2bf40ccc

    def __init__(self, slug: Any = None, title: Any = None, document: Any = None, settings: Any = None, format: Any = None, theme: Any = None) -> None:
        self.slug = slug
        self.title = title
        self.document = document
        self.settings = settings
        self.format = format
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.slug is not None:
            flags |= (1 << 0)
        if self.title is not None:
            flags |= (1 << 1)
        if self.document is not None:
            flags |= (1 << 2)
        if self.settings is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_string(self.format or '')
        if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)
        if self.slug is not None:
            writer.write_string(self.slug or '')
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.settings is not None:
            writer.write_vector(self.settings or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateTheme':
        flags = reader.read_uint32()
        format = reader.read_string()
        theme = reader.read_object()
        slug = reader.read_string() if (flags & (1 << 0)) else None
        title = reader.read_string() if (flags & (1 << 1)) else None
        document = reader.read_object() if (flags & (1 << 2)) else None
        settings = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        return cls(format=format, theme=theme, slug=slug, title=title, document=document, settings=settings)


@register_tl
class AccountSaveTheme(TLRequest):
    ID: int = 0xf257106c

    def __init__(self, theme: Any = None, unsave: Any = None) -> None:
        self.theme = theme
        self.unsave = unsave

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)
        writer.write_bool(bool(self.unsave))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSaveTheme':
        theme = reader.read_object()
        unsave = reader.read_bool()
        return cls(theme=theme, unsave=unsave)


@register_tl
class AccountInstallTheme(TLRequest):
    ID: int = 0xc727bb3b

    def __init__(self, dark: bool = False, theme: Any = None, format: Any = None, base_theme: Any = None) -> None:
        self.dark = dark
        self.theme = theme
        self.format = format
        self.base_theme = base_theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.dark:
            flags |= (1 << 0)
        if self.theme is not None:
            flags |= (1 << 1)
        if self.format is not None:
            flags |= (1 << 2)
        if self.base_theme is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.theme is not None:
            if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)
        if self.format is not None:
            writer.write_string(self.format or '')
        if self.base_theme is not None:
            if self.base_theme is not None and hasattr(self.base_theme, 'write'): self.base_theme.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountInstallTheme':
        flags = reader.read_uint32()
        dark = bool(flags & (1 << 0))
        theme = reader.read_object() if (flags & (1 << 1)) else None
        format = reader.read_string() if (flags & (1 << 2)) else None
        base_theme = reader.read_object() if (flags & (1 << 3)) else None
        return cls(dark=dark, theme=theme, format=format, base_theme=base_theme)


@register_tl
class AccountGetTheme(TLRequest):
    ID: int = 0x3a5869ec

    def __init__(self, format: Any = None, theme: Any = None) -> None:
        self.format = format
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.format or '')
        if self.theme is not None and hasattr(self.theme, 'write'): self.theme.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetTheme':
        format = reader.read_string()
        theme = reader.read_object()
        return cls(format=format, theme=theme)


@register_tl
class AccountGetThemes(TLRequest):
    ID: int = 0x7206e458

    def __init__(self, format: Any = None, hash: Any = None) -> None:
        self.format = format
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.format or '')
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetThemes':
        format = reader.read_string()
        hash = reader.read_int64()
        return cls(format=format, hash=hash)


@register_tl
class AccountSetContentSettings(TLRequest):
    ID: int = 0xb574b16b

    def __init__(self, sensitive_enabled: bool = False) -> None:
        self.sensitive_enabled = sensitive_enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sensitive_enabled:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetContentSettings':
        flags = reader.read_uint32()
        sensitive_enabled = bool(flags & (1 << 0))
        return cls(sensitive_enabled=sensitive_enabled)


@register_tl
class AccountGetContentSettings(TLRequest):
    ID: int = 0x8b9b4dae

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetContentSettings':
        return cls()


@register_tl
class AccountGetMultiWallPapers(TLRequest):
    ID: int = 0x65ad71dc

    def __init__(self, wallpapers: Any = None) -> None:
        self.wallpapers = wallpapers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.wallpapers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetMultiWallPapers':
        wallpapers = reader.read_vector(lambda r: reader.read_object())
        return cls(wallpapers=wallpapers)


@register_tl
class AccountGetGlobalPrivacySettings(TLRequest):
    ID: int = 0xeb2b4cf6

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetGlobalPrivacySettings':
        return cls()


@register_tl
class AccountSetGlobalPrivacySettings(TLRequest):
    ID: int = 0x1edaaac2

    def __init__(self, settings: Any = None) -> None:
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetGlobalPrivacySettings':
        settings = reader.read_object()
        return cls(settings=settings)


@register_tl
class AccountReportProfilePhoto(TLRequest):
    ID: int = 0xfa8cc6f5

    def __init__(self, peer: Any = None, photo_id: Any = None, reason: Any = None, message: Any = None) -> None:
        self.peer = peer
        self.photo_id = photo_id
        self.reason = reason
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.photo_id is not None and hasattr(self.photo_id, 'write'): self.photo_id.write(writer)
        if self.reason is not None and hasattr(self.reason, 'write'): self.reason.write(writer)
        writer.write_string(self.message or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountReportProfilePhoto':
        peer = reader.read_object()
        photo_id = reader.read_object()
        reason = reader.read_object()
        message = reader.read_string()
        return cls(peer=peer, photo_id=photo_id, reason=reason, message=message)


@register_tl
class AccountResetPassword(TLRequest):
    ID: int = 0x9308ce1b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResetPassword':
        return cls()


@register_tl
class AccountDeclinePasswordReset(TLRequest):
    ID: int = 0x4c9409f6

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDeclinePasswordReset':
        return cls()


@register_tl
class AccountGetChatThemes(TLRequest):
    ID: int = 0xd638de89

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetChatThemes':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountSetAuthorizationTTL(TLRequest):
    ID: int = 0xbf899aa0

    def __init__(self, authorization_ttl_days: Any = None) -> None:
        self.authorization_ttl_days = authorization_ttl_days

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.authorization_ttl_days or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetAuthorizationTTL':
        authorization_ttl_days = reader.read_int32()
        return cls(authorization_ttl_days=authorization_ttl_days)


@register_tl
class AccountChangeAuthorizationSettings(TLRequest):
    ID: int = 0x40f48462

    def __init__(self, confirmed: bool = False, encrypted_requests_disabled: Any = None, call_requests_disabled: Any = None, hash: Any = None) -> None:
        self.confirmed = confirmed
        self.encrypted_requests_disabled = encrypted_requests_disabled
        self.call_requests_disabled = call_requests_disabled
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.confirmed:
            flags |= (1 << 3)
        if self.encrypted_requests_disabled is not None:
            flags |= (1 << 0)
        if self.call_requests_disabled is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)
        if self.encrypted_requests_disabled is not None:
            writer.write_bool(bool(self.encrypted_requests_disabled))
        if self.call_requests_disabled is not None:
            writer.write_bool(bool(self.call_requests_disabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountChangeAuthorizationSettings':
        flags = reader.read_uint32()
        confirmed = bool(flags & (1 << 3))
        hash = reader.read_int64()
        encrypted_requests_disabled = reader.read_bool() if (flags & (1 << 0)) else None
        call_requests_disabled = reader.read_bool() if (flags & (1 << 1)) else None
        return cls(confirmed=confirmed, hash=hash, encrypted_requests_disabled=encrypted_requests_disabled, call_requests_disabled=call_requests_disabled)


@register_tl
class AccountGetSavedRingtones(TLRequest):
    ID: int = 0xe1902288

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetSavedRingtones':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountSaveRingtone(TLRequest):
    ID: int = 0x3dea5b03

    def __init__(self, id: Any = None, unsave: Any = None) -> None:
        self.id = id
        self.unsave = unsave

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_bool(bool(self.unsave))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSaveRingtone':
        id = reader.read_object()
        unsave = reader.read_bool()
        return cls(id=id, unsave=unsave)


@register_tl
class AccountUploadRingtone(TLRequest):
    ID: int = 0x831a83a2

    def __init__(self, file: Any = None, file_name: Any = None, mime_type: Any = None) -> None:
        self.file = file
        self.file_name = file_name
        self.mime_type = mime_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        writer.write_string(self.file_name or '')
        writer.write_string(self.mime_type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUploadRingtone':
        file = reader.read_object()
        file_name = reader.read_string()
        mime_type = reader.read_string()
        return cls(file=file, file_name=file_name, mime_type=mime_type)


@register_tl
class AccountUpdateEmojiStatus(TLRequest):
    ID: int = 0xfbd3de6b

    def __init__(self, emoji_status: Any = None) -> None:
        self.emoji_status = emoji_status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.emoji_status is not None and hasattr(self.emoji_status, 'write'): self.emoji_status.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateEmojiStatus':
        emoji_status = reader.read_object()
        return cls(emoji_status=emoji_status)


@register_tl
class AccountGetDefaultEmojiStatuses(TLRequest):
    ID: int = 0xd6753386

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetDefaultEmojiStatuses':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetRecentEmojiStatuses(TLRequest):
    ID: int = 0xf578105

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetRecentEmojiStatuses':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountClearRecentEmojiStatuses(TLRequest):
    ID: int = 0x18201aae

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountClearRecentEmojiStatuses':
        return cls()


@register_tl
class AccountReorderUsernames(TLRequest):
    ID: int = 0xef500eab

    def __init__(self, order: Any = None) -> None:
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.order or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountReorderUsernames':
        order = reader.read_vector(lambda r: r.read_string())
        return cls(order=order)


@register_tl
class AccountToggleUsername(TLRequest):
    ID: int = 0x58d6b376

    def __init__(self, username: Any = None, active: Any = None) -> None:
        self.username = username
        self.active = active

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.username or '')
        writer.write_bool(bool(self.active))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountToggleUsername':
        username = reader.read_string()
        active = reader.read_bool()
        return cls(username=username, active=active)


@register_tl
class AccountGetDefaultProfilePhotoEmojis(TLRequest):
    ID: int = 0xe2750328

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetDefaultProfilePhotoEmojis':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetDefaultGroupPhotoEmojis(TLRequest):
    ID: int = 0x915860ae

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetDefaultGroupPhotoEmojis':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetAutoSaveSettings(TLRequest):
    ID: int = 0xadcbbcda

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetAutoSaveSettings':
        return cls()


@register_tl
class AccountSaveAutoSaveSettings(TLRequest):
    ID: int = 0xd69b8361

    def __init__(self, users: bool = False, chats: bool = False, broadcasts: bool = False, peer: Any = None, settings: Any = None) -> None:
        self.users = users
        self.chats = chats
        self.broadcasts = broadcasts
        self.peer = peer
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.users:
            flags |= (1 << 0)
        if self.chats:
            flags |= (1 << 1)
        if self.broadcasts:
            flags |= (1 << 2)
        if self.peer is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.peer is not None:
            if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSaveAutoSaveSettings':
        flags = reader.read_uint32()
        users = bool(flags & (1 << 0))
        chats = bool(flags & (1 << 1))
        broadcasts = bool(flags & (1 << 2))
        peer = reader.read_object() if (flags & (1 << 3)) else None
        settings = reader.read_object()
        return cls(users=users, chats=chats, broadcasts=broadcasts, peer=peer, settings=settings)


@register_tl
class AccountDeleteAutoSaveExceptions(TLRequest):
    ID: int = 0x53bc0020

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDeleteAutoSaveExceptions':
        return cls()


@register_tl
class AccountInvalidateSignInCodes(TLRequest):
    ID: int = 0xca8ae8ba

    def __init__(self, codes: Any = None) -> None:
        self.codes = codes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.codes or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountInvalidateSignInCodes':
        codes = reader.read_vector(lambda r: r.read_string())
        return cls(codes=codes)


@register_tl
class AccountUpdateColor(TLRequest):
    ID: int = 0x684d214e

    def __init__(self, for_profile: bool = False, color: Any = None) -> None:
        self.for_profile = for_profile
        self.color = color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.for_profile:
            flags |= (1 << 1)
        if self.color is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.color is not None:
            if self.color is not None and hasattr(self.color, 'write'): self.color.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateColor':
        flags = reader.read_uint32()
        for_profile = bool(flags & (1 << 1))
        color = reader.read_object() if (flags & (1 << 2)) else None
        return cls(for_profile=for_profile, color=color)


@register_tl
class AccountGetDefaultBackgroundEmojis(TLRequest):
    ID: int = 0xa60ab9ce

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetDefaultBackgroundEmojis':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetChannelDefaultEmojiStatuses(TLRequest):
    ID: int = 0x7727a7d5

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetChannelDefaultEmojiStatuses':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetChannelRestrictedStatusEmojis(TLRequest):
    ID: int = 0x35a9e0d5

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetChannelRestrictedStatusEmojis':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountUpdateBusinessWorkHours(TLRequest):
    ID: int = 0x4b00e066

    def __init__(self, business_work_hours: Any = None) -> None:
        self.business_work_hours = business_work_hours

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.business_work_hours is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.business_work_hours is not None:
            if self.business_work_hours is not None and hasattr(self.business_work_hours, 'write'): self.business_work_hours.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateBusinessWorkHours':
        flags = reader.read_uint32()
        business_work_hours = reader.read_object() if (flags & (1 << 0)) else None
        return cls(business_work_hours=business_work_hours)


@register_tl
class AccountUpdateBusinessLocation(TLRequest):
    ID: int = 0x9e6b131a

    def __init__(self, geo_point: Any = None, address: Any = None) -> None:
        self.geo_point = geo_point
        self.address = address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo_point is not None:
            flags |= (1 << 1)
        if self.address is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.geo_point is not None:
            if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        if self.address is not None:
            writer.write_string(self.address or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateBusinessLocation':
        flags = reader.read_uint32()
        geo_point = reader.read_object() if (flags & (1 << 1)) else None
        address = reader.read_string() if (flags & (1 << 0)) else None
        return cls(geo_point=geo_point, address=address)


@register_tl
class AccountUpdateBusinessGreetingMessage(TLRequest):
    ID: int = 0x66cdafc4

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.message is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateBusinessGreetingMessage':
        flags = reader.read_uint32()
        message = reader.read_object() if (flags & (1 << 0)) else None
        return cls(message=message)


@register_tl
class AccountUpdateBusinessAwayMessage(TLRequest):
    ID: int = 0xa26a7fa5

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.message is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.message is not None:
            if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateBusinessAwayMessage':
        flags = reader.read_uint32()
        message = reader.read_object() if (flags & (1 << 0)) else None
        return cls(message=message)


@register_tl
class AccountUpdateConnectedBot(TLRequest):
    ID: int = 0x66a08c7e

    def __init__(self, deleted: bool = False, rights: Any = None, bot: Any = None, recipients: Any = None) -> None:
        self.deleted = deleted
        self.rights = rights
        self.bot = bot
        self.recipients = recipients

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.deleted:
            flags |= (1 << 1)
        if self.rights is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.rights is not None:
            if self.rights is not None and hasattr(self.rights, 'write'): self.rights.write(writer)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.recipients is not None and hasattr(self.recipients, 'write'): self.recipients.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateConnectedBot':
        flags = reader.read_uint32()
        deleted = bool(flags & (1 << 1))
        rights = reader.read_object() if (flags & (1 << 0)) else None
        bot = reader.read_object()
        recipients = reader.read_object()
        return cls(deleted=deleted, rights=rights, bot=bot, recipients=recipients)


@register_tl
class AccountGetConnectedBots(TLRequest):
    ID: int = 0x4ea4c80f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetConnectedBots':
        return cls()


@register_tl
class AccountGetBotBusinessConnection(TLRequest):
    ID: int = 0x76a86270

    def __init__(self, connection_id: Any = None) -> None:
        self.connection_id = connection_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.connection_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetBotBusinessConnection':
        connection_id = reader.read_string()
        return cls(connection_id=connection_id)


@register_tl
class AccountUpdateBusinessIntro(TLRequest):
    ID: int = 0xa614d034

    def __init__(self, intro: Any = None) -> None:
        self.intro = intro

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.intro is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.intro is not None:
            if self.intro is not None and hasattr(self.intro, 'write'): self.intro.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateBusinessIntro':
        flags = reader.read_uint32()
        intro = reader.read_object() if (flags & (1 << 0)) else None
        return cls(intro=intro)


@register_tl
class AccountToggleConnectedBotPaused(TLRequest):
    ID: int = 0x646e1097

    def __init__(self, peer: Any = None, paused: Any = None) -> None:
        self.peer = peer
        self.paused = paused

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_bool(bool(self.paused))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountToggleConnectedBotPaused':
        peer = reader.read_object()
        paused = reader.read_bool()
        return cls(peer=peer, paused=paused)


@register_tl
class AccountDisablePeerConnectedBot(TLRequest):
    ID: int = 0x5e437ed9

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDisablePeerConnectedBot':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class AccountUpdateBirthday(TLRequest):
    ID: int = 0xcc6e0c11

    def __init__(self, birthday: Any = None) -> None:
        self.birthday = birthday

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.birthday is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.birthday is not None:
            if self.birthday is not None and hasattr(self.birthday, 'write'): self.birthday.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdateBirthday':
        flags = reader.read_uint32()
        birthday = reader.read_object() if (flags & (1 << 0)) else None
        return cls(birthday=birthday)


@register_tl
class AccountCreateBusinessChatLink(TLRequest):
    ID: int = 0x8851e68e

    def __init__(self, link: Any = None) -> None:
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.link is not None and hasattr(self.link, 'write'): self.link.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountCreateBusinessChatLink':
        link = reader.read_object()
        return cls(link=link)


@register_tl
class AccountEditBusinessChatLink(TLRequest):
    ID: int = 0x8c3410af

    def __init__(self, slug: Any = None, link: Any = None) -> None:
        self.slug = slug
        self.link = link

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')
        if self.link is not None and hasattr(self.link, 'write'): self.link.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountEditBusinessChatLink':
        slug = reader.read_string()
        link = reader.read_object()
        return cls(slug=slug, link=link)


@register_tl
class AccountDeleteBusinessChatLink(TLRequest):
    ID: int = 0x60073674

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDeleteBusinessChatLink':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class AccountGetBusinessChatLinks(TLRequest):
    ID: int = 0x6f70dde1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetBusinessChatLinks':
        return cls()


@register_tl
class AccountResolveBusinessChatLink(TLRequest):
    ID: int = 0x5492e5ee

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountResolveBusinessChatLink':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class AccountUpdatePersonalChannel(TLRequest):
    ID: int = 0xd94305e0

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountUpdatePersonalChannel':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class AccountToggleSponsoredMessages(TLRequest):
    ID: int = 0xb9d9a38d

    def __init__(self, enabled: Any = None) -> None:
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountToggleSponsoredMessages':
        enabled = reader.read_bool()
        return cls(enabled=enabled)


@register_tl
class AccountGetReactionsNotifySettings(TLRequest):
    ID: int = 0x6dd654c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetReactionsNotifySettings':
        return cls()


@register_tl
class AccountSetReactionsNotifySettings(TLRequest):
    ID: int = 0x316ce548

    def __init__(self, settings: Any = None) -> None:
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.settings is not None and hasattr(self.settings, 'write'): self.settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetReactionsNotifySettings':
        settings = reader.read_object()
        return cls(settings=settings)


@register_tl
class AccountGetCollectibleEmojiStatuses(TLRequest):
    ID: int = 0x2e7b4543

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetCollectibleEmojiStatuses':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetPaidMessagesRevenue(TLRequest):
    ID: int = 0x19ba4a67

    def __init__(self, parent_peer: Any = None, user_id: Any = None) -> None:
        self.parent_peer = parent_peer
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.parent_peer is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetPaidMessagesRevenue':
        flags = reader.read_uint32()
        parent_peer = reader.read_object() if (flags & (1 << 0)) else None
        user_id = reader.read_object()
        return cls(parent_peer=parent_peer, user_id=user_id)


@register_tl
class AccountToggleNoPaidMessagesException(TLRequest):
    ID: int = 0xfe2eda76

    def __init__(self, refund_charged: bool = False, require_payment: bool = False, parent_peer: Any = None, user_id: Any = None) -> None:
        self.refund_charged = refund_charged
        self.require_payment = require_payment
        self.parent_peer = parent_peer
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.refund_charged:
            flags |= (1 << 0)
        if self.require_payment:
            flags |= (1 << 2)
        if self.parent_peer is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.parent_peer is not None:
            if self.parent_peer is not None and hasattr(self.parent_peer, 'write'): self.parent_peer.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountToggleNoPaidMessagesException':
        flags = reader.read_uint32()
        refund_charged = bool(flags & (1 << 0))
        require_payment = bool(flags & (1 << 2))
        parent_peer = reader.read_object() if (flags & (1 << 1)) else None
        user_id = reader.read_object()
        return cls(refund_charged=refund_charged, require_payment=require_payment, parent_peer=parent_peer, user_id=user_id)


@register_tl
class AccountSetMainProfileTab(TLRequest):
    ID: int = 0x5dee78b0

    def __init__(self, tab: Any = None) -> None:
        self.tab = tab

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.tab is not None and hasattr(self.tab, 'write'): self.tab.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSetMainProfileTab':
        tab = reader.read_object()
        return cls(tab=tab)


@register_tl
class AccountSaveMusic(TLRequest):
    ID: int = 0xb26732a9

    def __init__(self, unsave: bool = False, after_id: Any = None, id: Any = None) -> None:
        self.unsave = unsave
        self.after_id = after_id
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unsave:
            flags |= (1 << 0)
        if self.after_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.after_id is not None:
            if self.after_id is not None and hasattr(self.after_id, 'write'): self.after_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountSaveMusic':
        flags = reader.read_uint32()
        unsave = bool(flags & (1 << 0))
        id = reader.read_object()
        after_id = reader.read_object() if (flags & (1 << 1)) else None
        return cls(unsave=unsave, id=id, after_id=after_id)


@register_tl
class AccountGetSavedMusicIds(TLRequest):
    ID: int = 0xe09d5faf

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetSavedMusicIds':
        hash = reader.read_int64()
        return cls(hash=hash)


@register_tl
class AccountGetUniqueGiftChatThemes(TLRequest):
    ID: int = 0xe42ce9c9

    def __init__(self, offset: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetUniqueGiftChatThemes':
        offset = reader.read_string()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(offset=offset, limit=limit, hash=hash)


@register_tl
class AccountInitPasskeyRegistration(TLRequest):
    ID: int = 0x429547e8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountInitPasskeyRegistration':
        return cls()


@register_tl
class AccountRegisterPasskey(TLRequest):
    ID: int = 0x55b41fd6

    def __init__(self, credential: Any = None) -> None:
        self.credential = credential

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.credential is not None and hasattr(self.credential, 'write'): self.credential.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountRegisterPasskey':
        credential = reader.read_object()
        return cls(credential=credential)


@register_tl
class AccountGetPasskeys(TLRequest):
    ID: int = 0xea1f0c52

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountGetPasskeys':
        return cls()


@register_tl
class AccountDeletePasskey(TLRequest):
    ID: int = 0xf5b5563f

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDeletePasskey':
        id = reader.read_string()
        return cls(id=id)


@register_tl
class UsersGetUsers(TLRequest):
    ID: int = 0xd91a548

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersGetUsers':
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id)


@register_tl
class UsersGetFullUser(TLRequest):
    ID: int = 0xb60f5918

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersGetFullUser':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class UsersSetSecureValueErrors(TLRequest):
    ID: int = 0x90c894b5

    def __init__(self, id: Any = None, errors: Any = None) -> None:
        self.id = id
        self.errors = errors

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_vector(self.errors or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersSetSecureValueErrors':
        id = reader.read_object()
        errors = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id, errors=errors)


@register_tl
class UsersGetRequirementsToContact(TLRequest):
    ID: int = 0xd89a83a3

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersGetRequirementsToContact':
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id)


@register_tl
class UsersGetSavedMusic(TLRequest):
    ID: int = 0x788d7fe3

    def __init__(self, id: Any = None, offset: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.id = id
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersGetSavedMusic':
        id = reader.read_object()
        offset = reader.read_int32()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(id=id, offset=offset, limit=limit, hash=hash)


@register_tl
class UsersGetSavedMusicByID(TLRequest):
    ID: int = 0x7573a4e9

    def __init__(self, id: Any = None, documents: Any = None) -> None:
        self.id = id
        self.documents = documents

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_vector(self.documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersGetSavedMusicByID':
        id = reader.read_object()
        documents = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id, documents=documents)


@register_tl
class UsersSuggestBirthday(TLRequest):
    ID: int = 0xfc533372

    def __init__(self, id: Any = None, birthday: Any = None) -> None:
        self.id = id
        self.birthday = birthday

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.birthday is not None and hasattr(self.birthday, 'write'): self.birthday.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'UsersSuggestBirthday':
        id = reader.read_object()
        birthday = reader.read_object()
        return cls(id=id, birthday=birthday)


@register_tl
class ContactsGetContactIDs(TLRequest):
    ID: int = 0x7adc669d

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsGetContactIDs':
        hash = reader.read_int64()
        return cls(hash=hash)

