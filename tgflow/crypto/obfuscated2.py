import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Obfuscated2:
    def __init__(self, protocol_tag: bytes = b"\xee\xee\xee\xee") -> None:
        while True:
            init = bytearray(os.urandom(64))
            if init[0] == 0xef:
                continue
            first4 = bytes(init[:4])
            if first4 in (b"HEAD", b"POST", b"GET ", b"\xee\xee\xee\xee", b"\xdd\xdd\xdd\xdd"):
                continue
            if bytes(init[4:8]) == b"\x00\x00\x00\x00":
                continue
            break

        init[56:60] = protocol_tag
        enc_key = bytes(init[8:40])
        enc_iv = bytes(init[40:56])
        self._encryptor = Cipher(algorithms.AES(enc_key), modes.CTR(enc_iv)).encryptor()

        rev = bytes(init[55:7:-1])
        dec_key = bytes(rev[:32])
        dec_iv = bytes(rev[32:48])
        self._decryptor = Cipher(algorithms.AES(dec_key), modes.CTR(dec_iv)).decryptor()

        encrypted_init = self._encryptor.update(bytes(init))
        init[56:64] = encrypted_init[56:64]
        self.header = bytes(init)

    def encrypt(self, data: bytes) -> bytes:
        return self._encryptor.update(data)

    def decrypt(self, data: bytes) -> bytes:
        return self._decryptor.update(data)
