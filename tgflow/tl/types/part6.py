from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl

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

@register_tl
class InputPhoneCall(TLObject):
    ID: int = 0x1E36FDDA
    def __init__(self, id: int = 0, access_hash: int = 0) -> None:
        self.id = id
        self.access_hash = access_hash
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
    @classmethod
    def read(cls, reader: TLReader) -> "InputPhoneCall":
        return cls(id=reader.read_int64(), access_hash=reader.read_int64())

@register_tl
class PhoneCallEmpty(TLObject):
    ID: int = 0x5366C915
    def __init__(self, id: int = 0) -> None:
        self.id = id
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallEmpty":
        return cls(id=reader.read_int64())

@register_tl
class PhoneCallWaiting(TLObject):
    ID: int = 0xC5226F1A
    def __init__(
        self,
        id: int = 0,
        access_hash: int = 0,
        date: int = 0,
        admin_id: int = 0,
        participant_id: int = 0,
        protocol: Any = None,
        video: bool = False,
        receive_date: int | None = None,
    ) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.protocol = protocol
        self.video = video
        self.receive_date = receive_date
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 0)
        if self.receive_date is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
        writer.write_int32(self.date)
        writer.write_int64(self.admin_id)
        writer.write_int64(self.participant_id)
        writer.write_object(self.protocol)
        if self.receive_date is not None:
            writer.write_int32(self.receive_date)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallWaiting":
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        call_id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        protocol = reader.read_object()
        receive_date = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(
            id=call_id,
            access_hash=access_hash,
            date=date,
            admin_id=admin_id,
            participant_id=participant_id,
            protocol=protocol,
            video=video,
            receive_date=receive_date,
        )

@register_tl
class PhoneCallRequested(TLObject):
    ID: int = 0x14B0ED58
    def __init__(
        self,
        id: int = 0,
        access_hash: int = 0,
        date: int = 0,
        admin_id: int = 0,
        participant_id: int = 0,
        g_a_hash: bytes = b"",
        protocol: Any = None,
        video: bool = False,
    ) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_a_hash = g_a_hash
        self.protocol = protocol
        self.video = video
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 1 if self.video else 0
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
        writer.write_int32(self.date)
        writer.write_int64(self.admin_id)
        writer.write_int64(self.participant_id)
        writer.write_bytes(self.g_a_hash)
        writer.write_object(self.protocol)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallRequested":
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        call_id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_a_hash = reader.read_bytes()
        protocol = reader.read_object()
        return cls(
            id=call_id,
            access_hash=access_hash,
            date=date,
            admin_id=admin_id,
            participant_id=participant_id,
            g_a_hash=g_a_hash,
            protocol=protocol,
            video=video,
        )

@register_tl
class PhoneCallAccepted(TLObject):
    ID: int = 0x99D30B42
    def __init__(
        self,
        id: int = 0,
        access_hash: int = 0,
        date: int = 0,
        admin_id: int = 0,
        participant_id: int = 0,
        g_b: bytes = b"",
        protocol: Any = None,
        video: bool = False,
    ) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_b = g_b
        self.protocol = protocol
        self.video = video
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 1 if self.video else 0
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
        writer.write_int32(self.date)
        writer.write_int64(self.admin_id)
        writer.write_int64(self.participant_id)
        writer.write_bytes(self.g_b)
        writer.write_object(self.protocol)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallAccepted":
        flags = reader.read_uint32()
        video = bool(flags & (1 << 0))
        call_id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_b = reader.read_bytes()
        protocol = reader.read_object()
        return cls(
            id=call_id,
            access_hash=access_hash,
            date=date,
            admin_id=admin_id,
            participant_id=participant_id,
            g_b=g_b,
            protocol=protocol,
            video=video,
        )

