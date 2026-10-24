from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl



@register_tl
class ResPQ(TLObject):
    ID: int = 0x5162463

    def __init__(self, nonce: Any = None, server_nonce: Any = None, pq: Any = None, server_public_key_fingerprints: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.pq = pq
        self.server_public_key_fingerprints = server_public_key_fingerprints

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_bytes(self.pq or b'')
        writer.write_vector(self.server_public_key_fingerprints or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ResPQ':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        pq = reader.read_bytes()
        server_public_key_fingerprints = reader.read_vector(lambda r: r.read_int64())
        return cls(nonce=nonce, server_nonce=server_nonce, pq=pq, server_public_key_fingerprints=server_public_key_fingerprints)


@register_tl
class PQInnerDataDc(TLObject):
    ID: int = 0xa9f55f95

    def __init__(self, pq: Any = None, p: Any = None, q: Any = None, nonce: Any = None, server_nonce: Any = None, new_nonce: Any = None, dc: Any = None) -> None:
        self.pq = pq
        self.p = p
        self.q = q
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce = new_nonce
        self.dc = dc

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.pq or b'')
        writer.write_bytes(self.p or b'')
        writer.write_bytes(self.q or b'')
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int256(self.new_nonce or 0)
        writer.write_int32(self.dc or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PQInnerDataDc':
        pq = reader.read_bytes()
        p = reader.read_bytes()
        q = reader.read_bytes()
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce = reader.read_int256()
        dc = reader.read_int32()
        return cls(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce, dc=dc)


@register_tl
class PQInnerDataTempDc(TLObject):
    ID: int = 0x56fddf88

    def __init__(self, pq: Any = None, p: Any = None, q: Any = None, nonce: Any = None, server_nonce: Any = None, new_nonce: Any = None, dc: Any = None, expires_in: Any = None) -> None:
        self.pq = pq
        self.p = p
        self.q = q
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce = new_nonce
        self.dc = dc
        self.expires_in = expires_in

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.pq or b'')
        writer.write_bytes(self.p or b'')
        writer.write_bytes(self.q or b'')
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int256(self.new_nonce or 0)
        writer.write_int32(self.dc or 0)
        writer.write_int32(self.expires_in or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PQInnerDataTempDc':
        pq = reader.read_bytes()
        p = reader.read_bytes()
        q = reader.read_bytes()
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce = reader.read_int256()
        dc = reader.read_int32()
        expires_in = reader.read_int32()
        return cls(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce, dc=dc, expires_in=expires_in)


@register_tl
class ServerDHParamsOk(TLObject):
    ID: int = 0xd0e8075c

    def __init__(self, nonce: Any = None, server_nonce: Any = None, encrypted_answer: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_answer = encrypted_answer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_bytes(self.encrypted_answer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ServerDHParamsOk':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        encrypted_answer = reader.read_bytes()
        return cls(nonce=nonce, server_nonce=server_nonce, encrypted_answer=encrypted_answer)


@register_tl
class ServerDHInnerData(TLObject):
    ID: int = 0xb5890dba

    def __init__(self, nonce: Any = None, server_nonce: Any = None, g: Any = None, dh_prime: Any = None, g_a: Any = None, server_time: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.g = g
        self.dh_prime = dh_prime
        self.g_a = g_a
        self.server_time = server_time

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int32(self.g or 0)
        writer.write_bytes(self.dh_prime or b'')
        writer.write_bytes(self.g_a or b'')
        writer.write_int32(self.server_time or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ServerDHInnerData':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        g = reader.read_int32()
        dh_prime = reader.read_bytes()
        g_a = reader.read_bytes()
        server_time = reader.read_int32()
        return cls(nonce=nonce, server_nonce=server_nonce, g=g, dh_prime=dh_prime, g_a=g_a, server_time=server_time)


@register_tl
class ClientDHInnerData(TLObject):
    ID: int = 0x6643b654

    def __init__(self, nonce: Any = None, server_nonce: Any = None, retry_id: Any = None, g_b: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.retry_id = retry_id
        self.g_b = g_b

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int64(self.retry_id or 0)
        writer.write_bytes(self.g_b or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ClientDHInnerData':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        retry_id = reader.read_int64()
        g_b = reader.read_bytes()
        return cls(nonce=nonce, server_nonce=server_nonce, retry_id=retry_id, g_b=g_b)


@register_tl
class DhGenOk(TLObject):
    ID: int = 0x3bcbf734

    def __init__(self, nonce: Any = None, server_nonce: Any = None, new_nonce_hash1: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash1 = new_nonce_hash1

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int128(self.new_nonce_hash1 or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DhGenOk':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce_hash1 = reader.read_int128()
        return cls(nonce=nonce, server_nonce=server_nonce, new_nonce_hash1=new_nonce_hash1)


@register_tl
class DhGenRetry(TLObject):
    ID: int = 0x46dc1fb9

    def __init__(self, nonce: Any = None, server_nonce: Any = None, new_nonce_hash2: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash2 = new_nonce_hash2

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int128(self.new_nonce_hash2 or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DhGenRetry':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce_hash2 = reader.read_int128()
        return cls(nonce=nonce, server_nonce=server_nonce, new_nonce_hash2=new_nonce_hash2)


@register_tl
class DhGenFail(TLObject):
    ID: int = 0xa69dae02

    def __init__(self, nonce: Any = None, server_nonce: Any = None, new_nonce_hash3: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash3 = new_nonce_hash3

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int128(self.new_nonce_hash3 or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DhGenFail':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce_hash3 = reader.read_int128()
        return cls(nonce=nonce, server_nonce=server_nonce, new_nonce_hash3=new_nonce_hash3)


@register_tl
class BindAuthKeyInner(TLObject):
    ID: int = 0x75a3f765

    def __init__(self, nonce: Any = None, temp_auth_key_id: Any = None, perm_auth_key_id: Any = None, temp_session_id: Any = None, expires_at: Any = None) -> None:
        self.nonce = nonce
        self.temp_auth_key_id = temp_auth_key_id
        self.perm_auth_key_id = perm_auth_key_id
        self.temp_session_id = temp_session_id
        self.expires_at = expires_at

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.nonce or 0)
        writer.write_int64(self.temp_auth_key_id or 0)
        writer.write_int64(self.perm_auth_key_id or 0)
        writer.write_int64(self.temp_session_id or 0)
        writer.write_int32(self.expires_at or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BindAuthKeyInner':
        nonce = reader.read_int64()
        temp_auth_key_id = reader.read_int64()
        perm_auth_key_id = reader.read_int64()
        temp_session_id = reader.read_int64()
        expires_at = reader.read_int32()
        return cls(nonce=nonce, temp_auth_key_id=temp_auth_key_id, perm_auth_key_id=perm_auth_key_id, temp_session_id=temp_session_id, expires_at=expires_at)


@register_tl
class RpcResult(TLObject):
    ID: int = 0xf35c6d01

    def __init__(self, req_msg_id: Any = None, result: Any = None) -> None:
        self.req_msg_id = req_msg_id
        self.result = result

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.req_msg_id or 0)
        if self.result is not None and hasattr(self.result, 'write'): self.result.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'RpcResult':
        req_msg_id = reader.read_int64()
        result = reader.read_object()
        return cls(req_msg_id=req_msg_id, result=result)


@register_tl
class RpcError(TLObject):
    ID: int = 0x2144ca19

    def __init__(self, error_code: Any = None, error_message: Any = None) -> None:
        self.error_code = error_code
        self.error_message = error_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.error_code or 0)
        writer.write_string(self.error_message or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'RpcError':
        error_code = reader.read_int32()
        error_message = reader.read_string()
        return cls(error_code=error_code, error_message=error_message)


@register_tl
class RpcAnswerUnknown(TLObject):
    ID: int = 0x5e2ad36e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'RpcAnswerUnknown':
        return cls()


@register_tl
class RpcAnswerDroppedRunning(TLObject):
    ID: int = 0xcd78e586

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'RpcAnswerDroppedRunning':
        return cls()


@register_tl
class RpcAnswerDropped(TLObject):
    ID: int = 0xa43ad8b7

    def __init__(self, msg_id: Any = None, seq_no: Any = None, bytes: Any = None) -> None:
        self.msg_id = msg_id
        self.seq_no = seq_no
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.msg_id or 0)
        writer.write_int32(self.seq_no or 0)
        writer.write_int32(self.bytes or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'RpcAnswerDropped':
        msg_id = reader.read_int64()
        seq_no = reader.read_int32()
        bytes = reader.read_int32()
        return cls(msg_id=msg_id, seq_no=seq_no, bytes=bytes)


@register_tl
class FutureSalt(TLObject):
    ID: int = 0x949d9dc

    def __init__(self, valid_since: Any = None, valid_until: Any = None, salt: Any = None) -> None:
        self.valid_since = valid_since
        self.valid_until = valid_until
        self.salt = salt

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.valid_since or 0)
        writer.write_int32(self.valid_until or 0)
        writer.write_int64(self.salt or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'FutureSalt':
        valid_since = reader.read_int32()
        valid_until = reader.read_int32()
        salt = reader.read_int64()
        return cls(valid_since=valid_since, valid_until=valid_until, salt=salt)


@register_tl
class FutureSalts(TLObject):
    ID: int = 0xae500895

    def __init__(self, req_msg_id: Any = None, now: Any = None, salts: Any = None) -> None:
        self.req_msg_id = req_msg_id
        self.now = now
        self.salts = salts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.req_msg_id or 0)
        writer.write_int32(self.now or 0)
        writer.write_vector(self.salts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'FutureSalts':
        req_msg_id = reader.read_int64()
        now = reader.read_int32()
        salts = reader.read_vector(lambda r: reader.read_object())
        return cls(req_msg_id=req_msg_id, now=now, salts=salts)


@register_tl
class Pong(TLObject):
    ID: int = 0x347773c5

    def __init__(self, msg_id: Any = None, ping_id: Any = None) -> None:
        self.msg_id = msg_id
        self.ping_id = ping_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.msg_id or 0)
        writer.write_int64(self.ping_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Pong':
        msg_id = reader.read_int64()
        ping_id = reader.read_int64()
        return cls(msg_id=msg_id, ping_id=ping_id)


@register_tl
class DestroySessionOk(TLObject):
    ID: int = 0xe22045fc

    def __init__(self, session_id: Any = None) -> None:
        self.session_id = session_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.session_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DestroySessionOk':
        session_id = reader.read_int64()
        return cls(session_id=session_id)


@register_tl
class DestroySessionNone(TLObject):
    ID: int = 0x62d350c9

    def __init__(self, session_id: Any = None) -> None:
        self.session_id = session_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.session_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DestroySessionNone':
        session_id = reader.read_int64()
        return cls(session_id=session_id)


@register_tl
class NewSessionCreated(TLObject):
    ID: int = 0x9ec20908

    def __init__(self, first_msg_id: Any = None, unique_id: Any = None, server_salt: Any = None) -> None:
        self.first_msg_id = first_msg_id
        self.unique_id = unique_id
        self.server_salt = server_salt

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.first_msg_id or 0)
        writer.write_int64(self.unique_id or 0)
        writer.write_int64(self.server_salt or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'NewSessionCreated':
        first_msg_id = reader.read_int64()
        unique_id = reader.read_int64()
        server_salt = reader.read_int64()
        return cls(first_msg_id=first_msg_id, unique_id=unique_id, server_salt=server_salt)


@register_tl
class MsgContainer(TLObject):
    ID: int = 0x73f1f8dc

    def __init__(self, messages: Any = None) -> None:
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.messages or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgContainer':
        messages = reader.read_vector(lambda r: reader.read_object())
        return cls(messages=messages)


@register_tl
class MsgCopy(TLObject):
    ID: int = 0xe06046b2

    def __init__(self, orig_message: Any = None) -> None:
        self.orig_message = orig_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.orig_message is not None and hasattr(self.orig_message, 'write'): self.orig_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgCopy':
        orig_message = reader.read_object()
        return cls(orig_message=orig_message)


@register_tl
class GzipPacked(TLObject):
    ID: int = 0x3072cfa1

    def __init__(self, packed_data: Any = None) -> None:
        self.packed_data = packed_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.packed_data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'GzipPacked':
        packed_data = reader.read_bytes()
        return cls(packed_data=packed_data)


@register_tl
class MsgsAck(TLObject):
    ID: int = 0x62d6b459

    def __init__(self, msg_ids: Any = None) -> None:
        self.msg_ids = msg_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.msg_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgsAck':
        msg_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(msg_ids=msg_ids)


@register_tl
class BadMsgNotification(TLObject):
    ID: int = 0xa7eff811

    def __init__(self, bad_msg_id: Any = None, bad_msg_seqno: Any = None, error_code: Any = None) -> None:
        self.bad_msg_id = bad_msg_id
        self.bad_msg_seqno = bad_msg_seqno
        self.error_code = error_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bad_msg_id or 0)
        writer.write_int32(self.bad_msg_seqno or 0)
        writer.write_int32(self.error_code or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BadMsgNotification':
        bad_msg_id = reader.read_int64()
        bad_msg_seqno = reader.read_int32()
        error_code = reader.read_int32()
        return cls(bad_msg_id=bad_msg_id, bad_msg_seqno=bad_msg_seqno, error_code=error_code)


@register_tl
class BadServerSalt(TLObject):
    ID: int = 0xedab447b

    def __init__(self, bad_msg_id: Any = None, bad_msg_seqno: Any = None, error_code: Any = None, new_server_salt: Any = None) -> None:
        self.bad_msg_id = bad_msg_id
        self.bad_msg_seqno = bad_msg_seqno
        self.error_code = error_code
        self.new_server_salt = new_server_salt

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bad_msg_id or 0)
        writer.write_int32(self.bad_msg_seqno or 0)
        writer.write_int32(self.error_code or 0)
        writer.write_int64(self.new_server_salt or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BadServerSalt':
        bad_msg_id = reader.read_int64()
        bad_msg_seqno = reader.read_int32()
        error_code = reader.read_int32()
        new_server_salt = reader.read_int64()
        return cls(bad_msg_id=bad_msg_id, bad_msg_seqno=bad_msg_seqno, error_code=error_code, new_server_salt=new_server_salt)


@register_tl
class MsgResendReq(TLObject):
    ID: int = 0x7d861a08

    def __init__(self, msg_ids: Any = None) -> None:
        self.msg_ids = msg_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.msg_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgResendReq':
        msg_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(msg_ids=msg_ids)


@register_tl
class MsgsStateReq(TLObject):
    ID: int = 0xda69fb52

    def __init__(self, msg_ids: Any = None) -> None:
        self.msg_ids = msg_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.msg_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgsStateReq':
        msg_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(msg_ids=msg_ids)


@register_tl
class MsgsStateInfo(TLObject):
    ID: int = 0x4deb57d

    def __init__(self, req_msg_id: Any = None, info: Any = None) -> None:
        self.req_msg_id = req_msg_id
        self.info = info

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.req_msg_id or 0)
        writer.write_bytes(self.info or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgsStateInfo':
        req_msg_id = reader.read_int64()
        info = reader.read_bytes()
        return cls(req_msg_id=req_msg_id, info=info)


@register_tl
class MsgsAllInfo(TLObject):
    ID: int = 0x8cc0d131

    def __init__(self, msg_ids: Any = None, info: Any = None) -> None:
        self.msg_ids = msg_ids
        self.info = info

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.msg_ids or [], lambda w, x: w.write_int64(x))
        writer.write_bytes(self.info or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgsAllInfo':
        msg_ids = reader.read_vector(lambda r: r.read_int64())
        info = reader.read_bytes()
        return cls(msg_ids=msg_ids, info=info)


@register_tl
class MsgDetailedInfo(TLObject):
    ID: int = 0x276d3ec6

    def __init__(self, msg_id: Any = None, answer_msg_id: Any = None, bytes: Any = None, status: Any = None) -> None:
        self.msg_id = msg_id
        self.answer_msg_id = answer_msg_id
        self.bytes = bytes
        self.status = status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.msg_id or 0)
        writer.write_int64(self.answer_msg_id or 0)
        writer.write_int32(self.bytes or 0)
        writer.write_int32(self.status or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgDetailedInfo':
        msg_id = reader.read_int64()
        answer_msg_id = reader.read_int64()
        bytes = reader.read_int32()
        status = reader.read_int32()
        return cls(msg_id=msg_id, answer_msg_id=answer_msg_id, bytes=bytes, status=status)


@register_tl
class MsgNewDetailedInfo(TLObject):
    ID: int = 0x809db6df

    def __init__(self, answer_msg_id: Any = None, bytes: Any = None, status: Any = None) -> None:
        self.answer_msg_id = answer_msg_id
        self.bytes = bytes
        self.status = status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.answer_msg_id or 0)
        writer.write_int32(self.bytes or 0)
        writer.write_int32(self.status or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MsgNewDetailedInfo':
        answer_msg_id = reader.read_int64()
        bytes = reader.read_int32()
        status = reader.read_int32()
        return cls(answer_msg_id=answer_msg_id, bytes=bytes, status=status)


@register_tl
class DestroyAuthKeyOk(TLObject):
    ID: int = 0xf660e1d4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DestroyAuthKeyOk':
        return cls()


@register_tl
class DestroyAuthKeyNone(TLObject):
    ID: int = 0xa9f2259

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DestroyAuthKeyNone':
        return cls()


@register_tl
class DestroyAuthKeyFail(TLObject):
    ID: int = 0xea109b13

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DestroyAuthKeyFail':
        return cls()


@register_tl
class HttpWait(TLObject):
    ID: int = 0x9299359f

    def __init__(self, max_delay: Any = None, wait_after: Any = None, max_wait: Any = None) -> None:
        self.max_delay = max_delay
        self.wait_after = wait_after
        self.max_wait = max_wait

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.max_delay or 0)
        writer.write_int32(self.wait_after or 0)
        writer.write_int32(self.max_wait or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HttpWait':
        max_delay = reader.read_int32()
        wait_after = reader.read_int32()
        max_wait = reader.read_int32()
        return cls(max_delay=max_delay, wait_after=wait_after, max_wait=max_wait)


@register_tl
class ReqPq(TLObject):
    ID: int = 0x60469778

    def __init__(self, nonce: Any = None) -> None:
        self.nonce = nonce

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReqPq':
        nonce = reader.read_int128()
        return cls(nonce=nonce)


@register_tl
class PQInnerData(TLObject):
    ID: int = 0x83c95aec

    def __init__(self, pq: Any = None, p: Any = None, q: Any = None, nonce: Any = None, server_nonce: Any = None, new_nonce: Any = None) -> None:
        self.pq = pq
        self.p = p
        self.q = q
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce = new_nonce

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.pq or b'')
        writer.write_bytes(self.p or b'')
        writer.write_bytes(self.q or b'')
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int256(self.new_nonce or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PQInnerData':
        pq = reader.read_bytes()
        p = reader.read_bytes()
        q = reader.read_bytes()
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce = reader.read_int256()
        return cls(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce)


@register_tl
class ServerDHParamsFail(TLObject):
    ID: int = 0x79bf00ee

    def __init__(self, nonce: Any = None, server_nonce: Any = None, new_nonce_hash: Any = None) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash = new_nonce_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce or 0)
        writer.write_int128(self.server_nonce or 0)
        writer.write_int128(self.new_nonce_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ServerDHParamsFail':
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        new_nonce_hash = reader.read_int128()
        return cls(nonce=nonce, server_nonce=server_nonce, new_nonce_hash=new_nonce_hash)

