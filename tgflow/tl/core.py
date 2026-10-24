import io
import struct
from typing import Any, Callable, TypeVar, Type

T = TypeVar("T", bound="TLObject")

REGISTRY: dict[int, Type["TLObject"]] = {}


class TLObject:
    ID: int = 0

    def write(self, writer: "TLWriter") -> None:
        raise NotImplementedError

    @classmethod
    def read(cls: Type[T], reader: "TLReader") -> T:
        raise NotImplementedError

    def to_bytes(self) -> bytes:
        writer = TLWriter()
        self.write(writer)
        return writer.getvalue()


class TLRequest(TLObject):
    RESPONSE_TYPE: Any = None


def register_tl(cls: Type[T]) -> Type[T]:
    if cls.ID:
        REGISTRY[cls.ID] = cls
    return cls


class TLWriter:
    def __init__(self) -> None:
        self._buf = io.BytesIO()

    def write_int32(self, val: int) -> None:
        self._buf.write(struct.pack("<i", val))

    def write_uint32(self, val: int) -> None:
        self._buf.write(struct.pack("<I", val))

    def write_int64(self, val: int) -> None:
        self._buf.write(struct.pack("<q", val))

    def write_uint64(self, val: int) -> None:
        self._buf.write(struct.pack("<Q", val))

    def write_int128(self, val: int | bytes) -> None:
        if isinstance(val, bytes):
            if len(val) != 16:
                raise ValueError("int128 bytes must be length 16")
            self._buf.write(val)
        else:
            self._buf.write(val.to_bytes(16, "little", signed=False))

    def write_int256(self, val: int | bytes) -> None:
        if isinstance(val, bytes):
            if len(val) != 32:
                raise ValueError("int256 bytes must be length 32")
            self._buf.write(val)
        else:
            self._buf.write(val.to_bytes(32, "little", signed=False))

    def write_double(self, val: float) -> None:
        self._buf.write(struct.pack("<d", val))

    def write_bool(self, val: bool) -> None:
        self.write_uint32(0x997275B5 if val else 0xBC799737)

    def write_bytes(self, val: bytes) -> None:
        length = len(val)
        if length <= 253:
            padding = (4 - (1 + length) % 4) % 4
            self._buf.write(bytes([length]) + val + b"\x00" * padding)
        else:
            padding = (4 - (4 + length) % 4) % 4
            self._buf.write(bytes([254]) + length.to_bytes(3, "little") + val + b"\x00" * padding)

    def write_string(self, val: str) -> None:
        self.write_bytes(val.encode("utf-8"))

    def write_vector(self, items: list[Any], item_writer: Callable[["TLWriter", Any], None]) -> None:
        self.write_uint32(0x1CB5C415)
        self.write_int32(len(items))
        for item in items:
            item_writer(self, item)

    def write_object(self, obj: TLObject) -> None:
        obj.write(self)

    def getvalue(self) -> bytes:
        return self._buf.getvalue()


class TLReader:
    def __init__(self, data: bytes) -> None:
        self._buf = io.BytesIO(data)

    def read(self, n: int) -> bytes:
        res = self._buf.read(n)
        if len(res) < n:
            raise EOFError("Unexpected EOF while reading TL payload")
        return res

    def read_int32(self) -> int:
        return struct.unpack("<i", self.read(4))[0]

    def read_uint32(self) -> int:
        return struct.unpack("<I", self.read(4))[0]

    def read_int64(self) -> int:
        return struct.unpack("<q", self.read(8))[0]

    def read_uint64(self) -> int:
        return struct.unpack("<Q", self.read(8))[0]

    def read_int128(self) -> bytes:
        return self.read(16)

    def read_int256(self) -> bytes:
        return self.read(32)

    def read_double(self) -> float:
        return struct.unpack("<d", self.read(8))[0]

    def read_bool(self) -> bool:
        cid = self.read_uint32()
        if cid == 0x997275B5:
            return True
        if cid == 0xBC799737:
            return False
        raise ValueError(f"Invalid boolean constructor: {hex(cid)}")

    def read_bytes(self) -> bytes:
        first = self.read(1)[0]
        if first <= 253:
            length = first
            data = self.read(length)
            padding = (4 - (1 + length) % 4) % 4
            self.read(padding)
            return data
        else:
            len_bytes = self.read(3)
            length = int.from_bytes(len_bytes, "little")
            data = self.read(length)
            padding = (4 - (4 + length) % 4) % 4
            self.read(padding)
            return data

    def read_string(self) -> str:
        return self.read_bytes().decode("utf-8", errors="replace")

    def read_vector(self, item_reader: Callable[["TLReader"], Any]) -> list[Any]:
        cid = self.read_uint32()
        if cid != 0x1CB5C415:
            raise ValueError(f"Invalid vector constructor: {hex(cid)}")
        count = self.read_int32()
        return [item_reader(self) for _ in range(count)]

    def read_object(self) -> Any:
        cid = self.read_uint32()
        cls = REGISTRY.get(cid)
        if not cls:
            raise KeyError(f"Unknown TL constructor ID: {hex(cid)}")
        return cls.read(self)

    def has_remaining(self) -> bool:
        curr = self._buf.tell()
        self._buf.seek(0, io.SEEK_END)
        end = self._buf.tell()
        self._buf.seek(curr)
        return curr < end
