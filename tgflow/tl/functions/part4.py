from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class MessagesToggleTodoCompleted(TLRequest):
    ID: int = 0xd3e03124

    def __init__(self, peer: Any = None, msg_id: Any = None, completed: Any = None, incompleted: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.completed = completed
        self.incompleted = incompleted

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_vector(self.completed or [], lambda w, x: w.write_int32(x))
        writer.write_vector(self.incompleted or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesToggleTodoCompleted':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        completed = reader.read_vector(lambda r: r.read_int32())
        incompleted = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, msg_id=msg_id, completed=completed, incompleted=incompleted)


@register_tl
class MessagesAppendTodoList(TLRequest):
    ID: int = 0x21a61057

    def __init__(self, peer: Any = None, msg_id: Any = None, list: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.list = list

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_vector(self.list or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAppendTodoList':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        list = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, msg_id=msg_id, list=list)


@register_tl
class MessagesToggleSuggestedPostApproval(TLRequest):
    ID: int = 0x8107455c

    def __init__(self, reject: bool = False, schedule_date: Any = None, reject_comment: Any = None, peer: Any = None, msg_id: Any = None) -> None:
        self.reject = reject
        self.schedule_date = schedule_date
        self.reject_comment = reject_comment
        self.peer = peer
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.reject:
            flags |= (1 << 1)
        if self.schedule_date is not None:
            flags |= (1 << 0)
        if self.reject_comment is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        if self.schedule_date is not None:
            writer.write_int32(self.schedule_date or 0)
        if self.reject_comment is not None:
            writer.write_string(self.reject_comment or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesToggleSuggestedPostApproval':
        flags = reader.read_uint32()
        reject = bool(flags & (1 << 1))
        peer = reader.read_object()
        msg_id = reader.read_int32()
        schedule_date = reader.read_int32() if (flags & (1 << 0)) else None
        reject_comment = reader.read_string() if (flags & (1 << 2)) else None
        return cls(reject=reject, peer=peer, msg_id=msg_id, schedule_date=schedule_date, reject_comment=reject_comment)


@register_tl
class MessagesGetForumTopics(TLRequest):
    ID: int = 0x3ba47bff

    def __init__(self, q: Any = None, peer: Any = None, offset_date: Any = None, offset_id: Any = None, offset_topic: Any = None, limit: Any = None) -> None:
        self.q = q
        self.peer = peer
        self.offset_date = offset_date
        self.offset_id = offset_id
        self.offset_topic = offset_topic
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.q is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.q is not None:
            writer.write_string(self.q or '')
        writer.write_int32(self.offset_date or 0)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.offset_topic or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetForumTopics':
        flags = reader.read_uint32()
        peer = reader.read_object()
        q = reader.read_string() if (flags & (1 << 0)) else None
        offset_date = reader.read_int32()
        offset_id = reader.read_int32()
        offset_topic = reader.read_int32()
        limit = reader.read_int32()
        return cls(peer=peer, q=q, offset_date=offset_date, offset_id=offset_id, offset_topic=offset_topic, limit=limit)


@register_tl
class MessagesGetForumTopicsByID(TLRequest):
    ID: int = 0xaf0a4a08

    def __init__(self, peer: Any = None, topics: Any = None) -> None:
        self.peer = peer
        self.topics = topics

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.topics or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetForumTopicsByID':
        peer = reader.read_object()
        topics = reader.read_vector(lambda r: r.read_int32())
        return cls(peer=peer, topics=topics)


@register_tl
class MessagesEditForumTopic(TLRequest):
    ID: int = 0xcecc1134

    def __init__(self, title: Any = None, icon_emoji_id: Any = None, closed: Any = None, hidden: Any = None, peer: Any = None, topic_id: Any = None) -> None:
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.closed = closed
        self.hidden = hidden
        self.peer = peer
        self.topic_id = topic_id

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
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.topic_id or 0)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)
        if self.closed is not None:
            writer.write_bool(bool(self.closed))
        if self.hidden is not None:
            writer.write_bool(bool(self.hidden))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditForumTopic':
        flags = reader.read_uint32()
        peer = reader.read_object()
        topic_id = reader.read_int32()
        title = reader.read_string() if (flags & (1 << 0)) else None
        icon_emoji_id = reader.read_int64() if (flags & (1 << 1)) else None
        closed = reader.read_bool() if (flags & (1 << 2)) else None
        hidden = reader.read_bool() if (flags & (1 << 3)) else None
        return cls(peer=peer, topic_id=topic_id, title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)


@register_tl
class MessagesUpdatePinnedForumTopic(TLRequest):
    ID: int = 0x175df251

    def __init__(self, peer: Any = None, topic_id: Any = None, pinned: Any = None) -> None:
        self.peer = peer
        self.topic_id = topic_id
        self.pinned = pinned

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.topic_id or 0)
        writer.write_bool(bool(self.pinned))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesUpdatePinnedForumTopic':
        peer = reader.read_object()
        topic_id = reader.read_int32()
        pinned = reader.read_bool()
        return cls(peer=peer, topic_id=topic_id, pinned=pinned)


@register_tl
class MessagesReorderPinnedForumTopics(TLRequest):
    ID: int = 0xe7841f0

    def __init__(self, force: bool = False, peer: Any = None, order: Any = None) -> None:
        self.force = force
        self.peer = peer
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.force:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.order or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReorderPinnedForumTopics':
        flags = reader.read_uint32()
        force = bool(flags & (1 << 0))
        peer = reader.read_object()
        order = reader.read_vector(lambda r: r.read_int32())
        return cls(force=force, peer=peer, order=order)


@register_tl
class MessagesCreateForumTopic(TLRequest):
    ID: int = 0x2f98c3d5

    def __init__(self, title_missing: bool = False, icon_color: Any = None, icon_emoji_id: Any = None, send_as: Any = None, peer: Any = None, title: Any = None, random_id: Any = None) -> None:
        self.title_missing = title_missing
        self.icon_color = icon_color
        self.icon_emoji_id = icon_emoji_id
        self.send_as = send_as
        self.peer = peer
        self.title = title
        self.random_id = random_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.title_missing:
            flags |= (1 << 4)
        if self.icon_color is not None:
            flags |= (1 << 0)
        if self.icon_emoji_id is not None:
            flags |= (1 << 3)
        if self.send_as is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.title or '')
        if self.icon_color is not None:
            writer.write_int32(self.icon_color or 0)
        if self.icon_emoji_id is not None:
            writer.write_int64(self.icon_emoji_id or 0)
        writer.write_int64(self.random_id or 0)
        if self.send_as is not None:
            if self.send_as is not None and hasattr(self.send_as, 'write'): self.send_as.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCreateForumTopic':
        flags = reader.read_uint32()
        title_missing = bool(flags & (1 << 4))
        peer = reader.read_object()
        title = reader.read_string()
        icon_color = reader.read_int32() if (flags & (1 << 0)) else None
        icon_emoji_id = reader.read_int64() if (flags & (1 << 3)) else None
        random_id = reader.read_int64()
        send_as = reader.read_object() if (flags & (1 << 2)) else None
        return cls(title_missing=title_missing, peer=peer, title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id, random_id=random_id, send_as=send_as)


@register_tl
class MessagesDeleteTopicHistory(TLRequest):
    ID: int = 0xd2816f10

    def __init__(self, peer: Any = None, top_msg_id: Any = None) -> None:
        self.peer = peer
        self.top_msg_id = top_msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.top_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteTopicHistory':
        peer = reader.read_object()
        top_msg_id = reader.read_int32()
        return cls(peer=peer, top_msg_id=top_msg_id)


@register_tl
class MessagesGetEmojiGameInfo(TLRequest):
    ID: int = 0xfb7e8ca7

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetEmojiGameInfo':
        return cls()


@register_tl
class MessagesSummarizeText(TLRequest):
    ID: int = 0xabbbd346

    def __init__(self, to_lang: Any = None, tone: Any = None, peer: Any = None, id: Any = None) -> None:
        self.to_lang = to_lang
        self.tone = tone
        self.peer = peer
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.to_lang is not None:
            flags |= (1 << 0)
        if self.tone is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.id or 0)
        if self.to_lang is not None:
            writer.write_string(self.to_lang or '')
        if self.tone is not None:
            writer.write_string(self.tone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSummarizeText':
        flags = reader.read_uint32()
        peer = reader.read_object()
        id = reader.read_int32()
        to_lang = reader.read_string() if (flags & (1 << 0)) else None
        tone = reader.read_string() if (flags & (1 << 2)) else None
        return cls(peer=peer, id=id, to_lang=to_lang, tone=tone)


@register_tl
class MessagesEditChatCreator(TLRequest):
    ID: int = 0xf743b857

    def __init__(self, peer: Any = None, user_id: Any = None, password: Any = None) -> None:
        self.peer = peer
        self.user_id = user_id
        self.password = password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        if self.password is not None and hasattr(self.password, 'write'): self.password.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditChatCreator':
        peer = reader.read_object()
        user_id = reader.read_object()
        password = reader.read_object()
        return cls(peer=peer, user_id=user_id, password=password)


@register_tl
class MessagesGetFutureChatCreatorAfterLeave(TLRequest):
    ID: int = 0x3b7d0ea6

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetFutureChatCreatorAfterLeave':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class MessagesEditChatParticipantRank(TLRequest):
    ID: int = 0xa00f32b0

    def __init__(self, peer: Any = None, participant: Any = None, rank: Any = None) -> None:
        self.peer = peer
        self.participant = participant
        self.rank = rank

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)
        writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesEditChatParticipantRank':
        peer = reader.read_object()
        participant = reader.read_object()
        rank = reader.read_string()
        return cls(peer=peer, participant=participant, rank=rank)


