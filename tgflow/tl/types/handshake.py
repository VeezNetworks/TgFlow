from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl


@register_tl
class ResPQ(TLObject):
    ID: int = 0x05162463

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        pq: bytes = b"",
        server_public_key_fingerprints: list[int] | None = None,
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.pq = pq
        self.server_public_key_fingerprints = server_public_key_fingerprints or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_bytes(self.pq)
        writer.write_vector(
            self.server_public_key_fingerprints,
            lambda w, item: w.write_uint64(item),
        )

    @classmethod
    def read(cls, reader: TLReader) -> "ResPQ":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        pq = reader.read_bytes()
        fps = reader.read_vector(lambda r: r.read_uint64())
        return cls(
            nonce=nonce,
            server_nonce=server_nonce,
            pq=pq,
            server_public_key_fingerprints=fps,
        )


@register_tl
class ServerDHParamsOk(TLObject):
    ID: int = 0xD0E80A05

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        encrypted_answer: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_answer = encrypted_answer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_bytes(self.encrypted_answer)

    @classmethod
    def read(cls, reader: TLReader) -> "ServerDHParamsOk":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        encrypted_answer = reader.read_bytes()
        return cls(
            nonce=nonce,
            server_nonce=server_nonce,
            encrypted_answer=encrypted_answer,
        )


@register_tl
class DhGenOk(TLObject):
    ID: int = 0x3BCBF734

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        new_nonce_hash1: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash1 = new_nonce_hash1

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_int128(self.new_nonce_hash1)

    @classmethod
    def read(cls, reader: TLReader) -> "DhGenOk":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce_hash1 = reader.read_int128()
        return cls(
            nonce=nonce,
            server_nonce=server_nonce,
            new_nonce_hash1=new_nonce_hash1,
        )


@register_tl
class DhGenRetry(TLObject):
    ID: int = 0x462DE7B2

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        new_nonce_hash2: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash2 = new_nonce_hash2

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_int128(self.new_nonce_hash2)

    @classmethod
    def read(cls, reader: TLReader) -> "DhGenRetry":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce_hash2 = reader.read_int128()
        return cls(
            nonce=nonce,
            server_nonce=server_nonce,
            new_nonce_hash2=new_nonce_hash2,
        )


@register_tl
class DhGenFail(TLObject):
    ID: int = 0xA69DAE02

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        new_nonce_hash3: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash3 = new_nonce_hash3

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_int128(self.new_nonce_hash3)

    @classmethod
    def read(cls, reader: TLReader) -> "DhGenFail":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce_hash3 = reader.read_int128()
        return cls(
            nonce=nonce,
            server_nonce=server_nonce,
            new_nonce_hash3=new_nonce_hash3,
        )


@register_tl
class RpcResult(TLObject):
    ID: int = 0xF35C6D01

    def __init__(self, req_msg_id: int = 0, result: Any = None) -> None:
        self.req_msg_id = req_msg_id
        self.result = result

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.req_msg_id)
        if hasattr(self.result, "write"):
            self.result.write(writer)
        elif isinstance(self.result, bytes):
            writer.write_bytes(self.result)

    @classmethod
    def read(cls, reader: TLReader) -> "RpcResult":
        req_msg_id = reader.read_int64()
        result = reader.read_object()
        return cls(req_msg_id=req_msg_id, result=result)


@register_tl
class RpcError(TLObject):
    ID: int = 0x2144CA62

    def __init__(self, error_code: int = 0, error_message: str = "") -> None:
        self.error_code = error_code
        self.error_message = error_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.error_code)
        writer.write_string(self.error_message)

    @classmethod
    def read(cls, reader: TLReader) -> "RpcError":
        error_code = reader.read_int32()
        error_message = reader.read_string()
        return cls(error_code=error_code, error_message=error_message)


@register_tl
class MsgContainer(TLObject):
    ID: int = 0x73F1F8DC

    def __init__(self, messages: list[Any] | None = None) -> None:
        self.messages = messages or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(len(self.messages))
        for msg in self.messages:
            if hasattr(msg, "write"):
                msg.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> "MsgContainer":
        count = reader.read_int32()
        msgs = []
        for _ in range(count):
            msg_id = reader.read_int64()
            seq_no = reader.read_int32()
            bytes_len = reader.read_int32()
            body = reader.read_object()
            msgs.append({"msg_id": msg_id, "seq_no": seq_no, "body": body})
        return cls(messages=msgs)


@register_tl
class GzipPacked(TLObject):
    ID: int = 0x3072CFA1

    def __init__(self, packed_data: bytes = b"") -> None:
        self.packed_data = packed_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.packed_data)

    @classmethod
    def read(cls, reader: TLReader) -> "GzipPacked":
        packed_data = reader.read_bytes()
        return cls(packed_data=packed_data)


@register_tl
class BadMsgNotification(TLObject):
    ID: int = 0xA7EFF811

    def __init__(self, bad_msg_id: int = 0, bad_msg_seqno: int = 0, error_code: int = 0) -> None:
        self.bad_msg_id = bad_msg_id
        self.bad_msg_seqno = bad_msg_seqno
        self.error_code = error_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bad_msg_id)
        writer.write_int32(self.bad_msg_seqno)
        writer.write_int32(self.error_code)

    @classmethod
    def read(cls, reader: TLReader) -> "BadMsgNotification":
        bad_msg_id = reader.read_int64()
        bad_msg_seqno = reader.read_int32()
        error_code = reader.read_int32()
        return cls(bad_msg_id=bad_msg_id, bad_msg_seqno=bad_msg_seqno, error_code=error_code)


@register_tl
class BadServerSalt(TLObject):
    ID: int = 0xED4830A3

    def __init__(self, bad_msg_id: int = 0, bad_msg_seqno: int = 0, error_code: int = 0, new_server_salt: int = 0) -> None:
        self.bad_msg_id = bad_msg_id
        self.bad_msg_seqno = bad_msg_seqno
        self.error_code = error_code
        self.new_server_salt = new_server_salt

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bad_msg_id)
        writer.write_int32(self.bad_msg_seqno)
        writer.write_int32(self.error_code)
        writer.write_int64(self.new_server_salt)

    @classmethod
    def read(cls, reader: TLReader) -> "BadServerSalt":
        bad_msg_id = reader.read_int64()
        bad_msg_seqno = reader.read_int32()
        error_code = reader.read_int32()
        new_server_salt = reader.read_int64()
        return cls(
            bad_msg_id=bad_msg_id,
            bad_msg_seqno=bad_msg_seqno,
            error_code=error_code,
            new_server_salt=new_server_salt,
        )


@register_tl
class MsgsAck(TLObject):
    ID: int = 0x62D6B459

    def __init__(self, msg_ids: list[int] | None = None) -> None:
        self.msg_ids = msg_ids or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.msg_ids, lambda w, i: w.write_int64(i))

    @classmethod
    def read(cls, reader: TLReader) -> "MsgsAck":
        msg_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(msg_ids=msg_ids)
