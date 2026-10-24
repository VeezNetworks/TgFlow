from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl
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