@register_tl
class PhoneCall(TLObject):
    ID: int = 0x967F7C4C
    def __init__(
        self,
        id: int = 0,
        access_hash: int = 0,
        date: int = 0,
        admin_id: int = 0,
        participant_id: int = 0,
        g_a_or_b: bytes = b"",
        key_fingerprint: int = 0,
        protocol: Any = None,
        connections: list[Any] | None = None,
        start_date: int = 0,
        p2p_allowed: bool = True,
        video: bool = False,
        custom_parameters: Any = None,
    ) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_a_or_b = g_a_or_b
        self.key_fingerprint = key_fingerprint
        self.protocol = protocol
        self.connections = connections or []
        self.start_date = start_date
        self.p2p_allowed = p2p_allowed
        self.video = video
        self.custom_parameters = custom_parameters
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.p2p_allowed:
            flags |= (1 << 0)
        if self.video:
            flags |= (1 << 5)
        if self.custom_parameters is not None:
            flags |= (1 << 7)
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        writer.write_int64(self.access_hash)
        writer.write_int32(self.date)
        writer.write_int64(self.admin_id)
        writer.write_int64(self.participant_id)
        writer.write_bytes(self.g_a_or_b)
        writer.write_int64(self.key_fingerprint)
        writer.write_object(self.protocol)
        writer.write_vector(self.connections, lambda w, x: w.write_object(x))
        writer.write_int32(self.start_date)
        if self.custom_parameters is not None:
            writer.write_object(self.custom_parameters)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCall":
        flags = reader.read_uint32()
        p2p_allowed = bool(flags & (1 << 0))
        video = bool(flags & (1 << 5))
        call_id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_a_or_b = reader.read_bytes()
        key_fingerprint = reader.read_int64()
        protocol = reader.read_object()
        connections = reader.read_vector(lambda r: r.read_object())
        start_date = reader.read_int32()
        custom_parameters = reader.read_object() if (flags & (1 << 7)) else None
        return cls(
            id=call_id,
            access_hash=access_hash,
            date=date,
            admin_id=admin_id,
            participant_id=participant_id,
            g_a_or_b=g_a_or_b,
            key_fingerprint=key_fingerprint,
            protocol=protocol,
            connections=connections,
            start_date=start_date,
            p2p_allowed=p2p_allowed,
            video=video,
            custom_parameters=custom_parameters,
        )

@register_tl
class PhoneCallDiscarded(TLObject):
    ID: int = 0x50CA4DE1
    def __init__(
        self,
        id: int = 0,
        need_rating: bool = False,
        need_debug: bool = False,
        video: bool = False,
        reason: Any = None,
        duration: int | None = None,
    ) -> None:
        self.id = id
        self.need_rating = need_rating
        self.need_debug = need_debug
        self.video = video
        self.reason = reason
        self.duration = duration
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.need_rating:
            flags |= (1 << 2)
        if self.need_debug:
            flags |= (1 << 3)
        if self.video:
            flags |= (1 << 6)
        if self.reason is not None:
            flags |= (1 << 0)
        if self.duration is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        if self.reason is not None:
            writer.write_object(self.reason)
        if self.duration is not None:
            writer.write_int32(self.duration)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallDiscarded":
        flags = reader.read_uint32()
        need_rating = bool(flags & (1 << 2))
        need_debug = bool(flags & (1 << 3))
        video = bool(flags & (1 << 6))
        call_id = reader.read_int64()
        reason = reader.read_object() if (flags & (1 << 0)) else None
        duration = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(id=call_id, need_rating=need_rating, need_debug=need_debug, video=video, reason=reason, duration=duration)

@register_tl
class PhoneCallProtocol(TLObject):
    ID: int = 0xFC88194B
    def __init__(
        self,
        min_layer: int = 65,
        max_layer: int = 225,
        udp_p2p: bool = True,
        udp_reflector: bool = True,
        library_versions: list[str] | None = None,
    ) -> None:
        self.min_layer = min_layer
        self.max_layer = max_layer
        self.udp_p2p = udp_p2p
        self.udp_reflector = udp_reflector
        self.library_versions = library_versions or ["10.0.0"]
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.udp_p2p:
            flags |= (1 << 0)
        if self.udp_reflector:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.min_layer)
        writer.write_int32(self.max_layer)
        writer.write_vector(self.library_versions, lambda w, x: w.write_string(x))
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallProtocol":
        flags = reader.read_uint32()
        udp_p2p = bool(flags & (1 << 0))
        udp_reflector = bool(flags & (1 << 1))
        min_layer = reader.read_int32()
        max_layer = reader.read_int32()
        library_versions = reader.read_vector(lambda r: r.read_string())
        return cls(min_layer=min_layer, max_layer=max_layer, udp_p2p=udp_p2p, udp_reflector=udp_reflector, library_versions=library_versions)

