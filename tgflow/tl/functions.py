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


@register_tl
class RequestCall(TLRequest):
    ID: int = 0x42FF96ED

    def __init__(
        self,
        user_id: Any = None,
        random_id: int = 0,
        g_a_hash: bytes = b"",
        protocol: Any = None,
        video: bool = False,
    ) -> None:
        self.user_id = user_id
        self.random_id = random_id
        self.g_a_hash = g_a_hash
        self.protocol = protocol
        self.video = video

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_object(self.user_id)
        writer.write_int32(self.random_id)
        writer.write_bytes(self.g_a_hash)
        writer.write_object(self.protocol)

    @classmethod
    def read(cls, reader: TLReader) -> "RequestCall":
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        user_id = reader.read_object()
        random_id = reader.read_int32()
        g_a_hash = reader.read_bytes()
        protocol = reader.read_object()
        return cls(user_id=user_id, random_id=random_id, g_a_hash=g_a_hash, protocol=protocol, video=video)


@register_tl
class AcceptCall(TLRequest):
    ID: int = 0x3BD2B4A0

    def __init__(self, peer: Any = None, g_b: bytes = b"", protocol: Any = None) -> None:
        self.peer = peer
        self.g_b = g_b
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)
        writer.write_bytes(self.g_b)
        writer.write_object(self.protocol)

    @classmethod
    def read(cls, reader: TLReader) -> "AcceptCall":
        peer = reader.read_object()
        g_b = reader.read_bytes()
        protocol = reader.read_object()
        return cls(peer=peer, g_b=g_b, protocol=protocol)


@register_tl
class ConfirmCall(TLRequest):
    ID: int = 0x2EFE1722

    def __init__(self, peer: Any = None, g_a: bytes = b"", key_fingerprint: int = 0, protocol: Any = None) -> None:
        self.peer = peer
        self.g_a = g_a
        self.key_fingerprint = key_fingerprint
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)
        writer.write_bytes(self.g_a)
        writer.write_int64(self.key_fingerprint)
        writer.write_object(self.protocol)

    @classmethod
    def read(cls, reader: TLReader) -> "ConfirmCall":
        peer = reader.read_object()
        g_a = reader.read_bytes()
        key_fingerprint = reader.read_int64()
        protocol = reader.read_object()
        return cls(peer=peer, g_a=g_a, key_fingerprint=key_fingerprint, protocol=protocol)


@register_tl
class ReceivedCall(TLRequest):
    ID: int = 0x17D54F61

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)

    @classmethod
    def read(cls, reader: TLReader) -> "ReceivedCall":
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class DiscardCall(TLRequest):
    ID: int = 0xB2CDC4DC

    def __init__(
        self,
        peer: Any = None,
        duration: int = 0,
        reason: Any = None,
        connection_id: int = 0,
        video: bool = False,
    ) -> None:
        self.peer = peer
        self.duration = duration
        self.reason = reason
        self.connection_id = connection_id
        self.video = video

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_int32(self.duration)
        writer.write_object(self.reason)
        writer.write_int64(self.connection_id)

    @classmethod
    def read(cls, reader: TLReader) -> "DiscardCall":
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        peer = reader.read_object()
        duration = reader.read_int32()
        reason = reader.read_object()
        connection_id = reader.read_int64()
        return cls(peer=peer, duration=duration, reason=reason, connection_id=connection_id, video=video)


@register_tl
class SetCallRating(TLRequest):
    ID: int = 0x59EAD627

    def __init__(self, peer: Any = None, rating: int = 0, comment: str = "", user_initiative: bool = False) -> None:
        self.peer = peer
        self.rating = rating
        self.comment = comment
        self.user_initiative = user_initiative

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.user_initiative:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_int32(self.rating)
        writer.write_string(self.comment)

    @classmethod
    def read(cls, reader: TLReader) -> "SetCallRating":
        flags = reader.read_uint32()
        user_initiative = bool(flags & (1 << 0))
        peer = reader.read_object()
        rating = reader.read_int32()
        comment = reader.read_string()
        return cls(peer=peer, rating=rating, comment=comment, user_initiative=user_initiative)


