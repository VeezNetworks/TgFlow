import hashlib
import struct


def compute_msg_key(auth_key: bytes, msg_key_large: bytes, is_outgoing: bool) -> tuple[bytes, bytes]:
    x = 0 if is_outgoing else 8
    sha256_a = hashlib.sha256(msg_key_large + auth_key[x : x + 36]).digest()
    sha256_b = hashlib.sha256(auth_key[x + 40 : x + 76] + msg_key_large).digest()

    aes_key = sha256_a[:8] + sha256_b[8:24] + sha256_a[24:32]
    aes_iv = sha256_b[:8] + sha256_a[8:24] + sha256_b[24:32]
    return aes_key, aes_iv


def compute_auth_key_id(auth_key: bytes) -> int:
    digest = hashlib.sha1(auth_key).digest()
    return struct.unpack("<Q", digest[-8:])[0]


def perform_dh_step(g: int, b: int, dh_prime: int) -> int:
    return pow(g, b, dh_prime)
