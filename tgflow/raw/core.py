import io
import struct
from typing import Any, Callable, TypeVar, Union

T = TypeVar("T")


class TLWriter:
    def __init__(self):
        self._buf = io.BytesIO()

    def getvalue(self) -> bytes:
        return self._buf.getvalue()

    def write_int(self, value: int, signed: bool = True) -> None:
        self._buf.write(struct.pack("<i" if signed else "<I", value))

    def write_long(self, value: int, signed: bool = True) -> None:
        self._buf.write(struct.pack("<q" if signed else "<Q", value))

    def write_int128(self, value: bytes) -> None:
        if len(value) != 16:
            raise ValueError("int128 requires exactly 16 bytes")
        self._buf.write(value)

    def write_int256(self, value: bytes) -> None:
        if len(value) != 32:
            raise ValueError("int256 requires exactly 32 bytes")
        self._buf.write(value)

    def write_double(self, value: float) -> None:
        self._buf.write(struct.pack("<d", value))

    def write_bool(self, value: bool) -> None:
        # boolFalse = 0xbc799737, boolTrue = 0x997275b5
        self.write_int(0x997275B5 if value else 0xBC799737, signed=False)

    def write_bytes(self, data: bytes) -> None:
        length = len(data)
        if length < 254:
            self._buf.write(bytes([length]))
            self._buf.write(data)
            pad = (4 - (length + 1) % 4) % 4
            if pad:
                self._buf.write(b"\x00" * pad)
        else:
            self._buf.write(bytes([254, length & 0xFF, (length >> 8) & 0xFF, (length >> 16) & 0xFF]))
            self._buf.write(data)
            pad = (4 - length % 4) % 4
            if pad:
                self._buf.write(b"\x00" * pad)

    def write_string(self, text: str) -> None:
        self.write_bytes(text.encode("utf-8"))

    def write_vector(self, items: list[Any], writer_func: Callable[[Any], None]) -> None:
        self.write_int(0x1CB5C415, signed=False)
        self.write_int(len(items))
        for item in items:
            writer_func(item)

    def write_object(self, obj: Any) -> None:
        if hasattr(obj, "write"):
            obj.write(self)
        elif isinstance(obj, bool):
            self.write_bool(obj)
        elif isinstance(obj, int):
            self.write_int(obj)
        elif isinstance(obj, str):
            self.write_string(obj)
        elif isinstance(obj, bytes):
            self.write_bytes(obj)


class TLReader:
    def __init__(self, data: bytes):
        self._stream = io.BytesIO(data)

    def read_int(self, signed: bool = True) -> int:
        raw = self._stream.read(4)
        if len(raw) < 4:
            raise EOFError("Unexpected EOF while reading int")
        return struct.unpack("<i" if signed else "<I", raw)[0]

    def read_long(self, signed: bool = True) -> int:
        raw = self._stream.read(8)
        if len(raw) < 8:
            raise EOFError("Unexpected EOF while reading long")
        return struct.unpack("<q" if signed else "<Q", raw)[0]

    def read_int128(self) -> bytes:
        raw = self._stream.read(16)
        if len(raw) < 16:
            raise EOFError("Unexpected EOF while reading int128")
        return raw

    def read_int256(self) -> bytes:
        raw = self._stream.read(32)
        if len(raw) < 32:
            raise EOFError("Unexpected EOF while reading int256")
        return raw

    def read_double(self) -> float:
        raw = self._stream.read(8)
        if len(raw) < 8:
            raise EOFError("Unexpected EOF while reading double")
        return struct.unpack("<d", raw)[0]

    def read_bool(self) -> bool:
        ctor = self.read_int(signed=False)
        return ctor == 0x997275B5

    def read_bytes(self) -> bytes:
        first = self._stream.read(1)
        if not first:
            raise EOFError("Unexpected EOF while reading byte length")
        length = first[0]
        if length < 254:
            data = self._stream.read(length)
            pad = (4 - (length + 1) % 4) % 4
            if pad:
                self._stream.read(pad)
            return data
        else:
            len_bytes = self._stream.read(3)
            if len(len_bytes) < 3:
                raise EOFError("Unexpected EOF while reading extended bytes length")
            length = len_bytes[0] | (len_bytes[1] << 8) | (len_bytes[2] << 16)
            data = self._stream.read(length)
            pad = (4 - length % 4) % 4
            if pad:
                self._stream.read(pad)
            return data

    def read_string(self) -> str:
        return self.read_bytes().decode("utf-8", errors="replace")

    def read_vector(self, item_reader: Callable[["TLReader"], T]) -> list[T]:
        ctor = self.read_int(signed=False)
        if ctor != 0x1CB5C415:
            raise ValueError(f"Invalid vector constructor: 0x{ctor:08x}")
        count = self.read_int()
        return [item_reader(self) for _ in range(count)]


class TLObject:
    ID: int = 0
    QUALNAME: str = "TLObject"

    def write(self, writer: TLWriter) -> None:
        writer.write_int(self.ID, signed=False)

    @classmethod
    def read(cls, reader: TLReader) -> Any:
        raise NotImplementedError


class TLRequest(TLObject):
    def read_result(self, reader: TLReader) -> Any:
        return reader.read_int(signed=False)