@register_tl
class SaveCallDebug(TLRequest):
    ID: int = 0x277ADD7E

    def __init__(self, peer: Any = None, debug: Any = None) -> None:
        self.peer = peer
        self.debug = debug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)
        writer.write_object(self.debug)

    @classmethod
    def read(cls, reader: TLReader) -> "SaveCallDebug":
        peer = reader.read_object()
        debug = reader.read_object()
        return cls(peer=peer, debug=debug)


@register_tl
class InviteToGroupCall(TLRequest):
    ID: int = 0x7B393160

    def __init__(self, call: Any = None, users: list[Any] | None = None) -> None:
        self.call = call
        self.users = users or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.call)
        writer.write_vector(self.users, lambda w, u: w.write_object(u))

    @classmethod
    def read(cls, reader: TLReader) -> "InviteToGroupCall":
        call = reader.read_object()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(call=call, users=users)


@register_tl
class ToggleGroupCallSettings(TLRequest):
    ID: int = 0x74BA41CB

    def __init__(self, call: Any = None, join_muted: bool | None = None, reset_invite_hash: bool = False) -> None:
        self.call = call
        self.join_muted = join_muted
        self.reset_invite_hash = reset_invite_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.join_muted is not None:
            flags |= (1 << 0)
        if self.reset_invite_hash:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_object(self.call)
        if self.join_muted is not None:
            writer.write_bool(self.join_muted)

    @classmethod
    def read(cls, reader: TLReader) -> "ToggleGroupCallSettings":
        flags = reader.read_uint32()
        reset_invite_hash = bool(flags & (1 << 1))
        call = reader.read_object()
        join_muted = reader.read_bool() if (flags & (1 << 0)) else None
        return cls(call=call, join_muted=join_muted, reset_invite_hash=reset_invite_hash)


@register_tl
class StartScheduledGroupCall(TLRequest):
    ID: int = 0x564D16E1

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.call)

    @classmethod
    def read(cls, reader: TLReader) -> "StartScheduledGroupCall":
        call = reader.read_object()
        return cls(call=call)


@register_tl
class ToggleGroupCallRecord(TLRequest):
    ID: int = 0xF128C708

    def __init__(
        self,
        call: Any = None,
        start: bool = False,
        video: bool = False,
        title: str | None = None,
        video_portrait: bool | None = None,
    ) -> None:
        self.call = call
        self.start = start
        self.video = video
        self.title = title
        self.video_portrait = video_portrait

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.start:
            flags |= (1 << 0)
        if self.title is not None:
            flags |= (1 << 1)
        if self.video:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_object(self.call)
        if self.title is not None:
            writer.write_string(self.title)
        if self.video and self.video_portrait is not None:
            writer.write_bool(self.video_portrait)

    @classmethod
    def read(cls, reader: TLReader) -> "ToggleGroupCallRecord":
        flags = reader.read_uint32()
        start = bool(flags & (1 << 0))
        video = bool(flags & (1 << 2))
        call = reader.read_object()
        title = reader.read_string() if (flags & (1 << 1)) else None
        video_portrait = reader.read_bool() if video and (flags & (1 << 2)) else None
        return cls(call=call, start=start, video=video, title=title, video_portrait=video_portrait)


@register_tl
class SendCode(TLRequest):
    ID: int = 0xA677244F

    def __init__(
        self,
        phone_number: str = "",
        api_id: int = 0,
        api_hash: str = "",
        settings: Any = None,
    ) -> None:
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        writer.write_uint32(flags)
        writer.write_string(self.phone_number)
        writer.write_int32(self.api_id)
        writer.write_string(self.api_hash)
        writer.write_object(self.settings)

    @classmethod
    def read(cls, reader: TLReader) -> "SendCode":
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        api_id = reader.read_int32()
        api_hash = reader.read_string()
        settings = reader.read_object()
        return cls(phone_number=phone_number, api_id=api_id, api_hash=api_hash, settings=settings)