@register_tl
class PhoneConnection(TLObject):
    ID: int = 0x9D460E4B
    def __init__(
        self,
        id: int = 0,
        ip: str = "",
        ipv6: str = "",
        port: int = 0,
        peer_tag: bytes = b"",
        tcp: bool = False,
    ) -> None:
        self.id = id
        self.ip = ip
        self.ipv6 = ipv6
        self.port = port
        self.peer_tag = peer_tag
        self.tcp = tcp
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 1 if self.tcp else 0
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        writer.write_string(self.ip)
        writer.write_string(self.ipv6)
        writer.write_int32(self.port)
        writer.write_bytes(self.peer_tag)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneConnection":
        flags = reader.read_uint32()
        tcp = bool(flags & (1 << 0))
        conn_id = reader.read_int64()
        ip = reader.read_string()
        ipv6 = reader.read_string()
        port = reader.read_int32()
        peer_tag = reader.read_bytes()
        return cls(id=conn_id, ip=ip, ipv6=ipv6, port=port, peer_tag=peer_tag, tcp=tcp)

@register_tl
class PhoneConnectionWebrtc(TLObject):
    ID: int = 0x635FEAF1
    def __init__(
        self,
        id: int = 0,
        ip: str = "",
        ipv6: str = "",
        port: int = 0,
        username: str = "",
        password: str = "",
        turn: bool = True,
        stun: bool = False,
    ) -> None:
        self.id = id
        self.ip = ip
        self.ipv6 = ipv6
        self.port = port
        self.username = username
        self.password = password
        self.turn = turn
        self.stun = stun
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.turn:
            flags |= (1 << 0)
        if self.stun:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id)
        writer.write_string(self.ip)
        writer.write_string(self.ipv6)
        writer.write_int32(self.port)
        writer.write_string(self.username)
        writer.write_string(self.password)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneConnectionWebrtc":
        flags = reader.read_uint32()
        turn = bool(flags & (1 << 0))
        stun = bool(flags & (1 << 1))
        conn_id = reader.read_int64()
        ip = reader.read_string()
        ipv6 = reader.read_string()
        port = reader.read_int32()
        username = reader.read_string()
        password = reader.read_string()
        return cls(id=conn_id, ip=ip, ipv6=ipv6, port=port, username=username, password=password, turn=turn, stun=stun)

@register_tl
class PhoneCallDiscardReasonMissed(TLObject):
    ID: int = 0x85E42301
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallDiscardReasonMissed":
        return cls()

@register_tl
class PhoneCallDiscardReasonDisconnect(TLObject):
    ID: int = 0xE095C1A0
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallDiscardReasonDisconnect":
        return cls()

@register_tl
class PhoneCallDiscardReasonHangup(TLObject):
    ID: int = 0x57ADC690
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallDiscardReasonHangup":
        return cls()

@register_tl
class PhoneCallDiscardReasonBusy(TLObject):
    ID: int = 0xFAF7E8C9
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
    @classmethod
    def read(cls, reader: TLReader) -> "PhoneCallDiscardReasonBusy":
        return cls()

@register_tl
class PhonePhoneCall(TLObject):
    ID: int = 0xEC82E140
    def __init__(self, phone_call: Any = None, users: list[Any] | None = None) -> None:
        self.phone_call = phone_call
        self.users = users or []
    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.phone_call)
        writer.write_vector(self.users, lambda w, x: w.write_object(x))
    @classmethod
    def read(cls, reader: TLReader) -> "PhonePhoneCall":
        phone_call = reader.read_object()
        users = reader.read_vector(lambda r: r.read_object())
        return cls(phone_call=phone_call, users=users)

@register_tl
class InputChannel(TLObject):
    ID: int = 0xF35AEC28

    def __init__(self, channel_id: int = 0, access_hash: int = 0) -> None:
        self.channel_id = channel_id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.channel_id)
        writer.write_int64(self.access_hash)

    @classmethod
    def read(cls, reader: TLReader) -> "InputChannel":
        return cls(channel_id=reader.read_int64(), access_hash=reader.read_int64())

@register_tl
class InputChannelEmpty(TLObject):
    ID: int = 0xEE8C1E86

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> "InputChannelEmpty":
        return cls()

