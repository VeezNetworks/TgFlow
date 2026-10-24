from typing import Any
from .core import TLRequest, TLWriter, TLReader, register_tl


@register_tl
class ReqPqMulti(TLRequest):
    ID: int = 0xBE7E8EF1

    def __init__(self, nonce: bytes | int = b"\x00" * 16) -> None:
        self.nonce = nonce

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)

    @classmethod
    def read(cls, reader: TLReader) -> "ReqPqMulti":
        nonce = reader.read_int128()
        return cls(nonce=nonce)


@register_tl
class ReqDHParams(TLRequest):
    ID: int = 0xD712E4BE

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        p: bytes = b"",
        q: bytes = b"",
        public_key_fingerprint: int = 0,
        encrypted_data: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.p = p
        self.q = q
        self.public_key_fingerprint = public_key_fingerprint
        self.encrypted_data = encrypted_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_bytes(self.p)
        writer.write_bytes(self.q)
        writer.write_int64(self.public_key_fingerprint)
        writer.write_bytes(self.encrypted_data)

    @classmethod
    def read(cls, reader: TLReader) -> "ReqDHParams":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        p = reader.read_bytes()
        q = reader.read_bytes()
        public_key_fingerprint = reader.read_int64()
        encrypted_data = reader.read_bytes()
        return cls(
            nonce=nonce,
            server_nonce=server_nonce,
            p=p,
            q=q,
            public_key_fingerprint=public_key_fingerprint,
            encrypted_data=encrypted_data,
        )


@register_tl
class SetClientDHParams(TLRequest):
    ID: int = 0xF5045F1F

    def __init__(
        self,
        nonce: bytes | int = b"\x00" * 16,
        server_nonce: bytes | int = b"\x00" * 16,
        encrypted_data: bytes = b"",
    ) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_data = encrypted_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int128(self.nonce)
        writer.write_int128(self.server_nonce)
        writer.write_bytes(self.encrypted_data)

    @classmethod
    def read(cls, reader: TLReader) -> "SetClientDHParams":
        nonce = reader.read_int128()
        server_nonce = reader.read_int128()
        encrypted_data = reader.read_bytes()
        return cls(nonce=nonce, server_nonce=server_nonce, encrypted_data=encrypted_data)


@register_tl
class Ping(TLRequest):
    ID: int = 0x7ABE77EC

    def __init__(self, ping_id: int = 0) -> None:
        self.ping_id = ping_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.ping_id)

    @classmethod
    def read(cls, reader: TLReader) -> "Ping":
        ping_id = reader.read_int64()
        return cls(ping_id=ping_id)


@register_tl
class PingDelayDisconnect(TLRequest):
    ID: int = 0xF34277BC

    def __init__(self, ping_id: int = 0, disconnect_delay: int = 60) -> None:
        self.ping_id = ping_id
        self.disconnect_delay = disconnect_delay

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.ping_id)
        writer.write_int32(self.disconnect_delay)

    @classmethod
    def read(cls, reader: TLReader) -> "PingDelayDisconnect":
        ping_id = reader.read_int64()
        disconnect_delay = reader.read_int32()
        return cls(ping_id=ping_id, disconnect_delay=disconnect_delay)


