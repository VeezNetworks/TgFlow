from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl



@register_tl
class DecryptedMessage(TLObject):
    ID: int = 0x1f814f1f

    def __init__(self, random_id: Any = None, random_bytes: Any = None, message: Any = None, media: Any = None) -> None:
        self.random_id = random_id
        self.random_bytes = random_bytes
        self.message = message
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        writer.write_bytes(self.random_bytes or b'')
        writer.write_string(self.message or '')
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessage':
        random_id = reader.read_int64()
        random_bytes = reader.read_bytes()
        message = reader.read_string()
        media = reader.read_object()
        return cls(random_id=random_id, random_bytes=random_bytes, message=message, media=media)


@register_tl
class DecryptedMessageService(TLObject):
    ID: int = 0xaa48327d

    def __init__(self, random_id: Any = None, random_bytes: Any = None, action: Any = None) -> None:
        self.random_id = random_id
        self.random_bytes = random_bytes
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        writer.write_bytes(self.random_bytes or b'')
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageService':
        random_id = reader.read_int64()
        random_bytes = reader.read_bytes()
        action = reader.read_object()
        return cls(random_id=random_id, random_bytes=random_bytes, action=action)


@register_tl
class DecryptedMessageMediaEmpty(TLObject):
    ID: int = 0x89f5c4a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaEmpty':
        return cls()


@register_tl
class DecryptedMessageMediaPhoto(TLObject):
    ID: int = 0x32798a8c

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, w: Any = None, h: Any = None, size: Any = None, key: Any = None, iv: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.w = w
        self.h = h
        self.size = size
        self.key = key
        self.iv = iv

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaPhoto':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, w=w, h=h, size=size, key=key, iv=iv)


@register_tl
class DecryptedMessageMediaVideo(TLObject):
    ID: int = 0x4cee6ef3

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, duration: Any = None, w: Any = None, h: Any = None, size: Any = None, key: Any = None, iv: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.duration = duration
        self.w = w
        self.h = h
        self.size = size
        self.key = key
        self.iv = iv

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_int32(self.duration or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaVideo':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        duration = reader.read_int32()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, duration=duration, w=w, h=h, size=size, key=key, iv=iv)


@register_tl
class DecryptedMessageMediaGeoPoint(TLObject):
    ID: int = 0x35480a59

    def __init__(self, lat: Any = None, long: Any = None) -> None:
        self.lat = lat
        self.long = long

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_double(self.lat or 0.0)
        writer.write_double(self.long or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaGeoPoint':
        lat = reader.read_double()
        long = reader.read_double()
        return cls(lat=lat, long=long)


@register_tl
class DecryptedMessageMediaContact(TLObject):
    ID: int = 0x588a0a97

    def __init__(self, phone_number: Any = None, first_name: Any = None, last_name: Any = None, user_id: Any = None) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.phone_number or '')
        writer.write_string(self.first_name or '')
        writer.write_string(self.last_name or '')
        writer.write_int32(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaContact':
        phone_number = reader.read_string()
        first_name = reader.read_string()
        last_name = reader.read_string()
        user_id = reader.read_int32()
        return cls(phone_number=phone_number, first_name=first_name, last_name=last_name, user_id=user_id)


@register_tl
class DecryptedMessageActionSetMessageTTL(TLObject):
    ID: int = 0xa1733aec

    def __init__(self, ttl_seconds: Any = None) -> None:
        self.ttl_seconds = ttl_seconds

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.ttl_seconds or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionSetMessageTTL':
        ttl_seconds = reader.read_int32()
        return cls(ttl_seconds=ttl_seconds)


@register_tl
class DecryptedMessageMediaDocument(TLObject):
    ID: int = 0xb095434b

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, file_name: Any = None, mime_type: Any = None, size: Any = None, key: Any = None, iv: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.file_name = file_name
        self.mime_type = mime_type
        self.size = size
        self.key = key
        self.iv = iv

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_string(self.file_name or '')
        writer.write_string(self.mime_type or '')
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaDocument':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        file_name = reader.read_string()
        mime_type = reader.read_string()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, file_name=file_name, mime_type=mime_type, size=size, key=key, iv=iv)


@register_tl
class DecryptedMessageMediaAudio(TLObject):
    ID: int = 0x6080758f

    def __init__(self, duration: Any = None, size: Any = None, key: Any = None, iv: Any = None) -> None:
        self.duration = duration
        self.size = size
        self.key = key
        self.iv = iv

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.duration or 0)
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaAudio':
        duration = reader.read_int32()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        return cls(duration=duration, size=size, key=key, iv=iv)


