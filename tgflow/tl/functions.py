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


@register_tl
class GetGroupCall(TLRequest):
    ID: int = 0x4124C316
    def __init__(self, call: Any = None, limit: int = 100) -> None:
        self.call = call
        self.limit = limit
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.call)
        writer.write_int32(self.limit)
    @classmethod
    def read(cls, reader: TLReader) -> "GetGroupCall":
        call = reader.read_object()
        limit = reader.read_int32()
        return cls(call=call, limit=limit)


@register_tl
class GetGroupParticipants(TLRequest):
    ID: int = 0xC555C878
    def __init__(
        self,
        call: Any = None,
        ids: list[Any] | None = None,
        sources: list[int] | None = None,
        offset: str = "",
        limit: int = 100,
    ) -> None:
        self.call = call
        self.ids = ids or []
        self.sources = sources or []
        self.offset = offset
        self.limit = limit
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.call)
        writer.write_vector(self.ids, lambda w, x: w.write_object(x))
        writer.write_vector(self.sources, lambda w, x: w.write_int32(x))
        writer.write_string(self.offset)
        writer.write_int32(self.limit)
    @classmethod
    def read(cls, reader: TLReader) -> "GetGroupParticipants":
        call = reader.read_object()
        ids = reader.read_vector(lambda r: r.read_object())
        sources = reader.read_vector(lambda r: r.read_int32())
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(call=call, ids=ids, sources=sources, offset=offset, limit=limit)


@register_tl
class JoinGroupCall(TLRequest):
    ID: int = 0xB132FF7B
    def __init__(
        self,
        call: Any = None,
        join_as: Any = None,
        params: Any = None,
        invite_hash: str | None = None,
        muted: bool = False,
        video_stopped: bool = False,
    ) -> None:
        self.call = call
        self.join_as = join_as
        self.params = params
        self.invite_hash = invite_hash
        self.muted = muted
        self.video_stopped = video_stopped
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.muted:
            flags |= (1 << 0)
        if self.video_stopped:
            flags |= (1 << 2)
        if self.invite_hash is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_object(self.call)
        writer.write_object(self.join_as)
        if self.invite_hash is not None:
            writer.write_string(self.invite_hash)
        writer.write_object(self.params)
    @classmethod
    def read(cls, reader: TLReader) -> "JoinGroupCall":
        flags = reader.read_uint32()
        muted = bool(flags & (1 << 0))
        video_stopped = bool(flags & (1 << 2))
        call = reader.read_object()
        join_as = reader.read_object()
        invite_hash = reader.read_string() if (flags & (1 << 1)) else None
        params = reader.read_object()
        return cls(
            call=call,
            join_as=join_as,
            invite_hash=invite_hash,
            params=params,
            muted=muted,
            video_stopped=video_stopped,
        )


@register_tl
class LeaveGroupCall(TLRequest):
    ID: int = 0x500377F9
    def __init__(self, call: Any = None, source: int = 0) -> None:
        self.call = call
        self.source = source
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.call)
        writer.write_int32(self.source)
    @classmethod
    def read(cls, reader: TLReader) -> "LeaveGroupCall":
        call = reader.read_object()
        source = reader.read_int32()
        return cls(call=call, source=source)


@register_tl
class EditGroupCallParticipant(TLRequest):
    ID: int = 0xA5273ABF
    def __init__(
        self,
        call: Any = None,
        participant: Any = None,
        volume: int | None = None,
        raise_hand: bool | None = None,
        presentation_paused: bool | None = None,
    ) -> None:
        self.call = call
        self.participant = participant
        self.volume = volume
        self.raise_hand = raise_hand
        self.presentation_paused = presentation_paused
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.volume is not None:
            flags |= (1 << 1)
        if self.raise_hand is not None:
            flags |= (1 << 2)
        if self.presentation_paused is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_object(self.call)
        writer.write_object(self.participant)
        if self.volume is not None:
            writer.write_int32(self.volume)
        if self.raise_hand is not None:
            writer.write_bool(self.raise_hand)
        if self.presentation_paused is not None:
            writer.write_bool(self.presentation_paused)
    @classmethod
    def read(cls, reader: TLReader) -> "EditGroupCallParticipant":
        flags = reader.read_uint32()
        call = reader.read_object()
        participant = reader.read_object()
        volume = reader.read_int32() if (flags & (1 << 1)) else None
        raise_hand = reader.read_bool() if (flags & (1 << 2)) else None
        presentation_paused = reader.read_bool() if (flags & (1 << 3)) else None
        return cls(
            call=call,
            participant=participant,
            volume=volume,
            raise_hand=raise_hand,
            presentation_paused=presentation_paused,
        )


@register_tl
class CreateGroupCall(TLRequest):
    ID: int = 0x48CDC6D8
    def __init__(
        self,
        peer: Any = None,
        random_id: int = 0,
        title: str | None = None,
        schedule_date: int | None = None,
        rtmp_stream: bool = False,
    ) -> None:
        self.peer = peer
        self.random_id = random_id
        self.title = title
        self.schedule_date = schedule_date
        self.rtmp_stream = rtmp_stream
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rtmp_stream:
            flags |= (1 << 2)
        if self.title is not None:
            flags |= (1 << 0)
        if self.schedule_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_int32(self.random_id)
        if self.title is not None:
            writer.write_string(self.title)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date)
    @classmethod
    def read(cls, reader: TLReader) -> "CreateGroupCall":
        flags = reader.read_uint32()
        rtmp_stream = bool(flags & (1 << 2))
        peer = reader.read_object()
        random_id = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(peer=peer, random_id=random_id, title=title, schedule_date=schedule_date, rtmp_stream=rtmp_stream)


@register_tl
class DiscardGroupCall(TLRequest):
    ID: int = 0x7A777135
    def __init__(self, call: Any = None) -> None:
        self.call = call
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.call)
    @classmethod
    def read(cls, reader: TLReader) -> "DiscardGroupCall":
        call = reader.read_object()
        return cls(call=call)