@register_tl
class CodeSettings(TLObject):
    ID: int = 0xAD253D78

    def __init__(
        self,
        allow_flashcall: bool = False,
        current_number: bool = False,
        allow_app_hash: bool = False,
        allow_missed_call: bool = False,
        allow_firebase: bool = False,
        unknown_number: bool = False,
    ) -> None:
        self.allow_flashcall = allow_flashcall
        self.current_number = current_number
        self.allow_app_hash = allow_app_hash
        self.allow_missed_call = allow_missed_call
        self.allow_firebase = allow_firebase
        self.unknown_number = unknown_number

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.allow_flashcall:
            flags |= (1 << 0)
        if self.current_number:
            flags |= (1 << 1)
        if self.allow_app_hash:
            flags |= (1 << 4)
        if self.allow_missed_call:
            flags |= (1 << 5)
        if self.allow_firebase:
            flags |= (1 << 7)
        if self.unknown_number:
            flags |= (1 << 9)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> "CodeSettings":
        flags = reader.read_uint32()
        return cls(
            allow_flashcall=bool(flags & (1 << 0)),
            current_number=bool(flags & (1 << 1)),
            allow_app_hash=bool(flags & (1 << 4)),
            allow_missed_call=bool(flags & (1 << 5)),
            allow_firebase=bool(flags & (1 << 7)),
            unknown_number=bool(flags & (1 << 9)),
        )

@register_tl
class ContactsResolvedPeer(TLObject):
    ID: int = 0x7F077AD9

    def __init__(self, peer: Any = None, chats: list[Any] | None = None, users: list[Any] | None = None) -> None:
        self.peer = peer
        self.chats = chats or []
        self.users = users or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_object(self.peer)
        writer.write_vector(self.chats, lambda w, c: w.write_object(c))
        writer.write_vector(self.users, lambda w, u: w.write_object(u))

    @classmethod
    def read(cls, reader: TLReader) -> "ContactsResolvedPeer":
        peer = reader.read_object()
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(peer=peer, chats=chats, users=users)

@register_tl
class MessagesAffectedMessages(TLObject):
    ID: int = 0x84D0CAA0

    def __init__(self, pts: int = 0, pts_count: int = 0) -> None:
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pts)
        writer.write_int32(self.pts_count)

    @classmethod
    def read(cls, reader: TLReader) -> "MessagesAffectedMessages":
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(pts=pts, pts_count=pts_count)

@register_tl
class AuthLoggedOut(TLObject):
    ID: int = 0xC3A2835F

    def __init__(self, future_auth_token: bytes | None = None) -> None:
        self.future_auth_token = future_auth_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.future_auth_token is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.future_auth_token is not None:
            writer.write_bytes(self.future_auth_token)

    @classmethod
    def read(cls, reader: TLReader) -> "AuthLoggedOut":
        flags = reader.read_uint32()
        future_auth_token = reader.read_bytes() if (flags & (1 << 0)) else None
        return cls(future_auth_token=future_auth_token)

@register_tl
class InputCheckPasswordEmpty(TLObject):
    ID: int = 0x9880F658

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> "InputCheckPasswordEmpty":
        return cls()

@register_tl
class InputCheckPasswordSRP(TLObject):
    ID: int = 0xD27FF082

    def __init__(self, srp_id: int = 0, A: bytes = b"", M1: bytes = b"") -> None:
        self.srp_id = srp_id
        self.A = A
        self.M1 = M1

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.srp_id)
        writer.write_bytes(self.A)
        writer.write_bytes(self.M1)

    @classmethod
    def read(cls, reader: TLReader) -> "InputCheckPasswordSRP":
        return cls(srp_id=reader.read_int64(), A=reader.read_bytes(), M1=reader.read_bytes())