@register_tl
class DecryptedMessageActionReadMessages(TLObject):
    ID: int = 0xc4f40be

    def __init__(self, random_ids: Any = None) -> None:
        self.random_ids = random_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.random_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionReadMessages':
        random_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(random_ids=random_ids)


@register_tl
class DecryptedMessageActionDeleteMessages(TLObject):
    ID: int = 0x65614304

    def __init__(self, random_ids: Any = None) -> None:
        self.random_ids = random_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.random_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionDeleteMessages':
        random_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(random_ids=random_ids)


@register_tl
class DecryptedMessageActionScreenshotMessages(TLObject):
    ID: int = 0x8ac1f475

    def __init__(self, random_ids: Any = None) -> None:
        self.random_ids = random_ids

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.random_ids or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionScreenshotMessages':
        random_ids = reader.read_vector(lambda r: r.read_int64())
        return cls(random_ids=random_ids)


@register_tl
class DecryptedMessageActionFlushHistory(TLObject):
    ID: int = 0x6719e45c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionFlushHistory':
        return cls()


@register_tl
class DecryptedMessage(TLObject):
    ID: int = 0x204d3878

    def __init__(self, random_id: Any = None, ttl: Any = None, message: Any = None, media: Any = None) -> None:
        self.random_id = random_id
        self.ttl = ttl
        self.message = message
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        writer.write_int32(self.ttl or 0)
        writer.write_string(self.message or '')
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessage':
        random_id = reader.read_int64()
        ttl = reader.read_int32()
        message = reader.read_string()
        media = reader.read_object()
        return cls(random_id=random_id, ttl=ttl, message=message, media=media)


@register_tl
class DecryptedMessageService(TLObject):
    ID: int = 0x73164160

    def __init__(self, random_id: Any = None, action: Any = None) -> None:
        self.random_id = random_id
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageService':
        random_id = reader.read_int64()
        action = reader.read_object()
        return cls(random_id=random_id, action=action)


@register_tl
class DecryptedMessageMediaVideo(TLObject):
    ID: int = 0x524a415d

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, duration: Any = None, mime_type: Any = None, w: Any = None, h: Any = None, size: Any = None, key: Any = None, iv: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.duration = duration
        self.mime_type = mime_type
        self.w = w
        self.h = h
        self.size = size
        self.key = key
        self.iv = iv

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_int32(self.duration or 0)
        writer.write_string(self.mime_type or '')
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaVideo':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        duration = reader.read_int32()
        mime_type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, duration=duration, mime_type=mime_type, w=w, h=h, size=size, key=key, iv=iv)


@register_tl
class DecryptedMessageMediaAudio(TLObject):
    ID: int = 0x57e0a9cb

    def __init__(self, duration: Any = None, mime_type: Any = None, size: Any = None, key: Any = None, iv: Any = None) -> None:
        self.duration = duration
        self.mime_type = mime_type
        self.size = size
        self.key = key
        self.iv = iv

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.duration or 0)
        writer.write_string(self.mime_type or '')
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaAudio':
        duration = reader.read_int32()
        mime_type = reader.read_string()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        return cls(duration=duration, mime_type=mime_type, size=size, key=key, iv=iv)


