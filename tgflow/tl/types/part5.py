from typing import Any
from ..core import TLObject, TLWriter, TLReader, register_tl

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