@register_tl
class SignIn(TLRequest):
    ID: int = 0x8D52A951

    def __init__(
        self,
        phone_number: str = "",
        phone_code_hash: str = "",
        phone_code: str | None = None,
    ) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.phone_code is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        if self.phone_code is not None:
            writer.write_string(self.phone_code)

    @classmethod
    def read(cls, reader: TLReader) -> "SignIn":
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        phone_code = reader.read_string() if (flags & (1 << 0)) else None
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code)


@register_tl
class SignUp(TLRequest):
    ID: int = 0x80EEE427

    def __init__(
        self,
        phone_number: str = "",
        phone_code_hash: str = "",
        first_name: str = "",
        last_name: str = "",
    ) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.first_name = first_name
        self.last_name = last_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        writer.write_string(self.first_name)
        writer.write_string(self.last_name)

    @classmethod
    def read(cls, reader: TLReader) -> "SignUp":
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        return cls(
            phone_number=phone_number,
            phone_code_hash=phone_code_hash,
            first_name=first_name,
            last_name=last_name,
        )


@register_tl
class LogOut(TLRequest):
    ID: int = 0x3E72BA19

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> "LogOut":
        return cls()


@register_tl
class CheckPassword(TLRequest):
    ID: int = 0xD18B4D16

    def __init__(self, password: Any = None) -> None:
        self.password = password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.password)

    @classmethod
    def read(cls, reader: TLReader) -> "CheckPassword":
        password = reader.read_object()
        return cls(password=password)


@register_tl
class ResendCode(TLRequest):
    ID: int = 0x3EF1A9BF

    def __init__(self, phone_number: str = "", phone_code_hash: str = "", reason: str | None = None) -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.reason = reason

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reason is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)
        if self.reason is not None:
            writer.write_string(self.reason)

    @classmethod
    def read(cls, reader: TLReader) -> "ResendCode":
        flags = reader.read_uint32()
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        reason = reader.read_string() if (flags & (1 << 0)) else None
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash, reason=reason)


@register_tl
class CancelCode(TLRequest):
    ID: int = 0x1F04045B

    def __init__(self, phone_number: str = "", phone_code_hash: str = "") -> None:
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number)
        writer.write_string(self.phone_code_hash)

    @classmethod
    def read(cls, reader: TLReader) -> "CancelCode":
        phone_number = reader.read_string()
        phone_code_hash = reader.read_string()
        return cls(phone_number=phone_number, phone_code_hash=phone_code_hash)


@register_tl
class ExportAuthorization(TLRequest):
    ID: int = 0xE5B96423

    def __init__(self, dc_id: int = 0) -> None:
        self.dc_id = dc_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id)

    @classmethod
    def read(cls, reader: TLReader) -> "ExportAuthorization":
        return cls(dc_id=reader.read_int32())


@register_tl
class ImportAuthorization(TLRequest):
    ID: int = 0xA5757399

    def __init__(self, id: int = 0, bytes_data: bytes = b"") -> None:
        self.id = id
        self.bytes_data = bytes_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id)
        writer.write_bytes(self.bytes_data)

    @classmethod
    def read(cls, reader: TLReader) -> "ImportAuthorization":
        return cls(id=reader.read_int64(), bytes_data=reader.read_bytes())


@register_tl
class ResolveUsername(TLRequest):
    ID: int = 0xF93CCBA3

    def __init__(self, username: str = "") -> None:
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.username)

    @classmethod
    def read(cls, reader: TLReader) -> "ResolveUsername":
        return cls(username=reader.read_string())


@register_tl
class GetContacts(TLRequest):
    ID: int = 0x5DD69E12

    def __init__(self, hash: int = 0) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash)

    @classmethod
    def read(cls, reader: TLReader) -> "GetContacts":
        return cls(hash=reader.read_int64())