@register_tl
class SendMessage(TLRequest):
    ID: int = 0x983F9745

    def __init__(
        self,
        peer: Any = None,
        message: str = "",
        random_id: int = 0,
        reply_to: Any = None,
        reply_markup: Any = None,
        entities: list[Any] | None = None,
        no_webpage: bool = False,
        silent: bool = False,
        background: bool = False,
        clear_draft: bool = False,
        noforwards: bool = False,
        invert_media: bool = False,
    ) -> None:
        self.peer = peer
        self.message = message
        self.random_id = random_id
        self.reply_to = reply_to
        self.reply_markup = reply_markup
        self.entities = entities
        self.no_webpage = no_webpage
        self.silent = silent
        self.background = background
        self.clear_draft = clear_draft
        self.noforwards = noforwards
        self.invert_media = invert_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 1)
        if self.silent:
            flags |= (1 << 5)
        if self.background:
            flags |= (1 << 6)
        if self.clear_draft:
            flags |= (1 << 7)
        if self.noforwards:
            flags |= (1 << 14)
        if self.invert_media:
            flags |= (1 << 16)
        if self.reply_to is not None:
            flags |= (1 << 0)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        if self.entities is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if hasattr(self.peer, "write"):
            self.peer.write(writer)
        if self.reply_to is not None:
            if hasattr(self.reply_to, "write"):
                self.reply_to.write(writer)
        writer.write_string(self.message)
        writer.write_int64(self.random_id)
        if self.reply_markup is not None:
            if hasattr(self.reply_markup, "write"):
                self.reply_markup.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities, lambda w, x: x.write(w) if hasattr(x, "write") else w.write_object(x))

    @classmethod
    def read(cls, reader: TLReader) -> "SendMessage":
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        clear_draft = bool(flags & (1 << 7))
        noforwards = bool(flags & (1 << 14))
        invert_media = bool(flags & (1 << 16))
        peer = reader.read_object()
        reply_to = reader.read_object() if (flags & (1 << 0)) else None
        message = reader.read_string()
        random_id = reader.read_int64()
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        entities = reader.read_vector(lambda r: r.read_object()) if (flags & (1 << 3)) else None
        return cls(
            peer=peer,
            message=message,
            random_id=random_id,
            reply_to=reply_to,
            reply_markup=reply_markup,
            entities=entities,
            no_webpage=no_webpage,
            silent=silent,
            background=background,
            clear_draft=clear_draft,
            noforwards=noforwards,
            invert_media=invert_media,
        )


@register_tl
class EditMessage(TLRequest):
    ID: int = 0x48F71778

    def __init__(
        self,
        peer: Any = None,
        id: int = 0,
        message: str | None = None,
        reply_markup: Any = None,
        entities: list[Any] | None = None,
        no_webpage: bool = False,
    ) -> None:
        self.peer = peer
        self.id = id
        self.message = message
        self.reply_markup = reply_markup
        self.entities = entities
        self.no_webpage = no_webpage

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 1)
        if self.message is not None:
            flags |= (1 << 11)
        if self.reply_markup is not None:
            flags |= (1 << 2)
        if self.entities is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if hasattr(self.peer, "write"):
            self.peer.write(writer)
        writer.write_int32(self.id)
        if self.message is not None:
            writer.write_string(self.message)
        if self.reply_markup is not None:
            if hasattr(self.reply_markup, "write"):
                self.reply_markup.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities, lambda w, x: x.write(w) if hasattr(x, "write") else w.write_object(x))

    @classmethod
    def read(cls, reader: TLReader) -> "EditMessage":
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        peer = reader.read_object()
        id = reader.read_int32()
        message = reader.read_string() if (flags & (1 << 11)) else None
        reply_markup = reader.read_object() if (flags & (1 << 2)) else None
        entities = reader.read_vector(lambda r: r.read_object()) if (flags & (1 << 3)) else None
        return cls(
            peer=peer,
            id=id,
            message=message,
            reply_markup=reply_markup,
            entities=entities,
            no_webpage=no_webpage,
        )


@register_tl
class DeleteMessages(TLRequest):
    ID: int = 0xE58E9536

    def __init__(self, id: list[int] | None = None, revoke: bool = True) -> None:
        self.id = id or []
        self.revoke = revoke

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoke:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.id, lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> "DeleteMessages":
        flags = reader.read_uint32()
        revoke = bool(flags & (1 << 0))
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(id=id, revoke=revoke)


@register_tl
class GetHistory(TLRequest):
    ID: int = 0x4423E6C5

    def __init__(
        self,
        peer: Any = None,
        offset_id: int = 0,
        offset_date: int = 0,
        add_offset: int = 0,
        limit: int = 100,
        max_id: int = 0,
        min_id: int = 0,
        hash: int = 0,
    ) -> None:
        self.peer = peer
        self.offset_id = offset_id
        self.offset_date = offset_date
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, "write"):
            self.peer.write(writer)
        writer.write_int32(self.offset_id)
        writer.write_int32(self.offset_date)
        writer.write_int32(self.add_offset)
        writer.write_int32(self.limit)
        writer.write_int32(self.max_id)
        writer.write_int32(self.min_id)
        writer.write_int64(self.hash)

    @classmethod
    def read(cls, reader: TLReader) -> "GetHistory":
        peer = reader.read_object()
        offset_id = reader.read_int32()
        offset_date = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        hash = reader.read_int64()
        return cls(
            peer=peer,
            offset_id=offset_id,
            offset_date=offset_date,
            add_offset=add_offset,
            limit=limit,
            max_id=max_id,
            min_id=min_id,
            hash=hash,
        )