@register_tl
class ChatAdminRights(TLObject):
    ID: int = 0x5FB224D5

    def __init__(
        self,
        change_info: bool = False,
        post_messages: bool = False,
        edit_messages: bool = False,
        delete_messages: bool = False,
        ban_users: bool = False,
        invite_users: bool = False,
        pin_messages: bool = False,
        add_admins: bool = False,
        anonymous: bool = False,
        manage_call: bool = False,
        other: bool = False,
        manage_topics: bool = False,
        post_stories: bool = False,
        edit_stories: bool = False,
        delete_stories: bool = False,
    ) -> None:
        self.change_info = change_info
        self.post_messages = post_messages
        self.edit_messages = edit_messages
        self.delete_messages = delete_messages
        self.ban_users = ban_users
        self.invite_users = invite_users
        self.pin_messages = pin_messages
        self.add_admins = add_admins
        self.anonymous = anonymous
        self.manage_call = manage_call
        self.other = other
        self.manage_topics = manage_topics
        self.post_stories = post_stories
        self.edit_stories = edit_stories
        self.delete_stories = delete_stories

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.change_info:
            flags |= (1 << 0)
        if self.post_messages:
            flags |= (1 << 1)
        if self.edit_messages:
            flags |= (1 << 2)
        if self.delete_messages:
            flags |= (1 << 3)
        if self.ban_users:
            flags |= (1 << 4)
        if self.invite_users:
            flags |= (1 << 5)
        if self.pin_messages:
            flags |= (1 << 7)
        if self.add_admins:
            flags |= (1 << 9)
        if self.anonymous:
            flags |= (1 << 10)
        if self.manage_call:
            flags |= (1 << 11)
        if self.other:
            flags |= (1 << 12)
        if self.manage_topics:
            flags |= (1 << 13)
        if self.post_stories:
            flags |= (1 << 14)
        if self.edit_stories:
            flags |= (1 << 15)
        if self.delete_stories:
            flags |= (1 << 16)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> "ChatAdminRights":
        flags = reader.read_uint32()
        return cls(
            change_info=bool(flags & (1 << 0)),
            post_messages=bool(flags & (1 << 1)),
            edit_messages=bool(flags & (1 << 2)),
            delete_messages=bool(flags & (1 << 3)),
            ban_users=bool(flags & (1 << 4)),
            invite_users=bool(flags & (1 << 5)),
            pin_messages=bool(flags & (1 << 7)),
            add_admins=bool(flags & (1 << 9)),
            anonymous=bool(flags & (1 << 10)),
            manage_call=bool(flags & (1 << 11)),
            other=bool(flags & (1 << 12)),
            manage_topics=bool(flags & (1 << 13)),
            post_stories=bool(flags & (1 << 14)),
            edit_stories=bool(flags & (1 << 15)),
            delete_stories=bool(flags & (1 << 16)),
        )


@register_tl
class ChatBannedRights(TLObject):
    ID: int = 0x9F120418

    def __init__(
        self,
        view_messages: bool = False,
        send_messages: bool = False,
        send_media: bool = False,
        send_stickers: bool = False,
        send_gifs: bool = False,
        send_games: bool = False,
        send_inline: bool = False,
        embed_links: bool = False,
        send_polls: bool = False,
        change_info: bool = False,
        invite_users: bool = False,
        pin_messages: bool = False,
        manage_topics: bool = False,
        send_photos: bool = False,
        send_videos: bool = False,
        send_roundvideos: bool = False,
        send_audios: bool = False,
        send_voices: bool = False,
        send_docs: bool = False,
        send_plain: bool = False,
        until_date: int = 0,
    ) -> None:
        self.view_messages = view_messages
        self.send_messages = send_messages
        self.send_media = send_media
        self.send_stickers = send_stickers
        self.send_gifs = send_gifs
        self.send_games = send_games
        self.send_inline = send_inline
        self.embed_links = embed_links
        self.send_polls = send_polls
        self.change_info = change_info
        self.invite_users = invite_users
        self.pin_messages = pin_messages
        self.manage_topics = manage_topics
        self.send_photos = send_photos
        self.send_videos = send_videos
        self.send_roundvideos = send_roundvideos
        self.send_audios = send_audios
        self.send_voices = send_voices
        self.send_docs = send_docs
        self.send_plain = send_plain
        self.until_date = until_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.view_messages:
            flags |= (1 << 0)
        if self.send_messages:
            flags |= (1 << 1)
        if self.send_media:
            flags |= (1 << 2)
        if self.send_stickers:
            flags |= (1 << 3)
        if self.send_gifs:
            flags |= (1 << 4)
        if self.send_games:
            flags |= (1 << 5)
        if self.send_inline:
            flags |= (1 << 6)
        if self.embed_links:
            flags |= (1 << 7)
        if self.send_polls:
            flags |= (1 << 8)
        if self.change_info:
            flags |= (1 << 10)
        if self.invite_users:
            flags |= (1 << 15)
        if self.pin_messages:
            flags |= (1 << 17)
        if self.manage_topics:
            flags |= (1 << 18)
        if self.send_photos:
            flags |= (1 << 19)
        if self.send_videos:
            flags |= (1 << 20)
        if self.send_roundvideos:
            flags |= (1 << 21)
        if self.send_audios:
            flags |= (1 << 22)
        if self.send_voices:
            flags |= (1 << 23)
        if self.send_docs:
            flags |= (1 << 24)
        if self.send_plain:
            flags |= (1 << 25)
        writer.write_uint32(flags)
        writer.write_int32(self.until_date)

    @classmethod
    def read(cls, reader: TLReader) -> "ChatBannedRights":
        flags = reader.read_uint32()
        until_date = reader.read_int32()
        return cls(
            view_messages=bool(flags & (1 << 0)),
            send_messages=bool(flags & (1 << 1)),
            send_media=bool(flags & (1 << 2)),
            send_stickers=bool(flags & (1 << 3)),
            send_gifs=bool(flags & (1 << 4)),
            send_games=bool(flags & (1 << 5)),
            send_inline=bool(flags & (1 << 6)),
            embed_links=bool(flags & (1 << 7)),
            send_polls=bool(flags & (1 << 8)),
            change_info=bool(flags & (1 << 10)),
            invite_users=bool(flags & (1 << 15)),
            pin_messages=bool(flags & (1 << 17)),
            manage_topics=bool(flags & (1 << 18)),
            send_photos=bool(flags & (1 << 19)),
            send_videos=bool(flags & (1 << 20)),
            send_roundvideos=bool(flags & (1 << 21)),
            send_audios=bool(flags & (1 << 22)),
            send_voices=bool(flags & (1 << 23)),
            send_docs=bool(flags & (1 << 24)),
            send_plain=bool(flags & (1 << 25)),
            until_date=until_date,
        )