@register_tl
class SearchContacts(TLRequest):
    ID: int = 0x11F812D8

    def __init__(self, q: str = "", limit: int = 10) -> None:
        self.q = q
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q)
        writer.write_int32(self.limit)

    @classmethod
    def read(cls, reader: TLReader) -> "SearchContacts":
        return cls(q=reader.read_string(), limit=reader.read_int32())


@register_tl
class GetUsers(TLRequest):
    ID: int = 0x0D91A548

    def __init__(self, id: list[Any] | None = None) -> None:
        self.id = id or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id, lambda w, u: w.write_object(u))

    @classmethod
    def read(cls, reader: TLReader) -> "GetUsers":
        return cls(id=reader.read_vector(lambda r: r.read_object()))


@register_tl
class GetFullUser(TLRequest):
    ID: int = 0xB60ED36F

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.id)

    @classmethod
    def read(cls, reader: TLReader) -> "GetFullUser":
        return cls(id=reader.read_object())


@register_tl
class GetFullChannel(TLRequest):
    ID: int = 0x08736A09

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)

    @classmethod
    def read(cls, reader: TLReader) -> "GetFullChannel":
        return cls(channel=reader.read_object())


@register_tl
class JoinChannel(TLRequest):
    ID: int = 0x24B52477

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)

    @classmethod
    def read(cls, reader: TLReader) -> "JoinChannel":
        return cls(channel=reader.read_object())


@register_tl
class LeaveChannel(TLRequest):
    ID: int = 0xF836AA95

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)

    @classmethod
    def read(cls, reader: TLReader) -> "LeaveChannel":
        return cls(channel=reader.read_object())


@register_tl
class CreateChannel(TLRequest):
    ID: int = 0x3D793857

    def __init__(
        self,
        title: str = "",
        about: str = "",
        broadcast: bool = False,
        megagroup: bool = False,
    ) -> None:
        self.title = title
        self.about = about
        self.broadcast = broadcast
        self.megagroup = megagroup

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast:
            flags |= (1 << 0)
        if self.megagroup:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.title)
        writer.write_string(self.about)

    @classmethod
    def read(cls, reader: TLReader) -> "CreateChannel":
        flags = reader.read_uint32()
        broadcast = bool(flags & (1 << 0))
        megagroup = bool(flags & (1 << 1))
        title = reader.read_string()
        about = reader.read_string()
        return cls(title=title, about=about, broadcast=broadcast, megagroup=megagroup)





@register_tl
class DeleteMessages(TLRequest):
    ID: int = 0xE58E95D2

    def __init__(self, id: list[int] | None = None, revoke: bool = True) -> None:
        self.id = id or []
        self.revoke = revoke

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoke:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.id, lambda w, i: w.write_int32(i))

    @classmethod
    def read(cls, reader: TLReader) -> "DeleteMessages":
        flags = reader.read_uint32()
        revoke = bool(flags & (1 << 0))
        ids = reader.read_vector(lambda r: r.read_int32())
        return cls(id=ids, revoke=revoke)


@register_tl
class ReadHistory(TLRequest):
    ID: int = 0x0E306D3A

    def __init__(self, peer: Any = None, max_id: int = 0) -> None:
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)
        writer.write_int32(self.max_id)

    @classmethod
    def read(cls, reader: TLReader) -> "ReadHistory":
        return cls(peer=reader.read_object(), max_id=reader.read_int32())


