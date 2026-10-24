from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class BoolFalse(TLObject):
    ID: int = 0xbc799737

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BoolFalse':
        return cls()


@register_tl
class BoolTrue(TLObject):
    ID: int = 0x997275b5

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'BoolTrue':
        return cls()


@register_tl
class TrueType(TLObject):
    ID: int = 0x3fedd339

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TrueType':
        return cls()


@register_tl
class Vector(TLObject):
    ID: int = 0x1cb5c415

    def __init__(self, t: Any = None) -> None:
        self.t = t

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.t is not None and hasattr(self.t, 'write'): self.t.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'Vector':
        t = reader.read_object()
        return cls(t=t)


@register_tl
class Error(TLObject):
    ID: int = 0xc4b9f9bb

    def __init__(self, code: Any = None, text: Any = None) -> None:
        self.code = code
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.code or 0)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'Error':
        code = reader.read_int32()
        text = reader.read_string()
        return cls(code=code, text=text)


@register_tl
class Null(TLObject):
    ID: int = 0x56730bcc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'Null':
        return cls()


@register_tl
class InputPeerEmpty(TLObject):
    ID: int = 0x7f3b18ea

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerEmpty':
        return cls()


@register_tl
class InputPeerSelf(TLObject):
    ID: int = 0x7da07ec9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerSelf':
        return cls()


@register_tl
class InputPeerChat(TLObject):
    ID: int = 0x35a95cb9

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerChat':
        chat_id = reader.read_int64()
        return cls(chat_id=chat_id)


@register_tl
class InputPeerUser(TLObject):
    ID: int = 0xdde8a54c

    def __init__(self, user_id: Any = None, access_hash: Any = None) -> None:
        self.user_id = user_id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerUser':
        user_id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(user_id=user_id, access_hash=access_hash)


@register_tl
class InputPeerChannel(TLObject):
    ID: int = 0x27bcbbfc

    def __init__(self, channel_id: Any = None, access_hash: Any = None) -> None:
        self.channel_id = channel_id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerChannel':
        channel_id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(channel_id=channel_id, access_hash=access_hash)


@register_tl
class InputPeerUserFromMessage(TLObject):
    ID: int = 0xa87b0a1c

    def __init__(self, peer: Any = None, msg_id: Any = None, user_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerUserFromMessage':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        user_id = reader.read_int64()
        return cls(peer=peer, msg_id=msg_id, user_id=user_id)


@register_tl
class InputPeerChannelFromMessage(TLObject):
    ID: int = 0xbd2a0840

    def __init__(self, peer: Any = None, msg_id: Any = None, channel_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerChannelFromMessage':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        channel_id = reader.read_int64()
        return cls(peer=peer, msg_id=msg_id, channel_id=channel_id)


@register_tl
class InputUserEmpty(TLObject):
    ID: int = 0xb98886cf

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputUserEmpty':
        return cls()


@register_tl
class InputUserSelf(TLObject):
    ID: int = 0xf7c1b13f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputUserSelf':
        return cls()


@register_tl
class InputUser(TLObject):
    ID: int = 0xf21158c6

    def __init__(self, user_id: Any = None, access_hash: Any = None) -> None:
        self.user_id = user_id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputUser':
        user_id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(user_id=user_id, access_hash=access_hash)


@register_tl
class InputUserFromMessage(TLObject):
    ID: int = 0x1da448e2

    def __init__(self, peer: Any = None, msg_id: Any = None, user_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputUserFromMessage':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        user_id = reader.read_int64()
        return cls(peer=peer, msg_id=msg_id, user_id=user_id)


@register_tl
class InputPhoneContact(TLObject):
    ID: int = 0x6a1dc4be

    def __init__(self, note: Any = None, client_id: Any = None, phone: Any = None, first_name: Any = None, last_name: Any = None) -> None:
        self.note = note
        self.client_id = client_id
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.note is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.client_id or 0)
        writer.write_string(self.phone or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        if self.note is not None:
            if self.note is not None and hasattr(self.note, 'write'): self.note.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPhoneContact':
        flags = reader.read_uint32()
        client_id = reader.read_int64()
        phone = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        note = reader.read_object() if (flags & (1 << 0)) else None
        return cls(client_id=client_id, phone=phone, first_name=first_name, last_name=last_name, note=note)


@register_tl
class InputFile(TLObject):
    ID: int = 0xf52ff27f

    def __init__(self, id: Any = None, parts: Any = None, name: Any = None, md5_checksum: Any = None) -> None:
        self.id = id
        self.parts = parts
        self.name = name
        self.md5_checksum = md5_checksum

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int32(self.parts or 0)
        writer.write_string(self.name or '')
        writer.write_string(self.md5_checksum or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputFile':
        id = reader.read_int64()
        parts = reader.read_int32()
        name = reader.read_string()
        md5_checksum = reader.read_string()
        return cls(id=id, parts=parts, name=name, md5_checksum=md5_checksum)


@register_tl
class InputFileBig(TLObject):
    ID: int = 0xfa4f0bb5

    def __init__(self, id: Any = None, parts: Any = None, name: Any = None) -> None:
        self.id = id
        self.parts = parts
        self.name = name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int32(self.parts or 0)
        writer.write_string(self.name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputFileBig':
        id = reader.read_int64()
        parts = reader.read_int32()
        name = reader.read_string()
        return cls(id=id, parts=parts, name=name)


@register_tl
class InputFileStoryDocument(TLObject):
    ID: int = 0x62dc8b48

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputFileStoryDocument':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class InputMediaEmpty(TLObject):
    ID: int = 0x9664f57f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaEmpty':
        return cls()


@register_tl
class InputMediaUploadedPhoto(TLObject):
    ID: int = 0x7d8375da

    def __init__(self, spoiler: bool = False, live_photo: bool = False, stickers: Any = None, ttl_seconds: Any = None, video: Any = None, file: Any = None) -> None:
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.stickers = stickers
        self.ttl_seconds = ttl_seconds
        self.video = video
        self.file = file

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 2)
        if self.live_photo:
            flags |= (1 << 3)
        if self.stickers is not None:
            flags |= (1 << 0)
        if self.ttl_seconds is not None:
            flags |= (1 << 1)
        if self.video is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        if self.stickers is not None:
            writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video is not None:
            if self.video is not None and hasattr(self.video, 'write'): self.video.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaUploadedPhoto':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 2))
        live_photo = bool(flags & (1 << 3))
        file = reader.read_object()
        stickers = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        ttl_seconds = reader.read_int32() if (flags & (1 << 1)) else None
        video = reader.read_object() if (flags & (1 << 3)) else None
        return cls(spoiler=spoiler, live_photo=live_photo, file=file, stickers=stickers, ttl_seconds=ttl_seconds, video=video)


@register_tl
class InputMediaPhoto(TLObject):
    ID: int = 0xe3af4434

    def __init__(self, spoiler: bool = False, live_photo: bool = False, ttl_seconds: Any = None, video: Any = None, id: Any = None) -> None:
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.ttl_seconds = ttl_seconds
        self.video = video
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 1)
        if self.live_photo:
            flags |= (1 << 2)
        if self.ttl_seconds is not None:
            flags |= (1 << 0)
        if self.video is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video is not None:
            if self.video is not None and hasattr(self.video, 'write'): self.video.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPhoto':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 1))
        live_photo = bool(flags & (1 << 2))
        id = reader.read_object()
        ttl_seconds = reader.read_int32() if (flags & (1 << 0)) else None
        video = reader.read_object() if (flags & (1 << 2)) else None
        return cls(spoiler=spoiler, live_photo=live_photo, id=id, ttl_seconds=ttl_seconds, video=video)


@register_tl
class InputMediaGeoPoint(TLObject):
    ID: int = 0xf9c44144

    def __init__(self, geo_point: Any = None) -> None:
        self.geo_point = geo_point

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaGeoPoint':
        geo_point = reader.read_object()
        return cls(geo_point=geo_point)


@register_tl
class InputMediaContact(TLObject):
    ID: int = 0xf8ab7dfb

    def __init__(self, phone_number: Any = None, first_name: Any = None, last_name: Any = None, vcard: Any = None) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_string(self.vcard or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaContact':
        phone_number = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        vcard = reader.read_string()
        return cls(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard)


@register_tl
class InputMediaUploadedDocument(TLObject):
    ID: int = 0x37c9330

    def __init__(self, nosound_video: bool = False, force_file: bool = False, spoiler: bool = False, thumb: Any = None, stickers: Any = None, video_cover: Any = None, video_timestamp: Any = None, ttl_seconds: Any = None, file: Any = None, mime_type: Any = None, attributes: Any = None) -> None:
        self.nosound_video = nosound_video
        self.force_file = force_file
        self.spoiler = spoiler
        self.thumb = thumb
        self.stickers = stickers
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp
        self.ttl_seconds = ttl_seconds
        self.file = file
        self.mime_type = mime_type
        self.attributes = attributes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.nosound_video:
            flags |= (1 << 3)
        if self.force_file:
            flags |= (1 << 4)
        if self.spoiler:
            flags |= (1 << 5)
        if self.thumb is not None:
            flags |= (1 << 2)
        if self.stickers is not None:
            flags |= (1 << 0)
        if self.video_cover is not None:
            flags |= (1 << 6)
        if self.video_timestamp is not None:
            flags |= (1 << 7)
        if self.ttl_seconds is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        if self.thumb is not None:
            if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        writer.write_string(self.mime_type or '')
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.stickers is not None:
            writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.video_cover is not None:
            if self.video_cover is not None and hasattr(self.video_cover, 'write'): self.video_cover.write(writer)
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaUploadedDocument':
        flags = reader.read_uint32()
        nosound_video = bool(flags & (1 << 3))
        force_file = bool(flags & (1 << 4))
        spoiler = bool(flags & (1 << 5))
        file = reader.read_object()
        thumb = reader.read_object() if (flags & (1 << 2)) else None
        mime_type = reader.read_string()
        attributes = reader.read_vector(lambda r: reader.read_object())
        stickers = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 0)) else None
        video_cover = reader.read_object() if (flags & (1 << 6)) else None
        video_timestamp = reader.read_int32() if (flags & (1 << 7)) else None
        ttl_seconds = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(nosound_video=nosound_video, force_file=force_file, spoiler=spoiler, file=file, thumb=thumb, mime_type=mime_type, attributes=attributes, stickers=stickers, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds)


@register_tl
class InputMediaDocument(TLObject):
    ID: int = 0xa8763ab5

    def __init__(self, spoiler: bool = False, video_cover: Any = None, video_timestamp: Any = None, ttl_seconds: Any = None, query: Any = None, id: Any = None) -> None:
        self.spoiler = spoiler
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp
        self.ttl_seconds = ttl_seconds
        self.query = query
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 2)
        if self.video_cover is not None:
            flags |= (1 << 3)
        if self.video_timestamp is not None:
            flags |= (1 << 4)
        if self.ttl_seconds is not None:
            flags |= (1 << 0)
        if self.query is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        if self.video_cover is not None:
            if self.video_cover is not None and hasattr(self.video_cover, 'write'): self.video_cover.write(writer)
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.query is not None:
            writer.write_string(self.query or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaDocument':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 2))
        id = reader.read_object()
        video_cover = reader.read_object() if (flags & (1 << 3)) else None
        video_timestamp = reader.read_int32() if (flags & (1 << 4)) else None
        ttl_seconds = reader.read_int32() if (flags & (1 << 0)) else None
        query = reader.read_string() if (flags & (1 << 1)) else None
        return cls(spoiler=spoiler, id=id, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds, query=query)


@register_tl
class InputMediaVenue(TLObject):
    ID: int = 0xc13d1c11

    def __init__(self, geo_point: Any = None, title: Any = None, address: Any = None, provider: Any = None, venue_id: Any = None, venue_type: Any = None) -> None:
        self.geo_point = geo_point
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        writer.write_string(self.title or '')
        writer.write_string(self.address or '')
        writer.write_string(self.provider or '')
        writer.write_string(self.venue_id or '')
        writer.write_string(self.venue_type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaVenue':
        geo_point = reader.read_object()
        title = reader.read_string()
        address = reader.read_string()
        provider = reader.read_string()
        venue_id = reader.read_string()
        venue_type = reader.read_string()
        return cls(geo_point=geo_point, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)


@register_tl
class InputMediaPhotoExternal(TLObject):
    ID: int = 0xe5bbfe1a

    def __init__(self, spoiler: bool = False, ttl_seconds: Any = None, url: Any = None) -> None:
        self.spoiler = spoiler
        self.ttl_seconds = ttl_seconds
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 1)
        if self.ttl_seconds is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.url or '')
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPhotoExternal':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 1))
        url = reader.read_string()
        ttl_seconds = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(spoiler=spoiler, url=url, ttl_seconds=ttl_seconds)


@register_tl
class InputMediaDocumentExternal(TLObject):
    ID: int = 0x779600f9

    def __init__(self, spoiler: bool = False, ttl_seconds: Any = None, video_cover: Any = None, video_timestamp: Any = None, url: Any = None) -> None:
        self.spoiler = spoiler
        self.ttl_seconds = ttl_seconds
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 1)
        if self.ttl_seconds is not None:
            flags |= (1 << 0)
        if self.video_cover is not None:
            flags |= (1 << 2)
        if self.video_timestamp is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_string(self.url or '')
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video_cover is not None:
            if self.video_cover is not None and hasattr(self.video_cover, 'write'): self.video_cover.write(writer)
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaDocumentExternal':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 1))
        url = reader.read_string()
        ttl_seconds = reader.read_int32() if (flags & (1 << 0)) else None
        video_cover = reader.read_object() if (flags & (1 << 2)) else None
        video_timestamp = reader.read_int32() if (flags & (1 << 3)) else None
        return cls(spoiler=spoiler, url=url, ttl_seconds=ttl_seconds, video_cover=video_cover, video_timestamp=video_timestamp)