@register_tl
class DecryptedMessageLayer(TLObject):
    ID: int = 0x1be31789

    def __init__(self, random_bytes: Any = None, layer: Any = None, in_seq_no: Any = None, out_seq_no: Any = None, message: Any = None) -> None:
        self.random_bytes = random_bytes
        self.layer = layer
        self.in_seq_no = in_seq_no
        self.out_seq_no = out_seq_no
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.random_bytes or b'')
        writer.write_int32(self.layer or 0)
        writer.write_int32(self.in_seq_no or 0)
        writer.write_int32(self.out_seq_no or 0)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageLayer':
        random_bytes = reader.read_bytes()
        layer = reader.read_int32()
        in_seq_no = reader.read_int32()
        out_seq_no = reader.read_int32()
        message = reader.read_object()
        return cls(random_bytes=random_bytes, layer=layer, in_seq_no=in_seq_no, out_seq_no=out_seq_no, message=message)


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
    ID: int = 0x92042ff7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadVideoAction':
        return cls()


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
    ID: int = 0xe6ac8a6f

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadAudioAction':
        return cls()


@register_tl
class SendMessageUploadPhotoAction(TLObject):
    ID: int = 0x990a3c1a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadPhotoAction':
        return cls()


@register_tl
class SendMessageUploadDocumentAction(TLObject):
    ID: int = 0x8faee98e

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadDocumentAction':
        return cls()


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
class DecryptedMessageActionResend(TLObject):
    ID: int = 0x511110b0

    def __init__(self, start_seq_no: Any = None, end_seq_no: Any = None) -> None:
        self.start_seq_no = start_seq_no
        self.end_seq_no = end_seq_no

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.start_seq_no or 0)
        writer.write_int32(self.end_seq_no or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionResend':
        start_seq_no = reader.read_int32()
        end_seq_no = reader.read_int32()
        return cls(start_seq_no=start_seq_no, end_seq_no=end_seq_no)


@register_tl
class DecryptedMessageActionNotifyLayer(TLObject):
    ID: int = 0xf3048883

    def __init__(self, layer: Any = None) -> None:
        self.layer = layer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.layer or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionNotifyLayer':
        layer = reader.read_int32()
        return cls(layer=layer)


@register_tl
class DecryptedMessageActionTyping(TLObject):
    ID: int = 0xccb27641

    def __init__(self, action: Any = None) -> None:
        self.action = action

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.action is not None and hasattr(self.action, 'write'): self.action.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionTyping':
        action = reader.read_object()
        return cls(action=action)


@register_tl
class DecryptedMessageActionRequestKey(TLObject):
    ID: int = 0xf3c9611b

    def __init__(self, exchange_id: Any = None, g_a: Any = None) -> None:
        self.exchange_id = exchange_id
        self.g_a = g_a

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.exchange_id or 0)
        writer.write_bytes(self.g_a or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionRequestKey':
        exchange_id = reader.read_int64()
        g_a = reader.read_bytes()
        return cls(exchange_id=exchange_id, g_a=g_a)


@register_tl
class DecryptedMessageActionAcceptKey(TLObject):
    ID: int = 0x6fe1735b

    def __init__(self, exchange_id: Any = None, g_b: Any = None, key_fingerprint: Any = None) -> None:
        self.exchange_id = exchange_id
        self.g_b = g_b
        self.key_fingerprint = key_fingerprint

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.exchange_id or 0)
        writer.write_bytes(self.g_b or b'')
        writer.write_int64(self.key_fingerprint or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionAcceptKey':
        exchange_id = reader.read_int64()
        g_b = reader.read_bytes()
        key_fingerprint = reader.read_int64()
        return cls(exchange_id=exchange_id, g_b=g_b, key_fingerprint=key_fingerprint)


@register_tl
class DecryptedMessageActionAbortKey(TLObject):
    ID: int = 0xdd05ec6b

    def __init__(self, exchange_id: Any = None) -> None:
        self.exchange_id = exchange_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.exchange_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionAbortKey':
        exchange_id = reader.read_int64()
        return cls(exchange_id=exchange_id)


@register_tl
class DecryptedMessageActionCommitKey(TLObject):
    ID: int = 0xec2e0b9b

    def __init__(self, exchange_id: Any = None, key_fingerprint: Any = None) -> None:
        self.exchange_id = exchange_id
        self.key_fingerprint = key_fingerprint

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.exchange_id or 0)
        writer.write_int64(self.key_fingerprint or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionCommitKey':
        exchange_id = reader.read_int64()
        key_fingerprint = reader.read_int64()
        return cls(exchange_id=exchange_id, key_fingerprint=key_fingerprint)


@register_tl
class DecryptedMessageActionNoop(TLObject):
    ID: int = 0xa82fdd63

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageActionNoop':
        return cls()


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
    ID: int = 0xfb0a5727

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeSticker':
        return cls()


@register_tl
class DocumentAttributeVideo(TLObject):
    ID: int = 0x5910cccb

    def __init__(self, duration: Any = None, w: Any = None, h: Any = None) -> None:
        self.duration = duration
        self.w = w
        self.h = h

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.duration or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeVideo':
        duration = reader.read_int32()
        w = reader.read_int32()
        h = reader.read_int32()
        return cls(duration=duration, w=w, h=h)


@register_tl
class DocumentAttributeAudio(TLObject):
    ID: int = 0x51448e5

    def __init__(self, duration: Any = None) -> None:
        self.duration = duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeAudio':
        duration = reader.read_int32()
        return cls(duration=duration)


@register_tl
class DocumentAttributeFilename(TLObject):
    ID: int = 0x15590068

    def __init__(self, file_name: Any = None) -> None:
        self.file_name = file_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.file_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeFilename':
        file_name = reader.read_string()
        return cls(file_name=file_name)


@register_tl
class PhotoSizeEmpty(TLObject):
    ID: int = 0xe17e23c

    def __init__(self, type: Any = None) -> None:
        self.type = type

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.type or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSizeEmpty':
        type = reader.read_string()
        return cls(type=type)


@register_tl
class PhotoSize(TLObject):
    ID: int = 0x77bfb61b

    def __init__(self, type: Any = None, location: Any = None, w: Any = None, h: Any = None, size: Any = None) -> None:
        self.type = type
        self.location = location
        self.w = w
        self.h = h
        self.size = size

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.type or '')
        if self.location is not None and hasattr(self.location, 'write'): self.location.write(writer)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoSize':
        type = reader.read_string()
        location = reader.read_object()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        return cls(type=type, location=location, w=w, h=h, size=size)