@register_tl
class ForwardMessages(TLRequest):
    ID: int = 0xCCB03657

    def __init__(
        self,
        from_peer: Any = None,
        to_peer: Any = None,
        id: list[int] | None = None,
        random_id: list[int] | None = None,
        silent: bool = False,
        background: bool = False,
        drop_author: bool = False,
    ) -> None:
        self.from_peer = from_peer
        self.to_peer = to_peer
        self.id = id or []
        self.random_id = random_id or []
        self.silent = silent
        self.background = background
        self.drop_author = drop_author

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 5)
        if self.background:
            flags |= (1 << 6)
        if self.drop_author:
            flags |= (1 << 11)
        writer.write_uint32(flags)
        writer.write_object(self.from_peer)
        writer.write_vector(self.id, lambda w, i: w.write_int32(i))
        writer.write_vector(self.random_id, lambda w, r: w.write_int64(r))
        writer.write_object(self.to_peer)

    @classmethod
    def read(cls, reader: TLReader) -> "ForwardMessages":
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 5))
        background = bool(flags & (1 << 6))
        drop_author = bool(flags & (1 << 11))
        from_peer = reader.read_object()
        ids = reader.read_vector(lambda r: r.read_int32())
        rand_ids = reader.read_vector(lambda r: r.read_int64())
        to_peer = reader.read_object()
        return cls(
            from_peer=from_peer,
            to_peer=to_peer,
            id=ids,
            random_id=rand_ids,
            silent=silent,
            background=background,
            drop_author=drop_author,
        )


@register_tl
class SendReaction(TLRequest):
    ID: int = 0xD30D78D4

    def __init__(
        self,
        peer: Any = None,
        msg_id: int = 0,
        reaction: list[Any] | None = None,
        big: bool = False,
    ) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.reaction = reaction
        self.big = big

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reaction is not None:
            flags |= (1 << 0)
        if self.big:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_int32(self.msg_id)
        if self.reaction is not None:
            writer.write_vector(self.reaction, lambda w, r: w.write_object(r))

    @classmethod
    def read(cls, reader: TLReader) -> "SendReaction":
        flags = reader.read_uint32()
        big = bool(flags & (1 << 1))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        reaction = reader.read_vector(lambda r: r.read_object()) if (flags & (1 << 0)) else None
        return cls(peer=peer, msg_id=msg_id, reaction=reaction, big=big)


@register_tl
class SetTyping(TLRequest):
    ID: int = 0x58944461

    def __init__(self, peer: Any = None, action: Any = None) -> None:
        self.peer = peer
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_object(self.action)

    @classmethod
    def read(cls, reader: TLReader) -> "SetTyping":
        flags = reader.read_uint32()
        peer = reader.read_object()
        action = reader.read_object()
        return cls(peer=peer, action=action)


@register_tl
class UpdateProfile(TLRequest):
    ID: int = 0x78515775

    def __init__(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        about: str | None = None,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.about = about

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.first_name is not None:
            flags |= (1 << 0)
        if self.last_name is not None:
            flags |= (1 << 1)
        if self.about is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.first_name is not None:
            writer.write_string(self.first_name)
        if self.last_name is not None:
            writer.write_string(self.last_name)
        if self.about is not None:
            writer.write_string(self.about)

    @classmethod
    def read(cls, reader: TLReader) -> "UpdateProfile":
        flags = reader.read_uint32()
        first_name = reader.read_string() if (flags & (1 << 0)) else None
        last_name = reader.read_string() if (flags & (1 << 1)) else None
        about = reader.read_string() if (flags & (1 << 2)) else None
        return cls(first_name=first_name, last_name=last_name, about=about)


@register_tl
class UpdateStatus(TLRequest):
    ID: int = 0x6628F585

    def __init__(self, offline: bool = False) -> None:
        self.offline = offline

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(self.offline)

    @classmethod
    def read(cls, reader: TLReader) -> "UpdateStatus":
        return cls(offline=reader.read_bool())


@register_tl
class GetParticipants(TLRequest):
    ID: int = 0x77CED9D0

    def __init__(self, channel: Any = None, filter: Any = None, offset: int = 0, limit: int = 100, hash: int = 0) -> None:
        self.channel = channel
        self.filter = filter
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)
        writer.write_object(self.filter)
        writer.write_int32(self.offset)
        writer.write_int32(self.limit)
        writer.write_int64(self.hash)

    @classmethod
    def read(cls, reader: TLReader) -> "GetParticipants":
        channel = reader.read_object()
        filter_obj = reader.read_object()
        offset = reader.read_int32()
        limit = reader.read_int32()
        hash_val = reader.read_int64()
        return cls(channel=channel, filter=filter_obj, offset=offset, limit=limit, hash=hash_val)