@register_tl
class InputMediaGame(TLObject):
    ID: int = 0xd33f43f3

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaGame':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class InputMediaInvoice(TLObject):
    ID: int = 0x405fef0d

    def __init__(self, photo: Any = None, provider: Any = None, start_param: Any = None, extended_media: Any = None, title: Any = None, description: Any = None, invoice: Any = None, payload: Any = None, provider_data: Any = None) -> None:
        self.photo = photo
        self.provider = provider
        self.start_param = start_param
        self.extended_media = extended_media
        self.title = title
        self.description = description
        self.invoice = invoice
        self.payload = payload
        self.provider_data = provider_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.photo is not None:
            flags |= (1 << 0)
        if self.provider is not None:
            flags |= (1 << 3)
        if self.start_param is not None:
            flags |= (1 << 1)
        if self.extended_media is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        writer.write_bytes(self.payload or b'')
        if self.provider is not None:
            writer.write_string(self.provider or '')
        if self.provider_data is not None and hasattr(self.provider_data, 'write'): self.provider_data.write(writer)
        if self.start_param is not None:
            writer.write_string(self.start_param or '')
        if self.extended_media is not None:
            if self.extended_media is not None and hasattr(self.extended_media, 'write'): self.extended_media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaInvoice':
        flags = reader.read_uint32()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 0)) else None
        invoice = reader.read_object()
        payload = reader.read_bytes()
        provider = reader.read_string() if (flags & (1 << 3)) else None
        provider_data = reader.read_object()
        start_param = reader.read_string() if (flags & (1 << 1)) else None
        extended_media = reader.read_object() if (flags & (1 << 2)) else None
        return cls(title=title, description=description, photo=photo, invoice=invoice, payload=payload, provider=provider, provider_data=provider_data, start_param=start_param, extended_media=extended_media)


