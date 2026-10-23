import asyncio
import os
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Obfuscated2Stream:
    PROTOCOL_INTERMEDIATE = b"\xee\xee\xee\xee"
    PROTOCOL_PADDED = b"\xdd\xdd\xdd\xdd"

    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.reader = reader
        self.writer = writer
        self._encryptor = None
        self._decryptor = None

    async def handshake(self) -> None:
        while True:
            init = bytearray(os.urandom(64))
            val = struct.unpack("<I", init[:4])[0]
            val2 = struct.unpack("<I", init[4:8])[0]
            if init[0] != 0xEF and val not in (0x44414548, 0x54534F50, 0x20544547, 0x4954504F) and val2 != 0:
                init[56:60] = self.PROTOCOL_PADDED
                break

        key_enc = bytes(init[8:40])
        iv_enc = bytes(init[40:56])

        reversed_init = bytes(init[8:56])[::-1]
        key_dec = reversed_init[:32]
        iv_dec = reversed_init[32:48]

        self._encryptor = Cipher(algorithms.AES(key_enc), modes.CTR(iv_enc)).encryptor()
        self._decryptor = Cipher(algorithms.AES(key_dec), modes.CTR(iv_dec)).decryptor()

        encrypted_tail = self._encryptor.update(bytes(init[56:]))
        init[56:] = encrypted_tail

        self.writer.write(init)
        await self.writer.drain()

    async def send_packet(self, payload: bytes) -> None:
        pad_len = len(payload) % 16
        padding = os.urandom(pad_len)
        frame = payload + padding
        raw = struct.pack("<I", len(frame)) + frame
        self.writer.write(self._encryptor.update(raw))
        await self.writer.drain()

    async def read_packet(self) -> bytes:
        raw_len = await self.reader.readexactly(4)
        dec_len = self._decryptor.update(raw_len)
        length = struct.unpack("<I", dec_len)[0]
        encrypted_payload = await self.reader.readexactly(length)
        return self._decryptor.update(encrypted_payload)