@register_tl
class ChannelParticipantsRecent(TLObject):
    ID: int = 0xDE3F3C79

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantsRecent":
        return cls()


@register_tl
class ChannelParticipantsAdmins(TLObject):
    ID: int = 0xB4608969

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantsAdmins":
        return cls()


@register_tl
class ChannelParticipantsKicked(TLObject):
    ID: int = 0x3C37BB74

    def __init__(self, q: str = "") -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantsKicked":
        return cls(q=reader.read_string())


@register_tl
class ChannelParticipantsBanned(TLObject):
    ID: int = 0x1427A5E1

    def __init__(self, q: str = "") -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantsBanned":
        return cls(q=reader.read_string())


@register_tl
class ChannelParticipantsBots(TLObject):
    ID: int = 0xB0D1861B

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantsBots":
        return cls()


@register_tl
class ChannelParticipantsSearch(TLObject):
    ID: int = 0x0656AC4B

    def __init__(self, q: str = "") -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantsSearch":
        return cls(q=reader.read_string())


@register_tl
class ChannelParticipantsContacts(TLObject):
    ID: int = 0xBB6AE88D

    def __init__(self, q: str = "") -> None:
        self.q = q

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.q)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantsContacts":
        return cls(q=reader.read_string())


@register_tl
class ChannelsChannelParticipants(TLObject):
    ID: int = 0x9AB0FE02

    def __init__(
        self,
        count: int = 0,
        participants: list[Any] | None = None,
        chats: list[Any] | None = None,
        users: list[Any] | None = None,
    ) -> None:
        self.count = count
        self.participants = participants or []
        self.chats = chats or []
        self.users = users or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.count)
        writer.write_vector(self.participants, lambda w, p: w.write_object(p))
        writer.write_vector(self.chats, lambda w, c: w.write_object(c))
        writer.write_vector(self.users, lambda w, u: w.write_object(u))

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelsChannelParticipants":
        count = reader.read_int32()
        participants = reader.read_vector(lambda r: r.read_object())
        chats = reader.read_vector(lambda r: r.read_object())
        users = reader.read_vector(lambda r: r.read_object())
        return cls(count=count, participants=participants, chats=chats, users=users)


@register_tl
class ChannelParticipant(TLObject):
    ID: int = 0xCB44AC3B

    def __init__(self, user_id: int = 0, date: int = 0) -> None:
        self.user_id = user_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.user_id)
        writer.write_int32(self.date)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipant":
        return cls(user_id=reader.read_int64(), date=reader.read_int32())


@register_tl
class ChannelParticipantCreator(TLObject):
    ID: int = 0x2FE601D3

    def __init__(self, user_id: int = 0, admin_rights: Any = None, rank: str | None = None) -> None:
        self.user_id = user_id
        self.admin_rights = admin_rights
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id)
        writer.write_object(self.admin_rights)
        if self.rank is not None:
            writer.write_string(self.rank)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantCreator":
        flags = reader.read_uint32()
        user_id = reader.read_int64()
        admin_rights = reader.read_object()
        rank = reader.read_string() if (flags & (1 << 0)) else None
        return cls(user_id=user_id, admin_rights=admin_rights, rank=rank)