@register_tl
class PhotoCachedSize(TLObject):
    ID: int = 0xe9a734fa

    def __init__(self, type: Any = None, location: Any = None, w: Any = None, h: Any = None, bytes: Any = None) -> None:
        self.type = type
        self.location = location
        self.w = w
        self.h = h
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.type or '')
        if self.location is not None and hasattr(self.location, 'write'): self.location.write(writer)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotoCachedSize':
        type = reader.read_string()
        location = reader.read_object()
        w = reader.read_int32()
        h = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(type=type, location=location, w=w, h=h, bytes=bytes)


@register_tl
class FileLocationUnavailable(TLObject):
    ID: int = 0x7c596b46

    def __init__(self, volume_id: Any = None, local_id: Any = None, secret: Any = None) -> None:
        self.volume_id = volume_id
        self.local_id = local_id
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.volume_id or 0)
        writer.write_int32(self.local_id or 0)
        writer.write_int64(self.secret or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'FileLocationUnavailable':
        volume_id = reader.read_int64()
        local_id = reader.read_int32()
        secret = reader.read_int64()
        return cls(volume_id=volume_id, local_id=local_id, secret=secret)


@register_tl
class FileLocation(TLObject):
    ID: int = 0x53d69076

    def __init__(self, dc_id: Any = None, volume_id: Any = None, local_id: Any = None, secret: Any = None) -> None:
        self.dc_id = dc_id
        self.volume_id = volume_id
        self.local_id = local_id
        self.secret = secret

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id or 0)
        writer.write_int64(self.volume_id or 0)
        writer.write_int32(self.local_id or 0)
        writer.write_int64(self.secret or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'FileLocation':
        dc_id = reader.read_int32()
        volume_id = reader.read_int64()
        local_id = reader.read_int32()
        secret = reader.read_int64()
        return cls(dc_id=dc_id, volume_id=volume_id, local_id=local_id, secret=secret)


@register_tl
class DecryptedMessageMediaExternalDocument(TLObject):
    ID: int = 0xfa95b0dd

    def __init__(self, id: Any = None, access_hash: Any = None, date: Any = None, mime_type: Any = None, size: Any = None, thumb: Any = None, dc_id: Any = None, attributes: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.mime_type = mime_type
        self.size = size
        self.thumb = thumb
        self.dc_id = dc_id
        self.attributes = attributes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_string(self.mime_type or '')
        writer.write_int32(self.size or 0)
        if self.thumb is not None and hasattr(self.thumb, 'write'): self.thumb.write(writer)
        writer.write_int32(self.dc_id or 0)
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaExternalDocument':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        mime_type = reader.read_string()
        size = reader.read_int32()
        thumb = reader.read_object()
        dc_id = reader.read_int32()
        attributes = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id, access_hash=access_hash, date=date, mime_type=mime_type, size=size, thumb=thumb, dc_id=dc_id, attributes=attributes)


@register_tl
class DecryptedMessage(TLObject):
    ID: int = 0x36b091de

    def __init__(self, media: Any = None, entities: Any = None, via_bot_name: Any = None, reply_to_random_id: Any = None, random_id: Any = None, ttl: Any = None, message: Any = None) -> None:
        self.media = media
        self.entities = entities
        self.via_bot_name = via_bot_name
        self.reply_to_random_id = reply_to_random_id
        self.random_id = random_id
        self.ttl = ttl
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.media is not None:
            flags |= (1 << 9)
        if self.entities is not None:
            flags |= (1 << 7)
        if self.via_bot_name is not None:
            flags |= (1 << 11)
        if self.reply_to_random_id is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int64(self.random_id or 0)
        writer.write_int32(self.ttl or 0)
        writer.write_string(self.message or '')
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.via_bot_name is not None:
            writer.write_string(self.via_bot_name or '')
        if self.reply_to_random_id is not None:
            writer.write_int64(self.reply_to_random_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessage':
        flags = reader.read_uint32()
        random_id = reader.read_int64()
        ttl = reader.read_int32()
        message = reader.read_string()
        media = reader.read_object() if (flags & (1 << 9)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 7)) else None
        via_bot_name = reader.read_string() if (flags & (1 << 11)) else None
        reply_to_random_id = reader.read_int64() if (flags & (1 << 3)) else None
        return cls(random_id=random_id, ttl=ttl, message=message, media=media, entities=entities, via_bot_name=via_bot_name, reply_to_random_id=reply_to_random_id)


@register_tl
class DecryptedMessageMediaPhoto(TLObject):
    ID: int = 0xf1fa8d78

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, w: Any = None, h: Any = None, size: Any = None, key: Any = None, iv: Any = None, caption: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.w = w
        self.h = h
        self.size = size
        self.key = key
        self.iv = iv
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')
        writer.write_string(self.caption or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaPhoto':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        caption = reader.read_string()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, w=w, h=h, size=size, key=key, iv=iv, caption=caption)


@register_tl
class DecryptedMessageMediaVideo(TLObject):
    ID: int = 0x970c8c0e

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, duration: Any = None, mime_type: Any = None, w: Any = None, h: Any = None, size: Any = None, key: Any = None, iv: Any = None, caption: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.duration = duration
        self.mime_type = mime_type
        self.w = w
        self.h = h
        self.size = size
        self.key = key
        self.iv = iv
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_int32(self.duration or 0)
        writer.write_string(self.mime_type or '')
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')
        writer.write_string(self.caption or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaVideo':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        duration = reader.read_int32()
        mime_type = reader.read_string()
        w = reader.read_int32()
        h = reader.read_int32()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        caption = reader.read_string()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, duration=duration, mime_type=mime_type, w=w, h=h, size=size, key=key, iv=iv, caption=caption)


@register_tl
class DecryptedMessageMediaDocument(TLObject):
    ID: int = 0x7afe8ae2

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, mime_type: Any = None, size: Any = None, key: Any = None, iv: Any = None, attributes: Any = None, caption: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.mime_type = mime_type
        self.size = size
        self.key = key
        self.iv = iv
        self.attributes = attributes
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_string(self.mime_type or '')
        writer.write_int32(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.caption or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaDocument':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        mime_type = reader.read_string()
        size = reader.read_int32()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        attributes = reader.read_vector(lambda r: reader.read_object())
        caption = reader.read_string()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, mime_type=mime_type, size=size, key=key, iv=iv, attributes=attributes, caption=caption)


@register_tl
class DocumentAttributeSticker(TLObject):
    ID: int = 0x3a556302

    def __init__(self, alt: Any = None, stickerset: Any = None) -> None:
        self.alt = alt
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.alt or '')
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeSticker':
        alt = reader.read_string()
        stickerset = reader.read_object()
        return cls(alt=alt, stickerset=stickerset)


@register_tl
class DocumentAttributeAudio(TLObject):
    ID: int = 0xded218e0

    def __init__(self, duration: Any = None, title: Any = None, performer: Any = None) -> None:
        self.duration = duration
        self.title = title
        self.performer = performer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.duration or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.performer or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeAudio':
        duration = reader.read_int32()
        title = reader.read_string()
        performer = reader.read_string()
        return cls(duration=duration, title=title, performer=performer)


@register_tl
class MessageEntityUnknown(TLObject):
    ID: int = 0xbb92ba95

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityUnknown':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityMention(TLObject):
    ID: int = 0xfa04579d

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityMention':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityHashtag(TLObject):
    ID: int = 0x6f635b0d

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityHashtag':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityBotCommand(TLObject):
    ID: int = 0x6cef8ac7

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityBotCommand':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityUrl(TLObject):
    ID: int = 0x6ed02538

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityUrl':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityEmail(TLObject):
    ID: int = 0x64e475c2

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityEmail':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityBold(TLObject):
    ID: int = 0xbd610bc9

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityBold':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityItalic(TLObject):
    ID: int = 0x826f8b60

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityItalic':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityCode(TLObject):
    ID: int = 0x28a20571

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityCode':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityPre(TLObject):
    ID: int = 0x73924be0

    def __init__(self, offset: Any = None, length: Any = None, language: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.language = language

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_string(self.language or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityPre':
        offset = reader.read_int32()
        length = reader.read_int32()
        language = reader.read_string()
        return cls(offset=offset, length=length, language=language)


@register_tl
class MessageEntityTextUrl(TLObject):
    ID: int = 0x76a6d327

    def __init__(self, offset: Any = None, length: Any = None, url: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityTextUrl':
        offset = reader.read_int32()
        length = reader.read_int32()
        url = reader.read_string()
        return cls(offset=offset, length=length, url=url)


@register_tl
class InputStickerSetShortName(TLObject):
    ID: int = 0x861cc8a0

    def __init__(self, short_name: Any = None) -> None:
        self.short_name = short_name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.short_name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetShortName':
        short_name = reader.read_string()
        return cls(short_name=short_name)


@register_tl
class InputStickerSetEmpty(TLObject):
    ID: int = 0xffb62b95

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetEmpty':
        return cls()


@register_tl
class DecryptedMessageMediaVenue(TLObject):
    ID: int = 0x8a0df56f

    def __init__(self, lat: Any = None, long: Any = None, title: Any = None, address: Any = None, provider: Any = None, venue_id: Any = None) -> None:
        self.lat = lat
        self.long = long
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_double(self.lat or 0.0)
        writer.write_double(self.long or 0.0)
        writer.write_string(self.title or '')
        writer.write_string(self.address or '')
        writer.write_string(self.provider or '')
        writer.write_string(self.venue_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaVenue':
        lat = reader.read_double()
        long = reader.read_double()
        title = reader.read_string()
        address = reader.read_string()
        provider = reader.read_string()
        venue_id = reader.read_string()
        return cls(lat=lat, long=long, title=title, address=address, provider=provider, venue_id=venue_id)


@register_tl
class DecryptedMessageMediaWebPage(TLObject):
    ID: int = 0xe50511d8

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaWebPage':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class DocumentAttributeAudio(TLObject):
    ID: int = 0x9852f9c6

    def __init__(self, voice: bool = False, title: Any = None, performer: Any = None, waveform: Any = None, duration: Any = None) -> None:
        self.voice = voice
        self.title = title
        self.performer = performer
        self.waveform = waveform
        self.duration = duration

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
            writer.write_string(self.title or '')
        if self.performer is not None:
            writer.write_string(self.performer or '')
        if self.waveform is not None:
            writer.write_bytes(self.waveform or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeAudio':
        flags = reader.read_uint32()
        voice = bool(flags & (1 << 10))
        duration = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        performer = reader.read_string() if (flags & (1 << 1)) else None
        waveform = reader.read_bytes() if (flags & (1 << 2)) else None
        return cls(voice=voice, duration=duration, title=title, performer=performer, waveform=waveform)


@register_tl
class DocumentAttributeVideo(TLObject):
    ID: int = 0xef02ce6

    def __init__(self, round_message: bool = False, duration: Any = None, w: Any = None, h: Any = None) -> None:
        self.round_message = round_message
        self.duration = duration
        self.w = w
        self.h = h

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.round_message:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int32(self.duration or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeVideo':
        flags = reader.read_uint32()
        round_message = bool(flags & (1 << 0))
        duration = reader.read_int32()
        w = reader.read_int32()
        h = reader.read_int32()
        return cls(round_message=round_message, duration=duration, w=w, h=h)


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
    ID: int = 0xbb718624

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'SendMessageUploadRoundAction':
        return cls()


@register_tl
class DecryptedMessage(TLObject):
    ID: int = 0x91cc4674

    def __init__(self, no_webpage: bool = False, silent: bool = False, media: Any = None, entities: Any = None, via_bot_name: Any = None, reply_to_random_id: Any = None, grouped_id: Any = None, random_id: Any = None, ttl: Any = None, message: Any = None) -> None:
        self.no_webpage = no_webpage
        self.silent = silent
        self.media = media
        self.entities = entities
        self.via_bot_name = via_bot_name
        self.reply_to_random_id = reply_to_random_id
        self.grouped_id = grouped_id
        self.random_id = random_id
        self.ttl = ttl
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.no_webpage:
            flags |= (1 << 1)
        if self.silent:
            flags |= (1 << 5)
        if self.media is not None:
            flags |= (1 << 9)
        if self.entities is not None:
            flags |= (1 << 7)
        if self.via_bot_name is not None:
            flags |= (1 << 11)
        if self.reply_to_random_id is not None:
            flags |= (1 << 3)
        if self.grouped_id is not None:
            flags |= (1 << 17)
        writer.write_uint32(flags)
        writer.write_int64(self.random_id or 0)
        writer.write_int32(self.ttl or 0)
        writer.write_string(self.message or '')
        if self.media is not None:
            if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.entities is not None:
            writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.via_bot_name is not None:
            writer.write_string(self.via_bot_name or '')
        if self.reply_to_random_id is not None:
            writer.write_int64(self.reply_to_random_id or 0)
        if self.grouped_id is not None:
            writer.write_int64(self.grouped_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessage':
        flags = reader.read_uint32()
        no_webpage = bool(flags & (1 << 1))
        silent = bool(flags & (1 << 5))
        random_id = reader.read_int64()
        ttl = reader.read_int32()
        message = reader.read_string()
        media = reader.read_object() if (flags & (1 << 9)) else None
        entities = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 7)) else None
        via_bot_name = reader.read_string() if (flags & (1 << 11)) else None
        reply_to_random_id = reader.read_int64() if (flags & (1 << 3)) else None
        grouped_id = reader.read_int64() if (flags & (1 << 17)) else None
        return cls(no_webpage=no_webpage, silent=silent, random_id=random_id, ttl=ttl, message=message, media=media, entities=entities, via_bot_name=via_bot_name, reply_to_random_id=reply_to_random_id, grouped_id=grouped_id)


@register_tl
class MessageEntityUnderline(TLObject):
    ID: int = 0x9c4e7e8b

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityUnderline':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityStrike(TLObject):
    ID: int = 0xbf0693d4

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityStrike':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityBlockquote(TLObject):
    ID: int = 0x20df5d0

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityBlockquote':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class DecryptedMessageMediaDocument(TLObject):
    ID: int = 0x6abd9782

    def __init__(self, thumb: Any = None, thumb_w: Any = None, thumb_h: Any = None, mime_type: Any = None, size: Any = None, key: Any = None, iv: Any = None, attributes: Any = None, caption: Any = None) -> None:
        self.thumb = thumb
        self.thumb_w = thumb_w
        self.thumb_h = thumb_h
        self.mime_type = mime_type
        self.size = size
        self.key = key
        self.iv = iv
        self.attributes = attributes
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.thumb or b'')
        writer.write_int32(self.thumb_w or 0)
        writer.write_int32(self.thumb_h or 0)
        writer.write_string(self.mime_type or '')
        writer.write_int64(self.size or 0)
        writer.write_bytes(self.key or b'')
        writer.write_bytes(self.iv or b'')
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_string(self.caption or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DecryptedMessageMediaDocument':
        thumb = reader.read_bytes()
        thumb_w = reader.read_int32()
        thumb_h = reader.read_int32()
        mime_type = reader.read_string()
        size = reader.read_int64()
        key = reader.read_bytes()
        iv = reader.read_bytes()
        attributes = reader.read_vector(lambda r: reader.read_object())
        caption = reader.read_string()
        return cls(thumb=thumb, thumb_w=thumb_w, thumb_h=thumb_h, mime_type=mime_type, size=size, key=key, iv=iv, attributes=attributes, caption=caption)


@register_tl
class MessageEntitySpoiler(TLObject):
    ID: int = 0x32ca960f

    def __init__(self, offset: Any = None, length: Any = None) -> None:
        self.offset = offset
        self.length = length

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntitySpoiler':
        offset = reader.read_int32()
        length = reader.read_int32()
        return cls(offset=offset, length=length)


@register_tl
class MessageEntityCustomEmoji(TLObject):
    ID: int = 0xc8cf05f8

    def __init__(self, offset: Any = None, length: Any = None, document_id: Any = None) -> None:
        self.offset = offset
        self.length = length
        self.document_id = document_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.length or 0)
        writer.write_int64(self.document_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessageEntityCustomEmoji':
        offset = reader.read_int32()
        length = reader.read_int32()
        document_id = reader.read_int64()
        return cls(offset=offset, length=length, document_id=document_id)


@register_tl
class JsonObjectValue(TLObject):
    ID: int = 0xc0de1bd9

    def __init__(self, key: Any = None, value: Any = None) -> None:
        self.key = key
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.key or '')
        if self.value is not None and hasattr(self.value, 'write'): self.value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonObjectValue':
        key = reader.read_string()
        value = reader.read_object()
        return cls(key=key, value=value)


@register_tl
class JsonNull(TLObject):
    ID: int = 0x3f6d7b68

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonNull':
        return cls()


@register_tl
class JsonBool(TLObject):
    ID: int = 0xc7345e6a

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.value))

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonBool':
        value = reader.read_bool()
        return cls(value=value)


@register_tl
class JsonNumber(TLObject):
    ID: int = 0x2be0dfa4

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_double(self.value or 0.0)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonNumber':
        value = reader.read_double()
        return cls(value=value)


@register_tl
class JsonString(TLObject):
    ID: int = 0xb71e767a

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.value or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonString':
        value = reader.read_string()
        return cls(value=value)


@register_tl
class JsonArray(TLObject):
    ID: int = 0xf7444763

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.value or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonArray':
        value = reader.read_vector(lambda r: reader.read_object())
        return cls(value=value)


@register_tl
class JsonObject(TLObject):
    ID: int = 0x99c1d49d

    def __init__(self, value: Any = None) -> None:
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.value or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'JsonObject':
        value = reader.read_vector(lambda r: reader.read_object())
        return cls(value=value)


@register_tl
class TextWithEntities(TLObject):
    ID: int = 0x751f3146

    def __init__(self, text: Any = None, entities: Any = None) -> None:
        self.text = text
        self.entities = entities

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text or '')
        writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextWithEntities':
        text = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object())
        return cls(text=text, entities=entities)


@register_tl
class GroupCallMessage(TLObject):
    ID: int = 0x907ce88e

    def __init__(self, random_id: Any = None, message: Any = None) -> None:
        self.random_id = random_id
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.random_id or 0)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'GroupCallMessage':
        random_id = reader.read_int64()
        message = reader.read_object()
        return cls(random_id=random_id, message=message)

