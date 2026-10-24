import hashlib
import os


def derive_keys(auth_key: bytes, msg_key: bytes, to_server: bool) -> tuple[bytes, bytes]:
    x = 0 if to_server else 8
    sha256_a = hashlib.sha256(msg_key + auth_key[x:x + 36]).digest()
    sha256_b = hashlib.sha256(auth_key[40 + x:40 + x + 36] + msg_key).digest()
    aes_key = sha256_a[:8] + sha256_b[8:24] + sha256_a[24:32]
    aes_iv = sha256_b[:8] + sha256_a[8:24] + sha256_b[24:32]
    return aes_key, aes_iv


def compute_auth_key_id(auth_key: bytes) -> int:
    digest = hashlib.sha1(auth_key).digest()
    return int.from_bytes(digest[-8:], "little", signed=True)


def create_auth_key(server_b: int, client_a: int, dh_prime: int) -> bytes:
    shared_key = pow(server_b, client_a, dh_prime)
    key_bytes = shared_key.to_bytes(256, "big")
    return key_bytes


def generate_nonce(size: int = 16) -> bytes:
    return os.urandom(size)