@register_tl
class InputMediaGeoLive(TLObject):
    ID: int = 0x971fa843

    def __init__(self, stopped: bool = False, heading: Any = None, period: Any = None, proximity_notification_radius: Any = None, geo_point: Any = None) -> None:
        self.stopped = stopped
        self.heading = heading
        self.period = period
        self.proximity_notification_radius = proximity_notification_radius
        self.geo_point = geo_point

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.stopped:
            flags |= (1 << 0)
        if self.heading is not None:
            flags |= (1 << 2)
        if self.period is not None:
            flags |= (1 << 1)
        if self.proximity_notification_radius is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        if self.heading is not None:
            writer.write_int32(self.heading or 0)
        if self.period is not None:
            writer.write_int32(self.period or 0)
        if self.proximity_notification_radius is not None:
            writer.write_int32(self.proximity_notification_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaGeoLive':
        flags = reader.read_uint32()
        stopped = bool(flags & (1 << 0))
        geo_point = reader.read_object()
        heading = reader.read_int32() if (flags & (1 << 2)) else None
        period = reader.read_int32() if (flags & (1 << 1)) else None
        proximity_notification_radius = reader.read_int32() if (flags & (1 << 3)) else None
        return cls(stopped=stopped, geo_point=geo_point, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius)


@register_tl
class InputMediaPoll(TLObject):
    ID: int = 0x883a4108

    def __init__(self, correct_answers: Any = None, attached_media: Any = None, solution: Any = None, solution_entities: Any = None, solution_media: Any = None, poll: Any = None) -> None:
        self.correct_answers = correct_answers
        self.attached_media = attached_media
        self.solution = solution
        self.solution_entities = solution_entities
        self.solution_media = solution_media
        self.poll = poll

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.correct_answers is not None:
            flags |= (1 << 0)
        if self.attached_media is not None:
            flags |= (1 << 3)
        if self.solution is not None:
            flags |= (1 << 1)
        if self.solution_entities is not None:
            flags |= (1 << 1)
        if self.solution_media is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.poll is not None and hasattr(self.poll, 'write'): self.poll.write(writer)
        if self.correct_answers is not None:
            writer.write_vector(self.correct_answers or [], lambda w, x: w.write_int32(x))
        if self.attached_media is not None:
            if self.attached_media is not None and hasattr(self.attached_media, 'write'): self.attached_media.write(writer)
        if self.solution is not None:
            writer.write_string(self.solution or '')
        if self.solution_entities is not None:
            writer.write_vector(self.solution_entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.solution_media is not None:
            if self.solution_media is not None and hasattr(self.solution_media, 'write'): self.solution_media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPoll':
        flags = reader.read_uint32()
        poll = reader.read_object()
        correct_answers = reader.read_vector(lambda r: r.read_int32()) if (flags & (1 << 0)) else None
        attached_media = reader.read_object() if (flags & (1 << 3)) else None
        solution = reader.read_string() if (flags & (1 << 1)) else None
        solution_entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        solution_media = reader.read_object() if (flags & (1 << 2)) else None
        return cls(poll=poll, correct_answers=correct_answers, attached_media=attached_media, solution=solution, solution_entities=solution_entities, solution_media=solution_media)


@register_tl
class InputMediaDice(TLObject):
    ID: int = 0xe66fbf7b

    def __init__(self, emoticon: Any = None) -> None:
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaDice':
        emoticon = reader.read_string()
        return cls(emoticon=emoticon)


@register_tl
class InputMediaStory(TLObject):
    ID: int = 0x89fdd778

    def __init__(self, peer: Any = None, id: Any = None) -> None:
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaStory':
        peer = reader.read_object()
        id = reader.read_int32()
        return cls(peer=peer, id=id)


@register_tl
class InputMediaWebPage(TLObject):
    ID: int = 0xc21b8849

    def __init__(self, force_large_media: bool = False, force_small_media: bool = False, optional: bool = False, url: Any = None) -> None:
        self.force_large_media = force_large_media
        self.force_small_media = force_small_media
        self.optional = optional
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.force_large_media:
            flags |= (1 << 0)
        if self.force_small_media:
            flags |= (1 << 1)
        if self.optional:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaWebPage':
        flags = reader.read_uint32()
        force_large_media = bool(flags & (1 << 0))
        force_small_media = bool(flags & (1 << 1))
        optional = bool(flags & (1 << 2))
        url = reader.read_string()
        return cls(force_large_media=force_large_media, force_small_media=force_small_media, optional=optional, url=url)


@register_tl
class InputMediaPaidMedia(TLObject):
    ID: int = 0xc4103386

    def __init__(self, payload: Any = None, stars_amount: Any = None, extended_media: Any = None) -> None:
        self.payload = payload
        self.stars_amount = stars_amount
        self.extended_media = extended_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.payload is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars_amount or 0)
        writer.write_vector(self.extended_media or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.payload is not None:
            writer.write_string(self.payload or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPaidMedia':
        flags = reader.read_uint32()
        stars_amount = reader.read_int64()
        extended_media = reader.read_vector(lambda r: reader.read_object())
        payload = reader.read_string() if (flags & (1 << 0)) else None
        return cls(stars_amount=stars_amount, extended_media=extended_media, payload=payload)


@register_tl
class InputMediaTodo(TLObject):
    ID: int = 0x9fc55fde

    def __init__(self, todo: Any = None) -> None:
        self.todo = todo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.todo is not None and hasattr(self.todo, 'write'): self.todo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaTodo':
        todo = reader.read_object()
        return cls(todo=todo)


@register_tl
class InputMediaStakeDice(TLObject):
    ID: int = 0xf3a9244a

    def __init__(self, game_hash: Any = None, ton_amount: Any = None, client_seed: Any = None) -> None:
        self.game_hash = game_hash
        self.ton_amount = ton_amount
        self.client_seed = client_seed

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.game_hash or '')
        writer.write_int64(self.ton_amount or 0)
        writer.write_bytes(self.client_seed or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaStakeDice':
        game_hash = reader.read_string()
        ton_amount = reader.read_int64()
        client_seed = reader.read_bytes()
        return cls(game_hash=game_hash, ton_amount=ton_amount, client_seed=client_seed)


@register_tl
class InputChatPhotoEmpty(TLObject):
    ID: int = 0x1ca48f57

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatPhotoEmpty':
        return cls()


@register_tl
class InputChatUploadedPhoto(TLObject):
    ID: int = 0xbdcdaec0

    def __init__(self, file: Any = None, video: Any = None, video_start_ts: Any = None, video_emoji_markup: Any = None) -> None:
        self.file = file
        self.video = video
        self.video_start_ts = video_start_ts
        self.video_emoji_markup = video_emoji_markup

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.file is not None:
            flags |= (1 << 0)
        if self.video is not None:
            flags |= (1 << 1)
        if self.video_start_ts is not None:
            flags |= (1 << 2)
        if self.video_emoji_markup is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.file is not None:
            if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        if self.video is not None:
            if self.video is not None and hasattr(self.video, 'write'): self.video.write(writer)
        if self.video_start_ts is not None:
            writer.write_double(self.video_start_ts or 0.0)
        if self.video_emoji_markup is not None:
            if self.video_emoji_markup is not None and hasattr(self.video_emoji_markup, 'write'): self.video_emoji_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatUploadedPhoto':
        flags = reader.read_uint32()
        file = reader.read_object() if (flags & (1 << 0)) else None
        video = reader.read_object() if (flags & (1 << 1)) else None
        video_start_ts = reader.read_double() if (flags & (1 << 2)) else None
        video_emoji_markup = reader.read_object() if (flags & (1 << 3)) else None
        return cls(file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)


@register_tl
class InputChatPhoto(TLObject):
    ID: int = 0x8953ad37

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatPhoto':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class InputGeoPointEmpty(TLObject):
    ID: int = 0xe4c123d6

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGeoPointEmpty':
        return cls()


@register_tl
class InputGeoPoint(TLObject):
    ID: int = 0x48222faf

    def __init__(self, accuracy_radius: Any = None, lat: Any = None, long: Any = None) -> None:
        self.accuracy_radius = accuracy_radius
        self.lat = lat
        self.long = long

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accuracy_radius is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_double(self.lat or 0.0)
        writer.write_double(self.long or 0.0)
        if self.accuracy_radius is not None:
            writer.write_int32(self.accuracy_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGeoPoint':
        flags = reader.read_uint32()
        lat = reader.read_double()
        long = reader.read_double()
        accuracy_radius = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(lat=lat, long=long, accuracy_radius=accuracy_radius)


@register_tl
class InputPhotoEmpty(TLObject):
    ID: int = 0x1cd7bf0d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPhotoEmpty':
        return cls()


@register_tl
class InputPhoto(TLObject):
    ID: int = 0x3bb3b94a

    def __init__(self, id: Any = None, access_hash: Any = None, file_reference: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_bytes(self.file_reference or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPhoto':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        return cls(id=id, access_hash=access_hash, file_reference=file_reference)


@register_tl
class InputFileLocation(TLObject):
    ID: int = 0xdfdaabe1

    def __init__(self, volume_id: Any = None, local_id: Any = None, secret: Any = None, file_reference: Any = None) -> None:
        self.volume_id = volume_id
        self.local_id = local_id
        self.secret = secret
        self.file_reference = file_reference

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.volume_id or 0)
        writer.write_int32(self.local_id or 0)
        writer.write_int64(self.secret or 0)
        writer.write_bytes(self.file_reference or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputFileLocation':
        volume_id = reader.read_int64()
        local_id = reader.read_int32()
        secret = reader.read_int64()
        file_reference = reader.read_bytes()
        return cls(volume_id=volume_id, local_id=local_id, secret=secret, file_reference=file_reference)


@register_tl
class InputEncryptedFileLocation(TLObject):
    ID: int = 0xf5235d55

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputEncryptedFileLocation':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputDocumentFileLocation(TLObject):
    ID: int = 0xbad07584

    def __init__(self, id: Any = None, access_hash: Any = None, file_reference: Any = None, thumb_size: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.thumb_size = thumb_size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_bytes(self.file_reference or b'')
        writer.write_string(self.thumb_size or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputDocumentFileLocation':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        thumb_size = reader.read_string()
        return cls(id=id, access_hash=access_hash, file_reference=file_reference, thumb_size=thumb_size)


@register_tl
class InputSecureFileLocation(TLObject):
    ID: int = 0xcbc7ee28

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputSecureFileLocation':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class InputTakeoutFileLocation(TLObject):
    ID: int = 0x29be5899

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputTakeoutFileLocation':
        return cls()


@register_tl
class InputPhotoFileLocation(TLObject):
    ID: int = 0x40181ffe

    def __init__(self, id: Any = None, access_hash: Any = None, file_reference: Any = None, thumb_size: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.thumb_size = thumb_size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_bytes(self.file_reference or b'')
        writer.write_string(self.thumb_size or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPhotoFileLocation':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        thumb_size = reader.read_string()
        return cls(id=id, access_hash=access_hash, file_reference=file_reference, thumb_size=thumb_size)


@register_tl
class InputPhotoLegacyFileLocation(TLObject):
    ID: int = 0xd83466f3

    def __init__(self, id: Any = None, access_hash: Any = None, file_reference: Any = None, volume_id: Any = None, local_id: Any = None, secret: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.volume_id = volume_id
        self.local_id = local_id
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_bytes(self.file_reference or b'')
        writer.write_int64(self.volume_id or 0)
        writer.write_int32(self.local_id or 0)
        writer.write_int64(self.secret or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPhotoLegacyFileLocation':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        volume_id = reader.read_int64()
        local_id = reader.read_int32()
        secret = reader.read_int64()
        return cls(id=id, access_hash=access_hash, file_reference=file_reference, volume_id=volume_id, local_id=local_id, secret=secret)


@register_tl
class InputPeerPhotoFileLocation(TLObject):
    ID: int = 0x37257e99

    def __init__(self, big: bool = False, peer: Any = None, photo_id: Any = None) -> None:
        self.big = big
        self.peer = peer
        self.photo_id = photo_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.big:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int64(self.photo_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerPhotoFileLocation':
        flags = reader.read_uint32()
        big = bool(flags & (1 << 0))
        peer = reader.read_object()
        photo_id = reader.read_int64()
        return cls(big=big, peer=peer, photo_id=photo_id)


@register_tl
class InputStickerSetThumb(TLObject):
    ID: int = 0x9d84f3db

    def __init__(self, stickerset: Any = None, thumb_version: Any = None) -> None:
        self.stickerset = stickerset
        self.thumb_version = thumb_version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        writer.write_int32(self.thumb_version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetThumb':
        stickerset = reader.read_object()
        thumb_version = reader.read_int32()
        return cls(stickerset=stickerset, thumb_version=thumb_version)


@register_tl
class InputGroupCallStream(TLObject):
    ID: int = 0x598a92a

    def __init__(self, video_channel: Any = None, video_quality: Any = None, call: Any = None, time_ms: Any = None, scale: Any = None) -> None:
        self.video_channel = video_channel
        self.video_quality = video_quality
        self.call = call
        self.time_ms = time_ms
        self.scale = scale

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video_channel is not None:
            flags |= (1 << 0)
        if self.video_quality is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        writer.write_int64(self.time_ms or 0)
        writer.write_int32(self.scale or 0)
        if self.video_channel is not None:
            writer.write_int32(self.video_channel or 0)
        if self.video_quality is not None:
            writer.write_int32(self.video_quality or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGroupCallStream':
        flags = reader.read_uint32()
        call = reader.read_object()
        time_ms = reader.read_int64()
        scale = reader.read_int32()
        video_channel = reader.read_int32() if (flags & (1 << 0)) else None
        video_quality = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(call=call, time_ms=time_ms, scale=scale, video_channel=video_channel, video_quality=video_quality)


@register_tl
class PeerUser(TLObject):
    ID: int = 0x59511722

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerUser':
        user_id = reader.read_int64()
        return cls(user_id=user_id)


@register_tl
class PeerChat(TLObject):
    ID: int = 0x36c6019a

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerChat':
        chat_id = reader.read_int64()
        return cls(chat_id=chat_id)


@register_tl
class PeerChannel(TLObject):
    ID: int = 0xa2a5371e

    def __init__(self, channel_id: Any = None) -> None:
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerChannel':
        channel_id = reader.read_int64()
        return cls(channel_id=channel_id)


@register_tl
class StorageFileUnknown(TLObject):
    ID: int = 0xaa963b05

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFileUnknown':
        return cls()


@register_tl
class StorageFilePartial(TLObject):
    ID: int = 0x40bc6f52

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFilePartial':
        return cls()


@register_tl
class StorageFileJpeg(TLObject):
    ID: int = 0x7efe0e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFileJpeg':
        return cls()


@register_tl
class StorageFileGif(TLObject):
    ID: int = 0xcae1aadf

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFileGif':
        return cls()


@register_tl
class StorageFilePng(TLObject):
    ID: int = 0xa4f63c0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFilePng':
        return cls()


@register_tl
class StorageFilePdf(TLObject):
    ID: int = 0xae1e508d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFilePdf':
        return cls()


@register_tl
class StorageFileMp3(TLObject):
    ID: int = 0x528a0677

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFileMp3':
        return cls()


@register_tl
class StorageFileMov(TLObject):
    ID: int = 0x4b09ebbc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFileMov':
        return cls()


@register_tl
class StorageFileMp4(TLObject):
    ID: int = 0xb3cea0e4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFileMp4':
        return cls()


@register_tl
class StorageFileWebp(TLObject):
    ID: int = 0x1081464c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'StorageFileWebp':
        return cls()


@register_tl
class UserEmpty(TLObject):
    ID: int = 0xd3bc4b7a

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserEmpty':
        id = reader.read_int64()
        return cls(id=id)


@register_tl
class User(TLObject):
    ID: int = 0x31774388

    def __init__(self, self_: bool = False, contact: bool = False, mutual_contact: bool = False, deleted: bool = False, bot: bool = False, bot_chat_history: bool = False, bot_nochats: bool = False, verified: bool = False, restricted: bool = False, min: bool = False, bot_inline_geo: bool = False, support: bool = False, scam: bool = False, apply_min_photo: bool = False, fake: bool = False, bot_attach_menu: bool = False, premium: bool = False, attach_menu_enabled: bool = False, bot_can_edit: bool = False, close_friend: bool = False, stories_hidden: bool = False, stories_unavailable: bool = False, contact_require_premium: bool = False, bot_business: bool = False, bot_has_main_app: bool = False, bot_forum_view: bool = False, bot_forum_can_manage_topics: bool = False, bot_can_manage_bots: bool = False, bot_guestchat: bool = False, access_hash: Any = None, first_name: Any = None, last_name: Any = None, username: Any = None, phone: Any = None, photo: Any = None, status: Any = None, bot_info_version: Any = None, restriction_reason: Any = None, bot_inline_placeholder: Any = None, lang_code: Any = None, emoji_status: Any = None, usernames: Any = None, stories_max_id: Any = None, color: Any = None, profile_color: Any = None, bot_active_users: Any = None, bot_verification_icon: Any = None, send_paid_messages_stars: Any = None, id: Any = None) -> None:
        self.self_ = self_
        self.contact = contact
        self.mutual_contact = mutual_contact
        self.deleted = deleted
        self.bot = bot
        self.bot_chat_history = bot_chat_history
        self.bot_nochats = bot_nochats
        self.verified = verified
        self.restricted = restricted
        self.min = min
        self.bot_inline_geo = bot_inline_geo
        self.support = support
        self.scam = scam
        self.apply_min_photo = apply_min_photo
        self.fake = fake
        self.bot_attach_menu = bot_attach_menu
        self.premium = premium
        self.attach_menu_enabled = attach_menu_enabled
        self.bot_can_edit = bot_can_edit
        self.close_friend = close_friend
        self.stories_hidden = stories_hidden
        self.stories_unavailable = stories_unavailable
        self.contact_require_premium = contact_require_premium
        self.bot_business = bot_business
        self.bot_has_main_app = bot_has_main_app
        self.bot_forum_view = bot_forum_view
        self.bot_forum_can_manage_topics = bot_forum_can_manage_topics
        self.bot_can_manage_bots = bot_can_manage_bots
        self.bot_guestchat = bot_guestchat
        self.access_hash = access_hash
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone = phone
        self.photo = photo
        self.status = status
        self.bot_info_version = bot_info_version
        self.restriction_reason = restriction_reason
        self.bot_inline_placeholder = bot_inline_placeholder
        self.lang_code = lang_code
        self.emoji_status = emoji_status
        self.usernames = usernames
        self.stories_max_id = stories_max_id
        self.color = color
        self.profile_color = profile_color
        self.bot_active_users = bot_active_users
        self.bot_verification_icon = bot_verification_icon
        self.send_paid_messages_stars = send_paid_messages_stars
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        flags2 = 0
        if self.self_:
            flags |= (1 << 10)
        if self.contact:
            flags |= (1 << 11)
        if self.mutual_contact:
            flags |= (1 << 12)
        if self.deleted:
            flags |= (1 << 13)
        if self.bot:
            flags |= (1 << 14)
        if self.bot_chat_history:
            flags |= (1 << 15)
        if self.bot_nochats:
            flags |= (1 << 16)
        if self.verified:
            flags |= (1 << 17)
        if self.restricted:
            flags |= (1 << 18)
        if self.min:
            flags |= (1 << 20)
        if self.bot_inline_geo:
            flags |= (1 << 21)
        if self.support:
            flags |= (1 << 23)
        if self.scam:
            flags |= (1 << 24)
        if self.apply_min_photo:
            flags |= (1 << 25)
        if self.fake:
            flags |= (1 << 26)
        if self.bot_attach_menu:
            flags |= (1 << 27)
        if self.premium:
            flags |= (1 << 28)
        if self.attach_menu_enabled:
            flags |= (1 << 29)
        if self.bot_can_edit:
            flags2 |= (1 << 1)
        if self.close_friend:
            flags2 |= (1 << 2)
        if self.stories_hidden:
            flags2 |= (1 << 3)
        if self.stories_unavailable:
            flags2 |= (1 << 4)
        if self.contact_require_premium:
            flags2 |= (1 << 10)
        if self.bot_business:
            flags2 |= (1 << 11)
        if self.bot_has_main_app:
            flags2 |= (1 << 13)
        if self.bot_forum_view:
            flags2 |= (1 << 16)
        if self.bot_forum_can_manage_topics:
            flags2 |= (1 << 17)
        if self.bot_can_manage_bots:
            flags2 |= (1 << 18)
        if self.bot_guestchat:
            flags2 |= (1 << 19)
        if self.access_hash is not None:
            flags |= (1 << 0)
        if self.first_name is not None:
            flags |= (1 << 1)
        if self.last_name is not None:
            flags |= (1 << 2)
        if self.username is not None:
            flags |= (1 << 3)
        if self.phone is not None:
            flags |= (1 << 4)
        if self.photo is not None:
            flags |= (1 << 5)
        if self.status is not None:
            flags |= (1 << 6)
        if self.bot_info_version is not None:
            flags |= (1 << 14)
        if self.restriction_reason is not None:
            flags |= (1 << 18)
        if self.bot_inline_placeholder is not None:
            flags |= (1 << 19)
        if self.lang_code is not None:
            flags |= (1 << 22)
        if self.emoji_status is not None:
            flags |= (1 << 30)
        if self.usernames is not None:
            flags2 |= (1 << 0)
        if self.stories_max_id is not None:
            flags2 |= (1 << 5)
        if self.color is not None:
            flags2 |= (1 << 8)
        if self.profile_color is not None:
            flags2 |= (1 << 9)
        if self.bot_active_users is not None:
            flags2 |= (1 << 12)
        if self.bot_verification_icon is not None:
            flags2 |= (1 << 14)
        if self.send_paid_messages_stars is not None:
            flags2 |= (1 << 15)
        writer.write_uint32(flags)
        writer.write_uint32(flags2)
        writer.write_int64(self.id or 0)
        if self.access_hash is not None:
            writer.write_int64(self.access_hash or 0)
        if self.first_name is not None:
            writer.write_string(self.first_name or '')
        if self.last_name is not None:
            writer.write_string(self.last_name or '')
        if self.username is not None:
            writer.write_string(self.username or '')
        if self.phone is not None:
            writer.write_string(self.phone or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.status is not None:
            if self.status is not None and hasattr(self.status, 'write'): self.status.write(writer)
        if self.bot_info_version is not None:
            writer.write_int32(self.bot_info_version or 0)
        if self.restriction_reason is not None:
            writer.write_vector(self.restriction_reason or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.bot_inline_placeholder is not None:
            writer.write_string(self.bot_inline_placeholder or '')
        if self.lang_code is not None:
            writer.write_string(self.lang_code or '')
        if self.emoji_status is not None:
            if self.emoji_status is not None and hasattr(self.emoji_status, 'write'): self.emoji_status.write(writer)
        if self.usernames is not None:
            writer.write_vector(self.usernames or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.stories_max_id is not None:
            if self.stories_max_id is not None and hasattr(self.stories_max_id, 'write'): self.stories_max_id.write(writer)
        if self.color is not None:
            if self.color is not None and hasattr(self.color, 'write'): self.color.write(writer)
        if self.profile_color is not None:
            if self.profile_color is not None and hasattr(self.profile_color, 'write'): self.profile_color.write(writer)
        if self.bot_active_users is not None:
            writer.write_int32(self.bot_active_users or 0)
        if self.bot_verification_icon is not None:
            writer.write_int64(self.bot_verification_icon or 0)
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'User':
        flags = reader.read_uint32()
        flags2 = reader.read_uint32()
        self_ = bool(flags & (1 << 10))
        contact = bool(flags & (1 << 11))
        mutual_contact = bool(flags & (1 << 12))
        deleted = bool(flags & (1 << 13))
        bot = bool(flags & (1 << 14))
        bot_chat_history = bool(flags & (1 << 15))
        bot_nochats = bool(flags & (1 << 16))
        verified = bool(flags & (1 << 17))
        restricted = bool(flags & (1 << 18))
        min = bool(flags & (1 << 20))
        bot_inline_geo = bool(flags & (1 << 21))
        support = bool(flags & (1 << 23))
        scam = bool(flags & (1 << 24))
        apply_min_photo = bool(flags & (1 << 25))
        fake = bool(flags & (1 << 26))
        bot_attach_menu = bool(flags & (1 << 27))
        premium = bool(flags & (1 << 28))
        attach_menu_enabled = bool(flags & (1 << 29))
        bot_can_edit = bool(flags2 & (1 << 1))
        close_friend = bool(flags2 & (1 << 2))
        stories_hidden = bool(flags2 & (1 << 3))
        stories_unavailable = bool(flags2 & (1 << 4))
        contact_require_premium = bool(flags2 & (1 << 10))
        bot_business = bool(flags2 & (1 << 11))
        bot_has_main_app = bool(flags2 & (1 << 13))
        bot_forum_view = bool(flags2 & (1 << 16))
        bot_forum_can_manage_topics = bool(flags2 & (1 << 17))
        bot_can_manage_bots = bool(flags2 & (1 << 18))
        bot_guestchat = bool(flags2 & (1 << 19))
        id = reader.read_int64()
        access_hash = reader.read_int64() if (flags & (1 << 0)) else None
        first_name = reader.read_string() if (flags & (1 << 1)) else None
        last_name = reader.read_string() if (flags & (1 << 2)) else None
        username = reader.read_string() if (flags & (1 << 3)) else None
        phone = reader.read_string() if (flags & (1 << 4)) else None
        photo = reader.read_object() if (flags & (1 << 5)) else None
        status = reader.read_object() if (flags & (1 << 6)) else None
        bot_info_version = reader.read_int32() if (flags & (1 << 14)) else None
        restriction_reason = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 18)) else None
        bot_inline_placeholder = reader.read_string() if (flags & (1 << 19)) else None
        lang_code = reader.read_string() if (flags & (1 << 22)) else None
        emoji_status = reader.read_object() if (flags & (1 << 30)) else None
        usernames = reader.read_vector(lambda r: reader.read_object()) if (flags2 & (1 << 0)) else None
        stories_max_id = reader.read_object() if (flags2 & (1 << 5)) else None
        color = reader.read_object() if (flags2 & (1 << 8)) else None
        profile_color = reader.read_object() if (flags2 & (1 << 9)) else None
        bot_active_users = reader.read_int32() if (flags2 & (1 << 12)) else None
        bot_verification_icon = reader.read_int64() if (flags2 & (1 << 14)) else None
        send_paid_messages_stars = reader.read_int64() if (flags2 & (1 << 15)) else None
        return cls(self_=self_, contact=contact, mutual_contact=mutual_contact, deleted=deleted, bot=bot, bot_chat_history=bot_chat_history, bot_nochats=bot_nochats, verified=verified, restricted=restricted, min=min, bot_inline_geo=bot_inline_geo, support=support, scam=scam, apply_min_photo=apply_min_photo, fake=fake, bot_attach_menu=bot_attach_menu, premium=premium, attach_menu_enabled=attach_menu_enabled, bot_can_edit=bot_can_edit, close_friend=close_friend, stories_hidden=stories_hidden, stories_unavailable=stories_unavailable, contact_require_premium=contact_require_premium, bot_business=bot_business, bot_has_main_app=bot_has_main_app, bot_forum_view=bot_forum_view, bot_forum_can_manage_topics=bot_forum_can_manage_topics, bot_can_manage_bots=bot_can_manage_bots, bot_guestchat=bot_guestchat, id=id, access_hash=access_hash, first_name=first_name, last_name=last_name, username=username, phone=phone, photo=photo, status=status, bot_info_version=bot_info_version, restriction_reason=restriction_reason, bot_inline_placeholder=bot_inline_placeholder, lang_code=lang_code, emoji_status=emoji_status, usernames=usernames, stories_max_id=stories_max_id, color=color, profile_color=profile_color, bot_active_users=bot_active_users, bot_verification_icon=bot_verification_icon, send_paid_messages_stars=send_paid_messages_stars)


@register_tl
class UserProfilePhotoEmpty(TLObject):
    ID: int = 0x4f11bae1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserProfilePhotoEmpty':
        return cls()


@register_tl
class UserProfilePhoto(TLObject):
    ID: int = 0x82d1f706

    def __init__(self, has_video: bool = False, personal: bool = False, stripped_thumb: Any = None, photo_id: Any = None, dc_id: Any = None) -> None:
        self.has_video = has_video
        self.personal = personal
        self.stripped_thumb = stripped_thumb
        self.photo_id = photo_id
        self.dc_id = dc_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_video:
            flags |= (1 << 0)
        if self.personal:
            flags |= (1 << 2)
        if self.stripped_thumb is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.photo_id or 0)
        if self.stripped_thumb is not None:
            writer.write_bytes(self.stripped_thumb or b'')
        writer.write_int32(self.dc_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserProfilePhoto':
        flags = reader.read_uint32()
        has_video = bool(flags & (1 << 0))
        personal = bool(flags & (1 << 2))
        photo_id = reader.read_int64()
        stripped_thumb = reader.read_bytes() if (flags & (1 << 1)) else None
        dc_id = reader.read_int32()
        return cls(has_video=has_video, personal=personal, photo_id=photo_id, stripped_thumb=stripped_thumb, dc_id=dc_id)


@register_tl
class UserStatusEmpty(TLObject):
    ID: int = 0x9d05049

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserStatusEmpty':
        return cls()


@register_tl
class UserStatusOnline(TLObject):
    ID: int = 0xedb93949

    def __init__(self, expires: Any = None) -> None:
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.expires or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserStatusOnline':
        expires = reader.read_int32()
        return cls(expires=expires)


@register_tl
class UserStatusOffline(TLObject):
    ID: int = 0x8c703f

    def __init__(self, was_online: Any = None) -> None:
        self.was_online = was_online

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.was_online or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserStatusOffline':
        was_online = reader.read_int32()
        return cls(was_online=was_online)


@register_tl
class UserStatusRecently(TLObject):
    ID: int = 0x7b197dc8

    def __init__(self, by_me: bool = False) -> None:
        self.by_me = by_me

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.by_me:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserStatusRecently':
        flags = reader.read_uint32()
        by_me = bool(flags & (1 << 0))
        return cls(by_me=by_me)


@register_tl
class UserStatusLastWeek(TLObject):
    ID: int = 0x541a1d1a

    def __init__(self, by_me: bool = False) -> None:
        self.by_me = by_me

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.by_me:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserStatusLastWeek':
        flags = reader.read_uint32()
        by_me = bool(flags & (1 << 0))
        return cls(by_me=by_me)


@register_tl
class UserStatusLastMonth(TLObject):
    ID: int = 0x65899777

    def __init__(self, by_me: bool = False) -> None:
        self.by_me = by_me

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.by_me:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserStatusLastMonth':
        flags = reader.read_uint32()
        by_me = bool(flags & (1 << 0))
        return cls(by_me=by_me)


@register_tl
class ChatEmpty(TLObject):
    ID: int = 0x29562865

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatEmpty':
        id = reader.read_int64()
        return cls(id=id)


@register_tl
class Chat(TLObject):
    ID: int = 0x41cbf256

    def __init__(self, creator: bool = False, left: bool = False, deactivated: bool = False, call_active: bool = False, call_not_empty: bool = False, noforwards: bool = False, migrated_to: Any = None, admin_rights: Any = None, default_banned_rights: Any = None, id: Any = None, title: Any = None, photo: Any = None, participants_count: Any = None, date: Any = None, version: Any = None) -> None:
        self.creator = creator
        self.left = left
        self.deactivated = deactivated
        self.call_active = call_active
        self.call_not_empty = call_not_empty
        self.noforwards = noforwards
        self.migrated_to = migrated_to
        self.admin_rights = admin_rights
        self.default_banned_rights = default_banned_rights
        self.id = id
        self.title = title
        self.photo = photo
        self.participants_count = participants_count
        self.date = date
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.creator:
            flags |= (1 << 0)
        if self.left:
            flags |= (1 << 2)
        if self.deactivated:
            flags |= (1 << 5)
        if self.call_active:
            flags |= (1 << 23)
        if self.call_not_empty:
            flags |= (1 << 24)
        if self.noforwards:
            flags |= (1 << 25)
        if self.migrated_to is not None:
            flags |= (1 << 6)
        if self.admin_rights is not None:
            flags |= (1 << 14)
        if self.default_banned_rights is not None:
            flags |= (1 << 18)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(self.title or '')
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        writer.write_int32(self.participants_count or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.version or 0)
        if self.migrated_to is not None:
            if self.migrated_to is not None and hasattr(self.migrated_to, 'write'): self.migrated_to.write(writer)
        if self.admin_rights is not None:
            if self.admin_rights is not None and hasattr(self.admin_rights, 'write'): self.admin_rights.write(writer)
        if self.default_banned_rights is not None:
            if self.default_banned_rights is not None and hasattr(self.default_banned_rights, 'write'): self.default_banned_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'Chat':
        flags = reader.read_uint32()
        creator = bool(flags & (1 << 0))
        left = bool(flags & (1 << 2))
        deactivated = bool(flags & (1 << 5))
        call_active = bool(flags & (1 << 23))
        call_not_empty = bool(flags & (1 << 24))
        noforwards = bool(flags & (1 << 25))
        id = reader.read_int64()
        title = reader.read_string()
        photo = reader.read_object()
        participants_count = reader.read_int32()
        date = reader.read_int32()
        version = reader.read_int32()
        migrated_to = reader.read_object() if (flags & (1 << 6)) else None
        admin_rights = reader.read_object() if (flags & (1 << 14)) else None
        default_banned_rights = reader.read_object() if (flags & (1 << 18)) else None
        return cls(creator=creator, left=left, deactivated=deactivated, call_active=call_active, call_not_empty=call_not_empty, noforwards=noforwards, id=id, title=title, photo=photo, participants_count=participants_count, date=date, version=version, migrated_to=migrated_to, admin_rights=admin_rights, default_banned_rights=default_banned_rights)


@register_tl
class ChatForbidden(TLObject):
    ID: int = 0x6592a1a7

    def __init__(self, id: Any = None, title: Any = None) -> None:
        self.id = id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatForbidden':
        id = reader.read_int64()
        title = reader.read_string()
        return cls(id=id, title=title)


@register_tl
class Channel(TLObject):
    ID: int = 0x1c32b11c

    def __init__(self, creator: bool = False, left: bool = False, broadcast: bool = False, verified: bool = False, megagroup: bool = False, restricted: bool = False, signatures: bool = False, min: bool = False, scam: bool = False, has_link: bool = False, has_geo: bool = False, slowmode_enabled: bool = False, call_active: bool = False, call_not_empty: bool = False, fake: bool = False, gigagroup: bool = False, noforwards: bool = False, join_to_send: bool = False, join_request: bool = False, forum: bool = False, stories_hidden: bool = False, stories_hidden_min: bool = False, stories_unavailable: bool = False, signature_profiles: bool = False, autotranslation: bool = False, broadcast_messages_allowed: bool = False, monoforum: bool = False, forum_tabs: bool = False, access_hash: Any = None, username: Any = None, restriction_reason: Any = None, admin_rights: Any = None, banned_rights: Any = None, default_banned_rights: Any = None, participants_count: Any = None, usernames: Any = None, stories_max_id: Any = None, color: Any = None, profile_color: Any = None, emoji_status: Any = None, level: Any = None, subscription_until_date: Any = None, bot_verification_icon: Any = None, send_paid_messages_stars: Any = None, linked_monoforum_id: Any = None, id: Any = None, title: Any = None, photo: Any = None, date: Any = None) -> None:
        self.creator = creator
        self.left = left
        self.broadcast = broadcast
        self.verified = verified
        self.megagroup = megagroup
        self.restricted = restricted
        self.signatures = signatures
        self.min = min
        self.scam = scam
        self.has_link = has_link
        self.has_geo = has_geo
        self.slowmode_enabled = slowmode_enabled
        self.call_active = call_active
        self.call_not_empty = call_not_empty
        self.fake = fake
        self.gigagroup = gigagroup
        self.noforwards = noforwards
        self.join_to_send = join_to_send
        self.join_request = join_request
        self.forum = forum
        self.stories_hidden = stories_hidden
        self.stories_hidden_min = stories_hidden_min
        self.stories_unavailable = stories_unavailable
        self.signature_profiles = signature_profiles
        self.autotranslation = autotranslation
        self.broadcast_messages_allowed = broadcast_messages_allowed
        self.monoforum = monoforum
        self.forum_tabs = forum_tabs
        self.access_hash = access_hash
        self.username = username
        self.restriction_reason = restriction_reason
        self.admin_rights = admin_rights
        self.banned_rights = banned_rights
        self.default_banned_rights = default_banned_rights
        self.participants_count = participants_count
        self.usernames = usernames
        self.stories_max_id = stories_max_id
        self.color = color
        self.profile_color = profile_color
        self.emoji_status = emoji_status
        self.level = level
        self.subscription_until_date = subscription_until_date
        self.bot_verification_icon = bot_verification_icon
        self.send_paid_messages_stars = send_paid_messages_stars
        self.linked_monoforum_id = linked_monoforum_id
        self.id = id
        self.title = title
        self.photo = photo
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        flags2 = 0
        if self.creator:
            flags |= (1 << 0)
        if self.left:
            flags |= (1 << 2)
        if self.broadcast:
            flags |= (1 << 5)
        if self.verified:
            flags |= (1 << 7)
        if self.megagroup:
            flags |= (1 << 8)
        if self.restricted:
            flags |= (1 << 9)
        if self.signatures:
            flags |= (1 << 11)
        if self.min:
            flags |= (1 << 12)
        if self.scam:
            flags |= (1 << 19)
        if self.has_link:
            flags |= (1 << 20)
        if self.has_geo:
            flags |= (1 << 21)
        if self.slowmode_enabled:
            flags |= (1 << 22)
        if self.call_active:
            flags |= (1 << 23)
        if self.call_not_empty:
            flags |= (1 << 24)
        if self.fake:
            flags |= (1 << 25)
        if self.gigagroup:
            flags |= (1 << 26)
        if self.noforwards:
            flags |= (1 << 27)
        if self.join_to_send:
            flags |= (1 << 28)
        if self.join_request:
            flags |= (1 << 29)
        if self.forum:
            flags |= (1 << 30)
        if self.stories_hidden:
            flags2 |= (1 << 1)
        if self.stories_hidden_min:
            flags2 |= (1 << 2)
        if self.stories_unavailable:
            flags2 |= (1 << 3)
        if self.signature_profiles:
            flags2 |= (1 << 12)
        if self.autotranslation:
            flags2 |= (1 << 15)
        if self.broadcast_messages_allowed:
            flags2 |= (1 << 16)
        if self.monoforum:
            flags2 |= (1 << 17)
        if self.forum_tabs:
            flags2 |= (1 << 19)
        if self.access_hash is not None:
            flags |= (1 << 13)
        if self.username is not None:
            flags |= (1 << 6)
        if self.restriction_reason is not None:
            flags |= (1 << 9)
        if self.admin_rights is not None:
            flags |= (1 << 14)
        if self.banned_rights is not None:
            flags |= (1 << 15)
        if self.default_banned_rights is not None:
            flags |= (1 << 18)
        if self.participants_count is not None:
            flags |= (1 << 17)
        if self.usernames is not None:
            flags2 |= (1 << 0)
        if self.stories_max_id is not None:
            flags2 |= (1 << 4)
        if self.color is not None:
            flags2 |= (1 << 7)
        if self.profile_color is not None:
            flags2 |= (1 << 8)
        if self.emoji_status is not None:
            flags2 |= (1 << 9)
        if self.level is not None:
            flags2 |= (1 << 10)
        if self.subscription_until_date is not None:
            flags2 |= (1 << 11)
        if self.bot_verification_icon is not None:
            flags2 |= (1 << 13)
        if self.send_paid_messages_stars is not None:
            flags2 |= (1 << 14)
        if self.linked_monoforum_id is not None:
            flags2 |= (1 << 18)
        writer.write_uint32(flags)
        writer.write_uint32(flags2)
        writer.write_int64(self.id or 0)
        if self.access_hash is not None:
            writer.write_int64(self.access_hash or 0)
        writer.write_string(self.title or '')
        if self.username is not None:
            writer.write_string(self.username or '')
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        writer.write_int32(self.date or 0)
        if self.restriction_reason is not None:
            writer.write_vector(self.restriction_reason or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.admin_rights is not None:
            if self.admin_rights is not None and hasattr(self.admin_rights, 'write'): self.admin_rights.write(writer)
        if self.banned_rights is not None:
            if self.banned_rights is not None and hasattr(self.banned_rights, 'write'): self.banned_rights.write(writer)
        if self.default_banned_rights is not None:
            if self.default_banned_rights is not None and hasattr(self.default_banned_rights, 'write'): self.default_banned_rights.write(writer)
        if self.participants_count is not None:
            writer.write_int32(self.participants_count or 0)
        if self.usernames is not None:
            writer.write_vector(self.usernames or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.stories_max_id is not None:
            if self.stories_max_id is not None and hasattr(self.stories_max_id, 'write'): self.stories_max_id.write(writer)
        if self.color is not None:
            if self.color is not None and hasattr(self.color, 'write'): self.color.write(writer)
        if self.profile_color is not None:
            if self.profile_color is not None and hasattr(self.profile_color, 'write'): self.profile_color.write(writer)
        if self.emoji_status is not None:
            if self.emoji_status is not None and hasattr(self.emoji_status, 'write'): self.emoji_status.write(writer)
        if self.level is not None:
            writer.write_int32(self.level or 0)
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)
        if self.bot_verification_icon is not None:
            writer.write_int64(self.bot_verification_icon or 0)
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.linked_monoforum_id is not None:
            writer.write_int64(self.linked_monoforum_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Channel':
        flags = reader.read_uint32()
        flags2 = reader.read_uint32()
        creator = bool(flags & (1 << 0))
        left = bool(flags & (1 << 2))
        broadcast = bool(flags & (1 << 5))
        verified = bool(flags & (1 << 7))
        megagroup = bool(flags & (1 << 8))
        restricted = bool(flags & (1 << 9))
        signatures = bool(flags & (1 << 11))
        min = bool(flags & (1 << 12))
        scam = bool(flags & (1 << 19))
        has_link = bool(flags & (1 << 20))
        has_geo = bool(flags & (1 << 21))
        slowmode_enabled = bool(flags & (1 << 22))
        call_active = bool(flags & (1 << 23))
        call_not_empty = bool(flags & (1 << 24))
        fake = bool(flags & (1 << 25))
        gigagroup = bool(flags & (1 << 26))
        noforwards = bool(flags & (1 << 27))
        join_to_send = bool(flags & (1 << 28))
        join_request = bool(flags & (1 << 29))
        forum = bool(flags & (1 << 30))
        stories_hidden = bool(flags2 & (1 << 1))
        stories_hidden_min = bool(flags2 & (1 << 2))
        stories_unavailable = bool(flags2 & (1 << 3))
        signature_profiles = bool(flags2 & (1 << 12))
        autotranslation = bool(flags2 & (1 << 15))
        broadcast_messages_allowed = bool(flags2 & (1 << 16))
        monoforum = bool(flags2 & (1 << 17))
        forum_tabs = bool(flags2 & (1 << 19))
        id = reader.read_int64()
        access_hash = reader.read_int64() if (flags & (1 << 13)) else None
        title = reader.read_string()
        username = reader.read_string() if (flags & (1 << 6)) else None
        photo = reader.read_object()
        date = reader.read_int32()
        restriction_reason = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 9)) else None
        admin_rights = reader.read_object() if (flags & (1 << 14)) else None
        banned_rights = reader.read_object() if (flags & (1 << 15)) else None
        default_banned_rights = reader.read_object() if (flags & (1 << 18)) else None
        participants_count = reader.read_int32() if (flags & (1 << 17)) else None
        usernames = reader.read_vector(lambda r: reader.read_object()) if (flags2 & (1 << 0)) else None
        stories_max_id = reader.read_object() if (flags2 & (1 << 4)) else None
        color = reader.read_object() if (flags2 & (1 << 7)) else None
        profile_color = reader.read_object() if (flags2 & (1 << 8)) else None
        emoji_status = reader.read_object() if (flags2 & (1 << 9)) else None
        level = reader.read_int32() if (flags2 & (1 << 10)) else None
        subscription_until_date = reader.read_int32() if (flags2 & (1 << 11)) else None
        bot_verification_icon = reader.read_int64() if (flags2 & (1 << 13)) else None
        send_paid_messages_stars = reader.read_int64() if (flags2 & (1 << 14)) else None
        linked_monoforum_id = reader.read_int64() if (flags2 & (1 << 18)) else None
        return cls(creator=creator, left=left, broadcast=broadcast, verified=verified, megagroup=megagroup, restricted=restricted, signatures=signatures, min=min, scam=scam, has_link=has_link, has_geo=has_geo, slowmode_enabled=slowmode_enabled, call_active=call_active, call_not_empty=call_not_empty, fake=fake, gigagroup=gigagroup, noforwards=noforwards, join_to_send=join_to_send, join_request=join_request, forum=forum, stories_hidden=stories_hidden, stories_hidden_min=stories_hidden_min, stories_unavailable=stories_unavailable, signature_profiles=signature_profiles, autotranslation=autotranslation, broadcast_messages_allowed=broadcast_messages_allowed, monoforum=monoforum, forum_tabs=forum_tabs, id=id, access_hash=access_hash, title=title, username=username, photo=photo, date=date, restriction_reason=restriction_reason, admin_rights=admin_rights, banned_rights=banned_rights, default_banned_rights=default_banned_rights, participants_count=participants_count, usernames=usernames, stories_max_id=stories_max_id, color=color, profile_color=profile_color, emoji_status=emoji_status, level=level, subscription_until_date=subscription_until_date, bot_verification_icon=bot_verification_icon, send_paid_messages_stars=send_paid_messages_stars, linked_monoforum_id=linked_monoforum_id)


@register_tl
class ChannelForbidden(TLObject):
    ID: int = 0x17d493d5

    def __init__(self, broadcast: bool = False, megagroup: bool = False, monoforum: bool = False, until_date: Any = None, id: Any = None, access_hash: Any = None, title: Any = None) -> None:
        self.broadcast = broadcast
        self.megagroup = megagroup
        self.monoforum = monoforum
        self.until_date = until_date
        self.id = id
        self.access_hash = access_hash
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast:
            flags |= (1 << 5)
        if self.megagroup:
            flags |= (1 << 8)
        if self.monoforum:
            flags |= (1 << 10)
        if self.until_date is not None:
            flags |= (1 << 16)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_string(self.title or '')
        if self.until_date is not None:
            writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelForbidden':
        flags = reader.read_uint32()
        broadcast = bool(flags & (1 << 5))
        megagroup = bool(flags & (1 << 8))
        monoforum = bool(flags & (1 << 10))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        title = reader.read_string()
        until_date = reader.read_int32() if (flags & (1 << 16)) else None
        return cls(broadcast=broadcast, megagroup=megagroup, monoforum=monoforum, id=id, access_hash=access_hash, title=title, until_date=until_date)


@register_tl
class ChatFull(TLObject):
    ID: int = 0x2633421b

    def __init__(self, can_set_username: bool = False, has_scheduled: bool = False, translations_disabled: bool = False, chat_photo: Any = None, exported_invite: Any = None, bot_info: Any = None, pinned_msg_id: Any = None, folder_id: Any = None, call: Any = None, ttl_period: Any = None, groupcall_default_join_as: Any = None, theme_emoticon: Any = None, requests_pending: Any = None, recent_requesters: Any = None, available_reactions: Any = None, reactions_limit: Any = None, id: Any = None, about: Any = None, participants: Any = None, notify_settings: Any = None) -> None:
        self.can_set_username = can_set_username
        self.has_scheduled = has_scheduled
        self.translations_disabled = translations_disabled
        self.chat_photo = chat_photo
        self.exported_invite = exported_invite
        self.bot_info = bot_info
        self.pinned_msg_id = pinned_msg_id
        self.folder_id = folder_id
        self.call = call
        self.ttl_period = ttl_period
        self.groupcall_default_join_as = groupcall_default_join_as
        self.theme_emoticon = theme_emoticon
        self.requests_pending = requests_pending
        self.recent_requesters = recent_requesters
        self.available_reactions = available_reactions
        self.reactions_limit = reactions_limit
        self.id = id
        self.about = about
        self.participants = participants
        self.notify_settings = notify_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_set_username:
            flags |= (1 << 7)
        if self.has_scheduled:
            flags |= (1 << 8)
        if self.translations_disabled:
            flags |= (1 << 19)
        if self.chat_photo is not None:
            flags |= (1 << 2)
        if self.exported_invite is not None:
            flags |= (1 << 13)
        if self.bot_info is not None:
            flags |= (1 << 3)
        if self.pinned_msg_id is not None:
            flags |= (1 << 6)
        if self.folder_id is not None:
            flags |= (1 << 11)
        if self.call is not None:
            flags |= (1 << 12)
        if self.ttl_period is not None:
            flags |= (1 << 14)
        if self.groupcall_default_join_as is not None:
            flags |= (1 << 15)
        if self.theme_emoticon is not None:
            flags |= (1 << 16)
        if self.requests_pending is not None:
            flags |= (1 << 17)
        if self.recent_requesters is not None:
            flags |= (1 << 17)
        if self.available_reactions is not None:
            flags |= (1 << 18)
        if self.reactions_limit is not None:
            flags |= (1 << 20)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(self.about or '')
        if self.participants is not None and hasattr(self.participants, 'write'): self.participants.write(writer)
        if self.chat_photo is not None:
            if self.chat_photo is not None and hasattr(self.chat_photo, 'write'): self.chat_photo.write(writer)
        if self.notify_settings is not None and hasattr(self.notify_settings, 'write'): self.notify_settings.write(writer)
        if self.exported_invite is not None:
            if self.exported_invite is not None and hasattr(self.exported_invite, 'write'): self.exported_invite.write(writer)
        if self.bot_info is not None:
            writer.write_vector(self.bot_info or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.call is not None:
            if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.groupcall_default_join_as is not None:
            if self.groupcall_default_join_as is not None and hasattr(self.groupcall_default_join_as, 'write'): self.groupcall_default_join_as.write(writer)
        if self.theme_emoticon is not None:
            writer.write_string(self.theme_emoticon or '')
        if self.requests_pending is not None:
            writer.write_int32(self.requests_pending or 0)
        if self.recent_requesters is not None:
            writer.write_vector(self.recent_requesters or [], lambda w, x: w.write_int64(x))
        if self.available_reactions is not None:
            if self.available_reactions is not None and hasattr(self.available_reactions, 'write'): self.available_reactions.write(writer)
        if self.reactions_limit is not None:
            writer.write_int32(self.reactions_limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatFull':
        flags = reader.read_uint32()
        can_set_username = bool(flags & (1 << 7))
        has_scheduled = bool(flags & (1 << 8))
        translations_disabled = bool(flags & (1 << 19))
        id = reader.read_int64()
        about = reader.read_string()
        participants = reader.read_object()
        chat_photo = reader.read_object() if (flags & (1 << 2)) else None
        notify_settings = reader.read_object()
        exported_invite = reader.read_object() if (flags & (1 << 13)) else None
        bot_info = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 3)) else None
        pinned_msg_id = reader.read_int32() if (flags & (1 << 6)) else None
        folder_id = reader.read_int32() if (flags & (1 << 11)) else None
        call = reader.read_object() if (flags & (1 << 12)) else None
        ttl_period = reader.read_int32() if (flags & (1 << 14)) else None
        groupcall_default_join_as = reader.read_object() if (flags & (1 << 15)) else None
        theme_emoticon = reader.read_string() if (flags & (1 << 16)) else None
        requests_pending = reader.read_int32() if (flags & (1 << 17)) else None
        recent_requesters = reader.read_vector(lambda r: r.read_int64()) if (flags & (1 << 17)) else None
        available_reactions = reader.read_object() if (flags & (1 << 18)) else None
        reactions_limit = reader.read_int32() if (flags & (1 << 20)) else None
        return cls(can_set_username=can_set_username, has_scheduled=has_scheduled, translations_disabled=translations_disabled, id=id, about=about, participants=participants, chat_photo=chat_photo, notify_settings=notify_settings, exported_invite=exported_invite, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, call=call, ttl_period=ttl_period, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, available_reactions=available_reactions, reactions_limit=reactions_limit)


@register_tl
class ChannelFull(TLObject):
    ID: int = 0xe4e0b29d

    def __init__(self, can_view_participants: bool = False, can_set_username: bool = False, can_set_stickers: bool = False, hidden_prehistory: bool = False, can_set_location: bool = False, has_scheduled: bool = False, can_view_stats: bool = False, blocked: bool = False, can_delete_channel: bool = False, antispam: bool = False, participants_hidden: bool = False, translations_disabled: bool = False, stories_pinned_available: bool = False, view_forum_as_messages: bool = False, restricted_sponsored: bool = False, can_view_revenue: bool = False, paid_media_allowed: bool = False, can_view_stars_revenue: bool = False, paid_reactions_available: bool = False, stargifts_available: bool = False, paid_messages_available: bool = False, participants_count: Any = None, admins_count: Any = None, kicked_count: Any = None, banned_count: Any = None, online_count: Any = None, exported_invite: Any = None, migrated_from_chat_id: Any = None, migrated_from_max_id: Any = None, pinned_msg_id: Any = None, stickerset: Any = None, available_min_id: Any = None, folder_id: Any = None, linked_chat_id: Any = None, location: Any = None, slowmode_seconds: Any = None, slowmode_next_send_date: Any = None, stats_dc: Any = None, call: Any = None, ttl_period: Any = None, pending_suggestions: Any = None, groupcall_default_join_as: Any = None, theme_emoticon: Any = None, requests_pending: Any = None, recent_requesters: Any = None, default_send_as: Any = None, available_reactions: Any = None, reactions_limit: Any = None, stories: Any = None, wallpaper: Any = None, boosts_applied: Any = None, boosts_unrestrict: Any = None, emojiset: Any = None, bot_verification: Any = None, stargifts_count: Any = None, send_paid_messages_stars: Any = None, main_tab: Any = None, id: Any = None, about: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, chat_photo: Any = None, notify_settings: Any = None, bot_info: Any = None, pts: Any = None) -> None:
        self.can_view_participants = can_view_participants
        self.can_set_username = can_set_username
        self.can_set_stickers = can_set_stickers
        self.hidden_prehistory = hidden_prehistory
        self.can_set_location = can_set_location
        self.has_scheduled = has_scheduled
        self.can_view_stats = can_view_stats
        self.blocked = blocked
        self.can_delete_channel = can_delete_channel
        self.antispam = antispam
        self.participants_hidden = participants_hidden
        self.translations_disabled = translations_disabled
        self.stories_pinned_available = stories_pinned_available
        self.view_forum_as_messages = view_forum_as_messages
        self.restricted_sponsored = restricted_sponsored
        self.can_view_revenue = can_view_revenue
        self.paid_media_allowed = paid_media_allowed
        self.can_view_stars_revenue = can_view_stars_revenue
        self.paid_reactions_available = paid_reactions_available
        self.stargifts_available = stargifts_available
        self.paid_messages_available = paid_messages_available
        self.participants_count = participants_count
        self.admins_count = admins_count
        self.kicked_count = kicked_count
        self.banned_count = banned_count
        self.online_count = online_count
        self.exported_invite = exported_invite
        self.migrated_from_chat_id = migrated_from_chat_id
        self.migrated_from_max_id = migrated_from_max_id
        self.pinned_msg_id = pinned_msg_id
        self.stickerset = stickerset
        self.available_min_id = available_min_id
        self.folder_id = folder_id
        self.linked_chat_id = linked_chat_id
        self.location = location
        self.slowmode_seconds = slowmode_seconds
        self.slowmode_next_send_date = slowmode_next_send_date
        self.stats_dc = stats_dc
        self.call = call
        self.ttl_period = ttl_period
        self.pending_suggestions = pending_suggestions
        self.groupcall_default_join_as = groupcall_default_join_as
        self.theme_emoticon = theme_emoticon
        self.requests_pending = requests_pending
        self.recent_requesters = recent_requesters
        self.default_send_as = default_send_as
        self.available_reactions = available_reactions
        self.reactions_limit = reactions_limit
        self.stories = stories
        self.wallpaper = wallpaper
        self.boosts_applied = boosts_applied
        self.boosts_unrestrict = boosts_unrestrict
        self.emojiset = emojiset
        self.bot_verification = bot_verification
        self.stargifts_count = stargifts_count
        self.send_paid_messages_stars = send_paid_messages_stars
        self.main_tab = main_tab
        self.id = id
        self.about = about
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
        self.bot_info = bot_info
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        flags2 = 0
        if self.can_view_participants:
            flags |= (1 << 3)
        if self.can_set_username:
            flags |= (1 << 6)
        if self.can_set_stickers:
            flags |= (1 << 7)
        if self.hidden_prehistory:
            flags |= (1 << 10)
        if self.can_set_location:
            flags |= (1 << 16)
        if self.has_scheduled:
            flags |= (1 << 19)
        if self.can_view_stats:
            flags |= (1 << 20)
        if self.blocked:
            flags |= (1 << 22)
        if self.can_delete_channel:
            flags2 |= (1 << 0)
        if self.antispam:
            flags2 |= (1 << 1)
        if self.participants_hidden:
            flags2 |= (1 << 2)
        if self.translations_disabled:
            flags2 |= (1 << 3)
        if self.stories_pinned_available:
            flags2 |= (1 << 5)
        if self.view_forum_as_messages:
            flags2 |= (1 << 6)
        if self.restricted_sponsored:
            flags2 |= (1 << 11)
        if self.can_view_revenue:
            flags2 |= (1 << 12)
        if self.paid_media_allowed:
            flags2 |= (1 << 14)
        if self.can_view_stars_revenue:
            flags2 |= (1 << 15)
        if self.paid_reactions_available:
            flags2 |= (1 << 16)
        if self.stargifts_available:
            flags2 |= (1 << 19)
        if self.paid_messages_available:
            flags2 |= (1 << 20)
        if self.participants_count is not None:
            flags |= (1 << 0)
        if self.admins_count is not None:
            flags |= (1 << 1)
        if self.kicked_count is not None:
            flags |= (1 << 2)
        if self.banned_count is not None:
            flags |= (1 << 2)
        if self.online_count is not None:
            flags |= (1 << 13)
        if self.exported_invite is not None:
            flags |= (1 << 23)
        if self.migrated_from_chat_id is not None:
            flags |= (1 << 4)
        if self.migrated_from_max_id is not None:
            flags |= (1 << 4)
        if self.pinned_msg_id is not None:
            flags |= (1 << 5)
        if self.stickerset is not None:
            flags |= (1 << 8)
        if self.available_min_id is not None:
            flags |= (1 << 9)
        if self.folder_id is not None:
            flags |= (1 << 11)
        if self.linked_chat_id is not None:
            flags |= (1 << 14)
        if self.location is not None:
            flags |= (1 << 15)
        if self.slowmode_seconds is not None:
            flags |= (1 << 17)
        if self.slowmode_next_send_date is not None:
            flags |= (1 << 18)
        if self.stats_dc is not None:
            flags |= (1 << 12)
        if self.call is not None:
            flags |= (1 << 21)
        if self.ttl_period is not None:
            flags |= (1 << 24)
        if self.pending_suggestions is not None:
            flags |= (1 << 25)
        if self.groupcall_default_join_as is not None:
            flags |= (1 << 26)
        if self.theme_emoticon is not None:
            flags |= (1 << 27)
        if self.requests_pending is not None:
            flags |= (1 << 28)
        if self.recent_requesters is not None:
            flags |= (1 << 28)
        if self.default_send_as is not None:
            flags |= (1 << 29)
        if self.available_reactions is not None:
            flags |= (1 << 30)
        if self.reactions_limit is not None:
            flags2 |= (1 << 13)
        if self.stories is not None:
            flags2 |= (1 << 4)
        if self.wallpaper is not None:
            flags2 |= (1 << 7)
        if self.boosts_applied is not None:
            flags2 |= (1 << 8)
        if self.boosts_unrestrict is not None:
            flags2 |= (1 << 9)
        if self.emojiset is not None:
            flags2 |= (1 << 10)
        if self.bot_verification is not None:
            flags2 |= (1 << 17)
        if self.stargifts_count is not None:
            flags2 |= (1 << 18)
        if self.send_paid_messages_stars is not None:
            flags2 |= (1 << 21)
        if self.main_tab is not None:
            flags2 |= (1 << 22)
        writer.write_uint32(flags)
        writer.write_uint32(flags2)
        writer.write_int64(self.id or 0)
        writer.write_string(self.about or '')
        if self.participants_count is not None:
            writer.write_int32(self.participants_count or 0)
        if self.admins_count is not None:
            writer.write_int32(self.admins_count or 0)
        if self.kicked_count is not None:
            writer.write_int32(self.kicked_count or 0)
        if self.banned_count is not None:
            writer.write_int32(self.banned_count or 0)
        if self.online_count is not None:
            writer.write_int32(self.online_count or 0)
        writer.write_int32(self.read_inbox_max_id or 0)
        writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        if self.chat_photo is not None and hasattr(self.chat_photo, 'write'): self.chat_photo.write(writer)
        if self.notify_settings is not None and hasattr(self.notify_settings, 'write'): self.notify_settings.write(writer)
        if self.exported_invite is not None:
            if self.exported_invite is not None and hasattr(self.exported_invite, 'write'): self.exported_invite.write(writer)
        writer.write_vector(self.bot_info or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.migrated_from_chat_id is not None:
            writer.write_int64(self.migrated_from_chat_id or 0)
        if self.migrated_from_max_id is not None:
            writer.write_int32(self.migrated_from_max_id or 0)
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        if self.stickerset is not None:
            if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        if self.available_min_id is not None:
            writer.write_int32(self.available_min_id or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.linked_chat_id is not None:
            writer.write_int64(self.linked_chat_id or 0)
        if self.location is not None:
            if self.location is not None and hasattr(self.location, 'write'): self.location.write(writer)
        if self.slowmode_seconds is not None:
            writer.write_int32(self.slowmode_seconds or 0)
        if self.slowmode_next_send_date is not None:
            writer.write_int32(self.slowmode_next_send_date or 0)
        if self.stats_dc is not None:
            writer.write_int32(self.stats_dc or 0)
        writer.write_int32(self.pts or 0)
        if self.call is not None:
            if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.pending_suggestions is not None:
            writer.write_vector(self.pending_suggestions or [], lambda w, x: w.write_string(x))
        if self.groupcall_default_join_as is not None:
            if self.groupcall_default_join_as is not None and hasattr(self.groupcall_default_join_as, 'write'): self.groupcall_default_join_as.write(writer)
        if self.theme_emoticon is not None:
            writer.write_string(self.theme_emoticon or '')
        if self.requests_pending is not None:
            writer.write_int32(self.requests_pending or 0)
        if self.recent_requesters is not None:
            writer.write_vector(self.recent_requesters or [], lambda w, x: w.write_int64(x))
        if self.default_send_as is not None:
            if self.default_send_as is not None and hasattr(self.default_send_as, 'write'): self.default_send_as.write(writer)
        if self.available_reactions is not None:
            if self.available_reactions is not None and hasattr(self.available_reactions, 'write'): self.available_reactions.write(writer)
        if self.reactions_limit is not None:
            writer.write_int32(self.reactions_limit or 0)
        if self.stories is not None:
            if self.stories is not None and hasattr(self.stories, 'write'): self.stories.write(writer)
        if self.wallpaper is not None:
            if self.wallpaper is not None and hasattr(self.wallpaper, 'write'): self.wallpaper.write(writer)
        if self.boosts_applied is not None:
            writer.write_int32(self.boosts_applied or 0)
        if self.boosts_unrestrict is not None:
            writer.write_int32(self.boosts_unrestrict or 0)
        if self.emojiset is not None:
            if self.emojiset is not None and hasattr(self.emojiset, 'write'): self.emojiset.write(writer)
        if self.bot_verification is not None:
            if self.bot_verification is not None and hasattr(self.bot_verification, 'write'): self.bot_verification.write(writer)
        if self.stargifts_count is not None:
            writer.write_int32(self.stargifts_count or 0)
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.main_tab is not None:
            if self.main_tab is not None and hasattr(self.main_tab, 'write'): self.main_tab.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelFull':
        flags = reader.read_uint32()
        flags2 = reader.read_uint32()
        can_view_participants = bool(flags & (1 << 3))
        can_set_username = bool(flags & (1 << 6))
        can_set_stickers = bool(flags & (1 << 7))
        hidden_prehistory = bool(flags & (1 << 10))
        can_set_location = bool(flags & (1 << 16))
        has_scheduled = bool(flags & (1 << 19))
        can_view_stats = bool(flags & (1 << 20))
        blocked = bool(flags & (1 << 22))
        can_delete_channel = bool(flags2 & (1 << 0))
        antispam = bool(flags2 & (1 << 1))
        participants_hidden = bool(flags2 & (1 << 2))
        translations_disabled = bool(flags2 & (1 << 3))
        stories_pinned_available = bool(flags2 & (1 << 5))
        view_forum_as_messages = bool(flags2 & (1 << 6))
        restricted_sponsored = bool(flags2 & (1 << 11))
        can_view_revenue = bool(flags2 & (1 << 12))
        paid_media_allowed = bool(flags2 & (1 << 14))
        can_view_stars_revenue = bool(flags2 & (1 << 15))
        paid_reactions_available = bool(flags2 & (1 << 16))
        stargifts_available = bool(flags2 & (1 << 19))
        paid_messages_available = bool(flags2 & (1 << 20))
        id = reader.read_int64()
        about = reader.read_string()
        participants_count = reader.read_int32() if (flags & (1 << 0)) else None
        admins_count = reader.read_int32() if (flags & (1 << 1)) else None
        kicked_count = reader.read_int32() if (flags & (1 << 2)) else None
        banned_count = reader.read_int32() if (flags & (1 << 2)) else None
        online_count = reader.read_int32() if (flags & (1 << 13)) else None
        read_inbox_max_id = reader.read_int32()
        read_outbox_max_id = reader.read_int32()
        unread_count = reader.read_int32()
        chat_photo = reader.read_object()
        notify_settings = reader.read_object()
        exported_invite = reader.read_object() if (flags & (1 << 23)) else None
        bot_info = reader.read_vector(lambda r: reader.read_object())
        migrated_from_chat_id = reader.read_int64() if (flags & (1 << 4)) else None
        migrated_from_max_id = reader.read_int32() if (flags & (1 << 4)) else None
        pinned_msg_id = reader.read_int32() if (flags & (1 << 5)) else None
        stickerset = reader.read_object() if (flags & (1 << 8)) else None
        available_min_id = reader.read_int32() if (flags & (1 << 9)) else None
        folder_id = reader.read_int32() if (flags & (1 << 11)) else None
        linked_chat_id = reader.read_int64() if (flags & (1 << 14)) else None
        location = reader.read_object() if (flags & (1 << 15)) else None
        slowmode_seconds = reader.read_int32() if (flags & (1 << 17)) else None
        slowmode_next_send_date = reader.read_int32() if (flags & (1 << 18)) else None
        stats_dc = reader.read_int32() if (flags & (1 << 12)) else None
        pts = reader.read_int32()
        call = reader.read_object() if (flags & (1 << 21)) else None
        ttl_period = reader.read_int32() if (flags & (1 << 24)) else None
        pending_suggestions = reader.read_vector(lambda r: r.read_string()) if (flags & (1 << 25)) else None
        groupcall_default_join_as = reader.read_object() if (flags & (1 << 26)) else None
        theme_emoticon = reader.read_string() if (flags & (1 << 27)) else None
        requests_pending = reader.read_int32() if (flags & (1 << 28)) else None
        recent_requesters = reader.read_vector(lambda r: r.read_int64()) if (flags & (1 << 28)) else None
        default_send_as = reader.read_object() if (flags & (1 << 29)) else None
        available_reactions = reader.read_object() if (flags & (1 << 30)) else None
        reactions_limit = reader.read_int32() if (flags2 & (1 << 13)) else None
        stories = reader.read_object() if (flags2 & (1 << 4)) else None
        wallpaper = reader.read_object() if (flags2 & (1 << 7)) else None
        boosts_applied = reader.read_int32() if (flags2 & (1 << 8)) else None
        boosts_unrestrict = reader.read_int32() if (flags2 & (1 << 9)) else None
        emojiset = reader.read_object() if (flags2 & (1 << 10)) else None
        bot_verification = reader.read_object() if (flags2 & (1 << 17)) else None
        stargifts_count = reader.read_int32() if (flags2 & (1 << 18)) else None
        send_paid_messages_stars = reader.read_int64() if (flags2 & (1 << 21)) else None
        main_tab = reader.read_object() if (flags2 & (1 << 22)) else None
        return cls(can_view_participants=can_view_participants, can_set_username=can_set_username, can_set_stickers=can_set_stickers, hidden_prehistory=hidden_prehistory, can_set_location=can_set_location, has_scheduled=has_scheduled, can_view_stats=can_view_stats, blocked=blocked, can_delete_channel=can_delete_channel, antispam=antispam, participants_hidden=participants_hidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, view_forum_as_messages=view_forum_as_messages, restricted_sponsored=restricted_sponsored, can_view_revenue=can_view_revenue, paid_media_allowed=paid_media_allowed, can_view_stars_revenue=can_view_stars_revenue, paid_reactions_available=paid_reactions_available, stargifts_available=stargifts_available, paid_messages_available=paid_messages_available, id=id, about=about, participants_count=participants_count, admins_count=admins_count, kicked_count=kicked_count, banned_count=banned_count, online_count=online_count, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chat_photo=chat_photo, notify_settings=notify_settings, exported_invite=exported_invite, bot_info=bot_info, migrated_from_chat_id=migrated_from_chat_id, migrated_from_max_id=migrated_from_max_id, pinned_msg_id=pinned_msg_id, stickerset=stickerset, available_min_id=available_min_id, folder_id=folder_id, linked_chat_id=linked_chat_id, location=location, slowmode_seconds=slowmode_seconds, slowmode_next_send_date=slowmode_next_send_date, stats_dc=stats_dc, pts=pts, call=call, ttl_period=ttl_period, pending_suggestions=pending_suggestions, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, default_send_as=default_send_as, available_reactions=available_reactions, reactions_limit=reactions_limit, stories=stories, wallpaper=wallpaper, boosts_applied=boosts_applied, boosts_unrestrict=boosts_unrestrict, emojiset=emojiset, bot_verification=bot_verification, stargifts_count=stargifts_count, send_paid_messages_stars=send_paid_messages_stars, main_tab=main_tab)


@register_tl
class ChatParticipant(TLObject):
    ID: int = 0x38e79fde

    def __init__(self, rank: Any = None, user_id: Any = None, inviter_id: Any = None, date: Any = None) -> None:
        self.rank = rank
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipant':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        rank = reader.read_string() if (flags & (1 << 0)) else None
        return cls(user_id=user_id, inviter_id=inviter_id, date=date, rank=rank)


@register_tl
class ChatParticipantCreator(TLObject):
    ID: int = 0xe1f867b8

    def __init__(self, rank: Any = None, user_id: Any = None) -> None:
        self.rank = rank
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantCreator':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        rank = reader.read_string() if (flags & (1 << 0)) else None
        return cls(user_id=user_id, rank=rank)


@register_tl
class ChatParticipantAdmin(TLObject):
    ID: int = 0x360d5d2

    def __init__(self, rank: Any = None, user_id: Any = None, inviter_id: Any = None, date: Any = None) -> None:
        self.rank = rank
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantAdmin':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        rank = reader.read_string() if (flags & (1 << 0)) else None
        return cls(user_id=user_id, inviter_id=inviter_id, date=date, rank=rank)


@register_tl
class ChatParticipantsForbidden(TLObject):
    ID: int = 0x8763d3e1

    def __init__(self, self_participant: Any = None, chat_id: Any = None) -> None:
        self.self_participant = self_participant
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.self_participant is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.chat_id or 0)
        if self.self_participant is not None:
            if self.self_participant is not None and hasattr(self.self_participant, 'write'): self.self_participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantsForbidden':
        flags = reader.read_uint32()
        chat_id = reader.read_int64()
        self_participant = reader.read_object() if (flags & (1 << 0)) else None
        return cls(chat_id=chat_id, self_participant=self_participant)


@register_tl
class ChatParticipants(TLObject):
    ID: int = 0x3cbc93f8

    def __init__(self, chat_id: Any = None, participants: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.participants = participants
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_vector(self.participants or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipants':
        chat_id = reader.read_int64()
        participants = reader.read_vector(lambda r: reader.read_object())
        version = reader.read_int32()
        return cls(chat_id=chat_id, participants=participants, version=version)


@register_tl
class ChatPhotoEmpty(TLObject):
    ID: int = 0x37c1011c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatPhotoEmpty':
        return cls()


@register_tl
class ChatPhoto(TLObject):
    ID: int = 0x1c6e1c11

    def __init__(self, has_video: bool = False, stripped_thumb: Any = None, photo_id: Any = None, dc_id: Any = None) -> None:
        self.has_video = has_video
        self.stripped_thumb = stripped_thumb
        self.photo_id = photo_id
        self.dc_id = dc_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_video:
            flags |= (1 << 0)
        if self.stripped_thumb is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.photo_id or 0)
        if self.stripped_thumb is not None:
            writer.write_bytes(self.stripped_thumb or b'')
        writer.write_int32(self.dc_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatPhoto':
        flags = reader.read_uint32()
        has_video = bool(flags & (1 << 0))
        photo_id = reader.read_int64()
        stripped_thumb = reader.read_bytes() if (flags & (1 << 1)) else None
        dc_id = reader.read_int32()
        return cls(has_video=has_video, photo_id=photo_id, stripped_thumb=stripped_thumb, dc_id=dc_id)


@register_tl
class MessageEmpty(TLObject):
    ID: int = 0x90a6ca84

    def __init__(self, peer_id: Any = None, id: Any = None) -> None:
        self.peer_id = peer_id
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.peer_id is not None:
            if self.peer_id is not None and hasattr(self.peer_id, 'write'): self.peer_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEmpty':
        flags = reader.read_uint32()
        id = reader.read_int32()
        peer_id = reader.read_object() if (flags & (1 << 0)) else None
        return cls(id=id, peer_id=peer_id)