@register_tl
class ChannelParticipantAdmin(TLObject):
    ID: int = 0x34C48969

    def __init__(
        self,
        user_id: int = 0,
        promoted_by: int = 0,
        date: int = 0,
        admin_rights: Any = None,
        can_edit: bool = False,
        rank: str | None = None,
    ) -> None:
        self.user_id = user_id
        self.promoted_by = promoted_by
        self.date = date
        self.admin_rights = admin_rights
        self.can_edit = can_edit
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_edit:
            flags |= (1 << 0)
        if self.rank is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int64(self.user_id)
        writer.write_int64(self.promoted_by)
        writer.write_int32(self.date)
        writer.write_object(self.admin_rights)
        if self.rank is not None:
            writer.write_string(self.rank)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantAdmin":
        flags = reader.read_uint32()
        can_edit = bool(flags & (1 << 0))
        user_id = reader.read_int64()
        promoted_by = reader.read_int64()
        date = reader.read_int32()
        admin_rights = reader.read_object()
        rank = reader.read_string() if (flags & (1 << 2)) else None
        return cls(
            user_id=user_id,
            promoted_by=promoted_by,
            date=date,
            admin_rights=admin_rights,
            can_edit=can_edit,
            rank=rank,
        )


@register_tl
class ChannelParticipantBanned(TLObject):
    ID: int = 0x6DF8014E

    def __init__(
        self,
        peer: Any = None,
        date: int = 0,
        kicked_by: int = 0,
        banned_rights: Any = None,
        left: bool = False,
    ) -> None:
        self.peer = peer
        self.date = date
        self.kicked_by = kicked_by
        self.banned_rights = banned_rights
        self.left = left

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.left:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_object(self.peer)
        writer.write_int32(self.date)
        writer.write_int64(self.kicked_by)
        writer.write_object(self.banned_rights)

    @classmethod
    def read(cls, reader: TLReader) -> "ChannelParticipantBanned":
        flags = reader.read_uint32()
        left = bool(flags & (1 << 0))
        peer = reader.read_object()
        date = reader.read_int32()
        kicked_by = reader.read_int64()
        banned_rights = reader.read_object()
        return cls(peer=peer, date=date, kicked_by=kicked_by, banned_rights=banned_rights, left=left)


@register_tl
class KeyboardButton(TLObject):
    ID: int = 0xA2F9C463

    def __init__(self, text: str = "") -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButton":
        return cls(text=reader.read_string())


@register_tl
class KeyboardButtonUrl(TLObject):
    ID: int = 0x258AFF05

    def __init__(self, text: str = "", url: str = "") -> None:
        self.text = text
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text)
        writer.write_string(self.url)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonUrl":
        return cls(text=reader.read_string(), url=reader.read_string())


@register_tl
class KeyboardButtonCallback(TLObject):
    ID: int = 0x35BBDB6B

    def __init__(self, text: str = "", data: bytes = b"", requires_password: bool = False) -> None:
        self.text = text
        self.data = data
        self.requires_password = requires_password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.requires_password:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.text)
        writer.write_bytes(self.data)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonCallback":
        flags = reader.read_uint32()
        requires_password = bool(flags & (1 << 0))
        text = reader.read_string()
        data = reader.read_bytes()
        return cls(text=text, data=data, requires_password=requires_password)


@register_tl
class KeyboardButtonCopyText(TLObject):
    ID: int = 0xB510E197

    def __init__(self, text: str = "", copy_text: str = "") -> None:
        self.text = text
        self.copy_text = copy_text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text)
        writer.write_string(self.copy_text)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonCopyText":
        return cls(text=reader.read_string(), copy_text=reader.read_string())


@register_tl
class KeyboardButtonUserProfile(TLObject):
    ID: int = 0x308660C1

    def __init__(self, text: str = "", user_id: int = 0) -> None:
        self.text = text
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text)
        writer.write_int64(self.user_id)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonUserProfile":
        return cls(text=reader.read_string(), user_id=reader.read_int64())


@register_tl
class KeyboardButtonWebView(TLObject):
    ID: int = 0x10B78D29

    def __init__(self, text: str = "", url: str = "") -> None:
        self.text = text
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text)
        writer.write_string(self.url)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonWebView":
        return cls(text=reader.read_string(), url=reader.read_string())


