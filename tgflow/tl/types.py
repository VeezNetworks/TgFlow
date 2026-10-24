from typing import Any
from .core import TLObject, TLWriter, TLReader, register_tl

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
class TLTrue(TLObject):
    ID: int = 0x3fedd339

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'TLTrue':
        return cls()

@register_tl
class Vector(TLObject):
    ID: int = 0x1cb5c415

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'Vector':
        return cls()

@register_tl
class Error(TLObject):
    ID: int = 0xc4b9f9bb

    def __init__(self, code: Any = None, text: Any = None) -> None:
        self.code = code
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.code or 0)
        writer.write_string(str(self.text or ''))

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
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
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
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
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
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
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

    def __init__(self, client_id: Any = None, phone: Any = None, first_name: Any = None, last_name: Any = None, note: Any = None) -> None:
        self.client_id = client_id
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.note = note

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.note is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.client_id or 0)
        writer.write_string(str(self.phone or ''))
        writer.write_string(str(self.first_name or ''))
        writer.write_string(str(self.last_name or ''))
        if self.note is not None:
            if hasattr(self.note, 'write'):
                self.note.write(writer)
            else:
                writer.write_bytes(self.note or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPhoneContact':
        flags = reader.read_uint32()
        client_id = reader.read_int64()
        phone = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        note = None
        if flags & (1 << 0):
            note = reader.read_object()
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
        writer.write_string(str(self.name or ''))
        writer.write_string(str(self.md5_checksum or ''))

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
        writer.write_string(str(self.name or ''))

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
        if hasattr(self.id, 'write'):
            self.id.write(writer)
        else:
            writer.write_bytes(self.id or b'')

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

    def __init__(self, spoiler: bool = False, live_photo: bool = False, file: Any = None, stickers: Any = None, ttl_seconds: Any = None, video: Any = None) -> None:
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.file = file
        self.stickers = stickers
        self.ttl_seconds = ttl_seconds
        self.video = video

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
        if hasattr(self.file, 'write'):
            self.file.write(writer)
        else:
            writer.write_bytes(self.file or b'')
        if self.stickers is not None:
            writer.write_vector(self.stickers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video is not None:
            if hasattr(self.video, 'write'):
                self.video.write(writer)
            else:
                writer.write_bytes(self.video or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaUploadedPhoto':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 2))
        live_photo = bool(flags & (1 << 3))
        file = reader.read_object()
        stickers = None
        if flags & (1 << 0):
            stickers = reader.read_vector(lambda r: r.read_object())
        ttl_seconds = None
        if flags & (1 << 1):
            ttl_seconds = reader.read_int32()
        video = None
        if flags & (1 << 3):
            video = reader.read_object()
        return cls(spoiler=spoiler, live_photo=live_photo, file=file, stickers=stickers, ttl_seconds=ttl_seconds, video=video)

@register_tl
class InputMediaPhoto(TLObject):
    ID: int = 0xe3af4434

    def __init__(self, spoiler: bool = False, live_photo: bool = False, id: Any = None, ttl_seconds: Any = None, video: Any = None) -> None:
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.id = id
        self.ttl_seconds = ttl_seconds
        self.video = video

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
        if hasattr(self.id, 'write'):
            self.id.write(writer)
        else:
            writer.write_bytes(self.id or b'')
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video is not None:
            if hasattr(self.video, 'write'):
                self.video.write(writer)
            else:
                writer.write_bytes(self.video or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPhoto':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 1))
        live_photo = bool(flags & (1 << 2))
        id = reader.read_object()
        ttl_seconds = None
        if flags & (1 << 0):
            ttl_seconds = reader.read_int32()
        video = None
        if flags & (1 << 2):
            video = reader.read_object()
        return cls(spoiler=spoiler, live_photo=live_photo, id=id, ttl_seconds=ttl_seconds, video=video)

@register_tl
class InputMediaGeoPoint(TLObject):
    ID: int = 0xf9c44144

    def __init__(self, geo_point: Any = None) -> None:
        self.geo_point = geo_point

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.geo_point, 'write'):
            self.geo_point.write(writer)
        else:
            writer.write_bytes(self.geo_point or b'')

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
        writer.write_string(str(self.phone_number or ''))
        writer.write_string(str(self.first_name or ''))
        writer.write_string(str(self.last_name or ''))
        writer.write_string(str(self.vcard or ''))

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

    def __init__(self, nosound_video: bool = False, force_file: bool = False, spoiler: bool = False, file: Any = None, thumb: Any = None, mime_type: Any = None, attributes: Any = None, stickers: Any = None, video_cover: Any = None, video_timestamp: Any = None, ttl_seconds: Any = None) -> None:
        self.nosound_video = nosound_video
        self.force_file = force_file
        self.spoiler = spoiler
        self.file = file
        self.thumb = thumb
        self.mime_type = mime_type
        self.attributes = attributes
        self.stickers = stickers
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp
        self.ttl_seconds = ttl_seconds

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
        if hasattr(self.file, 'write'):
            self.file.write(writer)
        else:
            writer.write_bytes(self.file or b'')
        if self.thumb is not None:
            if hasattr(self.thumb, 'write'):
                self.thumb.write(writer)
            else:
                writer.write_bytes(self.thumb or b'')
        writer.write_string(str(self.mime_type or ''))
        writer.write_vector(self.attributes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.stickers is not None:
            writer.write_vector(self.stickers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.video_cover is not None:
            if hasattr(self.video_cover, 'write'):
                self.video_cover.write(writer)
            else:
                writer.write_bytes(self.video_cover or b'')
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
        thumb = None
        if flags & (1 << 2):
            thumb = reader.read_object()
        mime_type = reader.read_string()
        attributes = reader.read_vector(lambda r: r.read_object())
        stickers = None
        if flags & (1 << 0):
            stickers = reader.read_vector(lambda r: r.read_object())
        video_cover = None
        if flags & (1 << 6):
            video_cover = reader.read_object()
        video_timestamp = None
        if flags & (1 << 7):
            video_timestamp = reader.read_int32()
        ttl_seconds = None
        if flags & (1 << 1):
            ttl_seconds = reader.read_int32()
        return cls(nosound_video=nosound_video, force_file=force_file, spoiler=spoiler, file=file, thumb=thumb, mime_type=mime_type, attributes=attributes, stickers=stickers, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds)

@register_tl
class InputMediaDocument(TLObject):
    ID: int = 0xa8763ab5

    def __init__(self, spoiler: bool = False, id: Any = None, video_cover: Any = None, video_timestamp: Any = None, ttl_seconds: Any = None, query: Any = None) -> None:
        self.spoiler = spoiler
        self.id = id
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp
        self.ttl_seconds = ttl_seconds
        self.query = query

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
        if hasattr(self.id, 'write'):
            self.id.write(writer)
        else:
            writer.write_bytes(self.id or b'')
        if self.video_cover is not None:
            if hasattr(self.video_cover, 'write'):
                self.video_cover.write(writer)
            else:
                writer.write_bytes(self.video_cover or b'')
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.query is not None:
            writer.write_string(str(self.query or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaDocument':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 2))
        id = reader.read_object()
        video_cover = None
        if flags & (1 << 3):
            video_cover = reader.read_object()
        video_timestamp = None
        if flags & (1 << 4):
            video_timestamp = reader.read_int32()
        ttl_seconds = None
        if flags & (1 << 0):
            ttl_seconds = reader.read_int32()
        query = None
        if flags & (1 << 1):
            query = reader.read_string()
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
        if hasattr(self.geo_point, 'write'):
            self.geo_point.write(writer)
        else:
            writer.write_bytes(self.geo_point or b'')
        writer.write_string(str(self.title or ''))
        writer.write_string(str(self.address or ''))
        writer.write_string(str(self.provider or ''))
        writer.write_string(str(self.venue_id or ''))
        writer.write_string(str(self.venue_type or ''))

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

    def __init__(self, spoiler: bool = False, url: Any = None, ttl_seconds: Any = None) -> None:
        self.spoiler = spoiler
        self.url = url
        self.ttl_seconds = ttl_seconds

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 1)
        if self.ttl_seconds is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.url or ''))
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPhotoExternal':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 1))
        url = reader.read_string()
        ttl_seconds = None
        if flags & (1 << 0):
            ttl_seconds = reader.read_int32()
        return cls(spoiler=spoiler, url=url, ttl_seconds=ttl_seconds)

@register_tl
class InputMediaDocumentExternal(TLObject):
    ID: int = 0x779600f9

    def __init__(self, spoiler: bool = False, url: Any = None, ttl_seconds: Any = None, video_cover: Any = None, video_timestamp: Any = None) -> None:
        self.spoiler = spoiler
        self.url = url
        self.ttl_seconds = ttl_seconds
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp

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
        writer.write_string(str(self.url or ''))
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video_cover is not None:
            if hasattr(self.video_cover, 'write'):
                self.video_cover.write(writer)
            else:
                writer.write_bytes(self.video_cover or b'')
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaDocumentExternal':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 1))
        url = reader.read_string()
        ttl_seconds = None
        if flags & (1 << 0):
            ttl_seconds = reader.read_int32()
        video_cover = None
        if flags & (1 << 2):
            video_cover = reader.read_object()
        video_timestamp = None
        if flags & (1 << 3):
            video_timestamp = reader.read_int32()
        return cls(spoiler=spoiler, url=url, ttl_seconds=ttl_seconds, video_cover=video_cover, video_timestamp=video_timestamp)

@register_tl
class InputMediaGame(TLObject):
    ID: int = 0xd33f43f3

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.id, 'write'):
            self.id.write(writer)
        else:
            writer.write_bytes(self.id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaGame':
        id = reader.read_object()
        return cls(id=id)

@register_tl
class InputMediaInvoice(TLObject):
    ID: int = 0x405fef0d

    def __init__(self, title: Any = None, description: Any = None, photo: Any = None, invoice: Any = None, payload: Any = None, provider: Any = None, provider_data: Any = None, start_param: Any = None, extended_media: Any = None) -> None:
        self.title = title
        self.description = description
        self.photo = photo
        self.invoice = invoice
        self.payload = payload
        self.provider = provider
        self.provider_data = provider_data
        self.start_param = start_param
        self.extended_media = extended_media

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
        writer.write_string(str(self.title or ''))
        writer.write_string(str(self.description or ''))
        if self.photo is not None:
            if hasattr(self.photo, 'write'):
                self.photo.write(writer)
            else:
                writer.write_bytes(self.photo or b'')
        if hasattr(self.invoice, 'write'):
            self.invoice.write(writer)
        else:
            writer.write_bytes(self.invoice or b'')
        writer.write_bytes(self.payload or b'')
        if self.provider is not None:
            writer.write_string(str(self.provider or ''))
        if hasattr(self.provider_data, 'write'):
            self.provider_data.write(writer)
        else:
            writer.write_bytes(self.provider_data or b'')
        if self.start_param is not None:
            writer.write_string(str(self.start_param or ''))
        if self.extended_media is not None:
            if hasattr(self.extended_media, 'write'):
                self.extended_media.write(writer)
            else:
                writer.write_bytes(self.extended_media or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaInvoice':
        flags = reader.read_uint32()
        title = reader.read_string()
        description = reader.read_string()
        photo = None
        if flags & (1 << 0):
            photo = reader.read_object()
        invoice = reader.read_object()
        payload = reader.read_bytes()
        provider = None
        if flags & (1 << 3):
            provider = reader.read_string()
        provider_data = reader.read_object()
        start_param = None
        if flags & (1 << 1):
            start_param = reader.read_string()
        extended_media = None
        if flags & (1 << 2):
            extended_media = reader.read_object()
        return cls(title=title, description=description, photo=photo, invoice=invoice, payload=payload, provider=provider, provider_data=provider_data, start_param=start_param, extended_media=extended_media)

@register_tl
class InputMediaGeoLive(TLObject):
    ID: int = 0x971fa843

    def __init__(self, stopped: bool = False, geo_point: Any = None, heading: Any = None, period: Any = None, proximity_notification_radius: Any = None) -> None:
        self.stopped = stopped
        self.geo_point = geo_point
        self.heading = heading
        self.period = period
        self.proximity_notification_radius = proximity_notification_radius

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
        if hasattr(self.geo_point, 'write'):
            self.geo_point.write(writer)
        else:
            writer.write_bytes(self.geo_point or b'')
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
        heading = None
        if flags & (1 << 2):
            heading = reader.read_int32()
        period = None
        if flags & (1 << 1):
            period = reader.read_int32()
        proximity_notification_radius = None
        if flags & (1 << 3):
            proximity_notification_radius = reader.read_int32()
        return cls(stopped=stopped, geo_point=geo_point, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius)

@register_tl
class InputMediaPoll(TLObject):
    ID: int = 0x883a4108

    def __init__(self, poll: Any = None, correct_answers: Any = None, attached_media: Any = None, solution: Any = None, solution_entities: Any = None, solution_media: Any = None) -> None:
        self.poll = poll
        self.correct_answers = correct_answers
        self.attached_media = attached_media
        self.solution = solution
        self.solution_entities = solution_entities
        self.solution_media = solution_media

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
        if hasattr(self.poll, 'write'):
            self.poll.write(writer)
        else:
            writer.write_bytes(self.poll or b'')
        if self.correct_answers is not None:
            writer.write_vector(self.correct_answers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.attached_media is not None:
            if hasattr(self.attached_media, 'write'):
                self.attached_media.write(writer)
            else:
                writer.write_bytes(self.attached_media or b'')
        if self.solution is not None:
            writer.write_string(str(self.solution or ''))
        if self.solution_entities is not None:
            writer.write_vector(self.solution_entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.solution_media is not None:
            if hasattr(self.solution_media, 'write'):
                self.solution_media.write(writer)
            else:
                writer.write_bytes(self.solution_media or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPoll':
        flags = reader.read_uint32()
        poll = reader.read_object()
        correct_answers = None
        if flags & (1 << 0):
            correct_answers = reader.read_vector(lambda r: r.read_object())
        attached_media = None
        if flags & (1 << 3):
            attached_media = reader.read_object()
        solution = None
        if flags & (1 << 1):
            solution = reader.read_string()
        solution_entities = None
        if flags & (1 << 1):
            solution_entities = reader.read_vector(lambda r: r.read_object())
        solution_media = None
        if flags & (1 << 2):
            solution_media = reader.read_object()
        return cls(poll=poll, correct_answers=correct_answers, attached_media=attached_media, solution=solution, solution_entities=solution_entities, solution_media=solution_media)

@register_tl
class InputMediaDice(TLObject):
    ID: int = 0xe66fbf7b

    def __init__(self, emoticon: Any = None) -> None:
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.emoticon or ''))

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
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
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
        writer.write_string(str(self.url or ''))

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

    def __init__(self, stars_amount: Any = None, extended_media: Any = None, payload: Any = None) -> None:
        self.stars_amount = stars_amount
        self.extended_media = extended_media
        self.payload = payload

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.payload is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars_amount or 0)
        writer.write_vector(self.extended_media or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.payload is not None:
            writer.write_string(str(self.payload or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMediaPaidMedia':
        flags = reader.read_uint32()
        stars_amount = reader.read_int64()
        extended_media = reader.read_vector(lambda r: r.read_object())
        payload = None
        if flags & (1 << 0):
            payload = reader.read_string()
        return cls(stars_amount=stars_amount, extended_media=extended_media, payload=payload)

@register_tl
class InputMediaTodo(TLObject):
    ID: int = 0x9fc55fde

    def __init__(self, todo: Any = None) -> None:
        self.todo = todo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.todo, 'write'):
            self.todo.write(writer)
        else:
            writer.write_bytes(self.todo or b'')

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
        writer.write_string(str(self.game_hash or ''))
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
            if hasattr(self.file, 'write'):
                self.file.write(writer)
            else:
                writer.write_bytes(self.file or b'')
        if self.video is not None:
            if hasattr(self.video, 'write'):
                self.video.write(writer)
            else:
                writer.write_bytes(self.video or b'')
        if self.video_start_ts is not None:
            writer.write_double(float(self.video_start_ts or 0.0))
        if self.video_emoji_markup is not None:
            if hasattr(self.video_emoji_markup, 'write'):
                self.video_emoji_markup.write(writer)
            else:
                writer.write_bytes(self.video_emoji_markup or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputChatUploadedPhoto':
        flags = reader.read_uint32()
        file = None
        if flags & (1 << 0):
            file = reader.read_object()
        video = None
        if flags & (1 << 1):
            video = reader.read_object()
        video_start_ts = None
        if flags & (1 << 2):
            video_start_ts = reader.read_double()
        video_emoji_markup = None
        if flags & (1 << 3):
            video_emoji_markup = reader.read_object()
        return cls(file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

@register_tl
class InputChatPhoto(TLObject):
    ID: int = 0x8953ad37

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.id, 'write'):
            self.id.write(writer)
        else:
            writer.write_bytes(self.id or b'')

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

    def __init__(self, lat: Any = None, long: Any = None, accuracy_radius: Any = None) -> None:
        self.lat = lat
        self.long = long
        self.accuracy_radius = accuracy_radius

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accuracy_radius is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_double(float(self.lat or 0.0))
        writer.write_double(float(self.long or 0.0))
        if self.accuracy_radius is not None:
            writer.write_int32(self.accuracy_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputGeoPoint':
        flags = reader.read_uint32()
        lat = reader.read_double()
        long = reader.read_double()
        accuracy_radius = None
        if flags & (1 << 0):
            accuracy_radius = reader.read_int32()
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
        writer.write_string(str(self.thumb_size or ''))

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
        writer.write_string(str(self.thumb_size or ''))

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
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
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
        if hasattr(self.stickerset, 'write'):
            self.stickerset.write(writer)
        else:
            writer.write_bytes(self.stickerset or b'')
        writer.write_int32(self.thumb_version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetThumb':
        stickerset = reader.read_object()
        thumb_version = reader.read_int32()
        return cls(stickerset=stickerset, thumb_version=thumb_version)

@register_tl
class InputGroupCallStream(TLObject):
    ID: int = 0x598a92a

    def __init__(self, call: Any = None, time_ms: Any = None, scale: Any = None, video_channel: Any = None, video_quality: Any = None) -> None:
        self.call = call
        self.time_ms = time_ms
        self.scale = scale
        self.video_channel = video_channel
        self.video_quality = video_quality

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video_channel is not None:
            flags |= (1 << 0)
        if self.video_quality is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
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
        video_channel = None
        if flags & (1 << 0):
            video_channel = reader.read_int32()
        video_quality = None
        if flags & (1 << 0):
            video_quality = reader.read_int32()
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

    def __init__(self, is_self: bool = False, contact: bool = False, mutual_contact: bool = False, deleted: bool = False, bot: bool = False, bot_chat_history: bool = False, bot_nochats: bool = False, verified: bool = False, restricted: bool = False, min: bool = False, bot_inline_geo: bool = False, support: bool = False, scam: bool = False, apply_min_photo: bool = False, fake: bool = False, bot_attach_menu: bool = False, premium: bool = False, attach_menu_enabled: bool = False, bot_can_edit: bool = False, close_friend: bool = False, stories_hidden: bool = False, stories_unavailable: bool = False, contact_require_premium: bool = False, bot_business: bool = False, bot_has_main_app: bool = False, bot_forum_view: bool = False, bot_forum_can_manage_topics: bool = False, bot_can_manage_bots: bool = False, bot_guestchat: bool = False, id: Any = None, access_hash: Any = None, first_name: Any = None, last_name: Any = None, username: Any = None, phone: Any = None, photo: Any = None, status: Any = None, bot_info_version: Any = None, restriction_reason: Any = None, bot_inline_placeholder: Any = None, lang_code: Any = None, emoji_status: Any = None, usernames: Any = None, stories_max_id: Any = None, color: Any = None, profile_color: Any = None, bot_active_users: Any = None, bot_verification_icon: Any = None, send_paid_messages_stars: Any = None) -> None:
        self.is_self = is_self
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
        self.id = id
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

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.is_self:
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
            flags |= (1 << 1)
        if self.close_friend:
            flags |= (1 << 2)
        if self.stories_hidden:
            flags |= (1 << 3)
        if self.stories_unavailable:
            flags |= (1 << 4)
        if self.contact_require_premium:
            flags |= (1 << 10)
        if self.bot_business:
            flags |= (1 << 11)
        if self.bot_has_main_app:
            flags |= (1 << 13)
        if self.bot_forum_view:
            flags |= (1 << 16)
        if self.bot_forum_can_manage_topics:
            flags |= (1 << 17)
        if self.bot_can_manage_bots:
            flags |= (1 << 18)
        if self.bot_guestchat:
            flags |= (1 << 19)
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
            flags |= (1 << 0)
        if self.stories_max_id is not None:
            flags |= (1 << 5)
        if self.color is not None:
            flags |= (1 << 8)
        if self.profile_color is not None:
            flags |= (1 << 9)
        if self.bot_active_users is not None:
            flags |= (1 << 12)
        if self.bot_verification_icon is not None:
            flags |= (1 << 14)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 15)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.access_hash is not None:
            writer.write_int64(self.access_hash or 0)
        if self.first_name is not None:
            writer.write_string(str(self.first_name or ''))
        if self.last_name is not None:
            writer.write_string(str(self.last_name or ''))
        if self.username is not None:
            writer.write_string(str(self.username or ''))
        if self.phone is not None:
            writer.write_string(str(self.phone or ''))
        if self.photo is not None:
            if hasattr(self.photo, 'write'):
                self.photo.write(writer)
            else:
                writer.write_bytes(self.photo or b'')
        if self.status is not None:
            if hasattr(self.status, 'write'):
                self.status.write(writer)
            else:
                writer.write_bytes(self.status or b'')
        if self.bot_info_version is not None:
            writer.write_int32(self.bot_info_version or 0)
        if self.restriction_reason is not None:
            writer.write_vector(self.restriction_reason or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.bot_inline_placeholder is not None:
            writer.write_string(str(self.bot_inline_placeholder or ''))
        if self.lang_code is not None:
            writer.write_string(str(self.lang_code or ''))
        if self.emoji_status is not None:
            if hasattr(self.emoji_status, 'write'):
                self.emoji_status.write(writer)
            else:
                writer.write_bytes(self.emoji_status or b'')
        if self.usernames is not None:
            writer.write_vector(self.usernames or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.stories_max_id is not None:
            if hasattr(self.stories_max_id, 'write'):
                self.stories_max_id.write(writer)
            else:
                writer.write_bytes(self.stories_max_id or b'')
        if self.color is not None:
            if hasattr(self.color, 'write'):
                self.color.write(writer)
            else:
                writer.write_bytes(self.color or b'')
        if self.profile_color is not None:
            if hasattr(self.profile_color, 'write'):
                self.profile_color.write(writer)
            else:
                writer.write_bytes(self.profile_color or b'')
        if self.bot_active_users is not None:
            writer.write_int32(self.bot_active_users or 0)
        if self.bot_verification_icon is not None:
            writer.write_int64(self.bot_verification_icon or 0)
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'User':
        flags = reader.read_uint32()
        is_self = bool(flags & (1 << 10))
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
        bot_can_edit = bool(flags & (1 << 1))
        close_friend = bool(flags & (1 << 2))
        stories_hidden = bool(flags & (1 << 3))
        stories_unavailable = bool(flags & (1 << 4))
        contact_require_premium = bool(flags & (1 << 10))
        bot_business = bool(flags & (1 << 11))
        bot_has_main_app = bool(flags & (1 << 13))
        bot_forum_view = bool(flags & (1 << 16))
        bot_forum_can_manage_topics = bool(flags & (1 << 17))
        bot_can_manage_bots = bool(flags & (1 << 18))
        bot_guestchat = bool(flags & (1 << 19))
        id = reader.read_int64()
        access_hash = None
        if flags & (1 << 0):
            access_hash = reader.read_int64()
        first_name = None
        if flags & (1 << 1):
            first_name = reader.read_string()
        last_name = None
        if flags & (1 << 2):
            last_name = reader.read_string()
        username = None
        if flags & (1 << 3):
            username = reader.read_string()
        phone = None
        if flags & (1 << 4):
            phone = reader.read_string()
        photo = None
        if flags & (1 << 5):
            photo = reader.read_object()
        status = None
        if flags & (1 << 6):
            status = reader.read_object()
        bot_info_version = None
        if flags & (1 << 14):
            bot_info_version = reader.read_int32()
        restriction_reason = None
        if flags & (1 << 18):
            restriction_reason = reader.read_vector(lambda r: r.read_object())
        bot_inline_placeholder = None
        if flags & (1 << 19):
            bot_inline_placeholder = reader.read_string()
        lang_code = None
        if flags & (1 << 22):
            lang_code = reader.read_string()
        emoji_status = None
        if flags & (1 << 30):
            emoji_status = reader.read_object()
        usernames = None
        if flags & (1 << 0):
            usernames = reader.read_vector(lambda r: r.read_object())
        stories_max_id = None
        if flags & (1 << 5):
            stories_max_id = reader.read_object()
        color = None
        if flags & (1 << 8):
            color = reader.read_object()
        profile_color = None
        if flags & (1 << 9):
            profile_color = reader.read_object()
        bot_active_users = None
        if flags & (1 << 12):
            bot_active_users = reader.read_int32()
        bot_verification_icon = None
        if flags & (1 << 14):
            bot_verification_icon = reader.read_int64()
        send_paid_messages_stars = None
        if flags & (1 << 15):
            send_paid_messages_stars = reader.read_int64()
        return cls(is_self=is_self, contact=contact, mutual_contact=mutual_contact, deleted=deleted, bot=bot, bot_chat_history=bot_chat_history, bot_nochats=bot_nochats, verified=verified, restricted=restricted, min=min, bot_inline_geo=bot_inline_geo, support=support, scam=scam, apply_min_photo=apply_min_photo, fake=fake, bot_attach_menu=bot_attach_menu, premium=premium, attach_menu_enabled=attach_menu_enabled, bot_can_edit=bot_can_edit, close_friend=close_friend, stories_hidden=stories_hidden, stories_unavailable=stories_unavailable, contact_require_premium=contact_require_premium, bot_business=bot_business, bot_has_main_app=bot_has_main_app, bot_forum_view=bot_forum_view, bot_forum_can_manage_topics=bot_forum_can_manage_topics, bot_can_manage_bots=bot_can_manage_bots, bot_guestchat=bot_guestchat, id=id, access_hash=access_hash, first_name=first_name, last_name=last_name, username=username, phone=phone, photo=photo, status=status, bot_info_version=bot_info_version, restriction_reason=restriction_reason, bot_inline_placeholder=bot_inline_placeholder, lang_code=lang_code, emoji_status=emoji_status, usernames=usernames, stories_max_id=stories_max_id, color=color, profile_color=profile_color, bot_active_users=bot_active_users, bot_verification_icon=bot_verification_icon, send_paid_messages_stars=send_paid_messages_stars)

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

    def __init__(self, has_video: bool = False, personal: bool = False, photo_id: Any = None, stripped_thumb: Any = None, dc_id: Any = None) -> None:
        self.has_video = has_video
        self.personal = personal
        self.photo_id = photo_id
        self.stripped_thumb = stripped_thumb
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
        stripped_thumb = None
        if flags & (1 << 1):
            stripped_thumb = reader.read_bytes()
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

    def __init__(self, creator: bool = False, left: bool = False, deactivated: bool = False, call_active: bool = False, call_not_empty: bool = False, noforwards: bool = False, id: Any = None, title: Any = None, photo: Any = None, participants_count: Any = None, date: Any = None, version: Any = None, migrated_to: Any = None, admin_rights: Any = None, default_banned_rights: Any = None) -> None:
        self.creator = creator
        self.left = left
        self.deactivated = deactivated
        self.call_active = call_active
        self.call_not_empty = call_not_empty
        self.noforwards = noforwards
        self.id = id
        self.title = title
        self.photo = photo
        self.participants_count = participants_count
        self.date = date
        self.version = version
        self.migrated_to = migrated_to
        self.admin_rights = admin_rights
        self.default_banned_rights = default_banned_rights

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
        writer.write_string(str(self.title or ''))
        if hasattr(self.photo, 'write'):
            self.photo.write(writer)
        else:
            writer.write_bytes(self.photo or b'')
        writer.write_int32(self.participants_count or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.version or 0)
        if self.migrated_to is not None:
            if hasattr(self.migrated_to, 'write'):
                self.migrated_to.write(writer)
            else:
                writer.write_bytes(self.migrated_to or b'')
        if self.admin_rights is not None:
            if hasattr(self.admin_rights, 'write'):
                self.admin_rights.write(writer)
            else:
                writer.write_bytes(self.admin_rights or b'')
        if self.default_banned_rights is not None:
            if hasattr(self.default_banned_rights, 'write'):
                self.default_banned_rights.write(writer)
            else:
                writer.write_bytes(self.default_banned_rights or b'')

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
        migrated_to = None
        if flags & (1 << 6):
            migrated_to = reader.read_object()
        admin_rights = None
        if flags & (1 << 14):
            admin_rights = reader.read_object()
        default_banned_rights = None
        if flags & (1 << 18):
            default_banned_rights = reader.read_object()
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
        writer.write_string(str(self.title or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatForbidden':
        id = reader.read_int64()
        title = reader.read_string()
        return cls(id=id, title=title)

@register_tl
class Channel(TLObject):
    ID: int = 0x1c32b11c

    def __init__(self, creator: bool = False, left: bool = False, broadcast: bool = False, verified: bool = False, megagroup: bool = False, restricted: bool = False, signatures: bool = False, min: bool = False, scam: bool = False, has_link: bool = False, has_geo: bool = False, slowmode_enabled: bool = False, call_active: bool = False, call_not_empty: bool = False, fake: bool = False, gigagroup: bool = False, noforwards: bool = False, join_to_send: bool = False, join_request: bool = False, forum: bool = False, stories_hidden: bool = False, stories_hidden_min: bool = False, stories_unavailable: bool = False, signature_profiles: bool = False, autotranslation: bool = False, broadcast_messages_allowed: bool = False, monoforum: bool = False, forum_tabs: bool = False, id: Any = None, access_hash: Any = None, title: Any = None, username: Any = None, photo: Any = None, date: Any = None, restriction_reason: Any = None, admin_rights: Any = None, banned_rights: Any = None, default_banned_rights: Any = None, participants_count: Any = None, usernames: Any = None, stories_max_id: Any = None, color: Any = None, profile_color: Any = None, emoji_status: Any = None, level: Any = None, subscription_until_date: Any = None, bot_verification_icon: Any = None, send_paid_messages_stars: Any = None, linked_monoforum_id: Any = None) -> None:
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
        self.id = id
        self.access_hash = access_hash
        self.title = title
        self.username = username
        self.photo = photo
        self.date = date
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

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
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
            flags |= (1 << 1)
        if self.stories_hidden_min:
            flags |= (1 << 2)
        if self.stories_unavailable:
            flags |= (1 << 3)
        if self.signature_profiles:
            flags |= (1 << 12)
        if self.autotranslation:
            flags |= (1 << 15)
        if self.broadcast_messages_allowed:
            flags |= (1 << 16)
        if self.monoforum:
            flags |= (1 << 17)
        if self.forum_tabs:
            flags |= (1 << 19)
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
            flags |= (1 << 0)
        if self.stories_max_id is not None:
            flags |= (1 << 4)
        if self.color is not None:
            flags |= (1 << 7)
        if self.profile_color is not None:
            flags |= (1 << 8)
        if self.emoji_status is not None:
            flags |= (1 << 9)
        if self.level is not None:
            flags |= (1 << 10)
        if self.subscription_until_date is not None:
            flags |= (1 << 11)
        if self.bot_verification_icon is not None:
            flags |= (1 << 13)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 14)
        if self.linked_monoforum_id is not None:
            flags |= (1 << 18)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.access_hash is not None:
            writer.write_int64(self.access_hash or 0)
        writer.write_string(str(self.title or ''))
        if self.username is not None:
            writer.write_string(str(self.username or ''))
        if hasattr(self.photo, 'write'):
            self.photo.write(writer)
        else:
            writer.write_bytes(self.photo or b'')
        writer.write_int32(self.date or 0)
        if self.restriction_reason is not None:
            writer.write_vector(self.restriction_reason or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.admin_rights is not None:
            if hasattr(self.admin_rights, 'write'):
                self.admin_rights.write(writer)
            else:
                writer.write_bytes(self.admin_rights or b'')
        if self.banned_rights is not None:
            if hasattr(self.banned_rights, 'write'):
                self.banned_rights.write(writer)
            else:
                writer.write_bytes(self.banned_rights or b'')
        if self.default_banned_rights is not None:
            if hasattr(self.default_banned_rights, 'write'):
                self.default_banned_rights.write(writer)
            else:
                writer.write_bytes(self.default_banned_rights or b'')
        if self.participants_count is not None:
            writer.write_int32(self.participants_count or 0)
        if self.usernames is not None:
            writer.write_vector(self.usernames or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.stories_max_id is not None:
            if hasattr(self.stories_max_id, 'write'):
                self.stories_max_id.write(writer)
            else:
                writer.write_bytes(self.stories_max_id or b'')
        if self.color is not None:
            if hasattr(self.color, 'write'):
                self.color.write(writer)
            else:
                writer.write_bytes(self.color or b'')
        if self.profile_color is not None:
            if hasattr(self.profile_color, 'write'):
                self.profile_color.write(writer)
            else:
                writer.write_bytes(self.profile_color or b'')
        if self.emoji_status is not None:
            if hasattr(self.emoji_status, 'write'):
                self.emoji_status.write(writer)
            else:
                writer.write_bytes(self.emoji_status or b'')
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
        stories_hidden = bool(flags & (1 << 1))
        stories_hidden_min = bool(flags & (1 << 2))
        stories_unavailable = bool(flags & (1 << 3))
        signature_profiles = bool(flags & (1 << 12))
        autotranslation = bool(flags & (1 << 15))
        broadcast_messages_allowed = bool(flags & (1 << 16))
        monoforum = bool(flags & (1 << 17))
        forum_tabs = bool(flags & (1 << 19))
        id = reader.read_int64()
        access_hash = None
        if flags & (1 << 13):
            access_hash = reader.read_int64()
        title = reader.read_string()
        username = None
        if flags & (1 << 6):
            username = reader.read_string()
        photo = reader.read_object()
        date = reader.read_int32()
        restriction_reason = None
        if flags & (1 << 9):
            restriction_reason = reader.read_vector(lambda r: r.read_object())
        admin_rights = None
        if flags & (1 << 14):
            admin_rights = reader.read_object()
        banned_rights = None
        if flags & (1 << 15):
            banned_rights = reader.read_object()
        default_banned_rights = None
        if flags & (1 << 18):
            default_banned_rights = reader.read_object()
        participants_count = None
        if flags & (1 << 17):
            participants_count = reader.read_int32()
        usernames = None
        if flags & (1 << 0):
            usernames = reader.read_vector(lambda r: r.read_object())
        stories_max_id = None
        if flags & (1 << 4):
            stories_max_id = reader.read_object()
        color = None
        if flags & (1 << 7):
            color = reader.read_object()
        profile_color = None
        if flags & (1 << 8):
            profile_color = reader.read_object()
        emoji_status = None
        if flags & (1 << 9):
            emoji_status = reader.read_object()
        level = None
        if flags & (1 << 10):
            level = reader.read_int32()
        subscription_until_date = None
        if flags & (1 << 11):
            subscription_until_date = reader.read_int32()
        bot_verification_icon = None
        if flags & (1 << 13):
            bot_verification_icon = reader.read_int64()
        send_paid_messages_stars = None
        if flags & (1 << 14):
            send_paid_messages_stars = reader.read_int64()
        linked_monoforum_id = None
        if flags & (1 << 18):
            linked_monoforum_id = reader.read_int64()
        return cls(creator=creator, left=left, broadcast=broadcast, verified=verified, megagroup=megagroup, restricted=restricted, signatures=signatures, min=min, scam=scam, has_link=has_link, has_geo=has_geo, slowmode_enabled=slowmode_enabled, call_active=call_active, call_not_empty=call_not_empty, fake=fake, gigagroup=gigagroup, noforwards=noforwards, join_to_send=join_to_send, join_request=join_request, forum=forum, stories_hidden=stories_hidden, stories_hidden_min=stories_hidden_min, stories_unavailable=stories_unavailable, signature_profiles=signature_profiles, autotranslation=autotranslation, broadcast_messages_allowed=broadcast_messages_allowed, monoforum=monoforum, forum_tabs=forum_tabs, id=id, access_hash=access_hash, title=title, username=username, photo=photo, date=date, restriction_reason=restriction_reason, admin_rights=admin_rights, banned_rights=banned_rights, default_banned_rights=default_banned_rights, participants_count=participants_count, usernames=usernames, stories_max_id=stories_max_id, color=color, profile_color=profile_color, emoji_status=emoji_status, level=level, subscription_until_date=subscription_until_date, bot_verification_icon=bot_verification_icon, send_paid_messages_stars=send_paid_messages_stars, linked_monoforum_id=linked_monoforum_id)

@register_tl
class ChannelForbidden(TLObject):
    ID: int = 0x17d493d5

    def __init__(self, broadcast: bool = False, megagroup: bool = False, monoforum: bool = False, id: Any = None, access_hash: Any = None, title: Any = None, until_date: Any = None) -> None:
        self.broadcast = broadcast
        self.megagroup = megagroup
        self.monoforum = monoforum
        self.id = id
        self.access_hash = access_hash
        self.title = title
        self.until_date = until_date

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
        writer.write_string(str(self.title or ''))
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
        until_date = None
        if flags & (1 << 16):
            until_date = reader.read_int32()
        return cls(broadcast=broadcast, megagroup=megagroup, monoforum=monoforum, id=id, access_hash=access_hash, title=title, until_date=until_date)

@register_tl
class ChatFull(TLObject):
    ID: int = 0x2633421b

    def __init__(self, can_set_username: bool = False, has_scheduled: bool = False, translations_disabled: bool = False, id: Any = None, about: Any = None, participants: Any = None, chat_photo: Any = None, notify_settings: Any = None, exported_invite: Any = None, bot_info: Any = None, pinned_msg_id: Any = None, folder_id: Any = None, call: Any = None, ttl_period: Any = None, groupcall_default_join_as: Any = None, theme_emoticon: Any = None, requests_pending: Any = None, recent_requesters: Any = None, available_reactions: Any = None, reactions_limit: Any = None) -> None:
        self.can_set_username = can_set_username
        self.has_scheduled = has_scheduled
        self.translations_disabled = translations_disabled
        self.id = id
        self.about = about
        self.participants = participants
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
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
        writer.write_string(str(self.about or ''))
        if hasattr(self.participants, 'write'):
            self.participants.write(writer)
        else:
            writer.write_bytes(self.participants or b'')
        if self.chat_photo is not None:
            if hasattr(self.chat_photo, 'write'):
                self.chat_photo.write(writer)
            else:
                writer.write_bytes(self.chat_photo or b'')
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')
        if self.exported_invite is not None:
            if hasattr(self.exported_invite, 'write'):
                self.exported_invite.write(writer)
            else:
                writer.write_bytes(self.exported_invite or b'')
        if self.bot_info is not None:
            writer.write_vector(self.bot_info or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.call is not None:
            if hasattr(self.call, 'write'):
                self.call.write(writer)
            else:
                writer.write_bytes(self.call or b'')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.groupcall_default_join_as is not None:
            if hasattr(self.groupcall_default_join_as, 'write'):
                self.groupcall_default_join_as.write(writer)
            else:
                writer.write_bytes(self.groupcall_default_join_as or b'')
        if self.theme_emoticon is not None:
            writer.write_string(str(self.theme_emoticon or ''))
        if self.requests_pending is not None:
            writer.write_int32(self.requests_pending or 0)
        if self.recent_requesters is not None:
            writer.write_vector(self.recent_requesters or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.available_reactions is not None:
            if hasattr(self.available_reactions, 'write'):
                self.available_reactions.write(writer)
            else:
                writer.write_bytes(self.available_reactions or b'')
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
        chat_photo = None
        if flags & (1 << 2):
            chat_photo = reader.read_object()
        notify_settings = reader.read_object()
        exported_invite = None
        if flags & (1 << 13):
            exported_invite = reader.read_object()
        bot_info = None
        if flags & (1 << 3):
            bot_info = reader.read_vector(lambda r: r.read_object())
        pinned_msg_id = None
        if flags & (1 << 6):
            pinned_msg_id = reader.read_int32()
        folder_id = None
        if flags & (1 << 11):
            folder_id = reader.read_int32()
        call = None
        if flags & (1 << 12):
            call = reader.read_object()
        ttl_period = None
        if flags & (1 << 14):
            ttl_period = reader.read_int32()
        groupcall_default_join_as = None
        if flags & (1 << 15):
            groupcall_default_join_as = reader.read_object()
        theme_emoticon = None
        if flags & (1 << 16):
            theme_emoticon = reader.read_string()
        requests_pending = None
        if flags & (1 << 17):
            requests_pending = reader.read_int32()
        recent_requesters = None
        if flags & (1 << 17):
            recent_requesters = reader.read_vector(lambda r: r.read_object())
        available_reactions = None
        if flags & (1 << 18):
            available_reactions = reader.read_object()
        reactions_limit = None
        if flags & (1 << 20):
            reactions_limit = reader.read_int32()
        return cls(can_set_username=can_set_username, has_scheduled=has_scheduled, translations_disabled=translations_disabled, id=id, about=about, participants=participants, chat_photo=chat_photo, notify_settings=notify_settings, exported_invite=exported_invite, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, call=call, ttl_period=ttl_period, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, available_reactions=available_reactions, reactions_limit=reactions_limit)

@register_tl
class ChannelFull(TLObject):
    ID: int = 0xe4e0b29d

    def __init__(self, can_view_participants: bool = False, can_set_username: bool = False, can_set_stickers: bool = False, hidden_prehistory: bool = False, can_set_location: bool = False, has_scheduled: bool = False, can_view_stats: bool = False, blocked: bool = False, can_delete_channel: bool = False, antispam: bool = False, participants_hidden: bool = False, translations_disabled: bool = False, stories_pinned_available: bool = False, view_forum_as_messages: bool = False, restricted_sponsored: bool = False, can_view_revenue: bool = False, paid_media_allowed: bool = False, can_view_stars_revenue: bool = False, paid_reactions_available: bool = False, stargifts_available: bool = False, paid_messages_available: bool = False, id: Any = None, about: Any = None, participants_count: Any = None, admins_count: Any = None, kicked_count: Any = None, banned_count: Any = None, online_count: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, chat_photo: Any = None, notify_settings: Any = None, exported_invite: Any = None, bot_info: Any = None, migrated_from_chat_id: Any = None, migrated_from_max_id: Any = None, pinned_msg_id: Any = None, stickerset: Any = None, available_min_id: Any = None, folder_id: Any = None, linked_chat_id: Any = None, location: Any = None, slowmode_seconds: Any = None, slowmode_next_send_date: Any = None, stats_dc: Any = None, pts: Any = None, call: Any = None, ttl_period: Any = None, pending_suggestions: Any = None, groupcall_default_join_as: Any = None, theme_emoticon: Any = None, requests_pending: Any = None, recent_requesters: Any = None, default_send_as: Any = None, available_reactions: Any = None, reactions_limit: Any = None, stories: Any = None, wallpaper: Any = None, boosts_applied: Any = None, boosts_unrestrict: Any = None, emojiset: Any = None, bot_verification: Any = None, stargifts_count: Any = None, send_paid_messages_stars: Any = None, main_tab: Any = None) -> None:
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
        self.id = id
        self.about = about
        self.participants_count = participants_count
        self.admins_count = admins_count
        self.kicked_count = kicked_count
        self.banned_count = banned_count
        self.online_count = online_count
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.chat_photo = chat_photo
        self.notify_settings = notify_settings
        self.exported_invite = exported_invite
        self.bot_info = bot_info
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
        self.pts = pts
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

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
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
            flags |= (1 << 0)
        if self.antispam:
            flags |= (1 << 1)
        if self.participants_hidden:
            flags |= (1 << 2)
        if self.translations_disabled:
            flags |= (1 << 3)
        if self.stories_pinned_available:
            flags |= (1 << 5)
        if self.view_forum_as_messages:
            flags |= (1 << 6)
        if self.restricted_sponsored:
            flags |= (1 << 11)
        if self.can_view_revenue:
            flags |= (1 << 12)
        if self.paid_media_allowed:
            flags |= (1 << 14)
        if self.can_view_stars_revenue:
            flags |= (1 << 15)
        if self.paid_reactions_available:
            flags |= (1 << 16)
        if self.stargifts_available:
            flags |= (1 << 19)
        if self.paid_messages_available:
            flags |= (1 << 20)
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
            flags |= (1 << 13)
        if self.stories is not None:
            flags |= (1 << 4)
        if self.wallpaper is not None:
            flags |= (1 << 7)
        if self.boosts_applied is not None:
            flags |= (1 << 8)
        if self.boosts_unrestrict is not None:
            flags |= (1 << 9)
        if self.emojiset is not None:
            flags |= (1 << 10)
        if self.bot_verification is not None:
            flags |= (1 << 17)
        if self.stargifts_count is not None:
            flags |= (1 << 18)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 21)
        if self.main_tab is not None:
            flags |= (1 << 22)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(str(self.about or ''))
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
        if hasattr(self.chat_photo, 'write'):
            self.chat_photo.write(writer)
        else:
            writer.write_bytes(self.chat_photo or b'')
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')
        if self.exported_invite is not None:
            if hasattr(self.exported_invite, 'write'):
                self.exported_invite.write(writer)
            else:
                writer.write_bytes(self.exported_invite or b'')
        writer.write_vector(self.bot_info or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.migrated_from_chat_id is not None:
            writer.write_int64(self.migrated_from_chat_id or 0)
        if self.migrated_from_max_id is not None:
            writer.write_int32(self.migrated_from_max_id or 0)
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        if self.stickerset is not None:
            if hasattr(self.stickerset, 'write'):
                self.stickerset.write(writer)
            else:
                writer.write_bytes(self.stickerset or b'')
        if self.available_min_id is not None:
            writer.write_int32(self.available_min_id or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.linked_chat_id is not None:
            writer.write_int64(self.linked_chat_id or 0)
        if self.location is not None:
            if hasattr(self.location, 'write'):
                self.location.write(writer)
            else:
                writer.write_bytes(self.location or b'')
        if self.slowmode_seconds is not None:
            writer.write_int32(self.slowmode_seconds or 0)
        if self.slowmode_next_send_date is not None:
            writer.write_int32(self.slowmode_next_send_date or 0)
        if self.stats_dc is not None:
            writer.write_int32(self.stats_dc or 0)
        writer.write_int32(self.pts or 0)
        if self.call is not None:
            if hasattr(self.call, 'write'):
                self.call.write(writer)
            else:
                writer.write_bytes(self.call or b'')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.pending_suggestions is not None:
            writer.write_vector(self.pending_suggestions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.groupcall_default_join_as is not None:
            if hasattr(self.groupcall_default_join_as, 'write'):
                self.groupcall_default_join_as.write(writer)
            else:
                writer.write_bytes(self.groupcall_default_join_as or b'')
        if self.theme_emoticon is not None:
            writer.write_string(str(self.theme_emoticon or ''))
        if self.requests_pending is not None:
            writer.write_int32(self.requests_pending or 0)
        if self.recent_requesters is not None:
            writer.write_vector(self.recent_requesters or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.default_send_as is not None:
            if hasattr(self.default_send_as, 'write'):
                self.default_send_as.write(writer)
            else:
                writer.write_bytes(self.default_send_as or b'')
        if self.available_reactions is not None:
            if hasattr(self.available_reactions, 'write'):
                self.available_reactions.write(writer)
            else:
                writer.write_bytes(self.available_reactions or b'')
        if self.reactions_limit is not None:
            writer.write_int32(self.reactions_limit or 0)
        if self.stories is not None:
            if hasattr(self.stories, 'write'):
                self.stories.write(writer)
            else:
                writer.write_bytes(self.stories or b'')
        if self.wallpaper is not None:
            if hasattr(self.wallpaper, 'write'):
                self.wallpaper.write(writer)
            else:
                writer.write_bytes(self.wallpaper or b'')
        if self.boosts_applied is not None:
            writer.write_int32(self.boosts_applied or 0)
        if self.boosts_unrestrict is not None:
            writer.write_int32(self.boosts_unrestrict or 0)
        if self.emojiset is not None:
            if hasattr(self.emojiset, 'write'):
                self.emojiset.write(writer)
            else:
                writer.write_bytes(self.emojiset or b'')
        if self.bot_verification is not None:
            if hasattr(self.bot_verification, 'write'):
                self.bot_verification.write(writer)
            else:
                writer.write_bytes(self.bot_verification or b'')
        if self.stargifts_count is not None:
            writer.write_int32(self.stargifts_count or 0)
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.main_tab is not None:
            if hasattr(self.main_tab, 'write'):
                self.main_tab.write(writer)
            else:
                writer.write_bytes(self.main_tab or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelFull':
        flags = reader.read_uint32()
        can_view_participants = bool(flags & (1 << 3))
        can_set_username = bool(flags & (1 << 6))
        can_set_stickers = bool(flags & (1 << 7))
        hidden_prehistory = bool(flags & (1 << 10))
        can_set_location = bool(flags & (1 << 16))
        has_scheduled = bool(flags & (1 << 19))
        can_view_stats = bool(flags & (1 << 20))
        blocked = bool(flags & (1 << 22))
        can_delete_channel = bool(flags & (1 << 0))
        antispam = bool(flags & (1 << 1))
        participants_hidden = bool(flags & (1 << 2))
        translations_disabled = bool(flags & (1 << 3))
        stories_pinned_available = bool(flags & (1 << 5))
        view_forum_as_messages = bool(flags & (1 << 6))
        restricted_sponsored = bool(flags & (1 << 11))
        can_view_revenue = bool(flags & (1 << 12))
        paid_media_allowed = bool(flags & (1 << 14))
        can_view_stars_revenue = bool(flags & (1 << 15))
        paid_reactions_available = bool(flags & (1 << 16))
        stargifts_available = bool(flags & (1 << 19))
        paid_messages_available = bool(flags & (1 << 20))
        id = reader.read_int64()
        about = reader.read_string()
        participants_count = None
        if flags & (1 << 0):
            participants_count = reader.read_int32()
        admins_count = None
        if flags & (1 << 1):
            admins_count = reader.read_int32()
        kicked_count = None
        if flags & (1 << 2):
            kicked_count = reader.read_int32()
        banned_count = None
        if flags & (1 << 2):
            banned_count = reader.read_int32()
        online_count = None
        if flags & (1 << 13):
            online_count = reader.read_int32()
        read_inbox_max_id = reader.read_int32()
        read_outbox_max_id = reader.read_int32()
        unread_count = reader.read_int32()
        chat_photo = reader.read_object()
        notify_settings = reader.read_object()
        exported_invite = None
        if flags & (1 << 23):
            exported_invite = reader.read_object()
        bot_info = reader.read_vector(lambda r: r.read_object())
        migrated_from_chat_id = None
        if flags & (1 << 4):
            migrated_from_chat_id = reader.read_int64()
        migrated_from_max_id = None
        if flags & (1 << 4):
            migrated_from_max_id = reader.read_int32()
        pinned_msg_id = None
        if flags & (1 << 5):
            pinned_msg_id = reader.read_int32()
        stickerset = None
        if flags & (1 << 8):
            stickerset = reader.read_object()
        available_min_id = None
        if flags & (1 << 9):
            available_min_id = reader.read_int32()
        folder_id = None
        if flags & (1 << 11):
            folder_id = reader.read_int32()
        linked_chat_id = None
        if flags & (1 << 14):
            linked_chat_id = reader.read_int64()
        location = None
        if flags & (1 << 15):
            location = reader.read_object()
        slowmode_seconds = None
        if flags & (1 << 17):
            slowmode_seconds = reader.read_int32()
        slowmode_next_send_date = None
        if flags & (1 << 18):
            slowmode_next_send_date = reader.read_int32()
        stats_dc = None
        if flags & (1 << 12):
            stats_dc = reader.read_int32()
        pts = reader.read_int32()
        call = None
        if flags & (1 << 21):
            call = reader.read_object()
        ttl_period = None
        if flags & (1 << 24):
            ttl_period = reader.read_int32()
        pending_suggestions = None
        if flags & (1 << 25):
            pending_suggestions = reader.read_vector(lambda r: r.read_object())
        groupcall_default_join_as = None
        if flags & (1 << 26):
            groupcall_default_join_as = reader.read_object()
        theme_emoticon = None
        if flags & (1 << 27):
            theme_emoticon = reader.read_string()
        requests_pending = None
        if flags & (1 << 28):
            requests_pending = reader.read_int32()
        recent_requesters = None
        if flags & (1 << 28):
            recent_requesters = reader.read_vector(lambda r: r.read_object())
        default_send_as = None
        if flags & (1 << 29):
            default_send_as = reader.read_object()
        available_reactions = None
        if flags & (1 << 30):
            available_reactions = reader.read_object()
        reactions_limit = None
        if flags & (1 << 13):
            reactions_limit = reader.read_int32()
        stories = None
        if flags & (1 << 4):
            stories = reader.read_object()
        wallpaper = None
        if flags & (1 << 7):
            wallpaper = reader.read_object()
        boosts_applied = None
        if flags & (1 << 8):
            boosts_applied = reader.read_int32()
        boosts_unrestrict = None
        if flags & (1 << 9):
            boosts_unrestrict = reader.read_int32()
        emojiset = None
        if flags & (1 << 10):
            emojiset = reader.read_object()
        bot_verification = None
        if flags & (1 << 17):
            bot_verification = reader.read_object()
        stargifts_count = None
        if flags & (1 << 18):
            stargifts_count = reader.read_int32()
        send_paid_messages_stars = None
        if flags & (1 << 21):
            send_paid_messages_stars = reader.read_int64()
        main_tab = None
        if flags & (1 << 22):
            main_tab = reader.read_object()
        return cls(can_view_participants=can_view_participants, can_set_username=can_set_username, can_set_stickers=can_set_stickers, hidden_prehistory=hidden_prehistory, can_set_location=can_set_location, has_scheduled=has_scheduled, can_view_stats=can_view_stats, blocked=blocked, can_delete_channel=can_delete_channel, antispam=antispam, participants_hidden=participants_hidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, view_forum_as_messages=view_forum_as_messages, restricted_sponsored=restricted_sponsored, can_view_revenue=can_view_revenue, paid_media_allowed=paid_media_allowed, can_view_stars_revenue=can_view_stars_revenue, paid_reactions_available=paid_reactions_available, stargifts_available=stargifts_available, paid_messages_available=paid_messages_available, id=id, about=about, participants_count=participants_count, admins_count=admins_count, kicked_count=kicked_count, banned_count=banned_count, online_count=online_count, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chat_photo=chat_photo, notify_settings=notify_settings, exported_invite=exported_invite, bot_info=bot_info, migrated_from_chat_id=migrated_from_chat_id, migrated_from_max_id=migrated_from_max_id, pinned_msg_id=pinned_msg_id, stickerset=stickerset, available_min_id=available_min_id, folder_id=folder_id, linked_chat_id=linked_chat_id, location=location, slowmode_seconds=slowmode_seconds, slowmode_next_send_date=slowmode_next_send_date, stats_dc=stats_dc, pts=pts, call=call, ttl_period=ttl_period, pending_suggestions=pending_suggestions, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, default_send_as=default_send_as, available_reactions=available_reactions, reactions_limit=reactions_limit, stories=stories, wallpaper=wallpaper, boosts_applied=boosts_applied, boosts_unrestrict=boosts_unrestrict, emojiset=emojiset, bot_verification=bot_verification, stargifts_count=stargifts_count, send_paid_messages_stars=send_paid_messages_stars, main_tab=main_tab)

@register_tl
class ChatParticipant(TLObject):
    ID: int = 0x38e79fde

    def __init__(self, user_id: Any = None, inviter_id: Any = None, date: Any = None, rank: Any = None) -> None:
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.rank = rank

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
            writer.write_string(str(self.rank or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipant':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        rank = None
        if flags & (1 << 0):
            rank = reader.read_string()
        return cls(user_id=user_id, inviter_id=inviter_id, date=date, rank=rank)

@register_tl
class ChatParticipantCreator(TLObject):
    ID: int = 0xe1f867b8

    def __init__(self, user_id: Any = None, rank: Any = None) -> None:
        self.user_id = user_id
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.rank is not None:
            writer.write_string(str(self.rank or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantCreator':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        rank = None
        if flags & (1 << 0):
            rank = reader.read_string()
        return cls(user_id=user_id, rank=rank)

@register_tl
class ChatParticipantAdmin(TLObject):
    ID: int = 0x360d5d2

    def __init__(self, user_id: Any = None, inviter_id: Any = None, date: Any = None, rank: Any = None) -> None:
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.rank = rank

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
            writer.write_string(str(self.rank or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantAdmin':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        rank = None
        if flags & (1 << 0):
            rank = reader.read_string()
        return cls(user_id=user_id, inviter_id=inviter_id, date=date, rank=rank)

@register_tl
class ChatParticipantsForbidden(TLObject):
    ID: int = 0x8763d3e1

    def __init__(self, chat_id: Any = None, self_participant: Any = None) -> None:
        self.chat_id = chat_id
        self.self_participant = self_participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.self_participant is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.chat_id or 0)
        if self.self_participant is not None:
            if hasattr(self.self_participant, 'write'):
                self.self_participant.write(writer)
            else:
                writer.write_bytes(self.self_participant or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipantsForbidden':
        flags = reader.read_uint32()
        chat_id = reader.read_int64()
        self_participant = None
        if flags & (1 << 0):
            self_participant = reader.read_object()
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
        writer.write_vector(self.participants or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatParticipants':
        chat_id = reader.read_int64()
        participants = reader.read_vector(lambda r: r.read_object())
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

    def __init__(self, has_video: bool = False, photo_id: Any = None, stripped_thumb: Any = None, dc_id: Any = None) -> None:
        self.has_video = has_video
        self.photo_id = photo_id
        self.stripped_thumb = stripped_thumb
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
        stripped_thumb = None
        if flags & (1 << 1):
            stripped_thumb = reader.read_bytes()
        dc_id = reader.read_int32()
        return cls(has_video=has_video, photo_id=photo_id, stripped_thumb=stripped_thumb, dc_id=dc_id)

@register_tl
class MessageEmpty(TLObject):
    ID: int = 0x90a6ca84

    def __init__(self, id: Any = None, peer_id: Any = None) -> None:
        self.id = id
        self.peer_id = peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.peer_id is not None:
            if hasattr(self.peer_id, 'write'):
                self.peer_id.write(writer)
            else:
                writer.write_bytes(self.peer_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEmpty':
        flags = reader.read_uint32()
        id = reader.read_int32()
        peer_id = None
        if flags & (1 << 0):
            peer_id = reader.read_object()
        return cls(id=id, peer_id=peer_id)

@register_tl
class Message(TLObject):
    ID: int = 0x95ef6f2b

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, silent: bool = False, post: bool = False, from_scheduled: bool = False, legacy: bool = False, edit_hide: bool = False, pinned: bool = False, noforwards: bool = False, invert_media: bool = False, offline: bool = False, video_processing_pending: bool = False, paid_suggested_post_stars: bool = False, paid_suggested_post_ton: bool = False, id: Any = None, from_id: Any = None, from_boosts_applied: Any = None, from_rank: Any = None, peer_id: Any = None, saved_peer_id: Any = None, fwd_from: Any = None, via_bot_id: Any = None, via_business_bot_id: Any = None, guestchat_via_from: Any = None, reply_to: Any = None, date: Any = None, message: Any = None, media: Any = None, reply_markup: Any = None, entities: Any = None, views: Any = None, forwards: Any = None, replies: Any = None, edit_date: Any = None, post_author: Any = None, grouped_id: Any = None, reactions: Any = None, restriction_reason: Any = None, ttl_period: Any = None, quick_reply_shortcut_id: Any = None, effect: Any = None, factcheck: Any = None, report_delivery_until_date: Any = None, paid_message_stars: Any = None, suggested_post: Any = None, schedule_repeat_period: Any = None, summary_from_language: Any = None) -> None:
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.silent = silent
        self.post = post
        self.from_scheduled = from_scheduled
        self.legacy = legacy
        self.edit_hide = edit_hide
        self.pinned = pinned
        self.noforwards = noforwards
        self.invert_media = invert_media
        self.offline = offline
        self.video_processing_pending = video_processing_pending
        self.paid_suggested_post_stars = paid_suggested_post_stars
        self.paid_suggested_post_ton = paid_suggested_post_ton
        self.id = id
        self.from_id = from_id
        self.from_boosts_applied = from_boosts_applied
        self.from_rank = from_rank
        self.peer_id = peer_id
        self.saved_peer_id = saved_peer_id
        self.fwd_from = fwd_from
        self.via_bot_id = via_bot_id
        self.via_business_bot_id = via_business_bot_id
        self.guestchat_via_from = guestchat_via_from
        self.reply_to = reply_to
        self.date = date
        self.message = message
        self.media = media
        self.reply_markup = reply_markup
        self.entities = entities
        self.views = views
        self.forwards = forwards
        self.replies = replies
        self.edit_date = edit_date
        self.post_author = post_author
        self.grouped_id = grouped_id
        self.reactions = reactions
        self.restriction_reason = restriction_reason
        self.ttl_period = ttl_period
        self.quick_reply_shortcut_id = quick_reply_shortcut_id
        self.effect = effect
        self.factcheck = factcheck
        self.report_delivery_until_date = report_delivery_until_date
        self.paid_message_stars = paid_message_stars
        self.suggested_post = suggested_post
        self.schedule_repeat_period = schedule_repeat_period
        self.summary_from_language = summary_from_language

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.out:
            flags |= (1 << 1)
        if self.mentioned:
            flags |= (1 << 4)
        if self.media_unread:
            flags |= (1 << 5)
        if self.silent:
            flags |= (1 << 13)
        if self.post:
            flags |= (1 << 14)
        if self.from_scheduled:
            flags |= (1 << 18)
        if self.legacy:
            flags |= (1 << 19)
        if self.edit_hide:
            flags |= (1 << 21)
        if self.pinned:
            flags |= (1 << 24)
        if self.noforwards:
            flags |= (1 << 26)
        if self.invert_media:
            flags |= (1 << 27)
        if self.offline:
            flags |= (1 << 1)
        if self.video_processing_pending:
            flags |= (1 << 4)
        if self.paid_suggested_post_stars:
            flags |= (1 << 8)
        if self.paid_suggested_post_ton:
            flags |= (1 << 9)
        if self.from_id is not None:
            flags |= (1 << 8)
        if self.from_boosts_applied is not None:
            flags |= (1 << 29)
        if self.from_rank is not None:
            flags |= (1 << 12)
        if self.saved_peer_id is not None:
            flags |= (1 << 28)
        if self.fwd_from is not None:
            flags |= (1 << 2)
        if self.via_bot_id is not None:
            flags |= (1 << 11)
        if self.via_business_bot_id is not None:
            flags |= (1 << 0)
        if self.guestchat_via_from is not None:
            flags |= (1 << 19)
        if self.reply_to is not None:
            flags |= (1 << 3)
        if self.media is not None:
            flags |= (1 << 9)
        if self.reply_markup is not None:
            flags |= (1 << 6)
        if self.entities is not None:
            flags |= (1 << 7)
        if self.views is not None:
            flags |= (1 << 10)
        if self.forwards is not None:
            flags |= (1 << 10)
        if self.replies is not None:
            flags |= (1 << 23)
        if self.edit_date is not None:
            flags |= (1 << 15)
        if self.post_author is not None:
            flags |= (1 << 16)
        if self.grouped_id is not None:
            flags |= (1 << 17)
        if self.reactions is not None:
            flags |= (1 << 20)
        if self.restriction_reason is not None:
            flags |= (1 << 22)
        if self.ttl_period is not None:
            flags |= (1 << 25)
        if self.quick_reply_shortcut_id is not None:
            flags |= (1 << 30)
        if self.effect is not None:
            flags |= (1 << 2)
        if self.factcheck is not None:
            flags |= (1 << 3)
        if self.report_delivery_until_date is not None:
            flags |= (1 << 5)
        if self.paid_message_stars is not None:
            flags |= (1 << 6)
        if self.suggested_post is not None:
            flags |= (1 << 7)
        if self.schedule_repeat_period is not None:
            flags |= (1 << 10)
        if self.summary_from_language is not None:
            flags |= (1 << 11)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.from_id is not None:
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if self.from_boosts_applied is not None:
            writer.write_int32(self.from_boosts_applied or 0)
        if self.from_rank is not None:
            writer.write_string(str(self.from_rank or ''))
        if hasattr(self.peer_id, 'write'):
            self.peer_id.write(writer)
        else:
            writer.write_bytes(self.peer_id or b'')
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if self.fwd_from is not None:
            if hasattr(self.fwd_from, 'write'):
                self.fwd_from.write(writer)
            else:
                writer.write_bytes(self.fwd_from or b'')
        if self.via_bot_id is not None:
            writer.write_int64(self.via_bot_id or 0)
        if self.via_business_bot_id is not None:
            writer.write_int64(self.via_business_bot_id or 0)
        if self.guestchat_via_from is not None:
            if hasattr(self.guestchat_via_from, 'write'):
                self.guestchat_via_from.write(writer)
            else:
                writer.write_bytes(self.guestchat_via_from or b'')
        if self.reply_to is not None:
            if hasattr(self.reply_to, 'write'):
                self.reply_to.write(writer)
            else:
                writer.write_bytes(self.reply_to or b'')
        writer.write_int32(self.date or 0)
        writer.write_string(str(self.message or ''))
        if self.media is not None:
            if hasattr(self.media, 'write'):
                self.media.write(writer)
            else:
                writer.write_bytes(self.media or b'')
        if self.reply_markup is not None:
            if hasattr(self.reply_markup, 'write'):
                self.reply_markup.write(writer)
            else:
                writer.write_bytes(self.reply_markup or b'')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.views is not None:
            writer.write_int32(self.views or 0)
        if self.forwards is not None:
            writer.write_int32(self.forwards or 0)
        if self.replies is not None:
            if hasattr(self.replies, 'write'):
                self.replies.write(writer)
            else:
                writer.write_bytes(self.replies or b'')
        if self.edit_date is not None:
            writer.write_int32(self.edit_date or 0)
        if self.post_author is not None:
            writer.write_string(str(self.post_author or ''))
        if self.grouped_id is not None:
            writer.write_int64(self.grouped_id or 0)
        if self.reactions is not None:
            if hasattr(self.reactions, 'write'):
                self.reactions.write(writer)
            else:
                writer.write_bytes(self.reactions or b'')
        if self.restriction_reason is not None:
            writer.write_vector(self.restriction_reason or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.quick_reply_shortcut_id is not None:
            writer.write_int32(self.quick_reply_shortcut_id or 0)
        if self.effect is not None:
            writer.write_int64(self.effect or 0)
        if self.factcheck is not None:
            if hasattr(self.factcheck, 'write'):
                self.factcheck.write(writer)
            else:
                writer.write_bytes(self.factcheck or b'')
        if self.report_delivery_until_date is not None:
            writer.write_int32(self.report_delivery_until_date or 0)
        if self.paid_message_stars is not None:
            writer.write_int64(self.paid_message_stars or 0)
        if self.suggested_post is not None:
            if hasattr(self.suggested_post, 'write'):
                self.suggested_post.write(writer)
            else:
                writer.write_bytes(self.suggested_post or b'')
        if self.schedule_repeat_period is not None:
            writer.write_int32(self.schedule_repeat_period or 0)
        if self.summary_from_language is not None:
            writer.write_string(str(self.summary_from_language or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'Message':
        flags = reader.read_uint32()
        out = bool(flags & (1 << 1))
        mentioned = bool(flags & (1 << 4))
        media_unread = bool(flags & (1 << 5))
        silent = bool(flags & (1 << 13))
        post = bool(flags & (1 << 14))
        from_scheduled = bool(flags & (1 << 18))
        legacy = bool(flags & (1 << 19))
        edit_hide = bool(flags & (1 << 21))
        pinned = bool(flags & (1 << 24))
        noforwards = bool(flags & (1 << 26))
        invert_media = bool(flags & (1 << 27))
        offline = bool(flags & (1 << 1))
        video_processing_pending = bool(flags & (1 << 4))
        paid_suggested_post_stars = bool(flags & (1 << 8))
        paid_suggested_post_ton = bool(flags & (1 << 9))
        id = reader.read_int32()
        from_id = None
        if flags & (1 << 8):
            from_id = reader.read_object()
        from_boosts_applied = None
        if flags & (1 << 29):
            from_boosts_applied = reader.read_int32()
        from_rank = None
        if flags & (1 << 12):
            from_rank = reader.read_string()
        peer_id = reader.read_object()
        saved_peer_id = None
        if flags & (1 << 28):
            saved_peer_id = reader.read_object()
        fwd_from = None
        if flags & (1 << 2):
            fwd_from = reader.read_object()
        via_bot_id = None
        if flags & (1 << 11):
            via_bot_id = reader.read_int64()
        via_business_bot_id = None
        if flags & (1 << 0):
            via_business_bot_id = reader.read_int64()
        guestchat_via_from = None
        if flags & (1 << 19):
            guestchat_via_from = reader.read_object()
        reply_to = None
        if flags & (1 << 3):
            reply_to = reader.read_object()
        date = reader.read_int32()
        message = reader.read_string()
        media = None
        if flags & (1 << 9):
            media = reader.read_object()
        reply_markup = None
        if flags & (1 << 6):
            reply_markup = reader.read_object()
        entities = None
        if flags & (1 << 7):
            entities = reader.read_vector(lambda r: r.read_object())
        views = None
        if flags & (1 << 10):
            views = reader.read_int32()
        forwards = None
        if flags & (1 << 10):
            forwards = reader.read_int32()
        replies = None
        if flags & (1 << 23):
            replies = reader.read_object()
        edit_date = None
        if flags & (1 << 15):
            edit_date = reader.read_int32()
        post_author = None
        if flags & (1 << 16):
            post_author = reader.read_string()
        grouped_id = None
        if flags & (1 << 17):
            grouped_id = reader.read_int64()
        reactions = None
        if flags & (1 << 20):
            reactions = reader.read_object()
        restriction_reason = None
        if flags & (1 << 22):
            restriction_reason = reader.read_vector(lambda r: r.read_object())
        ttl_period = None
        if flags & (1 << 25):
            ttl_period = reader.read_int32()
        quick_reply_shortcut_id = None
        if flags & (1 << 30):
            quick_reply_shortcut_id = reader.read_int32()
        effect = None
        if flags & (1 << 2):
            effect = reader.read_int64()
        factcheck = None
        if flags & (1 << 3):
            factcheck = reader.read_object()
        report_delivery_until_date = None
        if flags & (1 << 5):
            report_delivery_until_date = reader.read_int32()
        paid_message_stars = None
        if flags & (1 << 6):
            paid_message_stars = reader.read_int64()
        suggested_post = None
        if flags & (1 << 7):
            suggested_post = reader.read_object()
        schedule_repeat_period = None
        if flags & (1 << 10):
            schedule_repeat_period = reader.read_int32()
        summary_from_language = None
        if flags & (1 << 11):
            summary_from_language = reader.read_string()
        return cls(out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, post=post, from_scheduled=from_scheduled, legacy=legacy, edit_hide=edit_hide, pinned=pinned, noforwards=noforwards, invert_media=invert_media, offline=offline, video_processing_pending=video_processing_pending, paid_suggested_post_stars=paid_suggested_post_stars, paid_suggested_post_ton=paid_suggested_post_ton, id=id, from_id=from_id, from_boosts_applied=from_boosts_applied, from_rank=from_rank, peer_id=peer_id, saved_peer_id=saved_peer_id, fwd_from=fwd_from, via_bot_id=via_bot_id, via_business_bot_id=via_business_bot_id, guestchat_via_from=guestchat_via_from, reply_to=reply_to, date=date, message=message, media=media, reply_markup=reply_markup, entities=entities, views=views, forwards=forwards, replies=replies, edit_date=edit_date, post_author=post_author, grouped_id=grouped_id, reactions=reactions, restriction_reason=restriction_reason, ttl_period=ttl_period, quick_reply_shortcut_id=quick_reply_shortcut_id, effect=effect, factcheck=factcheck, report_delivery_until_date=report_delivery_until_date, paid_message_stars=paid_message_stars, suggested_post=suggested_post, schedule_repeat_period=schedule_repeat_period, summary_from_language=summary_from_language)

@register_tl
class MessageService(TLObject):
    ID: int = 0x7a800e0a

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, reactions_are_possible: bool = False, silent: bool = False, post: bool = False, legacy: bool = False, id: Any = None, from_id: Any = None, peer_id: Any = None, saved_peer_id: Any = None, reply_to: Any = None, date: Any = None, action: Any = None, reactions: Any = None, ttl_period: Any = None) -> None:
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.reactions_are_possible = reactions_are_possible
        self.silent = silent
        self.post = post
        self.legacy = legacy
        self.id = id
        self.from_id = from_id
        self.peer_id = peer_id
        self.saved_peer_id = saved_peer_id
        self.reply_to = reply_to
        self.date = date
        self.action = action
        self.reactions = reactions
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.out:
            flags |= (1 << 1)
        if self.mentioned:
            flags |= (1 << 4)
        if self.media_unread:
            flags |= (1 << 5)
        if self.reactions_are_possible:
            flags |= (1 << 9)
        if self.silent:
            flags |= (1 << 13)
        if self.post:
            flags |= (1 << 14)
        if self.legacy:
            flags |= (1 << 19)
        if self.from_id is not None:
            flags |= (1 << 8)
        if self.saved_peer_id is not None:
            flags |= (1 << 28)
        if self.reply_to is not None:
            flags |= (1 << 3)
        if self.reactions is not None:
            flags |= (1 << 20)
        if self.ttl_period is not None:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.from_id is not None:
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if hasattr(self.peer_id, 'write'):
            self.peer_id.write(writer)
        else:
            writer.write_bytes(self.peer_id or b'')
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if self.reply_to is not None:
            if hasattr(self.reply_to, 'write'):
                self.reply_to.write(writer)
            else:
                writer.write_bytes(self.reply_to or b'')
        writer.write_int32(self.date or 0)
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')
        if self.reactions is not None:
            if hasattr(self.reactions, 'write'):
                self.reactions.write(writer)
            else:
                writer.write_bytes(self.reactions or b'')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageService':
        flags = reader.read_uint32()
        out = bool(flags & (1 << 1))
        mentioned = bool(flags & (1 << 4))
        media_unread = bool(flags & (1 << 5))
        reactions_are_possible = bool(flags & (1 << 9))
        silent = bool(flags & (1 << 13))
        post = bool(flags & (1 << 14))
        legacy = bool(flags & (1 << 19))
        id = reader.read_int32()
        from_id = None
        if flags & (1 << 8):
            from_id = reader.read_object()
        peer_id = reader.read_object()
        saved_peer_id = None
        if flags & (1 << 28):
            saved_peer_id = reader.read_object()
        reply_to = None
        if flags & (1 << 3):
            reply_to = reader.read_object()
        date = reader.read_int32()
        action = reader.read_object()
        reactions = None
        if flags & (1 << 20):
            reactions = reader.read_object()
        ttl_period = None
        if flags & (1 << 25):
            ttl_period = reader.read_int32()
        return cls(out=out, mentioned=mentioned, media_unread=media_unread, reactions_are_possible=reactions_are_possible, silent=silent, post=post, legacy=legacy, id=id, from_id=from_id, peer_id=peer_id, saved_peer_id=saved_peer_id, reply_to=reply_to, date=date, action=action, reactions=reactions, ttl_period=ttl_period)

@register_tl
class MessageMediaEmpty(TLObject):
    ID: int = 0x3ded6320

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaEmpty':
        return cls()

@register_tl
class MessageMediaPhoto(TLObject):
    ID: int = 0xe216eb63

    def __init__(self, spoiler: bool = False, live_photo: bool = False, photo: Any = None, ttl_seconds: Any = None, video: Any = None) -> None:
        self.spoiler = spoiler
        self.live_photo = live_photo
        self.photo = photo
        self.ttl_seconds = ttl_seconds
        self.video = video

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.spoiler:
            flags |= (1 << 3)
        if self.live_photo:
            flags |= (1 << 4)
        if self.photo is not None:
            flags |= (1 << 0)
        if self.ttl_seconds is not None:
            flags |= (1 << 2)
        if self.video is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.photo is not None:
            if hasattr(self.photo, 'write'):
                self.photo.write(writer)
            else:
                writer.write_bytes(self.photo or b'')
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)
        if self.video is not None:
            if hasattr(self.video, 'write'):
                self.video.write(writer)
            else:
                writer.write_bytes(self.video or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPhoto':
        flags = reader.read_uint32()
        spoiler = bool(flags & (1 << 3))
        live_photo = bool(flags & (1 << 4))
        photo = None
        if flags & (1 << 0):
            photo = reader.read_object()
        ttl_seconds = None
        if flags & (1 << 2):
            ttl_seconds = reader.read_int32()
        video = None
        if flags & (1 << 4):
            video = reader.read_object()
        return cls(spoiler=spoiler, live_photo=live_photo, photo=photo, ttl_seconds=ttl_seconds, video=video)

@register_tl
class MessageMediaGeo(TLObject):
    ID: int = 0x56e0d474

    def __init__(self, geo: Any = None) -> None:
        self.geo = geo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.geo, 'write'):
            self.geo.write(writer)
        else:
            writer.write_bytes(self.geo or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGeo':
        geo = reader.read_object()
        return cls(geo=geo)

@register_tl
class MessageMediaContact(TLObject):
    ID: int = 0x70322949

    def __init__(self, phone_number: Any = None, first_name: Any = None, last_name: Any = None, vcard: Any = None, user_id: Any = None) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.phone_number or ''))
        writer.write_string(str(self.first_name or ''))
        writer.write_string(str(self.last_name or ''))
        writer.write_string(str(self.vcard or ''))
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaContact':
        phone_number = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        vcard = reader.read_string()
        user_id = reader.read_int64()
        return cls(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard, user_id=user_id)

@register_tl
class MessageMediaUnsupported(TLObject):
    ID: int = 0x9f84f49e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaUnsupported':
        return cls()

@register_tl
class MessageMediaDocument(TLObject):
    ID: int = 0x52d8ccd9

    def __init__(self, nopremium: bool = False, spoiler: bool = False, video: bool = False, round: bool = False, voice: bool = False, document: Any = None, alt_documents: Any = None, video_cover: Any = None, video_timestamp: Any = None, ttl_seconds: Any = None) -> None:
        self.nopremium = nopremium
        self.spoiler = spoiler
        self.video = video
        self.round = round
        self.voice = voice
        self.document = document
        self.alt_documents = alt_documents
        self.video_cover = video_cover
        self.video_timestamp = video_timestamp
        self.ttl_seconds = ttl_seconds

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.nopremium:
            flags |= (1 << 3)
        if self.spoiler:
            flags |= (1 << 4)
        if self.video:
            flags |= (1 << 6)
        if self.round:
            flags |= (1 << 7)
        if self.voice:
            flags |= (1 << 8)
        if self.document is not None:
            flags |= (1 << 0)
        if self.alt_documents is not None:
            flags |= (1 << 5)
        if self.video_cover is not None:
            flags |= (1 << 9)
        if self.video_timestamp is not None:
            flags |= (1 << 10)
        if self.ttl_seconds is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.document is not None:
            if hasattr(self.document, 'write'):
                self.document.write(writer)
            else:
                writer.write_bytes(self.document or b'')
        if self.alt_documents is not None:
            writer.write_vector(self.alt_documents or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.video_cover is not None:
            if hasattr(self.video_cover, 'write'):
                self.video_cover.write(writer)
            else:
                writer.write_bytes(self.video_cover or b'')
        if self.video_timestamp is not None:
            writer.write_int32(self.video_timestamp or 0)
        if self.ttl_seconds is not None:
            writer.write_int32(self.ttl_seconds or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaDocument':
        flags = reader.read_uint32()
        nopremium = bool(flags & (1 << 3))
        spoiler = bool(flags & (1 << 4))
        video = bool(flags & (1 << 6))
        round = bool(flags & (1 << 7))
        voice = bool(flags & (1 << 8))
        document = None
        if flags & (1 << 0):
            document = reader.read_object()
        alt_documents = None
        if flags & (1 << 5):
            alt_documents = reader.read_vector(lambda r: r.read_object())
        video_cover = None
        if flags & (1 << 9):
            video_cover = reader.read_object()
        video_timestamp = None
        if flags & (1 << 10):
            video_timestamp = reader.read_int32()
        ttl_seconds = None
        if flags & (1 << 2):
            ttl_seconds = reader.read_int32()
        return cls(nopremium=nopremium, spoiler=spoiler, video=video, round=round, voice=voice, document=document, alt_documents=alt_documents, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds)

@register_tl
class MessageMediaWebPage(TLObject):
    ID: int = 0xddf10c3b

    def __init__(self, force_large_media: bool = False, force_small_media: bool = False, manual: bool = False, safe: bool = False, webpage: Any = None) -> None:
        self.force_large_media = force_large_media
        self.force_small_media = force_small_media
        self.manual = manual
        self.safe = safe
        self.webpage = webpage

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.force_large_media:
            flags |= (1 << 0)
        if self.force_small_media:
            flags |= (1 << 1)
        if self.manual:
            flags |= (1 << 3)
        if self.safe:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if hasattr(self.webpage, 'write'):
            self.webpage.write(writer)
        else:
            writer.write_bytes(self.webpage or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaWebPage':
        flags = reader.read_uint32()
        force_large_media = bool(flags & (1 << 0))
        force_small_media = bool(flags & (1 << 1))
        manual = bool(flags & (1 << 3))
        safe = bool(flags & (1 << 4))
        webpage = reader.read_object()
        return cls(force_large_media=force_large_media, force_small_media=force_small_media, manual=manual, safe=safe, webpage=webpage)

@register_tl
class MessageMediaVenue(TLObject):
    ID: int = 0x2ec0533f

    def __init__(self, geo: Any = None, title: Any = None, address: Any = None, provider: Any = None, venue_id: Any = None, venue_type: Any = None) -> None:
        self.geo = geo
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id
        self.venue_type = venue_type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.geo, 'write'):
            self.geo.write(writer)
        else:
            writer.write_bytes(self.geo or b'')
        writer.write_string(str(self.title or ''))
        writer.write_string(str(self.address or ''))
        writer.write_string(str(self.provider or ''))
        writer.write_string(str(self.venue_id or ''))
        writer.write_string(str(self.venue_type or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaVenue':
        geo = reader.read_object()
        title = reader.read_string()
        address = reader.read_string()
        provider = reader.read_string()
        venue_id = reader.read_string()
        venue_type = reader.read_string()
        return cls(geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)

@register_tl
class MessageMediaGame(TLObject):
    ID: int = 0xfdb19008

    def __init__(self, game: Any = None) -> None:
        self.game = game

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.game, 'write'):
            self.game.write(writer)
        else:
            writer.write_bytes(self.game or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGame':
        game = reader.read_object()
        return cls(game=game)

@register_tl
class MessageMediaInvoice(TLObject):
    ID: int = 0xf6a548d3

    def __init__(self, shipping_address_requested: bool = False, test: bool = False, title: Any = None, description: Any = None, photo: Any = None, receipt_msg_id: Any = None, currency: Any = None, total_amount: Any = None, start_param: Any = None, extended_media: Any = None) -> None:
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.title = title
        self.description = description
        self.photo = photo
        self.receipt_msg_id = receipt_msg_id
        self.currency = currency
        self.total_amount = total_amount
        self.start_param = start_param
        self.extended_media = extended_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.shipping_address_requested:
            flags |= (1 << 1)
        if self.test:
            flags |= (1 << 3)
        if self.photo is not None:
            flags |= (1 << 0)
        if self.receipt_msg_id is not None:
            flags |= (1 << 2)
        if self.extended_media is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(str(self.title or ''))
        writer.write_string(str(self.description or ''))
        if self.photo is not None:
            if hasattr(self.photo, 'write'):
                self.photo.write(writer)
            else:
                writer.write_bytes(self.photo or b'')
        if self.receipt_msg_id is not None:
            writer.write_int32(self.receipt_msg_id or 0)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        writer.write_string(str(self.start_param or ''))
        if self.extended_media is not None:
            if hasattr(self.extended_media, 'write'):
                self.extended_media.write(writer)
            else:
                writer.write_bytes(self.extended_media or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaInvoice':
        flags = reader.read_uint32()
        shipping_address_requested = bool(flags & (1 << 1))
        test = bool(flags & (1 << 3))
        title = reader.read_string()
        description = reader.read_string()
        photo = None
        if flags & (1 << 0):
            photo = reader.read_object()
        receipt_msg_id = None
        if flags & (1 << 2):
            receipt_msg_id = reader.read_int32()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        start_param = reader.read_string()
        extended_media = None
        if flags & (1 << 4):
            extended_media = reader.read_object()
        return cls(shipping_address_requested=shipping_address_requested, test=test, title=title, description=description, photo=photo, receipt_msg_id=receipt_msg_id, currency=currency, total_amount=total_amount, start_param=start_param, extended_media=extended_media)

@register_tl
class MessageMediaGeoLive(TLObject):
    ID: int = 0xb940c666

    def __init__(self, geo: Any = None, heading: Any = None, period: Any = None, proximity_notification_radius: Any = None) -> None:
        self.geo = geo
        self.heading = heading
        self.period = period
        self.proximity_notification_radius = proximity_notification_radius

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.heading is not None:
            flags |= (1 << 0)
        if self.proximity_notification_radius is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.geo, 'write'):
            self.geo.write(writer)
        else:
            writer.write_bytes(self.geo or b'')
        if self.heading is not None:
            writer.write_int32(self.heading or 0)
        writer.write_int32(self.period or 0)
        if self.proximity_notification_radius is not None:
            writer.write_int32(self.proximity_notification_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGeoLive':
        flags = reader.read_uint32()
        geo = reader.read_object()
        heading = None
        if flags & (1 << 0):
            heading = reader.read_int32()
        period = reader.read_int32()
        proximity_notification_radius = None
        if flags & (1 << 1):
            proximity_notification_radius = reader.read_int32()
        return cls(geo=geo, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius)

@register_tl
class MessageMediaPoll(TLObject):
    ID: int = 0x773f4e66

    def __init__(self, poll: Any = None, results: Any = None, attached_media: Any = None) -> None:
        self.poll = poll
        self.results = results
        self.attached_media = attached_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attached_media is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.poll, 'write'):
            self.poll.write(writer)
        else:
            writer.write_bytes(self.poll or b'')
        if hasattr(self.results, 'write'):
            self.results.write(writer)
        else:
            writer.write_bytes(self.results or b'')
        if self.attached_media is not None:
            if hasattr(self.attached_media, 'write'):
                self.attached_media.write(writer)
            else:
                writer.write_bytes(self.attached_media or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPoll':
        flags = reader.read_uint32()
        poll = reader.read_object()
        results = reader.read_object()
        attached_media = None
        if flags & (1 << 0):
            attached_media = reader.read_object()
        return cls(poll=poll, results=results, attached_media=attached_media)

@register_tl
class MessageMediaDice(TLObject):
    ID: int = 0x8cbec07

    def __init__(self, value: Any = None, emoticon: Any = None, game_outcome: Any = None) -> None:
        self.value = value
        self.emoticon = emoticon
        self.game_outcome = game_outcome

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.game_outcome is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.value or 0)
        writer.write_string(str(self.emoticon or ''))
        if self.game_outcome is not None:
            if hasattr(self.game_outcome, 'write'):
                self.game_outcome.write(writer)
            else:
                writer.write_bytes(self.game_outcome or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaDice':
        flags = reader.read_uint32()
        value = reader.read_int32()
        emoticon = reader.read_string()
        game_outcome = None
        if flags & (1 << 0):
            game_outcome = reader.read_object()
        return cls(value=value, emoticon=emoticon, game_outcome=game_outcome)

@register_tl
class MessageMediaStory(TLObject):
    ID: int = 0x68cb6283

    def __init__(self, via_mention: bool = False, peer: Any = None, id: Any = None, story: Any = None) -> None:
        self.via_mention = via_mention
        self.peer = peer
        self.id = id
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_mention:
            flags |= (1 << 1)
        if self.story is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.id or 0)
        if self.story is not None:
            if hasattr(self.story, 'write'):
                self.story.write(writer)
            else:
                writer.write_bytes(self.story or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaStory':
        flags = reader.read_uint32()
        via_mention = bool(flags & (1 << 1))
        peer = reader.read_object()
        id = reader.read_int32()
        story = None
        if flags & (1 << 0):
            story = reader.read_object()
        return cls(via_mention=via_mention, peer=peer, id=id, story=story)

@register_tl
class MessageMediaGiveaway(TLObject):
    ID: int = 0xaa073beb

    def __init__(self, only_new_subscribers: bool = False, winners_are_visible: bool = False, channels: Any = None, countries_iso2: Any = None, prize_description: Any = None, quantity: Any = None, months: Any = None, stars: Any = None, until_date: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.winners_are_visible = winners_are_visible
        self.channels = channels
        self.countries_iso2 = countries_iso2
        self.prize_description = prize_description
        self.quantity = quantity
        self.months = months
        self.stars = stars
        self.until_date = until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.only_new_subscribers:
            flags |= (1 << 0)
        if self.winners_are_visible:
            flags |= (1 << 2)
        if self.countries_iso2 is not None:
            flags |= (1 << 1)
        if self.prize_description is not None:
            flags |= (1 << 3)
        if self.months is not None:
            flags |= (1 << 4)
        if self.stars is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_vector(self.channels or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.countries_iso2 is not None:
            writer.write_vector(self.countries_iso2 or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.prize_description is not None:
            writer.write_string(str(self.prize_description or ''))
        writer.write_int32(self.quantity or 0)
        if self.months is not None:
            writer.write_int32(self.months or 0)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)
        writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGiveaway':
        flags = reader.read_uint32()
        only_new_subscribers = bool(flags & (1 << 0))
        winners_are_visible = bool(flags & (1 << 2))
        channels = reader.read_vector(lambda r: r.read_object())
        countries_iso2 = None
        if flags & (1 << 1):
            countries_iso2 = reader.read_vector(lambda r: r.read_object())
        prize_description = None
        if flags & (1 << 3):
            prize_description = reader.read_string()
        quantity = reader.read_int32()
        months = None
        if flags & (1 << 4):
            months = reader.read_int32()
        stars = None
        if flags & (1 << 5):
            stars = reader.read_int64()
        until_date = reader.read_int32()
        return cls(only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, channels=channels, countries_iso2=countries_iso2, prize_description=prize_description, quantity=quantity, months=months, stars=stars, until_date=until_date)

@register_tl
class MessageMediaGiveawayResults(TLObject):
    ID: int = 0xceaa3ea1

    def __init__(self, only_new_subscribers: bool = False, refunded: bool = False, channel_id: Any = None, additional_peers_count: Any = None, launch_msg_id: Any = None, winners_count: Any = None, unclaimed_count: Any = None, winners: Any = None, months: Any = None, stars: Any = None, prize_description: Any = None, until_date: Any = None) -> None:
        self.only_new_subscribers = only_new_subscribers
        self.refunded = refunded
        self.channel_id = channel_id
        self.additional_peers_count = additional_peers_count
        self.launch_msg_id = launch_msg_id
        self.winners_count = winners_count
        self.unclaimed_count = unclaimed_count
        self.winners = winners
        self.months = months
        self.stars = stars
        self.prize_description = prize_description
        self.until_date = until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.only_new_subscribers:
            flags |= (1 << 0)
        if self.refunded:
            flags |= (1 << 2)
        if self.additional_peers_count is not None:
            flags |= (1 << 3)
        if self.months is not None:
            flags |= (1 << 4)
        if self.stars is not None:
            flags |= (1 << 5)
        if self.prize_description is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.additional_peers_count is not None:
            writer.write_int32(self.additional_peers_count or 0)
        writer.write_int32(self.launch_msg_id or 0)
        writer.write_int32(self.winners_count or 0)
        writer.write_int32(self.unclaimed_count or 0)
        writer.write_vector(self.winners or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.months is not None:
            writer.write_int32(self.months or 0)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)
        if self.prize_description is not None:
            writer.write_string(str(self.prize_description or ''))
        writer.write_int32(self.until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaGiveawayResults':
        flags = reader.read_uint32()
        only_new_subscribers = bool(flags & (1 << 0))
        refunded = bool(flags & (1 << 2))
        channel_id = reader.read_int64()
        additional_peers_count = None
        if flags & (1 << 3):
            additional_peers_count = reader.read_int32()
        launch_msg_id = reader.read_int32()
        winners_count = reader.read_int32()
        unclaimed_count = reader.read_int32()
        winners = reader.read_vector(lambda r: r.read_object())
        months = None
        if flags & (1 << 4):
            months = reader.read_int32()
        stars = None
        if flags & (1 << 5):
            stars = reader.read_int64()
        prize_description = None
        if flags & (1 << 1):
            prize_description = reader.read_string()
        until_date = reader.read_int32()
        return cls(only_new_subscribers=only_new_subscribers, refunded=refunded, channel_id=channel_id, additional_peers_count=additional_peers_count, launch_msg_id=launch_msg_id, winners_count=winners_count, unclaimed_count=unclaimed_count, winners=winners, months=months, stars=stars, prize_description=prize_description, until_date=until_date)

@register_tl
class MessageMediaPaidMedia(TLObject):
    ID: int = 0xa8852491

    def __init__(self, stars_amount: Any = None, extended_media: Any = None) -> None:
        self.stars_amount = stars_amount
        self.extended_media = extended_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.stars_amount or 0)
        writer.write_vector(self.extended_media or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaPaidMedia':
        stars_amount = reader.read_int64()
        extended_media = reader.read_vector(lambda r: r.read_object())
        return cls(stars_amount=stars_amount, extended_media=extended_media)

@register_tl
class MessageMediaToDo(TLObject):
    ID: int = 0x8a53b014

    def __init__(self, todo: Any = None, completions: Any = None) -> None:
        self.todo = todo
        self.completions = completions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.completions is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.todo, 'write'):
            self.todo.write(writer)
        else:
            writer.write_bytes(self.todo or b'')
        if self.completions is not None:
            writer.write_vector(self.completions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaToDo':
        flags = reader.read_uint32()
        todo = reader.read_object()
        completions = None
        if flags & (1 << 0):
            completions = reader.read_vector(lambda r: r.read_object())
        return cls(todo=todo, completions=completions)

@register_tl
class MessageMediaVideoStream(TLObject):
    ID: int = 0xca5cab89

    def __init__(self, rtmp_stream: bool = False, call: Any = None) -> None:
        self.rtmp_stream = rtmp_stream
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rtmp_stream:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageMediaVideoStream':
        flags = reader.read_uint32()
        rtmp_stream = bool(flags & (1 << 0))
        call = reader.read_object()
        return cls(rtmp_stream=rtmp_stream, call=call)

@register_tl
class MessageActionEmpty(TLObject):
    ID: int = 0xb6aef7b0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionEmpty':
        return cls()

@register_tl
class MessageActionChatCreate(TLObject):
    ID: int = 0xbd47cbad

    def __init__(self, title: Any = None, users: Any = None) -> None:
        self.title = title
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.title or ''))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatCreate':
        title = reader.read_string()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(title=title, users=users)

@register_tl
class MessageActionChatEditTitle(TLObject):
    ID: int = 0xb5a1ce5a

    def __init__(self, title: Any = None) -> None:
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.title or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatEditTitle':
        title = reader.read_string()
        return cls(title=title)

@register_tl
class MessageActionChatEditPhoto(TLObject):
    ID: int = 0x7fcb13a8

    def __init__(self, photo: Any = None) -> None:
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.photo, 'write'):
            self.photo.write(writer)
        else:
            writer.write_bytes(self.photo or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatEditPhoto':
        photo = reader.read_object()
        return cls(photo=photo)

@register_tl
class MessageActionChatDeletePhoto(TLObject):
    ID: int = 0x95e3fbef

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatDeletePhoto':
        return cls()

@register_tl
class MessageActionChatAddUser(TLObject):
    ID: int = 0x15cefd00

    def __init__(self, users: Any = None) -> None:
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatAddUser':
        users = reader.read_vector(lambda r: r.read_object())
        return cls(users=users)

@register_tl
class MessageActionChatDeleteUser(TLObject):
    ID: int = 0xa43f30cc

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatDeleteUser':
        user_id = reader.read_int64()
        return cls(user_id=user_id)

@register_tl
class MessageActionChatJoinedByLink(TLObject):
    ID: int = 0x31224c3

    def __init__(self, inviter_id: Any = None) -> None:
        self.inviter_id = inviter_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.inviter_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatJoinedByLink':
        inviter_id = reader.read_int64()
        return cls(inviter_id=inviter_id)

@register_tl
class MessageActionChannelCreate(TLObject):
    ID: int = 0x95d2ac92

    def __init__(self, title: Any = None) -> None:
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.title or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChannelCreate':
        title = reader.read_string()
        return cls(title=title)

@register_tl
class MessageActionChatMigrateTo(TLObject):
    ID: int = 0xe1037f92

    def __init__(self, channel_id: Any = None) -> None:
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatMigrateTo':
        channel_id = reader.read_int64()
        return cls(channel_id=channel_id)

@register_tl
class MessageActionChannelMigrateFrom(TLObject):
    ID: int = 0xea3948e9

    def __init__(self, title: Any = None, chat_id: Any = None) -> None:
        self.title = title
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.title or ''))
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChannelMigrateFrom':
        title = reader.read_string()
        chat_id = reader.read_int64()
        return cls(title=title, chat_id=chat_id)

@register_tl
class MessageActionPinMessage(TLObject):
    ID: int = 0x94bd38ed

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPinMessage':
        return cls()

@register_tl
class MessageActionHistoryClear(TLObject):
    ID: int = 0x9fbab604

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionHistoryClear':
        return cls()

@register_tl
class MessageActionGameScore(TLObject):
    ID: int = 0x92a72876

    def __init__(self, game_id: Any = None, score: Any = None) -> None:
        self.game_id = game_id
        self.score = score

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.game_id or 0)
        writer.write_int32(self.score or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGameScore':
        game_id = reader.read_int64()
        score = reader.read_int32()
        return cls(game_id=game_id, score=score)

@register_tl
class MessageActionPaymentSentMe(TLObject):
    ID: int = 0xffa00ccc

    def __init__(self, recurring_init: bool = False, recurring_used: bool = False, currency: Any = None, total_amount: Any = None, payload: Any = None, info: Any = None, shipping_option_id: Any = None, charge: Any = None, subscription_until_date: Any = None) -> None:
        self.recurring_init = recurring_init
        self.recurring_used = recurring_used
        self.currency = currency
        self.total_amount = total_amount
        self.payload = payload
        self.info = info
        self.shipping_option_id = shipping_option_id
        self.charge = charge
        self.subscription_until_date = subscription_until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.recurring_init:
            flags |= (1 << 2)
        if self.recurring_used:
            flags |= (1 << 3)
        if self.info is not None:
            flags |= (1 << 0)
        if self.shipping_option_id is not None:
            flags |= (1 << 1)
        if self.subscription_until_date is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        writer.write_bytes(self.payload or b'')
        if self.info is not None:
            if hasattr(self.info, 'write'):
                self.info.write(writer)
            else:
                writer.write_bytes(self.info or b'')
        if self.shipping_option_id is not None:
            writer.write_string(str(self.shipping_option_id or ''))
        if hasattr(self.charge, 'write'):
            self.charge.write(writer)
        else:
            writer.write_bytes(self.charge or b'')
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentSentMe':
        flags = reader.read_uint32()
        recurring_init = bool(flags & (1 << 2))
        recurring_used = bool(flags & (1 << 3))
        currency = reader.read_string()
        total_amount = reader.read_int64()
        payload = reader.read_bytes()
        info = None
        if flags & (1 << 0):
            info = reader.read_object()
        shipping_option_id = None
        if flags & (1 << 1):
            shipping_option_id = reader.read_string()
        charge = reader.read_object()
        subscription_until_date = None
        if flags & (1 << 4):
            subscription_until_date = reader.read_int32()
        return cls(recurring_init=recurring_init, recurring_used=recurring_used, currency=currency, total_amount=total_amount, payload=payload, info=info, shipping_option_id=shipping_option_id, charge=charge, subscription_until_date=subscription_until_date)

@register_tl
class MessageActionPaymentSent(TLObject):
    ID: int = 0xc624b16e

    def __init__(self, recurring_init: bool = False, recurring_used: bool = False, currency: Any = None, total_amount: Any = None, invoice_slug: Any = None, subscription_until_date: Any = None) -> None:
        self.recurring_init = recurring_init
        self.recurring_used = recurring_used
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_slug = invoice_slug
        self.subscription_until_date = subscription_until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.recurring_init:
            flags |= (1 << 2)
        if self.recurring_used:
            flags |= (1 << 3)
        if self.invoice_slug is not None:
            flags |= (1 << 0)
        if self.subscription_until_date is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        if self.invoice_slug is not None:
            writer.write_string(str(self.invoice_slug or ''))
        if self.subscription_until_date is not None:
            writer.write_int32(self.subscription_until_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentSent':
        flags = reader.read_uint32()
        recurring_init = bool(flags & (1 << 2))
        recurring_used = bool(flags & (1 << 3))
        currency = reader.read_string()
        total_amount = reader.read_int64()
        invoice_slug = None
        if flags & (1 << 0):
            invoice_slug = reader.read_string()
        subscription_until_date = None
        if flags & (1 << 4):
            subscription_until_date = reader.read_int32()
        return cls(recurring_init=recurring_init, recurring_used=recurring_used, currency=currency, total_amount=total_amount, invoice_slug=invoice_slug, subscription_until_date=subscription_until_date)

@register_tl
class MessageActionPhoneCall(TLObject):
    ID: int = 0x80e11a7f

    def __init__(self, video: bool = False, call_id: Any = None, reason: Any = None, duration: Any = None) -> None:
        self.video = video
        self.call_id = call_id
        self.reason = reason
        self.duration = duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 2)
        if self.reason is not None:
            flags |= (1 << 0)
        if self.duration is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.call_id or 0)
        if self.reason is not None:
            if hasattr(self.reason, 'write'):
                self.reason.write(writer)
            else:
                writer.write_bytes(self.reason or b'')
        if self.duration is not None:
            writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPhoneCall':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 2))
        call_id = reader.read_int64()
        reason = None
        if flags & (1 << 0):
            reason = reader.read_object()
        duration = None
        if flags & (1 << 1):
            duration = reader.read_int32()
        return cls(video=video, call_id=call_id, reason=reason, duration=duration)

@register_tl
class MessageActionScreenshotTaken(TLObject):
    ID: int = 0x4792929b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionScreenshotTaken':
        return cls()

@register_tl
class MessageActionCustomAction(TLObject):
    ID: int = 0xfae69f56

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.message or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionCustomAction':
        message = reader.read_string()
        return cls(message=message)

@register_tl
class MessageActionBotAllowed(TLObject):
    ID: int = 0xc516d679

    def __init__(self, attach_menu: bool = False, from_request: bool = False, domain: Any = None, app: Any = None) -> None:
        self.attach_menu = attach_menu
        self.from_request = from_request
        self.domain = domain
        self.app = app

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.attach_menu:
            flags |= (1 << 1)
        if self.from_request:
            flags |= (1 << 3)
        if self.domain is not None:
            flags |= (1 << 0)
        if self.app is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.domain is not None:
            writer.write_string(str(self.domain or ''))
        if self.app is not None:
            if hasattr(self.app, 'write'):
                self.app.write(writer)
            else:
                writer.write_bytes(self.app or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionBotAllowed':
        flags = reader.read_uint32()
        attach_menu = bool(flags & (1 << 1))
        from_request = bool(flags & (1 << 3))
        domain = None
        if flags & (1 << 0):
            domain = reader.read_string()
        app = None
        if flags & (1 << 2):
            app = reader.read_object()
        return cls(attach_menu=attach_menu, from_request=from_request, domain=domain, app=app)

@register_tl
class MessageActionSecureValuesSentMe(TLObject):
    ID: int = 0x1b287353

    def __init__(self, values: Any = None, credentials: Any = None) -> None:
        self.values = values
        self.credentials = credentials

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.values or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if hasattr(self.credentials, 'write'):
            self.credentials.write(writer)
        else:
            writer.write_bytes(self.credentials or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSecureValuesSentMe':
        values = reader.read_vector(lambda r: r.read_object())
        credentials = reader.read_object()
        return cls(values=values, credentials=credentials)

@register_tl
class MessageActionSecureValuesSent(TLObject):
    ID: int = 0xd95c6154

    def __init__(self, types: Any = None) -> None:
        self.types = types

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.types or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSecureValuesSent':
        types = reader.read_vector(lambda r: r.read_object())
        return cls(types=types)

@register_tl
class MessageActionContactSignUp(TLObject):
    ID: int = 0xf3f25f76

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionContactSignUp':
        return cls()

@register_tl
class MessageActionGeoProximityReached(TLObject):
    ID: int = 0x98e0d697

    def __init__(self, from_id: Any = None, to_id: Any = None, distance: Any = None) -> None:
        self.from_id = from_id
        self.to_id = to_id
        self.distance = distance

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.from_id, 'write'):
            self.from_id.write(writer)
        else:
            writer.write_bytes(self.from_id or b'')
        if hasattr(self.to_id, 'write'):
            self.to_id.write(writer)
        else:
            writer.write_bytes(self.to_id or b'')
        writer.write_int32(self.distance or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGeoProximityReached':
        from_id = reader.read_object()
        to_id = reader.read_object()
        distance = reader.read_int32()
        return cls(from_id=from_id, to_id=to_id, distance=distance)

@register_tl
class MessageActionGroupCall(TLObject):
    ID: int = 0x7a0d7f42

    def __init__(self, call: Any = None, duration: Any = None) -> None:
        self.call = call
        self.duration = duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.duration is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        if self.duration is not None:
            writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGroupCall':
        flags = reader.read_uint32()
        call = reader.read_object()
        duration = None
        if flags & (1 << 0):
            duration = reader.read_int32()
        return cls(call=call, duration=duration)

@register_tl
class MessageActionInviteToGroupCall(TLObject):
    ID: int = 0x502f92f7

    def __init__(self, call: Any = None, users: Any = None) -> None:
        self.call = call
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionInviteToGroupCall':
        call = reader.read_object()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(call=call, users=users)

@register_tl
class MessageActionSetMessagesTTL(TLObject):
    ID: int = 0x3c134d7b

    def __init__(self, period: Any = None, auto_setting_from: Any = None) -> None:
        self.period = period
        self.auto_setting_from = auto_setting_from

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.auto_setting_from is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.period or 0)
        if self.auto_setting_from is not None:
            writer.write_int64(self.auto_setting_from or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSetMessagesTTL':
        flags = reader.read_uint32()
        period = reader.read_int32()
        auto_setting_from = None
        if flags & (1 << 0):
            auto_setting_from = reader.read_int64()
        return cls(period=period, auto_setting_from=auto_setting_from)

@register_tl
class MessageActionGroupCallScheduled(TLObject):
    ID: int = 0xb3a07661

    def __init__(self, call: Any = None, schedule_date: Any = None) -> None:
        self.call = call
        self.schedule_date = schedule_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        writer.write_int32(self.schedule_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGroupCallScheduled':
        call = reader.read_object()
        schedule_date = reader.read_int32()
        return cls(call=call, schedule_date=schedule_date)

@register_tl
class MessageActionSetChatTheme(TLObject):
    ID: int = 0xb91bbd3a

    def __init__(self, theme: Any = None) -> None:
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.theme, 'write'):
            self.theme.write(writer)
        else:
            writer.write_bytes(self.theme or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSetChatTheme':
        theme = reader.read_object()
        return cls(theme=theme)

@register_tl
class MessageActionChatJoinedByRequest(TLObject):
    ID: int = 0xebbca3cb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChatJoinedByRequest':
        return cls()

@register_tl
class MessageActionWebViewDataSentMe(TLObject):
    ID: int = 0x47dd8079

    def __init__(self, text: Any = None, data: Any = None) -> None:
        self.text = text
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.text or ''))
        writer.write_string(str(self.data or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionWebViewDataSentMe':
        text = reader.read_string()
        data = reader.read_string()
        return cls(text=text, data=data)

@register_tl
class MessageActionWebViewDataSent(TLObject):
    ID: int = 0xb4c38cb5

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.text or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionWebViewDataSent':
        text = reader.read_string()
        return cls(text=text)

@register_tl
class MessageActionGiftPremium(TLObject):
    ID: int = 0x48e91302

    def __init__(self, currency: Any = None, amount: Any = None, days: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, message: Any = None) -> None:
        self.currency = currency
        self.amount = amount
        self.days = days
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.crypto_currency is not None:
            flags |= (1 << 0)
        if self.crypto_amount is not None:
            flags |= (1 << 0)
        if self.message is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)
        writer.write_int32(self.days or 0)
        if self.crypto_currency is not None:
            writer.write_string(str(self.crypto_currency or ''))
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.message is not None:
            if hasattr(self.message, 'write'):
                self.message.write(writer)
            else:
                writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftPremium':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        days = reader.read_int32()
        crypto_currency = None
        if flags & (1 << 0):
            crypto_currency = reader.read_string()
        crypto_amount = None
        if flags & (1 << 0):
            crypto_amount = reader.read_int64()
        message = None
        if flags & (1 << 1):
            message = reader.read_object()
        return cls(currency=currency, amount=amount, days=days, crypto_currency=crypto_currency, crypto_amount=crypto_amount, message=message)

@register_tl
class MessageActionTopicCreate(TLObject):
    ID: int = 0xd999256

    def __init__(self, title_missing: bool = False, title: Any = None, icon_color: Any = None, icon_emoji_id: Any = None) -> None:
        self.title_missing = title_missing
        self.title = title
        self.icon_color = icon_color
        self.icon_emoji_id = icon_emoji_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title_missing:
            flags |= (1 << 1)
        if self.icon_emoji_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.title or ''))
        writer.write_int32(self.icon_color or 0)
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTopicCreate':
        flags = reader.read_uint32()
        title_missing = bool(flags & (1 << 1))
        title = reader.read_string()
        icon_color = reader.read_int32()
        icon_emoji_id = None
        if flags & (1 << 0):
            icon_emoji_id = reader.read_int64()
        return cls(title_missing=title_missing, title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id)

@register_tl
class MessageActionTopicEdit(TLObject):
    ID: int = 0xc0944820

    def __init__(self, title: Any = None, icon_emoji_id: Any = None, closed: Any = None, hidden: Any = None) -> None:
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
        if self.title is not None:
            writer.write_string(str(self.title or ''))
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)
        if self.closed is not None:
            writer.write_bool(bool(self.closed))
        if self.hidden is not None:
            writer.write_bool(bool(self.hidden))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTopicEdit':
        flags = reader.read_uint32()
        title = None
        if flags & (1 << 0):
            title = reader.read_string()
        icon_emoji_id = None
        if flags & (1 << 1):
            icon_emoji_id = reader.read_int64()
        closed = None
        if flags & (1 << 2):
            closed = reader.read_bool()
        hidden = None
        if flags & (1 << 3):
            hidden = reader.read_bool()
        return cls(title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)

@register_tl
class MessageActionSuggestProfilePhoto(TLObject):
    ID: int = 0x57de635e

    def __init__(self, photo: Any = None) -> None:
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.photo, 'write'):
            self.photo.write(writer)
        else:
            writer.write_bytes(self.photo or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestProfilePhoto':
        photo = reader.read_object()
        return cls(photo=photo)

@register_tl
class MessageActionRequestedPeer(TLObject):
    ID: int = 0x31518e9b

    def __init__(self, button_id: Any = None, peers: Any = None) -> None:
        self.button_id = button_id
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.button_id or 0)
        writer.write_vector(self.peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionRequestedPeer':
        button_id = reader.read_int32()
        peers = reader.read_vector(lambda r: r.read_object())
        return cls(button_id=button_id, peers=peers)

@register_tl
class MessageActionSetChatWallPaper(TLObject):
    ID: int = 0x5060a3f4

    def __init__(self, same: bool = False, for_both: bool = False, wallpaper: Any = None) -> None:
        self.same = same
        self.for_both = for_both
        self.wallpaper = wallpaper

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.same:
            flags |= (1 << 0)
        if self.for_both:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.wallpaper, 'write'):
            self.wallpaper.write(writer)
        else:
            writer.write_bytes(self.wallpaper or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSetChatWallPaper':
        flags = reader.read_uint32()
        same = bool(flags & (1 << 0))
        for_both = bool(flags & (1 << 1))
        wallpaper = reader.read_object()
        return cls(same=same, for_both=for_both, wallpaper=wallpaper)

@register_tl
class MessageActionGiftCode(TLObject):
    ID: int = 0x31c48347

    def __init__(self, via_giveaway: bool = False, unclaimed: bool = False, boost_peer: Any = None, days: Any = None, slug: Any = None, currency: Any = None, amount: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, message: Any = None) -> None:
        self.via_giveaway = via_giveaway
        self.unclaimed = unclaimed
        self.boost_peer = boost_peer
        self.days = days
        self.slug = slug
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_giveaway:
            flags |= (1 << 0)
        if self.unclaimed:
            flags |= (1 << 5)
        if self.boost_peer is not None:
            flags |= (1 << 1)
        if self.currency is not None:
            flags |= (1 << 2)
        if self.amount is not None:
            flags |= (1 << 2)
        if self.crypto_currency is not None:
            flags |= (1 << 3)
        if self.crypto_amount is not None:
            flags |= (1 << 3)
        if self.message is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.boost_peer is not None:
            if hasattr(self.boost_peer, 'write'):
                self.boost_peer.write(writer)
            else:
                writer.write_bytes(self.boost_peer or b'')
        writer.write_int32(self.days or 0)
        writer.write_string(str(self.slug or ''))
        if self.currency is not None:
            writer.write_string(str(self.currency or ''))
        if self.amount is not None:
            writer.write_int64(self.amount or 0)
        if self.crypto_currency is not None:
            writer.write_string(str(self.crypto_currency or ''))
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.message is not None:
            if hasattr(self.message, 'write'):
                self.message.write(writer)
            else:
                writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftCode':
        flags = reader.read_uint32()
        via_giveaway = bool(flags & (1 << 0))
        unclaimed = bool(flags & (1 << 5))
        boost_peer = None
        if flags & (1 << 1):
            boost_peer = reader.read_object()
        days = reader.read_int32()
        slug = reader.read_string()
        currency = None
        if flags & (1 << 2):
            currency = reader.read_string()
        amount = None
        if flags & (1 << 2):
            amount = reader.read_int64()
        crypto_currency = None
        if flags & (1 << 3):
            crypto_currency = reader.read_string()
        crypto_amount = None
        if flags & (1 << 3):
            crypto_amount = reader.read_int64()
        message = None
        if flags & (1 << 4):
            message = reader.read_object()
        return cls(via_giveaway=via_giveaway, unclaimed=unclaimed, boost_peer=boost_peer, days=days, slug=slug, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, message=message)

@register_tl
class MessageActionGiveawayLaunch(TLObject):
    ID: int = 0xa80f51e4

    def __init__(self, stars: Any = None) -> None:
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.stars is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.stars is not None:
            writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiveawayLaunch':
        flags = reader.read_uint32()
        stars = None
        if flags & (1 << 0):
            stars = reader.read_int64()
        return cls(stars=stars)

@register_tl
class MessageActionGiveawayResults(TLObject):
    ID: int = 0x87e2f155

    def __init__(self, stars: bool = False, winners_count: Any = None, unclaimed_count: Any = None) -> None:
        self.stars = stars
        self.winners_count = winners_count
        self.unclaimed_count = unclaimed_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.stars:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.winners_count or 0)
        writer.write_int32(self.unclaimed_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiveawayResults':
        flags = reader.read_uint32()
        stars = bool(flags & (1 << 0))
        winners_count = reader.read_int32()
        unclaimed_count = reader.read_int32()
        return cls(stars=stars, winners_count=winners_count, unclaimed_count=unclaimed_count)

@register_tl
class MessageActionBoostApply(TLObject):
    ID: int = 0xcc02aa6d

    def __init__(self, boosts: Any = None) -> None:
        self.boosts = boosts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.boosts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionBoostApply':
        boosts = reader.read_int32()
        return cls(boosts=boosts)

@register_tl
class MessageActionRequestedPeerSentMe(TLObject):
    ID: int = 0x93b31848

    def __init__(self, button_id: Any = None, peers: Any = None) -> None:
        self.button_id = button_id
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.button_id or 0)
        writer.write_vector(self.peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionRequestedPeerSentMe':
        button_id = reader.read_int32()
        peers = reader.read_vector(lambda r: r.read_object())
        return cls(button_id=button_id, peers=peers)

@register_tl
class MessageActionPaymentRefunded(TLObject):
    ID: int = 0x41b3e202

    def __init__(self, peer: Any = None, currency: Any = None, total_amount: Any = None, payload: Any = None, charge: Any = None) -> None:
        self.peer = peer
        self.currency = currency
        self.total_amount = total_amount
        self.payload = payload
        self.charge = charge

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.payload is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)
        if self.payload is not None:
            writer.write_bytes(self.payload or b'')
        if hasattr(self.charge, 'write'):
            self.charge.write(writer)
        else:
            writer.write_bytes(self.charge or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaymentRefunded':
        flags = reader.read_uint32()
        peer = reader.read_object()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        payload = None
        if flags & (1 << 0):
            payload = reader.read_bytes()
        charge = reader.read_object()
        return cls(peer=peer, currency=currency, total_amount=total_amount, payload=payload, charge=charge)

@register_tl
class MessageActionGiftStars(TLObject):
    ID: int = 0x45d5b021

    def __init__(self, currency: Any = None, amount: Any = None, stars: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, transaction_id: Any = None) -> None:
        self.currency = currency
        self.amount = amount
        self.stars = stars
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.transaction_id = transaction_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.crypto_currency is not None:
            flags |= (1 << 0)
        if self.crypto_amount is not None:
            flags |= (1 << 0)
        if self.transaction_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)
        writer.write_int64(self.stars or 0)
        if self.crypto_currency is not None:
            writer.write_string(str(self.crypto_currency or ''))
        if self.crypto_amount is not None:
            writer.write_int64(self.crypto_amount or 0)
        if self.transaction_id is not None:
            writer.write_string(str(self.transaction_id or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftStars':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        stars = reader.read_int64()
        crypto_currency = None
        if flags & (1 << 0):
            crypto_currency = reader.read_string()
        crypto_amount = None
        if flags & (1 << 0):
            crypto_amount = reader.read_int64()
        transaction_id = None
        if flags & (1 << 1):
            transaction_id = reader.read_string()
        return cls(currency=currency, amount=amount, stars=stars, crypto_currency=crypto_currency, crypto_amount=crypto_amount, transaction_id=transaction_id)

@register_tl
class MessageActionPrizeStars(TLObject):
    ID: int = 0xb00c47a2

    def __init__(self, unclaimed: bool = False, stars: Any = None, transaction_id: Any = None, boost_peer: Any = None, giveaway_msg_id: Any = None) -> None:
        self.unclaimed = unclaimed
        self.stars = stars
        self.transaction_id = transaction_id
        self.boost_peer = boost_peer
        self.giveaway_msg_id = giveaway_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unclaimed:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)
        writer.write_string(str(self.transaction_id or ''))
        if hasattr(self.boost_peer, 'write'):
            self.boost_peer.write(writer)
        else:
            writer.write_bytes(self.boost_peer or b'')
        writer.write_int32(self.giveaway_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPrizeStars':
        flags = reader.read_uint32()
        unclaimed = bool(flags & (1 << 0))
        stars = reader.read_int64()
        transaction_id = reader.read_string()
        boost_peer = reader.read_object()
        giveaway_msg_id = reader.read_int32()
        return cls(unclaimed=unclaimed, stars=stars, transaction_id=transaction_id, boost_peer=boost_peer, giveaway_msg_id=giveaway_msg_id)

@register_tl
class MessageActionStarGift(TLObject):
    ID: int = 0xea2c31d3

    def __init__(self, name_hidden: bool = False, saved: bool = False, converted: bool = False, upgraded: bool = False, refunded: bool = False, can_upgrade: bool = False, prepaid_upgrade: bool = False, upgrade_separate: bool = False, auction_acquired: bool = False, gift: Any = None, message: Any = None, convert_stars: Any = None, upgrade_msg_id: Any = None, upgrade_stars: Any = None, from_id: Any = None, peer: Any = None, saved_id: Any = None, prepaid_upgrade_hash: Any = None, gift_msg_id: Any = None, to_id: Any = None, gift_num: Any = None) -> None:
        self.name_hidden = name_hidden
        self.saved = saved
        self.converted = converted
        self.upgraded = upgraded
        self.refunded = refunded
        self.can_upgrade = can_upgrade
        self.prepaid_upgrade = prepaid_upgrade
        self.upgrade_separate = upgrade_separate
        self.auction_acquired = auction_acquired
        self.gift = gift
        self.message = message
        self.convert_stars = convert_stars
        self.upgrade_msg_id = upgrade_msg_id
        self.upgrade_stars = upgrade_stars
        self.from_id = from_id
        self.peer = peer
        self.saved_id = saved_id
        self.prepaid_upgrade_hash = prepaid_upgrade_hash
        self.gift_msg_id = gift_msg_id
        self.to_id = to_id
        self.gift_num = gift_num

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.name_hidden:
            flags |= (1 << 0)
        if self.saved:
            flags |= (1 << 2)
        if self.converted:
            flags |= (1 << 3)
        if self.upgraded:
            flags |= (1 << 5)
        if self.refunded:
            flags |= (1 << 9)
        if self.can_upgrade:
            flags |= (1 << 10)
        if self.prepaid_upgrade:
            flags |= (1 << 13)
        if self.upgrade_separate:
            flags |= (1 << 16)
        if self.auction_acquired:
            flags |= (1 << 17)
        if self.message is not None:
            flags |= (1 << 1)
        if self.convert_stars is not None:
            flags |= (1 << 4)
        if self.upgrade_msg_id is not None:
            flags |= (1 << 5)
        if self.upgrade_stars is not None:
            flags |= (1 << 8)
        if self.from_id is not None:
            flags |= (1 << 11)
        if self.peer is not None:
            flags |= (1 << 12)
        if self.saved_id is not None:
            flags |= (1 << 12)
        if self.prepaid_upgrade_hash is not None:
            flags |= (1 << 14)
        if self.gift_msg_id is not None:
            flags |= (1 << 15)
        if self.to_id is not None:
            flags |= (1 << 18)
        if self.gift_num is not None:
            flags |= (1 << 19)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if self.message is not None:
            if hasattr(self.message, 'write'):
                self.message.write(writer)
            else:
                writer.write_bytes(self.message or b'')
        if self.convert_stars is not None:
            writer.write_int64(self.convert_stars or 0)
        if self.upgrade_msg_id is not None:
            writer.write_int32(self.upgrade_msg_id or 0)
        if self.upgrade_stars is not None:
            writer.write_int64(self.upgrade_stars or 0)
        if self.from_id is not None:
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if self.saved_id is not None:
            writer.write_int64(self.saved_id or 0)
        if self.prepaid_upgrade_hash is not None:
            writer.write_string(str(self.prepaid_upgrade_hash or ''))
        if self.gift_msg_id is not None:
            writer.write_int32(self.gift_msg_id or 0)
        if self.to_id is not None:
            if hasattr(self.to_id, 'write'):
                self.to_id.write(writer)
            else:
                writer.write_bytes(self.to_id or b'')
        if self.gift_num is not None:
            writer.write_int32(self.gift_num or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGift':
        flags = reader.read_uint32()
        name_hidden = bool(flags & (1 << 0))
        saved = bool(flags & (1 << 2))
        converted = bool(flags & (1 << 3))
        upgraded = bool(flags & (1 << 5))
        refunded = bool(flags & (1 << 9))
        can_upgrade = bool(flags & (1 << 10))
        prepaid_upgrade = bool(flags & (1 << 13))
        upgrade_separate = bool(flags & (1 << 16))
        auction_acquired = bool(flags & (1 << 17))
        gift = reader.read_object()
        message = None
        if flags & (1 << 1):
            message = reader.read_object()
        convert_stars = None
        if flags & (1 << 4):
            convert_stars = reader.read_int64()
        upgrade_msg_id = None
        if flags & (1 << 5):
            upgrade_msg_id = reader.read_int32()
        upgrade_stars = None
        if flags & (1 << 8):
            upgrade_stars = reader.read_int64()
        from_id = None
        if flags & (1 << 11):
            from_id = reader.read_object()
        peer = None
        if flags & (1 << 12):
            peer = reader.read_object()
        saved_id = None
        if flags & (1 << 12):
            saved_id = reader.read_int64()
        prepaid_upgrade_hash = None
        if flags & (1 << 14):
            prepaid_upgrade_hash = reader.read_string()
        gift_msg_id = None
        if flags & (1 << 15):
            gift_msg_id = reader.read_int32()
        to_id = None
        if flags & (1 << 18):
            to_id = reader.read_object()
        gift_num = None
        if flags & (1 << 19):
            gift_num = reader.read_int32()
        return cls(name_hidden=name_hidden, saved=saved, converted=converted, upgraded=upgraded, refunded=refunded, can_upgrade=can_upgrade, prepaid_upgrade=prepaid_upgrade, upgrade_separate=upgrade_separate, auction_acquired=auction_acquired, gift=gift, message=message, convert_stars=convert_stars, upgrade_msg_id=upgrade_msg_id, upgrade_stars=upgrade_stars, from_id=from_id, peer=peer, saved_id=saved_id, prepaid_upgrade_hash=prepaid_upgrade_hash, gift_msg_id=gift_msg_id, to_id=to_id, gift_num=gift_num)

@register_tl
class MessageActionStarGiftUnique(TLObject):
    ID: int = 0xe6c31522

    def __init__(self, upgrade: bool = False, transferred: bool = False, saved: bool = False, refunded: bool = False, prepaid_upgrade: bool = False, assigned: bool = False, from_offer: bool = False, craft: bool = False, gift: Any = None, can_export_at: Any = None, transfer_stars: Any = None, from_id: Any = None, peer: Any = None, saved_id: Any = None, resale_amount: Any = None, can_transfer_at: Any = None, can_resell_at: Any = None, drop_original_details_stars: Any = None, can_craft_at: Any = None) -> None:
        self.upgrade = upgrade
        self.transferred = transferred
        self.saved = saved
        self.refunded = refunded
        self.prepaid_upgrade = prepaid_upgrade
        self.assigned = assigned
        self.from_offer = from_offer
        self.craft = craft
        self.gift = gift
        self.can_export_at = can_export_at
        self.transfer_stars = transfer_stars
        self.from_id = from_id
        self.peer = peer
        self.saved_id = saved_id
        self.resale_amount = resale_amount
        self.can_transfer_at = can_transfer_at
        self.can_resell_at = can_resell_at
        self.drop_original_details_stars = drop_original_details_stars
        self.can_craft_at = can_craft_at

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.upgrade:
            flags |= (1 << 0)
        if self.transferred:
            flags |= (1 << 1)
        if self.saved:
            flags |= (1 << 2)
        if self.refunded:
            flags |= (1 << 5)
        if self.prepaid_upgrade:
            flags |= (1 << 11)
        if self.assigned:
            flags |= (1 << 13)
        if self.from_offer:
            flags |= (1 << 14)
        if self.craft:
            flags |= (1 << 16)
        if self.can_export_at is not None:
            flags |= (1 << 3)
        if self.transfer_stars is not None:
            flags |= (1 << 4)
        if self.from_id is not None:
            flags |= (1 << 6)
        if self.peer is not None:
            flags |= (1 << 7)
        if self.saved_id is not None:
            flags |= (1 << 7)
        if self.resale_amount is not None:
            flags |= (1 << 8)
        if self.can_transfer_at is not None:
            flags |= (1 << 9)
        if self.can_resell_at is not None:
            flags |= (1 << 10)
        if self.drop_original_details_stars is not None:
            flags |= (1 << 12)
        if self.can_craft_at is not None:
            flags |= (1 << 15)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if self.can_export_at is not None:
            writer.write_int32(self.can_export_at or 0)
        if self.transfer_stars is not None:
            writer.write_int64(self.transfer_stars or 0)
        if self.from_id is not None:
            if hasattr(self.from_id, 'write'):
                self.from_id.write(writer)
            else:
                writer.write_bytes(self.from_id or b'')
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if self.saved_id is not None:
            writer.write_int64(self.saved_id or 0)
        if self.resale_amount is not None:
            if hasattr(self.resale_amount, 'write'):
                self.resale_amount.write(writer)
            else:
                writer.write_bytes(self.resale_amount or b'')
        if self.can_transfer_at is not None:
            writer.write_int32(self.can_transfer_at or 0)
        if self.can_resell_at is not None:
            writer.write_int32(self.can_resell_at or 0)
        if self.drop_original_details_stars is not None:
            writer.write_int64(self.drop_original_details_stars or 0)
        if self.can_craft_at is not None:
            writer.write_int32(self.can_craft_at or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGiftUnique':
        flags = reader.read_uint32()
        upgrade = bool(flags & (1 << 0))
        transferred = bool(flags & (1 << 1))
        saved = bool(flags & (1 << 2))
        refunded = bool(flags & (1 << 5))
        prepaid_upgrade = bool(flags & (1 << 11))
        assigned = bool(flags & (1 << 13))
        from_offer = bool(flags & (1 << 14))
        craft = bool(flags & (1 << 16))
        gift = reader.read_object()
        can_export_at = None
        if flags & (1 << 3):
            can_export_at = reader.read_int32()
        transfer_stars = None
        if flags & (1 << 4):
            transfer_stars = reader.read_int64()
        from_id = None
        if flags & (1 << 6):
            from_id = reader.read_object()
        peer = None
        if flags & (1 << 7):
            peer = reader.read_object()
        saved_id = None
        if flags & (1 << 7):
            saved_id = reader.read_int64()
        resale_amount = None
        if flags & (1 << 8):
            resale_amount = reader.read_object()
        can_transfer_at = None
        if flags & (1 << 9):
            can_transfer_at = reader.read_int32()
        can_resell_at = None
        if flags & (1 << 10):
            can_resell_at = reader.read_int32()
        drop_original_details_stars = None
        if flags & (1 << 12):
            drop_original_details_stars = reader.read_int64()
        can_craft_at = None
        if flags & (1 << 15):
            can_craft_at = reader.read_int32()
        return cls(upgrade=upgrade, transferred=transferred, saved=saved, refunded=refunded, prepaid_upgrade=prepaid_upgrade, assigned=assigned, from_offer=from_offer, craft=craft, gift=gift, can_export_at=can_export_at, transfer_stars=transfer_stars, from_id=from_id, peer=peer, saved_id=saved_id, resale_amount=resale_amount, can_transfer_at=can_transfer_at, can_resell_at=can_resell_at, drop_original_details_stars=drop_original_details_stars, can_craft_at=can_craft_at)

@register_tl
class MessageActionPaidMessagesRefunded(TLObject):
    ID: int = 0xac1f1fcd

    def __init__(self, count: Any = None, stars: Any = None) -> None:
        self.count = count
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaidMessagesRefunded':
        count = reader.read_int32()
        stars = reader.read_int64()
        return cls(count=count, stars=stars)

@register_tl
class MessageActionPaidMessagesPrice(TLObject):
    ID: int = 0x84b88578

    def __init__(self, broadcast_messages_allowed: bool = False, stars: Any = None) -> None:
        self.broadcast_messages_allowed = broadcast_messages_allowed
        self.stars = stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast_messages_allowed:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPaidMessagesPrice':
        flags = reader.read_uint32()
        broadcast_messages_allowed = bool(flags & (1 << 0))
        stars = reader.read_int64()
        return cls(broadcast_messages_allowed=broadcast_messages_allowed, stars=stars)

@register_tl
class MessageActionConferenceCall(TLObject):
    ID: int = 0x2ffe2f7a

    def __init__(self, missed: bool = False, active: bool = False, video: bool = False, call_id: Any = None, duration: Any = None, other_participants: Any = None) -> None:
        self.missed = missed
        self.active = active
        self.video = video
        self.call_id = call_id
        self.duration = duration
        self.other_participants = other_participants

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.missed:
            flags |= (1 << 0)
        if self.active:
            flags |= (1 << 1)
        if self.video:
            flags |= (1 << 4)
        if self.duration is not None:
            flags |= (1 << 2)
        if self.other_participants is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int64(self.call_id or 0)
        if self.duration is not None:
            writer.write_int32(self.duration or 0)
        if self.other_participants is not None:
            writer.write_vector(self.other_participants or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionConferenceCall':
        flags = reader.read_uint32()
        missed = bool(flags & (1 << 0))
        active = bool(flags & (1 << 1))
        video = bool(flags & (1 << 4))
        call_id = reader.read_int64()
        duration = None
        if flags & (1 << 2):
            duration = reader.read_int32()
        other_participants = None
        if flags & (1 << 3):
            other_participants = reader.read_vector(lambda r: r.read_object())
        return cls(missed=missed, active=active, video=video, call_id=call_id, duration=duration, other_participants=other_participants)

@register_tl
class MessageActionTodoCompletions(TLObject):
    ID: int = 0xcc7c5c89

    def __init__(self, completed: Any = None, incompleted: Any = None) -> None:
        self.completed = completed
        self.incompleted = incompleted

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.completed or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.incompleted or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTodoCompletions':
        completed = reader.read_vector(lambda r: r.read_object())
        incompleted = reader.read_vector(lambda r: r.read_object())
        return cls(completed=completed, incompleted=incompleted)

@register_tl
class MessageActionTodoAppendTasks(TLObject):
    ID: int = 0xc7edbc83

    def __init__(self, list: Any = None) -> None:
        self.list = list

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.list or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionTodoAppendTasks':
        list = reader.read_vector(lambda r: r.read_object())
        return cls(list=list)

@register_tl
class MessageActionSuggestedPostApproval(TLObject):
    ID: int = 0xee7a1596

    def __init__(self, rejected: bool = False, balance_too_low: bool = False, reject_comment: Any = None, schedule_date: Any = None, price: Any = None) -> None:
        self.rejected = rejected
        self.balance_too_low = balance_too_low
        self.reject_comment = reject_comment
        self.schedule_date = schedule_date
        self.price = price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rejected:
            flags |= (1 << 0)
        if self.balance_too_low:
            flags |= (1 << 1)
        if self.reject_comment is not None:
            flags |= (1 << 2)
        if self.schedule_date is not None:
            flags |= (1 << 3)
        if self.price is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.reject_comment is not None:
            writer.write_string(str(self.reject_comment or ''))
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.price is not None:
            if hasattr(self.price, 'write'):
                self.price.write(writer)
            else:
                writer.write_bytes(self.price or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestedPostApproval':
        flags = reader.read_uint32()
        rejected = bool(flags & (1 << 0))
        balance_too_low = bool(flags & (1 << 1))
        reject_comment = None
        if flags & (1 << 2):
            reject_comment = reader.read_string()
        schedule_date = None
        if flags & (1 << 3):
            schedule_date = reader.read_int32()
        price = None
        if flags & (1 << 4):
            price = reader.read_object()
        return cls(rejected=rejected, balance_too_low=balance_too_low, reject_comment=reject_comment, schedule_date=schedule_date, price=price)

@register_tl
class MessageActionSuggestedPostSuccess(TLObject):
    ID: int = 0x95ddcf69

    def __init__(self, price: Any = None) -> None:
        self.price = price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.price, 'write'):
            self.price.write(writer)
        else:
            writer.write_bytes(self.price or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestedPostSuccess':
        price = reader.read_object()
        return cls(price=price)

@register_tl
class MessageActionSuggestedPostRefund(TLObject):
    ID: int = 0x69f916f8

    def __init__(self, payer_initiated: bool = False) -> None:
        self.payer_initiated = payer_initiated

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.payer_initiated:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestedPostRefund':
        flags = reader.read_uint32()
        payer_initiated = bool(flags & (1 << 0))
        return cls(payer_initiated=payer_initiated)

@register_tl
class MessageActionGiftTon(TLObject):
    ID: int = 0xa8a3c699

    def __init__(self, currency: Any = None, amount: Any = None, crypto_currency: Any = None, crypto_amount: Any = None, transaction_id: Any = None) -> None:
        self.currency = currency
        self.amount = amount
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.transaction_id = transaction_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.transaction_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)
        writer.write_string(str(self.crypto_currency or ''))
        writer.write_int64(self.crypto_amount or 0)
        if self.transaction_id is not None:
            writer.write_string(str(self.transaction_id or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionGiftTon':
        flags = reader.read_uint32()
        currency = reader.read_string()
        amount = reader.read_int64()
        crypto_currency = reader.read_string()
        crypto_amount = reader.read_int64()
        transaction_id = None
        if flags & (1 << 0):
            transaction_id = reader.read_string()
        return cls(currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, transaction_id=transaction_id)

@register_tl
class MessageActionSuggestBirthday(TLObject):
    ID: int = 0x2c8f2a25

    def __init__(self, birthday: Any = None) -> None:
        self.birthday = birthday

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.birthday, 'write'):
            self.birthday.write(writer)
        else:
            writer.write_bytes(self.birthday or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionSuggestBirthday':
        birthday = reader.read_object()
        return cls(birthday=birthday)

@register_tl
class MessageActionStarGiftPurchaseOffer(TLObject):
    ID: int = 0x774278d4

    def __init__(self, accepted: bool = False, declined: bool = False, gift: Any = None, price: Any = None, expires_at: Any = None) -> None:
        self.accepted = accepted
        self.declined = declined
        self.gift = gift
        self.price = price
        self.expires_at = expires_at

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accepted:
            flags |= (1 << 0)
        if self.declined:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if hasattr(self.price, 'write'):
            self.price.write(writer)
        else:
            writer.write_bytes(self.price or b'')
        writer.write_int32(self.expires_at or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGiftPurchaseOffer':
        flags = reader.read_uint32()
        accepted = bool(flags & (1 << 0))
        declined = bool(flags & (1 << 1))
        gift = reader.read_object()
        price = reader.read_object()
        expires_at = reader.read_int32()
        return cls(accepted=accepted, declined=declined, gift=gift, price=price, expires_at=expires_at)

@register_tl
class MessageActionStarGiftPurchaseOfferDeclined(TLObject):
    ID: int = 0x73ada76b

    def __init__(self, expired: bool = False, gift: Any = None, price: Any = None) -> None:
        self.expired = expired
        self.gift = gift
        self.price = price

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.expired:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.gift, 'write'):
            self.gift.write(writer)
        else:
            writer.write_bytes(self.gift or b'')
        if hasattr(self.price, 'write'):
            self.price.write(writer)
        else:
            writer.write_bytes(self.price or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionStarGiftPurchaseOfferDeclined':
        flags = reader.read_uint32()
        expired = bool(flags & (1 << 0))
        gift = reader.read_object()
        price = reader.read_object()
        return cls(expired=expired, gift=gift, price=price)

@register_tl
class MessageActionNewCreatorPending(TLObject):
    ID: int = 0xb07ed085

    def __init__(self, new_creator_id: Any = None) -> None:
        self.new_creator_id = new_creator_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.new_creator_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionNewCreatorPending':
        new_creator_id = reader.read_int64()
        return cls(new_creator_id=new_creator_id)

@register_tl
class MessageActionChangeCreator(TLObject):
    ID: int = 0xe188503b

    def __init__(self, new_creator_id: Any = None) -> None:
        self.new_creator_id = new_creator_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.new_creator_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionChangeCreator':
        new_creator_id = reader.read_int64()
        return cls(new_creator_id=new_creator_id)

@register_tl
class MessageActionNoForwardsToggle(TLObject):
    ID: int = 0xbf7d6572

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.prev_value))
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionNoForwardsToggle':
        prev_value = reader.read_bool()
        new_value = reader.read_bool()
        return cls(prev_value=prev_value, new_value=new_value)

@register_tl
class MessageActionNoForwardsRequest(TLObject):
    ID: int = 0x3e2793ba

    def __init__(self, expired: bool = False, prev_value: Any = None, new_value: Any = None) -> None:
        self.expired = expired
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.expired:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_bool(bool(self.prev_value))
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionNoForwardsRequest':
        flags = reader.read_uint32()
        expired = bool(flags & (1 << 0))
        prev_value = reader.read_bool()
        new_value = reader.read_bool()
        return cls(expired=expired, prev_value=prev_value, new_value=new_value)

@register_tl
class MessageActionPollAppendAnswer(TLObject):
    ID: int = 0x9da1cd6c

    def __init__(self, answer: Any = None) -> None:
        self.answer = answer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.answer, 'write'):
            self.answer.write(writer)
        else:
            writer.write_bytes(self.answer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPollAppendAnswer':
        answer = reader.read_object()
        return cls(answer=answer)

@register_tl
class MessageActionPollDeleteAnswer(TLObject):
    ID: int = 0x399674dc

    def __init__(self, answer: Any = None) -> None:
        self.answer = answer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.answer, 'write'):
            self.answer.write(writer)
        else:
            writer.write_bytes(self.answer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionPollDeleteAnswer':
        answer = reader.read_object()
        return cls(answer=answer)

@register_tl
class MessageActionManagedBotCreated(TLObject):
    ID: int = 0x16605e3e

    def __init__(self, bot_id: Any = None) -> None:
        self.bot_id = bot_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bot_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageActionManagedBotCreated':
        bot_id = reader.read_int64()
        return cls(bot_id=bot_id)

@register_tl
class Dialog(TLObject):
    ID: int = 0xfc89f7f3

    def __init__(self, pinned: bool = False, unread_mark: bool = False, view_forum_as_messages: bool = False, peer: Any = None, top_message: Any = None, read_inbox_max_id: Any = None, read_outbox_max_id: Any = None, unread_count: Any = None, unread_mentions_count: Any = None, unread_reactions_count: Any = None, unread_poll_votes_count: Any = None, notify_settings: Any = None, pts: Any = None, draft: Any = None, folder_id: Any = None, ttl_period: Any = None) -> None:
        self.pinned = pinned
        self.unread_mark = unread_mark
        self.view_forum_as_messages = view_forum_as_messages
        self.peer = peer
        self.top_message = top_message
        self.read_inbox_max_id = read_inbox_max_id
        self.read_outbox_max_id = read_outbox_max_id
        self.unread_count = unread_count
        self.unread_mentions_count = unread_mentions_count
        self.unread_reactions_count = unread_reactions_count
        self.unread_poll_votes_count = unread_poll_votes_count
        self.notify_settings = notify_settings
        self.pts = pts
        self.draft = draft
        self.folder_id = folder_id
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 2)
        if self.unread_mark:
            flags |= (1 << 3)
        if self.view_forum_as_messages:
            flags |= (1 << 6)
        if self.pts is not None:
            flags |= (1 << 0)
        if self.draft is not None:
            flags |= (1 << 1)
        if self.folder_id is not None:
            flags |= (1 << 4)
        if self.ttl_period is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.read_inbox_max_id or 0)
        writer.write_int32(self.read_outbox_max_id or 0)
        writer.write_int32(self.unread_count or 0)
        writer.write_int32(self.unread_mentions_count or 0)
        writer.write_int32(self.unread_reactions_count or 0)
        writer.write_int32(self.unread_poll_votes_count or 0)
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')
        if self.pts is not None:
            writer.write_int32(self.pts or 0)
        if self.draft is not None:
            if hasattr(self.draft, 'write'):
                self.draft.write(writer)
            else:
                writer.write_bytes(self.draft or b'')
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Dialog':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 2))
        unread_mark = bool(flags & (1 << 3))
        view_forum_as_messages = bool(flags & (1 << 6))
        peer = reader.read_object()
        top_message = reader.read_int32()
        read_inbox_max_id = reader.read_int32()
        read_outbox_max_id = reader.read_int32()
        unread_count = reader.read_int32()
        unread_mentions_count = reader.read_int32()
        unread_reactions_count = reader.read_int32()
        unread_poll_votes_count = reader.read_int32()
        notify_settings = reader.read_object()
        pts = None
        if flags & (1 << 0):
            pts = reader.read_int32()
        draft = None
        if flags & (1 << 1):
            draft = reader.read_object()
        folder_id = None
        if flags & (1 << 4):
            folder_id = reader.read_int32()
        ttl_period = None
        if flags & (1 << 5):
            ttl_period = reader.read_int32()
        return cls(pinned=pinned, unread_mark=unread_mark, view_forum_as_messages=view_forum_as_messages, peer=peer, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, unread_poll_votes_count=unread_poll_votes_count, notify_settings=notify_settings, pts=pts, draft=draft, folder_id=folder_id, ttl_period=ttl_period)

@register_tl
class DialogFolder(TLObject):
    ID: int = 0x71bd134c

    def __init__(self, pinned: bool = False, folder: Any = None, peer: Any = None, top_message: Any = None, unread_muted_peers_count: Any = None, unread_unmuted_peers_count: Any = None, unread_muted_messages_count: Any = None, unread_unmuted_messages_count: Any = None) -> None:
        self.pinned = pinned
        self.folder = folder
        self.peer = peer
        self.top_message = top_message
        self.unread_muted_peers_count = unread_muted_peers_count
        self.unread_unmuted_peers_count = unread_unmuted_peers_count
        self.unread_muted_messages_count = unread_muted_messages_count
        self.unread_unmuted_messages_count = unread_unmuted_messages_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if hasattr(self.folder, 'write'):
            self.folder.write(writer)
        else:
            writer.write_bytes(self.folder or b'')
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.top_message or 0)
        writer.write_int32(self.unread_muted_peers_count or 0)
        writer.write_int32(self.unread_unmuted_peers_count or 0)
        writer.write_int32(self.unread_muted_messages_count or 0)
        writer.write_int32(self.unread_unmuted_messages_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DialogFolder':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 2))
        folder = reader.read_object()
        peer = reader.read_object()
        top_message = reader.read_int32()
        unread_muted_peers_count = reader.read_int32()
        unread_unmuted_peers_count = reader.read_int32()
        unread_muted_messages_count = reader.read_int32()
        unread_unmuted_messages_count = reader.read_int32()
        return cls(pinned=pinned, folder=folder, peer=peer, top_message=top_message, unread_muted_peers_count=unread_muted_peers_count, unread_unmuted_peers_count=unread_unmuted_peers_count, unread_muted_messages_count=unread_muted_messages_count, unread_unmuted_messages_count=unread_unmuted_messages_count)

@register_tl
class PhotoEmpty(TLObject):
    ID: int = 0x2331b22d

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoEmpty':
        id = reader.read_int64()
        return cls(id=id)

@register_tl
class Photo(TLObject):
    ID: int = 0xfb197a65

    def __init__(self, has_stickers: bool = False, id: Any = None, access_hash: Any = None, file_reference: Any = None, date: Any = None, sizes: Any = None, video_sizes: Any = None, dc_id: Any = None) -> None:
        self.has_stickers = has_stickers
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.date = date
        self.sizes = sizes
        self.video_sizes = video_sizes
        self.dc_id = dc_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_stickers:
            flags |= (1 << 0)
        if self.video_sizes is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_bytes(self.file_reference or b'')
        writer.write_int32(self.date or 0)
        writer.write_vector(self.sizes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.video_sizes is not None:
            writer.write_vector(self.video_sizes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.dc_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Photo':
        flags = reader.read_uint32()
        has_stickers = bool(flags & (1 << 0))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        date = reader.read_int32()
        sizes = reader.read_vector(lambda r: r.read_object())
        video_sizes = None
        if flags & (1 << 1):
            video_sizes = reader.read_vector(lambda r: r.read_object())
        dc_id = reader.read_int32()
        return cls(has_stickers=has_stickers, id=id, access_hash=access_hash, file_reference=file_reference, date=date, sizes=sizes, video_sizes=video_sizes, dc_id=dc_id)

@register_tl
class PhotoSizeEmpty(TLObject):
    ID: int = 0xe17e23c

    def __init__(self, type: Any = None) -> None:
        self.type = type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSizeEmpty':
        type = reader.read_string()
        return cls(type=type)

@register_tl
class PhotoSize(TLObject):
    ID: int = 0x75c78e60

    def __init__(self, type: Any = None, w: Any = None, h: Any = None, size: Any = None) -> None:
        self.type = type
        self.w = w
        self.h = h
        self.size = size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSize':
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        return cls(type=type, w=w, h=h, size=size)

@register_tl
class PhotoCachedSize(TLObject):
    ID: int = 0x21e1ad6

    def __init__(self, type: Any = None, w: Any = None, h: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.w = w
        self.h = h
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoCachedSize':
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(type=type, w=w, h=h, bytes=bytes)

@register_tl
class PhotoStrippedSize(TLObject):
    ID: int = 0xe0b0bc2e

    def __init__(self, type: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoStrippedSize':
        type = reader.read_string()
        bytes = reader.read_bytes()
        return cls(type=type, bytes=bytes)

@register_tl
class PhotoSizeProgressive(TLObject):
    ID: int = 0xfa3efb95

    def __init__(self, type: Any = None, w: Any = None, h: Any = None, sizes: Any = None) -> None:
        self.type = type
        self.w = w
        self.h = h
        self.sizes = sizes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_vector(self.sizes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSizeProgressive':
        type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        sizes = reader.read_vector(lambda r: r.read_object())
        return cls(type=type, w=w, h=h, sizes=sizes)

@register_tl
class PhotoPathSize(TLObject):
    ID: int = 0xd8214d41

    def __init__(self, type: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.type or ''))
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoPathSize':
        type = reader.read_string()
        bytes = reader.read_bytes()
        return cls(type=type, bytes=bytes)

@register_tl
class GeoPointEmpty(TLObject):
    ID: int = 0x1117dd5f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'GeoPointEmpty':
        return cls()

@register_tl
class GeoPoint(TLObject):
    ID: int = 0xb2a2f663

    def __init__(self, long: Any = None, lat: Any = None, access_hash: Any = None, accuracy_radius: Any = None) -> None:
        self.long = long
        self.lat = lat
        self.access_hash = access_hash
        self.accuracy_radius = accuracy_radius

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.accuracy_radius is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_double(float(self.long or 0.0))
        writer.write_double(float(self.lat or 0.0))
        writer.write_int64(self.access_hash or 0)
        if self.accuracy_radius is not None:
            writer.write_int32(self.accuracy_radius or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'GeoPoint':
        flags = reader.read_uint32()
        long = reader.read_double()
        lat = reader.read_double()
        access_hash = reader.read_int64()
        accuracy_radius = None
        if flags & (1 << 0):
            accuracy_radius = reader.read_int32()
        return cls(long=long, lat=lat, access_hash=access_hash, accuracy_radius=accuracy_radius)

@register_tl
class AuthSentCode(TLObject):
    ID: int = 0x5e002502

    def __init__(self, type: Any = None, phone_code_hash: Any = None, next_type: Any = None, timeout: Any = None) -> None:
        self.type = type
        self.phone_code_hash = phone_code_hash
        self.next_type = next_type
        self.timeout = timeout

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.next_type is not None:
            flags |= (1 << 1)
        if self.timeout is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if hasattr(self.type, 'write'):
            self.type.write(writer)
        else:
            writer.write_bytes(self.type or b'')
        writer.write_string(str(self.phone_code_hash or ''))
        if self.next_type is not None:
            if hasattr(self.next_type, 'write'):
                self.next_type.write(writer)
            else:
                writer.write_bytes(self.next_type or b'')
        if self.timeout is not None:
            writer.write_int32(self.timeout or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCode':
        flags = reader.read_uint32()
        type = reader.read_object()
        phone_code_hash = reader.read_string()
        next_type = None
        if flags & (1 << 1):
            next_type = reader.read_object()
        timeout = None
        if flags & (1 << 2):
            timeout = reader.read_int32()
        return cls(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)

@register_tl
class AuthSentCodeSuccess(TLObject):
    ID: int = 0x2390fe44

    def __init__(self, authorization: Any = None) -> None:
        self.authorization = authorization

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.authorization, 'write'):
            self.authorization.write(writer)
        else:
            writer.write_bytes(self.authorization or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodeSuccess':
        authorization = reader.read_object()
        return cls(authorization=authorization)

@register_tl
class AuthSentCodePaymentRequired(TLObject):
    ID: int = 0xf8827ebf

    def __init__(self, store_product: Any = None, phone_code_hash: Any = None, support_email_address: Any = None, support_email_subject: Any = None, premium_days: Any = None, currency: Any = None, amount: Any = None) -> None:
        self.store_product = store_product
        self.phone_code_hash = phone_code_hash
        self.support_email_address = support_email_address
        self.support_email_subject = support_email_subject
        self.premium_days = premium_days
        self.currency = currency
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.store_product or ''))
        writer.write_string(str(self.phone_code_hash or ''))
        writer.write_string(str(self.support_email_address or ''))
        writer.write_string(str(self.support_email_subject or ''))
        writer.write_int32(self.premium_days or 0)
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthSentCodePaymentRequired':
        store_product = reader.read_string()
        phone_code_hash = reader.read_string()
        support_email_address = reader.read_string()
        support_email_subject = reader.read_string()
        premium_days = reader.read_int32()
        currency = reader.read_string()
        amount = reader.read_int64()
        return cls(store_product=store_product, phone_code_hash=phone_code_hash, support_email_address=support_email_address, support_email_subject=support_email_subject, premium_days=premium_days, currency=currency, amount=amount)

@register_tl
class AuthAuthorization(TLObject):
    ID: int = 0x2ea2c0d4

    def __init__(self, setup_password_required: bool = False, otherwise_relogin_days: Any = None, tmp_sessions: Any = None, future_auth_token: Any = None, user: Any = None) -> None:
        self.setup_password_required = setup_password_required
        self.otherwise_relogin_days = otherwise_relogin_days
        self.tmp_sessions = tmp_sessions
        self.future_auth_token = future_auth_token
        self.user = user

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.setup_password_required:
            flags |= (1 << 1)
        if self.otherwise_relogin_days is not None:
            flags |= (1 << 1)
        if self.tmp_sessions is not None:
            flags |= (1 << 0)
        if self.future_auth_token is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.otherwise_relogin_days is not None:
            writer.write_int32(self.otherwise_relogin_days or 0)
        if self.tmp_sessions is not None:
            writer.write_int32(self.tmp_sessions or 0)
        if self.future_auth_token is not None:
            writer.write_bytes(self.future_auth_token or b'')
        if hasattr(self.user, 'write'):
            self.user.write(writer)
        else:
            writer.write_bytes(self.user or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthAuthorization':
        flags = reader.read_uint32()
        setup_password_required = bool(flags & (1 << 1))
        otherwise_relogin_days = None
        if flags & (1 << 1):
            otherwise_relogin_days = reader.read_int32()
        tmp_sessions = None
        if flags & (1 << 0):
            tmp_sessions = reader.read_int32()
        future_auth_token = None
        if flags & (1 << 2):
            future_auth_token = reader.read_bytes()
        user = reader.read_object()
        return cls(setup_password_required=setup_password_required, otherwise_relogin_days=otherwise_relogin_days, tmp_sessions=tmp_sessions, future_auth_token=future_auth_token, user=user)

@register_tl
class AuthAuthorizationSignUpRequired(TLObject):
    ID: int = 0x44747e9a

    def __init__(self, terms_of_service: Any = None) -> None:
        self.terms_of_service = terms_of_service

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.terms_of_service is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.terms_of_service is not None:
            if hasattr(self.terms_of_service, 'write'):
                self.terms_of_service.write(writer)
            else:
                writer.write_bytes(self.terms_of_service or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthAuthorizationSignUpRequired':
        flags = reader.read_uint32()
        terms_of_service = None
        if flags & (1 << 0):
            terms_of_service = reader.read_object()
        return cls(terms_of_service=terms_of_service)

@register_tl
class AuthExportedAuthorization(TLObject):
    ID: int = 0xb434e2b8

    def __init__(self, id: Any = None, bytes: Any = None) -> None:
        self.id = id
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthExportedAuthorization':
        id = reader.read_int64()
        bytes = reader.read_bytes()
        return cls(id=id, bytes=bytes)

@register_tl
class InputNotifyPeer(TLObject):
    ID: int = 0xb8bc5b0c

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyPeer':
        peer = reader.read_object()
        return cls(peer=peer)

@register_tl
class InputNotifyUsers(TLObject):
    ID: int = 0x193b4417

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyUsers':
        return cls()

@register_tl
class InputNotifyChats(TLObject):
    ID: int = 0x4a95e84e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyChats':
        return cls()

@register_tl
class InputNotifyBroadcasts(TLObject):
    ID: int = 0xb1db7c7e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyBroadcasts':
        return cls()

@register_tl
class InputNotifyForumTopic(TLObject):
    ID: int = 0x5c467992

    def __init__(self, peer: Any = None, top_msg_id: Any = None) -> None:
        self.peer = peer
        self.top_msg_id = top_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.top_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputNotifyForumTopic':
        peer = reader.read_object()
        top_msg_id = reader.read_int32()
        return cls(peer=peer, top_msg_id=top_msg_id)

@register_tl
class InputPeerNotifySettings(TLObject):
    ID: int = 0xcacb6ae2

    def __init__(self, show_previews: Any = None, silent: Any = None, mute_until: Any = None, sound: Any = None, stories_muted: Any = None, stories_hide_sender: Any = None, stories_sound: Any = None) -> None:
        self.show_previews = show_previews
        self.silent = silent
        self.mute_until = mute_until
        self.sound = sound
        self.stories_muted = stories_muted
        self.stories_hide_sender = stories_hide_sender
        self.stories_sound = stories_sound

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.show_previews is not None:
            flags |= (1 << 0)
        if self.silent is not None:
            flags |= (1 << 1)
        if self.mute_until is not None:
            flags |= (1 << 2)
        if self.sound is not None:
            flags |= (1 << 3)
        if self.stories_muted is not None:
            flags |= (1 << 6)
        if self.stories_hide_sender is not None:
            flags |= (1 << 7)
        if self.stories_sound is not None:
            flags |= (1 << 8)
        writer.write_uint32(flags)
        if self.show_previews is not None:
            writer.write_bool(bool(self.show_previews))
        if self.silent is not None:
            writer.write_bool(bool(self.silent))
        if self.mute_until is not None:
            writer.write_int32(self.mute_until or 0)
        if self.sound is not None:
            if hasattr(self.sound, 'write'):
                self.sound.write(writer)
            else:
                writer.write_bytes(self.sound or b'')
        if self.stories_muted is not None:
            writer.write_bool(bool(self.stories_muted))
        if self.stories_hide_sender is not None:
            writer.write_bool(bool(self.stories_hide_sender))
        if self.stories_sound is not None:
            if hasattr(self.stories_sound, 'write'):
                self.stories_sound.write(writer)
            else:
                writer.write_bytes(self.stories_sound or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPeerNotifySettings':
        flags = reader.read_uint32()
        show_previews = None
        if flags & (1 << 0):
            show_previews = reader.read_bool()
        silent = None
        if flags & (1 << 1):
            silent = reader.read_bool()
        mute_until = None
        if flags & (1 << 2):
            mute_until = reader.read_int32()
        sound = None
        if flags & (1 << 3):
            sound = reader.read_object()
        stories_muted = None
        if flags & (1 << 6):
            stories_muted = reader.read_bool()
        stories_hide_sender = None
        if flags & (1 << 7):
            stories_hide_sender = reader.read_bool()
        stories_sound = None
        if flags & (1 << 8):
            stories_sound = reader.read_object()
        return cls(show_previews=show_previews, silent=silent, mute_until=mute_until, sound=sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_sound=stories_sound)

@register_tl
class PeerNotifySettings(TLObject):
    ID: int = 0x99622c0c

    def __init__(self, show_previews: Any = None, silent: Any = None, mute_until: Any = None, ios_sound: Any = None, android_sound: Any = None, other_sound: Any = None, stories_muted: Any = None, stories_hide_sender: Any = None, stories_ios_sound: Any = None, stories_android_sound: Any = None, stories_other_sound: Any = None) -> None:
        self.show_previews = show_previews
        self.silent = silent
        self.mute_until = mute_until
        self.ios_sound = ios_sound
        self.android_sound = android_sound
        self.other_sound = other_sound
        self.stories_muted = stories_muted
        self.stories_hide_sender = stories_hide_sender
        self.stories_ios_sound = stories_ios_sound
        self.stories_android_sound = stories_android_sound
        self.stories_other_sound = stories_other_sound

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.show_previews is not None:
            flags |= (1 << 0)
        if self.silent is not None:
            flags |= (1 << 1)
        if self.mute_until is not None:
            flags |= (1 << 2)
        if self.ios_sound is not None:
            flags |= (1 << 3)
        if self.android_sound is not None:
            flags |= (1 << 4)
        if self.other_sound is not None:
            flags |= (1 << 5)
        if self.stories_muted is not None:
            flags |= (1 << 6)
        if self.stories_hide_sender is not None:
            flags |= (1 << 7)
        if self.stories_ios_sound is not None:
            flags |= (1 << 8)
        if self.stories_android_sound is not None:
            flags |= (1 << 9)
        if self.stories_other_sound is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.show_previews is not None:
            writer.write_bool(bool(self.show_previews))
        if self.silent is not None:
            writer.write_bool(bool(self.silent))
        if self.mute_until is not None:
            writer.write_int32(self.mute_until or 0)
        if self.ios_sound is not None:
            if hasattr(self.ios_sound, 'write'):
                self.ios_sound.write(writer)
            else:
                writer.write_bytes(self.ios_sound or b'')
        if self.android_sound is not None:
            if hasattr(self.android_sound, 'write'):
                self.android_sound.write(writer)
            else:
                writer.write_bytes(self.android_sound or b'')
        if self.other_sound is not None:
            if hasattr(self.other_sound, 'write'):
                self.other_sound.write(writer)
            else:
                writer.write_bytes(self.other_sound or b'')
        if self.stories_muted is not None:
            writer.write_bool(bool(self.stories_muted))
        if self.stories_hide_sender is not None:
            writer.write_bool(bool(self.stories_hide_sender))
        if self.stories_ios_sound is not None:
            if hasattr(self.stories_ios_sound, 'write'):
                self.stories_ios_sound.write(writer)
            else:
                writer.write_bytes(self.stories_ios_sound or b'')
        if self.stories_android_sound is not None:
            if hasattr(self.stories_android_sound, 'write'):
                self.stories_android_sound.write(writer)
            else:
                writer.write_bytes(self.stories_android_sound or b'')
        if self.stories_other_sound is not None:
            if hasattr(self.stories_other_sound, 'write'):
                self.stories_other_sound.write(writer)
            else:
                writer.write_bytes(self.stories_other_sound or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerNotifySettings':
        flags = reader.read_uint32()
        show_previews = None
        if flags & (1 << 0):
            show_previews = reader.read_bool()
        silent = None
        if flags & (1 << 1):
            silent = reader.read_bool()
        mute_until = None
        if flags & (1 << 2):
            mute_until = reader.read_int32()
        ios_sound = None
        if flags & (1 << 3):
            ios_sound = reader.read_object()
        android_sound = None
        if flags & (1 << 4):
            android_sound = reader.read_object()
        other_sound = None
        if flags & (1 << 5):
            other_sound = reader.read_object()
        stories_muted = None
        if flags & (1 << 6):
            stories_muted = reader.read_bool()
        stories_hide_sender = None
        if flags & (1 << 7):
            stories_hide_sender = reader.read_bool()
        stories_ios_sound = None
        if flags & (1 << 8):
            stories_ios_sound = reader.read_object()
        stories_android_sound = None
        if flags & (1 << 9):
            stories_android_sound = reader.read_object()
        stories_other_sound = None
        if flags & (1 << 10):
            stories_other_sound = reader.read_object()
        return cls(show_previews=show_previews, silent=silent, mute_until=mute_until, ios_sound=ios_sound, android_sound=android_sound, other_sound=other_sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_ios_sound=stories_ios_sound, stories_android_sound=stories_android_sound, stories_other_sound=stories_other_sound)

@register_tl
class PeerSettings(TLObject):
    ID: int = 0xf47741f7

    def __init__(self, report_spam: bool = False, add_contact: bool = False, block_contact: bool = False, share_contact: bool = False, need_contacts_exception: bool = False, report_geo: bool = False, autoarchived: bool = False, invite_members: bool = False, request_chat_broadcast: bool = False, business_bot_paused: bool = False, business_bot_can_reply: bool = False, geo_distance: Any = None, request_chat_title: Any = None, request_chat_date: Any = None, business_bot_id: Any = None, business_bot_manage_url: Any = None, charge_paid_message_stars: Any = None, registration_month: Any = None, phone_country: Any = None, name_change_date: Any = None, photo_change_date: Any = None) -> None:
        self.report_spam = report_spam
        self.add_contact = add_contact
        self.block_contact = block_contact
        self.share_contact = share_contact
        self.need_contacts_exception = need_contacts_exception
        self.report_geo = report_geo
        self.autoarchived = autoarchived
        self.invite_members = invite_members
        self.request_chat_broadcast = request_chat_broadcast
        self.business_bot_paused = business_bot_paused
        self.business_bot_can_reply = business_bot_can_reply
        self.geo_distance = geo_distance
        self.request_chat_title = request_chat_title
        self.request_chat_date = request_chat_date
        self.business_bot_id = business_bot_id
        self.business_bot_manage_url = business_bot_manage_url
        self.charge_paid_message_stars = charge_paid_message_stars
        self.registration_month = registration_month
        self.phone_country = phone_country
        self.name_change_date = name_change_date
        self.photo_change_date = photo_change_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.report_spam:
            flags |= (1 << 0)
        if self.add_contact:
            flags |= (1 << 1)
        if self.block_contact:
            flags |= (1 << 2)
        if self.share_contact:
            flags |= (1 << 3)
        if self.need_contacts_exception:
            flags |= (1 << 4)
        if self.report_geo:
            flags |= (1 << 5)
        if self.autoarchived:
            flags |= (1 << 7)
        if self.invite_members:
            flags |= (1 << 8)
        if self.request_chat_broadcast:
            flags |= (1 << 10)
        if self.business_bot_paused:
            flags |= (1 << 11)
        if self.business_bot_can_reply:
            flags |= (1 << 12)
        if self.geo_distance is not None:
            flags |= (1 << 6)
        if self.request_chat_title is not None:
            flags |= (1 << 9)
        if self.request_chat_date is not None:
            flags |= (1 << 9)
        if self.business_bot_id is not None:
            flags |= (1 << 13)
        if self.business_bot_manage_url is not None:
            flags |= (1 << 13)
        if self.charge_paid_message_stars is not None:
            flags |= (1 << 14)
        if self.registration_month is not None:
            flags |= (1 << 15)
        if self.phone_country is not None:
            flags |= (1 << 16)
        if self.name_change_date is not None:
            flags |= (1 << 17)
        if self.photo_change_date is not None:
            flags |= (1 << 18)
        writer.write_uint32(flags)
        if self.geo_distance is not None:
            writer.write_int32(self.geo_distance or 0)
        if self.request_chat_title is not None:
            writer.write_string(str(self.request_chat_title or ''))
        if self.request_chat_date is not None:
            writer.write_int32(self.request_chat_date or 0)
        if self.business_bot_id is not None:
            writer.write_int64(self.business_bot_id or 0)
        if self.business_bot_manage_url is not None:
            writer.write_string(str(self.business_bot_manage_url or ''))
        if self.charge_paid_message_stars is not None:
            writer.write_int64(self.charge_paid_message_stars or 0)
        if self.registration_month is not None:
            writer.write_string(str(self.registration_month or ''))
        if self.phone_country is not None:
            writer.write_string(str(self.phone_country or ''))
        if self.name_change_date is not None:
            writer.write_int32(self.name_change_date or 0)
        if self.photo_change_date is not None:
            writer.write_int32(self.photo_change_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PeerSettings':
        flags = reader.read_uint32()
        report_spam = bool(flags & (1 << 0))
        add_contact = bool(flags & (1 << 1))
        block_contact = bool(flags & (1 << 2))
        share_contact = bool(flags & (1 << 3))
        need_contacts_exception = bool(flags & (1 << 4))
        report_geo = bool(flags & (1 << 5))
        autoarchived = bool(flags & (1 << 7))
        invite_members = bool(flags & (1 << 8))
        request_chat_broadcast = bool(flags & (1 << 10))
        business_bot_paused = bool(flags & (1 << 11))
        business_bot_can_reply = bool(flags & (1 << 12))
        geo_distance = None
        if flags & (1 << 6):
            geo_distance = reader.read_int32()
        request_chat_title = None
        if flags & (1 << 9):
            request_chat_title = reader.read_string()
        request_chat_date = None
        if flags & (1 << 9):
            request_chat_date = reader.read_int32()
        business_bot_id = None
        if flags & (1 << 13):
            business_bot_id = reader.read_int64()
        business_bot_manage_url = None
        if flags & (1 << 13):
            business_bot_manage_url = reader.read_string()
        charge_paid_message_stars = None
        if flags & (1 << 14):
            charge_paid_message_stars = reader.read_int64()
        registration_month = None
        if flags & (1 << 15):
            registration_month = reader.read_string()
        phone_country = None
        if flags & (1 << 16):
            phone_country = reader.read_string()
        name_change_date = None
        if flags & (1 << 17):
            name_change_date = reader.read_int32()
        photo_change_date = None
        if flags & (1 << 18):
            photo_change_date = reader.read_int32()
        return cls(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact, share_contact=share_contact, need_contacts_exception=need_contacts_exception, report_geo=report_geo, autoarchived=autoarchived, invite_members=invite_members, request_chat_broadcast=request_chat_broadcast, business_bot_paused=business_bot_paused, business_bot_can_reply=business_bot_can_reply, geo_distance=geo_distance, request_chat_title=request_chat_title, request_chat_date=request_chat_date, business_bot_id=business_bot_id, business_bot_manage_url=business_bot_manage_url, charge_paid_message_stars=charge_paid_message_stars, registration_month=registration_month, phone_country=phone_country, name_change_date=name_change_date, photo_change_date=photo_change_date)

@register_tl
class WallPaper(TLObject):
    ID: int = 0xa437c3ed

    def __init__(self, id: Any = None, creator: bool = False, default: bool = False, pattern: bool = False, dark: bool = False, access_hash: Any = None, slug: Any = None, document: Any = None, settings: Any = None) -> None:
        self.id = id
        self.creator = creator
        self.default = default
        self.pattern = pattern
        self.dark = dark
        self.access_hash = access_hash
        self.slug = slug
        self.document = document
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.creator:
            flags |= (1 << 0)
        if self.default:
            flags |= (1 << 1)
        if self.pattern:
            flags |= (1 << 3)
        if self.dark:
            flags |= (1 << 4)
        if self.settings is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_string(str(self.slug or ''))
        if hasattr(self.document, 'write'):
            self.document.write(writer)
        else:
            writer.write_bytes(self.document or b'')
        if self.settings is not None:
            if hasattr(self.settings, 'write'):
                self.settings.write(writer)
            else:
                writer.write_bytes(self.settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'WallPaper':
        flags = reader.read_uint32()
        id = reader.read_int64()
        creator = bool(flags & (1 << 0))
        default = bool(flags & (1 << 1))
        pattern = bool(flags & (1 << 3))
        dark = bool(flags & (1 << 4))
        access_hash = reader.read_int64()
        slug = reader.read_string()
        document = reader.read_object()
        settings = None
        if flags & (1 << 2):
            settings = reader.read_object()
        return cls(id=id, creator=creator, default=default, pattern=pattern, dark=dark, access_hash=access_hash, slug=slug, document=document, settings=settings)

@register_tl
class WallPaperNoFile(TLObject):
    ID: int = 0xe0804116

    def __init__(self, id: Any = None, default: bool = False, dark: bool = False, settings: Any = None) -> None:
        self.id = id
        self.default = default
        self.dark = dark
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.default:
            flags |= (1 << 1)
        if self.dark:
            flags |= (1 << 4)
        if self.settings is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.settings is not None:
            if hasattr(self.settings, 'write'):
                self.settings.write(writer)
            else:
                writer.write_bytes(self.settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'WallPaperNoFile':
        flags = reader.read_uint32()
        id = reader.read_int64()
        default = bool(flags & (1 << 1))
        dark = bool(flags & (1 << 4))
        settings = None
        if flags & (1 << 2):
            settings = reader.read_object()
        return cls(id=id, default=default, dark=dark, settings=settings)

@register_tl
class InputReportReasonSpam(TLObject):
    ID: int = 0x58dbcab8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonSpam':
        return cls()

@register_tl
class InputReportReasonViolence(TLObject):
    ID: int = 0x1e22c78d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonViolence':
        return cls()

@register_tl
class InputReportReasonPornography(TLObject):
    ID: int = 0x2e59d922

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonPornography':
        return cls()

@register_tl
class InputReportReasonChildAbuse(TLObject):
    ID: int = 0xadf44ee3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonChildAbuse':
        return cls()

@register_tl
class InputReportReasonOther(TLObject):
    ID: int = 0xc1e4a2b1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonOther':
        return cls()

@register_tl
class InputReportReasonCopyright(TLObject):
    ID: int = 0x9b89f93a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonCopyright':
        return cls()

@register_tl
class InputReportReasonGeoIrrelevant(TLObject):
    ID: int = 0xdbd4feed

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonGeoIrrelevant':
        return cls()

@register_tl
class InputReportReasonFake(TLObject):
    ID: int = 0xf5ddd6e7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonFake':
        return cls()

@register_tl
class InputReportReasonIllegalDrugs(TLObject):
    ID: int = 0xa8eb2be

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonIllegalDrugs':
        return cls()

@register_tl
class InputReportReasonPersonalDetails(TLObject):
    ID: int = 0x9ec7863d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputReportReasonPersonalDetails':
        return cls()

@register_tl
class UserFull(TLObject):
    ID: int = 0x6cbe645

    def __init__(self, blocked: bool = False, phone_calls_available: bool = False, phone_calls_private: bool = False, can_pin_message: bool = False, has_scheduled: bool = False, video_calls_available: bool = False, voice_messages_forbidden: bool = False, translations_disabled: bool = False, stories_pinned_available: bool = False, blocked_my_stories_from: bool = False, wallpaper_overridden: bool = False, contact_require_premium: bool = False, read_dates_private: bool = False, sponsored_enabled: bool = False, can_view_revenue: bool = False, bot_can_manage_emoji_status: bool = False, display_gifts_button: bool = False, noforwards_my_enabled: bool = False, noforwards_peer_enabled: bool = False, unofficial_security_risk: bool = False, id: Any = None, about: Any = None, settings: Any = None, personal_photo: Any = None, profile_photo: Any = None, fallback_photo: Any = None, notify_settings: Any = None, bot_info: Any = None, pinned_msg_id: Any = None, common_chats_count: Any = None, folder_id: Any = None, ttl_period: Any = None, theme: Any = None, private_forward_name: Any = None, bot_group_admin_rights: Any = None, bot_broadcast_admin_rights: Any = None, wallpaper: Any = None, stories: Any = None, business_work_hours: Any = None, business_location: Any = None, business_greeting_message: Any = None, business_away_message: Any = None, business_intro: Any = None, birthday: Any = None, personal_channel_id: Any = None, personal_channel_message: Any = None, stargifts_count: Any = None, starref_program: Any = None, bot_verification: Any = None, send_paid_messages_stars: Any = None, disallowed_gifts: Any = None, stars_rating: Any = None, stars_my_pending_rating: Any = None, stars_my_pending_rating_date: Any = None, main_tab: Any = None, saved_music: Any = None, note: Any = None, bot_manager_id: Any = None) -> None:
        self.blocked = blocked
        self.phone_calls_available = phone_calls_available
        self.phone_calls_private = phone_calls_private
        self.can_pin_message = can_pin_message
        self.has_scheduled = has_scheduled
        self.video_calls_available = video_calls_available
        self.voice_messages_forbidden = voice_messages_forbidden
        self.translations_disabled = translations_disabled
        self.stories_pinned_available = stories_pinned_available
        self.blocked_my_stories_from = blocked_my_stories_from
        self.wallpaper_overridden = wallpaper_overridden
        self.contact_require_premium = contact_require_premium
        self.read_dates_private = read_dates_private
        self.sponsored_enabled = sponsored_enabled
        self.can_view_revenue = can_view_revenue
        self.bot_can_manage_emoji_status = bot_can_manage_emoji_status
        self.display_gifts_button = display_gifts_button
        self.noforwards_my_enabled = noforwards_my_enabled
        self.noforwards_peer_enabled = noforwards_peer_enabled
        self.unofficial_security_risk = unofficial_security_risk
        self.id = id
        self.about = about
        self.settings = settings
        self.personal_photo = personal_photo
        self.profile_photo = profile_photo
        self.fallback_photo = fallback_photo
        self.notify_settings = notify_settings
        self.bot_info = bot_info
        self.pinned_msg_id = pinned_msg_id
        self.common_chats_count = common_chats_count
        self.folder_id = folder_id
        self.ttl_period = ttl_period
        self.theme = theme
        self.private_forward_name = private_forward_name
        self.bot_group_admin_rights = bot_group_admin_rights
        self.bot_broadcast_admin_rights = bot_broadcast_admin_rights
        self.wallpaper = wallpaper
        self.stories = stories
        self.business_work_hours = business_work_hours
        self.business_location = business_location
        self.business_greeting_message = business_greeting_message
        self.business_away_message = business_away_message
        self.business_intro = business_intro
        self.birthday = birthday
        self.personal_channel_id = personal_channel_id
        self.personal_channel_message = personal_channel_message
        self.stargifts_count = stargifts_count
        self.starref_program = starref_program
        self.bot_verification = bot_verification
        self.send_paid_messages_stars = send_paid_messages_stars
        self.disallowed_gifts = disallowed_gifts
        self.stars_rating = stars_rating
        self.stars_my_pending_rating = stars_my_pending_rating
        self.stars_my_pending_rating_date = stars_my_pending_rating_date
        self.main_tab = main_tab
        self.saved_music = saved_music
        self.note = note
        self.bot_manager_id = bot_manager_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blocked:
            flags |= (1 << 0)
        if self.phone_calls_available:
            flags |= (1 << 4)
        if self.phone_calls_private:
            flags |= (1 << 5)
        if self.can_pin_message:
            flags |= (1 << 7)
        if self.has_scheduled:
            flags |= (1 << 12)
        if self.video_calls_available:
            flags |= (1 << 13)
        if self.voice_messages_forbidden:
            flags |= (1 << 20)
        if self.translations_disabled:
            flags |= (1 << 23)
        if self.stories_pinned_available:
            flags |= (1 << 26)
        if self.blocked_my_stories_from:
            flags |= (1 << 27)
        if self.wallpaper_overridden:
            flags |= (1 << 28)
        if self.contact_require_premium:
            flags |= (1 << 29)
        if self.read_dates_private:
            flags |= (1 << 30)
        if self.sponsored_enabled:
            flags |= (1 << 7)
        if self.can_view_revenue:
            flags |= (1 << 9)
        if self.bot_can_manage_emoji_status:
            flags |= (1 << 10)
        if self.display_gifts_button:
            flags |= (1 << 16)
        if self.noforwards_my_enabled:
            flags |= (1 << 23)
        if self.noforwards_peer_enabled:
            flags |= (1 << 24)
        if self.unofficial_security_risk:
            flags |= (1 << 26)
        if self.about is not None:
            flags |= (1 << 1)
        if self.personal_photo is not None:
            flags |= (1 << 21)
        if self.profile_photo is not None:
            flags |= (1 << 2)
        if self.fallback_photo is not None:
            flags |= (1 << 22)
        if self.bot_info is not None:
            flags |= (1 << 3)
        if self.pinned_msg_id is not None:
            flags |= (1 << 6)
        if self.folder_id is not None:
            flags |= (1 << 11)
        if self.ttl_period is not None:
            flags |= (1 << 14)
        if self.theme is not None:
            flags |= (1 << 15)
        if self.private_forward_name is not None:
            flags |= (1 << 16)
        if self.bot_group_admin_rights is not None:
            flags |= (1 << 17)
        if self.bot_broadcast_admin_rights is not None:
            flags |= (1 << 18)
        if self.wallpaper is not None:
            flags |= (1 << 24)
        if self.stories is not None:
            flags |= (1 << 25)
        if self.business_work_hours is not None:
            flags |= (1 << 0)
        if self.business_location is not None:
            flags |= (1 << 1)
        if self.business_greeting_message is not None:
            flags |= (1 << 2)
        if self.business_away_message is not None:
            flags |= (1 << 3)
        if self.business_intro is not None:
            flags |= (1 << 4)
        if self.birthday is not None:
            flags |= (1 << 5)
        if self.personal_channel_id is not None:
            flags |= (1 << 6)
        if self.personal_channel_message is not None:
            flags |= (1 << 6)
        if self.stargifts_count is not None:
            flags |= (1 << 8)
        if self.starref_program is not None:
            flags |= (1 << 11)
        if self.bot_verification is not None:
            flags |= (1 << 12)
        if self.send_paid_messages_stars is not None:
            flags |= (1 << 14)
        if self.disallowed_gifts is not None:
            flags |= (1 << 15)
        if self.stars_rating is not None:
            flags |= (1 << 17)
        if self.stars_my_pending_rating is not None:
            flags |= (1 << 18)
        if self.stars_my_pending_rating_date is not None:
            flags |= (1 << 18)
        if self.main_tab is not None:
            flags |= (1 << 20)
        if self.saved_music is not None:
            flags |= (1 << 21)
        if self.note is not None:
            flags |= (1 << 22)
        if self.bot_manager_id is not None:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.about is not None:
            writer.write_string(str(self.about or ''))
        if hasattr(self.settings, 'write'):
            self.settings.write(writer)
        else:
            writer.write_bytes(self.settings or b'')
        if self.personal_photo is not None:
            if hasattr(self.personal_photo, 'write'):
                self.personal_photo.write(writer)
            else:
                writer.write_bytes(self.personal_photo or b'')
        if self.profile_photo is not None:
            if hasattr(self.profile_photo, 'write'):
                self.profile_photo.write(writer)
            else:
                writer.write_bytes(self.profile_photo or b'')
        if self.fallback_photo is not None:
            if hasattr(self.fallback_photo, 'write'):
                self.fallback_photo.write(writer)
            else:
                writer.write_bytes(self.fallback_photo or b'')
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')
        if self.bot_info is not None:
            if hasattr(self.bot_info, 'write'):
                self.bot_info.write(writer)
            else:
                writer.write_bytes(self.bot_info or b'')
        if self.pinned_msg_id is not None:
            writer.write_int32(self.pinned_msg_id or 0)
        writer.write_int32(self.common_chats_count or 0)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)
        if self.theme is not None:
            if hasattr(self.theme, 'write'):
                self.theme.write(writer)
            else:
                writer.write_bytes(self.theme or b'')
        if self.private_forward_name is not None:
            writer.write_string(str(self.private_forward_name or ''))
        if self.bot_group_admin_rights is not None:
            if hasattr(self.bot_group_admin_rights, 'write'):
                self.bot_group_admin_rights.write(writer)
            else:
                writer.write_bytes(self.bot_group_admin_rights or b'')
        if self.bot_broadcast_admin_rights is not None:
            if hasattr(self.bot_broadcast_admin_rights, 'write'):
                self.bot_broadcast_admin_rights.write(writer)
            else:
                writer.write_bytes(self.bot_broadcast_admin_rights or b'')
        if self.wallpaper is not None:
            if hasattr(self.wallpaper, 'write'):
                self.wallpaper.write(writer)
            else:
                writer.write_bytes(self.wallpaper or b'')
        if self.stories is not None:
            if hasattr(self.stories, 'write'):
                self.stories.write(writer)
            else:
                writer.write_bytes(self.stories or b'')
        if self.business_work_hours is not None:
            if hasattr(self.business_work_hours, 'write'):
                self.business_work_hours.write(writer)
            else:
                writer.write_bytes(self.business_work_hours or b'')
        if self.business_location is not None:
            if hasattr(self.business_location, 'write'):
                self.business_location.write(writer)
            else:
                writer.write_bytes(self.business_location or b'')
        if self.business_greeting_message is not None:
            if hasattr(self.business_greeting_message, 'write'):
                self.business_greeting_message.write(writer)
            else:
                writer.write_bytes(self.business_greeting_message or b'')
        if self.business_away_message is not None:
            if hasattr(self.business_away_message, 'write'):
                self.business_away_message.write(writer)
            else:
                writer.write_bytes(self.business_away_message or b'')
        if self.business_intro is not None:
            if hasattr(self.business_intro, 'write'):
                self.business_intro.write(writer)
            else:
                writer.write_bytes(self.business_intro or b'')
        if self.birthday is not None:
            if hasattr(self.birthday, 'write'):
                self.birthday.write(writer)
            else:
                writer.write_bytes(self.birthday or b'')
        if self.personal_channel_id is not None:
            writer.write_int64(self.personal_channel_id or 0)
        if self.personal_channel_message is not None:
            writer.write_int32(self.personal_channel_message or 0)
        if self.stargifts_count is not None:
            writer.write_int32(self.stargifts_count or 0)
        if self.starref_program is not None:
            if hasattr(self.starref_program, 'write'):
                self.starref_program.write(writer)
            else:
                writer.write_bytes(self.starref_program or b'')
        if self.bot_verification is not None:
            if hasattr(self.bot_verification, 'write'):
                self.bot_verification.write(writer)
            else:
                writer.write_bytes(self.bot_verification or b'')
        if self.send_paid_messages_stars is not None:
            writer.write_int64(self.send_paid_messages_stars or 0)
        if self.disallowed_gifts is not None:
            if hasattr(self.disallowed_gifts, 'write'):
                self.disallowed_gifts.write(writer)
            else:
                writer.write_bytes(self.disallowed_gifts or b'')
        if self.stars_rating is not None:
            if hasattr(self.stars_rating, 'write'):
                self.stars_rating.write(writer)
            else:
                writer.write_bytes(self.stars_rating or b'')
        if self.stars_my_pending_rating is not None:
            if hasattr(self.stars_my_pending_rating, 'write'):
                self.stars_my_pending_rating.write(writer)
            else:
                writer.write_bytes(self.stars_my_pending_rating or b'')
        if self.stars_my_pending_rating_date is not None:
            writer.write_int32(self.stars_my_pending_rating_date or 0)
        if self.main_tab is not None:
            if hasattr(self.main_tab, 'write'):
                self.main_tab.write(writer)
            else:
                writer.write_bytes(self.main_tab or b'')
        if self.saved_music is not None:
            if hasattr(self.saved_music, 'write'):
                self.saved_music.write(writer)
            else:
                writer.write_bytes(self.saved_music or b'')
        if self.note is not None:
            if hasattr(self.note, 'write'):
                self.note.write(writer)
            else:
                writer.write_bytes(self.note or b'')
        if self.bot_manager_id is not None:
            writer.write_int64(self.bot_manager_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UserFull':
        flags = reader.read_uint32()
        blocked = bool(flags & (1 << 0))
        phone_calls_available = bool(flags & (1 << 4))
        phone_calls_private = bool(flags & (1 << 5))
        can_pin_message = bool(flags & (1 << 7))
        has_scheduled = bool(flags & (1 << 12))
        video_calls_available = bool(flags & (1 << 13))
        voice_messages_forbidden = bool(flags & (1 << 20))
        translations_disabled = bool(flags & (1 << 23))
        stories_pinned_available = bool(flags & (1 << 26))
        blocked_my_stories_from = bool(flags & (1 << 27))
        wallpaper_overridden = bool(flags & (1 << 28))
        contact_require_premium = bool(flags & (1 << 29))
        read_dates_private = bool(flags & (1 << 30))
        sponsored_enabled = bool(flags & (1 << 7))
        can_view_revenue = bool(flags & (1 << 9))
        bot_can_manage_emoji_status = bool(flags & (1 << 10))
        display_gifts_button = bool(flags & (1 << 16))
        noforwards_my_enabled = bool(flags & (1 << 23))
        noforwards_peer_enabled = bool(flags & (1 << 24))
        unofficial_security_risk = bool(flags & (1 << 26))
        id = reader.read_int64()
        about = None
        if flags & (1 << 1):
            about = reader.read_string()
        settings = reader.read_object()
        personal_photo = None
        if flags & (1 << 21):
            personal_photo = reader.read_object()
        profile_photo = None
        if flags & (1 << 2):
            profile_photo = reader.read_object()
        fallback_photo = None
        if flags & (1 << 22):
            fallback_photo = reader.read_object()
        notify_settings = reader.read_object()
        bot_info = None
        if flags & (1 << 3):
            bot_info = reader.read_object()
        pinned_msg_id = None
        if flags & (1 << 6):
            pinned_msg_id = reader.read_int32()
        common_chats_count = reader.read_int32()
        folder_id = None
        if flags & (1 << 11):
            folder_id = reader.read_int32()
        ttl_period = None
        if flags & (1 << 14):
            ttl_period = reader.read_int32()
        theme = None
        if flags & (1 << 15):
            theme = reader.read_object()
        private_forward_name = None
        if flags & (1 << 16):
            private_forward_name = reader.read_string()
        bot_group_admin_rights = None
        if flags & (1 << 17):
            bot_group_admin_rights = reader.read_object()
        bot_broadcast_admin_rights = None
        if flags & (1 << 18):
            bot_broadcast_admin_rights = reader.read_object()
        wallpaper = None
        if flags & (1 << 24):
            wallpaper = reader.read_object()
        stories = None
        if flags & (1 << 25):
            stories = reader.read_object()
        business_work_hours = None
        if flags & (1 << 0):
            business_work_hours = reader.read_object()
        business_location = None
        if flags & (1 << 1):
            business_location = reader.read_object()
        business_greeting_message = None
        if flags & (1 << 2):
            business_greeting_message = reader.read_object()
        business_away_message = None
        if flags & (1 << 3):
            business_away_message = reader.read_object()
        business_intro = None
        if flags & (1 << 4):
            business_intro = reader.read_object()
        birthday = None
        if flags & (1 << 5):
            birthday = reader.read_object()
        personal_channel_id = None
        if flags & (1 << 6):
            personal_channel_id = reader.read_int64()
        personal_channel_message = None
        if flags & (1 << 6):
            personal_channel_message = reader.read_int32()
        stargifts_count = None
        if flags & (1 << 8):
            stargifts_count = reader.read_int32()
        starref_program = None
        if flags & (1 << 11):
            starref_program = reader.read_object()
        bot_verification = None
        if flags & (1 << 12):
            bot_verification = reader.read_object()
        send_paid_messages_stars = None
        if flags & (1 << 14):
            send_paid_messages_stars = reader.read_int64()
        disallowed_gifts = None
        if flags & (1 << 15):
            disallowed_gifts = reader.read_object()
        stars_rating = None
        if flags & (1 << 17):
            stars_rating = reader.read_object()
        stars_my_pending_rating = None
        if flags & (1 << 18):
            stars_my_pending_rating = reader.read_object()
        stars_my_pending_rating_date = None
        if flags & (1 << 18):
            stars_my_pending_rating_date = reader.read_int32()
        main_tab = None
        if flags & (1 << 20):
            main_tab = reader.read_object()
        saved_music = None
        if flags & (1 << 21):
            saved_music = reader.read_object()
        note = None
        if flags & (1 << 22):
            note = reader.read_object()
        bot_manager_id = None
        if flags & (1 << 25):
            bot_manager_id = reader.read_int64()
        return cls(blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, video_calls_available=video_calls_available, voice_messages_forbidden=voice_messages_forbidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, blocked_my_stories_from=blocked_my_stories_from, wallpaper_overridden=wallpaper_overridden, contact_require_premium=contact_require_premium, read_dates_private=read_dates_private, sponsored_enabled=sponsored_enabled, can_view_revenue=can_view_revenue, bot_can_manage_emoji_status=bot_can_manage_emoji_status, display_gifts_button=display_gifts_button, noforwards_my_enabled=noforwards_my_enabled, noforwards_peer_enabled=noforwards_peer_enabled, unofficial_security_risk=unofficial_security_risk, id=id, about=about, settings=settings, personal_photo=personal_photo, profile_photo=profile_photo, fallback_photo=fallback_photo, notify_settings=notify_settings, bot_info=bot_info, pinned_msg_id=pinned_msg_id, common_chats_count=common_chats_count, folder_id=folder_id, ttl_period=ttl_period, theme=theme, private_forward_name=private_forward_name, bot_group_admin_rights=bot_group_admin_rights, bot_broadcast_admin_rights=bot_broadcast_admin_rights, wallpaper=wallpaper, stories=stories, business_work_hours=business_work_hours, business_location=business_location, business_greeting_message=business_greeting_message, business_away_message=business_away_message, business_intro=business_intro, birthday=birthday, personal_channel_id=personal_channel_id, personal_channel_message=personal_channel_message, stargifts_count=stargifts_count, starref_program=starref_program, bot_verification=bot_verification, send_paid_messages_stars=send_paid_messages_stars, disallowed_gifts=disallowed_gifts, stars_rating=stars_rating, stars_my_pending_rating=stars_my_pending_rating, stars_my_pending_rating_date=stars_my_pending_rating_date, main_tab=main_tab, saved_music=saved_music, note=note, bot_manager_id=bot_manager_id)

@register_tl
class Contact(TLObject):
    ID: int = 0x145ade0b

    def __init__(self, user_id: Any = None, mutual: Any = None) -> None:
        self.user_id = user_id
        self.mutual = mutual

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_bool(bool(self.mutual))

    @classmethod
    def read(cls, reader: TLReader) -> 'Contact':
        user_id = reader.read_int64()
        mutual = reader.read_bool()
        return cls(user_id=user_id, mutual=mutual)

@register_tl
class ImportedContact(TLObject):
    ID: int = 0xc13e3c50

    def __init__(self, user_id: Any = None, client_id: Any = None) -> None:
        self.user_id = user_id
        self.client_id = client_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.client_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ImportedContact':
        user_id = reader.read_int64()
        client_id = reader.read_int64()
        return cls(user_id=user_id, client_id=client_id)

@register_tl
class ContactStatus(TLObject):
    ID: int = 0x16d9703b

    def __init__(self, user_id: Any = None, status: Any = None) -> None:
        self.user_id = user_id
        self.status = status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.status, 'write'):
            self.status.write(writer)
        else:
            writer.write_bytes(self.status or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactStatus':
        user_id = reader.read_int64()
        status = reader.read_object()
        return cls(user_id=user_id, status=status)

@register_tl
class ContactsContactsNotModified(TLObject):
    ID: int = 0xb74ba9d2

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsContactsNotModified':
        return cls()

@register_tl
class ContactsContacts(TLObject):
    ID: int = 0xeae87e42

    def __init__(self, contacts: Any = None, saved_count: Any = None, users: Any = None) -> None:
        self.contacts = contacts
        self.saved_count = saved_count
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.contacts or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.saved_count or 0)
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsContacts':
        contacts = reader.read_vector(lambda r: r.read_object())
        saved_count = reader.read_int32()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(contacts=contacts, saved_count=saved_count, users=users)

@register_tl
class ContactsImportedContacts(TLObject):
    ID: int = 0x77d01c3b

    def __init__(self, imported: Any = None, popular_invites: Any = None, retry_contacts: Any = None, users: Any = None) -> None:
        self.imported = imported
        self.popular_invites = popular_invites
        self.retry_contacts = retry_contacts
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.imported or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.popular_invites or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.retry_contacts or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsImportedContacts':
        imported = reader.read_vector(lambda r: r.read_object())
        popular_invites = reader.read_vector(lambda r: r.read_object())
        retry_contacts = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(imported=imported, popular_invites=popular_invites, retry_contacts=retry_contacts, users=users)

@register_tl
class ContactsBlocked(TLObject):
    ID: int = 0xade1591

    def __init__(self, blocked: Any = None, chats: Any = None, users: Any = None) -> None:
        self.blocked = blocked
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.blocked or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlocked':
        blocked = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(blocked=blocked, chats=chats, users=users)

@register_tl
class ContactsBlockedSlice(TLObject):
    ID: int = 0xe1664194

    def __init__(self, count: Any = None, blocked: Any = None, chats: Any = None, users: Any = None) -> None:
        self.count = count
        self.blocked = blocked
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.blocked or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsBlockedSlice':
        count = reader.read_int32()
        blocked = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, blocked=blocked, chats=chats, users=users)

@register_tl
class MessagesDialogs(TLObject):
    ID: int = 0x15ba6c40

    def __init__(self, dialogs: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dialogs or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogs':
        dialogs = reader.read_vector(lambda r: r.read_object())
        messages = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(dialogs=dialogs, messages=messages, chats=chats, users=users)

@register_tl
class MessagesDialogsSlice(TLObject):
    ID: int = 0x71e094f3

    def __init__(self, count: Any = None, dialogs: Any = None, messages: Any = None, chats: Any = None, users: Any = None) -> None:
        self.count = count
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.dialogs or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogsSlice':
        count = reader.read_int32()
        dialogs = reader.read_vector(lambda r: r.read_object())
        messages = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, dialogs=dialogs, messages=messages, chats=chats, users=users)

@register_tl
class MessagesDialogsNotModified(TLObject):
    ID: int = 0xf0e3e596

    def __init__(self, count: Any = None) -> None:
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDialogsNotModified':
        count = reader.read_int32()
        return cls(count=count)

@register_tl
class MessagesMessages(TLObject):
    ID: int = 0x1d73e7ea

    def __init__(self, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.topics or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessages':
        messages = reader.read_vector(lambda r: r.read_object())
        topics = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(messages=messages, topics=topics, chats=chats, users=users)

@register_tl
class MessagesMessagesSlice(TLObject):
    ID: int = 0x5f206716

    def __init__(self, inexact: bool = False, count: Any = None, next_rate: Any = None, offset_id_offset: Any = None, search_flood: Any = None, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.inexact = inexact
        self.count = count
        self.next_rate = next_rate
        self.offset_id_offset = offset_id_offset
        self.search_flood = search_flood
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inexact:
            flags |= (1 << 1)
        if self.next_rate is not None:
            flags |= (1 << 0)
        if self.offset_id_offset is not None:
            flags |= (1 << 2)
        if self.search_flood is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int32(self.count or 0)
        if self.next_rate is not None:
            writer.write_int32(self.next_rate or 0)
        if self.offset_id_offset is not None:
            writer.write_int32(self.offset_id_offset or 0)
        if self.search_flood is not None:
            if hasattr(self.search_flood, 'write'):
                self.search_flood.write(writer)
            else:
                writer.write_bytes(self.search_flood or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.topics or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessagesSlice':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 1))
        count = reader.read_int32()
        next_rate = None
        if flags & (1 << 0):
            next_rate = reader.read_int32()
        offset_id_offset = None
        if flags & (1 << 2):
            offset_id_offset = reader.read_int32()
        search_flood = None
        if flags & (1 << 3):
            search_flood = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        topics = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(inexact=inexact, count=count, next_rate=next_rate, offset_id_offset=offset_id_offset, search_flood=search_flood, messages=messages, topics=topics, chats=chats, users=users)

@register_tl
class MessagesChannelMessages(TLObject):
    ID: int = 0xc776ba4e

    def __init__(self, inexact: bool = False, pts: Any = None, count: Any = None, offset_id_offset: Any = None, messages: Any = None, topics: Any = None, chats: Any = None, users: Any = None) -> None:
        self.inexact = inexact
        self.pts = pts
        self.count = count
        self.offset_id_offset = offset_id_offset
        self.messages = messages
        self.topics = topics
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.inexact:
            flags |= (1 << 1)
        if self.offset_id_offset is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.count or 0)
        if self.offset_id_offset is not None:
            writer.write_int32(self.offset_id_offset or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.topics or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChannelMessages':
        flags = reader.read_uint32()
        inexact = bool(flags & (1 << 1))
        pts = reader.read_int32()
        count = reader.read_int32()
        offset_id_offset = None
        if flags & (1 << 2):
            offset_id_offset = reader.read_int32()
        messages = reader.read_vector(lambda r: r.read_object())
        topics = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(inexact=inexact, pts=pts, count=count, offset_id_offset=offset_id_offset, messages=messages, topics=topics, chats=chats, users=users)

@register_tl
class MessagesMessagesNotModified(TLObject):
    ID: int = 0x74535f21

    def __init__(self, count: Any = None) -> None:
        self.count = count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesMessagesNotModified':
        count = reader.read_int32()
        return cls(count=count)

@register_tl
class MessagesChats(TLObject):
    ID: int = 0x64ff9fd5

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChats':
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(chats=chats)

@register_tl
class MessagesChatsSlice(TLObject):
    ID: int = 0x9cd81144

    def __init__(self, count: Any = None, chats: Any = None) -> None:
        self.count = count
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatsSlice':
        count = reader.read_int32()
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, chats=chats)

@register_tl
class MessagesChatFull(TLObject):
    ID: int = 0xe5d7d19c

    def __init__(self, full_chat: Any = None, chats: Any = None, users: Any = None) -> None:
        self.full_chat = full_chat
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.full_chat, 'write'):
            self.full_chat.write(writer)
        else:
            writer.write_bytes(self.full_chat or b'')
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesChatFull':
        full_chat = reader.read_object()
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(full_chat=full_chat, chats=chats, users=users)

@register_tl
class MessagesAffectedHistory(TLObject):
    ID: int = 0xb45c69d1

    def __init__(self, pts: Any = None, pts_count: Any = None, offset: Any = None) -> None:
        self.pts = pts
        self.pts_count = pts_count
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        writer.write_int32(self.offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAffectedHistory':
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        offset = reader.read_int32()
        return cls(pts=pts, pts_count=pts_count, offset=offset)

@register_tl
class InputMessagesFilterEmpty(TLObject):
    ID: int = 0x57e2f66c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterEmpty':
        return cls()

@register_tl
class InputMessagesFilterPhotos(TLObject):
    ID: int = 0x9609a51c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPhotos':
        return cls()

@register_tl
class InputMessagesFilterVideo(TLObject):
    ID: int = 0x9fc00e65

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterVideo':
        return cls()

@register_tl
class InputMessagesFilterPhotoVideo(TLObject):
    ID: int = 0x56e9f0e4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPhotoVideo':
        return cls()

@register_tl
class InputMessagesFilterDocument(TLObject):
    ID: int = 0x9eddf188

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterDocument':
        return cls()

@register_tl
class InputMessagesFilterUrl(TLObject):
    ID: int = 0x7ef0dd87

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterUrl':
        return cls()

@register_tl
class InputMessagesFilterGif(TLObject):
    ID: int = 0xffc86587

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterGif':
        return cls()

@register_tl
class InputMessagesFilterVoice(TLObject):
    ID: int = 0x50f5c392

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterVoice':
        return cls()

@register_tl
class InputMessagesFilterMusic(TLObject):
    ID: int = 0x3751b49e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterMusic':
        return cls()

@register_tl
class InputMessagesFilterChatPhotos(TLObject):
    ID: int = 0x3a20ecb8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterChatPhotos':
        return cls()

@register_tl
class InputMessagesFilterPhoneCalls(TLObject):
    ID: int = 0x80c99768

    def __init__(self, missed: bool = False) -> None:
        self.missed = missed

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.missed:
            flags |= (1 << 0)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPhoneCalls':
        flags = reader.read_uint32()
        missed = bool(flags & (1 << 0))
        return cls(missed=missed)

@register_tl
class InputMessagesFilterRoundVoice(TLObject):
    ID: int = 0x7a7c17a4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterRoundVoice':
        return cls()

@register_tl
class InputMessagesFilterRoundVideo(TLObject):
    ID: int = 0xb549da53

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterRoundVideo':
        return cls()

@register_tl
class InputMessagesFilterMyMentions(TLObject):
    ID: int = 0xc1f8e69a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterMyMentions':
        return cls()

@register_tl
class InputMessagesFilterGeo(TLObject):
    ID: int = 0xe7026d0d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterGeo':
        return cls()

@register_tl
class InputMessagesFilterContacts(TLObject):
    ID: int = 0xe062db83

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterContacts':
        return cls()

@register_tl
class InputMessagesFilterPinned(TLObject):
    ID: int = 0x1bb00451

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPinned':
        return cls()

@register_tl
class InputMessagesFilterPoll(TLObject):
    ID: int = 0xfa2bc90a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputMessagesFilterPoll':
        return cls()

@register_tl
class UpdateNewMessage(TLObject):
    ID: int = 0x1f2b0afd

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)

@register_tl
class UpdateMessageID(TLObject):
    ID: int = 0x4e90bfd6

    def __init__(self, id: Any = None, random_id: Any = None) -> None:
        self.id = id
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.random_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessageID':
        id = reader.read_int32()
        random_id = reader.read_int64()
        return cls(id=id, random_id=random_id)

@register_tl
class UpdateDeleteMessages(TLObject):
    ID: int = 0xa20db0e5

    def __init__(self, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteMessages':
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(messages=messages, pts=pts, pts_count=pts_count)

@register_tl
class UpdateUserTyping(TLObject):
    ID: int = 0x2a17bf5c

    def __init__(self, user_id: Any = None, top_msg_id: Any = None, action: Any = None) -> None:
        self.user_id = user_id
        self.top_msg_id = top_msg_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserTyping':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        action = reader.read_object()
        return cls(user_id=user_id, top_msg_id=top_msg_id, action=action)

@register_tl
class UpdateChatUserTyping(TLObject):
    ID: int = 0x83487af0

    def __init__(self, chat_id: Any = None, from_id: Any = None, action: Any = None) -> None:
        self.chat_id = chat_id
        self.from_id = from_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        if hasattr(self.from_id, 'write'):
            self.from_id.write(writer)
        else:
            writer.write_bytes(self.from_id or b'')
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatUserTyping':
        chat_id = reader.read_int64()
        from_id = reader.read_object()
        action = reader.read_object()
        return cls(chat_id=chat_id, from_id=from_id, action=action)

@register_tl
class UpdateChatParticipants(TLObject):
    ID: int = 0x7761198

    def __init__(self, participants: Any = None) -> None:
        self.participants = participants

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.participants, 'write'):
            self.participants.write(writer)
        else:
            writer.write_bytes(self.participants or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipants':
        participants = reader.read_object()
        return cls(participants=participants)

@register_tl
class UpdateUserStatus(TLObject):
    ID: int = 0xe5bdf8de

    def __init__(self, user_id: Any = None, status: Any = None) -> None:
        self.user_id = user_id
        self.status = status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.status, 'write'):
            self.status.write(writer)
        else:
            writer.write_bytes(self.status or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserStatus':
        user_id = reader.read_int64()
        status = reader.read_object()
        return cls(user_id=user_id, status=status)

@register_tl
class UpdateUserName(TLObject):
    ID: int = 0xa7848924

    def __init__(self, user_id: Any = None, first_name: Any = None, last_name: Any = None, usernames: Any = None) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.usernames = usernames

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.first_name or ''))
        writer.write_string(str(self.last_name or ''))
        writer.write_vector(self.usernames or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserName':
        user_id = reader.read_int64()
        first_name = reader.read_string()
        last_name = reader.read_string()
        usernames = reader.read_vector(lambda r: r.read_object())
        return cls(user_id=user_id, first_name=first_name, last_name=last_name, usernames=usernames)

@register_tl
class UpdateNewAuthorization(TLObject):
    ID: int = 0x8951abef

    def __init__(self, unconfirmed: bool = False, hash: Any = None, date: Any = None, device: Any = None, location: Any = None) -> None:
        self.unconfirmed = unconfirmed
        self.hash = hash
        self.date = date
        self.device = device
        self.location = location

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unconfirmed:
            flags |= (1 << 0)
        if self.date is not None:
            flags |= (1 << 0)
        if self.device is not None:
            flags |= (1 << 0)
        if self.location is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)
        if self.date is not None:
            writer.write_int32(self.date or 0)
        if self.device is not None:
            writer.write_string(str(self.device or ''))
        if self.location is not None:
            writer.write_string(str(self.location or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewAuthorization':
        flags = reader.read_uint32()
        unconfirmed = bool(flags & (1 << 0))
        hash = reader.read_int64()
        date = None
        if flags & (1 << 0):
            date = reader.read_int32()
        device = None
        if flags & (1 << 0):
            device = reader.read_string()
        location = None
        if flags & (1 << 0):
            location = reader.read_string()
        return cls(unconfirmed=unconfirmed, hash=hash, date=date, device=device, location=location)

@register_tl
class UpdateNewEncryptedMessage(TLObject):
    ID: int = 0x12bcbd9a

    def __init__(self, message: Any = None, qts: Any = None) -> None:
        self.message = message
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewEncryptedMessage':
        message = reader.read_object()
        qts = reader.read_int32()
        return cls(message=message, qts=qts)

@register_tl
class UpdateEncryptedChatTyping(TLObject):
    ID: int = 0x1710f156

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryptedChatTyping':
        chat_id = reader.read_int32()
        return cls(chat_id=chat_id)

@register_tl
class UpdateEncryption(TLObject):
    ID: int = 0xb4a2e88d

    def __init__(self, chat: Any = None, date: Any = None) -> None:
        self.chat = chat
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.chat, 'write'):
            self.chat.write(writer)
        else:
            writer.write_bytes(self.chat or b'')
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryption':
        chat = reader.read_object()
        date = reader.read_int32()
        return cls(chat=chat, date=date)

@register_tl
class UpdateEncryptedMessagesRead(TLObject):
    ID: int = 0x38fe25b7

    def __init__(self, chat_id: Any = None, max_date: Any = None, date: Any = None) -> None:
        self.chat_id = chat_id
        self.max_date = max_date
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.chat_id or 0)
        writer.write_int32(self.max_date or 0)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEncryptedMessagesRead':
        chat_id = reader.read_int32()
        max_date = reader.read_int32()
        date = reader.read_int32()
        return cls(chat_id=chat_id, max_date=max_date, date=date)

@register_tl
class UpdateChatParticipantAdd(TLObject):
    ID: int = 0x3dda5451

    def __init__(self, chat_id: Any = None, user_id: Any = None, inviter_id: Any = None, date: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.inviter_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantAdd':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        inviter_id = reader.read_int64()
        date = reader.read_int32()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, inviter_id=inviter_id, date=date, version=version)

@register_tl
class UpdateChatParticipantDelete(TLObject):
    ID: int = 0xe32f3d77

    def __init__(self, chat_id: Any = None, user_id: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantDelete':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, version=version)

@register_tl
class UpdateDcOptions(TLObject):
    ID: int = 0x8e5e9873

    def __init__(self, dc_options: Any = None) -> None:
        self.dc_options = dc_options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.dc_options or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDcOptions':
        dc_options = reader.read_vector(lambda r: r.read_object())
        return cls(dc_options=dc_options)

@register_tl
class UpdateNotifySettings(TLObject):
    ID: int = 0xbec268ef

    def __init__(self, peer: Any = None, notify_settings: Any = None) -> None:
        self.peer = peer
        self.notify_settings = notify_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.notify_settings, 'write'):
            self.notify_settings.write(writer)
        else:
            writer.write_bytes(self.notify_settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNotifySettings':
        peer = reader.read_object()
        notify_settings = reader.read_object()
        return cls(peer=peer, notify_settings=notify_settings)

@register_tl
class UpdateServiceNotification(TLObject):
    ID: int = 0xebe46819

    def __init__(self, popup: bool = False, invert_media: bool = False, inbox_date: Any = None, type: Any = None, message: Any = None, media: Any = None, entities: Any = None) -> None:
        self.popup = popup
        self.invert_media = invert_media
        self.inbox_date = inbox_date
        self.type = type
        self.message = message
        self.media = media
        self.entities = entities

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.popup:
            flags |= (1 << 0)
        if self.invert_media:
            flags |= (1 << 2)
        if self.inbox_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.inbox_date is not None:
            writer.write_int32(self.inbox_date or 0)
        writer.write_string(str(self.type or ''))
        writer.write_string(str(self.message or ''))
        if hasattr(self.media, 'write'):
            self.media.write(writer)
        else:
            writer.write_bytes(self.media or b'')
        writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateServiceNotification':
        flags = reader.read_uint32()
        popup = bool(flags & (1 << 0))
        invert_media = bool(flags & (1 << 2))
        inbox_date = None
        if flags & (1 << 1):
            inbox_date = reader.read_int32()
        type = reader.read_string()
        message = reader.read_string()
        media = reader.read_object()
        entities = reader.read_vector(lambda r: r.read_object())
        return cls(popup=popup, invert_media=invert_media, inbox_date=inbox_date, type=type, message=message, media=media, entities=entities)

@register_tl
class UpdatePrivacy(TLObject):
    ID: int = 0xee3b272a

    def __init__(self, key: Any = None, rules: Any = None) -> None:
        self.key = key
        self.rules = rules

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.key, 'write'):
            self.key.write(writer)
        else:
            writer.write_bytes(self.key or b'')
        writer.write_vector(self.rules or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePrivacy':
        key = reader.read_object()
        rules = reader.read_vector(lambda r: r.read_object())
        return cls(key=key, rules=rules)

@register_tl
class UpdateUserPhone(TLObject):
    ID: int = 0x5492a13

    def __init__(self, user_id: Any = None, phone: Any = None) -> None:
        self.user_id = user_id
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.phone or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserPhone':
        user_id = reader.read_int64()
        phone = reader.read_string()
        return cls(user_id=user_id, phone=phone)

@register_tl
class UpdateReadHistoryInbox(TLObject):
    ID: int = 0x9e84bc99

    def __init__(self, folder_id: Any = None, peer: Any = None, top_msg_id: Any = None, max_id: Any = None, still_unread_count: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.folder_id = folder_id
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.max_id = max_id
        self.still_unread_count = still_unread_count
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 0)
        if self.top_msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.still_unread_count or 0)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadHistoryInbox':
        flags = reader.read_uint32()
        folder_id = None
        if flags & (1 << 0):
            folder_id = reader.read_int32()
        peer = reader.read_object()
        top_msg_id = None
        if flags & (1 << 1):
            top_msg_id = reader.read_int32()
        max_id = reader.read_int32()
        still_unread_count = reader.read_int32()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(folder_id=folder_id, peer=peer, top_msg_id=top_msg_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts, pts_count=pts_count)

@register_tl
class UpdateReadHistoryOutbox(TLObject):
    ID: int = 0x2f2f21bf

    def __init__(self, peer: Any = None, max_id: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.peer = peer
        self.max_id = max_id
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadHistoryOutbox':
        peer = reader.read_object()
        max_id = reader.read_int32()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(peer=peer, max_id=max_id, pts=pts, pts_count=pts_count)

@register_tl
class UpdateWebPage(TLObject):
    ID: int = 0x7f891213

    def __init__(self, webpage: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.webpage, 'write'):
            self.webpage.write(writer)
        else:
            writer.write_bytes(self.webpage or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateWebPage':
        webpage = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(webpage=webpage, pts=pts, pts_count=pts_count)

@register_tl
class UpdateReadMessagesContents(TLObject):
    ID: int = 0xf8227181

    def __init__(self, messages: Any = None, pts: Any = None, pts_count: Any = None, date: Any = None) -> None:
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.date is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        if self.date is not None:
            writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadMessagesContents':
        flags = reader.read_uint32()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        date = None
        if flags & (1 << 0):
            date = reader.read_int32()
        return cls(messages=messages, pts=pts, pts_count=pts_count, date=date)

@register_tl
class UpdateChannelTooLong(TLObject):
    ID: int = 0x108d941f

    def __init__(self, channel_id: Any = None, pts: Any = None) -> None:
        self.channel_id = channel_id
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pts is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.pts is not None:
            writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelTooLong':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        pts = None
        if flags & (1 << 0):
            pts = reader.read_int32()
        return cls(channel_id=channel_id, pts=pts)

@register_tl
class UpdateChannel(TLObject):
    ID: int = 0x635b4c09

    def __init__(self, channel_id: Any = None) -> None:
        self.channel_id = channel_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannel':
        channel_id = reader.read_int64()
        return cls(channel_id=channel_id)

@register_tl
class UpdateNewChannelMessage(TLObject):
    ID: int = 0x62ba04d9

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewChannelMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)

@register_tl
class UpdateReadChannelInbox(TLObject):
    ID: int = 0x922e6e10

    def __init__(self, folder_id: Any = None, channel_id: Any = None, max_id: Any = None, still_unread_count: Any = None, pts: Any = None) -> None:
        self.folder_id = folder_id
        self.channel_id = channel_id
        self.max_id = max_id
        self.still_unread_count = still_unread_count
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.still_unread_count or 0)
        writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelInbox':
        flags = reader.read_uint32()
        folder_id = None
        if flags & (1 << 0):
            folder_id = reader.read_int32()
        channel_id = reader.read_int64()
        max_id = reader.read_int32()
        still_unread_count = reader.read_int32()
        pts = reader.read_int32()
        return cls(folder_id=folder_id, channel_id=channel_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts)

@register_tl
class UpdateDeleteChannelMessages(TLObject):
    ID: int = 0xc32d5b12

    def __init__(self, channel_id: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.channel_id = channel_id
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteChannelMessages':
        channel_id = reader.read_int64()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count)

@register_tl
class UpdateChannelMessageViews(TLObject):
    ID: int = 0xf226ac08

    def __init__(self, channel_id: Any = None, id: Any = None, views: Any = None) -> None:
        self.channel_id = channel_id
        self.id = id
        self.views = views

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.views or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelMessageViews':
        channel_id = reader.read_int64()
        id = reader.read_int32()
        views = reader.read_int32()
        return cls(channel_id=channel_id, id=id, views=views)

@register_tl
class UpdateChatParticipantAdmin(TLObject):
    ID: int = 0xd7ca61a2

    def __init__(self, chat_id: Any = None, user_id: Any = None, is_admin: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_admin = is_admin
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bool(bool(self.is_admin))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantAdmin':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        is_admin = reader.read_bool()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, is_admin=is_admin, version=version)

@register_tl
class UpdateNewStickerSet(TLObject):
    ID: int = 0x688a30aa

    def __init__(self, stickerset: Any = None) -> None:
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.stickerset, 'write'):
            self.stickerset.write(writer)
        else:
            writer.write_bytes(self.stickerset or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewStickerSet':
        stickerset = reader.read_object()
        return cls(stickerset=stickerset)

@register_tl
class UpdateStickerSetsOrder(TLObject):
    ID: int = 0xbb2d201

    def __init__(self, masks: bool = False, emojis: bool = False, order: Any = None) -> None:
        self.masks = masks
        self.emojis = emojis
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStickerSetsOrder':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        order = reader.read_vector(lambda r: r.read_object())
        return cls(masks=masks, emojis=emojis, order=order)

@register_tl
class UpdateStickerSets(TLObject):
    ID: int = 0x31c24808

    def __init__(self, masks: bool = False, emojis: bool = False) -> None:
        self.masks = masks
        self.emojis = emojis

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStickerSets':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        return cls(masks=masks, emojis=emojis)

@register_tl
class UpdateSavedGifs(TLObject):
    ID: int = 0x9375341e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSavedGifs':
        return cls()

@register_tl
class UpdateBotInlineQuery(TLObject):
    ID: int = 0x496f379c

    def __init__(self, query_id: Any = None, user_id: Any = None, query: Any = None, geo: Any = None, peer_type: Any = None, offset: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.query = query
        self.geo = geo
        self.peer_type = peer_type
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo is not None:
            flags |= (1 << 0)
        if self.peer_type is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.query or ''))
        if self.geo is not None:
            if hasattr(self.geo, 'write'):
                self.geo.write(writer)
            else:
                writer.write_bytes(self.geo or b'')
        if self.peer_type is not None:
            if hasattr(self.peer_type, 'write'):
                self.peer_type.write(writer)
            else:
                writer.write_bytes(self.peer_type or b'')
        writer.write_string(str(self.offset or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotInlineQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        query = reader.read_string()
        geo = None
        if flags & (1 << 0):
            geo = reader.read_object()
        peer_type = None
        if flags & (1 << 1):
            peer_type = reader.read_object()
        offset = reader.read_string()
        return cls(query_id=query_id, user_id=user_id, query=query, geo=geo, peer_type=peer_type, offset=offset)

@register_tl
class UpdateBotInlineSend(TLObject):
    ID: int = 0x12f12a07

    def __init__(self, user_id: Any = None, query: Any = None, geo: Any = None, id: Any = None, msg_id: Any = None) -> None:
        self.user_id = user_id
        self.query = query
        self.geo = geo
        self.id = id
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.geo is not None:
            flags |= (1 << 0)
        if self.msg_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.query or ''))
        if self.geo is not None:
            if hasattr(self.geo, 'write'):
                self.geo.write(writer)
            else:
                writer.write_bytes(self.geo or b'')
        writer.write_string(str(self.id or ''))
        if self.msg_id is not None:
            if hasattr(self.msg_id, 'write'):
                self.msg_id.write(writer)
            else:
                writer.write_bytes(self.msg_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotInlineSend':
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        query = reader.read_string()
        geo = None
        if flags & (1 << 0):
            geo = reader.read_object()
        id = reader.read_string()
        msg_id = None
        if flags & (1 << 1):
            msg_id = reader.read_object()
        return cls(user_id=user_id, query=query, geo=geo, id=id, msg_id=msg_id)

@register_tl
class UpdateEditChannelMessage(TLObject):
    ID: int = 0x1b3f4df7

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEditChannelMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)

@register_tl
class UpdateBotCallbackQuery(TLObject):
    ID: int = 0xb9cfc48d

    def __init__(self, query_id: Any = None, user_id: Any = None, peer: Any = None, msg_id: Any = None, chat_instance: Any = None, data: Any = None, game_short_name: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.peer = peer
        self.msg_id = msg_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.game_short_name is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.chat_instance or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')
        if self.game_short_name is not None:
            writer.write_string(str(self.game_short_name or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotCallbackQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        peer = reader.read_object()
        msg_id = reader.read_int32()
        chat_instance = reader.read_int64()
        data = None
        if flags & (1 << 0):
            data = reader.read_bytes()
        game_short_name = None
        if flags & (1 << 1):
            game_short_name = reader.read_string()
        return cls(query_id=query_id, user_id=user_id, peer=peer, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)

@register_tl
class UpdateEditMessage(TLObject):
    ID: int = 0xe40370a3

    def __init__(self, message: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.message = message
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEditMessage':
        message = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(message=message, pts=pts, pts_count=pts_count)

@register_tl
class UpdateInlineBotCallbackQuery(TLObject):
    ID: int = 0x691e9052

    def __init__(self, query_id: Any = None, user_id: Any = None, msg_id: Any = None, chat_instance: Any = None, data: Any = None, game_short_name: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.msg_id = msg_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.data is not None:
            flags |= (1 << 0)
        if self.game_short_name is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.msg_id, 'write'):
            self.msg_id.write(writer)
        else:
            writer.write_bytes(self.msg_id or b'')
        writer.write_int64(self.chat_instance or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')
        if self.game_short_name is not None:
            writer.write_string(str(self.game_short_name or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateInlineBotCallbackQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        msg_id = reader.read_object()
        chat_instance = reader.read_int64()
        data = None
        if flags & (1 << 0):
            data = reader.read_bytes()
        game_short_name = None
        if flags & (1 << 1):
            game_short_name = reader.read_string()
        return cls(query_id=query_id, user_id=user_id, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)

@register_tl
class UpdateReadChannelOutbox(TLObject):
    ID: int = 0xb75f99a9

    def __init__(self, channel_id: Any = None, max_id: Any = None) -> None:
        self.channel_id = channel_id
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelOutbox':
        channel_id = reader.read_int64()
        max_id = reader.read_int32()
        return cls(channel_id=channel_id, max_id=max_id)

@register_tl
class UpdateDraftMessage(TLObject):
    ID: int = 0xedfc111e

    def __init__(self, peer: Any = None, top_msg_id: Any = None, saved_peer_id: Any = None, draft: Any = None) -> None:
        self.peer = peer
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.draft = draft

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if hasattr(self.draft, 'write'):
            self.draft.write(writer)
        else:
            writer.write_bytes(self.draft or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDraftMessage':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        draft = reader.read_object()
        return cls(peer=peer, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, draft=draft)

@register_tl
class UpdateReadFeaturedStickers(TLObject):
    ID: int = 0x571d2742

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadFeaturedStickers':
        return cls()

@register_tl
class UpdateRecentStickers(TLObject):
    ID: int = 0x9a422c20

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateRecentStickers':
        return cls()

@register_tl
class UpdateConfig(TLObject):
    ID: int = 0xa229dd06

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateConfig':
        return cls()

@register_tl
class UpdatePtsChanged(TLObject):
    ID: int = 0x3354678f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePtsChanged':
        return cls()

@register_tl
class UpdateChannelWebPage(TLObject):
    ID: int = 0x2f2ba99f

    def __init__(self, channel_id: Any = None, webpage: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.channel_id = channel_id
        self.webpage = webpage
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        if hasattr(self.webpage, 'write'):
            self.webpage.write(writer)
        else:
            writer.write_bytes(self.webpage or b'')
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelWebPage':
        channel_id = reader.read_int64()
        webpage = reader.read_object()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(channel_id=channel_id, webpage=webpage, pts=pts, pts_count=pts_count)

@register_tl
class UpdateDialogPinned(TLObject):
    ID: int = 0x6e6fe51c

    def __init__(self, pinned: bool = False, folder_id: Any = None, peer: Any = None) -> None:
        self.pinned = pinned
        self.folder_id = folder_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        if self.folder_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogPinned':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        folder_id = None
        if flags & (1 << 1):
            folder_id = reader.read_int32()
        peer = reader.read_object()
        return cls(pinned=pinned, folder_id=folder_id, peer=peer)

@register_tl
class UpdatePinnedDialogs(TLObject):
    ID: int = 0xfa0f3ca2

    def __init__(self, folder_id: Any = None, order: Any = None) -> None:
        self.folder_id = folder_id
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 1)
        if self.order is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        if self.order is not None:
            writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedDialogs':
        flags = reader.read_uint32()
        folder_id = None
        if flags & (1 << 1):
            folder_id = reader.read_int32()
        order = None
        if flags & (1 << 0):
            order = reader.read_vector(lambda r: r.read_object())
        return cls(folder_id=folder_id, order=order)

@register_tl
class UpdateBotWebhookJSON(TLObject):
    ID: int = 0x8317c0c3

    def __init__(self, data: Any = None) -> None:
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.data, 'write'):
            self.data.write(writer)
        else:
            writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotWebhookJSON':
        data = reader.read_object()
        return cls(data=data)

@register_tl
class UpdateBotWebhookJSONQuery(TLObject):
    ID: int = 0x9b9240a6

    def __init__(self, query_id: Any = None, data: Any = None, timeout: Any = None) -> None:
        self.query_id = query_id
        self.data = data
        self.timeout = timeout

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        if hasattr(self.data, 'write'):
            self.data.write(writer)
        else:
            writer.write_bytes(self.data or b'')
        writer.write_int32(self.timeout or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotWebhookJSONQuery':
        query_id = reader.read_int64()
        data = reader.read_object()
        timeout = reader.read_int32()
        return cls(query_id=query_id, data=data, timeout=timeout)

@register_tl
class UpdateBotShippingQuery(TLObject):
    ID: int = 0xb5aefd7d

    def __init__(self, query_id: Any = None, user_id: Any = None, payload: Any = None, shipping_address: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.payload = payload
        self.shipping_address = shipping_address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bytes(self.payload or b'')
        if hasattr(self.shipping_address, 'write'):
            self.shipping_address.write(writer)
        else:
            writer.write_bytes(self.shipping_address or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotShippingQuery':
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        payload = reader.read_bytes()
        shipping_address = reader.read_object()
        return cls(query_id=query_id, user_id=user_id, payload=payload, shipping_address=shipping_address)

@register_tl
class UpdateBotPrecheckoutQuery(TLObject):
    ID: int = 0x8caa9a96

    def __init__(self, query_id: Any = None, user_id: Any = None, payload: Any = None, info: Any = None, shipping_option_id: Any = None, currency: Any = None, total_amount: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.payload = payload
        self.info = info
        self.shipping_option_id = shipping_option_id
        self.currency = currency
        self.total_amount = total_amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.info is not None:
            flags |= (1 << 0)
        if self.shipping_option_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_bytes(self.payload or b'')
        if self.info is not None:
            if hasattr(self.info, 'write'):
                self.info.write(writer)
            else:
                writer.write_bytes(self.info or b'')
        if self.shipping_option_id is not None:
            writer.write_string(str(self.shipping_option_id or ''))
        writer.write_string(str(self.currency or ''))
        writer.write_int64(self.total_amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotPrecheckoutQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        payload = reader.read_bytes()
        info = None
        if flags & (1 << 0):
            info = reader.read_object()
        shipping_option_id = None
        if flags & (1 << 1):
            shipping_option_id = reader.read_string()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        return cls(query_id=query_id, user_id=user_id, payload=payload, info=info, shipping_option_id=shipping_option_id, currency=currency, total_amount=total_amount)

@register_tl
class UpdatePhoneCall(TLObject):
    ID: int = 0xab0f6b1e

    def __init__(self, phone_call: Any = None) -> None:
        self.phone_call = phone_call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.phone_call, 'write'):
            self.phone_call.write(writer)
        else:
            writer.write_bytes(self.phone_call or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePhoneCall':
        phone_call = reader.read_object()
        return cls(phone_call=phone_call)

@register_tl
class UpdateLangPackTooLong(TLObject):
    ID: int = 0x46560264

    def __init__(self, lang_code: Any = None) -> None:
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.lang_code or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLangPackTooLong':
        lang_code = reader.read_string()
        return cls(lang_code=lang_code)

@register_tl
class UpdateLangPack(TLObject):
    ID: int = 0x56022f4d

    def __init__(self, difference: Any = None) -> None:
        self.difference = difference

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.difference, 'write'):
            self.difference.write(writer)
        else:
            writer.write_bytes(self.difference or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLangPack':
        difference = reader.read_object()
        return cls(difference=difference)

@register_tl
class UpdateFavedStickers(TLObject):
    ID: int = 0xe511996d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateFavedStickers':
        return cls()

@register_tl
class UpdateChannelReadMessagesContents(TLObject):
    ID: int = 0x25f324f7

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, saved_peer_id: Any = None, messages: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelReadMessagesContents':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, messages=messages)

@register_tl
class UpdateContactsReset(TLObject):
    ID: int = 0x7084a7be

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateContactsReset':
        return cls()

@register_tl
class UpdateChannelAvailableMessages(TLObject):
    ID: int = 0xb23fc698

    def __init__(self, channel_id: Any = None, available_min_id: Any = None) -> None:
        self.channel_id = channel_id
        self.available_min_id = available_min_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.available_min_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelAvailableMessages':
        channel_id = reader.read_int64()
        available_min_id = reader.read_int32()
        return cls(channel_id=channel_id, available_min_id=available_min_id)

@register_tl
class UpdateDialogUnreadMark(TLObject):
    ID: int = 0xb658f23e

    def __init__(self, unread: bool = False, peer: Any = None, saved_peer_id: Any = None) -> None:
        self.unread = unread
        self.peer = peer
        self.saved_peer_id = saved_peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.unread:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogUnreadMark':
        flags = reader.read_uint32()
        unread = bool(flags & (1 << 0))
        peer = reader.read_object()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        return cls(unread=unread, peer=peer, saved_peer_id=saved_peer_id)

@register_tl
class UpdateMessagePoll(TLObject):
    ID: int = 0xd64c522b

    def __init__(self, peer: Any = None, msg_id: Any = None, top_msg_id: Any = None, poll_id: Any = None, poll: Any = None, results: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.top_msg_id = top_msg_id
        self.poll_id = poll_id
        self.poll = poll
        self.results = results

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.peer is not None:
            flags |= (1 << 1)
        if self.msg_id is not None:
            flags |= (1 << 1)
        if self.top_msg_id is not None:
            flags |= (1 << 2)
        if self.poll is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if self.msg_id is not None:
            writer.write_int32(self.msg_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int64(self.poll_id or 0)
        if self.poll is not None:
            if hasattr(self.poll, 'write'):
                self.poll.write(writer)
            else:
                writer.write_bytes(self.poll or b'')
        if hasattr(self.results, 'write'):
            self.results.write(writer)
        else:
            writer.write_bytes(self.results or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessagePoll':
        flags = reader.read_uint32()
        peer = None
        if flags & (1 << 1):
            peer = reader.read_object()
        msg_id = None
        if flags & (1 << 1):
            msg_id = reader.read_int32()
        top_msg_id = None
        if flags & (1 << 2):
            top_msg_id = reader.read_int32()
        poll_id = reader.read_int64()
        poll = None
        if flags & (1 << 0):
            poll = reader.read_object()
        results = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, top_msg_id=top_msg_id, poll_id=poll_id, poll=poll, results=results)

@register_tl
class UpdateChatDefaultBannedRights(TLObject):
    ID: int = 0x54c01850

    def __init__(self, peer: Any = None, default_banned_rights: Any = None, version: Any = None) -> None:
        self.peer = peer
        self.default_banned_rights = default_banned_rights
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.default_banned_rights, 'write'):
            self.default_banned_rights.write(writer)
        else:
            writer.write_bytes(self.default_banned_rights or b'')
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatDefaultBannedRights':
        peer = reader.read_object()
        default_banned_rights = reader.read_object()
        version = reader.read_int32()
        return cls(peer=peer, default_banned_rights=default_banned_rights, version=version)

@register_tl
class UpdateFolderPeers(TLObject):
    ID: int = 0x19360dc0

    def __init__(self, folder_peers: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.folder_peers = folder_peers
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.folder_peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateFolderPeers':
        folder_peers = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(folder_peers=folder_peers, pts=pts, pts_count=pts_count)

@register_tl
class UpdatePeerSettings(TLObject):
    ID: int = 0x6a7e7366

    def __init__(self, peer: Any = None, settings: Any = None) -> None:
        self.peer = peer
        self.settings = settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.settings, 'write'):
            self.settings.write(writer)
        else:
            writer.write_bytes(self.settings or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerSettings':
        peer = reader.read_object()
        settings = reader.read_object()
        return cls(peer=peer, settings=settings)

@register_tl
class UpdatePeerLocated(TLObject):
    ID: int = 0xb4afcfb0

    def __init__(self, peers: Any = None) -> None:
        self.peers = peers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.peers or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerLocated':
        peers = reader.read_vector(lambda r: r.read_object())
        return cls(peers=peers)

@register_tl
class UpdateNewScheduledMessage(TLObject):
    ID: int = 0x39a51dfb

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewScheduledMessage':
        message = reader.read_object()
        return cls(message=message)

@register_tl
class UpdateDeleteScheduledMessages(TLObject):
    ID: int = 0xf2a71983

    def __init__(self, peer: Any = None, messages: Any = None, sent_messages: Any = None) -> None:
        self.peer = peer
        self.messages = messages
        self.sent_messages = sent_messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.sent_messages is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.sent_messages is not None:
            writer.write_vector(self.sent_messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteScheduledMessages':
        flags = reader.read_uint32()
        peer = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        sent_messages = None
        if flags & (1 << 0):
            sent_messages = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, messages=messages, sent_messages=sent_messages)

@register_tl
class UpdateTheme(TLObject):
    ID: int = 0x8216fba3

    def __init__(self, theme: Any = None) -> None:
        self.theme = theme

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.theme, 'write'):
            self.theme.write(writer)
        else:
            writer.write_bytes(self.theme or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateTheme':
        theme = reader.read_object()
        return cls(theme=theme)

@register_tl
class UpdateGeoLiveViewed(TLObject):
    ID: int = 0x871fb939

    def __init__(self, peer: Any = None, msg_id: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGeoLiveViewed':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id)

@register_tl
class UpdateLoginToken(TLObject):
    ID: int = 0x564fe691

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateLoginToken':
        return cls()

@register_tl
class UpdateMessagePollVote(TLObject):
    ID: int = 0x7699f014

    def __init__(self, poll_id: Any = None, peer: Any = None, options: Any = None, positions: Any = None, qts: Any = None) -> None:
        self.poll_id = poll_id
        self.peer = peer
        self.options = options
        self.positions = positions
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.poll_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_vector(self.options or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.positions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessagePollVote':
        poll_id = reader.read_int64()
        peer = reader.read_object()
        options = reader.read_vector(lambda r: r.read_object())
        positions = reader.read_vector(lambda r: r.read_object())
        qts = reader.read_int32()
        return cls(poll_id=poll_id, peer=peer, options=options, positions=positions, qts=qts)

@register_tl
class UpdateDialogFilter(TLObject):
    ID: int = 0x26ffde7d

    def __init__(self, id: Any = None, filter: Any = None) -> None:
        self.id = id
        self.filter = filter

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.filter is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        if self.filter is not None:
            if hasattr(self.filter, 'write'):
                self.filter.write(writer)
            else:
                writer.write_bytes(self.filter or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilter':
        flags = reader.read_uint32()
        id = reader.read_int32()
        filter = None
        if flags & (1 << 0):
            filter = reader.read_object()
        return cls(id=id, filter=filter)

@register_tl
class UpdateDialogFilterOrder(TLObject):
    ID: int = 0xa5d72105

    def __init__(self, order: Any = None) -> None:
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilterOrder':
        order = reader.read_vector(lambda r: r.read_object())
        return cls(order=order)

@register_tl
class UpdateDialogFilters(TLObject):
    ID: int = 0x3504914f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDialogFilters':
        return cls()

@register_tl
class UpdatePhoneCallSignalingData(TLObject):
    ID: int = 0x2661bf09

    def __init__(self, phone_call_id: Any = None, data: Any = None) -> None:
        self.phone_call_id = phone_call_id
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.phone_call_id or 0)
        writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePhoneCallSignalingData':
        phone_call_id = reader.read_int64()
        data = reader.read_bytes()
        return cls(phone_call_id=phone_call_id, data=data)

@register_tl
class UpdateChannelMessageForwards(TLObject):
    ID: int = 0xd29a27f4

    def __init__(self, channel_id: Any = None, id: Any = None, forwards: Any = None) -> None:
        self.channel_id = channel_id
        self.id = id
        self.forwards = forwards

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.forwards or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelMessageForwards':
        channel_id = reader.read_int64()
        id = reader.read_int32()
        forwards = reader.read_int32()
        return cls(channel_id=channel_id, id=id, forwards=forwards)

@register_tl
class UpdateReadChannelDiscussionInbox(TLObject):
    ID: int = 0xd6b19546

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, read_max_id: Any = None, broadcast_id: Any = None, broadcast_post: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.read_max_id = read_max_id
        self.broadcast_id = broadcast_id
        self.broadcast_post = broadcast_post

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast_id is not None:
            flags |= (1 << 0)
        if self.broadcast_post is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.read_max_id or 0)
        if self.broadcast_id is not None:
            writer.write_int64(self.broadcast_id or 0)
        if self.broadcast_post is not None:
            writer.write_int32(self.broadcast_post or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelDiscussionInbox':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        top_msg_id = reader.read_int32()
        read_max_id = reader.read_int32()
        broadcast_id = None
        if flags & (1 << 0):
            broadcast_id = reader.read_int64()
        broadcast_post = None
        if flags & (1 << 0):
            broadcast_post = reader.read_int32()
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, read_max_id=read_max_id, broadcast_id=broadcast_id, broadcast_post=broadcast_post)

@register_tl
class UpdateReadChannelDiscussionOutbox(TLObject):
    ID: int = 0x695c9e7c

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, read_max_id: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.read_max_id = read_max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.read_max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadChannelDiscussionOutbox':
        channel_id = reader.read_int64()
        top_msg_id = reader.read_int32()
        read_max_id = reader.read_int32()
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, read_max_id=read_max_id)

@register_tl
class UpdatePeerBlocked(TLObject):
    ID: int = 0xebe07752

    def __init__(self, blocked: bool = False, blocked_my_stories_from: bool = False, peer_id: Any = None) -> None:
        self.blocked = blocked
        self.blocked_my_stories_from = blocked_my_stories_from
        self.peer_id = peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.blocked:
            flags |= (1 << 0)
        if self.blocked_my_stories_from:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer_id, 'write'):
            self.peer_id.write(writer)
        else:
            writer.write_bytes(self.peer_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerBlocked':
        flags = reader.read_uint32()
        blocked = bool(flags & (1 << 0))
        blocked_my_stories_from = bool(flags & (1 << 1))
        peer_id = reader.read_object()
        return cls(blocked=blocked, blocked_my_stories_from=blocked_my_stories_from, peer_id=peer_id)

@register_tl
class UpdateChannelUserTyping(TLObject):
    ID: int = 0x8c88c923

    def __init__(self, channel_id: Any = None, top_msg_id: Any = None, from_id: Any = None, action: Any = None) -> None:
        self.channel_id = channel_id
        self.top_msg_id = top_msg_id
        self.from_id = from_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if hasattr(self.from_id, 'write'):
            self.from_id.write(writer)
        else:
            writer.write_bytes(self.from_id or b'')
        if hasattr(self.action, 'write'):
            self.action.write(writer)
        else:
            writer.write_bytes(self.action or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelUserTyping':
        flags = reader.read_uint32()
        channel_id = reader.read_int64()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        from_id = reader.read_object()
        action = reader.read_object()
        return cls(channel_id=channel_id, top_msg_id=top_msg_id, from_id=from_id, action=action)

@register_tl
class UpdatePinnedMessages(TLObject):
    ID: int = 0xed85eab5

    def __init__(self, pinned: bool = False, peer: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.pinned = pinned
        self.peer = peer
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedMessages':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        peer = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(pinned=pinned, peer=peer, messages=messages, pts=pts, pts_count=pts_count)

@register_tl
class UpdatePinnedChannelMessages(TLObject):
    ID: int = 0x5bb98608

    def __init__(self, pinned: bool = False, channel_id: Any = None, messages: Any = None, pts: Any = None, pts_count: Any = None) -> None:
        self.pinned = pinned
        self.channel_id = channel_id
        self.messages = messages
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedChannelMessages':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        channel_id = reader.read_int64()
        messages = reader.read_vector(lambda r: r.read_object())
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(pinned=pinned, channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count)

@register_tl
class UpdateChat(TLObject):
    ID: int = 0xf89a6a4e

    def __init__(self, chat_id: Any = None) -> None:
        self.chat_id = chat_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChat':
        chat_id = reader.read_int64()
        return cls(chat_id=chat_id)

@register_tl
class UpdateGroupCallParticipants(TLObject):
    ID: int = 0xf2ebdb4e

    def __init__(self, call: Any = None, participants: Any = None, version: Any = None) -> None:
        self.call = call
        self.participants = participants
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        writer.write_vector(self.participants or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCallParticipants':
        call = reader.read_object()
        participants = reader.read_vector(lambda r: r.read_object())
        version = reader.read_int32()
        return cls(call=call, participants=participants, version=version)

@register_tl
class UpdateGroupCall(TLObject):
    ID: int = 0x9d2216e0

    def __init__(self, live_story: bool = False, peer: Any = None, call: Any = None) -> None:
        self.live_story = live_story
        self.peer = peer
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.live_story:
            flags |= (1 << 2)
        if self.peer is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None:
            if hasattr(self.peer, 'write'):
                self.peer.write(writer)
            else:
                writer.write_bytes(self.peer or b'')
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCall':
        flags = reader.read_uint32()
        live_story = bool(flags & (1 << 2))
        peer = None
        if flags & (1 << 1):
            peer = reader.read_object()
        call = reader.read_object()
        return cls(live_story=live_story, peer=peer, call=call)

@register_tl
class UpdatePeerHistoryTTL(TLObject):
    ID: int = 0xbb9bb9a5

    def __init__(self, peer: Any = None, ttl_period: Any = None) -> None:
        self.peer = peer
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ttl_period is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerHistoryTTL':
        flags = reader.read_uint32()
        peer = reader.read_object()
        ttl_period = None
        if flags & (1 << 0):
            ttl_period = reader.read_int32()
        return cls(peer=peer, ttl_period=ttl_period)

@register_tl
class UpdateChatParticipant(TLObject):
    ID: int = 0xd087663a

    def __init__(self, chat_id: Any = None, date: Any = None, actor_id: Any = None, user_id: Any = None, prev_participant: Any = None, new_participant: Any = None, invite: Any = None, qts: Any = None) -> None:
        self.chat_id = chat_id
        self.date = date
        self.actor_id = actor_id
        self.user_id = user_id
        self.prev_participant = prev_participant
        self.new_participant = new_participant
        self.invite = invite
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.prev_participant is not None:
            flags |= (1 << 0)
        if self.new_participant is not None:
            flags |= (1 << 1)
        if self.invite is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.chat_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.actor_id or 0)
        writer.write_int64(self.user_id or 0)
        if self.prev_participant is not None:
            if hasattr(self.prev_participant, 'write'):
                self.prev_participant.write(writer)
            else:
                writer.write_bytes(self.prev_participant or b'')
        if self.new_participant is not None:
            if hasattr(self.new_participant, 'write'):
                self.new_participant.write(writer)
            else:
                writer.write_bytes(self.new_participant or b'')
        if self.invite is not None:
            if hasattr(self.invite, 'write'):
                self.invite.write(writer)
            else:
                writer.write_bytes(self.invite or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipant':
        flags = reader.read_uint32()
        chat_id = reader.read_int64()
        date = reader.read_int32()
        actor_id = reader.read_int64()
        user_id = reader.read_int64()
        prev_participant = None
        if flags & (1 << 0):
            prev_participant = reader.read_object()
        new_participant = None
        if flags & (1 << 1):
            new_participant = reader.read_object()
        invite = None
        if flags & (1 << 2):
            invite = reader.read_object()
        qts = reader.read_int32()
        return cls(chat_id=chat_id, date=date, actor_id=actor_id, user_id=user_id, prev_participant=prev_participant, new_participant=new_participant, invite=invite, qts=qts)

@register_tl
class UpdateChannelParticipant(TLObject):
    ID: int = 0x985d3abb

    def __init__(self, via_chatlist: bool = False, channel_id: Any = None, date: Any = None, actor_id: Any = None, user_id: Any = None, prev_participant: Any = None, new_participant: Any = None, invite: Any = None, qts: Any = None) -> None:
        self.via_chatlist = via_chatlist
        self.channel_id = channel_id
        self.date = date
        self.actor_id = actor_id
        self.user_id = user_id
        self.prev_participant = prev_participant
        self.new_participant = new_participant
        self.invite = invite
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_chatlist:
            flags |= (1 << 3)
        if self.prev_participant is not None:
            flags |= (1 << 0)
        if self.new_participant is not None:
            flags |= (1 << 1)
        if self.invite is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.actor_id or 0)
        writer.write_int64(self.user_id or 0)
        if self.prev_participant is not None:
            if hasattr(self.prev_participant, 'write'):
                self.prev_participant.write(writer)
            else:
                writer.write_bytes(self.prev_participant or b'')
        if self.new_participant is not None:
            if hasattr(self.new_participant, 'write'):
                self.new_participant.write(writer)
            else:
                writer.write_bytes(self.new_participant or b'')
        if self.invite is not None:
            if hasattr(self.invite, 'write'):
                self.invite.write(writer)
            else:
                writer.write_bytes(self.invite or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelParticipant':
        flags = reader.read_uint32()
        via_chatlist = bool(flags & (1 << 3))
        channel_id = reader.read_int64()
        date = reader.read_int32()
        actor_id = reader.read_int64()
        user_id = reader.read_int64()
        prev_participant = None
        if flags & (1 << 0):
            prev_participant = reader.read_object()
        new_participant = None
        if flags & (1 << 1):
            new_participant = reader.read_object()
        invite = None
        if flags & (1 << 2):
            invite = reader.read_object()
        qts = reader.read_int32()
        return cls(via_chatlist=via_chatlist, channel_id=channel_id, date=date, actor_id=actor_id, user_id=user_id, prev_participant=prev_participant, new_participant=new_participant, invite=invite, qts=qts)

@register_tl
class UpdateBotStopped(TLObject):
    ID: int = 0xc4870a49

    def __init__(self, user_id: Any = None, date: Any = None, stopped: Any = None, qts: Any = None) -> None:
        self.user_id = user_id
        self.date = date
        self.stopped = stopped
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_bool(bool(self.stopped))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotStopped':
        user_id = reader.read_int64()
        date = reader.read_int32()
        stopped = reader.read_bool()
        qts = reader.read_int32()
        return cls(user_id=user_id, date=date, stopped=stopped, qts=qts)

@register_tl
class UpdateGroupCallConnection(TLObject):
    ID: int = 0xb783982

    def __init__(self, presentation: bool = False, params: Any = None) -> None:
        self.presentation = presentation
        self.params = params

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.presentation:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.params, 'write'):
            self.params.write(writer)
        else:
            writer.write_bytes(self.params or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCallConnection':
        flags = reader.read_uint32()
        presentation = bool(flags & (1 << 0))
        params = reader.read_object()
        return cls(presentation=presentation, params=params)

@register_tl
class UpdateBotCommands(TLObject):
    ID: int = 0x4d712f2e

    def __init__(self, peer: Any = None, bot_id: Any = None, commands: Any = None) -> None:
        self.peer = peer
        self.bot_id = bot_id
        self.commands = commands

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int64(self.bot_id or 0)
        writer.write_vector(self.commands or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotCommands':
        peer = reader.read_object()
        bot_id = reader.read_int64()
        commands = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, bot_id=bot_id, commands=commands)

@register_tl
class UpdatePendingJoinRequests(TLObject):
    ID: int = 0x7063c3db

    def __init__(self, peer: Any = None, requests_pending: Any = None, recent_requesters: Any = None) -> None:
        self.peer = peer
        self.requests_pending = requests_pending
        self.recent_requesters = recent_requesters

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.requests_pending or 0)
        writer.write_vector(self.recent_requesters or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePendingJoinRequests':
        peer = reader.read_object()
        requests_pending = reader.read_int32()
        recent_requesters = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, requests_pending=requests_pending, recent_requesters=recent_requesters)

@register_tl
class UpdateBotChatInviteRequester(TLObject):
    ID: int = 0x11dfa986

    def __init__(self, peer: Any = None, date: Any = None, user_id: Any = None, about: Any = None, invite: Any = None, qts: Any = None) -> None:
        self.peer = peer
        self.date = date
        self.user_id = user_id
        self.about = about
        self.invite = invite
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.date or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.about or ''))
        if hasattr(self.invite, 'write'):
            self.invite.write(writer)
        else:
            writer.write_bytes(self.invite or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotChatInviteRequester':
        peer = reader.read_object()
        date = reader.read_int32()
        user_id = reader.read_int64()
        about = reader.read_string()
        invite = reader.read_object()
        qts = reader.read_int32()
        return cls(peer=peer, date=date, user_id=user_id, about=about, invite=invite, qts=qts)

@register_tl
class UpdateMessageReactions(TLObject):
    ID: int = 0x1e297bfa

    def __init__(self, peer: Any = None, msg_id: Any = None, top_msg_id: Any = None, saved_peer_id: Any = None, reactions: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id
        self.reactions = reactions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.saved_peer_id is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        if self.saved_peer_id is not None:
            if hasattr(self.saved_peer_id, 'write'):
                self.saved_peer_id.write(writer)
            else:
                writer.write_bytes(self.saved_peer_id or b'')
        if hasattr(self.reactions, 'write'):
            self.reactions.write(writer)
        else:
            writer.write_bytes(self.reactions or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessageReactions':
        flags = reader.read_uint32()
        peer = reader.read_object()
        msg_id = reader.read_int32()
        top_msg_id = None
        if flags & (1 << 0):
            top_msg_id = reader.read_int32()
        saved_peer_id = None
        if flags & (1 << 1):
            saved_peer_id = reader.read_object()
        reactions = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id, reactions=reactions)

@register_tl
class UpdateAttachMenuBots(TLObject):
    ID: int = 0x17b7a20b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateAttachMenuBots':
        return cls()

@register_tl
class UpdateWebViewResultSent(TLObject):
    ID: int = 0x1592b79d

    def __init__(self, query_id: Any = None) -> None:
        self.query_id = query_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateWebViewResultSent':
        query_id = reader.read_int64()
        return cls(query_id=query_id)

@register_tl
class UpdateBotMenuButton(TLObject):
    ID: int = 0x14b85813

    def __init__(self, bot_id: Any = None, button: Any = None) -> None:
        self.bot_id = bot_id
        self.button = button

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.bot_id or 0)
        if hasattr(self.button, 'write'):
            self.button.write(writer)
        else:
            writer.write_bytes(self.button or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotMenuButton':
        bot_id = reader.read_int64()
        button = reader.read_object()
        return cls(bot_id=bot_id, button=button)

@register_tl
class UpdateSavedRingtones(TLObject):
    ID: int = 0x74d8be99

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSavedRingtones':
        return cls()

@register_tl
class UpdateTranscribedAudio(TLObject):
    ID: int = 0x84cd5a

    def __init__(self, pending: bool = False, peer: Any = None, msg_id: Any = None, transcription_id: Any = None, text: Any = None) -> None:
        self.pending = pending
        self.peer = peer
        self.msg_id = msg_id
        self.transcription_id = transcription_id
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pending:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_int64(self.transcription_id or 0)
        writer.write_string(str(self.text or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateTranscribedAudio':
        flags = reader.read_uint32()
        pending = bool(flags & (1 << 0))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        transcription_id = reader.read_int64()
        text = reader.read_string()
        return cls(pending=pending, peer=peer, msg_id=msg_id, transcription_id=transcription_id, text=text)

@register_tl
class UpdateReadFeaturedEmojiStickers(TLObject):
    ID: int = 0xfb4c496c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadFeaturedEmojiStickers':
        return cls()

@register_tl
class UpdateUserEmojiStatus(TLObject):
    ID: int = 0x28373599

    def __init__(self, user_id: Any = None, emoji_status: Any = None) -> None:
        self.user_id = user_id
        self.emoji_status = emoji_status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        if hasattr(self.emoji_status, 'write'):
            self.emoji_status.write(writer)
        else:
            writer.write_bytes(self.emoji_status or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUserEmojiStatus':
        user_id = reader.read_int64()
        emoji_status = reader.read_object()
        return cls(user_id=user_id, emoji_status=emoji_status)

@register_tl
class UpdateRecentEmojiStatuses(TLObject):
    ID: int = 0x30f443db

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateRecentEmojiStatuses':
        return cls()

@register_tl
class UpdateRecentReactions(TLObject):
    ID: int = 0x6f7863f4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateRecentReactions':
        return cls()

@register_tl
class UpdateMoveStickerSetToTop(TLObject):
    ID: int = 0x86fccf85

    def __init__(self, masks: bool = False, emojis: bool = False, stickerset: Any = None) -> None:
        self.masks = masks
        self.emojis = emojis
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.masks:
            flags |= (1 << 0)
        if self.emojis:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.stickerset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMoveStickerSetToTop':
        flags = reader.read_uint32()
        masks = bool(flags & (1 << 0))
        emojis = bool(flags & (1 << 1))
        stickerset = reader.read_int64()
        return cls(masks=masks, emojis=emojis, stickerset=stickerset)

@register_tl
class UpdateMessageExtendedMedia(TLObject):
    ID: int = 0xd5a41724

    def __init__(self, peer: Any = None, msg_id: Any = None, extended_media: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.extended_media = extended_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_vector(self.extended_media or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMessageExtendedMedia':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        extended_media = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, msg_id=msg_id, extended_media=extended_media)

@register_tl
class UpdateUser(TLObject):
    ID: int = 0x20529438

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateUser':
        user_id = reader.read_int64()
        return cls(user_id=user_id)

@register_tl
class UpdateAutoSaveSettings(TLObject):
    ID: int = 0xec05b097

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateAutoSaveSettings':
        return cls()

@register_tl
class UpdateStory(TLObject):
    ID: int = 0x75b3b798

    def __init__(self, peer: Any = None, story: Any = None) -> None:
        self.peer = peer
        self.story = story

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.story, 'write'):
            self.story.write(writer)
        else:
            writer.write_bytes(self.story or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStory':
        peer = reader.read_object()
        story = reader.read_object()
        return cls(peer=peer, story=story)

@register_tl
class UpdateReadStories(TLObject):
    ID: int = 0xf74e932b

    def __init__(self, peer: Any = None, max_id: Any = None) -> None:
        self.peer = peer
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadStories':
        peer = reader.read_object()
        max_id = reader.read_int32()
        return cls(peer=peer, max_id=max_id)

@register_tl
class UpdateStoryID(TLObject):
    ID: int = 0x1bf335b9

    def __init__(self, id: Any = None, random_id: Any = None) -> None:
        self.id = id
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.random_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStoryID':
        id = reader.read_int32()
        random_id = reader.read_int64()
        return cls(id=id, random_id=random_id)

@register_tl
class UpdateStoriesStealthMode(TLObject):
    ID: int = 0x2c084dc1

    def __init__(self, stealth_mode: Any = None) -> None:
        self.stealth_mode = stealth_mode

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.stealth_mode, 'write'):
            self.stealth_mode.write(writer)
        else:
            writer.write_bytes(self.stealth_mode or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStoriesStealthMode':
        stealth_mode = reader.read_object()
        return cls(stealth_mode=stealth_mode)

@register_tl
class UpdateSentStoryReaction(TLObject):
    ID: int = 0x7d627683

    def __init__(self, peer: Any = None, story_id: Any = None, reaction: Any = None) -> None:
        self.peer = peer
        self.story_id = story_id
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.story_id or 0)
        if hasattr(self.reaction, 'write'):
            self.reaction.write(writer)
        else:
            writer.write_bytes(self.reaction or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSentStoryReaction':
        peer = reader.read_object()
        story_id = reader.read_int32()
        reaction = reader.read_object()
        return cls(peer=peer, story_id=story_id, reaction=reaction)

@register_tl
class UpdateBotChatBoost(TLObject):
    ID: int = 0x904dd49c

    def __init__(self, peer: Any = None, boost: Any = None, qts: Any = None) -> None:
        self.peer = peer
        self.boost = boost
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.boost, 'write'):
            self.boost.write(writer)
        else:
            writer.write_bytes(self.boost or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotChatBoost':
        peer = reader.read_object()
        boost = reader.read_object()
        qts = reader.read_int32()
        return cls(peer=peer, boost=boost, qts=qts)

@register_tl
class UpdateChannelViewForumAsMessages(TLObject):
    ID: int = 0x7b68920

    def __init__(self, channel_id: Any = None, enabled: Any = None) -> None:
        self.channel_id = channel_id
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChannelViewForumAsMessages':
        channel_id = reader.read_int64()
        enabled = reader.read_bool()
        return cls(channel_id=channel_id, enabled=enabled)

@register_tl
class UpdatePeerWallpaper(TLObject):
    ID: int = 0xae3f101d

    def __init__(self, wallpaper_overridden: bool = False, peer: Any = None, wallpaper: Any = None) -> None:
        self.wallpaper_overridden = wallpaper_overridden
        self.peer = peer
        self.wallpaper = wallpaper

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.wallpaper_overridden:
            flags |= (1 << 1)
        if self.wallpaper is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.wallpaper is not None:
            if hasattr(self.wallpaper, 'write'):
                self.wallpaper.write(writer)
            else:
                writer.write_bytes(self.wallpaper or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePeerWallpaper':
        flags = reader.read_uint32()
        wallpaper_overridden = bool(flags & (1 << 1))
        peer = reader.read_object()
        wallpaper = None
        if flags & (1 << 0):
            wallpaper = reader.read_object()
        return cls(wallpaper_overridden=wallpaper_overridden, peer=peer, wallpaper=wallpaper)

@register_tl
class UpdateBotMessageReaction(TLObject):
    ID: int = 0xac21d3ce

    def __init__(self, peer: Any = None, msg_id: Any = None, date: Any = None, actor: Any = None, old_reactions: Any = None, new_reactions: Any = None, qts: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.date = date
        self.actor = actor
        self.old_reactions = old_reactions
        self.new_reactions = new_reactions
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_int32(self.date or 0)
        if hasattr(self.actor, 'write'):
            self.actor.write(writer)
        else:
            writer.write_bytes(self.actor or b'')
        writer.write_vector(self.old_reactions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.new_reactions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotMessageReaction':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        date = reader.read_int32()
        actor = reader.read_object()
        old_reactions = reader.read_vector(lambda r: r.read_object())
        new_reactions = reader.read_vector(lambda r: r.read_object())
        qts = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id, date=date, actor=actor, old_reactions=old_reactions, new_reactions=new_reactions, qts=qts)

@register_tl
class UpdateBotMessageReactions(TLObject):
    ID: int = 0x9cb7759

    def __init__(self, peer: Any = None, msg_id: Any = None, date: Any = None, reactions: Any = None, qts: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.date = date
        self.reactions = reactions
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.msg_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_vector(self.reactions or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotMessageReactions':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        date = reader.read_int32()
        reactions = reader.read_vector(lambda r: r.read_object())
        qts = reader.read_int32()
        return cls(peer=peer, msg_id=msg_id, date=date, reactions=reactions, qts=qts)

@register_tl
class UpdateSavedDialogPinned(TLObject):
    ID: int = 0xaeaf9e74

    def __init__(self, pinned: bool = False, peer: Any = None) -> None:
        self.pinned = pinned
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSavedDialogPinned':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        peer = reader.read_object()
        return cls(pinned=pinned, peer=peer)

@register_tl
class UpdatePinnedSavedDialogs(TLObject):
    ID: int = 0x686c85a6

    def __init__(self, order: Any = None) -> None:
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.order is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.order is not None:
            writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedSavedDialogs':
        flags = reader.read_uint32()
        order = None
        if flags & (1 << 0):
            order = reader.read_vector(lambda r: r.read_object())
        return cls(order=order)

@register_tl
class UpdateSavedReactionTags(TLObject):
    ID: int = 0x39c67432

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSavedReactionTags':
        return cls()

@register_tl
class UpdateSmsJob(TLObject):
    ID: int = 0xf16269d4

    def __init__(self, job_id: Any = None) -> None:
        self.job_id = job_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.job_id or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSmsJob':
        job_id = reader.read_string()
        return cls(job_id=job_id)

@register_tl
class UpdateQuickReplies(TLObject):
    ID: int = 0xf9470ab2

    def __init__(self, quick_replies: Any = None) -> None:
        self.quick_replies = quick_replies

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.quick_replies or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateQuickReplies':
        quick_replies = reader.read_vector(lambda r: r.read_object())
        return cls(quick_replies=quick_replies)

@register_tl
class UpdateNewQuickReply(TLObject):
    ID: int = 0xf53da717

    def __init__(self, quick_reply: Any = None) -> None:
        self.quick_reply = quick_reply

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.quick_reply, 'write'):
            self.quick_reply.write(writer)
        else:
            writer.write_bytes(self.quick_reply or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewQuickReply':
        quick_reply = reader.read_object()
        return cls(quick_reply=quick_reply)

@register_tl
class UpdateDeleteQuickReply(TLObject):
    ID: int = 0x53e6f1ec

    def __init__(self, shortcut_id: Any = None) -> None:
        self.shortcut_id = shortcut_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteQuickReply':
        shortcut_id = reader.read_int32()
        return cls(shortcut_id=shortcut_id)

@register_tl
class UpdateQuickReplyMessage(TLObject):
    ID: int = 0x3e050d0f

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateQuickReplyMessage':
        message = reader.read_object()
        return cls(message=message)

@register_tl
class UpdateDeleteQuickReplyMessages(TLObject):
    ID: int = 0x566fe7cd

    def __init__(self, shortcut_id: Any = None, messages: Any = None) -> None:
        self.shortcut_id = shortcut_id
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.shortcut_id or 0)
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteQuickReplyMessages':
        shortcut_id = reader.read_int32()
        messages = reader.read_vector(lambda r: r.read_object())
        return cls(shortcut_id=shortcut_id, messages=messages)

@register_tl
class UpdateBotBusinessConnect(TLObject):
    ID: int = 0x8ae5c97a

    def __init__(self, connection: Any = None, qts: Any = None) -> None:
        self.connection = connection
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.connection, 'write'):
            self.connection.write(writer)
        else:
            writer.write_bytes(self.connection or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotBusinessConnect':
        connection = reader.read_object()
        qts = reader.read_int32()
        return cls(connection=connection, qts=qts)

@register_tl
class UpdateBotNewBusinessMessage(TLObject):
    ID: int = 0x9ddb347c

    def __init__(self, connection_id: Any = None, message: Any = None, reply_to_message: Any = None, qts: Any = None) -> None:
        self.connection_id = connection_id
        self.message = message
        self.reply_to_message = reply_to_message
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_to_message is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.connection_id or ''))
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        if self.reply_to_message is not None:
            if hasattr(self.reply_to_message, 'write'):
                self.reply_to_message.write(writer)
            else:
                writer.write_bytes(self.reply_to_message or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotNewBusinessMessage':
        flags = reader.read_uint32()
        connection_id = reader.read_string()
        message = reader.read_object()
        reply_to_message = None
        if flags & (1 << 0):
            reply_to_message = reader.read_object()
        qts = reader.read_int32()
        return cls(connection_id=connection_id, message=message, reply_to_message=reply_to_message, qts=qts)

@register_tl
class UpdateBotEditBusinessMessage(TLObject):
    ID: int = 0x7df587c

    def __init__(self, connection_id: Any = None, message: Any = None, reply_to_message: Any = None, qts: Any = None) -> None:
        self.connection_id = connection_id
        self.message = message
        self.reply_to_message = reply_to_message
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_to_message is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.connection_id or ''))
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        if self.reply_to_message is not None:
            if hasattr(self.reply_to_message, 'write'):
                self.reply_to_message.write(writer)
            else:
                writer.write_bytes(self.reply_to_message or b'')
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotEditBusinessMessage':
        flags = reader.read_uint32()
        connection_id = reader.read_string()
        message = reader.read_object()
        reply_to_message = None
        if flags & (1 << 0):
            reply_to_message = reader.read_object()
        qts = reader.read_int32()
        return cls(connection_id=connection_id, message=message, reply_to_message=reply_to_message, qts=qts)

@register_tl
class UpdateBotDeleteBusinessMessage(TLObject):
    ID: int = 0xa02a982e

    def __init__(self, connection_id: Any = None, peer: Any = None, messages: Any = None, qts: Any = None) -> None:
        self.connection_id = connection_id
        self.peer = peer
        self.messages = messages
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.connection_id or ''))
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotDeleteBusinessMessage':
        connection_id = reader.read_string()
        peer = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        qts = reader.read_int32()
        return cls(connection_id=connection_id, peer=peer, messages=messages, qts=qts)

@register_tl
class UpdateNewStoryReaction(TLObject):
    ID: int = 0x1824e40b

    def __init__(self, story_id: Any = None, peer: Any = None, reaction: Any = None) -> None:
        self.story_id = story_id
        self.peer = peer
        self.reaction = reaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.story_id or 0)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.reaction, 'write'):
            self.reaction.write(writer)
        else:
            writer.write_bytes(self.reaction or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateNewStoryReaction':
        story_id = reader.read_int32()
        peer = reader.read_object()
        reaction = reader.read_object()
        return cls(story_id=story_id, peer=peer, reaction=reaction)

@register_tl
class UpdateStarsBalance(TLObject):
    ID: int = 0x4e80a379

    def __init__(self, balance: Any = None) -> None:
        self.balance = balance

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.balance, 'write'):
            self.balance.write(writer)
        else:
            writer.write_bytes(self.balance or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStarsBalance':
        balance = reader.read_object()
        return cls(balance=balance)

@register_tl
class UpdateBusinessBotCallbackQuery(TLObject):
    ID: int = 0x1ea2fda7

    def __init__(self, query_id: Any = None, user_id: Any = None, connection_id: Any = None, message: Any = None, reply_to_message: Any = None, chat_instance: Any = None, data: Any = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.connection_id = connection_id
        self.message = message
        self.reply_to_message = reply_to_message
        self.chat_instance = chat_instance
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reply_to_message is not None:
            flags |= (1 << 2)
        if self.data is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.connection_id or ''))
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        if self.reply_to_message is not None:
            if hasattr(self.reply_to_message, 'write'):
                self.reply_to_message.write(writer)
            else:
                writer.write_bytes(self.reply_to_message or b'')
        writer.write_int64(self.chat_instance or 0)
        if self.data is not None:
            writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBusinessBotCallbackQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        user_id = reader.read_int64()
        connection_id = reader.read_string()
        message = reader.read_object()
        reply_to_message = None
        if flags & (1 << 2):
            reply_to_message = reader.read_object()
        chat_instance = reader.read_int64()
        data = None
        if flags & (1 << 0):
            data = reader.read_bytes()
        return cls(query_id=query_id, user_id=user_id, connection_id=connection_id, message=message, reply_to_message=reply_to_message, chat_instance=chat_instance, data=data)

@register_tl
class UpdateStarsRevenueStatus(TLObject):
    ID: int = 0xa584b019

    def __init__(self, peer: Any = None, status: Any = None) -> None:
        self.peer = peer
        self.status = status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if hasattr(self.status, 'write'):
            self.status.write(writer)
        else:
            writer.write_bytes(self.status or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStarsRevenueStatus':
        peer = reader.read_object()
        status = reader.read_object()
        return cls(peer=peer, status=status)

@register_tl
class UpdateBotPurchasedPaidMedia(TLObject):
    ID: int = 0x283bd312

    def __init__(self, user_id: Any = None, payload: Any = None, qts: Any = None) -> None:
        self.user_id = user_id
        self.payload = payload
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.payload or ''))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotPurchasedPaidMedia':
        user_id = reader.read_int64()
        payload = reader.read_string()
        qts = reader.read_int32()
        return cls(user_id=user_id, payload=payload, qts=qts)

@register_tl
class UpdatePaidReactionPrivacy(TLObject):
    ID: int = 0x8b725fce

    def __init__(self, private: Any = None) -> None:
        self.private = private

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.private, 'write'):
            self.private.write(writer)
        else:
            writer.write_bytes(self.private or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePaidReactionPrivacy':
        private = reader.read_object()
        return cls(private=private)

@register_tl
class UpdateSentPhoneCode(TLObject):
    ID: int = 0x504aa18f

    def __init__(self, sent_code: Any = None) -> None:
        self.sent_code = sent_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.sent_code, 'write'):
            self.sent_code.write(writer)
        else:
            writer.write_bytes(self.sent_code or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateSentPhoneCode':
        sent_code = reader.read_object()
        return cls(sent_code=sent_code)

@register_tl
class UpdateGroupCallChainBlocks(TLObject):
    ID: int = 0xa477288f

    def __init__(self, call: Any = None, sub_chain_id: Any = None, blocks: Any = None, next_offset: Any = None) -> None:
        self.call = call
        self.sub_chain_id = sub_chain_id
        self.blocks = blocks
        self.next_offset = next_offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        writer.write_int32(self.sub_chain_id or 0)
        writer.write_vector(self.blocks or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.next_offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCallChainBlocks':
        call = reader.read_object()
        sub_chain_id = reader.read_int32()
        blocks = reader.read_vector(lambda r: r.read_object())
        next_offset = reader.read_int32()
        return cls(call=call, sub_chain_id=sub_chain_id, blocks=blocks, next_offset=next_offset)

@register_tl
class UpdateReadMonoForumInbox(TLObject):
    ID: int = 0x77b0e372

    def __init__(self, channel_id: Any = None, saved_peer_id: Any = None, read_max_id: Any = None) -> None:
        self.channel_id = channel_id
        self.saved_peer_id = saved_peer_id
        self.read_max_id = read_max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        if hasattr(self.saved_peer_id, 'write'):
            self.saved_peer_id.write(writer)
        else:
            writer.write_bytes(self.saved_peer_id or b'')
        writer.write_int32(self.read_max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadMonoForumInbox':
        channel_id = reader.read_int64()
        saved_peer_id = reader.read_object()
        read_max_id = reader.read_int32()
        return cls(channel_id=channel_id, saved_peer_id=saved_peer_id, read_max_id=read_max_id)

@register_tl
class UpdateReadMonoForumOutbox(TLObject):
    ID: int = 0xa4a79376

    def __init__(self, channel_id: Any = None, saved_peer_id: Any = None, read_max_id: Any = None) -> None:
        self.channel_id = channel_id
        self.saved_peer_id = saved_peer_id
        self.read_max_id = read_max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id or 0)
        if hasattr(self.saved_peer_id, 'write'):
            self.saved_peer_id.write(writer)
        else:
            writer.write_bytes(self.saved_peer_id or b'')
        writer.write_int32(self.read_max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateReadMonoForumOutbox':
        channel_id = reader.read_int64()
        saved_peer_id = reader.read_object()
        read_max_id = reader.read_int32()
        return cls(channel_id=channel_id, saved_peer_id=saved_peer_id, read_max_id=read_max_id)

@register_tl
class UpdateMonoForumNoPaidException(TLObject):
    ID: int = 0x9f812b08

    def __init__(self, exception: bool = False, channel_id: Any = None, saved_peer_id: Any = None) -> None:
        self.exception = exception
        self.channel_id = channel_id
        self.saved_peer_id = saved_peer_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.exception:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.channel_id or 0)
        if hasattr(self.saved_peer_id, 'write'):
            self.saved_peer_id.write(writer)
        else:
            writer.write_bytes(self.saved_peer_id or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateMonoForumNoPaidException':
        flags = reader.read_uint32()
        exception = bool(flags & (1 << 0))
        channel_id = reader.read_int64()
        saved_peer_id = reader.read_object()
        return cls(exception=exception, channel_id=channel_id, saved_peer_id=saved_peer_id)

@register_tl
class UpdateGroupCallMessage(TLObject):
    ID: int = 0xd8326f0d

    def __init__(self, call: Any = None, message: Any = None) -> None:
        self.call = call
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCallMessage':
        call = reader.read_object()
        message = reader.read_object()
        return cls(call=call, message=message)

@register_tl
class UpdateGroupCallEncryptedMessage(TLObject):
    ID: int = 0xc957a766

    def __init__(self, call: Any = None, from_id: Any = None, encrypted_message: Any = None) -> None:
        self.call = call
        self.from_id = from_id
        self.encrypted_message = encrypted_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        if hasattr(self.from_id, 'write'):
            self.from_id.write(writer)
        else:
            writer.write_bytes(self.from_id or b'')
        writer.write_bytes(self.encrypted_message or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateGroupCallEncryptedMessage':
        call = reader.read_object()
        from_id = reader.read_object()
        encrypted_message = reader.read_bytes()
        return cls(call=call, from_id=from_id, encrypted_message=encrypted_message)

@register_tl
class UpdatePinnedForumTopic(TLObject):
    ID: int = 0x683b2c52

    def __init__(self, pinned: bool = False, peer: Any = None, topic_id: Any = None) -> None:
        self.pinned = pinned
        self.peer = peer
        self.topic_id = topic_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pinned:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.topic_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedForumTopic':
        flags = reader.read_uint32()
        pinned = bool(flags & (1 << 0))
        peer = reader.read_object()
        topic_id = reader.read_int32()
        return cls(pinned=pinned, peer=peer, topic_id=topic_id)

@register_tl
class UpdatePinnedForumTopics(TLObject):
    ID: int = 0xdef143d0

    def __init__(self, peer: Any = None, order: Any = None) -> None:
        self.peer = peer
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.order is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        if self.order is not None:
            writer.write_vector(self.order or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatePinnedForumTopics':
        flags = reader.read_uint32()
        peer = reader.read_object()
        order = None
        if flags & (1 << 0):
            order = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, order=order)

@register_tl
class UpdateDeleteGroupCallMessages(TLObject):
    ID: int = 0x3e85e92c

    def __init__(self, call: Any = None, messages: Any = None) -> None:
        self.call = call
        self.messages = messages

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.call, 'write'):
            self.call.write(writer)
        else:
            writer.write_bytes(self.call or b'')
        writer.write_vector(self.messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateDeleteGroupCallMessages':
        call = reader.read_object()
        messages = reader.read_vector(lambda r: r.read_object())
        return cls(call=call, messages=messages)

@register_tl
class UpdateStarGiftAuctionState(TLObject):
    ID: int = 0x48e246c2

    def __init__(self, gift_id: Any = None, state: Any = None) -> None:
        self.gift_id = gift_id
        self.state = state

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)
        if hasattr(self.state, 'write'):
            self.state.write(writer)
        else:
            writer.write_bytes(self.state or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStarGiftAuctionState':
        gift_id = reader.read_int64()
        state = reader.read_object()
        return cls(gift_id=gift_id, state=state)

@register_tl
class UpdateStarGiftAuctionUserState(TLObject):
    ID: int = 0xdc58f31e

    def __init__(self, gift_id: Any = None, user_state: Any = None) -> None:
        self.gift_id = gift_id
        self.user_state = user_state

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.gift_id or 0)
        if hasattr(self.user_state, 'write'):
            self.user_state.write(writer)
        else:
            writer.write_bytes(self.user_state or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStarGiftAuctionUserState':
        gift_id = reader.read_int64()
        user_state = reader.read_object()
        return cls(gift_id=gift_id, user_state=user_state)

@register_tl
class UpdateEmojiGameInfo(TLObject):
    ID: int = 0xfb9c547a

    def __init__(self, info: Any = None) -> None:
        self.info = info

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.info, 'write'):
            self.info.write(writer)
        else:
            writer.write_bytes(self.info or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateEmojiGameInfo':
        info = reader.read_object()
        return cls(info=info)

@register_tl
class UpdateStarGiftCraftFail(TLObject):
    ID: int = 0xac072444

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateStarGiftCraftFail':
        return cls()

@register_tl
class UpdateChatParticipantRank(TLObject):
    ID: int = 0xbd8367b9

    def __init__(self, chat_id: Any = None, user_id: Any = None, rank: Any = None, version: Any = None) -> None:
        self.chat_id = chat_id
        self.user_id = user_id
        self.rank = rank
        self.version = version

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.chat_id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.rank or ''))
        writer.write_int32(self.version or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateChatParticipantRank':
        chat_id = reader.read_int64()
        user_id = reader.read_int64()
        rank = reader.read_string()
        version = reader.read_int32()
        return cls(chat_id=chat_id, user_id=user_id, rank=rank, version=version)

@register_tl
class UpdateManagedBot(TLObject):
    ID: int = 0x4880ed9a

    def __init__(self, user_id: Any = None, bot_id: Any = None, qts: Any = None) -> None:
        self.user_id = user_id
        self.bot_id = bot_id
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id or 0)
        writer.write_int64(self.bot_id or 0)
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateManagedBot':
        user_id = reader.read_int64()
        bot_id = reader.read_int64()
        qts = reader.read_int32()
        return cls(user_id=user_id, bot_id=bot_id, qts=qts)

@register_tl
class UpdateBotGuestChatQuery(TLObject):
    ID: int = 0xcdd4093d

    def __init__(self, query_id: Any = None, message: Any = None, reference_messages: Any = None, qts: Any = None) -> None:
        self.query_id = query_id
        self.message = message
        self.reference_messages = reference_messages
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reference_messages is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.query_id or 0)
        if hasattr(self.message, 'write'):
            self.message.write(writer)
        else:
            writer.write_bytes(self.message or b'')
        if self.reference_messages is not None:
            writer.write_vector(self.reference_messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.qts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateBotGuestChatQuery':
        flags = reader.read_uint32()
        query_id = reader.read_int64()
        message = reader.read_object()
        reference_messages = None
        if flags & (1 << 0):
            reference_messages = reader.read_vector(lambda r: r.read_object())
        qts = reader.read_int32()
        return cls(query_id=query_id, message=message, reference_messages=reference_messages, qts=qts)

@register_tl
class UpdateAiComposeTones(TLObject):
    ID: int = 0x8c0f91fb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateAiComposeTones':
        return cls()

@register_tl
class UpdatesState(TLObject):
    ID: int = 0xa56c2a3e

    def __init__(self, pts: Any = None, qts: Any = None, date: Any = None, seq: Any = None, unread_count: Any = None) -> None:
        self.pts = pts
        self.qts = qts
        self.date = date
        self.seq = seq
        self.unread_count = unread_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.qts or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.seq or 0)
        writer.write_int32(self.unread_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesState':
        pts = reader.read_int32()
        qts = reader.read_int32()
        date = reader.read_int32()
        seq = reader.read_int32()
        unread_count = reader.read_int32()
        return cls(pts=pts, qts=qts, date=date, seq=seq, unread_count=unread_count)

@register_tl
class UpdatesDifferenceEmpty(TLObject):
    ID: int = 0x5d75a138

    def __init__(self, date: Any = None, seq: Any = None) -> None:
        self.date = date
        self.seq = seq

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.seq or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesDifferenceEmpty':
        date = reader.read_int32()
        seq = reader.read_int32()
        return cls(date=date, seq=seq)

@register_tl
class UpdatesDifference(TLObject):
    ID: int = 0xf49ca0

    def __init__(self, new_messages: Any = None, new_encrypted_messages: Any = None, other_updates: Any = None, chats: Any = None, users: Any = None, state: Any = None) -> None:
        self.new_messages = new_messages
        self.new_encrypted_messages = new_encrypted_messages
        self.other_updates = other_updates
        self.chats = chats
        self.users = users
        self.state = state

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.new_messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.new_encrypted_messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.other_updates or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if hasattr(self.state, 'write'):
            self.state.write(writer)
        else:
            writer.write_bytes(self.state or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesDifference':
        new_messages = reader.read_vector(lambda r: r.read_object())
        new_encrypted_messages = reader.read_vector(lambda r: r.read_object())
        other_updates = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        state = reader.read_object()
        return cls(new_messages=new_messages, new_encrypted_messages=new_encrypted_messages, other_updates=other_updates, chats=chats, users=users, state=state)

@register_tl
class UpdatesDifferenceSlice(TLObject):
    ID: int = 0xa8fb1981

    def __init__(self, new_messages: Any = None, new_encrypted_messages: Any = None, other_updates: Any = None, chats: Any = None, users: Any = None, intermediate_state: Any = None) -> None:
        self.new_messages = new_messages
        self.new_encrypted_messages = new_encrypted_messages
        self.other_updates = other_updates
        self.chats = chats
        self.users = users
        self.intermediate_state = intermediate_state

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.new_messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.new_encrypted_messages or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.other_updates or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if hasattr(self.intermediate_state, 'write'):
            self.intermediate_state.write(writer)
        else:
            writer.write_bytes(self.intermediate_state or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesDifferenceSlice':
        new_messages = reader.read_vector(lambda r: r.read_object())
        new_encrypted_messages = reader.read_vector(lambda r: r.read_object())
        other_updates = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        intermediate_state = reader.read_object()
        return cls(new_messages=new_messages, new_encrypted_messages=new_encrypted_messages, other_updates=other_updates, chats=chats, users=users, intermediate_state=intermediate_state)

@register_tl
class UpdatesDifferenceTooLong(TLObject):
    ID: int = 0x4afe8f6d

    def __init__(self, pts: Any = None) -> None:
        self.pts = pts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesDifferenceTooLong':
        pts = reader.read_int32()
        return cls(pts=pts)

@register_tl
class UpdatesTooLong(TLObject):
    ID: int = 0xe317af7e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesTooLong':
        return cls()

@register_tl
class UpdateShortMessage(TLObject):
    ID: int = 0x313bc7f8

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, silent: bool = False, id: Any = None, user_id: Any = None, message: Any = None, pts: Any = None, pts_count: Any = None, date: Any = None, fwd_from: Any = None, via_bot_id: Any = None, reply_to: Any = None, entities: Any = None, ttl_period: Any = None) -> None:
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.silent = silent
        self.id = id
        self.user_id = user_id
        self.message = message
        self.pts = pts
        self.pts_count = pts_count
        self.date = date
        self.fwd_from = fwd_from
        self.via_bot_id = via_bot_id
        self.reply_to = reply_to
        self.entities = entities
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.out:
            flags |= (1 << 1)
        if self.mentioned:
            flags |= (1 << 4)
        if self.media_unread:
            flags |= (1 << 5)
        if self.silent:
            flags |= (1 << 13)
        if self.fwd_from is not None:
            flags |= (1 << 2)
        if self.via_bot_id is not None:
            flags |= (1 << 11)
        if self.reply_to is not None:
            flags |= (1 << 3)
        if self.entities is not None:
            flags |= (1 << 7)
        if self.ttl_period is not None:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.user_id or 0)
        writer.write_string(str(self.message or ''))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        writer.write_int32(self.date or 0)
        if self.fwd_from is not None:
            if hasattr(self.fwd_from, 'write'):
                self.fwd_from.write(writer)
            else:
                writer.write_bytes(self.fwd_from or b'')
        if self.via_bot_id is not None:
            writer.write_int64(self.via_bot_id or 0)
        if self.reply_to is not None:
            if hasattr(self.reply_to, 'write'):
                self.reply_to.write(writer)
            else:
                writer.write_bytes(self.reply_to or b'')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateShortMessage':
        flags = reader.read_uint32()
        out = bool(flags & (1 << 1))
        mentioned = bool(flags & (1 << 4))
        media_unread = bool(flags & (1 << 5))
        silent = bool(flags & (1 << 13))
        id = reader.read_int32()
        user_id = reader.read_int64()
        message = reader.read_string()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        date = reader.read_int32()
        fwd_from = None
        if flags & (1 << 2):
            fwd_from = reader.read_object()
        via_bot_id = None
        if flags & (1 << 11):
            via_bot_id = reader.read_int64()
        reply_to = None
        if flags & (1 << 3):
            reply_to = reader.read_object()
        entities = None
        if flags & (1 << 7):
            entities = reader.read_vector(lambda r: r.read_object())
        ttl_period = None
        if flags & (1 << 25):
            ttl_period = reader.read_int32()
        return cls(out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, id=id, user_id=user_id, message=message, pts=pts, pts_count=pts_count, date=date, fwd_from=fwd_from, via_bot_id=via_bot_id, reply_to=reply_to, entities=entities, ttl_period=ttl_period)

@register_tl
class UpdateShortChatMessage(TLObject):
    ID: int = 0x4d6deea5

    def __init__(self, out: bool = False, mentioned: bool = False, media_unread: bool = False, silent: bool = False, id: Any = None, from_id: Any = None, chat_id: Any = None, message: Any = None, pts: Any = None, pts_count: Any = None, date: Any = None, fwd_from: Any = None, via_bot_id: Any = None, reply_to: Any = None, entities: Any = None, ttl_period: Any = None) -> None:
        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.silent = silent
        self.id = id
        self.from_id = from_id
        self.chat_id = chat_id
        self.message = message
        self.pts = pts
        self.pts_count = pts_count
        self.date = date
        self.fwd_from = fwd_from
        self.via_bot_id = via_bot_id
        self.reply_to = reply_to
        self.entities = entities
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.out:
            flags |= (1 << 1)
        if self.mentioned:
            flags |= (1 << 4)
        if self.media_unread:
            flags |= (1 << 5)
        if self.silent:
            flags |= (1 << 13)
        if self.fwd_from is not None:
            flags |= (1 << 2)
        if self.via_bot_id is not None:
            flags |= (1 << 11)
        if self.reply_to is not None:
            flags |= (1 << 3)
        if self.entities is not None:
            flags |= (1 << 7)
        if self.ttl_period is not None:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.from_id or 0)
        writer.write_int64(self.chat_id or 0)
        writer.write_string(str(self.message or ''))
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        writer.write_int32(self.date or 0)
        if self.fwd_from is not None:
            if hasattr(self.fwd_from, 'write'):
                self.fwd_from.write(writer)
            else:
                writer.write_bytes(self.fwd_from or b'')
        if self.via_bot_id is not None:
            writer.write_int64(self.via_bot_id or 0)
        if self.reply_to is not None:
            if hasattr(self.reply_to, 'write'):
                self.reply_to.write(writer)
            else:
                writer.write_bytes(self.reply_to or b'')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateShortChatMessage':
        flags = reader.read_uint32()
        out = bool(flags & (1 << 1))
        mentioned = bool(flags & (1 << 4))
        media_unread = bool(flags & (1 << 5))
        silent = bool(flags & (1 << 13))
        id = reader.read_int32()
        from_id = reader.read_int64()
        chat_id = reader.read_int64()
        message = reader.read_string()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        date = reader.read_int32()
        fwd_from = None
        if flags & (1 << 2):
            fwd_from = reader.read_object()
        via_bot_id = None
        if flags & (1 << 11):
            via_bot_id = reader.read_int64()
        reply_to = None
        if flags & (1 << 3):
            reply_to = reader.read_object()
        entities = None
        if flags & (1 << 7):
            entities = reader.read_vector(lambda r: r.read_object())
        ttl_period = None
        if flags & (1 << 25):
            ttl_period = reader.read_int32()
        return cls(out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, id=id, from_id=from_id, chat_id=chat_id, message=message, pts=pts, pts_count=pts_count, date=date, fwd_from=fwd_from, via_bot_id=via_bot_id, reply_to=reply_to, entities=entities, ttl_period=ttl_period)

@register_tl
class UpdateShort(TLObject):
    ID: int = 0x78d4dec1

    def __init__(self, update: Any = None, date: Any = None) -> None:
        self.update = update
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.update, 'write'):
            self.update.write(writer)
        else:
            writer.write_bytes(self.update or b'')
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateShort':
        update = reader.read_object()
        date = reader.read_int32()
        return cls(update=update, date=date)

@register_tl
class UpdatesCombined(TLObject):
    ID: int = 0x725b04c3

    def __init__(self, updates: Any = None, users: Any = None, chats: Any = None, date: Any = None, seq_start: Any = None, seq: Any = None) -> None:
        self.updates = updates
        self.users = users
        self.chats = chats
        self.date = date
        self.seq_start = seq_start
        self.seq = seq

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.updates or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.date or 0)
        writer.write_int32(self.seq_start or 0)
        writer.write_int32(self.seq or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesCombined':
        updates = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        date = reader.read_int32()
        seq_start = reader.read_int32()
        seq = reader.read_int32()
        return cls(updates=updates, users=users, chats=chats, date=date, seq_start=seq_start, seq=seq)

@register_tl
class Updates(TLObject):
    ID: int = 0x74ae4240

    def __init__(self, updates: Any = None, users: Any = None, chats: Any = None, date: Any = None, seq: Any = None) -> None:
        self.updates = updates
        self.users = users
        self.chats = chats
        self.date = date
        self.seq = seq

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.updates or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.date or 0)
        writer.write_int32(self.seq or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Updates':
        updates = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        date = reader.read_int32()
        seq = reader.read_int32()
        return cls(updates=updates, users=users, chats=chats, date=date, seq=seq)

@register_tl
class UpdateShortSentMessage(TLObject):
    ID: int = 0x9015e101

    def __init__(self, out: bool = False, id: Any = None, pts: Any = None, pts_count: Any = None, date: Any = None, media: Any = None, entities: Any = None, ttl_period: Any = None) -> None:
        self.out = out
        self.id = id
        self.pts = pts
        self.pts_count = pts_count
        self.date = date
        self.media = media
        self.entities = entities
        self.ttl_period = ttl_period

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.out:
            flags |= (1 << 1)
        if self.media is not None:
            flags |= (1 << 9)
        if self.entities is not None:
            flags |= (1 << 7)
        if self.ttl_period is not None:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)
        writer.write_int32(self.date or 0)
        if self.media is not None:
            if hasattr(self.media, 'write'):
                self.media.write(writer)
            else:
                writer.write_bytes(self.media or b'')
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdateShortSentMessage':
        flags = reader.read_uint32()
        out = bool(flags & (1 << 1))
        id = reader.read_int32()
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        date = reader.read_int32()
        media = None
        if flags & (1 << 9):
            media = reader.read_object()
        entities = None
        if flags & (1 << 7):
            entities = reader.read_vector(lambda r: r.read_object())
        ttl_period = None
        if flags & (1 << 25):
            ttl_period = reader.read_int32()
        return cls(out=out, id=id, pts=pts, pts_count=pts_count, date=date, media=media, entities=entities, ttl_period=ttl_period)

@register_tl
class PhotosPhotos(TLObject):
    ID: int = 0x8dca6aa5

    def __init__(self, photos: Any = None, users: Any = None) -> None:
        self.photos = photos
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.photos or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosPhotos':
        photos = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(photos=photos, users=users)

@register_tl
class PhotosPhotosSlice(TLObject):
    ID: int = 0x15051f54

    def __init__(self, count: Any = None, photos: Any = None, users: Any = None) -> None:
        self.count = count
        self.photos = photos
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count or 0)
        writer.write_vector(self.photos or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosPhotosSlice':
        count = reader.read_int32()
        photos = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, photos=photos, users=users)

@register_tl
class PhotosPhoto(TLObject):
    ID: int = 0x20212ca8

    def __init__(self, photo: Any = None, users: Any = None) -> None:
        self.photo = photo
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.photo, 'write'):
            self.photo.write(writer)
        else:
            writer.write_bytes(self.photo or b'')
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosPhoto':
        photo = reader.read_object()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(photo=photo, users=users)

@register_tl
class UploadFile(TLObject):
    ID: int = 0x96a18d5

    def __init__(self, type: Any = None, mtime: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.mtime = mtime
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.type, 'write'):
            self.type.write(writer)
        else:
            writer.write_bytes(self.type or b'')
        writer.write_int32(self.mtime or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadFile':
        type = reader.read_object()
        mtime = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(type=type, mtime=mtime, bytes=bytes)

@register_tl
class UploadFileCdnRedirect(TLObject):
    ID: int = 0xf18cda44

    def __init__(self, dc_id: Any = None, file_token: Any = None, encryption_key: Any = None, encryption_iv: Any = None, file_hashes: Any = None) -> None:
        self.dc_id = dc_id
        self.file_token = file_token
        self.encryption_key = encryption_key
        self.encryption_iv = encryption_iv
        self.file_hashes = file_hashes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id or 0)
        writer.write_bytes(self.file_token or b'')
        writer.write_bytes(self.encryption_key or b'')
        writer.write_bytes(self.encryption_iv or b'')
        writer.write_vector(self.file_hashes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadFileCdnRedirect':
        dc_id = reader.read_int32()
        file_token = reader.read_bytes()
        encryption_key = reader.read_bytes()
        encryption_iv = reader.read_bytes()
        file_hashes = reader.read_vector(lambda r: r.read_object())
        return cls(dc_id=dc_id, file_token=file_token, encryption_key=encryption_key, encryption_iv=encryption_iv, file_hashes=file_hashes)

@register_tl
class DcOption(TLObject):
    ID: int = 0x18b7a10d

    def __init__(self, ipv6: bool = False, media_only: bool = False, tcpo_only: bool = False, cdn: bool = False, static: bool = False, this_port_only: bool = False, id: Any = None, ip_address: Any = None, port: Any = None, secret: Any = None) -> None:
        self.ipv6 = ipv6
        self.media_only = media_only
        self.tcpo_only = tcpo_only
        self.cdn = cdn
        self.static = static
        self.this_port_only = this_port_only
        self.id = id
        self.ip_address = ip_address
        self.port = port
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.ipv6:
            flags |= (1 << 0)
        if self.media_only:
            flags |= (1 << 1)
        if self.tcpo_only:
            flags |= (1 << 2)
        if self.cdn:
            flags |= (1 << 3)
        if self.static:
            flags |= (1 << 4)
        if self.this_port_only:
            flags |= (1 << 5)
        if self.secret is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_string(str(self.ip_address or ''))
        writer.write_int32(self.port or 0)
        if self.secret is not None:
            writer.write_bytes(self.secret or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DcOption':
        flags = reader.read_uint32()
        ipv6 = bool(flags & (1 << 0))
        media_only = bool(flags & (1 << 1))
        tcpo_only = bool(flags & (1 << 2))
        cdn = bool(flags & (1 << 3))
        static = bool(flags & (1 << 4))
        this_port_only = bool(flags & (1 << 5))
        id = reader.read_int32()
        ip_address = reader.read_string()
        port = reader.read_int32()
        secret = None
        if flags & (1 << 10):
            secret = reader.read_bytes()
        return cls(ipv6=ipv6, media_only=media_only, tcpo_only=tcpo_only, cdn=cdn, static=static, this_port_only=this_port_only, id=id, ip_address=ip_address, port=port, secret=secret)

@register_tl
class Config(TLObject):
    ID: int = 0xcc1a241e

    def __init__(self, default_p2p_contacts: bool = False, preload_featured_stickers: bool = False, revoke_pm_inbox: bool = False, blocked_mode: bool = False, force_try_ipv6: bool = False, date: Any = None, expires: Any = None, test_mode: Any = None, this_dc: Any = None, dc_options: Any = None, dc_txt_domain_name: Any = None, chat_size_max: Any = None, megagroup_size_max: Any = None, forwarded_count_max: Any = None, online_update_period_ms: Any = None, offline_blur_timeout_ms: Any = None, offline_idle_timeout_ms: Any = None, online_cloud_timeout_ms: Any = None, notify_cloud_delay_ms: Any = None, notify_default_delay_ms: Any = None, push_chat_period_ms: Any = None, push_chat_limit: Any = None, edit_time_limit: Any = None, revoke_time_limit: Any = None, revoke_pm_time_limit: Any = None, rating_e_decay: Any = None, stickers_recent_limit: Any = None, channels_read_media_period: Any = None, tmp_sessions: Any = None, call_receive_timeout_ms: Any = None, call_ring_timeout_ms: Any = None, call_connect_timeout_ms: Any = None, call_packet_timeout_ms: Any = None, me_url_prefix: Any = None, autoupdate_url_prefix: Any = None, gif_search_username: Any = None, venue_search_username: Any = None, img_search_username: Any = None, static_maps_provider: Any = None, caption_length_max: Any = None, message_length_max: Any = None, webfile_dc_id: Any = None, suggested_lang_code: Any = None, lang_pack_version: Any = None, base_lang_pack_version: Any = None, reactions_default: Any = None, autologin_token: Any = None) -> None:
        self.default_p2p_contacts = default_p2p_contacts
        self.preload_featured_stickers = preload_featured_stickers
        self.revoke_pm_inbox = revoke_pm_inbox
        self.blocked_mode = blocked_mode
        self.force_try_ipv6 = force_try_ipv6
        self.date = date
        self.expires = expires
        self.test_mode = test_mode
        self.this_dc = this_dc
        self.dc_options = dc_options
        self.dc_txt_domain_name = dc_txt_domain_name
        self.chat_size_max = chat_size_max
        self.megagroup_size_max = megagroup_size_max
        self.forwarded_count_max = forwarded_count_max
        self.online_update_period_ms = online_update_period_ms
        self.offline_blur_timeout_ms = offline_blur_timeout_ms
        self.offline_idle_timeout_ms = offline_idle_timeout_ms
        self.online_cloud_timeout_ms = online_cloud_timeout_ms
        self.notify_cloud_delay_ms = notify_cloud_delay_ms
        self.notify_default_delay_ms = notify_default_delay_ms
        self.push_chat_period_ms = push_chat_period_ms
        self.push_chat_limit = push_chat_limit
        self.edit_time_limit = edit_time_limit
        self.revoke_time_limit = revoke_time_limit
        self.revoke_pm_time_limit = revoke_pm_time_limit
        self.rating_e_decay = rating_e_decay
        self.stickers_recent_limit = stickers_recent_limit
        self.channels_read_media_period = channels_read_media_period
        self.tmp_sessions = tmp_sessions
        self.call_receive_timeout_ms = call_receive_timeout_ms
        self.call_ring_timeout_ms = call_ring_timeout_ms
        self.call_connect_timeout_ms = call_connect_timeout_ms
        self.call_packet_timeout_ms = call_packet_timeout_ms
        self.me_url_prefix = me_url_prefix
        self.autoupdate_url_prefix = autoupdate_url_prefix
        self.gif_search_username = gif_search_username
        self.venue_search_username = venue_search_username
        self.img_search_username = img_search_username
        self.static_maps_provider = static_maps_provider
        self.caption_length_max = caption_length_max
        self.message_length_max = message_length_max
        self.webfile_dc_id = webfile_dc_id
        self.suggested_lang_code = suggested_lang_code
        self.lang_pack_version = lang_pack_version
        self.base_lang_pack_version = base_lang_pack_version
        self.reactions_default = reactions_default
        self.autologin_token = autologin_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.default_p2p_contacts:
            flags |= (1 << 3)
        if self.preload_featured_stickers:
            flags |= (1 << 4)
        if self.revoke_pm_inbox:
            flags |= (1 << 6)
        if self.blocked_mode:
            flags |= (1 << 8)
        if self.force_try_ipv6:
            flags |= (1 << 14)
        if self.tmp_sessions is not None:
            flags |= (1 << 0)
        if self.autoupdate_url_prefix is not None:
            flags |= (1 << 7)
        if self.gif_search_username is not None:
            flags |= (1 << 9)
        if self.venue_search_username is not None:
            flags |= (1 << 10)
        if self.img_search_username is not None:
            flags |= (1 << 11)
        if self.static_maps_provider is not None:
            flags |= (1 << 12)
        if self.suggested_lang_code is not None:
            flags |= (1 << 2)
        if self.lang_pack_version is not None:
            flags |= (1 << 2)
        if self.base_lang_pack_version is not None:
            flags |= (1 << 2)
        if self.reactions_default is not None:
            flags |= (1 << 15)
        if self.autologin_token is not None:
            flags |= (1 << 16)
        writer.write_uint32(flags)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.expires or 0)
        writer.write_bool(bool(self.test_mode))
        writer.write_int32(self.this_dc or 0)
        writer.write_vector(self.dc_options or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_string(str(self.dc_txt_domain_name or ''))
        writer.write_int32(self.chat_size_max or 0)
        writer.write_int32(self.megagroup_size_max or 0)
        writer.write_int32(self.forwarded_count_max or 0)
        writer.write_int32(self.online_update_period_ms or 0)
        writer.write_int32(self.offline_blur_timeout_ms or 0)
        writer.write_int32(self.offline_idle_timeout_ms or 0)
        writer.write_int32(self.online_cloud_timeout_ms or 0)
        writer.write_int32(self.notify_cloud_delay_ms or 0)
        writer.write_int32(self.notify_default_delay_ms or 0)
        writer.write_int32(self.push_chat_period_ms or 0)
        writer.write_int32(self.push_chat_limit or 0)
        writer.write_int32(self.edit_time_limit or 0)
        writer.write_int32(self.revoke_time_limit or 0)
        writer.write_int32(self.revoke_pm_time_limit or 0)
        writer.write_int32(self.rating_e_decay or 0)
        writer.write_int32(self.stickers_recent_limit or 0)
        writer.write_int32(self.channels_read_media_period or 0)
        if self.tmp_sessions is not None:
            writer.write_int32(self.tmp_sessions or 0)
        writer.write_int32(self.call_receive_timeout_ms or 0)
        writer.write_int32(self.call_ring_timeout_ms or 0)
        writer.write_int32(self.call_connect_timeout_ms or 0)
        writer.write_int32(self.call_packet_timeout_ms or 0)
        writer.write_string(str(self.me_url_prefix or ''))
        if self.autoupdate_url_prefix is not None:
            writer.write_string(str(self.autoupdate_url_prefix or ''))
        if self.gif_search_username is not None:
            writer.write_string(str(self.gif_search_username or ''))
        if self.venue_search_username is not None:
            writer.write_string(str(self.venue_search_username or ''))
        if self.img_search_username is not None:
            writer.write_string(str(self.img_search_username or ''))
        if self.static_maps_provider is not None:
            writer.write_string(str(self.static_maps_provider or ''))
        writer.write_int32(self.caption_length_max or 0)
        writer.write_int32(self.message_length_max or 0)
        writer.write_int32(self.webfile_dc_id or 0)
        if self.suggested_lang_code is not None:
            writer.write_string(str(self.suggested_lang_code or ''))
        if self.lang_pack_version is not None:
            writer.write_int32(self.lang_pack_version or 0)
        if self.base_lang_pack_version is not None:
            writer.write_int32(self.base_lang_pack_version or 0)
        if self.reactions_default is not None:
            if hasattr(self.reactions_default, 'write'):
                self.reactions_default.write(writer)
            else:
                writer.write_bytes(self.reactions_default or b'')
        if self.autologin_token is not None:
            writer.write_string(str(self.autologin_token or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'Config':
        flags = reader.read_uint32()
        default_p2p_contacts = bool(flags & (1 << 3))
        preload_featured_stickers = bool(flags & (1 << 4))
        revoke_pm_inbox = bool(flags & (1 << 6))
        blocked_mode = bool(flags & (1 << 8))
        force_try_ipv6 = bool(flags & (1 << 14))
        date = reader.read_int32()
        expires = reader.read_int32()
        test_mode = reader.read_bool()
        this_dc = reader.read_int32()
        dc_options = reader.read_vector(lambda r: r.read_object())
        dc_txt_domain_name = reader.read_string()
        chat_size_max = reader.read_int32()
        megagroup_size_max = reader.read_int32()
        forwarded_count_max = reader.read_int32()
        online_update_period_ms = reader.read_int32()
        offline_blur_timeout_ms = reader.read_int32()
        offline_idle_timeout_ms = reader.read_int32()
        online_cloud_timeout_ms = reader.read_int32()
        notify_cloud_delay_ms = reader.read_int32()
        notify_default_delay_ms = reader.read_int32()
        push_chat_period_ms = reader.read_int32()
        push_chat_limit = reader.read_int32()
        edit_time_limit = reader.read_int32()
        revoke_time_limit = reader.read_int32()
        revoke_pm_time_limit = reader.read_int32()
        rating_e_decay = reader.read_int32()
        stickers_recent_limit = reader.read_int32()
        channels_read_media_period = reader.read_int32()
        tmp_sessions = None
        if flags & (1 << 0):
            tmp_sessions = reader.read_int32()
        call_receive_timeout_ms = reader.read_int32()
        call_ring_timeout_ms = reader.read_int32()
        call_connect_timeout_ms = reader.read_int32()
        call_packet_timeout_ms = reader.read_int32()
        me_url_prefix = reader.read_string()
        autoupdate_url_prefix = None
        if flags & (1 << 7):
            autoupdate_url_prefix = reader.read_string()
        gif_search_username = None
        if flags & (1 << 9):
            gif_search_username = reader.read_string()
        venue_search_username = None
        if flags & (1 << 10):
            venue_search_username = reader.read_string()
        img_search_username = None
        if flags & (1 << 11):
            img_search_username = reader.read_string()
        static_maps_provider = None
        if flags & (1 << 12):
            static_maps_provider = reader.read_string()
        caption_length_max = reader.read_int32()
        message_length_max = reader.read_int32()
        webfile_dc_id = reader.read_int32()
        suggested_lang_code = None
        if flags & (1 << 2):
            suggested_lang_code = reader.read_string()
        lang_pack_version = None
        if flags & (1 << 2):
            lang_pack_version = reader.read_int32()
        base_lang_pack_version = None
        if flags & (1 << 2):
            base_lang_pack_version = reader.read_int32()
        reactions_default = None
        if flags & (1 << 15):
            reactions_default = reader.read_object()
        autologin_token = None
        if flags & (1 << 16):
            autologin_token = reader.read_string()
        return cls(default_p2p_contacts=default_p2p_contacts, preload_featured_stickers=preload_featured_stickers, revoke_pm_inbox=revoke_pm_inbox, blocked_mode=blocked_mode, force_try_ipv6=force_try_ipv6, date=date, expires=expires, test_mode=test_mode, this_dc=this_dc, dc_options=dc_options, dc_txt_domain_name=dc_txt_domain_name, chat_size_max=chat_size_max, megagroup_size_max=megagroup_size_max, forwarded_count_max=forwarded_count_max, online_update_period_ms=online_update_period_ms, offline_blur_timeout_ms=offline_blur_timeout_ms, offline_idle_timeout_ms=offline_idle_timeout_ms, online_cloud_timeout_ms=online_cloud_timeout_ms, notify_cloud_delay_ms=notify_cloud_delay_ms, notify_default_delay_ms=notify_default_delay_ms, push_chat_period_ms=push_chat_period_ms, push_chat_limit=push_chat_limit, edit_time_limit=edit_time_limit, revoke_time_limit=revoke_time_limit, revoke_pm_time_limit=revoke_pm_time_limit, rating_e_decay=rating_e_decay, stickers_recent_limit=stickers_recent_limit, channels_read_media_period=channels_read_media_period, tmp_sessions=tmp_sessions, call_receive_timeout_ms=call_receive_timeout_ms, call_ring_timeout_ms=call_ring_timeout_ms, call_connect_timeout_ms=call_connect_timeout_ms, call_packet_timeout_ms=call_packet_timeout_ms, me_url_prefix=me_url_prefix, autoupdate_url_prefix=autoupdate_url_prefix, gif_search_username=gif_search_username, venue_search_username=venue_search_username, img_search_username=img_search_username, static_maps_provider=static_maps_provider, caption_length_max=caption_length_max, message_length_max=message_length_max, webfile_dc_id=webfile_dc_id, suggested_lang_code=suggested_lang_code, lang_pack_version=lang_pack_version, base_lang_pack_version=base_lang_pack_version, reactions_default=reactions_default, autologin_token=autologin_token)

@register_tl
class NearestDc(TLObject):
    ID: int = 0x8e1a1775

    def __init__(self, country: Any = None, this_dc: Any = None, nearest_dc: Any = None) -> None:
        self.country = country
        self.this_dc = this_dc
        self.nearest_dc = nearest_dc

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.country or ''))
        writer.write_int32(self.this_dc or 0)
        writer.write_int32(self.nearest_dc or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'NearestDc':
        country = reader.read_string()
        this_dc = reader.read_int32()
        nearest_dc = reader.read_int32()
        return cls(country=country, this_dc=this_dc, nearest_dc=nearest_dc)

@register_tl
class HelpAppUpdate(TLObject):
    ID: int = 0xccbbce30

    def __init__(self, can_not_skip: bool = False, id: Any = None, version: Any = None, text: Any = None, entities: Any = None, document: Any = None, url: Any = None, sticker: Any = None) -> None:
        self.can_not_skip = can_not_skip
        self.id = id
        self.version = version
        self.text = text
        self.entities = entities
        self.document = document
        self.url = url
        self.sticker = sticker

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_not_skip:
            flags |= (1 << 0)
        if self.document is not None:
            flags |= (1 << 1)
        if self.url is not None:
            flags |= (1 << 2)
        if self.sticker is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)
        writer.write_string(str(self.version or ''))
        writer.write_string(str(self.text or ''))
        writer.write_vector(self.entities or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.document is not None:
            if hasattr(self.document, 'write'):
                self.document.write(writer)
            else:
                writer.write_bytes(self.document or b'')
        if self.url is not None:
            writer.write_string(str(self.url or ''))
        if self.sticker is not None:
            if hasattr(self.sticker, 'write'):
                self.sticker.write(writer)
            else:
                writer.write_bytes(self.sticker or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpAppUpdate':
        flags = reader.read_uint32()
        can_not_skip = bool(flags & (1 << 0))
        id = reader.read_int32()
        version = reader.read_string()
        text = reader.read_string()
        entities = reader.read_vector(lambda r: r.read_object())
        document = None
        if flags & (1 << 1):
            document = reader.read_object()
        url = None
        if flags & (1 << 2):
            url = reader.read_string()
        sticker = None
        if flags & (1 << 3):
            sticker = reader.read_object()
        return cls(can_not_skip=can_not_skip, id=id, version=version, text=text, entities=entities, document=document, url=url, sticker=sticker)

@register_tl
class HelpNoAppUpdate(TLObject):
    ID: int = 0xc45a6536

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpNoAppUpdate':
        return cls()

@register_tl
class HelpInviteText(TLObject):
    ID: int = 0x18cb9f78

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.message or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpInviteText':
        message = reader.read_string()
        return cls(message=message)

@register_tl
class EncryptedChatEmpty(TLObject):
    ID: int = 0xab7ec0a0

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedChatEmpty':
        id = reader.read_int32()
        return cls(id=id)

@register_tl
class EncryptedChatWaiting(TLObject):
    ID: int = 0x66b25953

    def __init__(self, id: Any = None, access_hash: Any = None, date: Any = None, admin_id: Any = None, participant_id: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.admin_id or 0)
        writer.write_int64(self.participant_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedChatWaiting':
        id = reader.read_int32()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        return cls(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id)

@register_tl
class EncryptedChatRequested(TLObject):
    ID: int = 0x48f1d94c

    def __init__(self, folder_id: Any = None, id: Any = None, access_hash: Any = None, date: Any = None, admin_id: Any = None, participant_id: Any = None, g_a: Any = None) -> None:
        self.folder_id = folder_id
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_a = g_a

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.folder_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.folder_id is not None:
            writer.write_int32(self.folder_id or 0)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.admin_id or 0)
        writer.write_int64(self.participant_id or 0)
        writer.write_bytes(self.g_a or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedChatRequested':
        flags = reader.read_uint32()
        folder_id = None
        if flags & (1 << 0):
            folder_id = reader.read_int32()
        id = reader.read_int32()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_a = reader.read_bytes()
        return cls(folder_id=folder_id, id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a=g_a)

@register_tl
class EncryptedChat(TLObject):
    ID: int = 0x61f0d4c7

    def __init__(self, id: Any = None, access_hash: Any = None, date: Any = None, admin_id: Any = None, participant_id: Any = None, g_a_or_b: Any = None, key_fingerprint: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_a_or_b = g_a_or_b
        self.key_fingerprint = key_fingerprint

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.admin_id or 0)
        writer.write_int64(self.participant_id or 0)
        writer.write_bytes(self.g_a_or_b or b'')
        writer.write_int64(self.key_fingerprint or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedChat':
        id = reader.read_int32()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_a_or_b = reader.read_bytes()
        key_fingerprint = reader.read_int64()
        return cls(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint)

@register_tl
class EncryptedChatDiscarded(TLObject):
    ID: int = 0x1e1c7c45

    def __init__(self, history_deleted: bool = False, id: Any = None) -> None:
        self.history_deleted = history_deleted
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.history_deleted:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedChatDiscarded':
        flags = reader.read_uint32()
        history_deleted = bool(flags & (1 << 0))
        id = reader.read_int32()
        return cls(history_deleted=history_deleted, id=id)

@register_tl
class InputEncryptedChat(TLObject):
    ID: int = 0xf141b5e1

    def __init__(self, chat_id: Any = None, access_hash: Any = None) -> None:
        self.chat_id = chat_id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.chat_id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputEncryptedChat':
        chat_id = reader.read_int32()
        access_hash = reader.read_int64()
        return cls(chat_id=chat_id, access_hash=access_hash)

@register_tl
class EncryptedFileEmpty(TLObject):
    ID: int = 0xc21f497e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedFileEmpty':
        return cls()

@register_tl
class EncryptedFile(TLObject):
    ID: int = 0xa8008cd8

    def __init__(self, id: Any = None, access_hash: Any = None, size: Any = None, dc_id: Any = None, key_fingerprint: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.size = size
        self.dc_id = dc_id
        self.key_fingerprint = key_fingerprint

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int64(self.size or 0)
        writer.write_int32(self.dc_id or 0)
        writer.write_int32(self.key_fingerprint or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedFile':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        size = reader.read_int64()
        dc_id = reader.read_int32()
        key_fingerprint = reader.read_int32()
        return cls(id=id, access_hash=access_hash, size=size, dc_id=dc_id, key_fingerprint=key_fingerprint)

@register_tl
class InputEncryptedFileEmpty(TLObject):
    ID: int = 0x1837c364

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputEncryptedFileEmpty':
        return cls()

@register_tl
class InputEncryptedFileUploaded(TLObject):
    ID: int = 0x64bd0306

    def __init__(self, id: Any = None, parts: Any = None, md5_checksum: Any = None, key_fingerprint: Any = None) -> None:
        self.id = id
        self.parts = parts
        self.md5_checksum = md5_checksum
        self.key_fingerprint = key_fingerprint

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int32(self.parts or 0)
        writer.write_string(str(self.md5_checksum or ''))
        writer.write_int32(self.key_fingerprint or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputEncryptedFileUploaded':
        id = reader.read_int64()
        parts = reader.read_int32()
        md5_checksum = reader.read_string()
        key_fingerprint = reader.read_int32()
        return cls(id=id, parts=parts, md5_checksum=md5_checksum, key_fingerprint=key_fingerprint)

@register_tl
class InputEncryptedFile(TLObject):
    ID: int = 0x5a17b5e5

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputEncryptedFile':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)

@register_tl
class InputEncryptedFileBigUploaded(TLObject):
    ID: int = 0x2dc173c8

    def __init__(self, id: Any = None, parts: Any = None, key_fingerprint: Any = None) -> None:
        self.id = id
        self.parts = parts
        self.key_fingerprint = key_fingerprint

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int32(self.parts or 0)
        writer.write_int32(self.key_fingerprint or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputEncryptedFileBigUploaded':
        id = reader.read_int64()
        parts = reader.read_int32()
        key_fingerprint = reader.read_int32()
        return cls(id=id, parts=parts, key_fingerprint=key_fingerprint)

@register_tl
class EncryptedMessage(TLObject):
    ID: int = 0xed18c118

    def __init__(self, random_id: Any = None, chat_id: Any = None, date: Any = None, bytes: Any = None, file: Any = None) -> None:
        self.random_id = random_id
        self.chat_id = chat_id
        self.date = date
        self.bytes = bytes
        self.file = file

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        writer.write_int32(self.chat_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_bytes(self.bytes or b'')
        if hasattr(self.file, 'write'):
            self.file.write(writer)
        else:
            writer.write_bytes(self.file or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedMessage':
        random_id = reader.read_int64()
        chat_id = reader.read_int32()
        date = reader.read_int32()
        bytes = reader.read_bytes()
        file = reader.read_object()
        return cls(random_id=random_id, chat_id=chat_id, date=date, bytes=bytes, file=file)

@register_tl
class EncryptedMessageService(TLObject):
    ID: int = 0x23734b06

    def __init__(self, random_id: Any = None, chat_id: Any = None, date: Any = None, bytes: Any = None) -> None:
        self.random_id = random_id
        self.chat_id = chat_id
        self.date = date
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        writer.write_int32(self.chat_id or 0)
        writer.write_int32(self.date or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'EncryptedMessageService':
        random_id = reader.read_int64()
        chat_id = reader.read_int32()
        date = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(random_id=random_id, chat_id=chat_id, date=date, bytes=bytes)

@register_tl
class MessagesDhConfigNotModified(TLObject):
    ID: int = 0xc0e24635

    def __init__(self, random: Any = None) -> None:
        self.random = random

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.random or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDhConfigNotModified':
        random = reader.read_bytes()
        return cls(random=random)

@register_tl
class MessagesDhConfig(TLObject):
    ID: int = 0x2c221edd

    def __init__(self, g: Any = None, p: Any = None, version: Any = None, random: Any = None) -> None:
        self.g = g
        self.p = p
        self.version = version
        self.random = random

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.g or 0)
        writer.write_bytes(self.p or b'')
        writer.write_int32(self.version or 0)
        writer.write_bytes(self.random or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDhConfig':
        g = reader.read_int32()
        p = reader.read_bytes()
        version = reader.read_int32()
        random = reader.read_bytes()
        return cls(g=g, p=p, version=version, random=random)

@register_tl
class MessagesSentEncryptedMessage(TLObject):
    ID: int = 0x560f8935

    def __init__(self, date: Any = None) -> None:
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSentEncryptedMessage':
        date = reader.read_int32()
        return cls(date=date)

@register_tl
class MessagesSentEncryptedFile(TLObject):
    ID: int = 0x9493ff32

    def __init__(self, date: Any = None, file: Any = None) -> None:
        self.date = date
        self.file = file

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.date or 0)
        if hasattr(self.file, 'write'):
            self.file.write(writer)
        else:
            writer.write_bytes(self.file or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSentEncryptedFile':
        date = reader.read_int32()
        file = reader.read_object()
        return cls(date=date, file=file)

@register_tl
class InputDocumentEmpty(TLObject):
    ID: int = 0x72f0eaae

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputDocumentEmpty':
        return cls()

@register_tl
class InputDocument(TLObject):
    ID: int = 0x1abfb575

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
    def read(cls, reader: TLReader) -> 'InputDocument':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        return cls(id=id, access_hash=access_hash, file_reference=file_reference)

@register_tl
class DocumentEmpty(TLObject):
    ID: int = 0x36f8c871

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentEmpty':
        id = reader.read_int64()
        return cls(id=id)

@register_tl
class Document(TLObject):
    ID: int = 0x8fd4c4d8

    def __init__(self, id: Any = None, access_hash: Any = None, file_reference: Any = None, date: Any = None, mime_type: Any = None, size: Any = None, thumbs: Any = None, video_thumbs: Any = None, dc_id: Any = None, attributes: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.file_reference = file_reference
        self.date = date
        self.mime_type = mime_type
        self.size = size
        self.thumbs = thumbs
        self.video_thumbs = video_thumbs
        self.dc_id = dc_id
        self.attributes = attributes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.thumbs is not None:
            flags |= (1 << 0)
        if self.video_thumbs is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_bytes(self.file_reference or b'')
        writer.write_int32(self.date or 0)
        writer.write_string(str(self.mime_type or ''))
        writer.write_int64(self.size or 0)
        if self.thumbs is not None:
            writer.write_vector(self.thumbs or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        if self.video_thumbs is not None:
            writer.write_vector(self.video_thumbs or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_int32(self.dc_id or 0)
        writer.write_vector(self.attributes or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'Document':
        flags = reader.read_uint32()
        id = reader.read_int64()
        access_hash = reader.read_int64()
        file_reference = reader.read_bytes()
        date = reader.read_int32()
        mime_type = reader.read_string()
        size = reader.read_int64()
        thumbs = None
        if flags & (1 << 0):
            thumbs = reader.read_vector(lambda r: r.read_object())
        video_thumbs = None
        if flags & (1 << 1):
            video_thumbs = reader.read_vector(lambda r: r.read_object())
        dc_id = reader.read_int32()
        attributes = reader.read_vector(lambda r: r.read_object())
        return cls(id=id, access_hash=access_hash, file_reference=file_reference, date=date, mime_type=mime_type, size=size, thumbs=thumbs, video_thumbs=video_thumbs, dc_id=dc_id, attributes=attributes)

@register_tl
class HelpSupport(TLObject):
    ID: int = 0x17c6b5f6

    def __init__(self, phone_number: Any = None, user: Any = None) -> None:
        self.phone_number = phone_number
        self.user = user

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.phone_number or ''))
        if hasattr(self.user, 'write'):
            self.user.write(writer)
        else:
            writer.write_bytes(self.user or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpSupport':
        phone_number = reader.read_string()
        user = reader.read_object()
        return cls(phone_number=phone_number, user=user)

@register_tl
class NotifyPeer(TLObject):
    ID: int = 0x9fd40bd8

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'NotifyPeer':
        peer = reader.read_object()
        return cls(peer=peer)

@register_tl
class NotifyUsers(TLObject):
    ID: int = 0xb4c83b4c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'NotifyUsers':
        return cls()

@register_tl
class NotifyChats(TLObject):
    ID: int = 0xc007cec3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'NotifyChats':
        return cls()

@register_tl
class NotifyBroadcasts(TLObject):
    ID: int = 0xd612e8ef

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'NotifyBroadcasts':
        return cls()

@register_tl
class NotifyForumTopic(TLObject):
    ID: int = 0x226e6308

    def __init__(self, peer: Any = None, top_msg_id: Any = None) -> None:
        self.peer = peer
        self.top_msg_id = top_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if hasattr(self.peer, 'write'):
            self.peer.write(writer)
        else:
            writer.write_bytes(self.peer or b'')
        writer.write_int32(self.top_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'NotifyForumTopic':
        peer = reader.read_object()
        top_msg_id = reader.read_int32()
        return cls(peer=peer, top_msg_id=top_msg_id)

@register_tl
class SendMessageTypingAction(TLObject):
    ID: int = 0x16bf744e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageTypingAction':
        return cls()

@register_tl
class SendMessageCancelAction(TLObject):
    ID: int = 0xfd5ec8f5

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageCancelAction':
        return cls()

@register_tl
class SendMessageRecordVideoAction(TLObject):
    ID: int = 0xa187d66f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageRecordVideoAction':
        return cls()

@register_tl
class SendMessageUploadVideoAction(TLObject):
    ID: int = 0xe9763aec

    def __init__(self, progress: Any = None) -> None:
        self.progress = progress

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.progress or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadVideoAction':
        progress = reader.read_int32()
        return cls(progress=progress)

@register_tl
class SendMessageRecordAudioAction(TLObject):
    ID: int = 0xd52f73f7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageRecordAudioAction':
        return cls()

@register_tl
class SendMessageUploadAudioAction(TLObject):
    ID: int = 0xf351d7ab

    def __init__(self, progress: Any = None) -> None:
        self.progress = progress

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.progress or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadAudioAction':
        progress = reader.read_int32()
        return cls(progress=progress)

@register_tl
class SendMessageUploadPhotoAction(TLObject):
    ID: int = 0xd1d34a26

    def __init__(self, progress: Any = None) -> None:
        self.progress = progress

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.progress or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadPhotoAction':
        progress = reader.read_int32()
        return cls(progress=progress)

@register_tl
class SendMessageUploadDocumentAction(TLObject):
    ID: int = 0xaa0cd9e4

    def __init__(self, progress: Any = None) -> None:
        self.progress = progress

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.progress or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadDocumentAction':
        progress = reader.read_int32()
        return cls(progress=progress)

@register_tl
class SendMessageGeoLocationAction(TLObject):
    ID: int = 0x176f8ba1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageGeoLocationAction':
        return cls()

@register_tl
class SendMessageChooseContactAction(TLObject):
    ID: int = 0x628cbc6f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageChooseContactAction':
        return cls()

@register_tl
class SendMessageGamePlayAction(TLObject):
    ID: int = 0xdd6a8f48

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageGamePlayAction':
        return cls()

@register_tl
class SendMessageRecordRoundAction(TLObject):
    ID: int = 0x88f27fbc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageRecordRoundAction':
        return cls()

@register_tl
class SendMessageUploadRoundAction(TLObject):
    ID: int = 0x243e1c66

    def __init__(self, progress: Any = None) -> None:
        self.progress = progress

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.progress or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadRoundAction':
        progress = reader.read_int32()
        return cls(progress=progress)

@register_tl
class SpeakingInGroupCallAction(TLObject):
    ID: int = 0xd92c2285

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SpeakingInGroupCallAction':
        return cls()

@register_tl
class SendMessageHistoryImportAction(TLObject):
    ID: int = 0xdbda9246

    def __init__(self, progress: Any = None) -> None:
        self.progress = progress

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.progress or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageHistoryImportAction':
        progress = reader.read_int32()
        return cls(progress=progress)

@register_tl
class SendMessageChooseStickerAction(TLObject):
    ID: int = 0xb05ac6b1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageChooseStickerAction':
        return cls()

@register_tl
class SendMessageEmojiInteraction(TLObject):
    ID: int = 0x25972bcb

    def __init__(self, emoticon: Any = None, msg_id: Any = None, interaction: Any = None) -> None:
        self.emoticon = emoticon
        self.msg_id = msg_id
        self.interaction = interaction

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.emoticon or ''))
        writer.write_int32(self.msg_id or 0)
        if hasattr(self.interaction, 'write'):
            self.interaction.write(writer)
        else:
            writer.write_bytes(self.interaction or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageEmojiInteraction':
        emoticon = reader.read_string()
        msg_id = reader.read_int32()
        interaction = reader.read_object()
        return cls(emoticon=emoticon, msg_id=msg_id, interaction=interaction)

@register_tl
class SendMessageEmojiInteractionSeen(TLObject):
    ID: int = 0xb665902e

    def __init__(self, emoticon: Any = None) -> None:
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.emoticon or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageEmojiInteractionSeen':
        emoticon = reader.read_string()
        return cls(emoticon=emoticon)

@register_tl
class SendMessageTextDraftAction(TLObject):
    ID: int = 0x376d975c

    def __init__(self, random_id: Any = None, text: Any = None) -> None:
        self.random_id = random_id
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        if hasattr(self.text, 'write'):
            self.text.write(writer)
        else:
            writer.write_bytes(self.text or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageTextDraftAction':
        random_id = reader.read_int64()
        text = reader.read_object()
        return cls(random_id=random_id, text=text)

@register_tl
class ContactsFound(TLObject):
    ID: int = 0xb3134d9d

    def __init__(self, my_results: Any = None, results: Any = None, chats: Any = None, users: Any = None) -> None:
        self.my_results = my_results
        self.results = results
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.my_results or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.results or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsFound':
        my_results = reader.read_vector(lambda r: r.read_object())
        results = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(my_results=my_results, results=results, chats=chats, users=users)

@register_tl
class InputPrivacyKeyStatusTimestamp(TLObject):
    ID: int = 0x4f96cb18

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyStatusTimestamp':
        return cls()

@register_tl
class InputPrivacyKeyChatInvite(TLObject):
    ID: int = 0xbdfb0426

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyChatInvite':
        return cls()

@register_tl
class InputPrivacyKeyPhoneCall(TLObject):
    ID: int = 0xfabadc5f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyPhoneCall':
        return cls()

@register_tl
class InputPrivacyKeyPhoneP2P(TLObject):
    ID: int = 0xdb9e70d2

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyPhoneP2P':
        return cls()

@register_tl
class InputPrivacyKeyForwards(TLObject):
    ID: int = 0xa4dd4c08

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyForwards':
        return cls()

@register_tl
class InputPrivacyKeyProfilePhoto(TLObject):
    ID: int = 0x5719bacc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyProfilePhoto':
        return cls()

@register_tl
class InputPrivacyKeyPhoneNumber(TLObject):
    ID: int = 0x352dafa

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyPhoneNumber':
        return cls()

@register_tl
class InputPrivacyKeyAddedByPhone(TLObject):
    ID: int = 0xd1219bdd

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyAddedByPhone':
        return cls()

@register_tl
class InputPrivacyKeyVoiceMessages(TLObject):
    ID: int = 0xaee69d68

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyVoiceMessages':
        return cls()

@register_tl
class InputPrivacyKeyAbout(TLObject):
    ID: int = 0x3823cc40

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyAbout':
        return cls()

@register_tl
class InputPrivacyKeyBirthday(TLObject):
    ID: int = 0xd65a11cc

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyBirthday':
        return cls()

@register_tl
class InputPrivacyKeyStarGiftsAutoSave(TLObject):
    ID: int = 0xe1732341

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyStarGiftsAutoSave':
        return cls()

@register_tl
class InputPrivacyKeyNoPaidMessages(TLObject):
    ID: int = 0xbdc597b4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeyNoPaidMessages':
        return cls()

@register_tl
class InputPrivacyKeySavedMusic(TLObject):
    ID: int = 0x4dbe9226

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyKeySavedMusic':
        return cls()

@register_tl
class PrivacyKeyStatusTimestamp(TLObject):
    ID: int = 0xbc2eab30

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyStatusTimestamp':
        return cls()

@register_tl
class PrivacyKeyChatInvite(TLObject):
    ID: int = 0x500e6dfa

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyChatInvite':
        return cls()

@register_tl
class PrivacyKeyPhoneCall(TLObject):
    ID: int = 0x3d662b7b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyPhoneCall':
        return cls()

@register_tl
class PrivacyKeyPhoneP2P(TLObject):
    ID: int = 0x39491cc8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyPhoneP2P':
        return cls()

@register_tl
class PrivacyKeyForwards(TLObject):
    ID: int = 0x69ec56a3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyForwards':
        return cls()

@register_tl
class PrivacyKeyProfilePhoto(TLObject):
    ID: int = 0x96151fed

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyProfilePhoto':
        return cls()

@register_tl
class PrivacyKeyPhoneNumber(TLObject):
    ID: int = 0xd19ae46d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyPhoneNumber':
        return cls()

@register_tl
class PrivacyKeyAddedByPhone(TLObject):
    ID: int = 0x42ffd42b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyAddedByPhone':
        return cls()

@register_tl
class PrivacyKeyVoiceMessages(TLObject):
    ID: int = 0x697f414

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyVoiceMessages':
        return cls()

@register_tl
class PrivacyKeyAbout(TLObject):
    ID: int = 0xa486b761

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyAbout':
        return cls()

@register_tl
class PrivacyKeyBirthday(TLObject):
    ID: int = 0x2000a518

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyBirthday':
        return cls()

@register_tl
class PrivacyKeyStarGiftsAutoSave(TLObject):
    ID: int = 0x2ca4fdf8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyStarGiftsAutoSave':
        return cls()

@register_tl
class PrivacyKeyNoPaidMessages(TLObject):
    ID: int = 0x17d348d2

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeyNoPaidMessages':
        return cls()

@register_tl
class PrivacyKeySavedMusic(TLObject):
    ID: int = 0xff7a571b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyKeySavedMusic':
        return cls()

@register_tl
class InputPrivacyValueAllowContacts(TLObject):
    ID: int = 0xd09e07b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowContacts':
        return cls()

@register_tl
class InputPrivacyValueAllowAll(TLObject):
    ID: int = 0x184b35ce

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowAll':
        return cls()

@register_tl
class InputPrivacyValueAllowUsers(TLObject):
    ID: int = 0x131cc67f

    def __init__(self, users: Any = None) -> None:
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowUsers':
        users = reader.read_vector(lambda r: r.read_object())
        return cls(users=users)

@register_tl
class InputPrivacyValueDisallowContacts(TLObject):
    ID: int = 0xba52007

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueDisallowContacts':
        return cls()

@register_tl
class InputPrivacyValueDisallowAll(TLObject):
    ID: int = 0xd66b66c9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueDisallowAll':
        return cls()

@register_tl
class InputPrivacyValueDisallowUsers(TLObject):
    ID: int = 0x90110467

    def __init__(self, users: Any = None) -> None:
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueDisallowUsers':
        users = reader.read_vector(lambda r: r.read_object())
        return cls(users=users)

@register_tl
class InputPrivacyValueAllowChatParticipants(TLObject):
    ID: int = 0x840649cf

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(chats=chats)

@register_tl
class InputPrivacyValueDisallowChatParticipants(TLObject):
    ID: int = 0xe94f0f86

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueDisallowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(chats=chats)

@register_tl
class InputPrivacyValueAllowCloseFriends(TLObject):
    ID: int = 0x2f453e49

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowCloseFriends':
        return cls()

@register_tl
class InputPrivacyValueAllowPremium(TLObject):
    ID: int = 0x77cdc9f1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowPremium':
        return cls()

@register_tl
class InputPrivacyValueAllowBots(TLObject):
    ID: int = 0x5a4fcce5

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowBots':
        return cls()

@register_tl
class InputPrivacyValueDisallowBots(TLObject):
    ID: int = 0xc4e57915

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueDisallowBots':
        return cls()

@register_tl
class PrivacyValueAllowContacts(TLObject):
    ID: int = 0xfffe1bac

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowContacts':
        return cls()

@register_tl
class PrivacyValueAllowAll(TLObject):
    ID: int = 0x65427b82

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowAll':
        return cls()

@register_tl
class PrivacyValueAllowUsers(TLObject):
    ID: int = 0xb8905fb2

    def __init__(self, users: Any = None) -> None:
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowUsers':
        users = reader.read_vector(lambda r: r.read_object())
        return cls(users=users)

@register_tl
class PrivacyValueDisallowContacts(TLObject):
    ID: int = 0xf888fa1a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueDisallowContacts':
        return cls()

@register_tl
class PrivacyValueDisallowAll(TLObject):
    ID: int = 0x8b73e763

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueDisallowAll':
        return cls()

@register_tl
class PrivacyValueDisallowUsers(TLObject):
    ID: int = 0xe4621141

    def __init__(self, users: Any = None) -> None:
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueDisallowUsers':
        users = reader.read_vector(lambda r: r.read_object())
        return cls(users=users)

@register_tl
class PrivacyValueAllowChatParticipants(TLObject):
    ID: int = 0x6b134e8e

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(chats=chats)

@register_tl
class PrivacyValueDisallowChatParticipants(TLObject):
    ID: int = 0x41c87565

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueDisallowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_object())
        return cls(chats=chats)

@register_tl
class PrivacyValueAllowCloseFriends(TLObject):
    ID: int = 0xf7e8d89b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowCloseFriends':
        return cls()

@register_tl
class PrivacyValueAllowPremium(TLObject):
    ID: int = 0xece9814b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowPremium':
        return cls()

@register_tl
class PrivacyValueAllowBots(TLObject):
    ID: int = 0x21461b5d

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowBots':
        return cls()

@register_tl
class PrivacyValueDisallowBots(TLObject):
    ID: int = 0xf6a5f82f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueDisallowBots':
        return cls()

@register_tl
class AccountPrivacyRules(TLObject):
    ID: int = 0x50a04e45

    def __init__(self, rules: Any = None, chats: Any = None, users: Any = None) -> None:
        self.rules = rules
        self.chats = chats
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.rules or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.chats or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))
        writer.write_vector(self.users or [], lambda w, x: w.write_object(x) if hasattr(x, 'write') else w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPrivacyRules':
        rules = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(rules=rules, chats=chats, users=users)

@register_tl
class AccountDaysTTL(TLObject):
    ID: int = 0xb8d0afdf

    def __init__(self, days: Any = None) -> None:
        self.days = days

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.days or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountDaysTTL':
        days = reader.read_int32()
        return cls(days=days)

@register_tl
class DocumentAttributeImageSize(TLObject):
    ID: int = 0x6c37c15c

    def __init__(self, w: Any = None, h: Any = None) -> None:
        self.w = w
        self.h = h

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeImageSize':
        w = reader.read_int32()
        h = reader.read_int32()
        return cls(w=w, h=h)

@register_tl
class DocumentAttributeAnimated(TLObject):
    ID: int = 0x11b58939

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeAnimated':
        return cls()

@register_tl
class DocumentAttributeSticker(TLObject):
    ID: int = 0x6319d612

    def __init__(self, mask: bool = False, alt: Any = None, stickerset: Any = None, mask_coords: Any = None) -> None:
        self.mask = mask
        self.alt = alt
        self.stickerset = stickerset
        self.mask_coords = mask_coords

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.mask:
            flags |= (1 << 1)
        if self.mask_coords is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(str(self.alt or ''))
        if hasattr(self.stickerset, 'write'):
            self.stickerset.write(writer)
        else:
            writer.write_bytes(self.stickerset or b'')
        if self.mask_coords is not None:
            if hasattr(self.mask_coords, 'write'):
                self.mask_coords.write(writer)
            else:
                writer.write_bytes(self.mask_coords or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeSticker':
        flags = reader.read_uint32()
        mask = bool(flags & (1 << 1))
        alt = reader.read_string()
        stickerset = reader.read_object()
        mask_coords = None
        if flags & (1 << 0):
            mask_coords = reader.read_object()
        return cls(mask=mask, alt=alt, stickerset=stickerset, mask_coords=mask_coords)

@register_tl
class DocumentAttributeVideo(TLObject):
    ID: int = 0x43c57c48

    def __init__(self, round_message: bool = False, supports_streaming: bool = False, nosound: bool = False, duration: Any = None, w: Any = None, h: Any = None, preload_prefix_size: Any = None, video_start_ts: Any = None, video_codec: Any = None) -> None:
        self.round_message = round_message
        self.supports_streaming = supports_streaming
        self.nosound = nosound
        self.duration = duration
        self.w = w
        self.h = h
        self.preload_prefix_size = preload_prefix_size
        self.video_start_ts = video_start_ts
        self.video_codec = video_codec

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.round_message:
            flags |= (1 << 0)
        if self.supports_streaming:
            flags |= (1 << 1)
        if self.nosound:
            flags |= (1 << 3)
        if self.preload_prefix_size is not None:
            flags |= (1 << 2)
        if self.video_start_ts is not None:
            flags |= (1 << 4)
        if self.video_codec is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_double(float(self.duration or 0.0))
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        if self.preload_prefix_size is not None:
            writer.write_int32(self.preload_prefix_size or 0)
        if self.video_start_ts is not None:
            writer.write_double(float(self.video_start_ts or 0.0))
        if self.video_codec is not None:
            writer.write_string(str(self.video_codec or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeVideo':
        flags = reader.read_uint32()
        round_message = bool(flags & (1 << 0))
        supports_streaming = bool(flags & (1 << 1))
        nosound = bool(flags & (1 << 3))
        duration = reader.read_double()
        w = reader.read_int32()
        h = reader.read_int32()
        preload_prefix_size = None
        if flags & (1 << 2):
            preload_prefix_size = reader.read_int32()
        video_start_ts = None
        if flags & (1 << 4):
            video_start_ts = reader.read_double()
        video_codec = None
        if flags & (1 << 5):
            video_codec = reader.read_string()
        return cls(round_message=round_message, supports_streaming=supports_streaming, nosound=nosound, duration=duration, w=w, h=h, preload_prefix_size=preload_prefix_size, video_start_ts=video_start_ts, video_codec=video_codec)

@register_tl
class DocumentAttributeAudio(TLObject):
    ID: int = 0x9852f9c6

    def __init__(self, voice: bool = False, duration: Any = None, title: Any = None, performer: Any = None, waveform: Any = None) -> None:
        self.voice = voice
        self.duration = duration
        self.title = title
        self.performer = performer
        self.waveform = waveform

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.voice:
            flags |= (1 << 10)
        if self.title is not None:
            flags |= (1 << 0)
        if self.performer is not None:
            flags |= (1 << 1)
        if self.waveform is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.duration or 0)
        if self.title is not None:
            writer.write_string(str(self.title or ''))
        if self.performer is not None:
            writer.write_string(str(self.performer or ''))
        if self.waveform is not None:
            writer.write_bytes(self.waveform or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeAudio':
        flags = reader.read_uint32()
        voice = bool(flags & (1 << 10))
        duration = reader.read_int32()
        title = None
        if flags & (1 << 0):
            title = reader.read_string()
        performer = None
        if flags & (1 << 1):
            performer = reader.read_string()
        waveform = None
        if flags & (1 << 2):
            waveform = reader.read_bytes()
        return cls(voice=voice, duration=duration, title=title, performer=performer, waveform=waveform)

@register_tl
class DocumentAttributeFilename(TLObject):
    ID: int = 0x15590068

    def __init__(self, file_name: Any = None) -> None:
        self.file_name = file_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(str(self.file_name or ''))

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeFilename':
        file_name = reader.read_string()
        return cls(file_name=file_name)

@register_tl
class DocumentAttributeHasStickers(TLObject):
    ID: int = 0x9801d2f7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeHasStickers':
        return cls()


@register_tl
class MessageEntityUnknown(TLObject):
    ID: int = 0xBB92BA95
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityUnknown":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityMention(TLObject):
    ID: int = 0xFA04579D
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityMention":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityHashtag(TLObject):
    ID: int = 0x6F12E79F
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityHashtag":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityBotCommand(TLObject):
    ID: int = 0x6CEF8AC7
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityBotCommand":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityUrl(TLObject):
    ID: int = 0x6ED02538
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityUrl":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityEmail(TLObject):
    ID: int = 0x64E475C2
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityEmail":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityBold(TLObject):
    ID: int = 0xBD610BC2
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityBold":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityItalic(TLObject):
    ID: int = 0x826F8E60
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityItalic":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityCode(TLObject):
    ID: int = 0x28B4E794
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityCode":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityPre(TLObject):
    ID: int = 0x739260E3
    def __init__(self, offset: int = 0, length: int = 0, language: str = "") -> None:
        self.offset = offset
        self.length = length
        self.language = language
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
        writer.write_string(self.language or "")
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityPre":
        return cls(offset=reader.read_int32(), length=reader.read_int32(), language=reader.read_string())


@register_tl
class MessageEntityTextUrl(TLObject):
    ID: int = 0x76A6D327
    def __init__(self, offset: int = 0, length: int = 0, url: str = "") -> None:
        self.offset = offset
        self.length = length
        self.url = url
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
        writer.write_string(self.url or "")
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityTextUrl":
        return cls(offset=reader.read_int32(), length=reader.read_int32(), url=reader.read_string())


@register_tl
class MessageEntityPhone(TLObject):
    ID: int = 0x9B69E34B
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityPhone":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityCashtag(TLObject):
    ID: int = 0x4C4E743F
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityCashtag":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityUnderline(TLObject):
    ID: int = 0x9C792A29
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityUnderline":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityStrike(TLObject):
    ID: int = 0xBF613066
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityStrike":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityBlockquote(TLObject):
    ID: int = 0x20DF5D12
    def __init__(self, offset: int = 0, length: int = 0, collapsed: bool = False) -> None:
        self.offset = offset
        self.length = length
        self.collapsed = collapsed
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 1 if self.collapsed else 0
        writer.write_uint32(flags)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityBlockquote":
        flags = reader.read_uint32()
        collapsed = bool(flags & 1)
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length, collapsed=collapsed)


@register_tl
class MessageEntityExpandableBlockquote(TLObject):
    ID: int = 0x79069D51
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityExpandableBlockquote":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntitySpoiler(TLObject):
    ID: int = 0x32CA960F
    def __init__(self, offset: int = 0, length: int = 0) -> None:
        self.offset = offset
        self.length = length
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntitySpoiler":
        return cls(offset=reader.read_int32(), length=reader.read_int32())


@register_tl
class MessageEntityCustomEmoji(TLObject):
    ID: int = 0xC8CF05F8
    def __init__(self, offset: int = 0, length: int = 0, document_id: int = 0) -> None:
        self.offset = offset
        self.length = length
        self.document_id = document_id
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset)
        writer.write_int32(self.length)
        writer.write_int64(self.document_id)
    @classmethod
    def read(cls, reader: TLReader) -> "MessageEntityCustomEmoji":
        return cls(offset=reader.read_int32(), length=reader.read_int32(), document_id=reader.read_int64())


@register_tl
class InputReplyToMessage(TLObject):
    ID: int = 0x22C0848D
    def __init__(
        self,
        reply_to_msg_id: int = 0,
        top_msg_id: int | None = None,
        reply_to_peer_id: Any = None,
        quote_text: str | None = None,
        quote_entities: list[Any] | None = None,
        quote_offset: int | None = None,
    ) -> None:
        self.reply_to_msg_id = reply_to_msg_id
        self.top_msg_id = top_msg_id
        self.reply_to_peer_id = reply_to_peer_id
        self.quote_text = quote_text
        self.quote_entities = quote_entities
        self.quote_offset = quote_offset
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        if self.reply_to_peer_id is not None:
            flags |= (1 << 1)
        if self.quote_text is not None:
            flags |= (1 << 6)
        if self.quote_entities is not None:
            flags |= (1 << 7)
        if self.quote_offset is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        writer.write_int32(self.reply_to_msg_id)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id)
        if self.reply_to_peer_id is not None:
            writer.write_object(self.reply_to_peer_id)
        if self.quote_text is not None:
            writer.write_string(self.quote_text)
        if self.quote_entities is not None:
            writer.write_vector(self.quote_entities, lambda w, x: w.write_object(x))
        if self.quote_offset is not None:
            writer.write_int32(self.quote_offset)
    @classmethod
    def read(cls, reader: TLReader) -> "InputReplyToMessage":
        flags = reader.read_uint32()
        reply_to_msg_id = reader.read_int32()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        reply_to_peer_id = reader.read_object() if (flags & (1 << 1)) else None
        quote_text = reader.read_string() if (flags & (1 << 6)) else None
        quote_entities = reader.read_vector(lambda r: r.read_object()) if (flags & (1 << 7)) else None
        quote_offset = reader.read_int32() if (flags & (1 << 10)) else None
        return cls(
            reply_to_msg_id=reply_to_msg_id,
            top_msg_id=top_msg_id,
            reply_to_peer_id=reply_to_peer_id,
            quote_text=quote_text,
            quote_entities=quote_entities,
            quote_offset=quote_offset,
        )


@register_tl
class ReactionEmpty(TLObject):
    ID: int = 0x79F5D419
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
    @classmethod
    def read(cls, reader: TLReader) -> "ReactionEmpty":
        return cls()


@register_tl
class ReactionEmoji(TLObject):
    ID: int = 0x1B2286B8
    def __init__(self, emoticon: str = "") -> None:
        self.emoticon = emoticon
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon)
    @classmethod
    def read(cls, reader: TLReader) -> "ReactionEmoji":
        return cls(emoticon=reader.read_string())


@register_tl
class ReactionCustomEmoji(TLObject):
    ID: int = 0x8935FC73
    def __init__(self, document_id: int = 0) -> None:
        self.document_id = document_id
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.document_id)
    @classmethod
    def read(cls, reader: TLReader) -> "ReactionCustomEmoji":
        return cls(document_id=reader.read_int64())


@register_tl
class ReactionPaid(TLObject):
    ID: int = 0x523DA4EB
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
    @classmethod
    def read(cls, reader: TLReader) -> "ReactionPaid":
        return cls()


@register_tl
class DataJSON(TLObject):
    ID: int = 0x7D748D04
    def __init__(self, data: str = "{}") -> None:
        self.data = data
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.data)
    @classmethod
    def read(cls, reader: TLReader) -> "DataJSON":
        return cls(data=reader.read_string())


@register_tl
class InputGroupCall(TLObject):
    ID: int = 0xD8AA840F
    def __init__(self, id: int = 0, access_hash: int = 0) -> None:
        self.id = id
        self.access_hash = access_hash
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
    @classmethod
    def read(cls, reader: TLReader) -> "InputGroupCall":
        return cls(id=reader.read_int64(), access_hash=reader.read_int64())


@register_tl
class GroupCallDiscarded(TLObject):
    ID: int = 0x7780BCB4
    def __init__(self, id: int = 0, access_hash: int = 0, duration: int = 0) -> None:
        self.id = id
        self.access_hash = access_hash
        self.duration = duration
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
        writer.write_int32(self.duration)
    @classmethod
    def read(cls, reader: TLReader) -> "GroupCallDiscarded":
        return cls(id=reader.read_int64(), access_hash=reader.read_int64(), duration=reader.read_int32())


@register_tl
class GroupCall(TLObject):
    ID: int = 0xDCB1183C
    def __init__(
        self,
        id: int = 0,
        access_hash: int = 0,
        participants_count: int = 0,
        unmuted_video_limit: int = 0,
        version: int = 0,
        can_change_join_muted: bool = False,
        join_muted: bool = False,
        can_start_video: bool = False,
        record_video_active: bool = False,
        rtmp_stream: bool = False,
        listeners_hidden: bool = False,
        title: str | None = None,
        stream_dc_id: int | None = None,
        record_start_date: int | None = None,
        schedule_date: int | None = None,
        unmuted_video_count: int | None = None,
    ) -> None:
        self.id = id
        self.access_hash = access_hash
        self.participants_count = participants_count
        self.unmuted_video_limit = unmuted_video_limit
        self.version = version
        self.can_change_join_muted = can_change_join_muted
        self.join_muted = join_muted
        self.can_start_video = can_start_video
        self.record_video_active = record_video_active
        self.rtmp_stream = rtmp_stream
        self.listeners_hidden = listeners_hidden
        self.title = title
        self.stream_dc_id = stream_dc_id
        self.record_start_date = record_start_date
        self.schedule_date = schedule_date
        self.unmuted_video_count = unmuted_video_count
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_change_join_muted:
            flags |= (1 << 1)
        if self.join_muted:
            flags |= (1 << 2)
        if self.can_start_video:
            flags |= (1 << 9)
        if self.record_video_active:
            flags |= (1 << 11)
        if self.rtmp_stream:
            flags |= (1 << 12)
        if self.listeners_hidden:
            flags |= (1 << 13)
        if self.title is not None:
            flags |= (1 << 3)
        if self.stream_dc_id is not None:
            flags |= (1 << 4)
        if self.record_start_date is not None:
            flags |= (1 << 5)
        if self.schedule_date is not None:
            flags |= (1 << 7)
        if self.unmuted_video_count is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
        writer.write_int32(self.participants_count)
        if self.title is not None:
            writer.write_string(self.title)
        if self.stream_dc_id is not None:
            writer.write_int32(self.stream_dc_id)
        if self.record_start_date is not None:
            writer.write_int32(self.record_start_date)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date)
        if self.unmuted_video_count is not None:
            writer.write_int32(self.unmuted_video_count)
        writer.write_int32(self.unmuted_video_limit)
        writer.write_int32(self.version)
    @classmethod
    def read(cls, reader: TLReader) -> "GroupCall":
        flags = reader.read_uint32()
        can_change_join_muted = bool(flags & (1 << 1))
        join_muted = bool(flags & (1 << 2))
        can_start_video = bool(flags & (1 << 9))
        record_video_active = bool(flags & (1 << 11))
        rtmp_stream = bool(flags & (1 << 12))
        listeners_hidden = bool(flags & (1 << 13))
        call_id = reader.read_int64()
        access_hash = reader.read_int64()
        participants_count = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 3)) else None
        stream_dc_id = reader.read_int32() if (flags & (1 << 4)) else None
        record_start_date = reader.read_int32() if (flags & (1 << 5)) else None
        schedule_date = reader.read_int32() if (flags & (1 << 7)) else None
        unmuted_video_count = reader.read_int32() if (flags & (1 << 10)) else None
        unmuted_video_limit = reader.read_int32()
        version = reader.read_int32()
        return cls(
            id=call_id,
            access_hash=access_hash,
            participants_count=participants_count,
            unmuted_video_limit=unmuted_video_limit,
            version=version,
            can_change_join_muted=can_change_join_muted,
            join_muted=join_muted,
            can_start_video=can_start_video,
            record_video_active=record_video_active,
            rtmp_stream=rtmp_stream,
            listeners_hidden=listeners_hidden,
            title=title,
            stream_dc_id=stream_dc_id,
            record_start_date=record_start_date,
            schedule_date=schedule_date,
            unmuted_video_count=unmuted_video_count,
        )


@register_tl
class GroupCallParticipant(TLObject):
    ID: int = 0xEBA636FE
    def __init__(
        self,
        peer: Any = None,
        date: int = 0,
        source: int = 0,
        muted: bool = False,
        left: bool = False,
        can_self_unmute: bool = False,
        just_joined: bool = False,
        versioned: bool = False,
        min: bool = False,
        muted_by_you: bool = False,
        volume_by_admin: bool = False,
        is_self: bool = False,
        video_joined: bool = False,
        active_date: int | None = None,
        volume: int | None = None,
        about: str | None = None,
        raise_hand_rating: int | None = None,
    ) -> None:
        self.peer = peer
        self.date = date
        self.source = source
        self.muted = muted
        self.left = left
        self.can_self_unmute = can_self_unmute
        self.just_joined = just_joined
        self.versioned = versioned
        self.min = min
        self.muted_by_you = muted_by_you
        self.volume_by_admin = volume_by_admin
        self.is_self = is_self
        self.video_joined = video_joined
        self.active_date = active_date
        self.volume = volume
        self.about = about
        self.raise_hand_rating = raise_hand_rating
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.muted:
            flags |= (1 << 0)
        if self.left:
            flags |= (1 << 1)
        if self.can_self_unmute:
            flags |= (1 << 2)
        if self.just_joined:
            flags |= (1 << 4)
        if self.versioned:
            flags |= (1 << 5)
        if self.min:
            flags |= (1 << 8)
        if self.muted_by_you:
            flags |= (1 << 9)
        if self.volume_by_admin:
            flags |= (1 << 10)
        if self.is_self:
            flags |= (1 << 12)
        if self.video_joined:
            flags |= (1 << 15)
        if self.active_date is not None:
            flags |= (1 << 3)
        if self.volume is not None:
            flags |= (1 << 7)
        if self.about is not None:
            flags |= (1 << 11)
        if self.raise_hand_rating is not None:
            flags |= (1 << 13)
        writer.write_uint32(flags)
        if hasattr(self.peer, "write"):
            self.peer.write(writer)
        writer.write_int32(self.date)
        if self.active_date is not None:
            writer.write_int32(self.active_date)
        writer.write_int32(self.source)
        if self.volume is not None:
            writer.write_int32(self.volume)
        if self.about is not None:
            writer.write_string(self.about)
        if self.raise_hand_rating is not None:
            writer.write_int64(self.raise_hand_rating)
    @classmethod
    def read(cls, reader: TLReader) -> "GroupCallParticipant":
        flags = reader.read_uint32()
        muted = bool(flags & (1 << 0))
        left = bool(flags & (1 << 1))
        can_self_unmute = bool(flags & (1 << 2))
        just_joined = bool(flags & (1 << 4))
        versioned = bool(flags & (1 << 5))
        min_flag = bool(flags & (1 << 8))
        muted_by_you = bool(flags & (1 << 9))
        volume_by_admin = bool(flags & (1 << 10))
        is_self = bool(flags & (1 << 12))
        video_joined = bool(flags & (1 << 15))
        peer = reader.read_object()
        date = reader.read_int32()
        active_date = reader.read_int32() if (flags & (1 << 3)) else None
        source = reader.read_int32()
        volume = reader.read_int32() if (flags & (1 << 7)) else None
        about = reader.read_string() if (flags & (1 << 11)) else None
        raise_hand_rating = reader.read_int64() if (flags & (1 << 13)) else None
        return cls(
            peer=peer,
            date=date,
            source=source,
            muted=muted,
            left=left,
            can_self_unmute=can_self_unmute,
            just_joined=just_joined,
            versioned=versioned,
            min=min_flag,
            muted_by_you=muted_by_you,
            volume_by_admin=volume_by_admin,
            is_self=is_self,
            video_joined=video_joined,
            active_date=active_date,
            volume=volume,
            about=about,
            raise_hand_rating=raise_hand_rating,
        )


@register_tl
class PhoneGroupCall(TLObject):
    ID: int = 0x9E727AAD
    def __init__(
        self,
        call: Any = None,
        participants: list[Any] | None = None,
        participants_next_offset: str = "",
        chats: list[Any] | None = None,
        users: list[Any] | None = None,
    ) -> None:
        self.call = call
        self.participants = participants or []
        self.participants_next_offset = participants_next_offset
        self.chats = chats or []
        self.users = users or []
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.call)
        writer.write_vector(self.participants, lambda w, x: w.write_object(x))
        writer.write_string(self.participants_next_offset)
        writer.write_vector(self.chats, lambda w, x: w.write_object(x))
        writer.write_vector(self.users, lambda w, x: w.write_object(x))
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneGroupCall":
        call = reader.read_object()
        participants = reader.read_vector(lambda r: r.read_object())
        next_offset = reader.read_string()
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(call=call, participants=participants, participants_next_offset=next_offset, chats=chats, users=users)


@register_tl
class PhoneGroupParticipants(TLObject):
    ID: int = 0xF47751B6
    def __init__(
        self,
        count: int = 0,
        participants: list[Any] | None = None,
        next_offset: str = "",
        chats: list[Any] | None = None,
        users: list[Any] | None = None,
        version: int = 0,
    ) -> None:
        self.count = count
        self.participants = participants or []
        self.next_offset = next_offset
        self.chats = chats or []
        self.users = users or []
        self.version = version
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count)
        writer.write_vector(self.participants, lambda w, x: w.write_object(x))
        writer.write_string(self.next_offset)
        writer.write_vector(self.chats, lambda w, x: w.write_object(x))
        writer.write_vector(self.users, lambda w, x: w.write_object(x))
        writer.write_int32(self.version)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneGroupParticipants":
        count = reader.read_int32()
        participants = reader.read_vector(lambda r: r.read_object())
        next_offset = reader.read_string()
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        version = reader.read_int32()
        return cls(count=count, participants=participants, next_offset=next_offset, chats=chats, users=users, version=version)
