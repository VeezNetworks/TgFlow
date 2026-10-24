from typing import Any
from ..core import TLRequest, TLWriter, TLReader, register_tl



@register_tl
class ReqPqMulti(TLRequest):
    ID: int = 0xbe7e8ef1

    def __init__(self, nonce: Any = None) -> None:
        self.nonce = nonce

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReqPqMulti':
        nonce = reader.read_int128()
        return cls(nonce=nonce)


@register_tl
class ReqDHParams(TLRequest):
    ID: int = 0xd712e4be

    def __init__(self, nonce: Any = None, server_nonce: Any = None, p: Any = None, q: Any = None, public_key_fingerprint: Any = None, encrypted_data: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.p = p
        self.q = q
        self.public_key_fingerprint = public_key_fingerprint
        self.encrypted_data = encrypted_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_bytes(self.p or b'')
        writer.write_bytes(self.q or b'')
        writer.write_int64(self.public_key_fingerprint or 0)
        writer.write_bytes(self.encrypted_data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ReqDHParams':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        p = reader.read_bytes()
        q = reader.read_bytes()
        public_key_fingerprint = reader.read_int64()
        encrypted_data = reader.read_bytes()
        return cls(nonce=nonce, server_nonce=server_nonce, p=p, q=q, public_key_fingerprint=public_key_fingerprint, encrypted_data=encrypted_data)


@register_tl
class SetClientDHParams(TLRequest):
    ID: int = 0xf5045f1f

    def __init__(self, nonce: Any = None, server_nonce: Any = None, encrypted_data: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_data = encrypted_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_bytes(self.encrypted_data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SetClientDHParams':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        encrypted_data = reader.read_bytes()
        return cls(nonce=nonce, server_nonce=server_nonce, encrypted_data=encrypted_data)


@register_tl
class RpcDropAnswer(TLRequest):
    ID: int = 0x58e4a740

    def __init__(self, req_msg_id: Any = None) -> None:
        self.req_msg_id = req_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.req_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'RpcDropAnswer':
        req_msg_id = reader.read_int64()
        return cls(req_msg_id=req_msg_id)


@register_tl
class GetFutureSalts(TLRequest):
    ID: int = 0xb921bd04

    def __init__(self, num: Any = None) -> None:
        self.num = num

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.num or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GetFutureSalts':
        num = reader.read_int32()
        return cls(num=num)


@register_tl
class Ping(TLRequest):
    ID: int = 0x7abe77ec

    def __init__(self, ping_id: Any = None) -> None:
        self.ping_id = ping_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.ping_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Ping':
        ping_id = reader.read_int64()
        return cls(ping_id=ping_id)


@register_tl
class PingDelayDisconnect(TLRequest):
    ID: int = 0xf3427b8c

    def __init__(self, ping_id: Any = None, disconnect_delay: Any = None) -> None:
        self.ping_id = ping_id
        self.disconnect_delay = disconnect_delay

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.ping_id or 0)
        writer.write_int32(self.disconnect_delay or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PingDelayDisconnect':
        ping_id = reader.read_int64()
        disconnect_delay = reader.read_int32()
        return cls(ping_id=ping_id, disconnect_delay=disconnect_delay)


@register_tl
class DestroySession(TLRequest):
    ID: int = 0xe7512126

    def __init__(self, session_id: Any = None) -> None:
        self.session_id = session_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.session_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DestroySession':
        session_id = reader.read_int64()
        return cls(session_id=session_id)


@register_tl
class DestroyAuthKey(TLRequest):
    ID: int = 0xd1435160

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DestroyAuthKey':
        return cls()

