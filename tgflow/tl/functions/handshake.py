from typing import Any
from ..core import TLRequest, TLWriter, TLReader, register_tl


@register_tl
class ReqPqMulti(TLRequest):
    ID: int = 0xBE7E8EF1

    def __init__(self, nonce: bytes | int = b"\x00" * 16) -> None:
        self.nonce = nonce

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)

    @classmethod
    def read(cls, reader: TLReader) -> "ReqPqMulti":
        nonce = reader.read_int128()
        return cls(nonce=nonce)


@register_tl
class ReqDHParams(TLRequest):
    ID: int = 0xD712E4BE

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        p: bytes = b"",
        q: bytes = b"",
        public_key_fingerprint: int = 0,
        encrypted_data: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.p = p
        self.q = q
        self.public_key_fingerprint = public_key_fingerprint
        self.encrypted_data = encrypted_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_string(self.p.decode("latin1") if isinstance(self.p, bytes) else str(self.p))
        writer.write_string(self.q.decode("latin1") if isinstance(self.q, bytes) else str(self.q))
        writer.write_uint64(self.public_key_fingerprint)
        writer.write_bytes(self.encrypted_data)

    @classmethod
    def read(cls, reader: TLReader) -> "ReqDHParams":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        p = reader.read_string().encode("latin1")
        q = reader.read_string().encode("latin1")
        public_key_fingerprint = reader.read_uint64()
        encrypted_data = reader.read_bytes()
        return cls(
            nonce=nonce,
            server_nonce=server_nonce,
            p=p,
            q=q,
            public_key_fingerprint=public_key_fingerprint,
            encrypted_data=encrypted_data,
        )


@register_tl
class SetClientDHParams(TLRequest):
    ID: int = 0xF5045F1F

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        encrypted_data: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_data = encrypted_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_bytes(self.encrypted_data)

    @classmethod
    def read(cls, reader: TLReader) -> "SetClientDHParams":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        encrypted_data = reader.read_bytes()
        return cls(nonce=nonce, server_nonce=server_nonce, encrypted_data=encrypted_data)


@register_tl
class Ping(TLRequest):
    ID: int = 0x7ABE77EC

    def __init__(self, ping_id: int = 0) -> None:
        self.ping_id = ping_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.ping_id)

    @classmethod
    def read(cls, reader: TLReader) -> "Ping":
        return cls(ping_id=reader.read_int64())


@register_tl
class PingDelayDisconnect(TLRequest):
    ID: int = 0xF342779D

    def __init__(self, ping_id: int = 0, disconnect_delay: int = 60) -> None:
        self.ping_id = ping_id
        self.disconnect_delay = disconnect_delay

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.ping_id)
        writer.write_int32(self.disconnect_delay)

    @classmethod
    def read(cls, reader: TLReader) -> "PingDelayDisconnect":
        return cls(ping_id=reader.read_int64(), disconnect_delay=reader.read_int32())
