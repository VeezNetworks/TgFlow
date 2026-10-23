import base64
import struct
import time
import zlib
from dataclasses import dataclass
from typing import Optional


MAGIC = b"TGFL"
VERSION = 1


@dataclass(slots=True)
class SessionData:
    dc_id: int
    test_mode: bool
    is_bot: bool
    api_id: int
    user_id: int
    auth_key: bytes
    created_at: int = 0


def encode_session(data: SessionData) -> str:
    if len(data.auth_key) != 256:
        raise ValueError(f"Auth key must be exactly 256 bytes, got {len(data.auth_key)}")

    flags = (1 if data.test_mode else 0) | ((1 if data.is_bot else 0) << 1)
    timestamp = data.created_at or int(time.time())

    # Pack: MAGIC(4B) + Version(1B) + DC(1B) + Flags(1B) + API_ID(4B) + UserID(8B) + AuthKey(256B) + Timestamp(4B)
    header = struct.pack(
        "<4sBBB IQ",
        MAGIC,
        VERSION,
        data.dc_id,
        flags,
        data.api_id,
        data.user_id,
    )
    payload_body = header + data.auth_key + struct.pack("<I", timestamp)
    checksum = zlib.crc32(payload_body) & 0xFFFFFFFF
    full_payload = payload_body + struct.pack("<I", checksum)

    token_b64 = base64.urlsafe_b64encode(full_payload).decode("ascii").rstrip("=")
    prefix = "tgflow_test_" if data.test_mode else "tgflow_live_"
    return f"{prefix}{token_b64}"


def decode_session(token: str) -> SessionData:
    token = token.strip()
    if not token.startswith(("tgflow_live_", "tgflow_test_")):
        raise ValueError("Invalid TgFlow session token prefix. Expected 'tgflow_live_' or 'tgflow_test_'")

    is_test_prefix = token.startswith("tgflow_test_")
    raw_b64 = token.split("_", 2)[2]

    # Add back padding
    pad_len = (4 - len(raw_b64) % 4) % 4
    raw_bytes = base64.urlsafe_b64decode(raw_b64 + ("=" * pad_len))

    if len(raw_bytes) != 283:
        raise ValueError(f"Malformed TgFlow session token payload length: {len(raw_bytes)} bytes (expected 283)")

    body, expected_checksum = raw_bytes[:-4], raw_bytes[-4:]
    actual_crc = zlib.crc32(body) & 0xFFFFFFFF
    exp_crc = struct.unpack("<I", expected_checksum)[0]

    if actual_crc != exp_crc:
        raise ValueError("TgFlow session token checksum failed. Token is corrupted or truncated.")

    magic, version, dc_id, flags, api_id, user_id = struct.unpack("<4sBBB IQ", body[:19])
    if magic != MAGIC or version != VERSION:
        raise ValueError(f"Unsupported TgFlow session version or magic: {magic!r} v{version}")

    auth_key = body[19 : 19 + 256]
    timestamp = struct.unpack("<I", body[19 + 256 :])[0]

    test_mode = bool(flags & 1) or is_test_prefix
    is_bot = bool((flags >> 1) & 1)

    return SessionData(
        dc_id=dc_id,
        test_mode=test_mode,
        is_bot=is_bot,
        api_id=api_id,
        user_id=user_id,
        auth_key=auth_key,
        created_at=timestamp,
    )


def generate_new_session(
    api_id: int,
    user_id: int,
    dc_id: int = 2,
    is_bot: bool = False,
    test_mode: bool = False,
    auth_key: Optional[bytes] = None,
) -> str:
    import os

    key = auth_key or os.urandom(256)
    data = SessionData(
        dc_id=dc_id,
        test_mode=test_mode,
        is_bot=is_bot,
        api_id=api_id,
        user_id=user_id,
        auth_key=key,
        created_at=int(time.time()),
    )
    return encode_session(data)


if __name__ == "__main__":
    print("=" * 60)
    print("TgFlow Interactive Session Generator")
    print("=" * 60)
    try:
        raw_api_id = input("Enter API ID: ").strip()
        api_id = int(raw_api_id) if raw_api_id else 123456
        raw_uid = input("Enter User ID or Bot ID: ").strip()
        uid = int(raw_uid) if raw_uid else 999123456
        mode = input("Is this a bot token session? (y/N): ").strip().lower()
        is_bot = mode.startswith("y")
        test_in = input("Use Telegram Test DC? (y/N): ").strip().lower()
        test_mode = test_in.startswith("y")

        token = generate_new_session(
            api_id=api_id,
            user_id=uid,
            dc_id=2,
            is_bot=is_bot,
            test_mode=test_mode,
        )

        print("\n" + "-" * 60)
        print("Your Unique TgFlow Session Token:")
        print("-" * 60)
        print(token)
        print("-" * 60)
        print("Save this securely. Use in your code as:")
        print(f'client = TgFlow(session="{token}")')
        print("=" * 60)
    except (KeyboardInterrupt, EOFError):
        print("\nAborted.")