@register_tl
class EditAdmin(TLRequest):
    ID: int = 0xD33C8902

    def __init__(self, channel: Any = None, user_id: Any = None, admin_rights: Any = None, rank: str = "") -> None:
        self.channel = channel
        self.user_id = user_id
        self.admin_rights = admin_rights
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)
        writer.write_object(self.user_id)
        writer.write_object(self.admin_rights)
        writer.write_string(self.rank)

    @classmethod
    def read(cls, reader: TLReader) -> "EditAdmin":
        channel = reader.read_object()
        user_id = reader.read_object()
        admin_rights = reader.read_object()
        rank = reader.read_string()
        return cls(channel=channel, user_id=user_id, admin_rights=admin_rights, rank=rank)


@register_tl
class EditBanned(TLRequest):
    ID: int = 0x96E6CEDA

    def __init__(self, channel: Any = None, participant: Any = None, banned_rights: Any = None) -> None:
        self.channel = channel
        self.participant = participant
        self.banned_rights = banned_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)
        writer.write_object(self.participant)
        writer.write_object(self.banned_rights)

    @classmethod
    def read(cls, reader: TLReader) -> "EditBanned":
        channel = reader.read_object()
        participant = reader.read_object()
        banned_rights = reader.read_object()
        return cls(channel=channel, participant=participant, banned_rights=banned_rights)


@register_tl
class GetChats(TLRequest):
    ID: int = 0x49E95D02

    def __init__(self, id: list[int] | None = None) -> None:
        self.id = id or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id, lambda w, i: w.write_int64(i))

    @classmethod
    def read(cls, reader: TLReader) -> "GetChats":
        return cls(id=reader.read_vector(lambda r: r.read_int64()))


@register_tl
class GetFullChat(TLRequest):
    ID: int = 0xAEB00B34

    def __init__(self, chat_id: int = 0) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id)

    @classmethod
    def read(cls, reader: TLReader) -> "GetFullChat":
        return cls(chat_id=reader.read_int64())


@register_tl
class GetMessages(TLRequest):
    ID: int = 0x63C66506

    def __init__(self, id: list[Any] | None = None) -> None:
        self.id = id or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id, lambda w, i: w.write_object(i))

    @classmethod
    def read(cls, reader: TLReader) -> "GetMessages":
        return cls(id=reader.read_vector(lambda r: r.read_object()))


@register_tl
class SearchMessages(TLRequest):
    ID: int = 0x29EE047C

    def __init__(
        self,
        peer: Any = None,
        q: str = "",
        filter: Any = None,
        min_date: int = 0,
        max_date: int = 0,
        offset_id: int = 0,
        add_offset: int = 0,
        limit: int = 100,
        max_id: int = 0,
        min_id: int = 0,
        hash: int = 0,
    ) -> None:
        self.peer = peer
        self.q = q
        self.filter = filter
        self.min_date = min_date
        self.max_date = max_date
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_string(self.q)
        writer.write_object(self.filter)
        writer.write_int32(self.min_date)
        writer.write_int32(self.max_date)
        writer.write_int32(self.offset_id)
        writer.write_int32(self.add_offset)
        writer.write_int32(self.limit)
        writer.write_int32(self.max_id)
        writer.write_int32(self.min_id)
        writer.write_int64(self.hash)

    @classmethod
    def read(cls, reader: TLReader) -> "SearchMessages":
        flags = reader.read_uint32()
        peer = reader.read_object()
        q = reader.read_string()
        filter_obj = reader.read_object()
        min_date = reader.read_int32()
        max_date = reader.read_int32()
        offset_id = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        hash_val = reader.read_int64()
        return cls(
            peer=peer,
            q=q,
            filter=filter_obj,
            min_date=min_date,
            max_date=max_date,
            offset_id=offset_id,
            add_offset=add_offset,
            limit=limit,
            max_id=max_id,
            min_id=min_id,
            hash=hash_val,
        )


