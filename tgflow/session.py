import base64
import os
import struct
import zlib
from typing import Optional

DEFAULT_DCS = {
    1: "149.154.175.53",
    2: "149.154.167.50",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
}

DEFAULT_TEST_DCS = {
    1: "149.154.175.10",
    2: "149.154.167.40",
    3: "149.154.175.117",
}


class Session:
    def __init__(
        self,
        name: str = "tgflow",
        dc_id: int = 2,
        server_address: str | None = None,
        port: int = 443,
        auth_key: bytes | None = None,
        is_bot: bool = False,
        user_id: int = 0,
        test_mode: bool = False,
    ) -> None:
        self.name = name
        self.dc_id = dc_id
        self.test_mode = test_mode
        if server_address is None:
            dc_map = DEFAULT_TEST_DCS if test_mode else DEFAULT_DCS
            self.server_address = dc_map.get(dc_id, "149.154.167.50")
        else:
            self.server_address = server_address
        self.port = port
        self.auth_key = auth_key
        self.is_bot = is_bot
        self.user_id = user_id
        self.salt: int = 0
        self.session_id: int = int.from_bytes(os.urandom(8), "little")

    def export_string(self) -> str:
        if not self.auth_key or len(self.auth_key) != 256:
            raise ValueError("Cannot export session without valid 256-byte auth_key")
        addr_bytes = self.server_address.encode("ascii")
        prefix = "tgflow_test_" if self.test_mode else "tgflow_live_"
        payload = struct.pack(
            f">B H B Q B {len(addr_bytes)}s 256s",
            self.dc_id,
            self.port,
            1 if self.is_bot else 0,
            self.user_id,
            len(addr_bytes),
            addr_bytes,
            self.auth_key,
        )
        checksum = struct.pack(">I", zlib.crc32(payload))
        encoded = base64.urlsafe_b64encode(payload + checksum).decode("ascii").rstrip("=")
        return prefix + encoded

    @classmethod
    def from_string(cls, session_str: str) -> "Session":
        session_str = session_str.strip()
        test_mode = False
        if session_str.startswith("tgflow_test_"):
            test_mode = True
            token = session_str[len("tgflow_test_"):]
        elif session_str.startswith("tgflow_live_"):
            token = session_str[len("tgflow_live_"):]
        else:
            token = session_str

        pad = len(token) % 4
        if pad:
            token += "=" * (4 - pad)
        raw = base64.urlsafe_b64decode(token.encode("ascii"))
        if len(raw) < 4:
            raise ValueError("Invalid session string: too short")
        payload = raw[:-4]
        expected_crc = struct.unpack(">I", raw[-4:])[0]
        actual_crc = zlib.crc32(payload)
        if actual_crc != expected_crc:
            raise ValueError("Session integrity verification failed: CRC32 mismatch")

        dc_id, port, is_bot_int, user_id, addr_len = struct.unpack_from(">B H B Q B", payload, 0)
        offset = 1 + 2 + 1 + 8 + 1
        addr_bytes = payload[offset:offset + addr_len]
        server_address = addr_bytes.decode("ascii")
        offset += addr_len
        auth_key = payload[offset:offset + 256]

        session = cls(
            name="imported",
            dc_id=dc_id,
            server_address=server_address,
            port=port,
            auth_key=auth_key,
            is_bot=bool(is_bot_int),
            user_id=user_id,
            test_mode=test_mode,
        )
        return session

    def save_file(self, path: str) -> None:
        token = self.export_string()
        with open(path, "w", encoding="utf-8") as f:
            f.write(token)

    @classmethod
    def load_file(cls, path: str) -> "Session":
        with open(path, "r", encoding="utf-8") as f:
            token = f.read().strip()
        return cls.from_string(token)
