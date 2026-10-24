import hashlib
import os
import struct
from ..crypto.aes_ige import aes_ige_encrypt, aes_ige_decrypt
from ..crypto.diffie_hellman import derive_keys, compute_auth_key_id
from ..errors import SecurityError


class PacketCodec:
    @staticmethod
    def pack_unencrypted(msg_id: int, data: bytes) -> bytes:
        header = struct.pack("<q q i", 0, msg_id, len(data))
        return header + data

    @staticmethod
    def unpack_unencrypted(data: bytes) -> tuple[int, bytes]:
        if len(data) < 20:
            raise ValueError("Unencrypted packet is too short")
        auth_key_id, msg_id, length = struct.unpack_from("<q q i", data, 0)
        if auth_key_id != 0:
            raise ValueError("Expected unencrypted packet with auth_key_id == 0")
        payload = data[20:20 + length]
        return msg_id, payload

    @staticmethod
    def pack_encrypted(
        auth_key: bytes,
        salt: int,
        session_id: int,
        msg_id: int,
        seq_no: int,
        data: bytes,
    ) -> bytes:
        payload_header = struct.pack("<q q q i i", salt, session_id, msg_id, seq_no, len(data))
        inner_data = payload_header + data
        padding_size = (16 - (len(inner_data) % 16))
        if padding_size < 12:
            padding_size += 16
        padding = os.urandom(padding_size)
        plaintext = inner_data + padding

        msg_key_large = hashlib.sha256(auth_key[88:88 + 32] + plaintext).digest()
        msg_key = msg_key_large[8:24]

        aes_key, aes_iv = derive_keys(auth_key, msg_key, to_server=True)
        ciphertext = aes_ige_encrypt(plaintext, aes_key, aes_iv)

        auth_key_id = compute_auth_key_id(auth_key)
        auth_key_bytes = struct.pack("<q", auth_key_id)
        return auth_key_bytes + msg_key + ciphertext

    @staticmethod
    def unpack_encrypted(auth_key: bytes, data: bytes) -> tuple[int, int, int, int, bytes]:
        if len(data) < 24:
            raise ValueError("Encrypted packet is too short")
        expected_auth_key_id = compute_auth_key_id(auth_key)
        auth_key_id = struct.unpack_from("<q", data, 0)[0]
        if auth_key_id != expected_auth_key_id:
            raise SecurityError("auth_key_id mismatch")

        msg_key = data[8:24]
        ciphertext = data[24:]
        if len(ciphertext) % 16 != 0:
            raise ValueError("Ciphertext length must be multiple of 16")

        aes_key, aes_iv = derive_keys(auth_key, msg_key, to_server=False)
        plaintext = aes_ige_decrypt(ciphertext, aes_key, aes_iv)

        check_msg_key = hashlib.sha256(auth_key[96:96 + 32] + plaintext).digest()[8:24]
        if check_msg_key != msg_key:
            raise SecurityError("msg_key verification failed")

        salt, session_id, msg_id, seq_no, length = struct.unpack_from("<q q q i i", plaintext, 0)
        payload = plaintext[32:32 + length]
        return salt, session_id, msg_id, seq_no, payload
