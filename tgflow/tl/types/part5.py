from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

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
        writer.write_string(self.emoticon or '')
        writer.write_int32(self.msg_id or 0)
        if self.interaction is not None and hasattr(self.interaction, 'write'): self.interaction.write(writer)

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
        writer.write_string(self.emoticon or '')

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
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

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
        writer.write_vector(self.my_results or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.results or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ContactsFound':
        my_results = reader.read_vector(lambda r: reader.read_object())
        results = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowUsers':
        users = reader.read_vector(lambda r: reader.read_object())
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
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueDisallowUsers':
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(users=users)


@register_tl
class InputPrivacyValueAllowChatParticipants(TLObject):
    ID: int = 0x840649cf

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueAllowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_int64())
        return cls(chats=chats)


@register_tl
class InputPrivacyValueDisallowChatParticipants(TLObject):
    ID: int = 0xe94f0f86

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPrivacyValueDisallowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_int64())
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
        writer.write_vector(self.users or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowUsers':
        users = reader.read_vector(lambda r: r.read_int64())
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
        writer.write_vector(self.users or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueDisallowUsers':
        users = reader.read_vector(lambda r: r.read_int64())
        return cls(users=users)


@register_tl
class PrivacyValueAllowChatParticipants(TLObject):
    ID: int = 0x6b134e8e

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueAllowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_int64())
        return cls(chats=chats)


@register_tl
class PrivacyValueDisallowChatParticipants(TLObject):
    ID: int = 0x41c87565

    def __init__(self, chats: Any = None) -> None:
        self.chats = chats

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.chats or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PrivacyValueDisallowChatParticipants':
        chats = reader.read_vector(lambda r: r.read_int64())
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
        writer.write_vector(self.rules or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.chats or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPrivacyRules':
        rules = reader.read_vector(lambda r: reader.read_object())
        chats = reader.read_vector(lambda r: reader.read_object())
        users = reader.read_vector(lambda r: reader.read_object())
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

    def __init__(self, mask: bool = False, mask_coords: Any = None, alt: Any = None, stickerset: Any = None) -> None:
        self.mask = mask
        self.mask_coords = mask_coords
        self.alt = alt
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.mask:
            flags |= (1 << 1)
        if self.mask_coords is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_string(self.alt or '')
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)
        if self.mask_coords is not None:
            if self.mask_coords is not None and hasattr(self.mask_coords, 'write'): self.mask_coords.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeSticker':
        flags = reader.read_uint32()
        mask = bool(flags & (1 << 1))
        alt = reader.read_string()
        stickerset = reader.read_object()
        mask_coords = reader.read_object() if (flags & (1 << 0)) else None
        return cls(mask=mask, alt=alt, stickerset=stickerset, mask_coords=mask_coords)


@register_tl
class DocumentAttributeVideo(TLObject):
    ID: int = 0x43c57c48

    def __init__(self, round_message: bool = False, supports_streaming: bool = False, nosound: bool = False, preload_prefix_size: Any = None, video_start_ts: Any = None, video_codec: Any = None, duration: Any = None, w: Any = None, h: Any = None) -> None:
        self.round_message = round_message
        self.supports_streaming = supports_streaming
        self.nosound = nosound
        self.preload_prefix_size = preload_prefix_size
        self.video_start_ts = video_start_ts
        self.video_codec = video_codec
        self.duration = duration
        self.w = w
        self.h = h

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
        writer.write_double(self.duration or 0.0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        if self.preload_prefix_size is not None:
            writer.write_int32(self.preload_prefix_size or 0)
        if self.video_start_ts is not None:
            writer.write_double(self.video_start_ts or 0.0)
        if self.video_codec is not None:
            writer.write_string(self.video_codec or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeVideo':
        flags = reader.read_uint32()
        round_message = bool(flags & (1 << 0))
        supports_streaming = bool(flags & (1 << 1))
        nosound = bool(flags & (1 << 3))
        duration = reader.read_double()
        w = reader.read_int32()
        h = reader.read_int32()
        preload_prefix_size = reader.read_int32() if (flags & (1 << 2)) else None
        video_start_ts = reader.read_double() if (flags & (1 << 4)) else None
        video_codec = reader.read_string() if (flags & (1 << 5)) else None
        return cls(round_message=round_message, supports_streaming=supports_streaming, nosound=nosound, duration=duration, w=w, h=h, preload_prefix_size=preload_prefix_size, video_start_ts=video_start_ts, video_codec=video_codec)


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
class DocumentAttributeCustomEmoji(TLObject):
    ID: int = 0xfd149899

    def __init__(self, free: bool = False, text_color: bool = False, alt: Any = None, stickerset: Any = None) -> None:
        self.free = free
        self.text_color = text_color
        self.alt = alt
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.free:
            flags |= (1 << 0)
        if self.text_color:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.alt or '')
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'DocumentAttributeCustomEmoji':
        flags = reader.read_uint32()
        free = bool(flags & (1 << 0))
        text_color = bool(flags & (1 << 1))
        alt = reader.read_string()
        stickerset = reader.read_object()
        return cls(free=free, text_color=text_color, alt=alt, stickerset=stickerset)


@register_tl
class MessagesStickersNotModified(TLObject):
    ID: int = 0xf1749a22

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStickersNotModified':
        return cls()


@register_tl
class MessagesStickers(TLObject):
    ID: int = 0x30a6ec7e

    def __init__(self, hash: Any = None, stickers: Any = None) -> None:
        self.hash = hash
        self.stickers = stickers

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.stickers or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStickers':
        hash = reader.read_int64()
        stickers = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, stickers=stickers)


@register_tl
class StickerPack(TLObject):
    ID: int = 0x12b299d4

    def __init__(self, emoticon: Any = None, documents: Any = None) -> None:
        self.emoticon = emoticon
        self.documents = documents

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')
        writer.write_vector(self.documents or [], lambda w, x: w.write_int64(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'StickerPack':
        emoticon = reader.read_string()
        documents = reader.read_vector(lambda r: r.read_int64())
        return cls(emoticon=emoticon, documents=documents)


@register_tl
class MessagesAllStickersNotModified(TLObject):
    ID: int = 0xe86602c3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAllStickersNotModified':
        return cls()


@register_tl
class MessagesAllStickers(TLObject):
    ID: int = 0xcdbbcebb

    def __init__(self, hash: Any = None, sets: Any = None) -> None:
        self.hash = hash
        self.sets = sets

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.hash or 0)
        writer.write_vector(self.sets or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAllStickers':
        hash = reader.read_int64()
        sets = reader.read_vector(lambda r: reader.read_object())
        return cls(hash=hash, sets=sets)


@register_tl
class MessagesAffectedMessages(TLObject):
    ID: int = 0x84d19185

    def __init__(self, pts: Any = None, pts_count: Any = None) -> None:
        self.pts = pts
        self.pts_count = pts_count

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.pts_count or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAffectedMessages':
        pts = reader.read_int32()
        pts_count = reader.read_int32()
        return cls(pts=pts, pts_count=pts_count)


@register_tl
class WebPageEmpty(TLObject):
    ID: int = 0x211a1788

    def __init__(self, url: Any = None, id: Any = None) -> None:
        self.url = url
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.url is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.url is not None:
            writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageEmpty':
        flags = reader.read_uint32()
        id = reader.read_int64()
        url = reader.read_string() if (flags & (1 << 0)) else None
        return cls(id=id, url=url)


@register_tl
class WebPagePending(TLObject):
    ID: int = 0xb0d13e47

    def __init__(self, url: Any = None, id: Any = None, date: Any = None) -> None:
        self.url = url
        self.id = id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.url is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        if self.url is not None:
            writer.write_string(self.url or '')
        writer.write_int32(self.date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPagePending':
        flags = reader.read_uint32()
        id = reader.read_int64()
        url = reader.read_string() if (flags & (1 << 0)) else None
        date = reader.read_int32()
        return cls(id=id, url=url, date=date)


@register_tl
class WebPage(TLObject):
    ID: int = 0xe89c45b2

    def __init__(self, has_large_media: bool = False, video_cover_photo: bool = False, type: Any = None, site_name: Any = None, title: Any = None, description: Any = None, photo: Any = None, embed_url: Any = None, embed_type: Any = None, embed_width: Any = None, embed_height: Any = None, duration: Any = None, author: Any = None, document: Any = None, cached_page: Any = None, attributes: Any = None, id: Any = None, url: Any = None, display_url: Any = None, hash: Any = None) -> None:
        self.has_large_media = has_large_media
        self.video_cover_photo = video_cover_photo
        self.type = type
        self.site_name = site_name
        self.title = title
        self.description = description
        self.photo = photo
        self.embed_url = embed_url
        self.embed_type = embed_type
        self.embed_width = embed_width
        self.embed_height = embed_height
        self.duration = duration
        self.author = author
        self.document = document
        self.cached_page = cached_page
        self.attributes = attributes
        self.id = id
        self.url = url
        self.display_url = display_url
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_large_media:
            flags |= (1 << 13)
        if self.video_cover_photo:
            flags |= (1 << 14)
        if self.type is not None:
            flags |= (1 << 0)
        if self.site_name is not None:
            flags |= (1 << 1)
        if self.title is not None:
            flags |= (1 << 2)
        if self.description is not None:
            flags |= (1 << 3)
        if self.photo is not None:
            flags |= (1 << 4)
        if self.embed_url is not None:
            flags |= (1 << 5)
        if self.embed_type is not None:
            flags |= (1 << 5)
        if self.embed_width is not None:
            flags |= (1 << 6)
        if self.embed_height is not None:
            flags |= (1 << 6)
        if self.duration is not None:
            flags |= (1 << 7)
        if self.author is not None:
            flags |= (1 << 8)
        if self.document is not None:
            flags |= (1 << 9)
        if self.cached_page is not None:
            flags |= (1 << 10)
        if self.attributes is not None:
            flags |= (1 << 12)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(self.url or '')
        writer.write_string(self.display_url or '')
        writer.write_int32(self.hash or 0)
        if self.type is not None:
            writer.write_string(self.type or '')
        if self.site_name is not None:
            writer.write_string(self.site_name or '')
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.embed_url is not None:
            writer.write_string(self.embed_url or '')
        if self.embed_type is not None:
            writer.write_string(self.embed_type or '')
        if self.embed_width is not None:
            writer.write_int32(self.embed_width or 0)
        if self.embed_height is not None:
            writer.write_int32(self.embed_height or 0)
        if self.duration is not None:
            writer.write_int32(self.duration or 0)
        if self.author is not None:
            writer.write_string(self.author or '')
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.cached_page is not None:
            if self.cached_page is not None and hasattr(self.cached_page, 'write'): self.cached_page.write(writer)
        if self.attributes is not None:
            writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPage':
        flags = reader.read_uint32()
        has_large_media = bool(flags & (1 << 13))
        video_cover_photo = bool(flags & (1 << 14))
        id = reader.read_int64()
        url = reader.read_string()
        display_url = reader.read_string()
        hash = reader.read_int32()
        type = reader.read_string() if (flags & (1 << 0)) else None
        site_name = reader.read_string() if (flags & (1 << 1)) else None
        title = reader.read_string() if (flags & (1 << 2)) else None
        description = reader.read_string() if (flags & (1 << 3)) else None
        photo = reader.read_object() if (flags & (1 << 4)) else None
        embed_url = reader.read_string() if (flags & (1 << 5)) else None
        embed_type = reader.read_string() if (flags & (1 << 5)) else None
        embed_width = reader.read_int32() if (flags & (1 << 6)) else None
        embed_height = reader.read_int32() if (flags & (1 << 6)) else None
        duration = reader.read_int32() if (flags & (1 << 7)) else None
        author = reader.read_string() if (flags & (1 << 8)) else None
        document = reader.read_object() if (flags & (1 << 9)) else None
        cached_page = reader.read_object() if (flags & (1 << 10)) else None
        attributes = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 12)) else None
        return cls(has_large_media=has_large_media, video_cover_photo=video_cover_photo, id=id, url=url, display_url=display_url, hash=hash, type=type, site_name=site_name, title=title, description=description, photo=photo, embed_url=embed_url, embed_type=embed_type, embed_width=embed_width, embed_height=embed_height, duration=duration, author=author, document=document, cached_page=cached_page, attributes=attributes)


@register_tl
class WebPageNotModified(TLObject):
    ID: int = 0x7311ca11

    def __init__(self, cached_page_views: Any = None) -> None:
        self.cached_page_views = cached_page_views

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.cached_page_views is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.cached_page_views is not None:
            writer.write_int32(self.cached_page_views or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebPageNotModified':
        flags = reader.read_uint32()
        cached_page_views = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(cached_page_views=cached_page_views)


@register_tl
class Authorization(TLObject):
    ID: int = 0xad01d61d

    def __init__(self, current: bool = False, official_app: bool = False, password_pending: bool = False, encrypted_requests_disabled: bool = False, call_requests_disabled: bool = False, unconfirmed: bool = False, hash: Any = None, device_model: Any = None, platform: Any = None, system_version: Any = None, api_id: Any = None, app_name: Any = None, app_version: Any = None, date_created: Any = None, date_active: Any = None, ip: Any = None, country: Any = None, region: Any = None) -> None:
        self.current = current
        self.official_app = official_app
        self.password_pending = password_pending
        self.encrypted_requests_disabled = encrypted_requests_disabled
        self.call_requests_disabled = call_requests_disabled
        self.unconfirmed = unconfirmed
        self.hash = hash
        self.device_model = device_model
        self.platform = platform
        self.system_version = system_version
        self.api_id = api_id
        self.app_name = app_name
        self.app_version = app_version
        self.date_created = date_created
        self.date_active = date_active
        self.ip = ip
        self.country = country
        self.region = region

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.current:
            flags |= (1 << 0)
        if self.official_app:
            flags |= (1 << 1)
        if self.password_pending:
            flags |= (1 << 2)
        if self.encrypted_requests_disabled:
            flags |= (1 << 3)
        if self.call_requests_disabled:
            flags |= (1 << 4)
        if self.unconfirmed:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_int64(self.hash or 0)
        writer.write_string(self.device_model or '')
        writer.write_string(self.platform or '')
        writer.write_string(self.system_version or '')
        writer.write_int32(self.api_id or 0)
        writer.write_string(self.app_name or '')
        writer.write_string(self.app_version or '')
        writer.write_int32(self.date_created or 0)
        writer.write_int32(self.date_active or 0)
        writer.write_string(self.ip or '')
        writer.write_string(self.country or '')
        writer.write_string(self.region or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'Authorization':
        flags = reader.read_uint32()
        current = bool(flags & (1 << 0))
        official_app = bool(flags & (1 << 1))
        password_pending = bool(flags & (1 << 2))
        encrypted_requests_disabled = bool(flags & (1 << 3))
        call_requests_disabled = bool(flags & (1 << 4))
        unconfirmed = bool(flags & (1 << 5))
        hash = reader.read_int64()
        device_model = reader.read_string()
        platform = reader.read_string()
        system_version = reader.read_string()
        api_id = reader.read_int32()
        app_name = reader.read_string()
        app_version = reader.read_string()
        date_created = reader.read_int32()
        date_active = reader.read_int32()
        ip = reader.read_string()
        country = reader.read_string()
        region = reader.read_string()
        return cls(current=current, official_app=official_app, password_pending=password_pending, encrypted_requests_disabled=encrypted_requests_disabled, call_requests_disabled=call_requests_disabled, unconfirmed=unconfirmed, hash=hash, device_model=device_model, platform=platform, system_version=system_version, api_id=api_id, app_name=app_name, app_version=app_version, date_created=date_created, date_active=date_active, ip=ip, country=country, region=region)


@register_tl
class AccountAuthorizations(TLObject):
    ID: int = 0x4bff8ea0

    def __init__(self, authorization_ttl_days: Any = None, authorizations: Any = None) -> None:
        self.authorization_ttl_days = authorization_ttl_days
        self.authorizations = authorizations

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.authorization_ttl_days or 0)
        writer.write_vector(self.authorizations or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountAuthorizations':
        authorization_ttl_days = reader.read_int32()
        authorizations = reader.read_vector(lambda r: reader.read_object())
        return cls(authorization_ttl_days=authorization_ttl_days, authorizations=authorizations)


@register_tl
class AccountPassword(TLObject):
    ID: int = 0x957b50fb

    def __init__(self, has_recovery: bool = False, has_secure_values: bool = False, has_password: bool = False, current_algo: Any = None, srp_B: Any = None, srp_id: Any = None, hint: Any = None, email_unconfirmed_pattern: Any = None, pending_reset_date: Any = None, login_email_pattern: Any = None, new_algo: Any = None, new_secure_algo: Any = None, secure_random: Any = None) -> None:
        self.has_recovery = has_recovery
        self.has_secure_values = has_secure_values
        self.has_password = has_password
        self.current_algo = current_algo
        self.srp_B = srp_B
        self.srp_id = srp_id
        self.hint = hint
        self.email_unconfirmed_pattern = email_unconfirmed_pattern
        self.pending_reset_date = pending_reset_date
        self.login_email_pattern = login_email_pattern
        self.new_algo = new_algo
        self.new_secure_algo = new_secure_algo
        self.secure_random = secure_random

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_recovery:
            flags |= (1 << 0)
        if self.has_secure_values:
            flags |= (1 << 1)
        if self.has_password:
            flags |= (1 << 2)
        if self.current_algo is not None:
            flags |= (1 << 2)
        if self.srp_B is not None:
            flags |= (1 << 2)
        if self.srp_id is not None:
            flags |= (1 << 2)
        if self.hint is not None:
            flags |= (1 << 3)
        if self.email_unconfirmed_pattern is not None:
            flags |= (1 << 4)
        if self.pending_reset_date is not None:
            flags |= (1 << 5)
        if self.login_email_pattern is not None:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        if self.current_algo is not None:
            if self.current_algo is not None and hasattr(self.current_algo, 'write'): self.current_algo.write(writer)
        if self.srp_B is not None:
            writer.write_bytes(self.srp_B or b'')
        if self.srp_id is not None:
            writer.write_int64(self.srp_id or 0)
        if self.hint is not None:
            writer.write_string(self.hint or '')
        if self.email_unconfirmed_pattern is not None:
            writer.write_string(self.email_unconfirmed_pattern or '')
        if self.new_algo is not None and hasattr(self.new_algo, 'write'): self.new_algo.write(writer)
        if self.new_secure_algo is not None and hasattr(self.new_secure_algo, 'write'): self.new_secure_algo.write(writer)
        writer.write_bytes(self.secure_random or b'')
        if self.pending_reset_date is not None:
            writer.write_int32(self.pending_reset_date or 0)
        if self.login_email_pattern is not None:
            writer.write_string(self.login_email_pattern or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPassword':
        flags = reader.read_uint32()
        has_recovery = bool(flags & (1 << 0))
        has_secure_values = bool(flags & (1 << 1))
        has_password = bool(flags & (1 << 2))
        current_algo = reader.read_object() if (flags & (1 << 2)) else None
        srp_B = reader.read_bytes() if (flags & (1 << 2)) else None
        srp_id = reader.read_int64() if (flags & (1 << 2)) else None
        hint = reader.read_string() if (flags & (1 << 3)) else None
        email_unconfirmed_pattern = reader.read_string() if (flags & (1 << 4)) else None
        new_algo = reader.read_object()
        new_secure_algo = reader.read_object()
        secure_random = reader.read_bytes()
        pending_reset_date = reader.read_int32() if (flags & (1 << 5)) else None
        login_email_pattern = reader.read_string() if (flags & (1 << 6)) else None
        return cls(has_recovery=has_recovery, has_secure_values=has_secure_values, has_password=has_password, current_algo=current_algo, srp_B=srp_B, srp_id=srp_id, hint=hint, email_unconfirmed_pattern=email_unconfirmed_pattern, new_algo=new_algo, new_secure_algo=new_secure_algo, secure_random=secure_random, pending_reset_date=pending_reset_date, login_email_pattern=login_email_pattern)


@register_tl
class AccountPasswordSettings(TLObject):
    ID: int = 0x9a5c33e5

    def __init__(self, email: Any = None, secure_settings: Any = None) -> None:
        self.email = email
        self.secure_settings = secure_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.email is not None:
            flags |= (1 << 0)
        if self.secure_settings is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.email is not None:
            writer.write_string(self.email or '')
        if self.secure_settings is not None:
            if self.secure_settings is not None and hasattr(self.secure_settings, 'write'): self.secure_settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPasswordSettings':
        flags = reader.read_uint32()
        email = reader.read_string() if (flags & (1 << 0)) else None
        secure_settings = reader.read_object() if (flags & (1 << 1)) else None
        return cls(email=email, secure_settings=secure_settings)


@register_tl
class AccountPasswordInputSettings(TLObject):
    ID: int = 0xc23727c9

    def __init__(self, new_algo: Any = None, new_password_hash: Any = None, hint: Any = None, email: Any = None, new_secure_settings: Any = None) -> None:
        self.new_algo = new_algo
        self.new_password_hash = new_password_hash
        self.hint = hint
        self.email = email
        self.new_secure_settings = new_secure_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.new_algo is not None:
            flags |= (1 << 0)
        if self.new_password_hash is not None:
            flags |= (1 << 0)
        if self.hint is not None:
            flags |= (1 << 0)
        if self.email is not None:
            flags |= (1 << 1)
        if self.new_secure_settings is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.new_algo is not None:
            if self.new_algo is not None and hasattr(self.new_algo, 'write'): self.new_algo.write(writer)
        if self.new_password_hash is not None:
            writer.write_bytes(self.new_password_hash or b'')
        if self.hint is not None:
            writer.write_string(self.hint or '')
        if self.email is not None:
            writer.write_string(self.email or '')
        if self.new_secure_settings is not None:
            if self.new_secure_settings is not None and hasattr(self.new_secure_settings, 'write'): self.new_secure_settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountPasswordInputSettings':
        flags = reader.read_uint32()
        new_algo = reader.read_object() if (flags & (1 << 0)) else None
        new_password_hash = reader.read_bytes() if (flags & (1 << 0)) else None
        hint = reader.read_string() if (flags & (1 << 0)) else None
        email = reader.read_string() if (flags & (1 << 1)) else None
        new_secure_settings = reader.read_object() if (flags & (1 << 2)) else None
        return cls(new_algo=new_algo, new_password_hash=new_password_hash, hint=hint, email=email, new_secure_settings=new_secure_settings)


@register_tl
class AuthPasswordRecovery(TLObject):
    ID: int = 0x137948a5

    def __init__(self, email_pattern: Any = None) -> None:
        self.email_pattern = email_pattern

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.email_pattern or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'AuthPasswordRecovery':
        email_pattern = reader.read_string()
        return cls(email_pattern=email_pattern)


@register_tl
class ReceivedNotifyMessage(TLObject):
    ID: int = 0xa384b779

    def __init__(self, id: Any = None, flags: Any = None) -> None:
        self.id = id
        self.flags = flags

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.id or 0)
        writer.write_int32(self.flags or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReceivedNotifyMessage':
        id = reader.read_int32()
        flags = reader.read_int32()
        return cls(id=id, flags=flags)


@register_tl
class ChatInviteExported(TLObject):
    ID: int = 0xa22cbd96

    def __init__(self, revoked: bool = False, permanent: bool = False, request_needed: bool = False, start_date: Any = None, expire_date: Any = None, usage_limit: Any = None, usage: Any = None, requested: Any = None, subscription_expired: Any = None, title: Any = None, subscription_pricing: Any = None, link: Any = None, admin_id: Any = None, date: Any = None) -> None:
        self.revoked = revoked
        self.permanent = permanent
        self.request_needed = request_needed
        self.start_date = start_date
        self.expire_date = expire_date
        self.usage_limit = usage_limit
        self.usage = usage
        self.requested = requested
        self.subscription_expired = subscription_expired
        self.title = title
        self.subscription_pricing = subscription_pricing
        self.link = link
        self.admin_id = admin_id
        self.date = date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.revoked:
            flags |= (1 << 0)
        if self.permanent:
            flags |= (1 << 5)
        if self.request_needed:
            flags |= (1 << 6)
        if self.start_date is not None:
            flags |= (1 << 4)
        if self.expire_date is not None:
            flags |= (1 << 1)
        if self.usage_limit is not None:
            flags |= (1 << 2)
        if self.usage is not None:
            flags |= (1 << 3)
        if self.requested is not None:
            flags |= (1 << 7)
        if self.subscription_expired is not None:
            flags |= (1 << 10)
        if self.title is not None:
            flags |= (1 << 8)
        if self.subscription_pricing is not None:
            flags |= (1 << 9)
        writer.write_uint32(flags)
        writer.write_string(self.link or '')
        writer.write_int64(self.admin_id or 0)
        writer.write_int32(self.date or 0)
        if self.start_date is not None:
            writer.write_int32(self.start_date or 0)
        if self.expire_date is not None:
            writer.write_int32(self.expire_date or 0)
        if self.usage_limit is not None:
            writer.write_int32(self.usage_limit or 0)
        if self.usage is not None:
            writer.write_int32(self.usage or 0)
        if self.requested is not None:
            writer.write_int32(self.requested or 0)
        if self.subscription_expired is not None:
            writer.write_int32(self.subscription_expired or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.subscription_pricing is not None:
            if self.subscription_pricing is not None and hasattr(self.subscription_pricing, 'write'): self.subscription_pricing.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatInviteExported':
        flags = reader.read_uint32()
        revoked = bool(flags & (1 << 0))
        permanent = bool(flags & (1 << 5))
        request_needed = bool(flags & (1 << 6))
        link = reader.read_string()
        admin_id = reader.read_int64()
        date = reader.read_int32()
        start_date = reader.read_int32() if (flags & (1 << 4)) else None
        expire_date = reader.read_int32() if (flags & (1 << 1)) else None
        usage_limit = reader.read_int32() if (flags & (1 << 2)) else None
        usage = reader.read_int32() if (flags & (1 << 3)) else None
        requested = reader.read_int32() if (flags & (1 << 7)) else None
        subscription_expired = reader.read_int32() if (flags & (1 << 10)) else None
        title = reader.read_string() if (flags & (1 << 8)) else None
        subscription_pricing = reader.read_object() if (flags & (1 << 9)) else None
        return cls(revoked=revoked, permanent=permanent, request_needed=request_needed, link=link, admin_id=admin_id, date=date, start_date=start_date, expire_date=expire_date, usage_limit=usage_limit, usage=usage, requested=requested, subscription_expired=subscription_expired, title=title, subscription_pricing=subscription_pricing)


@register_tl
class ChatInvitePublicJoinRequests(TLObject):
    ID: int = 0xed107ab7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatInvitePublicJoinRequests':
        return cls()


@register_tl
class ChatInviteAlready(TLObject):
    ID: int = 0x5a686d7c

    def __init__(self, chat: Any = None) -> None:
        self.chat = chat

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chat is not None and hasattr(self.chat, 'write'): self.chat.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatInviteAlready':
        chat = reader.read_object()
        return cls(chat=chat)


@register_tl
class ChatInvite(TLObject):
    ID: int = 0x5c9d3702

    def __init__(self, channel: bool = False, broadcast: bool = False, public: bool = False, megagroup: bool = False, request_needed: bool = False, verified: bool = False, scam: bool = False, fake: bool = False, can_refulfill_subscription: bool = False, about: Any = None, participants: Any = None, subscription_pricing: Any = None, subscription_form_id: Any = None, bot_verification: Any = None, title: Any = None, photo: Any = None, participants_count: Any = None, color: Any = None) -> None:
        self.channel = channel
        self.broadcast = broadcast
        self.public = public
        self.megagroup = megagroup
        self.request_needed = request_needed
        self.verified = verified
        self.scam = scam
        self.fake = fake
        self.can_refulfill_subscription = can_refulfill_subscription
        self.about = about
        self.participants = participants
        self.subscription_pricing = subscription_pricing
        self.subscription_form_id = subscription_form_id
        self.bot_verification = bot_verification
        self.title = title
        self.photo = photo
        self.participants_count = participants_count
        self.color = color

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.channel:
            flags |= (1 << 0)
        if self.broadcast:
            flags |= (1 << 1)
        if self.public:
            flags |= (1 << 2)
        if self.megagroup:
            flags |= (1 << 3)
        if self.request_needed:
            flags |= (1 << 6)
        if self.verified:
            flags |= (1 << 7)
        if self.scam:
            flags |= (1 << 8)
        if self.fake:
            flags |= (1 << 9)
        if self.can_refulfill_subscription:
            flags |= (1 << 11)
        if self.about is not None:
            flags |= (1 << 5)
        if self.participants is not None:
            flags |= (1 << 4)
        if self.subscription_pricing is not None:
            flags |= (1 << 10)
        if self.subscription_form_id is not None:
            flags |= (1 << 12)
        if self.bot_verification is not None:
            flags |= (1 << 13)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        if self.about is not None:
            writer.write_string(self.about or '')
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        writer.write_int32(self.participants_count or 0)
        if self.participants is not None:
            writer.write_vector(self.participants or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.color or 0)
        if self.subscription_pricing is not None:
            if self.subscription_pricing is not None and hasattr(self.subscription_pricing, 'write'): self.subscription_pricing.write(writer)
        if self.subscription_form_id is not None:
            writer.write_int64(self.subscription_form_id or 0)
        if self.bot_verification is not None:
            if self.bot_verification is not None and hasattr(self.bot_verification, 'write'): self.bot_verification.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatInvite':
        flags = reader.read_uint32()
        channel = bool(flags & (1 << 0))
        broadcast = bool(flags & (1 << 1))
        public = bool(flags & (1 << 2))
        megagroup = bool(flags & (1 << 3))
        request_needed = bool(flags & (1 << 6))
        verified = bool(flags & (1 << 7))
        scam = bool(flags & (1 << 8))
        fake = bool(flags & (1 << 9))
        can_refulfill_subscription = bool(flags & (1 << 11))
        title = reader.read_string()
        about = reader.read_string() if (flags & (1 << 5)) else None
        photo = reader.read_object()
        participants_count = reader.read_int32()
        participants = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        color = reader.read_int32()
        subscription_pricing = reader.read_object() if (flags & (1 << 10)) else None
        subscription_form_id = reader.read_int64() if (flags & (1 << 12)) else None
        bot_verification = reader.read_object() if (flags & (1 << 13)) else None
        return cls(channel=channel, broadcast=broadcast, public=public, megagroup=megagroup, request_needed=request_needed, verified=verified, scam=scam, fake=fake, can_refulfill_subscription=can_refulfill_subscription, title=title, about=about, photo=photo, participants_count=participants_count, participants=participants, color=color, subscription_pricing=subscription_pricing, subscription_form_id=subscription_form_id, bot_verification=bot_verification)


@register_tl
class ChatInvitePeek(TLObject):
    ID: int = 0x61695cb0

    def __init__(self, chat: Any = None, expires: Any = None) -> None:
        self.chat = chat
        self.expires = expires

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.chat is not None and hasattr(self.chat, 'write'): self.chat.write(writer)
        writer.write_int32(self.expires or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChatInvitePeek':
        chat = reader.read_object()
        expires = reader.read_int32()
        return cls(chat=chat, expires=expires)


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
class InputStickerSetID(TLObject):
    ID: int = 0x9de7a269

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetID':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


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
class InputStickerSetAnimatedEmoji(TLObject):
    ID: int = 0x28703c8

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetAnimatedEmoji':
        return cls()


@register_tl
class InputStickerSetDice(TLObject):
    ID: int = 0xe67f520e

    def __init__(self, emoticon: Any = None) -> None:
        self.emoticon = emoticon

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.emoticon or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetDice':
        emoticon = reader.read_string()
        return cls(emoticon=emoticon)


@register_tl
class InputStickerSetAnimatedEmojiAnimations(TLObject):
    ID: int = 0xcde3739

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetAnimatedEmojiAnimations':
        return cls()


@register_tl
class InputStickerSetPremiumGifts(TLObject):
    ID: int = 0xc88b3b02

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetPremiumGifts':
        return cls()


@register_tl
class InputStickerSetEmojiGenericAnimations(TLObject):
    ID: int = 0x4c4d4ce

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetEmojiGenericAnimations':
        return cls()


@register_tl
class InputStickerSetEmojiDefaultStatuses(TLObject):
    ID: int = 0x29d0f5ee

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetEmojiDefaultStatuses':
        return cls()


@register_tl
class InputStickerSetEmojiDefaultTopicIcons(TLObject):
    ID: int = 0x44c1f8e9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetEmojiDefaultTopicIcons':
        return cls()


@register_tl
class InputStickerSetEmojiChannelDefaultStatuses(TLObject):
    ID: int = 0x49748553

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetEmojiChannelDefaultStatuses':
        return cls()


@register_tl
class InputStickerSetTonGifts(TLObject):
    ID: int = 0x1cf671a0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetTonGifts':
        return cls()


@register_tl
class StickerSet(TLObject):
    ID: int = 0x2dd14edc

    def __init__(self, archived: bool = False, official: bool = False, masks: bool = False, emojis: bool = False, text_color: bool = False, channel_emoji_status: bool = False, creator: bool = False, installed_date: Any = None, thumbs: Any = None, thumb_dc_id: Any = None, thumb_version: Any = None, thumb_document_id: Any = None, id: Any = None, access_hash: Any = None, title: Any = None, short_name: Any = None, count: Any = None, hash: Any = None) -> None:
        self.archived = archived
        self.official = official
        self.masks = masks
        self.emojis = emojis
        self.text_color = text_color
        self.channel_emoji_status = channel_emoji_status
        self.creator = creator
        self.installed_date = installed_date
        self.thumbs = thumbs
        self.thumb_dc_id = thumb_dc_id
        self.thumb_version = thumb_version
        self.thumb_document_id = thumb_document_id
        self.id = id
        self.access_hash = access_hash
        self.title = title
        self.short_name = short_name
        self.count = count
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.archived:
            flags |= (1 << 1)
        if self.official:
            flags |= (1 << 2)
        if self.masks:
            flags |= (1 << 3)
        if self.emojis:
            flags |= (1 << 7)
        if self.text_color:
            flags |= (1 << 9)
        if self.channel_emoji_status:
            flags |= (1 << 10)
        if self.creator:
            flags |= (1 << 11)
        if self.installed_date is not None:
            flags |= (1 << 0)
        if self.thumbs is not None:
            flags |= (1 << 4)
        if self.thumb_dc_id is not None:
            flags |= (1 << 4)
        if self.thumb_version is not None:
            flags |= (1 << 4)
        if self.thumb_document_id is not None:
            flags |= (1 << 8)
        writer.write_uint32(flags)
        if self.installed_date is not None:
            writer.write_int32(self.installed_date or 0)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.short_name or '')
        if self.thumbs is not None:
            writer.write_vector(self.thumbs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.thumb_dc_id is not None:
            writer.write_int32(self.thumb_dc_id or 0)
        if self.thumb_version is not None:
            writer.write_int32(self.thumb_version or 0)
        if self.thumb_document_id is not None:
            writer.write_int64(self.thumb_document_id or 0)
        writer.write_int32(self.count or 0)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'StickerSet':
        flags = reader.read_uint32()
        archived = bool(flags & (1 << 1))
        official = bool(flags & (1 << 2))
        masks = bool(flags & (1 << 3))
        emojis = bool(flags & (1 << 7))
        text_color = bool(flags & (1 << 9))
        channel_emoji_status = bool(flags & (1 << 10))
        creator = bool(flags & (1 << 11))
        installed_date = reader.read_int32() if (flags & (1 << 0)) else None
        id = reader.read_int64()
        access_hash = reader.read_int64()
        title = reader.read_string()
        short_name = reader.read_string()
        thumbs = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 4)) else None
        thumb_dc_id = reader.read_int32() if (flags & (1 << 4)) else None
        thumb_version = reader.read_int32() if (flags & (1 << 4)) else None
        thumb_document_id = reader.read_int64() if (flags & (1 << 8)) else None
        count = reader.read_int32()
        hash = reader.read_int32()
        return cls(archived=archived, official=official, masks=masks, emojis=emojis, text_color=text_color, channel_emoji_status=channel_emoji_status, creator=creator, installed_date=installed_date, id=id, access_hash=access_hash, title=title, short_name=short_name, thumbs=thumbs, thumb_dc_id=thumb_dc_id, thumb_version=thumb_version, thumb_document_id=thumb_document_id, count=count, hash=hash)


@register_tl
class MessagesStickerSet(TLObject):
    ID: int = 0x6e153f16

    def __init__(self, set: Any = None, packs: Any = None, keywords: Any = None, documents: Any = None) -> None:
        self.set = set
        self.packs = packs
        self.keywords = keywords
        self.documents = documents

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.set is not None and hasattr(self.set, 'write'): self.set.write(writer)
        writer.write_vector(self.packs or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.keywords or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.documents or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStickerSet':
        set = reader.read_object()
        packs = reader.read_vector(lambda r: reader.read_object())
        keywords = reader.read_vector(lambda r: reader.read_object())
        documents = reader.read_vector(lambda r: reader.read_object())
        return cls(set=set, packs=packs, keywords=keywords, documents=documents)


@register_tl
class MessagesStickerSetNotModified(TLObject):
    ID: int = 0xd3f924eb

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesStickerSetNotModified':
        return cls()


@register_tl
class BotCommand(TLObject):
    ID: int = 0xc27ac8c7

    def __init__(self, command: Any = None, description: Any = None) -> None:
        self.command = command
        self.description = description

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.command or '')
        writer.write_string(self.description or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotCommand':
        command = reader.read_string()
        description = reader.read_string()
        return cls(command=command, description=description)


@register_tl
class BotInfo(TLObject):
    ID: int = 0x4d8a0299

    def __init__(self, has_preview_medias: bool = False, user_id: Any = None, description: Any = None, description_photo: Any = None, description_document: Any = None, commands: Any = None, menu_button: Any = None, privacy_policy_url: Any = None, app_settings: Any = None, verifier_settings: Any = None) -> None:
        self.has_preview_medias = has_preview_medias
        self.user_id = user_id
        self.description = description
        self.description_photo = description_photo
        self.description_document = description_document
        self.commands = commands
        self.menu_button = menu_button
        self.privacy_policy_url = privacy_policy_url
        self.app_settings = app_settings
        self.verifier_settings = verifier_settings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_preview_medias:
            flags |= (1 << 6)
        if self.user_id is not None:
            flags |= (1 << 0)
        if self.description is not None:
            flags |= (1 << 1)
        if self.description_photo is not None:
            flags |= (1 << 4)
        if self.description_document is not None:
            flags |= (1 << 5)
        if self.commands is not None:
            flags |= (1 << 2)
        if self.menu_button is not None:
            flags |= (1 << 3)
        if self.privacy_policy_url is not None:
            flags |= (1 << 7)
        if self.app_settings is not None:
            flags |= (1 << 8)
        if self.verifier_settings is not None:
            flags |= (1 << 9)
        writer.write_uint32(flags)
        if self.user_id is not None:
            writer.write_int64(self.user_id or 0)
        if self.description is not None:
            writer.write_string(self.description or '')
        if self.description_photo is not None:
            if self.description_photo is not None and hasattr(self.description_photo, 'write'): self.description_photo.write(writer)
        if self.description_document is not None:
            if self.description_document is not None and hasattr(self.description_document, 'write'): self.description_document.write(writer)
        if self.commands is not None:
            writer.write_vector(self.commands or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.menu_button is not None:
            if self.menu_button is not None and hasattr(self.menu_button, 'write'): self.menu_button.write(writer)
        if self.privacy_policy_url is not None:
            writer.write_string(self.privacy_policy_url or '')
        if self.app_settings is not None:
            if self.app_settings is not None and hasattr(self.app_settings, 'write'): self.app_settings.write(writer)
        if self.verifier_settings is not None:
            if self.verifier_settings is not None and hasattr(self.verifier_settings, 'write'): self.verifier_settings.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotInfo':
        flags = reader.read_uint32()
        has_preview_medias = bool(flags & (1 << 6))
        user_id = reader.read_int64() if (flags & (1 << 0)) else None
        description = reader.read_string() if (flags & (1 << 1)) else None
        description_photo = reader.read_object() if (flags & (1 << 4)) else None
        description_document = reader.read_object() if (flags & (1 << 5)) else None
        commands = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 2)) else None
        menu_button = reader.read_object() if (flags & (1 << 3)) else None
        privacy_policy_url = reader.read_string() if (flags & (1 << 7)) else None
        app_settings = reader.read_object() if (flags & (1 << 8)) else None
        verifier_settings = reader.read_object() if (flags & (1 << 9)) else None
        return cls(has_preview_medias=has_preview_medias, user_id=user_id, description=description, description_photo=description_photo, description_document=description_document, commands=commands, menu_button=menu_button, privacy_policy_url=privacy_policy_url, app_settings=app_settings, verifier_settings=verifier_settings)


@register_tl
class KeyboardButton(TLObject):
    ID: int = 0x7d170cff

    def __init__(self, style: Any = None, text: Any = None) -> None:
        self.style = style
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButton':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        return cls(style=style, text=text)


@register_tl
class KeyboardButtonUrl(TLObject):
    ID: int = 0xd80c25ec

    def __init__(self, style: Any = None, text: Any = None, url: Any = None) -> None:
        self.style = style
        self.text = text
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonUrl':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        url = reader.read_string()
        return cls(style=style, text=text, url=url)


@register_tl
class KeyboardButtonCallback(TLObject):
    ID: int = 0xe62bc960

    def __init__(self, requires_password: bool = False, style: Any = None, text: Any = None, data: Any = None) -> None:
        self.requires_password = requires_password
        self.style = style
        self.text = text
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.requires_password:
            flags |= (1 << 0)
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_bytes(self.data or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonCallback':
        flags = reader.read_uint32()
        requires_password = bool(flags & (1 << 0))
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        data = reader.read_bytes()
        return cls(requires_password=requires_password, style=style, text=text, data=data)


@register_tl
class KeyboardButtonRequestPhone(TLObject):
    ID: int = 0x417efd8f

    def __init__(self, style: Any = None, text: Any = None) -> None:
        self.style = style
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonRequestPhone':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        return cls(style=style, text=text)


@register_tl
class KeyboardButtonRequestGeoLocation(TLObject):
    ID: int = 0xaa40f94d

    def __init__(self, style: Any = None, text: Any = None) -> None:
        self.style = style
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonRequestGeoLocation':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        return cls(style=style, text=text)


@register_tl
class KeyboardButtonSwitchInline(TLObject):
    ID: int = 0x991399fc

    def __init__(self, same_peer: bool = False, style: Any = None, peer_types: Any = None, text: Any = None, query: Any = None) -> None:
        self.same_peer = same_peer
        self.style = style
        self.peer_types = peer_types
        self.text = text
        self.query = query

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.same_peer:
            flags |= (1 << 0)
        if self.style is not None:
            flags |= (1 << 10)
        if self.peer_types is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_string(self.query or '')
        if self.peer_types is not None:
            writer.write_vector(self.peer_types or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonSwitchInline':
        flags = reader.read_uint32()
        same_peer = bool(flags & (1 << 0))
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        query = reader.read_string()
        peer_types = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        return cls(same_peer=same_peer, style=style, text=text, query=query, peer_types=peer_types)


@register_tl
class KeyboardButtonGame(TLObject):
    ID: int = 0x89c590f9

    def __init__(self, style: Any = None, text: Any = None) -> None:
        self.style = style
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonGame':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        return cls(style=style, text=text)


@register_tl
class KeyboardButtonBuy(TLObject):
    ID: int = 0x3fa53905

    def __init__(self, style: Any = None, text: Any = None) -> None:
        self.style = style
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonBuy':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        return cls(style=style, text=text)


@register_tl
class KeyboardButtonUrlAuth(TLObject):
    ID: int = 0xf51006f9

    def __init__(self, style: Any = None, fwd_text: Any = None, text: Any = None, url: Any = None, button_id: Any = None) -> None:
        self.style = style
        self.fwd_text = fwd_text
        self.text = text
        self.url = url
        self.button_id = button_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        if self.fwd_text is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        if self.fwd_text is not None:
            writer.write_string(self.fwd_text or '')
        writer.write_string(self.url or '')
        writer.write_int32(self.button_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonUrlAuth':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        fwd_text = reader.read_string() if (flags & (1 << 0)) else None
        url = reader.read_string()
        button_id = reader.read_int32()
        return cls(style=style, text=text, fwd_text=fwd_text, url=url, button_id=button_id)


@register_tl
class InputKeyboardButtonUrlAuth(TLObject):
    ID: int = 0x68013e72

    def __init__(self, request_write_access: bool = False, style: Any = None, fwd_text: Any = None, text: Any = None, url: Any = None, bot: Any = None) -> None:
        self.request_write_access = request_write_access
        self.style = style
        self.fwd_text = fwd_text
        self.text = text
        self.url = url
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.request_write_access:
            flags |= (1 << 0)
        if self.style is not None:
            flags |= (1 << 10)
        if self.fwd_text is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        if self.fwd_text is not None:
            writer.write_string(self.fwd_text or '')
        writer.write_string(self.url or '')
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputKeyboardButtonUrlAuth':
        flags = reader.read_uint32()
        request_write_access = bool(flags & (1 << 0))
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        fwd_text = reader.read_string() if (flags & (1 << 1)) else None
        url = reader.read_string()
        bot = reader.read_object()
        return cls(request_write_access=request_write_access, style=style, text=text, fwd_text=fwd_text, url=url, bot=bot)


@register_tl
class KeyboardButtonRequestPoll(TLObject):
    ID: int = 0x7a11d782

    def __init__(self, style: Any = None, quiz: Any = None, text: Any = None) -> None:
        self.style = style
        self.quiz = quiz
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        if self.quiz is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        if self.quiz is not None:
            writer.write_bool(bool(self.quiz))
        writer.write_string(self.text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonRequestPoll':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        quiz = reader.read_bool() if (flags & (1 << 0)) else None
        text = reader.read_string()
        return cls(style=style, quiz=quiz, text=text)


@register_tl
class InputKeyboardButtonUserProfile(TLObject):
    ID: int = 0x7d5e07c7

    def __init__(self, style: Any = None, text: Any = None, user_id: Any = None) -> None:
        self.style = style
        self.text = text
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputKeyboardButtonUserProfile':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        user_id = reader.read_object()
        return cls(style=style, text=text, user_id=user_id)


@register_tl
class KeyboardButtonUserProfile(TLObject):
    ID: int = 0xc0fd5d09

    def __init__(self, style: Any = None, text: Any = None, user_id: Any = None) -> None:
        self.style = style
        self.text = text
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_int64(self.user_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonUserProfile':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        user_id = reader.read_int64()
        return cls(style=style, text=text, user_id=user_id)


@register_tl
class KeyboardButtonWebView(TLObject):
    ID: int = 0xe846b1a0

    def __init__(self, style: Any = None, text: Any = None, url: Any = None) -> None:
        self.style = style
        self.text = text
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonWebView':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        url = reader.read_string()
        return cls(style=style, text=text, url=url)


@register_tl
class KeyboardButtonSimpleWebView(TLObject):
    ID: int = 0xe15c4370

    def __init__(self, style: Any = None, text: Any = None, url: Any = None) -> None:
        self.style = style
        self.text = text
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonSimpleWebView':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        url = reader.read_string()
        return cls(style=style, text=text, url=url)


@register_tl
class KeyboardButtonRequestPeer(TLObject):
    ID: int = 0x5b0f15f5

    def __init__(self, style: Any = None, text: Any = None, button_id: Any = None, peer_type: Any = None, max_quantity: Any = None) -> None:
        self.style = style
        self.text = text
        self.button_id = button_id
        self.peer_type = peer_type
        self.max_quantity = max_quantity

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_int32(self.button_id or 0)
        if self.peer_type is not None and hasattr(self.peer_type, 'write'): self.peer_type.write(writer)
        writer.write_int32(self.max_quantity or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonRequestPeer':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        button_id = reader.read_int32()
        peer_type = reader.read_object()
        max_quantity = reader.read_int32()
        return cls(style=style, text=text, button_id=button_id, peer_type=peer_type, max_quantity=max_quantity)


@register_tl
class InputKeyboardButtonRequestPeer(TLObject):
    ID: int = 0x2b78156

    def __init__(self, name_requested: bool = False, username_requested: bool = False, photo_requested: bool = False, style: Any = None, text: Any = None, button_id: Any = None, peer_type: Any = None, max_quantity: Any = None) -> None:
        self.name_requested = name_requested
        self.username_requested = username_requested
        self.photo_requested = photo_requested
        self.style = style
        self.text = text
        self.button_id = button_id
        self.peer_type = peer_type
        self.max_quantity = max_quantity

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.name_requested:
            flags |= (1 << 0)
        if self.username_requested:
            flags |= (1 << 1)
        if self.photo_requested:
            flags |= (1 << 2)
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_int32(self.button_id or 0)
        if self.peer_type is not None and hasattr(self.peer_type, 'write'): self.peer_type.write(writer)
        writer.write_int32(self.max_quantity or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputKeyboardButtonRequestPeer':
        flags = reader.read_uint32()
        name_requested = bool(flags & (1 << 0))
        username_requested = bool(flags & (1 << 1))
        photo_requested = bool(flags & (1 << 2))
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        button_id = reader.read_int32()
        peer_type = reader.read_object()
        max_quantity = reader.read_int32()
        return cls(name_requested=name_requested, username_requested=username_requested, photo_requested=photo_requested, style=style, text=text, button_id=button_id, peer_type=peer_type, max_quantity=max_quantity)


@register_tl
class KeyboardButtonCopy(TLObject):
    ID: int = 0xbcc4af10

    def __init__(self, style: Any = None, text: Any = None, copy_text: Any = None) -> None:
        self.style = style
        self.text = text
        self.copy_text = copy_text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.style is not None:
            flags |= (1 << 10)
        writer.write_uint32(flags)
        if self.style is not None:
            if self.style is not None and hasattr(self.style, 'write'): self.style.write(writer)
        writer.write_string(self.text or '')
        writer.write_string(self.copy_text or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonCopy':
        flags = reader.read_uint32()
        style = reader.read_object() if (flags & (1 << 10)) else None
        text = reader.read_string()
        copy_text = reader.read_string()
        return cls(style=style, text=text, copy_text=copy_text)


@register_tl
class KeyboardButtonRow(TLObject):
    ID: int = 0x77608b83

    def __init__(self, buttons: Any = None) -> None:
        self.buttons = buttons

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.buttons or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'KeyboardButtonRow':
        buttons = reader.read_vector(lambda r: reader.read_object())
        return cls(buttons=buttons)


@register_tl
class ReplyKeyboardHide(TLObject):
    ID: int = 0xa03e5b85

    def __init__(self, selective: bool = False) -> None:
        self.selective = selective

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.selective:
            flags |= (1 << 2)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReplyKeyboardHide':
        flags = reader.read_uint32()
        selective = bool(flags & (1 << 2))
        return cls(selective=selective)


@register_tl
class ReplyKeyboardForceReply(TLObject):
    ID: int = 0x86b40b08

    def __init__(self, single_use: bool = False, selective: bool = False, placeholder: Any = None) -> None:
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
            writer.write_string(self.placeholder or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ReplyKeyboardForceReply':
        flags = reader.read_uint32()
        single_use = bool(flags & (1 << 1))
        selective = bool(flags & (1 << 2))
        placeholder = reader.read_string() if (flags & (1 << 3)) else None
        return cls(single_use=single_use, selective=selective, placeholder=placeholder)


@register_tl
class ReplyKeyboardMarkup(TLObject):
    ID: int = 0x85dd99d1

    def __init__(self, resize: bool = False, single_use: bool = False, selective: bool = False, persistent: bool = False, placeholder: Any = None, rows: Any = None) -> None:
        self.resize = resize
        self.single_use = single_use
        self.selective = selective
        self.persistent = persistent
        self.placeholder = placeholder
        self.rows = rows

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.resize:
            flags |= (1 << 0)
        if self.single_use:
            flags |= (1 << 1)
        if self.selective:
            flags |= (1 << 2)
        if self.persistent:
            flags |= (1 << 4)
        if self.placeholder is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_vector(self.rows or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.placeholder is not None:
            writer.write_string(self.placeholder or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ReplyKeyboardMarkup':
        flags = reader.read_uint32()
        resize = bool(flags & (1 << 0))
        single_use = bool(flags & (1 << 1))
        selective = bool(flags & (1 << 2))
        persistent = bool(flags & (1 << 4))
        rows = reader.read_vector(lambda r: reader.read_object())
        placeholder = reader.read_string() if (flags & (1 << 3)) else None
        return cls(resize=resize, single_use=single_use, selective=selective, persistent=persistent, rows=rows, placeholder=placeholder)


@register_tl
class ReplyInlineMarkup(TLObject):
    ID: int = 0x48a30254

    def __init__(self, rows: Any = None) -> None:
        self.rows = rows

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.rows or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ReplyInlineMarkup':
        rows = reader.read_vector(lambda r: reader.read_object())
        return cls(rows=rows)


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