@register_tl
class GetDialogs(TLRequest):
    ID: int = 0xA0F4CB4F

    def __init__(
        self,
        offset_date: int = 0,
        offset_id: int = 0,
        offset_peer: Any = None,
        limit: int = 100,
        hash: int = 0,
        exclude_pinned: bool = False,
        folder_id: int | None = None,
    ) -> None:
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_peer = offset_peer
        self.limit = limit
        self.hash = hash
        self.exclude_pinned = exclude_pinned
        self.folder_id = folder_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.exclude_pinned:
            flags |= (1 << 0)
        if self.folder_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id)
        writer.write_int32(self.offset_date)
        writer.write_int32(self.offset_id)
        writer.write_object(self.offset_peer)
        writer.write_int32(self.limit)
        writer.write_int64(self.hash)

    @classmethod
    def read(cls, reader: TLReader) -> "GetDialogs":
        flags = reader.read_uint32()
        exclude_pinned = bool(flags & (1 << 0))
        folder_id = reader.read_int32() if (flags & (1 << 1)) else None
        offset_date = reader.read_int32()
        offset_id = reader.read_int32()
        offset_peer = reader.read_object()
        limit = reader.read_int32()
        hash_val = reader.read_int64()
        return cls(
            offset_date=offset_date,
            offset_id=offset_id,
            offset_peer=offset_peer,
            limit=limit,
            hash=hash_val,
            exclude_pinned=exclude_pinned,
            folder_id=folder_id,
        )


@register_tl
class PinChatMessage(TLRequest):
    ID: int = 0x3252A303

    def __init__(self, peer: Any = None, id: int = 0, silent: bool = False, both_sides: bool = False) -> None:
        self.peer = peer
        self.id = id
        self.silent = silent
        self.both_sides = both_sides

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.silent:
            flags |= (1 << 0)
        if self.both_sides:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_int32(self.id)

    @classmethod
    def read(cls, reader: TLReader) -> "PinChatMessage":
        flags = reader.read_uint32()
        silent = bool(flags & (1 << 0))
        both_sides = bool(flags & (1 << 2))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, id=msg_id, silent=silent, both_sides=both_sides)


@register_tl
class UnpinAllMessages(TLRequest):
    ID: int = 0xF025BC8B

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)

    @classmethod
    def read(cls, reader: TLReader) -> "UnpinAllMessages":
        return cls(peer=reader.read_object())


@register_tl
class EditChatTitle(TLRequest):
    ID: int = 0x73783FFD

    def __init__(self, chat_id: int = 0, title: str = "") -> None:
        self.chat_id = chat_id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id)
        writer.write_string(self.title)

    @classmethod
    def read(cls, reader: TLReader) -> "EditChatTitle":
        return cls(chat_id=reader.read_int64(), title=reader.read_string())


@register_tl
class EditChatAbout(TLRequest):
    ID: int = 0xDEF60797

    def __init__(self, peer: Any = None, about: str = "") -> None:
        self.peer = peer
        self.about = about

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)
        writer.write_string(self.about)

    @classmethod
    def read(cls, reader: TLReader) -> "EditChatAbout":
        return cls(peer=reader.read_object(), about=reader.read_string())


@register_tl
class ToggleForum(TLRequest):
    ID: int = 0x58D6B470

    def __init__(self, channel: Any = None, enabled: bool = True) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)
        writer.write_bool(self.enabled)

    @classmethod
    def read(cls, reader: TLReader) -> "ToggleForum":
        return cls(channel=reader.read_object(), enabled=reader.read_bool())