@register_tl
class MessagesDeclineUrlAuth(TLRequest):
    ID: int = 0x35436bbc

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeclineUrlAuth':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class MessagesCheckUrlAuthMatchCode(TLRequest):
    ID: int = 0xc9a47b0b

    def __init__(self, url: Any = None, match_code: Any = None) -> None:
        self.url = url
        self.match_code = match_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_string(self.match_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesCheckUrlAuthMatchCode':
        url = reader.read_string()
        match_code = reader.read_string()
        return cls(url=url, match_code=match_code)


@register_tl
class MessagesComposeMessageWithAI(TLRequest):
    ID: int = 0xdaecc589

    def __init__(self, proofread: bool = False, emojify: bool = False, translate_to_lang: Any = None, tone: Any = None, text: Any = None) -> None:
        self.proofread = proofread
        self.emojify = emojify
        self.translate_to_lang = translate_to_lang
        self.tone = tone
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.proofread:
            flags |= (1 << 0)
        if self.emojify:
            flags |= (1 << 3)
        if self.translate_to_lang is not None:
            flags |= (1 << 1)
        if self.tone is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        if self.translate_to_lang is not None:
            writer.write_string(self.translate_to_lang or '')
        if self.tone is not None:
            if self.tone is not None and hasattr(self.tone, 'write'): self.tone.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesComposeMessageWithAI':
        flags = reader.read_uint32()
        proofread = bool(flags & (1 << 0))
        emojify = bool(flags & (1 << 3))
        text = reader.read_object()
        translate_to_lang = reader.read_string() if (flags & (1 << 1)) else None
        tone = reader.read_object() if (flags & (1 << 2)) else None
        return cls(proofread=proofread, emojify=emojify, text=text, translate_to_lang=translate_to_lang, tone=tone)


@register_tl
class MessagesReportReadMetrics(TLRequest):
    ID: int = 0x4067c5e6

    def __init__(self, peer: Any = None, metrics: Any = None) -> None:
        self.peer = peer
        self.metrics = metrics

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_vector(self.metrics or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReportReadMetrics':
        peer = reader.read_object()
        metrics = reader.read_vector(lambda r: reader.read_object())
        return cls(peer=peer, metrics=metrics)


@register_tl
class MessagesReportMusicListen(TLRequest):
    ID: int = 0xddbcd819

    def __init__(self, id: Any = None, listened_duration: Any = None) -> None:
        self.id = id
        self.listened_duration = listened_duration

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)
        writer.write_int32(self.listened_duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReportMusicListen':
        id = reader.read_object()
        listened_duration = reader.read_int32()
        return cls(id=id, listened_duration=listened_duration)


@register_tl
class MessagesAddPollAnswer(TLRequest):
    ID: int = 0x19bc4b6d

    def __init__(self, peer: Any = None, msg_id: Any = None, answer: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.answer = answer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        if self.answer is not None and hasattr(self.answer, 'write'): self.answer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesAddPollAnswer':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        answer = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, answer=answer)


@register_tl
class MessagesDeletePollAnswer(TLRequest):
    ID: int = 0xac8505a5

    def __init__(self, peer: Any = None, msg_id: Any = None, option: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.option = option

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        writer.write_bytes(self.option or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeletePollAnswer':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        option = reader.read_bytes()
        return cls(peer=peer, msg_id=msg_id, option=option)


@register_tl
class MessagesGetUnreadPollVotes(TLRequest):
    ID: int = 0x43286cf2

    def __init__(self, top_msg_id: Any = None, peer: Any = None, offset_id: Any = None, add_offset: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.peer = peer
        self.offset_id = offset_id
        self.add_offset = add_offset
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.add_offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetUnreadPollVotes':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        offset_id = reader.read_int32()
        add_offset = reader.read_int32()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        return cls(peer=peer, top_msg_id=top_msg_id, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id)


@register_tl
class MessagesReadPollVotes(TLRequest):
    ID: int = 0x1720b4d8

    def __init__(self, top_msg_id: Any = None, peer: Any = None) -> None:
        self.top_msg_id = top_msg_id
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.top_msg_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.top_msg_id is not None:
            writer.write_int32(self.top_msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesReadPollVotes':
        flags = reader.read_uint32()
        peer = reader.read_object()
        top_msg_id = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(peer=peer, top_msg_id=top_msg_id)


@register_tl
class MessagesSetBotGuestChatResult(TLRequest):
    ID: int = 0xb8f106e3

    def __init__(self, query_id: Any = None, result: Any = None) -> None:
        self.query_id = query_id
        self.result = result

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        if self.result is not None and hasattr(self.result, 'write'): self.result.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesSetBotGuestChatResult':
        query_id = reader.read_int64()
        result = reader.read_object()
        return cls(query_id=query_id, result=result)


@register_tl
class MessagesDeleteParticipantReactions(TLRequest):
    ID: int = 0xa0b80cf8

    def __init__(self, peer: Any = None, participant: Any = None) -> None:
        self.peer = peer
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteParticipantReactions':
        peer = reader.read_object()
        participant = reader.read_object()
        return cls(peer=peer, participant=participant)


@register_tl
class MessagesDeleteParticipantReaction(TLRequest):
    ID: int = 0xe3b7f82c

    def __init__(self, peer: Any = None, msg_id: Any = None, participant: Any = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_int32(self.msg_id or 0)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesDeleteParticipantReaction':
        peer = reader.read_object()
        msg_id = reader.read_int32()
        participant = reader.read_object()
        return cls(peer=peer, msg_id=msg_id, participant=participant)


@register_tl
class MessagesGetPersonalChannelHistory(TLRequest):
    ID: int = 0x55fb0996

    def __init__(self, user_id: Any = None, limit: Any = None, max_id: Any = None, min_id: Any = None, hash: Any = None) -> None:
        self.user_id = user_id
        self.limit = limit
        self.max_id = max_id
        self.min_id = min_id
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.limit or 0)
        writer.write_int32(self.max_id or 0)
        writer.write_int32(self.min_id or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'MessagesGetPersonalChannelHistory':
        user_id = reader.read_object()
        limit = reader.read_int32()
        max_id = reader.read_int32()
        min_id = reader.read_int32()
        hash = reader.read_int64()
        return cls(user_id=user_id, limit=limit, max_id=max_id, min_id=min_id, hash=hash)


@register_tl
class UpdatesGetState(TLRequest):
    ID: int = 0xedd4882a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesGetState':
        return cls()


@register_tl
class UpdatesGetDifference(TLRequest):
    ID: int = 0x19c2f763

    def __init__(self, pts_limit: Any = None, pts_total_limit: Any = None, qts_limit: Any = None, pts: Any = None, date: Any = None, qts: Any = None) -> None:
        self.pts_limit = pts_limit
        self.pts_total_limit = pts_total_limit
        self.qts_limit = qts_limit
        self.pts = pts
        self.date = date
        self.qts = qts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.pts_limit is not None:
            flags |= (1 << 1)
        if self.pts_total_limit is not None:
            flags |= (1 << 0)
        if self.qts_limit is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.pts or 0)
        if self.pts_limit is not None:
            writer.write_int32(self.pts_limit or 0)
        if self.pts_total_limit is not None:
            writer.write_int32(self.pts_total_limit or 0)
        writer.write_int32(self.date or 0)
        writer.write_int32(self.qts or 0)
        if self.qts_limit is not None:
            writer.write_int32(self.qts_limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesGetDifference':
        flags = reader.read_uint32()
        pts = reader.read_int32()
        pts_limit = reader.read_int32() if (flags & (1 << 1)) else None
        pts_total_limit = reader.read_int32() if (flags & (1 << 0)) else None
        date = reader.read_int32()
        qts = reader.read_int32()
        qts_limit = reader.read_int32() if (flags & (1 << 2)) else None
        return cls(pts=pts, pts_limit=pts_limit, pts_total_limit=pts_total_limit, date=date, qts=qts, qts_limit=qts_limit)


@register_tl
class UpdatesGetChannelDifference(TLRequest):
    ID: int = 0x3173d78

    def __init__(self, force: bool = False, channel: Any = None, filter: Any = None, pts: Any = None, limit: Any = None) -> None:
        self.force = force
        self.channel = channel
        self.filter = filter
        self.pts = pts
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.force:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.pts or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UpdatesGetChannelDifference':
        flags = reader.read_uint32()
        force = bool(flags & (1 << 0))
        channel = reader.read_object()
        filter = reader.read_object()
        pts = reader.read_int32()
        limit = reader.read_int32()
        return cls(force=force, channel=channel, filter=filter, pts=pts, limit=limit)


@register_tl
class PhotosUpdateProfilePhoto(TLRequest):
    ID: int = 0x9e82039

    def __init__(self, fallback: bool = False, bot: Any = None, id: Any = None) -> None:
        self.fallback = fallback
        self.bot = bot
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.fallback:
            flags |= (1 << 0)
        if self.bot is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.bot is not None:
            if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosUpdateProfilePhoto':
        flags = reader.read_uint32()
        fallback = bool(flags & (1 << 0))
        bot = reader.read_object() if (flags & (1 << 1)) else None
        id = reader.read_object()
        return cls(fallback=fallback, bot=bot, id=id)


@register_tl
class PhotosUploadProfilePhoto(TLRequest):
    ID: int = 0x388a3b5

    def __init__(self, fallback: bool = False, bot: Any = None, file: Any = None, video: Any = None, video_start_ts: Any = None, video_emoji_markup: Any = None) -> None:
        self.fallback = fallback
        self.bot = bot
        self.file = file
        self.video = video
        self.video_start_ts = video_start_ts
        self.video_emoji_markup = video_emoji_markup

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.fallback:
            flags |= (1 << 3)
        if self.bot is not None:
            flags |= (1 << 5)
        if self.file is not None:
            flags |= (1 << 0)
        if self.video is not None:
            flags |= (1 << 1)
        if self.video_start_ts is not None:
            flags |= (1 << 2)
        if self.video_emoji_markup is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        if self.bot is not None:
            if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        if self.file is not None:
            if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        if self.video is not None:
            if self.video is not None and hasattr(self.video, 'write'): self.video.write(writer)
        if self.video_start_ts is not None:
            writer.write_double(self.video_start_ts or 0.0)
        if self.video_emoji_markup is not None:
            if self.video_emoji_markup is not None and hasattr(self.video_emoji_markup, 'write'): self.video_emoji_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosUploadProfilePhoto':
        flags = reader.read_uint32()
        fallback = bool(flags & (1 << 3))
        bot = reader.read_object() if (flags & (1 << 5)) else None
        file = reader.read_object() if (flags & (1 << 0)) else None
        video = reader.read_object() if (flags & (1 << 1)) else None
        video_start_ts = reader.read_double() if (flags & (1 << 2)) else None
        video_emoji_markup = reader.read_object() if (flags & (1 << 4)) else None
        return cls(fallback=fallback, bot=bot, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)


@register_tl
class PhotosDeletePhotos(TLRequest):
    ID: int = 0x87cf7f2f

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosDeletePhotos':
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id)


@register_tl
class PhotosGetUserPhotos(TLRequest):
    ID: int = 0x91cd32a8

    def __init__(self, user_id: Any = None, offset: Any = None, max_id: Any = None, limit: Any = None) -> None:
        self.user_id = user_id
        self.offset = offset
        self.max_id = max_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_int32(self.offset or 0)
        writer.write_int64(self.max_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosGetUserPhotos':
        user_id = reader.read_object()
        offset = reader.read_int32()
        max_id = reader.read_int64()
        limit = reader.read_int32()
        return cls(user_id=user_id, offset=offset, max_id=max_id, limit=limit)


@register_tl
class PhotosUploadContactProfilePhoto(TLRequest):
    ID: int = 0xe14c4a71

    def __init__(self, suggest: bool = False, save: bool = False, file: Any = None, video: Any = None, video_start_ts: Any = None, video_emoji_markup: Any = None, user_id: Any = None) -> None:
        self.suggest = suggest
        self.save = save
        self.file = file
        self.video = video
        self.video_start_ts = video_start_ts
        self.video_emoji_markup = video_emoji_markup
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.suggest:
            flags |= (1 << 3)
        if self.save:
            flags |= (1 << 4)
        if self.file is not None:
            flags |= (1 << 0)
        if self.video is not None:
            flags |= (1 << 1)
        if self.video_start_ts is not None:
            flags |= (1 << 2)
        if self.video_emoji_markup is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        if self.file is not None:
            if self.file is not None and hasattr(self.file, 'write'): self.file.write(writer)
        if self.video is not None:
            if self.video is not None and hasattr(self.video, 'write'): self.video.write(writer)
        if self.video_start_ts is not None:
            writer.write_double(self.video_start_ts or 0.0)
        if self.video_emoji_markup is not None:
            if self.video_emoji_markup is not None and hasattr(self.video_emoji_markup, 'write'): self.video_emoji_markup.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhotosUploadContactProfilePhoto':
        flags = reader.read_uint32()
        suggest = bool(flags & (1 << 3))
        save = bool(flags & (1 << 4))
        user_id = reader.read_object()
        file = reader.read_object() if (flags & (1 << 0)) else None
        video = reader.read_object() if (flags & (1 << 1)) else None
        video_start_ts = reader.read_double() if (flags & (1 << 2)) else None
        video_emoji_markup = reader.read_object() if (flags & (1 << 5)) else None
        return cls(suggest=suggest, save=save, user_id=user_id, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)


@register_tl
class UploadSaveFilePart(TLRequest):
    ID: int = 0xb304a621

    def __init__(self, file_id: Any = None, file_part: Any = None, bytes: Any = None) -> None:
        self.file_id = file_id
        self.file_part = file_part
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.file_id or 0)
        writer.write_int32(self.file_part or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadSaveFilePart':
        file_id = reader.read_int64()
        file_part = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(file_id=file_id, file_part=file_part, bytes=bytes)


@register_tl
class UploadGetFile(TLRequest):
    ID: int = 0xbe5335be

    def __init__(self, precise: bool = False, cdn_supported: bool = False, location: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.precise = precise
        self.cdn_supported = cdn_supported
        self.location = location
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.precise:
            flags |= (1 << 0)
        if self.cdn_supported:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.location is not None and hasattr(self.location, 'write'): self.location.write(writer)
        writer.write_int64(self.offset or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadGetFile':
        flags = reader.read_uint32()
        precise = bool(flags & (1 << 0))
        cdn_supported = bool(flags & (1 << 1))
        location = reader.read_object()
        offset = reader.read_int64()
        limit = reader.read_int32()
        return cls(precise=precise, cdn_supported=cdn_supported, location=location, offset=offset, limit=limit)


@register_tl
class UploadSaveBigFilePart(TLRequest):
    ID: int = 0xde7b673d

    def __init__(self, file_id: Any = None, file_part: Any = None, file_total_parts: Any = None, bytes: Any = None) -> None:
        self.file_id = file_id
        self.file_part = file_part
        self.file_total_parts = file_total_parts
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.file_id or 0)
        writer.write_int32(self.file_part or 0)
        writer.write_int32(self.file_total_parts or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadSaveBigFilePart':
        file_id = reader.read_int64()
        file_part = reader.read_int32()
        file_total_parts = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(file_id=file_id, file_part=file_part, file_total_parts=file_total_parts, bytes=bytes)


@register_tl
class UploadGetWebFile(TLRequest):
    ID: int = 0x24e6818d

    def __init__(self, location: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.location = location
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.location is not None and hasattr(self.location, 'write'): self.location.write(writer)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadGetWebFile':
        location = reader.read_object()
        offset = reader.read_int32()
        limit = reader.read_int32()
        return cls(location=location, offset=offset, limit=limit)


@register_tl
class UploadGetCdnFile(TLRequest):
    ID: int = 0x395f69da

    def __init__(self, file_token: Any = None, offset: Any = None, limit: Any = None) -> None:
        self.file_token = file_token
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.file_token or b'')
        writer.write_int64(self.offset or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadGetCdnFile':
        file_token = reader.read_bytes()
        offset = reader.read_int64()
        limit = reader.read_int32()
        return cls(file_token=file_token, offset=offset, limit=limit)


@register_tl
class UploadReuploadCdnFile(TLRequest):
    ID: int = 0x9b2754a8

    def __init__(self, file_token: Any = None, request_token: Any = None) -> None:
        self.file_token = file_token
        self.request_token = request_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.file_token or b'')
        writer.write_bytes(self.request_token or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadReuploadCdnFile':
        file_token = reader.read_bytes()
        request_token = reader.read_bytes()
        return cls(file_token=file_token, request_token=request_token)


@register_tl
class UploadGetCdnFileHashes(TLRequest):
    ID: int = 0x91dc3f31

    def __init__(self, file_token: Any = None, offset: Any = None) -> None:
        self.file_token = file_token
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.file_token or b'')
        writer.write_int64(self.offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadGetCdnFileHashes':
        file_token = reader.read_bytes()
        offset = reader.read_int64()
        return cls(file_token=file_token, offset=offset)


@register_tl
class UploadGetFileHashes(TLRequest):
    ID: int = 0x9156982a

    def __init__(self, location: Any = None, offset: Any = None) -> None:
        self.location = location
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.location is not None and hasattr(self.location, 'write'): self.location.write(writer)
        writer.write_int64(self.offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadGetFileHashes':
        location = reader.read_object()
        offset = reader.read_int64()
        return cls(location=location, offset=offset)


@register_tl
class HelpGetConfig(TLRequest):
    ID: int = 0xc4f9186b

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetConfig':
        return cls()


@register_tl
class HelpGetNearestDc(TLRequest):
    ID: int = 0x1fb33026

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetNearestDc':
        return cls()


@register_tl
class HelpGetAppUpdate(TLRequest):
    ID: int = 0x522d5a7d

    def __init__(self, source: Any = None) -> None:
        self.source = source

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.source or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetAppUpdate':
        source = reader.read_string()
        return cls(source=source)


@register_tl
class HelpGetInviteText(TLRequest):
    ID: int = 0x4d392343

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetInviteText':
        return cls()


@register_tl
class HelpGetSupport(TLRequest):
    ID: int = 0x9cdf08cd

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetSupport':
        return cls()


@register_tl
class HelpSetBotUpdatesStatus(TLRequest):
    ID: int = 0xec22cfcd

    def __init__(self, pending_updates_count: Any = None, message: Any = None) -> None:
        self.pending_updates_count = pending_updates_count
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.pending_updates_count or 0)
        writer.write_string(self.message or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpSetBotUpdatesStatus':
        pending_updates_count = reader.read_int32()
        message = reader.read_string()
        return cls(pending_updates_count=pending_updates_count, message=message)


@register_tl
class HelpGetCdnConfig(TLRequest):
    ID: int = 0x52029342

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetCdnConfig':
        return cls()


@register_tl
class HelpGetRecentMeUrls(TLRequest):
    ID: int = 0x3dc0f114

    def __init__(self, referer: Any = None) -> None:
        self.referer = referer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.referer or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetRecentMeUrls':
        referer = reader.read_string()
        return cls(referer=referer)


@register_tl
class HelpGetTermsOfServiceUpdate(TLRequest):
    ID: int = 0x2ca51fd1

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetTermsOfServiceUpdate':
        return cls()


@register_tl
class HelpAcceptTermsOfService(TLRequest):
    ID: int = 0xee72f79a

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.id is not None and hasattr(self.id, 'write'): self.id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpAcceptTermsOfService':
        id = reader.read_object()
        return cls(id=id)


@register_tl
class HelpGetDeepLinkInfo(TLRequest):
    ID: int = 0x3fedc75f

    def __init__(self, path: Any = None) -> None:
        self.path = path

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.path or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetDeepLinkInfo':
        path = reader.read_string()
        return cls(path=path)


@register_tl
class HelpGetAppConfig(TLRequest):
    ID: int = 0x61e3f854

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetAppConfig':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class HelpSaveAppLog(TLRequest):
    ID: int = 0x6f02f748

    def __init__(self, events: Any = None) -> None:
        self.events = events

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.events or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpSaveAppLog':
        events = reader.read_vector(lambda r: reader.read_object())
        return cls(events=events)


@register_tl
class HelpGetPassportConfig(TLRequest):
    ID: int = 0xc661ad08

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetPassportConfig':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class HelpGetSupportName(TLRequest):
    ID: int = 0xd360e72c

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetSupportName':
        return cls()


@register_tl
class HelpGetUserInfo(TLRequest):
    ID: int = 0x38a08d3

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetUserInfo':
        user_id = reader.read_object()
        return cls(user_id=user_id)


@register_tl
class HelpEditUserInfo(TLRequest):
    ID: int = 0x66b91b70

    def __init__(self, user_id: Any = None, message: Any = None, entities: Any = None) -> None:
        self.user_id = user_id
        self.message = message
        self.entities = entities

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        writer.write_string(self.message or '')
        writer.write_vector(self.entities or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpEditUserInfo':
        user_id = reader.read_object()
        message = reader.read_string()
        entities = reader.read_vector(lambda r: reader.read_object())
        return cls(user_id=user_id, message=message, entities=entities)


@register_tl
class HelpGetPromoData(TLRequest):
    ID: int = 0xc0977421

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetPromoData':
        return cls()


@register_tl
class HelpHidePromoData(TLRequest):
    ID: int = 0x1e251c95

    def __init__(self, peer: Any = None) -> None:
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpHidePromoData':
        peer = reader.read_object()
        return cls(peer=peer)


@register_tl
class HelpDismissSuggestion(TLRequest):
    ID: int = 0xf50dbaa1

    def __init__(self, peer: Any = None, suggestion: Any = None) -> None:
        self.peer = peer
        self.suggestion = suggestion

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)
        writer.write_string(self.suggestion or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpDismissSuggestion':
        peer = reader.read_object()
        suggestion = reader.read_string()
        return cls(peer=peer, suggestion=suggestion)


@register_tl
class HelpGetCountriesList(TLRequest):
    ID: int = 0x735787a8

    def __init__(self, lang_code: Any = None, hash: Any = None) -> None:
        self.lang_code = lang_code
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetCountriesList':
        lang_code = reader.read_string()
        hash = reader.read_int32()
        return cls(lang_code=lang_code, hash=hash)


@register_tl
class HelpGetPremiumPromo(TLRequest):
    ID: int = 0xb81b93d4

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetPremiumPromo':
        return cls()


@register_tl
class HelpGetPeerColors(TLRequest):
    ID: int = 0xda80f42f

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetPeerColors':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class HelpGetPeerProfileColors(TLRequest):
    ID: int = 0xabcfa9fd

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetPeerProfileColors':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class HelpGetTimezonesList(TLRequest):
    ID: int = 0x49b30240

    def __init__(self, hash: Any = None) -> None:
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'HelpGetTimezonesList':
        hash = reader.read_int32()
        return cls(hash=hash)


@register_tl
class ChannelsReadHistory(TLRequest):
    ID: int = 0xcc104937

    def __init__(self, channel: Any = None, max_id: Any = None) -> None:
        self.channel = channel
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsReadHistory':
        channel = reader.read_object()
        max_id = reader.read_int32()
        return cls(channel=channel, max_id=max_id)


@register_tl
class ChannelsDeleteMessages(TLRequest):
    ID: int = 0x84c1fd4e

    def __init__(self, channel: Any = None, id: Any = None) -> None:
        self.channel = channel
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsDeleteMessages':
        channel = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(channel=channel, id=id)


@register_tl
class ChannelsReportSpam(TLRequest):
    ID: int = 0xf44a8315

    def __init__(self, channel: Any = None, participant: Any = None, id: Any = None) -> None:
        self.channel = channel
        self.participant = participant
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsReportSpam':
        channel = reader.read_object()
        participant = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(channel=channel, participant=participant, id=id)


@register_tl
class ChannelsGetMessages(TLRequest):
    ID: int = 0xad8c9a23

    def __init__(self, channel: Any = None, id: Any = None) -> None:
        self.channel = channel
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetMessages':
        channel = reader.read_object()
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(channel=channel, id=id)


@register_tl
class ChannelsGetParticipants(TLRequest):
    ID: int = 0x77ced9d0

    def __init__(self, channel: Any = None, filter: Any = None, offset: Any = None, limit: Any = None, hash: Any = None) -> None:
        self.channel = channel
        self.filter = filter
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.filter is not None and hasattr(self.filter, 'write'): self.filter.write(writer)
        writer.write_int32(self.offset or 0)
        writer.write_int32(self.limit or 0)
        writer.write_int64(self.hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetParticipants':
        channel = reader.read_object()
        filter = reader.read_object()
        offset = reader.read_int32()
        limit = reader.read_int32()
        hash = reader.read_int64()
        return cls(channel=channel, filter=filter, offset=offset, limit=limit, hash=hash)


@register_tl
class ChannelsGetParticipant(TLRequest):
    ID: int = 0xa0ab6cc6

    def __init__(self, channel: Any = None, participant: Any = None) -> None:
        self.channel = channel
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetParticipant':
        channel = reader.read_object()
        participant = reader.read_object()
        return cls(channel=channel, participant=participant)


@register_tl
class ChannelsGetChannels(TLRequest):
    ID: int = 0xa7f6bbb

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.id or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetChannels':
        id = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id)


@register_tl
class ChannelsGetFullChannel(TLRequest):
    ID: int = 0x8736a09

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetFullChannel':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class ChannelsCreateChannel(TLRequest):
    ID: int = 0x91006707

    def __init__(self, broadcast: bool = False, megagroup: bool = False, for_import: bool = False, forum: bool = False, geo_point: Any = None, address: Any = None, ttl_period: Any = None, title: Any = None, about: Any = None) -> None:
        self.broadcast = broadcast
        self.megagroup = megagroup
        self.for_import = for_import
        self.forum = forum
        self.geo_point = geo_point
        self.address = address
        self.ttl_period = ttl_period
        self.title = title
        self.about = about

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast:
            flags |= (1 << 0)
        if self.megagroup:
            flags |= (1 << 1)
        if self.for_import:
            flags |= (1 << 3)
        if self.forum:
            flags |= (1 << 5)
        if self.geo_point is not None:
            flags |= (1 << 2)
        if self.address is not None:
            flags |= (1 << 2)
        if self.ttl_period is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(self.title or '')
        writer.write_string(self.about or '')
        if self.geo_point is not None:
            if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        if self.address is not None:
            writer.write_string(self.address or '')
        if self.ttl_period is not None:
            writer.write_int32(self.ttl_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsCreateChannel':
        flags = reader.read_uint32()
        broadcast = bool(flags & (1 << 0))
        megagroup = bool(flags & (1 << 1))
        for_import = bool(flags & (1 << 3))
        forum = bool(flags & (1 << 5))
        title = reader.read_string()
        about = reader.read_string()
        geo_point = reader.read_object() if (flags & (1 << 2)) else None
        address = reader.read_string() if (flags & (1 << 2)) else None
        ttl_period = reader.read_int32() if (flags & (1 << 4)) else None
        return cls(broadcast=broadcast, megagroup=megagroup, for_import=for_import, forum=forum, title=title, about=about, geo_point=geo_point, address=address, ttl_period=ttl_period)


@register_tl
class ChannelsEditAdmin(TLRequest):
    ID: int = 0x9a98ad68

    def __init__(self, rank: Any = None, channel: Any = None, user_id: Any = None, admin_rights: Any = None) -> None:
        self.rank = rank
        self.channel = channel
        self.user_id = user_id
        self.admin_rights = admin_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.rank is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        if self.admin_rights is not None and hasattr(self.admin_rights, 'write'): self.admin_rights.write(writer)
        if self.rank is not None:
            writer.write_string(self.rank or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsEditAdmin':
        flags = reader.read_uint32()
        channel = reader.read_object()
        user_id = reader.read_object()
        admin_rights = reader.read_object()
        rank = reader.read_string() if (flags & (1 << 0)) else None
        return cls(channel=channel, user_id=user_id, admin_rights=admin_rights, rank=rank)


@register_tl
class ChannelsEditTitle(TLRequest):
    ID: int = 0x566decd0

    def __init__(self, channel: Any = None, title: Any = None) -> None:
        self.channel = channel
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsEditTitle':
        channel = reader.read_object()
        title = reader.read_string()
        return cls(channel=channel, title=title)


@register_tl
class ChannelsEditPhoto(TLRequest):
    ID: int = 0xf12e57c9

    def __init__(self, channel: Any = None, photo: Any = None) -> None:
        self.channel = channel
        self.photo = photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsEditPhoto':
        channel = reader.read_object()
        photo = reader.read_object()
        return cls(channel=channel, photo=photo)


@register_tl
class ChannelsCheckUsername(TLRequest):
    ID: int = 0x10e6bd2c

    def __init__(self, channel: Any = None, username: Any = None) -> None:
        self.channel = channel
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_string(self.username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsCheckUsername':
        channel = reader.read_object()
        username = reader.read_string()
        return cls(channel=channel, username=username)


@register_tl
class ChannelsUpdateUsername(TLRequest):
    ID: int = 0x3514b3de

    def __init__(self, channel: Any = None, username: Any = None) -> None:
        self.channel = channel
        self.username = username

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_string(self.username or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsUpdateUsername':
        channel = reader.read_object()
        username = reader.read_string()
        return cls(channel=channel, username=username)


@register_tl
class ChannelsJoinChannel(TLRequest):
    ID: int = 0x24b524c5

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsJoinChannel':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class ChannelsLeaveChannel(TLRequest):
    ID: int = 0xf836aa95

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsLeaveChannel':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class ChannelsInviteToChannel(TLRequest):
    ID: int = 0xc9e33d54

    def __init__(self, channel: Any = None, users: Any = None) -> None:
        self.channel = channel
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsInviteToChannel':
        channel = reader.read_object()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(channel=channel, users=users)


@register_tl
class ChannelsDeleteChannel(TLRequest):
    ID: int = 0xc0111fe3

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsDeleteChannel':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class ChannelsExportMessageLink(TLRequest):
    ID: int = 0xe63fadeb

    def __init__(self, grouped: bool = False, thread: bool = False, channel: Any = None, id: Any = None) -> None:
        self.grouped = grouped
        self.thread = thread
        self.channel = channel
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.grouped:
            flags |= (1 << 0)
        if self.thread:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsExportMessageLink':
        flags = reader.read_uint32()
        grouped = bool(flags & (1 << 0))
        thread = bool(flags & (1 << 1))
        channel = reader.read_object()
        id = reader.read_int32()
        return cls(grouped=grouped, thread=thread, channel=channel, id=id)


@register_tl
class ChannelsToggleSignatures(TLRequest):
    ID: int = 0x418d549c

    def __init__(self, signatures_enabled: bool = False, profiles_enabled: bool = False, channel: Any = None) -> None:
        self.signatures_enabled = signatures_enabled
        self.profiles_enabled = profiles_enabled
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.signatures_enabled:
            flags |= (1 << 0)
        if self.profiles_enabled:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleSignatures':
        flags = reader.read_uint32()
        signatures_enabled = bool(flags & (1 << 0))
        profiles_enabled = bool(flags & (1 << 1))
        channel = reader.read_object()
        return cls(signatures_enabled=signatures_enabled, profiles_enabled=profiles_enabled, channel=channel)


@register_tl
class ChannelsGetAdminedPublicChannels(TLRequest):
    ID: int = 0xf8b036af

    def __init__(self, by_location: bool = False, check_limit: bool = False, for_personal: bool = False) -> None:
        self.by_location = by_location
        self.check_limit = check_limit
        self.for_personal = for_personal

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.by_location:
            flags |= (1 << 0)
        if self.check_limit:
            flags |= (1 << 1)
        if self.for_personal:
            flags |= (1 << 2)
        writer.write_uint32(flags)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetAdminedPublicChannels':
        flags = reader.read_uint32()
        by_location = bool(flags & (1 << 0))
        check_limit = bool(flags & (1 << 1))
        for_personal = bool(flags & (1 << 2))
        return cls(by_location=by_location, check_limit=check_limit, for_personal=for_personal)


@register_tl
class ChannelsEditBanned(TLRequest):
    ID: int = 0x96e6cd81

    def __init__(self, channel: Any = None, participant: Any = None, banned_rights: Any = None) -> None:
        self.channel = channel
        self.participant = participant
        self.banned_rights = banned_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)
        if self.banned_rights is not None and hasattr(self.banned_rights, 'write'): self.banned_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsEditBanned':
        channel = reader.read_object()
        participant = reader.read_object()
        banned_rights = reader.read_object()
        return cls(channel=channel, participant=participant, banned_rights=banned_rights)


@register_tl
class ChannelsGetAdminLog(TLRequest):
    ID: int = 0x33ddf480

    def __init__(self, events_filter: Any = None, admins: Any = None, channel: Any = None, q: Any = None, max_id: Any = None, min_id: Any = None, limit: Any = None) -> None:
        self.events_filter = events_filter
        self.admins = admins
        self.channel = channel
        self.q = q
        self.max_id = max_id
        self.min_id = min_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.events_filter is not None:
            flags |= (1 << 0)
        if self.admins is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_string(self.q or '')
        if self.events_filter is not None:
            if self.events_filter is not None and hasattr(self.events_filter, 'write'): self.events_filter.write(writer)
        if self.admins is not None:
            writer.write_vector(self.admins or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int64(self.max_id or 0)
        writer.write_int64(self.min_id or 0)
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetAdminLog':
        flags = reader.read_uint32()
        channel = reader.read_object()
        q = reader.read_string()
        events_filter = reader.read_object() if (flags & (1 << 0)) else None
        admins = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        max_id = reader.read_int64()
        min_id = reader.read_int64()
        limit = reader.read_int32()
        return cls(channel=channel, q=q, events_filter=events_filter, admins=admins, max_id=max_id, min_id=min_id, limit=limit)


@register_tl
class ChannelsSetStickers(TLRequest):
    ID: int = 0xea8ca4f9

    def __init__(self, channel: Any = None, stickerset: Any = None) -> None:
        self.channel = channel
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSetStickers':
        channel = reader.read_object()
        stickerset = reader.read_object()
        return cls(channel=channel, stickerset=stickerset)


@register_tl
class ChannelsReadMessageContents(TLRequest):
    ID: int = 0xeab5dc38

    def __init__(self, channel: Any = None, id: Any = None) -> None:
        self.channel = channel
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_vector(self.id or [], lambda w, x: w.write_int32(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsReadMessageContents':
        channel = reader.read_object()
        id = reader.read_vector(lambda r: r.read_int32())
        return cls(channel=channel, id=id)


@register_tl
class ChannelsDeleteHistory(TLRequest):
    ID: int = 0x9baa9647

    def __init__(self, for_everyone: bool = False, channel: Any = None, max_id: Any = None) -> None:
        self.for_everyone = for_everyone
        self.channel = channel
        self.max_id = max_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.for_everyone:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.max_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsDeleteHistory':
        flags = reader.read_uint32()
        for_everyone = bool(flags & (1 << 0))
        channel = reader.read_object()
        max_id = reader.read_int32()
        return cls(for_everyone=for_everyone, channel=channel, max_id=max_id)


@register_tl
class ChannelsTogglePreHistoryHidden(TLRequest):
    ID: int = 0xeabbb94c

    def __init__(self, channel: Any = None, enabled: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsTogglePreHistoryHidden':
        channel = reader.read_object()
        enabled = reader.read_bool()
        return cls(channel=channel, enabled=enabled)


@register_tl
class ChannelsGetLeftChannels(TLRequest):
    ID: int = 0x8341ecc0

    def __init__(self, offset: Any = None) -> None:
        self.offset = offset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.offset or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetLeftChannels':
        offset = reader.read_int32()
        return cls(offset=offset)


@register_tl
class ChannelsGetGroupsForDiscussion(TLRequest):
    ID: int = 0xf5dad378

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetGroupsForDiscussion':
        return cls()


@register_tl
class ChannelsSetDiscussionGroup(TLRequest):
    ID: int = 0x40582bb2

    def __init__(self, broadcast: Any = None, group: Any = None) -> None:
        self.broadcast = broadcast
        self.group = group

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.broadcast is not None and hasattr(self.broadcast, 'write'): self.broadcast.write(writer)
        if self.group is not None and hasattr(self.group, 'write'): self.group.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSetDiscussionGroup':
        broadcast = reader.read_object()
        group = reader.read_object()
        return cls(broadcast=broadcast, group=group)


@register_tl
class ChannelsEditLocation(TLRequest):
    ID: int = 0x58e63f6d

    def __init__(self, channel: Any = None, geo_point: Any = None, address: Any = None) -> None:
        self.channel = channel
        self.geo_point = geo_point
        self.address = address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        writer.write_string(self.address or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsEditLocation':
        channel = reader.read_object()
        geo_point = reader.read_object()
        address = reader.read_string()
        return cls(channel=channel, geo_point=geo_point, address=address)


@register_tl
class ChannelsToggleSlowMode(TLRequest):
    ID: int = 0xedd49ef0

    def __init__(self, channel: Any = None, seconds: Any = None) -> None:
        self.channel = channel
        self.seconds = seconds

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.seconds or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleSlowMode':
        channel = reader.read_object()
        seconds = reader.read_int32()
        return cls(channel=channel, seconds=seconds)


@register_tl
class ChannelsGetInactiveChannels(TLRequest):
    ID: int = 0x11e831ee

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetInactiveChannels':
        return cls()


@register_tl
class ChannelsConvertToGigagroup(TLRequest):
    ID: int = 0xb290c69

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsConvertToGigagroup':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class ChannelsGetSendAs(TLRequest):
    ID: int = 0xe785a43f

    def __init__(self, for_paid_reactions: bool = False, for_live_stories: bool = False, peer: Any = None) -> None:
        self.for_paid_reactions = for_paid_reactions
        self.for_live_stories = for_live_stories
        self.peer = peer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.for_paid_reactions:
            flags |= (1 << 0)
        if self.for_live_stories:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.peer is not None and hasattr(self.peer, 'write'): self.peer.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetSendAs':
        flags = reader.read_uint32()
        for_paid_reactions = bool(flags & (1 << 0))
        for_live_stories = bool(flags & (1 << 1))
        peer = reader.read_object()
        return cls(for_paid_reactions=for_paid_reactions, for_live_stories=for_live_stories, peer=peer)


@register_tl
class ChannelsDeleteParticipantHistory(TLRequest):
    ID: int = 0x367544db

    def __init__(self, channel: Any = None, participant: Any = None) -> None:
        self.channel = channel
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsDeleteParticipantHistory':
        channel = reader.read_object()
        participant = reader.read_object()
        return cls(channel=channel, participant=participant)


@register_tl
class ChannelsToggleJoinToSend(TLRequest):
    ID: int = 0xe4cb9580

    def __init__(self, channel: Any = None, enabled: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleJoinToSend':
        channel = reader.read_object()
        enabled = reader.read_bool()
        return cls(channel=channel, enabled=enabled)


@register_tl
class ChannelsToggleJoinRequest(TLRequest):
    ID: int = 0x4c2985b6

    def __init__(self, channel: Any = None, enabled: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleJoinRequest':
        channel = reader.read_object()
        enabled = reader.read_bool()
        return cls(channel=channel, enabled=enabled)


@register_tl
class ChannelsReorderUsernames(TLRequest):
    ID: int = 0xb45ced1d

    def __init__(self, channel: Any = None, order: Any = None) -> None:
        self.channel = channel
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_vector(self.order or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsReorderUsernames':
        channel = reader.read_object()
        order = reader.read_vector(lambda r: r.read_string())
        return cls(channel=channel, order=order)


@register_tl
class ChannelsToggleUsername(TLRequest):
    ID: int = 0x50f24105

    def __init__(self, channel: Any = None, username: Any = None, active: Any = None) -> None:
        self.channel = channel
        self.username = username
        self.active = active

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_string(self.username or '')
        writer.write_bool(bool(self.active))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleUsername':
        channel = reader.read_object()
        username = reader.read_string()
        active = reader.read_bool()
        return cls(channel=channel, username=username, active=active)


@register_tl
class ChannelsDeactivateAllUsernames(TLRequest):
    ID: int = 0xa245dd3

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsDeactivateAllUsernames':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class ChannelsToggleForum(TLRequest):
    ID: int = 0x3ff75734

    def __init__(self, channel: Any = None, enabled: Any = None, tabs: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled
        self.tabs = tabs

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))
        writer.write_bool(bool(self.tabs))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleForum':
        channel = reader.read_object()
        enabled = reader.read_bool()
        tabs = reader.read_bool()
        return cls(channel=channel, enabled=enabled, tabs=tabs)


@register_tl
class ChannelsToggleAntiSpam(TLRequest):
    ID: int = 0x68f3e4eb

    def __init__(self, channel: Any = None, enabled: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleAntiSpam':
        channel = reader.read_object()
        enabled = reader.read_bool()
        return cls(channel=channel, enabled=enabled)


@register_tl
class ChannelsReportAntiSpamFalsePositive(TLRequest):
    ID: int = 0xa850a693

    def __init__(self, channel: Any = None, msg_id: Any = None) -> None:
        self.channel = channel
        self.msg_id = msg_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.msg_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsReportAntiSpamFalsePositive':
        channel = reader.read_object()
        msg_id = reader.read_int32()
        return cls(channel=channel, msg_id=msg_id)


@register_tl
class ChannelsToggleParticipantsHidden(TLRequest):
    ID: int = 0x6a6e7854

    def __init__(self, channel: Any = None, enabled: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleParticipantsHidden':
        channel = reader.read_object()
        enabled = reader.read_bool()
        return cls(channel=channel, enabled=enabled)


@register_tl
class ChannelsUpdateColor(TLRequest):
    ID: int = 0xd8aa3671

    def __init__(self, for_profile: bool = False, color: Any = None, background_emoji_id: Any = None, channel: Any = None) -> None:
        self.for_profile = for_profile
        self.color = color
        self.background_emoji_id = background_emoji_id
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.for_profile:
            flags |= (1 << 1)
        if self.color is not None:
            flags |= (1 << 2)
        if self.background_emoji_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.color is not None:
            writer.write_int32(self.color or 0)
        if self.background_emoji_id is not None:
            writer.write_int64(self.background_emoji_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsUpdateColor':
        flags = reader.read_uint32()
        for_profile = bool(flags & (1 << 1))
        channel = reader.read_object()
        color = reader.read_int32() if (flags & (1 << 2)) else None
        background_emoji_id = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(for_profile=for_profile, channel=channel, color=color, background_emoji_id=background_emoji_id)


@register_tl
class ChannelsToggleViewForumAsMessages(TLRequest):
    ID: int = 0x9738bb15

    def __init__(self, channel: Any = None, enabled: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleViewForumAsMessages':
        channel = reader.read_object()
        enabled = reader.read_bool()
        return cls(channel=channel, enabled=enabled)


@register_tl
class ChannelsGetChannelRecommendations(TLRequest):
    ID: int = 0x25a71742

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.channel is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None:
            if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetChannelRecommendations':
        flags = reader.read_uint32()
        channel = reader.read_object() if (flags & (1 << 0)) else None
        return cls(channel=channel)


@register_tl
class ChannelsUpdateEmojiStatus(TLRequest):
    ID: int = 0xf0d3e6a8

    def __init__(self, channel: Any = None, emoji_status: Any = None) -> None:
        self.channel = channel
        self.emoji_status = emoji_status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.emoji_status is not None and hasattr(self.emoji_status, 'write'): self.emoji_status.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsUpdateEmojiStatus':
        channel = reader.read_object()
        emoji_status = reader.read_object()
        return cls(channel=channel, emoji_status=emoji_status)


@register_tl
class ChannelsSetBoostsToUnblockRestrictions(TLRequest):
    ID: int = 0xad399cee

    def __init__(self, channel: Any = None, boosts: Any = None) -> None:
        self.channel = channel
        self.boosts = boosts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.boosts or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSetBoostsToUnblockRestrictions':
        channel = reader.read_object()
        boosts = reader.read_int32()
        return cls(channel=channel, boosts=boosts)


@register_tl
class ChannelsSetEmojiStickers(TLRequest):
    ID: int = 0x3cd930b7

    def __init__(self, channel: Any = None, stickerset: Any = None) -> None:
        self.channel = channel
        self.stickerset = stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.stickerset is not None and hasattr(self.stickerset, 'write'): self.stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSetEmojiStickers':
        channel = reader.read_object()
        stickerset = reader.read_object()
        return cls(channel=channel, stickerset=stickerset)


@register_tl
class ChannelsRestrictSponsoredMessages(TLRequest):
    ID: int = 0x9ae91519

    def __init__(self, channel: Any = None, restricted: Any = None) -> None:
        self.channel = channel
        self.restricted = restricted

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.restricted))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsRestrictSponsoredMessages':
        channel = reader.read_object()
        restricted = reader.read_bool()
        return cls(channel=channel, restricted=restricted)


@register_tl
class ChannelsSearchPosts(TLRequest):
    ID: int = 0xf2c4f24d

    def __init__(self, hashtag: Any = None, query: Any = None, allow_paid_stars: Any = None, offset_rate: Any = None, offset_peer: Any = None, offset_id: Any = None, limit: Any = None) -> None:
        self.hashtag = hashtag
        self.query = query
        self.allow_paid_stars = allow_paid_stars
        self.offset_rate = offset_rate
        self.offset_peer = offset_peer
        self.offset_id = offset_id
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.hashtag is not None:
            flags |= (1 << 0)
        if self.query is not None:
            flags |= (1 << 1)
        if self.allow_paid_stars is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        if self.hashtag is not None:
            writer.write_string(self.hashtag or '')
        if self.query is not None:
            writer.write_string(self.query or '')
        writer.write_int32(self.offset_rate or 0)
        if self.offset_peer is not None and hasattr(self.offset_peer, 'write'): self.offset_peer.write(writer)
        writer.write_int32(self.offset_id or 0)
        writer.write_int32(self.limit or 0)
        if self.allow_paid_stars is not None:
            writer.write_int64(self.allow_paid_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSearchPosts':
        flags = reader.read_uint32()
        hashtag = reader.read_string() if (flags & (1 << 0)) else None
        query = reader.read_string() if (flags & (1 << 1)) else None
        offset_rate = reader.read_int32()
        offset_peer = reader.read_object()
        offset_id = reader.read_int32()
        limit = reader.read_int32()
        allow_paid_stars = reader.read_int64() if (flags & (1 << 2)) else None
        return cls(hashtag=hashtag, query=query, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit, allow_paid_stars=allow_paid_stars)


@register_tl
class ChannelsUpdatePaidMessagesPrice(TLRequest):
    ID: int = 0x4b12327b

    def __init__(self, broadcast_messages_allowed: bool = False, channel: Any = None, send_paid_messages_stars: Any = None) -> None:
        self.broadcast_messages_allowed = broadcast_messages_allowed
        self.channel = channel
        self.send_paid_messages_stars = send_paid_messages_stars

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.broadcast_messages_allowed:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int64(self.send_paid_messages_stars or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsUpdatePaidMessagesPrice':
        flags = reader.read_uint32()
        broadcast_messages_allowed = bool(flags & (1 << 0))
        channel = reader.read_object()
        send_paid_messages_stars = reader.read_int64()
        return cls(broadcast_messages_allowed=broadcast_messages_allowed, channel=channel, send_paid_messages_stars=send_paid_messages_stars)


@register_tl
class ChannelsToggleAutotranslation(TLRequest):
    ID: int = 0x167fc0a1

    def __init__(self, channel: Any = None, enabled: Any = None) -> None:
        self.channel = channel
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsToggleAutotranslation':
        channel = reader.read_object()
        enabled = reader.read_bool()
        return cls(channel=channel, enabled=enabled)


@register_tl
class ChannelsGetMessageAuthor(TLRequest):
    ID: int = 0xece2a0e6

    def __init__(self, channel: Any = None, id: Any = None) -> None:
        self.channel = channel
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        writer.write_int32(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsGetMessageAuthor':
        channel = reader.read_object()
        id = reader.read_int32()
        return cls(channel=channel, id=id)


@register_tl
class ChannelsCheckSearchPostsFlood(TLRequest):
    ID: int = 0x22567115

    def __init__(self, query: Any = None) -> None:
        self.query = query

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.query is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.query is not None:
            writer.write_string(self.query or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsCheckSearchPostsFlood':
        flags = reader.read_uint32()
        query = reader.read_string() if (flags & (1 << 0)) else None
        return cls(query=query)


@register_tl
class ChannelsSetMainProfileTab(TLRequest):
    ID: int = 0x3583fcb1

    def __init__(self, channel: Any = None, tab: Any = None) -> None:
        self.channel = channel
        self.tab = tab

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)
        if self.tab is not None and hasattr(self.tab, 'write'): self.tab.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelsSetMainProfileTab':
        channel = reader.read_object()
        tab = reader.read_object()
        return cls(channel=channel, tab=tab)


@register_tl
class BotsSendCustomRequest(TLRequest):
    ID: int = 0xaa2769ed

    def __init__(self, custom_method: Any = None, params: Any = None) -> None:
        self.custom_method = custom_method
        self.params = params

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.custom_method or '')
        if self.params is not None and hasattr(self.params, 'write'): self.params.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsSendCustomRequest':
        custom_method = reader.read_string()
        params = reader.read_object()
        return cls(custom_method=custom_method, params=params)


@register_tl
class BotsAnswerWebhookJSONQuery(TLRequest):
    ID: int = 0xe6213f4d

    def __init__(self, query_id: Any = None, data: Any = None) -> None:
        self.query_id = query_id
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.query_id or 0)
        if self.data is not None and hasattr(self.data, 'write'): self.data.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsAnswerWebhookJSONQuery':
        query_id = reader.read_int64()
        data = reader.read_object()
        return cls(query_id=query_id, data=data)


@register_tl
class BotsSetBotCommands(TLRequest):
    ID: int = 0x517165a

    def __init__(self, scope: Any = None, lang_code: Any = None, commands: Any = None) -> None:
        self.scope = scope
        self.lang_code = lang_code
        self.commands = commands

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.scope is not None and hasattr(self.scope, 'write'): self.scope.write(writer)
        writer.write_string(self.lang_code or '')
        writer.write_vector(self.commands or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsSetBotCommands':
        scope = reader.read_object()
        lang_code = reader.read_string()
        commands = reader.read_vector(lambda r: reader.read_object())
        return cls(scope=scope, lang_code=lang_code, commands=commands)


@register_tl
class BotsResetBotCommands(TLRequest):
    ID: int = 0x3d8de0f9

    def __init__(self, scope: Any = None, lang_code: Any = None) -> None:
        self.scope = scope
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.scope is not None and hasattr(self.scope, 'write'): self.scope.write(writer)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsResetBotCommands':
        scope = reader.read_object()
        lang_code = reader.read_string()
        return cls(scope=scope, lang_code=lang_code)


@register_tl
class BotsGetBotCommands(TLRequest):
    ID: int = 0xe34c0dd6

    def __init__(self, scope: Any = None, lang_code: Any = None) -> None:
        self.scope = scope
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.scope is not None and hasattr(self.scope, 'write'): self.scope.write(writer)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetBotCommands':
        scope = reader.read_object()
        lang_code = reader.read_string()
        return cls(scope=scope, lang_code=lang_code)


@register_tl
class BotsSetBotMenuButton(TLRequest):
    ID: int = 0x4504d54f

    def __init__(self, user_id: Any = None, button: Any = None) -> None:
        self.user_id = user_id
        self.button = button

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        if self.button is not None and hasattr(self.button, 'write'): self.button.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsSetBotMenuButton':
        user_id = reader.read_object()
        button = reader.read_object()
        return cls(user_id=user_id, button=button)


@register_tl
class BotsGetBotMenuButton(TLRequest):
    ID: int = 0x9c60eb28

    def __init__(self, user_id: Any = None) -> None:
        self.user_id = user_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetBotMenuButton':
        user_id = reader.read_object()
        return cls(user_id=user_id)


@register_tl
class BotsSetBotBroadcastDefaultAdminRights(TLRequest):
    ID: int = 0x788464e1

    def __init__(self, admin_rights: Any = None) -> None:
        self.admin_rights = admin_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.admin_rights is not None and hasattr(self.admin_rights, 'write'): self.admin_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsSetBotBroadcastDefaultAdminRights':
        admin_rights = reader.read_object()
        return cls(admin_rights=admin_rights)


@register_tl
class BotsSetBotGroupDefaultAdminRights(TLRequest):
    ID: int = 0x925ec9ea

    def __init__(self, admin_rights: Any = None) -> None:
        self.admin_rights = admin_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.admin_rights is not None and hasattr(self.admin_rights, 'write'): self.admin_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsSetBotGroupDefaultAdminRights':
        admin_rights = reader.read_object()
        return cls(admin_rights=admin_rights)


@register_tl
class BotsSetBotInfo(TLRequest):
    ID: int = 0x10cf3123

    def __init__(self, bot: Any = None, name: Any = None, about: Any = None, description: Any = None, lang_code: Any = None) -> None:
        self.bot = bot
        self.name = name
        self.about = about
        self.description = description
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.bot is not None:
            flags |= (1 << 2)
        if self.name is not None:
            flags |= (1 << 3)
        if self.about is not None:
            flags |= (1 << 0)
        if self.description is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.bot is not None:
            if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.lang_code or '')
        if self.name is not None:
            writer.write_string(self.name or '')
        if self.about is not None:
            writer.write_string(self.about or '')
        if self.description is not None:
            writer.write_string(self.description or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsSetBotInfo':
        flags = reader.read_uint32()
        bot = reader.read_object() if (flags & (1 << 2)) else None
        lang_code = reader.read_string()
        name = reader.read_string() if (flags & (1 << 3)) else None
        about = reader.read_string() if (flags & (1 << 0)) else None
        description = reader.read_string() if (flags & (1 << 1)) else None
        return cls(bot=bot, lang_code=lang_code, name=name, about=about, description=description)


@register_tl
class BotsGetBotInfo(TLRequest):
    ID: int = 0xdcd914fd

    def __init__(self, bot: Any = None, lang_code: Any = None) -> None:
        self.bot = bot
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.bot is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.bot is not None:
            if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetBotInfo':
        flags = reader.read_uint32()
        bot = reader.read_object() if (flags & (1 << 0)) else None
        lang_code = reader.read_string()
        return cls(bot=bot, lang_code=lang_code)


@register_tl
class BotsReorderUsernames(TLRequest):
    ID: int = 0x9709b1c2

    def __init__(self, bot: Any = None, order: Any = None) -> None:
        self.bot = bot
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_vector(self.order or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsReorderUsernames':
        bot = reader.read_object()
        order = reader.read_vector(lambda r: r.read_string())
        return cls(bot=bot, order=order)


@register_tl
class BotsToggleUsername(TLRequest):
    ID: int = 0x53ca973

    def __init__(self, bot: Any = None, username: Any = None, active: Any = None) -> None:
        self.bot = bot
        self.username = username
        self.active = active

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.username or '')
        writer.write_bool(bool(self.active))

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsToggleUsername':
        bot = reader.read_object()
        username = reader.read_string()
        active = reader.read_bool()
        return cls(bot=bot, username=username, active=active)


@register_tl
class BotsCanSendMessage(TLRequest):
    ID: int = 0x1359f4e6

    def __init__(self, bot: Any = None) -> None:
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsCanSendMessage':
        bot = reader.read_object()
        return cls(bot=bot)


@register_tl
class BotsAllowSendMessage(TLRequest):
    ID: int = 0xf132e3ef

    def __init__(self, bot: Any = None) -> None:
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsAllowSendMessage':
        bot = reader.read_object()
        return cls(bot=bot)


@register_tl
class BotsInvokeWebViewCustomMethod(TLRequest):
    ID: int = 0x87fc5e7

    def __init__(self, bot: Any = None, custom_method: Any = None, params: Any = None) -> None:
        self.bot = bot
        self.custom_method = custom_method
        self.params = params

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.custom_method or '')
        if self.params is not None and hasattr(self.params, 'write'): self.params.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsInvokeWebViewCustomMethod':
        bot = reader.read_object()
        custom_method = reader.read_string()
        params = reader.read_object()
        return cls(bot=bot, custom_method=custom_method, params=params)


@register_tl
class BotsGetPopularAppBots(TLRequest):
    ID: int = 0xc2510192

    def __init__(self, offset: Any = None, limit: Any = None) -> None:
        self.offset = offset
        self.limit = limit

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.offset or '')
        writer.write_int32(self.limit or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetPopularAppBots':
        offset = reader.read_string()
        limit = reader.read_int32()
        return cls(offset=offset, limit=limit)


@register_tl
class BotsAddPreviewMedia(TLRequest):
    ID: int = 0x17aeb75a

    def __init__(self, bot: Any = None, lang_code: Any = None, media: Any = None) -> None:
        self.bot = bot
        self.lang_code = lang_code
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.lang_code or '')
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsAddPreviewMedia':
        bot = reader.read_object()
        lang_code = reader.read_string()
        media = reader.read_object()
        return cls(bot=bot, lang_code=lang_code, media=media)


@register_tl
class BotsEditPreviewMedia(TLRequest):
    ID: int = 0x8525606f

    def __init__(self, bot: Any = None, lang_code: Any = None, media: Any = None, new_media: Any = None) -> None:
        self.bot = bot
        self.lang_code = lang_code
        self.media = media
        self.new_media = new_media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.lang_code or '')
        if self.media is not None and hasattr(self.media, 'write'): self.media.write(writer)
        if self.new_media is not None and hasattr(self.new_media, 'write'): self.new_media.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsEditPreviewMedia':
        bot = reader.read_object()
        lang_code = reader.read_string()
        media = reader.read_object()
        new_media = reader.read_object()
        return cls(bot=bot, lang_code=lang_code, media=media, new_media=new_media)


@register_tl
class BotsDeletePreviewMedia(TLRequest):
    ID: int = 0x2d0135b3

    def __init__(self, bot: Any = None, lang_code: Any = None, media: Any = None) -> None:
        self.bot = bot
        self.lang_code = lang_code
        self.media = media

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.lang_code or '')
        writer.write_vector(self.media or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsDeletePreviewMedia':
        bot = reader.read_object()
        lang_code = reader.read_string()
        media = reader.read_vector(lambda r: reader.read_object())
        return cls(bot=bot, lang_code=lang_code, media=media)


@register_tl
class BotsReorderPreviewMedias(TLRequest):
    ID: int = 0xb627f3aa

    def __init__(self, bot: Any = None, lang_code: Any = None, order: Any = None) -> None:
        self.bot = bot
        self.lang_code = lang_code
        self.order = order

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.lang_code or '')
        writer.write_vector(self.order or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsReorderPreviewMedias':
        bot = reader.read_object()
        lang_code = reader.read_string()
        order = reader.read_vector(lambda r: reader.read_object())
        return cls(bot=bot, lang_code=lang_code, order=order)


@register_tl
class BotsGetPreviewInfo(TLRequest):
    ID: int = 0x423ab3ad

    def __init__(self, bot: Any = None, lang_code: Any = None) -> None:
        self.bot = bot
        self.lang_code = lang_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.lang_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetPreviewInfo':
        bot = reader.read_object()
        lang_code = reader.read_string()
        return cls(bot=bot, lang_code=lang_code)


@register_tl
class BotsGetPreviewMedias(TLRequest):
    ID: int = 0xa2a5594d

    def __init__(self, bot: Any = None) -> None:
        self.bot = bot

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsGetPreviewMedias':
        bot = reader.read_object()
        return cls(bot=bot)


@register_tl
class BotsUpdateUserEmojiStatus(TLRequest):
    ID: int = 0xed9f30c5

    def __init__(self, user_id: Any = None, emoji_status: Any = None) -> None:
        self.user_id = user_id
        self.emoji_status = emoji_status

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.user_id is not None and hasattr(self.user_id, 'write'): self.user_id.write(writer)
        if self.emoji_status is not None and hasattr(self.emoji_status, 'write'): self.emoji_status.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsUpdateUserEmojiStatus':
        user_id = reader.read_object()
        emoji_status = reader.read_object()
        return cls(user_id=user_id, emoji_status=emoji_status)


@register_tl
class BotsToggleUserEmojiStatusPermission(TLRequest):
    ID: int = 0x6de6392

    def __init__(self, bot: Any = None, enabled: Any = None) -> None:
        self.bot = bot
        self.enabled = enabled

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_bool(bool(self.enabled))

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsToggleUserEmojiStatusPermission':
        bot = reader.read_object()
        enabled = reader.read_bool()
        return cls(bot=bot, enabled=enabled)


@register_tl
class BotsCheckDownloadFileParams(TLRequest):
    ID: int = 0x50077589

    def __init__(self, bot: Any = None, file_name: Any = None, url: Any = None) -> None:
        self.bot = bot
        self.file_name = file_name
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.bot is not None and hasattr(self.bot, 'write'): self.bot.write(writer)
        writer.write_string(self.file_name or '')
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'BotsCheckDownloadFileParams':
        bot = reader.read_object()
        file_name = reader.read_string()
        url = reader.read_string()
        return cls(bot=bot, file_name=file_name, url=url)