@register_tl
class KeyboardButtonSwitchInline(TLObject):
    ID: int = 0x568A74E0

    def __init__(self, text: str = "", query: str = "", same_peer: bool = False) -> None:
        self.text = text
        self.query = query
        self.same_peer = same_peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.same_peer:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.text)
        writer.write_string(self.query)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonSwitchInline":
        flags = reader.read_uint32()
        same_peer = bool(flags & (1 << 0))
        text = reader.read_string()
        query = reader.read_string()
        return cls(text=text, query=query, same_peer=same_peer)


@register_tl
class KeyboardButtonBuy(TLObject):
    ID: int = 0xAFD93FBB

    def __init__(self, text: str = "") -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.text)

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonBuy":
        return cls(text=reader.read_string())


@register_tl
class KeyboardButtonRow(TLObject):
    ID: int = 0x776288D4

    def __init__(self, buttons: list[Any] | None = None) -> None:
        self.buttons = buttons or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.buttons, lambda w, b: w.write_object(b))

    @classmethod
    def read(cls, reader: TLReader) -> "KeyboardButtonRow":
        return cls(buttons=reader.read_vector(lambda r: r.read_object()))


@register_tl
class ReplyInlineMarkup(TLObject):
    ID: int = 0x48A30254

    def __init__(self, rows: list[Any] | None = None) -> None:
        self.rows = rows or []

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.rows, lambda w, r: w.write_object(r))

    @classmethod
    def read(cls, reader: TLReader) -> "ReplyInlineMarkup":
        return cls(rows=reader.read_vector(lambda r: r.read_object()))


@register_tl
class ReplyKeyboardMarkup(TLObject):
    ID: int = 0x85DD99D1

    def __init__(
        self,
        rows: list[Any] | None = None,
        resize: bool = False,
        single_use: bool = False,
        selective: bool = False,
        persistent: bool = False,
        placeholder: str | None = None,
    ) -> None:
        self.rows = rows or []
        self.resize = resize
        self.single_use = single_use
        self.selective = selective
        self.persistent = persistent
        self.placeholder = placeholder

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.resize:
            flags |= (1 << 0)
        if self.single_use:
            flags |= (1 << 1)
        if self.selective:
            flags |= (1 << 2)
        if self.placeholder is not None:
            flags |= (1 << 3)
        if self.persistent:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_vector(self.rows, lambda w, r: w.write_object(r))
        if self.placeholder is not None:
            writer.write_string(self.placeholder)

    @classmethod
    def read(cls, reader: TLReader) -> "ReplyKeyboardMarkup":
        flags = reader.read_uint32()
        resize = bool(flags & (1 << 0))
        single_use = bool(flags & (1 << 1))
        selective = bool(flags & (1 << 2))
        persistent = bool(flags & (1 << 4))
        rows = reader.read_vector(lambda r: r.read_object())
        placeholder = reader.read_string() if (flags & (1 << 3)) else None
        return cls(
            rows=rows,
            resize=resize,
            single_use=single_use,
            selective=selective,
            persistent=persistent,
            placeholder=placeholder,
        )


@register_tl
class ReplyKeyboardHide(TLObject):
    ID: int = 0xA03E5B85

    def __init__(self, selective: bool = False) -> None:
        self.selective = selective

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.selective:
            flags |= (1 << 2)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> "ReplyKeyboardHide":
        flags = reader.read_uint32()
        return cls(selective=bool(flags & (1 << 2)))


@register_tl
class ReplyKeyboardForceReply(TLObject):
    ID: int = 0xF072834B

    def __init__(self, single_use: bool = False, selective: bool = False, placeholder: str | None = None) -> None:
        self.single_use = single_use
        self.selective = selective
        self.placeholder = placeholder

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.single_use:
            flags |= (1 << 1)
        if self.selective:
            flags |= (1 << 2)
        if self.placeholder is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.placeholder is not None:
            writer.write_string(self.placeholder)

    @classmethod
    def read(cls, reader: TLReader) -> "ReplyKeyboardForceReply":
        flags = reader.read_uint32()
        single_use = bool(flags & (1 << 1))
        selective = bool(flags & (1 << 2))
        placeholder = reader.read_string() if (flags & (1 << 3)) else None
        return cls(single_use=single_use, selective=selective, placeholder=placeholder)
