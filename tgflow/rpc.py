import os
import struct
import time
from typing import Any, Optional


REQ_PQ_MULTI_CONSTRUCTOR = 0xBE7E8EF1
RES_PQ_CONSTRUCTOR = 0x05162463


class RPCMessage:
    def __init__(self, msg_id: int, seq_no: int, body: bytes):
        self.msg_id = msg_id
        self.seq_no = seq_no
        self.body = body


class RPCEngine:
    def __init__(self, session_id: Optional[int] = None):
        self.session_id = session_id or int.from_bytes(os.urandom(8), "little")
        self.last_msg_id = 0
        self.sequence_number = 0
        self.salt = 0

    def generate_msg_id(self) -> int:
        now = time.time()
        nanos = int(now * 4294967296)
        if nanos <= self.last_msg_id:
            nanos = self.last_msg_id + 4
        self.last_msg_id = nanos
        return nanos

    def build_unencrypted_message(self, data: bytes) -> bytes:
        msg_id = self.generate_msg_id()
        header = struct.pack("<QQI", 0, msg_id, len(data))
        return header + data

    def parse_unencrypted_message(self, raw: bytes) -> tuple[int, bytes]:
        if len(raw) < 20:
            raise ValueError(f"Packet too short for unencrypted message: {len(raw)} bytes")

        auth_key_id, msg_id, length = struct.unpack("<QQI", raw[:20])
        if auth_key_id != 0:
            raise ValueError(f"Expected unencrypted auth_key_id 0, got {auth_key_id}")

        body = raw[20 : 20 + length]
        return msg_id, body

    @staticmethod
    def build_req_pq_multi(nonce: bytes) -> bytes:
        if len(nonce) != 16:
            raise ValueError("Nonce must be 16 bytes")
        return struct.pack("<I", REQ_PQ_MULTI_CONSTRUCTOR) + nonce

    @staticmethod
    def parse_res_pq(data: bytes) -> dict[str, Any]:
        if len(data) < 20:
            raise ValueError("Data too short for resPQ")

        constructor = struct.unpack("<I", data[:4])[0]
        if constructor != RES_PQ_CONSTRUCTOR:
            raise ValueError(f"Unexpected constructor: {hex(constructor)}, expected {hex(RES_PQ_CONSTRUCTOR)}")

        nonce = data[4:20]
        server_nonce = data[20:36]

        offset = 36
        pq_len = data[offset]
        offset += 1
        pq_bytes = data[offset : offset + pq_len]
        offset += pq_len

        padding = (4 - ((pq_len + 1) % 4)) % 4
        offset += padding

        vector_constructor = struct.unpack("<I", data[offset : offset + 4])[0]
        offset += 4

        count = struct.unpack("<I", data[offset : offset + 4])[0]
        offset += 4

        fingerprints = []
        for _ in range(count):
            fp = struct.unpack("<Q", data[offset : offset + 8])[0]
            fingerprints.append(fp)
            offset += 8

        return {
            "constructor": constructor,
            "nonce": nonce,
            "server_nonce": server_nonce,
            "pq": int.from_bytes(pq_bytes, "big"),
            "pq_bytes": pq_bytes,
            "fingerprints": fingerprints,
        }
