import asyncio
import struct
from ..crypto.obfuscated2 import Obfuscated2
from ..errors import ConnectionError


class TCPTransport:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None
        self._obfuscation: Obfuscated2 | None = None

    async def connect(self, timeout: float = 10.0) -> None:
        try:
            self._reader, self._writer = await asyncio.wait_for(
                asyncio.open_connection(self.host, self.port),
                timeout=timeout,
            )
            self._obfuscation = Obfuscated2(b"\xee\xee\xee\xee")
            self._writer.write(self._obfuscation.header)
            await self._writer.drain()
        except Exception as e:
            await self.close()
            raise ConnectionError(f"Failed to connect to {self.host}:{self.port} - {e}") from e

    async def send(self, data: bytes) -> None:
        if not self._writer or not self._obfuscation:
            raise ConnectionError("Transport is not connected")
        length_header = struct.pack("<i", len(data))
        packet = length_header + data
        encrypted = self._obfuscation.encrypt(packet)
        self._writer.write(encrypted)
        await self._writer.drain()

    async def receive(self) -> bytes:
        if not self._reader or not self._obfuscation:
            raise ConnectionError("Transport is not connected")
        length_header_enc = await self._reader.readexactly(4)
        length_header = self._obfuscation.decrypt(length_header_enc)
        length = struct.unpack("<i", length_header)[0]
        if length <= 0 or length > 16 * 1024 * 1024:
            raise ValueError(f"Invalid frame length: {length}")
        payload_enc = await self._reader.readexactly(length)
        payload = self._obfuscation.decrypt(payload_enc)
        return payload

    async def close(self) -> None:
        if self._writer:
            try:
                self._writer.close()
                await self._writer.wait_closed()
            except Exception:
                pass
            self._writer = None
        self._reader = None
        self._obfuscation = None

    @property
    def is_connected(self) -> bool:
        return self._writer is not None and not self._writer.is_closing()