@register_tl
class CreateForumTopic(TLRequest):
    ID: int = 0xF40C0224

    def __init__(self, channel: Any = None, title: str = "", icon_color: int | None = None, icon_emoji_id: int | None = None) -> None:
        self.channel = channel
        self.title = title
        self.icon_color = icon_color
        self.icon_emoji_id = icon_emoji_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.icon_color is not None:
            flags |= (1 << 0)
        if self.icon_emoji_id is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_object(self.channel)
        writer.write_string(self.title)
        if self.icon_color is not None:
            writer.write_int32(self.icon_color)
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id)

    @classmethod
    def read(cls, reader: TLReader) -> "CreateForumTopic":
        flags = reader.read_uint32()
        channel = reader.read_object()
        title = reader.read_string()
        icon_color = reader.read_int32() if (flags & (1 << 0)) else None
        icon_emoji_id = reader.read_int64() if (flags & (1 << 3)) else None
        return cls(channel=channel, title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id)


@register_tl
class EditForumTopic(TLRequest):
    ID: int = 0xF23C49E9

    def __init__(
        self,
        channel: Any = None,
        topic_id: int = 0,
        title: str | None = None,
        icon_emoji_id: int | None = None,
        closed: bool | None = None,
        hidden: bool | None = None,
    ) -> None:
        self.channel = channel
        self.topic_id = topic_id
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.closed = closed
        self.hidden = hidden

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title is not None:
            flags |= (1 << 0)
        if self.icon_emoji_id is not None:
            flags |= (1 << 1)
        if self.closed is not None:
            flags |= (1 << 2)
        if self.hidden is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_object(self.channel)
        writer.write_int32(self.topic_id)
        if self.title is not None:
            writer.write_string(self.title)
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id)
        if self.closed is not None:
            writer.write_bool(self.closed)
        if self.hidden is not None:
            writer.write_bool(self.hidden)

    @classmethod
    def read(cls, reader: TLReader) -> "EditForumTopic":
        flags = reader.read_uint32()
        channel = reader.read_object()
        topic_id = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        icon_emoji_id = reader.read_int64() if (flags & (1 << 1)) else None
        closed = reader.read_bool() if (flags & (1 << 2)) else None
        hidden = reader.read_bool() if (flags & (1 << 3)) else None
        return cls(
            channel=channel,
            topic_id=topic_id,
            title=title,
            icon_emoji_id=icon_emoji_id,
            closed=closed,
            hidden=hidden,
        )


@register_tl
class SetBotCallbackAnswer(TLRequest):
    ID: int = 0xD58F130A

    def __init__(self, query_id: int = 0, message: str | None = None, alert: bool = False, url: str | None = None, cache_time: int = 0) -> None:
        self.query_id = query_id
        self.message = message
        self.alert = alert
        self.url = url
        self.cache_time = cache_time

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.message is not None:
            flags |= (1 << 0)
        if self.alert:
            flags |= (1 << 1)
        if self.url is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id)
        if self.message is not None:
            writer.write_string(self.message)
        if self.url is not None:
            writer.write_string(self.url)
        writer.write_int32(self.cache_time)

    @classmethod
    def read(cls, reader: TLReader) -> "SetBotCallbackAnswer":
        flags = reader.read_uint32()
        alert = bool(flags & (1 << 1))
        query_id = reader.read_int64()
        message = reader.read_string() if (flags & (1 << 0)) else None
        url = reader.read_string() if (flags & (1 << 2)) else None
        cache_time = reader.read_int32()
        return cls(query_id=query_id, message=message, alert=alert, url=url, cache_time=cache_time)


@register_tl
class DeleteTopicHistory(TLRequest):
    ID: int = 0xE0B64E9A

    def __init__(self, channel: Any = None, topic_id: int = 0) -> None:
        self.channel = channel
        self.topic_id = topic_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.channel)
        writer.write_int32(self.topic_id)

    @classmethod
    def read(cls, reader: TLReader) -> "DeleteTopicHistory":
        return cls(channel=reader.read_object(), topic_id=reader.read_int32())
