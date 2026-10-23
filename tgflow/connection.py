import asyncio
import os
import struct
import time
from typing import Optional
from tgflow.crypto.obfuscated2 import Obfuscated2Stream
from tgflow.errors import ConnectionClosed


DC_MAP_PROD = {
    1: ("149.154.175.50", 443),
    2: ("149.154.167.51", 443),
    3: ("149.154.175.100", 443),
    4: ("149.154.167.91", 443),
    5: ("91.108.56.165", 443),
}

DC_MAP_TEST = {
    1: ("149.154.175.10", 443),
    2: ("149.154.167.40", 443),
    3: ("149.154.175.117", 443),
}


class TCPConnection:
    def __init__(self, ip: str, port: int = 443, use_obfuscation: bool = True):
        self.ip = ip
        self.port = port
        self.use_obfuscation = use_obfuscation
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None
        self.stream: Optional[Obfuscated2Stream] = None
        self._connected = False

    async def connect(self, timeout: float = 10.0) -> None:
        self.reader, self.writer = await asyncio.wait_for(
            asyncio.open_connection(self.ip, self.port),
            timeout=timeout,
        )

        if self.use_obfuscation:
            self.stream = Obfuscated2Stream(self.reader, self.writer)
            await self.stream.handshake()
        else:
            self.writer.write(b"\xef")
            await self.writer.drain()

        self._connected = True

    async def send(self, data: bytes) -> None:
        if not self._connected or not self.writer:
            raise ConnectionClosed("Socket is not connected")

        if self.stream:
            await self.stream.send_packet(data)
        else:
            length = len(data) // 4
            if length < 127:
                header = struct.pack("B", length)
            else:
                header = b"\x7f" + struct.pack("<I", length)[:3]
            self.writer.write(header + data)
            await self.writer.drain()

    async def receive(self) -> bytes:
        if not self._connected or not self.reader:
            raise ConnectionClosed("Socket is not connected")

        if self.stream:
            return await self.stream.read_packet()

        first_byte = await self.reader.readexactly(1)
        length = first_byte[0]
        if length == 127:
            length_bytes = await self.reader.readexactly(3)
            length = struct.unpack("<I", length_bytes + b"\x00")[0]

        return await self.reader.readexactly(length * 4)

    async def close(self) -> None:
        self._connected = False
        if self.writer:
            try:
                self.writer.close()
                await self.writer.wait_closed()
            except Exception:
                pass
            self.writer = None
            self.reader = None
