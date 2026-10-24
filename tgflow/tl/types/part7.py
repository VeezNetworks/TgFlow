from typing import Any
from ..core import TLObject, TLRequest, TLWriter, TLReader, register_tl

@register_tl
class TextItalic(TLObject):
    ID: int = 0xd912a59c

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextItalic':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class TextUnderline(TLObject):
    ID: int = 0xc12622c4

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextUnderline':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class TextStrike(TLObject):
    ID: int = 0x9bf8bb95

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextStrike':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class TextFixed(TLObject):
    ID: int = 0x6c3f19b9

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextFixed':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class TextUrl(TLObject):
    ID: int = 0x3c2884c1

    def __init__(self, text: Any = None, url: Any = None, webpage_id: Any = None) -> None:
        self.text = text
        self.url = url
        self.webpage_id = webpage_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        writer.write_string(self.url or '')
        writer.write_int64(self.webpage_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextUrl':
        text = reader.read_object()
        url = reader.read_string()
        webpage_id = reader.read_int64()
        return cls(text=text, url=url, webpage_id=webpage_id)


@register_tl
class TextEmail(TLObject):
    ID: int = 0xde5a0dd6

    def __init__(self, text: Any = None, email: Any = None) -> None:
        self.text = text
        self.email = email

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        writer.write_string(self.email or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'TextEmail':
        text = reader.read_object()
        email = reader.read_string()
        return cls(text=text, email=email)


@register_tl
class TextConcat(TLObject):
    ID: int = 0x7e6260d7

    def __init__(self, texts: Any = None) -> None:
        self.texts = texts

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.texts or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextConcat':
        texts = reader.read_vector(lambda r: reader.read_object())
        return cls(texts=texts)


@register_tl
class TextSubscript(TLObject):
    ID: int = 0xed6a8504

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextSubscript':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class TextSuperscript(TLObject):
    ID: int = 0xc7fb5e01

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextSuperscript':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class TextMarked(TLObject):
    ID: int = 0x34b8621

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextMarked':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class TextPhone(TLObject):
    ID: int = 0x1ccb966a

    def __init__(self, text: Any = None, phone: Any = None) -> None:
        self.text = text
        self.phone = phone

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        writer.write_string(self.phone or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'TextPhone':
        text = reader.read_object()
        phone = reader.read_string()
        return cls(text=text, phone=phone)


@register_tl
class TextImage(TLObject):
    ID: int = 0x81ccf4f

    def __init__(self, document_id: Any = None, w: Any = None, h: Any = None) -> None:
        self.document_id = document_id
        self.w = w
        self.h = h

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.document_id or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'TextImage':
        document_id = reader.read_int64()
        w = reader.read_int32()
        h = reader.read_int32()
        return cls(document_id=document_id, w=w, h=h)


@register_tl
class TextAnchor(TLObject):
    ID: int = 0x35553762

    def __init__(self, text: Any = None, name: Any = None) -> None:
        self.text = text
        self.name = name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        writer.write_string(self.name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'TextAnchor':
        text = reader.read_object()
        name = reader.read_string()
        return cls(text=text, name=name)


@register_tl
class PageBlockUnsupported(TLObject):
    ID: int = 0x13567e8a

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockUnsupported':
        return cls()


@register_tl
class PageBlockTitle(TLObject):
    ID: int = 0x70abc3fd

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockTitle':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageBlockSubtitle(TLObject):
    ID: int = 0x8ffa9a1f

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockSubtitle':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageBlockAuthorDate(TLObject):
    ID: int = 0xbaafe5e0

    def __init__(self, author: Any = None, published_date: Any = None) -> None:
        self.author = author
        self.published_date = published_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.author is not None and hasattr(self.author, 'write'): self.author.write(writer)
        writer.write_int32(self.published_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockAuthorDate':
        author = reader.read_object()
        published_date = reader.read_int32()
        return cls(author=author, published_date=published_date)


@register_tl
class PageBlockHeader(TLObject):
    ID: int = 0xbfd064ec

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockHeader':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageBlockSubheader(TLObject):
    ID: int = 0xf12bb6e1

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockSubheader':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageBlockParagraph(TLObject):
    ID: int = 0x467a0766

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockParagraph':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageBlockPreformatted(TLObject):
    ID: int = 0xc070d93e

    def __init__(self, text: Any = None, language: Any = None) -> None:
        self.text = text
        self.language = language

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        writer.write_string(self.language or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockPreformatted':
        text = reader.read_object()
        language = reader.read_string()
        return cls(text=text, language=language)


@register_tl
class PageBlockFooter(TLObject):
    ID: int = 0x48870999

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockFooter':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageBlockDivider(TLObject):
    ID: int = 0xdb20b188

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockDivider':
        return cls()


@register_tl
class PageBlockAnchor(TLObject):
    ID: int = 0xce0d37b0

    def __init__(self, name: Any = None) -> None:
        self.name = name

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.name or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockAnchor':
        name = reader.read_string()
        return cls(name=name)


@register_tl
class PageBlockList(TLObject):
    ID: int = 0xe4e88011

    def __init__(self, items: Any = None) -> None:
        self.items = items

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.items or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockList':
        items = reader.read_vector(lambda r: reader.read_object())
        return cls(items=items)


@register_tl
class PageBlockBlockquote(TLObject):
    ID: int = 0x263d7c26

    def __init__(self, text: Any = None, caption: Any = None) -> None:
        self.text = text
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockBlockquote':
        text = reader.read_object()
        caption = reader.read_object()
        return cls(text=text, caption=caption)


@register_tl
class PageBlockPullquote(TLObject):
    ID: int = 0x4f4456d3

    def __init__(self, text: Any = None, caption: Any = None) -> None:
        self.text = text
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockPullquote':
        text = reader.read_object()
        caption = reader.read_object()
        return cls(text=text, caption=caption)


@register_tl
class PageBlockPhoto(TLObject):
    ID: int = 0x1759c560

    def __init__(self, url: Any = None, webpage_id: Any = None, photo_id: Any = None, caption: Any = None) -> None:
        self.url = url
        self.webpage_id = webpage_id
        self.photo_id = photo_id
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.url is not None:
            flags |= (1 << 0)
        if self.webpage_id is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.photo_id or 0)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.webpage_id is not None:
            writer.write_int64(self.webpage_id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockPhoto':
        flags = reader.read_uint32()
        photo_id = reader.read_int64()
        caption = reader.read_object()
        url = reader.read_string() if (flags & (1 << 0)) else None
        webpage_id = reader.read_int64() if (flags & (1 << 0)) else None
        return cls(photo_id=photo_id, caption=caption, url=url, webpage_id=webpage_id)


@register_tl
class PageBlockVideo(TLObject):
    ID: int = 0x7c8fe7b6

    def __init__(self, autoplay: bool = False, loop: bool = False, video_id: Any = None, caption: Any = None) -> None:
        self.autoplay = autoplay
        self.loop = loop
        self.video_id = video_id
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.autoplay:
            flags |= (1 << 0)
        if self.loop:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.video_id or 0)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockVideo':
        flags = reader.read_uint32()
        autoplay = bool(flags & (1 << 0))
        loop = bool(flags & (1 << 1))
        video_id = reader.read_int64()
        caption = reader.read_object()
        return cls(autoplay=autoplay, loop=loop, video_id=video_id, caption=caption)


@register_tl
class PageBlockCover(TLObject):
    ID: int = 0x39f23300

    def __init__(self, cover: Any = None) -> None:
        self.cover = cover

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.cover is not None and hasattr(self.cover, 'write'): self.cover.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockCover':
        cover = reader.read_object()
        return cls(cover=cover)


@register_tl
class PageBlockEmbed(TLObject):
    ID: int = 0xa8718dc5

    def __init__(self, full_width: bool = False, allow_scrolling: bool = False, url: Any = None, html: Any = None, poster_photo_id: Any = None, w: Any = None, h: Any = None, caption: Any = None) -> None:
        self.full_width = full_width
        self.allow_scrolling = allow_scrolling
        self.url = url
        self.html = html
        self.poster_photo_id = poster_photo_id
        self.w = w
        self.h = h
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.full_width:
            flags |= (1 << 0)
        if self.allow_scrolling:
            flags |= (1 << 3)
        if self.url is not None:
            flags |= (1 << 1)
        if self.html is not None:
            flags |= (1 << 2)
        if self.poster_photo_id is not None:
            flags |= (1 << 4)
        if self.w is not None:
            flags |= (1 << 5)
        if self.h is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        if self.url is not None:
            writer.write_string(self.url or '')
        if self.html is not None:
            writer.write_string(self.html or '')
        if self.poster_photo_id is not None:
            writer.write_int64(self.poster_photo_id or 0)
        if self.w is not None:
            writer.write_int32(self.w or 0)
        if self.h is not None:
            writer.write_int32(self.h or 0)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockEmbed':
        flags = reader.read_uint32()
        full_width = bool(flags & (1 << 0))
        allow_scrolling = bool(flags & (1 << 3))
        url = reader.read_string() if (flags & (1 << 1)) else None
        html = reader.read_string() if (flags & (1 << 2)) else None
        poster_photo_id = reader.read_int64() if (flags & (1 << 4)) else None
        w = reader.read_int32() if (flags & (1 << 5)) else None
        h = reader.read_int32() if (flags & (1 << 5)) else None
        caption = reader.read_object()
        return cls(full_width=full_width, allow_scrolling=allow_scrolling, url=url, html=html, poster_photo_id=poster_photo_id, w=w, h=h, caption=caption)


@register_tl
class PageBlockEmbedPost(TLObject):
    ID: int = 0xf259a80b

    def __init__(self, url: Any = None, webpage_id: Any = None, author_photo_id: Any = None, author: Any = None, date: Any = None, blocks: Any = None, caption: Any = None) -> None:
        self.url = url
        self.webpage_id = webpage_id
        self.author_photo_id = author_photo_id
        self.author = author
        self.date = date
        self.blocks = blocks
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int64(self.webpage_id or 0)
        writer.write_int64(self.author_photo_id or 0)
        writer.write_string(self.author or '')
        writer.write_int32(self.date or 0)
        writer.write_vector(self.blocks or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockEmbedPost':
        url = reader.read_string()
        webpage_id = reader.read_int64()
        author_photo_id = reader.read_int64()
        author = reader.read_string()
        date = reader.read_int32()
        blocks = reader.read_vector(lambda r: reader.read_object())
        caption = reader.read_object()
        return cls(url=url, webpage_id=webpage_id, author_photo_id=author_photo_id, author=author, date=date, blocks=blocks, caption=caption)


@register_tl
class PageBlockCollage(TLObject):
    ID: int = 0x65a0fa4d

    def __init__(self, items: Any = None, caption: Any = None) -> None:
        self.items = items
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.items or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockCollage':
        items = reader.read_vector(lambda r: reader.read_object())
        caption = reader.read_object()
        return cls(items=items, caption=caption)


@register_tl
class PageBlockSlideshow(TLObject):
    ID: int = 0x31f9590

    def __init__(self, items: Any = None, caption: Any = None) -> None:
        self.items = items
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.items or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockSlideshow':
        items = reader.read_vector(lambda r: reader.read_object())
        caption = reader.read_object()
        return cls(items=items, caption=caption)


@register_tl
class PageBlockChannel(TLObject):
    ID: int = 0xef1751b5

    def __init__(self, channel: Any = None) -> None:
        self.channel = channel

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.channel is not None and hasattr(self.channel, 'write'): self.channel.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockChannel':
        channel = reader.read_object()
        return cls(channel=channel)


@register_tl
class PageBlockAudio(TLObject):
    ID: int = 0x804361ea

    def __init__(self, audio_id: Any = None, caption: Any = None) -> None:
        self.audio_id = audio_id
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.audio_id or 0)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockAudio':
        audio_id = reader.read_int64()
        caption = reader.read_object()
        return cls(audio_id=audio_id, caption=caption)


@register_tl
class PageBlockKicker(TLObject):
    ID: int = 0x1e148390

    def __init__(self, text: Any = None) -> None:
        self.text = text

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.text is not None and hasattr(self.text, 'write'): self.text.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockKicker':
        text = reader.read_object()
        return cls(text=text)


@register_tl
class PageBlockTable(TLObject):
    ID: int = 0xbf4dea82

    def __init__(self, bordered: bool = False, striped: bool = False, title: Any = None, rows: Any = None) -> None:
        self.bordered = bordered
        self.striped = striped
        self.title = title
        self.rows = rows

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.bordered:
            flags |= (1 << 0)
        if self.striped:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)
        writer.write_vector(self.rows or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockTable':
        flags = reader.read_uint32()
        bordered = bool(flags & (1 << 0))
        striped = bool(flags & (1 << 1))
        title = reader.read_object()
        rows = reader.read_vector(lambda r: reader.read_object())
        return cls(bordered=bordered, striped=striped, title=title, rows=rows)


@register_tl
class PageBlockOrderedList(TLObject):
    ID: int = 0x9a8ae1e1

    def __init__(self, items: Any = None) -> None:
        self.items = items

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.items or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockOrderedList':
        items = reader.read_vector(lambda r: reader.read_object())
        return cls(items=items)


@register_tl
class PageBlockDetails(TLObject):
    ID: int = 0x76768bed

    def __init__(self, open: bool = False, blocks: Any = None, title: Any = None) -> None:
        self.open = open
        self.blocks = blocks
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.open:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_vector(self.blocks or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockDetails':
        flags = reader.read_uint32()
        open = bool(flags & (1 << 0))
        blocks = reader.read_vector(lambda r: reader.read_object())
        title = reader.read_object()
        return cls(open=open, blocks=blocks, title=title)


@register_tl
class PageBlockRelatedArticles(TLObject):
    ID: int = 0x16115a96

    def __init__(self, title: Any = None, articles: Any = None) -> None:
        self.title = title
        self.articles = articles

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.title is not None and hasattr(self.title, 'write'): self.title.write(writer)
        writer.write_vector(self.articles or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockRelatedArticles':
        title = reader.read_object()
        articles = reader.read_vector(lambda r: reader.read_object())
        return cls(title=title, articles=articles)


@register_tl
class PageBlockMap(TLObject):
    ID: int = 0xa44f3ef6

    def __init__(self, geo: Any = None, zoom: Any = None, w: Any = None, h: Any = None, caption: Any = None) -> None:
        self.geo = geo
        self.zoom = zoom
        self.w = w
        self.h = h
        self.caption = caption

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.geo is not None and hasattr(self.geo, 'write'): self.geo.write(writer)
        writer.write_int32(self.zoom or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        if self.caption is not None and hasattr(self.caption, 'write'): self.caption.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PageBlockMap':
        geo = reader.read_object()
        zoom = reader.read_int32()
        w = reader.read_int32()
        h = reader.read_int32()
        caption = reader.read_object()
        return cls(geo=geo, zoom=zoom, w=w, h=h, caption=caption)


@register_tl
class PhoneCallDiscardReasonMissed(TLObject):
    ID: int = 0x85e42301

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallDiscardReasonMissed':
        return cls()


@register_tl
class PhoneCallDiscardReasonDisconnect(TLObject):
    ID: int = 0xe095c1a0

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallDiscardReasonDisconnect':
        return cls()


@register_tl
class PhoneCallDiscardReasonHangup(TLObject):
    ID: int = 0x57adc690

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallDiscardReasonHangup':
        return cls()


@register_tl
class PhoneCallDiscardReasonBusy(TLObject):
    ID: int = 0xfaf7e8c9

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallDiscardReasonBusy':
        return cls()


@register_tl
class PhoneCallDiscardReasonMigrateConferenceCall(TLObject):
    ID: int = 0x9fbbf1f7

    def __init__(self, slug: Any = None) -> None:
        self.slug = slug

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.slug or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallDiscardReasonMigrateConferenceCall':
        slug = reader.read_string()
        return cls(slug=slug)


@register_tl
class DataJSON(TLObject):
    ID: int = 0x7d748d04

    def __init__(self, data: Any = None) -> None:
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.data or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'DataJSON':
        data = reader.read_string()
        return cls(data=data)


@register_tl
class LabeledPrice(TLObject):
    ID: int = 0xcb296bf8

    def __init__(self, label: Any = None, amount: Any = None) -> None:
        self.label = label
        self.amount = amount

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.label or '')
        writer.write_int64(self.amount or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'LabeledPrice':
        label = reader.read_string()
        amount = reader.read_int64()
        return cls(label=label, amount=amount)


@register_tl
class Invoice(TLObject):
    ID: int = 0x49ee584

    def __init__(self, test: bool = False, name_requested: bool = False, phone_requested: bool = False, email_requested: bool = False, shipping_address_requested: bool = False, flexible: bool = False, phone_to_provider: bool = False, email_to_provider: bool = False, recurring: bool = False, max_tip_amount: Any = None, suggested_tip_amounts: Any = None, terms_url: Any = None, subscription_period: Any = None, currency: Any = None, prices: Any = None) -> None:
        self.test = test
        self.name_requested = name_requested
        self.phone_requested = phone_requested
        self.email_requested = email_requested
        self.shipping_address_requested = shipping_address_requested
        self.flexible = flexible
        self.phone_to_provider = phone_to_provider
        self.email_to_provider = email_to_provider
        self.recurring = recurring
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.terms_url = terms_url
        self.subscription_period = subscription_period
        self.currency = currency
        self.prices = prices

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.test:
            flags |= (1 << 0)
        if self.name_requested:
            flags |= (1 << 1)
        if self.phone_requested:
            flags |= (1 << 2)
        if self.email_requested:
            flags |= (1 << 3)
        if self.shipping_address_requested:
            flags |= (1 << 4)
        if self.flexible:
            flags |= (1 << 5)
        if self.phone_to_provider:
            flags |= (1 << 6)
        if self.email_to_provider:
            flags |= (1 << 7)
        if self.recurring:
            flags |= (1 << 9)
        if self.max_tip_amount is not None:
            flags |= (1 << 8)
        if self.suggested_tip_amounts is not None:
            flags |= (1 << 8)
        if self.terms_url is not None:
            flags |= (1 << 10)
        if self.subscription_period is not None:
            flags |= (1 << 11)
        writer.write_uint32(flags)
        writer.write_string(self.currency or '')
        writer.write_vector(self.prices or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.max_tip_amount is not None:
            writer.write_int64(self.max_tip_amount or 0)
        if self.suggested_tip_amounts is not None:
            writer.write_vector(self.suggested_tip_amounts or [], lambda w, x: w.write_int64(x))
        if self.terms_url is not None:
            writer.write_string(self.terms_url or '')
        if self.subscription_period is not None:
            writer.write_int32(self.subscription_period or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'Invoice':
        flags = reader.read_uint32()
        test = bool(flags & (1 << 0))
        name_requested = bool(flags & (1 << 1))
        phone_requested = bool(flags & (1 << 2))
        email_requested = bool(flags & (1 << 3))
        shipping_address_requested = bool(flags & (1 << 4))
        flexible = bool(flags & (1 << 5))
        phone_to_provider = bool(flags & (1 << 6))
        email_to_provider = bool(flags & (1 << 7))
        recurring = bool(flags & (1 << 9))
        currency = reader.read_string()
        prices = reader.read_vector(lambda r: reader.read_object())
        max_tip_amount = reader.read_int64() if (flags & (1 << 8)) else None
        suggested_tip_amounts = reader.read_vector(lambda r: r.read_int64()) if (flags & (1 << 8)) else None
        terms_url = reader.read_string() if (flags & (1 << 10)) else None
        subscription_period = reader.read_int32() if (flags & (1 << 11)) else None
        return cls(test=test, name_requested=name_requested, phone_requested=phone_requested, email_requested=email_requested, shipping_address_requested=shipping_address_requested, flexible=flexible, phone_to_provider=phone_to_provider, email_to_provider=email_to_provider, recurring=recurring, currency=currency, prices=prices, max_tip_amount=max_tip_amount, suggested_tip_amounts=suggested_tip_amounts, terms_url=terms_url, subscription_period=subscription_period)


@register_tl
class PaymentCharge(TLObject):
    ID: int = 0xea02c27e

    def __init__(self, id: Any = None, provider_charge_id: Any = None) -> None:
        self.id = id
        self.provider_charge_id = provider_charge_id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_string(self.provider_charge_id or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentCharge':
        id = reader.read_string()
        provider_charge_id = reader.read_string()
        return cls(id=id, provider_charge_id=provider_charge_id)


@register_tl
class PostAddress(TLObject):
    ID: int = 0x1e8caaeb

    def __init__(self, street_line1: Any = None, street_line2: Any = None, city: Any = None, state: Any = None, country_iso2: Any = None, post_code: Any = None) -> None:
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.city = city
        self.state = state
        self.country_iso2 = country_iso2
        self.post_code = post_code

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.street_line1 or '')
        writer.write_string(self.street_line2 or '')
        writer.write_string(self.city or '')
        writer.write_string(self.state or '')
        writer.write_string(self.country_iso2 or '')
        writer.write_string(self.post_code or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PostAddress':
        street_line1 = reader.read_string()
        street_line2 = reader.read_string()
        city = reader.read_string()
        state = reader.read_string()
        country_iso2 = reader.read_string()
        post_code = reader.read_string()
        return cls(street_line1=street_line1, street_line2=street_line2, city=city, state=state, country_iso2=country_iso2, post_code=post_code)


@register_tl
class PaymentRequestedInfo(TLObject):
    ID: int = 0x909c3f94

    def __init__(self, name: Any = None, phone: Any = None, email: Any = None, shipping_address: Any = None) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.shipping_address = shipping_address

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.name is not None:
            flags |= (1 << 0)
        if self.phone is not None:
            flags |= (1 << 1)
        if self.email is not None:
            flags |= (1 << 2)
        if self.shipping_address is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        if self.name is not None:
            writer.write_string(self.name or '')
        if self.phone is not None:
            writer.write_string(self.phone or '')
        if self.email is not None:
            writer.write_string(self.email or '')
        if self.shipping_address is not None:
            if self.shipping_address is not None and hasattr(self.shipping_address, 'write'): self.shipping_address.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentRequestedInfo':
        flags = reader.read_uint32()
        name = reader.read_string() if (flags & (1 << 0)) else None
        phone = reader.read_string() if (flags & (1 << 1)) else None
        email = reader.read_string() if (flags & (1 << 2)) else None
        shipping_address = reader.read_object() if (flags & (1 << 3)) else None
        return cls(name=name, phone=phone, email=email, shipping_address=shipping_address)


@register_tl
class PaymentSavedCredentialsCard(TLObject):
    ID: int = 0xcdc27a1f

    def __init__(self, id: Any = None, title: Any = None) -> None:
        self.id = id
        self.title = title

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_string(self.title or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentSavedCredentialsCard':
        id = reader.read_string()
        title = reader.read_string()
        return cls(id=id, title=title)


@register_tl
class WebDocument(TLObject):
    ID: int = 0x1c570ed1

    def __init__(self, url: Any = None, access_hash: Any = None, size: Any = None, mime_type: Any = None, attributes: Any = None) -> None:
        self.url = url
        self.access_hash = access_hash
        self.size = size
        self.mime_type = mime_type
        self.attributes = attributes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.size or 0)
        writer.write_string(self.mime_type or '')
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebDocument':
        url = reader.read_string()
        access_hash = reader.read_int64()
        size = reader.read_int32()
        mime_type = reader.read_string()
        attributes = reader.read_vector(lambda r: reader.read_object())
        return cls(url=url, access_hash=access_hash, size=size, mime_type=mime_type, attributes=attributes)


@register_tl
class WebDocumentNoProxy(TLObject):
    ID: int = 0xf9c8bcc6

    def __init__(self, url: Any = None, size: Any = None, mime_type: Any = None, attributes: Any = None) -> None:
        self.url = url
        self.size = size
        self.mime_type = mime_type
        self.attributes = attributes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int32(self.size or 0)
        writer.write_string(self.mime_type or '')
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'WebDocumentNoProxy':
        url = reader.read_string()
        size = reader.read_int32()
        mime_type = reader.read_string()
        attributes = reader.read_vector(lambda r: reader.read_object())
        return cls(url=url, size=size, mime_type=mime_type, attributes=attributes)


@register_tl
class InputWebDocument(TLObject):
    ID: int = 0x9bed434d

    def __init__(self, url: Any = None, size: Any = None, mime_type: Any = None, attributes: Any = None) -> None:
        self.url = url
        self.size = size
        self.mime_type = mime_type
        self.attributes = attributes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int32(self.size or 0)
        writer.write_string(self.mime_type or '')
        writer.write_vector(self.attributes or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputWebDocument':
        url = reader.read_string()
        size = reader.read_int32()
        mime_type = reader.read_string()
        attributes = reader.read_vector(lambda r: reader.read_object())
        return cls(url=url, size=size, mime_type=mime_type, attributes=attributes)


@register_tl
class InputWebFileLocation(TLObject):
    ID: int = 0xc239d686

    def __init__(self, url: Any = None, access_hash: Any = None) -> None:
        self.url = url
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputWebFileLocation':
        url = reader.read_string()
        access_hash = reader.read_int64()
        return cls(url=url, access_hash=access_hash)


@register_tl
class InputWebFileGeoPointLocation(TLObject):
    ID: int = 0x9f2221c9

    def __init__(self, geo_point: Any = None, access_hash: Any = None, w: Any = None, h: Any = None, zoom: Any = None, scale: Any = None) -> None:
        self.geo_point = geo_point
        self.access_hash = access_hash
        self.w = w
        self.h = h
        self.zoom = zoom
        self.scale = scale

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.geo_point is not None and hasattr(self.geo_point, 'write'): self.geo_point.write(writer)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.w or 0)
        writer.write_int32(self.h or 0)
        writer.write_int32(self.zoom or 0)
        writer.write_int32(self.scale or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputWebFileGeoPointLocation':
        geo_point = reader.read_object()
        access_hash = reader.read_int64()
        w = reader.read_int32()
        h = reader.read_int32()
        zoom = reader.read_int32()
        scale = reader.read_int32()
        return cls(geo_point=geo_point, access_hash=access_hash, w=w, h=h, zoom=zoom, scale=scale)


@register_tl
class InputWebFileAudioAlbumThumbLocation(TLObject):
    ID: int = 0xf46fe924

    def __init__(self, small: bool = False, document: Any = None, title: Any = None, performer: Any = None) -> None:
        self.small = small
        self.document = document
        self.title = title
        self.performer = performer

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.small:
            flags |= (1 << 2)
        if self.document is not None:
            flags |= (1 << 0)
        if self.title is not None:
            flags |= (1 << 1)
        if self.performer is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.document is not None:
            if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        if self.title is not None:
            writer.write_string(self.title or '')
        if self.performer is not None:
            writer.write_string(self.performer or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputWebFileAudioAlbumThumbLocation':
        flags = reader.read_uint32()
        small = bool(flags & (1 << 2))
        document = reader.read_object() if (flags & (1 << 0)) else None
        title = reader.read_string() if (flags & (1 << 1)) else None
        performer = reader.read_string() if (flags & (1 << 1)) else None
        return cls(small=small, document=document, title=title, performer=performer)


@register_tl
class UploadWebFile(TLObject):
    ID: int = 0x21e753bc

    def __init__(self, size: Any = None, mime_type: Any = None, file_type: Any = None, mtime: Any = None, bytes: Any = None) -> None:
        self.size = size
        self.mime_type = mime_type
        self.file_type = file_type
        self.mtime = mtime
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.size or 0)
        writer.write_string(self.mime_type or '')
        if self.file_type is not None and hasattr(self.file_type, 'write'): self.file_type.write(writer)
        writer.write_int32(self.mtime or 0)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadWebFile':
        size = reader.read_int32()
        mime_type = reader.read_string()
        file_type = reader.read_object()
        mtime = reader.read_int32()
        bytes = reader.read_bytes()
        return cls(size=size, mime_type=mime_type, file_type=file_type, mtime=mtime, bytes=bytes)


@register_tl
class PaymentsPaymentForm(TLObject):
    ID: int = 0xa0058751

    def __init__(self, can_save_credentials: bool = False, password_missing: bool = False, photo: Any = None, native_provider: Any = None, native_params: Any = None, additional_methods: Any = None, saved_info: Any = None, saved_credentials: Any = None, form_id: Any = None, bot_id: Any = None, title: Any = None, description: Any = None, invoice: Any = None, provider_id: Any = None, url: Any = None, users: Any = None) -> None:
        self.can_save_credentials = can_save_credentials
        self.password_missing = password_missing
        self.photo = photo
        self.native_provider = native_provider
        self.native_params = native_params
        self.additional_methods = additional_methods
        self.saved_info = saved_info
        self.saved_credentials = saved_credentials
        self.form_id = form_id
        self.bot_id = bot_id
        self.title = title
        self.description = description
        self.invoice = invoice
        self.provider_id = provider_id
        self.url = url
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.can_save_credentials:
            flags |= (1 << 2)
        if self.password_missing:
            flags |= (1 << 3)
        if self.photo is not None:
            flags |= (1 << 5)
        if self.native_provider is not None:
            flags |= (1 << 4)
        if self.native_params is not None:
            flags |= (1 << 4)
        if self.additional_methods is not None:
            flags |= (1 << 6)
        if self.saved_info is not None:
            flags |= (1 << 0)
        if self.saved_credentials is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.form_id or 0)
        writer.write_int64(self.bot_id or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        writer.write_int64(self.provider_id or 0)
        writer.write_string(self.url or '')
        if self.native_provider is not None:
            writer.write_string(self.native_provider or '')
        if self.native_params is not None:
            if self.native_params is not None and hasattr(self.native_params, 'write'): self.native_params.write(writer)
        if self.additional_methods is not None:
            writer.write_vector(self.additional_methods or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        if self.saved_info is not None:
            if self.saved_info is not None and hasattr(self.saved_info, 'write'): self.saved_info.write(writer)
        if self.saved_credentials is not None:
            writer.write_vector(self.saved_credentials or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsPaymentForm':
        flags = reader.read_uint32()
        can_save_credentials = bool(flags & (1 << 2))
        password_missing = bool(flags & (1 << 3))
        form_id = reader.read_int64()
        bot_id = reader.read_int64()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 5)) else None
        invoice = reader.read_object()
        provider_id = reader.read_int64()
        url = reader.read_string()
        native_provider = reader.read_string() if (flags & (1 << 4)) else None
        native_params = reader.read_object() if (flags & (1 << 4)) else None
        additional_methods = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 6)) else None
        saved_info = reader.read_object() if (flags & (1 << 0)) else None
        saved_credentials = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(can_save_credentials=can_save_credentials, password_missing=password_missing, form_id=form_id, bot_id=bot_id, title=title, description=description, photo=photo, invoice=invoice, provider_id=provider_id, url=url, native_provider=native_provider, native_params=native_params, additional_methods=additional_methods, saved_info=saved_info, saved_credentials=saved_credentials, users=users)


@register_tl
class PaymentsPaymentFormStars(TLObject):
    ID: int = 0x7bf6b15c

    def __init__(self, photo: Any = None, form_id: Any = None, bot_id: Any = None, title: Any = None, description: Any = None, invoice: Any = None, users: Any = None) -> None:
        self.photo = photo
        self.form_id = form_id
        self.bot_id = bot_id
        self.title = title
        self.description = description
        self.invoice = invoice
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.photo is not None:
            flags |= (1 << 5)
        writer.write_uint32(flags)
        writer.write_int64(self.form_id or 0)
        writer.write_int64(self.bot_id or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsPaymentFormStars':
        flags = reader.read_uint32()
        form_id = reader.read_int64()
        bot_id = reader.read_int64()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 5)) else None
        invoice = reader.read_object()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(form_id=form_id, bot_id=bot_id, title=title, description=description, photo=photo, invoice=invoice, users=users)


@register_tl
class PaymentsPaymentFormStarGift(TLObject):
    ID: int = 0xb425cfe1

    def __init__(self, form_id: Any = None, invoice: Any = None) -> None:
        self.form_id = form_id
        self.invoice = invoice

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.form_id or 0)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsPaymentFormStarGift':
        form_id = reader.read_int64()
        invoice = reader.read_object()
        return cls(form_id=form_id, invoice=invoice)


@register_tl
class PaymentsValidatedRequestedInfo(TLObject):
    ID: int = 0xd1451883

    def __init__(self, id: Any = None, shipping_options: Any = None) -> None:
        self.id = id
        self.shipping_options = shipping_options

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.id is not None:
            flags |= (1 << 0)
        if self.shipping_options is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.id is not None:
            writer.write_string(self.id or '')
        if self.shipping_options is not None:
            writer.write_vector(self.shipping_options or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsValidatedRequestedInfo':
        flags = reader.read_uint32()
        id = reader.read_string() if (flags & (1 << 0)) else None
        shipping_options = reader.read_vector(lambda r: reader.read_object()) if (flags & (1 << 1)) else None
        return cls(id=id, shipping_options=shipping_options)


@register_tl
class PaymentsPaymentResult(TLObject):
    ID: int = 0x4e5f810d

    def __init__(self, updates: Any = None) -> None:
        self.updates = updates

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.updates is not None and hasattr(self.updates, 'write'): self.updates.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsPaymentResult':
        updates = reader.read_object()
        return cls(updates=updates)


@register_tl
class PaymentsPaymentVerificationNeeded(TLObject):
    ID: int = 0xd8411139

    def __init__(self, url: Any = None) -> None:
        self.url = url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsPaymentVerificationNeeded':
        url = reader.read_string()
        return cls(url=url)


@register_tl
class PaymentsPaymentReceipt(TLObject):
    ID: int = 0x70c4fe03

    def __init__(self, photo: Any = None, info: Any = None, shipping: Any = None, tip_amount: Any = None, date: Any = None, bot_id: Any = None, provider_id: Any = None, title: Any = None, description: Any = None, invoice: Any = None, currency: Any = None, total_amount: Any = None, credentials_title: Any = None, users: Any = None) -> None:
        self.photo = photo
        self.info = info
        self.shipping = shipping
        self.tip_amount = tip_amount
        self.date = date
        self.bot_id = bot_id
        self.provider_id = provider_id
        self.title = title
        self.description = description
        self.invoice = invoice
        self.currency = currency
        self.total_amount = total_amount
        self.credentials_title = credentials_title
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.photo is not None:
            flags |= (1 << 2)
        if self.info is not None:
            flags |= (1 << 0)
        if self.shipping is not None:
            flags |= (1 << 1)
        if self.tip_amount is not None:
            flags |= (1 << 3)
        writer.write_uint32(flags)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.bot_id or 0)
        writer.write_int64(self.provider_id or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        if self.info is not None:
            if self.info is not None and hasattr(self.info, 'write'): self.info.write(writer)
        if self.shipping is not None:
            if self.shipping is not None and hasattr(self.shipping, 'write'): self.shipping.write(writer)
        if self.tip_amount is not None:
            writer.write_int64(self.tip_amount or 0)
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)
        writer.write_string(self.credentials_title or '')
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsPaymentReceipt':
        flags = reader.read_uint32()
        date = reader.read_int32()
        bot_id = reader.read_int64()
        provider_id = reader.read_int64()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 2)) else None
        invoice = reader.read_object()
        info = reader.read_object() if (flags & (1 << 0)) else None
        shipping = reader.read_object() if (flags & (1 << 1)) else None
        tip_amount = reader.read_int64() if (flags & (1 << 3)) else None
        currency = reader.read_string()
        total_amount = reader.read_int64()
        credentials_title = reader.read_string()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(date=date, bot_id=bot_id, provider_id=provider_id, title=title, description=description, photo=photo, invoice=invoice, info=info, shipping=shipping, tip_amount=tip_amount, currency=currency, total_amount=total_amount, credentials_title=credentials_title, users=users)


@register_tl
class PaymentsPaymentReceiptStars(TLObject):
    ID: int = 0xdabbf83a

    def __init__(self, photo: Any = None, date: Any = None, bot_id: Any = None, title: Any = None, description: Any = None, invoice: Any = None, currency: Any = None, total_amount: Any = None, transaction_id: Any = None, users: Any = None) -> None:
        self.photo = photo
        self.date = date
        self.bot_id = bot_id
        self.title = title
        self.description = description
        self.invoice = invoice
        self.currency = currency
        self.total_amount = total_amount
        self.transaction_id = transaction_id
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.photo is not None:
            flags |= (1 << 2)
        writer.write_uint32(flags)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.bot_id or 0)
        writer.write_string(self.title or '')
        writer.write_string(self.description or '')
        if self.photo is not None:
            if self.photo is not None and hasattr(self.photo, 'write'): self.photo.write(writer)
        if self.invoice is not None and hasattr(self.invoice, 'write'): self.invoice.write(writer)
        writer.write_string(self.currency or '')
        writer.write_int64(self.total_amount or 0)
        writer.write_string(self.transaction_id or '')
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsPaymentReceiptStars':
        flags = reader.read_uint32()
        date = reader.read_int32()
        bot_id = reader.read_int64()
        title = reader.read_string()
        description = reader.read_string()
        photo = reader.read_object() if (flags & (1 << 2)) else None
        invoice = reader.read_object()
        currency = reader.read_string()
        total_amount = reader.read_int64()
        transaction_id = reader.read_string()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(date=date, bot_id=bot_id, title=title, description=description, photo=photo, invoice=invoice, currency=currency, total_amount=total_amount, transaction_id=transaction_id, users=users)


@register_tl
class PaymentsSavedInfo(TLObject):
    ID: int = 0xfb8fe43c

    def __init__(self, has_saved_credentials: bool = False, saved_info: Any = None) -> None:
        self.has_saved_credentials = has_saved_credentials
        self.saved_info = saved_info

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.has_saved_credentials:
            flags |= (1 << 1)
        if self.saved_info is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.saved_info is not None:
            if self.saved_info is not None and hasattr(self.saved_info, 'write'): self.saved_info.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PaymentsSavedInfo':
        flags = reader.read_uint32()
        has_saved_credentials = bool(flags & (1 << 1))
        saved_info = reader.read_object() if (flags & (1 << 0)) else None
        return cls(has_saved_credentials=has_saved_credentials, saved_info=saved_info)


@register_tl
class InputPaymentCredentialsSaved(TLObject):
    ID: int = 0xc10eb2cf

    def __init__(self, id: Any = None, tmp_password: Any = None) -> None:
        self.id = id
        self.tmp_password = tmp_password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_bytes(self.tmp_password or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPaymentCredentialsSaved':
        id = reader.read_string()
        tmp_password = reader.read_bytes()
        return cls(id=id, tmp_password=tmp_password)


@register_tl
class InputPaymentCredentials(TLObject):
    ID: int = 0x3417d728

    def __init__(self, save: bool = False, data: Any = None) -> None:
        self.save = save
        self.data = data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.save:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.data is not None and hasattr(self.data, 'write'): self.data.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPaymentCredentials':
        flags = reader.read_uint32()
        save = bool(flags & (1 << 0))
        data = reader.read_object()
        return cls(save=save, data=data)


@register_tl
class InputPaymentCredentialsApplePay(TLObject):
    ID: int = 0xaa1c39f

    def __init__(self, payment_data: Any = None) -> None:
        self.payment_data = payment_data

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.payment_data is not None and hasattr(self.payment_data, 'write'): self.payment_data.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPaymentCredentialsApplePay':
        payment_data = reader.read_object()
        return cls(payment_data=payment_data)


@register_tl
class InputPaymentCredentialsGooglePay(TLObject):
    ID: int = 0x8ac32801

    def __init__(self, payment_token: Any = None) -> None:
        self.payment_token = payment_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.payment_token is not None and hasattr(self.payment_token, 'write'): self.payment_token.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPaymentCredentialsGooglePay':
        payment_token = reader.read_object()
        return cls(payment_token=payment_token)


@register_tl
class AccountTmpPassword(TLObject):
    ID: int = 0xdb64fd34

    def __init__(self, tmp_password: Any = None, valid_until: Any = None) -> None:
        self.tmp_password = tmp_password
        self.valid_until = valid_until

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.tmp_password or b'')
        writer.write_int32(self.valid_until or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'AccountTmpPassword':
        tmp_password = reader.read_bytes()
        valid_until = reader.read_int32()
        return cls(tmp_password=tmp_password, valid_until=valid_until)


@register_tl
class ShippingOption(TLObject):
    ID: int = 0xb6213cdf

    def __init__(self, id: Any = None, title: Any = None, prices: Any = None) -> None:
        self.id = id
        self.title = title
        self.prices = prices

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.id or '')
        writer.write_string(self.title or '')
        writer.write_vector(self.prices or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'ShippingOption':
        id = reader.read_string()
        title = reader.read_string()
        prices = reader.read_vector(lambda r: reader.read_object())
        return cls(id=id, title=title, prices=prices)


@register_tl
class InputStickerSetItem(TLObject):
    ID: int = 0x32da9e9c

    def __init__(self, mask_coords: Any = None, keywords: Any = None, document: Any = None, emoji: Any = None) -> None:
        self.mask_coords = mask_coords
        self.keywords = keywords
        self.document = document
        self.emoji = emoji

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.mask_coords is not None:
            flags |= (1 << 0)
        if self.keywords is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.document is not None and hasattr(self.document, 'write'): self.document.write(writer)
        writer.write_string(self.emoji or '')
        if self.mask_coords is not None:
            if self.mask_coords is not None and hasattr(self.mask_coords, 'write'): self.mask_coords.write(writer)
        if self.keywords is not None:
            writer.write_string(self.keywords or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'InputStickerSetItem':
        flags = reader.read_uint32()
        document = reader.read_object()
        emoji = reader.read_string()
        mask_coords = reader.read_object() if (flags & (1 << 0)) else None
        keywords = reader.read_string() if (flags & (1 << 1)) else None
        return cls(document=document, emoji=emoji, mask_coords=mask_coords, keywords=keywords)


@register_tl
class InputPhoneCall(TLObject):
    ID: int = 0x1e36fded

    def __init__(self, id: Any = None, access_hash: Any = None) -> None:
        self.id = id
        self.access_hash = access_hash

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'InputPhoneCall':
        id = reader.read_int64()
        access_hash = reader.read_int64()
        return cls(id=id, access_hash=access_hash)


@register_tl
class PhoneCallEmpty(TLObject):
    ID: int = 0x5366c915

    def __init__(self, id: Any = None) -> None:
        self.id = id

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.id or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallEmpty':
        id = reader.read_int64()
        return cls(id=id)


@register_tl
class PhoneCallWaiting(TLObject):
    ID: int = 0xc5226f17

    def __init__(self, video: bool = False, receive_date: Any = None, id: Any = None, access_hash: Any = None, date: Any = None, admin_id: Any = None, participant_id: Any = None, protocol: Any = None) -> None:
        self.video = video
        self.receive_date = receive_date
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 6)
        if self.receive_date is not None:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.admin_id or 0)
        writer.write_int64(self.participant_id or 0)
        if self.protocol is not None and hasattr(self.protocol, 'write'): self.protocol.write(writer)
        if self.receive_date is not None:
            writer.write_int32(self.receive_date or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallWaiting':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 6))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        protocol = reader.read_object()
        receive_date = reader.read_int32() if (flags & (1 << 0)) else None
        return cls(video=video, id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, protocol=protocol, receive_date=receive_date)


@register_tl
class PhoneCallRequested(TLObject):
    ID: int = 0x14b0ed0c

    def __init__(self, video: bool = False, id: Any = None, access_hash: Any = None, date: Any = None, admin_id: Any = None, participant_id: Any = None, g_a_hash: Any = None, protocol: Any = None) -> None:
        self.video = video
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_a_hash = g_a_hash
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.admin_id or 0)
        writer.write_int64(self.participant_id or 0)
        writer.write_bytes(self.g_a_hash or b'')
        if self.protocol is not None and hasattr(self.protocol, 'write'): self.protocol.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallRequested':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 6))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_a_hash = reader.read_bytes()
        protocol = reader.read_object()
        return cls(video=video, id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_hash=g_a_hash, protocol=protocol)


@register_tl
class PhoneCallAccepted(TLObject):
    ID: int = 0x3660c311

    def __init__(self, video: bool = False, id: Any = None, access_hash: Any = None, date: Any = None, admin_id: Any = None, participant_id: Any = None, g_b: Any = None, protocol: Any = None) -> None:
        self.video = video
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_b = g_b
        self.protocol = protocol

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.video:
            flags |= (1 << 6)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.admin_id or 0)
        writer.write_int64(self.participant_id or 0)
        writer.write_bytes(self.g_b or b'')
        if self.protocol is not None and hasattr(self.protocol, 'write'): self.protocol.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallAccepted':
        flags = reader.read_uint32()
        video = bool(flags & (1 << 6))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_b = reader.read_bytes()
        protocol = reader.read_object()
        return cls(video=video, id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_b=g_b, protocol=protocol)


@register_tl
class PhoneCall(TLObject):
    ID: int = 0x30535af5

    def __init__(self, p2p_allowed: bool = False, video: bool = False, conference_supported: bool = False, custom_parameters: Any = None, id: Any = None, access_hash: Any = None, date: Any = None, admin_id: Any = None, participant_id: Any = None, g_a_or_b: Any = None, key_fingerprint: Any = None, protocol: Any = None, connections: Any = None, start_date: Any = None) -> None:
        self.p2p_allowed = p2p_allowed
        self.video = video
        self.conference_supported = conference_supported
        self.custom_parameters = custom_parameters
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id
        self.g_a_or_b = g_a_or_b
        self.key_fingerprint = key_fingerprint
        self.protocol = protocol
        self.connections = connections
        self.start_date = start_date

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.p2p_allowed:
            flags |= (1 << 5)
        if self.video:
            flags |= (1 << 6)
        if self.conference_supported:
            flags |= (1 << 8)
        if self.custom_parameters is not None:
            flags |= (1 << 7)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_int64(self.access_hash or 0)
        writer.write_int32(self.date or 0)
        writer.write_int64(self.admin_id or 0)
        writer.write_int64(self.participant_id or 0)
        writer.write_bytes(self.g_a_or_b or b'')
        writer.write_int64(self.key_fingerprint or 0)
        if self.protocol is not None and hasattr(self.protocol, 'write'): self.protocol.write(writer)
        writer.write_vector(self.connections or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)
        writer.write_int32(self.start_date or 0)
        if self.custom_parameters is not None:
            if self.custom_parameters is not None and hasattr(self.custom_parameters, 'write'): self.custom_parameters.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCall':
        flags = reader.read_uint32()
        p2p_allowed = bool(flags & (1 << 5))
        video = bool(flags & (1 << 6))
        conference_supported = bool(flags & (1 << 8))
        id = reader.read_int64()
        access_hash = reader.read_int64()
        date = reader.read_int32()
        admin_id = reader.read_int64()
        participant_id = reader.read_int64()
        g_a_or_b = reader.read_bytes()
        key_fingerprint = reader.read_int64()
        protocol = reader.read_object()
        connections = reader.read_vector(lambda r: reader.read_object())
        start_date = reader.read_int32()
        custom_parameters = reader.read_object() if (flags & (1 << 7)) else None
        return cls(p2p_allowed=p2p_allowed, video=video, conference_supported=conference_supported, id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint, protocol=protocol, connections=connections, start_date=start_date, custom_parameters=custom_parameters)


@register_tl
class PhoneCallDiscarded(TLObject):
    ID: int = 0x50ca4de1

    def __init__(self, need_rating: bool = False, need_debug: bool = False, video: bool = False, reason: Any = None, duration: Any = None, id: Any = None) -> None:
        self.need_rating = need_rating
        self.need_debug = need_debug
        self.video = video
        self.reason = reason
        self.duration = duration
        self.id = id

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
        writer.write_int64(self.id or 0)
        if self.reason is not None:
            if self.reason is not None and hasattr(self.reason, 'write'): self.reason.write(writer)
        if self.duration is not None:
            writer.write_int32(self.duration or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallDiscarded':
        flags = reader.read_uint32()
        need_rating = bool(flags & (1 << 2))
        need_debug = bool(flags & (1 << 3))
        video = bool(flags & (1 << 6))
        id = reader.read_int64()
        reason = reader.read_object() if (flags & (1 << 0)) else None
        duration = reader.read_int32() if (flags & (1 << 1)) else None
        return cls(need_rating=need_rating, need_debug=need_debug, video=video, id=id, reason=reason, duration=duration)


@register_tl
class PhoneConnection(TLObject):
    ID: int = 0x9cc123c7

    def __init__(self, tcp: bool = False, id: Any = None, ip: Any = None, ipv6: Any = None, port: Any = None, peer_tag: Any = None) -> None:
        self.tcp = tcp
        self.id = id
        self.ip = ip
        self.ipv6 = ipv6
        self.port = port
        self.peer_tag = peer_tag

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.tcp:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(self.ip or '')
        writer.write_string(self.ipv6 or '')
        writer.write_int32(self.port or 0)
        writer.write_bytes(self.peer_tag or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneConnection':
        flags = reader.read_uint32()
        tcp = bool(flags & (1 << 0))
        id = reader.read_int64()
        ip = reader.read_string()
        ipv6 = reader.read_string()
        port = reader.read_int32()
        peer_tag = reader.read_bytes()
        return cls(tcp=tcp, id=id, ip=ip, ipv6=ipv6, port=port, peer_tag=peer_tag)


@register_tl
class PhoneConnectionWebrtc(TLObject):
    ID: int = 0x635fe375

    def __init__(self, turn: bool = False, stun: bool = False, id: Any = None, ip: Any = None, ipv6: Any = None, port: Any = None, username: Any = None, password: Any = None) -> None:
        self.turn = turn
        self.stun = stun
        self.id = id
        self.ip = ip
        self.ipv6 = ipv6
        self.port = port
        self.username = username
        self.password = password

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.turn:
            flags |= (1 << 0)
        if self.stun:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int64(self.id or 0)
        writer.write_string(self.ip or '')
        writer.write_string(self.ipv6 or '')
        writer.write_int32(self.port or 0)
        writer.write_string(self.username or '')
        writer.write_string(self.password or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneConnectionWebrtc':
        flags = reader.read_uint32()
        turn = bool(flags & (1 << 0))
        stun = bool(flags & (1 << 1))
        id = reader.read_int64()
        ip = reader.read_string()
        ipv6 = reader.read_string()
        port = reader.read_int32()
        username = reader.read_string()
        password = reader.read_string()
        return cls(turn=turn, stun=stun, id=id, ip=ip, ipv6=ipv6, port=port, username=username, password=password)


@register_tl
class PhoneCallProtocol(TLObject):
    ID: int = 0xfc878fc8

    def __init__(self, udp_p2p: bool = False, udp_reflector: bool = False, min_layer: Any = None, max_layer: Any = None, library_versions: Any = None) -> None:
        self.udp_p2p = udp_p2p
        self.udp_reflector = udp_reflector
        self.min_layer = min_layer
        self.max_layer = max_layer
        self.library_versions = library_versions

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.udp_p2p:
            flags |= (1 << 0)
        if self.udp_reflector:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_int32(self.min_layer or 0)
        writer.write_int32(self.max_layer or 0)
        writer.write_vector(self.library_versions or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'PhoneCallProtocol':
        flags = reader.read_uint32()
        udp_p2p = bool(flags & (1 << 0))
        udp_reflector = bool(flags & (1 << 1))
        min_layer = reader.read_int32()
        max_layer = reader.read_int32()
        library_versions = reader.read_vector(lambda r: r.read_string())
        return cls(udp_p2p=udp_p2p, udp_reflector=udp_reflector, min_layer=min_layer, max_layer=max_layer, library_versions=library_versions)


@register_tl
class PhonePhoneCall(TLObject):
    ID: int = 0xec82e140

    def __init__(self, phone_call: Any = None, users: Any = None) -> None:
        self.phone_call = phone_call
        self.users = users

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.phone_call is not None and hasattr(self.phone_call, 'write'): self.phone_call.write(writer)
        writer.write_vector(self.users or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'PhonePhoneCall':
        phone_call = reader.read_object()
        users = reader.read_vector(lambda r: reader.read_object())
        return cls(phone_call=phone_call, users=users)


@register_tl
class UploadCdnFileReuploadNeeded(TLObject):
    ID: int = 0xeea8e46e

    def __init__(self, request_token: Any = None) -> None:
        self.request_token = request_token

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.request_token or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadCdnFileReuploadNeeded':
        request_token = reader.read_bytes()
        return cls(request_token=request_token)


@register_tl
class UploadCdnFile(TLObject):
    ID: int = 0xa99fca4f

    def __init__(self, bytes: Any = None) -> None:
        self.bytes = bytes

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bytes(self.bytes or b'')

    @classmethod
    def read(cls, reader: TLReader) -> 'UploadCdnFile':
        bytes = reader.read_bytes()
        return cls(bytes=bytes)


@register_tl
class CdnPublicKey(TLObject):
    ID: int = 0xc982eaba

    def __init__(self, dc_id: Any = None, public_key: Any = None) -> None:
        self.dc_id = dc_id
        self.public_key = public_key

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.dc_id or 0)
        writer.write_string(self.public_key or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'CdnPublicKey':
        dc_id = reader.read_int32()
        public_key = reader.read_string()
        return cls(dc_id=dc_id, public_key=public_key)


@register_tl
class CdnConfig(TLObject):
    ID: int = 0x5725e40a

    def __init__(self, public_keys: Any = None) -> None:
        self.public_keys = public_keys

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.public_keys or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'CdnConfig':
        public_keys = reader.read_vector(lambda r: reader.read_object())
        return cls(public_keys=public_keys)


@register_tl
class LangPackString(TLObject):
    ID: int = 0xcad181f6

    def __init__(self, key: Any = None, value: Any = None) -> None:
        self.key = key
        self.value = value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.key or '')
        writer.write_string(self.value or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'LangPackString':
        key = reader.read_string()
        value = reader.read_string()
        return cls(key=key, value=value)


@register_tl
class LangPackStringPluralized(TLObject):
    ID: int = 0x6c47ac9f

    def __init__(self, zero_value: Any = None, one_value: Any = None, two_value: Any = None, few_value: Any = None, many_value: Any = None, key: Any = None, other_value: Any = None) -> None:
        self.zero_value = zero_value
        self.one_value = one_value
        self.two_value = two_value
        self.few_value = few_value
        self.many_value = many_value
        self.key = key
        self.other_value = other_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.zero_value is not None:
            flags |= (1 << 0)
        if self.one_value is not None:
            flags |= (1 << 1)
        if self.two_value is not None:
            flags |= (1 << 2)
        if self.few_value is not None:
            flags |= (1 << 3)
        if self.many_value is not None:
            flags |= (1 << 4)
        writer.write_uint32(flags)
        writer.write_string(self.key or '')
        if self.zero_value is not None:
            writer.write_string(self.zero_value or '')
        if self.one_value is not None:
            writer.write_string(self.one_value or '')
        if self.two_value is not None:
            writer.write_string(self.two_value or '')
        if self.few_value is not None:
            writer.write_string(self.few_value or '')
        if self.many_value is not None:
            writer.write_string(self.many_value or '')
        writer.write_string(self.other_value or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'LangPackStringPluralized':
        flags = reader.read_uint32()
        key = reader.read_string()
        zero_value = reader.read_string() if (flags & (1 << 0)) else None
        one_value = reader.read_string() if (flags & (1 << 1)) else None
        two_value = reader.read_string() if (flags & (1 << 2)) else None
        few_value = reader.read_string() if (flags & (1 << 3)) else None
        many_value = reader.read_string() if (flags & (1 << 4)) else None
        other_value = reader.read_string()
        return cls(key=key, zero_value=zero_value, one_value=one_value, two_value=two_value, few_value=few_value, many_value=many_value, other_value=other_value)


@register_tl
class LangPackStringDeleted(TLObject):
    ID: int = 0x2979eeb2

    def __init__(self, key: Any = None) -> None:
        self.key = key

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.key or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'LangPackStringDeleted':
        key = reader.read_string()
        return cls(key=key)


@register_tl
class LangPackDifference(TLObject):
    ID: int = 0xf385c1f6

    def __init__(self, lang_code: Any = None, from_version: Any = None, version: Any = None, strings: Any = None) -> None:
        self.lang_code = lang_code
        self.from_version = from_version
        self.version = version
        self.strings = strings

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.lang_code or '')
        writer.write_int32(self.from_version or 0)
        writer.write_int32(self.version or 0)
        writer.write_vector(self.strings or [], lambda w, x: x.write(w) if hasattr(x, 'write') else None)

    @classmethod
    def read(cls, reader: TLReader) -> 'LangPackDifference':
        lang_code = reader.read_string()
        from_version = reader.read_int32()
        version = reader.read_int32()
        strings = reader.read_vector(lambda r: reader.read_object())
        return cls(lang_code=lang_code, from_version=from_version, version=version, strings=strings)


@register_tl
class LangPackLanguage(TLObject):
    ID: int = 0xeeca5ce3

    def __init__(self, official: bool = False, rtl: bool = False, beta: bool = False, base_lang_code: Any = None, name: Any = None, native_name: Any = None, lang_code: Any = None, plural_code: Any = None, strings_count: Any = None, translated_count: Any = None, translations_url: Any = None) -> None:
        self.official = official
        self.rtl = rtl
        self.beta = beta
        self.base_lang_code = base_lang_code
        self.name = name
        self.native_name = native_name
        self.lang_code = lang_code
        self.plural_code = plural_code
        self.strings_count = strings_count
        self.translated_count = translated_count
        self.translations_url = translations_url

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.official:
            flags |= (1 << 0)
        if self.rtl:
            flags |= (1 << 2)
        if self.beta:
            flags |= (1 << 3)
        if self.base_lang_code is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        writer.write_string(self.name or '')
        writer.write_string(self.native_name or '')
        writer.write_string(self.lang_code or '')
        if self.base_lang_code is not None:
            writer.write_string(self.base_lang_code or '')
        writer.write_string(self.plural_code or '')
        writer.write_int32(self.strings_count or 0)
        writer.write_int32(self.translated_count or 0)
        writer.write_string(self.translations_url or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'LangPackLanguage':
        flags = reader.read_uint32()
        official = bool(flags & (1 << 0))
        rtl = bool(flags & (1 << 2))
        beta = bool(flags & (1 << 3))
        name = reader.read_string()
        native_name = reader.read_string()
        lang_code = reader.read_string()
        base_lang_code = reader.read_string() if (flags & (1 << 1)) else None
        plural_code = reader.read_string()
        strings_count = reader.read_int32()
        translated_count = reader.read_int32()
        translations_url = reader.read_string()
        return cls(official=official, rtl=rtl, beta=beta, name=name, native_name=native_name, lang_code=lang_code, base_lang_code=base_lang_code, plural_code=plural_code, strings_count=strings_count, translated_count=translated_count, translations_url=translations_url)


@register_tl
class ChannelAdminLogEventActionChangeTitle(TLObject):
    ID: int = 0xe6dfb825

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.prev_value or '')
        writer.write_string(self.new_value or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeTitle':
        prev_value = reader.read_string()
        new_value = reader.read_string()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeAbout(TLObject):
    ID: int = 0x55188a2e

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.prev_value or '')
        writer.write_string(self.new_value or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeAbout':
        prev_value = reader.read_string()
        new_value = reader.read_string()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeUsername(TLObject):
    ID: int = 0x6a4afc38

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_string(self.prev_value or '')
        writer.write_string(self.new_value or '')

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeUsername':
        prev_value = reader.read_string()
        new_value = reader.read_string()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangePhoto(TLObject):
    ID: int = 0x434bd2af

    def __init__(self, prev_photo: Any = None, new_photo: Any = None) -> None:
        self.prev_photo = prev_photo
        self.new_photo = new_photo

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_photo is not None and hasattr(self.prev_photo, 'write'): self.prev_photo.write(writer)
        if self.new_photo is not None and hasattr(self.new_photo, 'write'): self.new_photo.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangePhoto':
        prev_photo = reader.read_object()
        new_photo = reader.read_object()
        return cls(prev_photo=prev_photo, new_photo=new_photo)


@register_tl
class ChannelAdminLogEventActionToggleInvites(TLObject):
    ID: int = 0x1b7907ae

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleInvites':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionToggleSignatures(TLObject):
    ID: int = 0x26ae0971

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleSignatures':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionUpdatePinned(TLObject):
    ID: int = 0xe9e82c18

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionUpdatePinned':
        message = reader.read_object()
        return cls(message=message)


@register_tl
class ChannelAdminLogEventActionEditMessage(TLObject):
    ID: int = 0x709b2405

    def __init__(self, prev_message: Any = None, new_message: Any = None) -> None:
        self.prev_message = prev_message
        self.new_message = new_message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_message is not None and hasattr(self.prev_message, 'write'): self.prev_message.write(writer)
        if self.new_message is not None and hasattr(self.new_message, 'write'): self.new_message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionEditMessage':
        prev_message = reader.read_object()
        new_message = reader.read_object()
        return cls(prev_message=prev_message, new_message=new_message)


@register_tl
class ChannelAdminLogEventActionDeleteMessage(TLObject):
    ID: int = 0x42e047bb

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionDeleteMessage':
        message = reader.read_object()
        return cls(message=message)


@register_tl
class ChannelAdminLogEventActionParticipantJoin(TLObject):
    ID: int = 0x183040d3

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantJoin':
        return cls()


@register_tl
class ChannelAdminLogEventActionParticipantLeave(TLObject):
    ID: int = 0xf89777f2

    def __init__(self) -> None:
        pass

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantLeave':
        return cls()


@register_tl
class ChannelAdminLogEventActionParticipantInvite(TLObject):
    ID: int = 0xe31c34d8

    def __init__(self, participant: Any = None) -> None:
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantInvite':
        participant = reader.read_object()
        return cls(participant=participant)


@register_tl
class ChannelAdminLogEventActionParticipantToggleBan(TLObject):
    ID: int = 0xe6d83d7e

    def __init__(self, prev_participant: Any = None, new_participant: Any = None) -> None:
        self.prev_participant = prev_participant
        self.new_participant = new_participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_participant is not None and hasattr(self.prev_participant, 'write'): self.prev_participant.write(writer)
        if self.new_participant is not None and hasattr(self.new_participant, 'write'): self.new_participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantToggleBan':
        prev_participant = reader.read_object()
        new_participant = reader.read_object()
        return cls(prev_participant=prev_participant, new_participant=new_participant)


@register_tl
class ChannelAdminLogEventActionParticipantToggleAdmin(TLObject):
    ID: int = 0xd5676710

    def __init__(self, prev_participant: Any = None, new_participant: Any = None) -> None:
        self.prev_participant = prev_participant
        self.new_participant = new_participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_participant is not None and hasattr(self.prev_participant, 'write'): self.prev_participant.write(writer)
        if self.new_participant is not None and hasattr(self.new_participant, 'write'): self.new_participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantToggleAdmin':
        prev_participant = reader.read_object()
        new_participant = reader.read_object()
        return cls(prev_participant=prev_participant, new_participant=new_participant)


@register_tl
class ChannelAdminLogEventActionChangeStickerSet(TLObject):
    ID: int = 0xb1c3caa7

    def __init__(self, prev_stickerset: Any = None, new_stickerset: Any = None) -> None:
        self.prev_stickerset = prev_stickerset
        self.new_stickerset = new_stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_stickerset is not None and hasattr(self.prev_stickerset, 'write'): self.prev_stickerset.write(writer)
        if self.new_stickerset is not None and hasattr(self.new_stickerset, 'write'): self.new_stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeStickerSet':
        prev_stickerset = reader.read_object()
        new_stickerset = reader.read_object()
        return cls(prev_stickerset=prev_stickerset, new_stickerset=new_stickerset)


@register_tl
class ChannelAdminLogEventActionTogglePreHistoryHidden(TLObject):
    ID: int = 0x5f5c95f1

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionTogglePreHistoryHidden':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionDefaultBannedRights(TLObject):
    ID: int = 0x2df5fc0a

    def __init__(self, prev_banned_rights: Any = None, new_banned_rights: Any = None) -> None:
        self.prev_banned_rights = prev_banned_rights
        self.new_banned_rights = new_banned_rights

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_banned_rights is not None and hasattr(self.prev_banned_rights, 'write'): self.prev_banned_rights.write(writer)
        if self.new_banned_rights is not None and hasattr(self.new_banned_rights, 'write'): self.new_banned_rights.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionDefaultBannedRights':
        prev_banned_rights = reader.read_object()
        new_banned_rights = reader.read_object()
        return cls(prev_banned_rights=prev_banned_rights, new_banned_rights=new_banned_rights)


@register_tl
class ChannelAdminLogEventActionStopPoll(TLObject):
    ID: int = 0x8f079643

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionStopPoll':
        message = reader.read_object()
        return cls(message=message)


@register_tl
class ChannelAdminLogEventActionChangeLinkedChat(TLObject):
    ID: int = 0x50c7ac8

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int64(self.prev_value or 0)
        writer.write_int64(self.new_value or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeLinkedChat':
        prev_value = reader.read_int64()
        new_value = reader.read_int64()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeLocation(TLObject):
    ID: int = 0xe6b76ae

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_value is not None and hasattr(self.prev_value, 'write'): self.prev_value.write(writer)
        if self.new_value is not None and hasattr(self.new_value, 'write'): self.new_value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeLocation':
        prev_value = reader.read_object()
        new_value = reader.read_object()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionToggleSlowMode(TLObject):
    ID: int = 0x53909779

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.prev_value or 0)
        writer.write_int32(self.new_value or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleSlowMode':
        prev_value = reader.read_int32()
        new_value = reader.read_int32()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionStartGroupCall(TLObject):
    ID: int = 0x23209745

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionStartGroupCall':
        call = reader.read_object()
        return cls(call=call)


@register_tl
class ChannelAdminLogEventActionDiscardGroupCall(TLObject):
    ID: int = 0xdb9f9140

    def __init__(self, call: Any = None) -> None:
        self.call = call

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.call is not None and hasattr(self.call, 'write'): self.call.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionDiscardGroupCall':
        call = reader.read_object()
        return cls(call=call)


@register_tl
class ChannelAdminLogEventActionParticipantMute(TLObject):
    ID: int = 0xf92424d2

    def __init__(self, participant: Any = None) -> None:
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantMute':
        participant = reader.read_object()
        return cls(participant=participant)


@register_tl
class ChannelAdminLogEventActionParticipantUnmute(TLObject):
    ID: int = 0xe64429c0

    def __init__(self, participant: Any = None) -> None:
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantUnmute':
        participant = reader.read_object()
        return cls(participant=participant)


@register_tl
class ChannelAdminLogEventActionToggleGroupCallSetting(TLObject):
    ID: int = 0x56d6a247

    def __init__(self, join_muted: Any = None) -> None:
        self.join_muted = join_muted

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.join_muted))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleGroupCallSetting':
        join_muted = reader.read_bool()
        return cls(join_muted=join_muted)


@register_tl
class ChannelAdminLogEventActionParticipantJoinByInvite(TLObject):
    ID: int = 0xfe9fc158

    def __init__(self, via_chatlist: bool = False, invite: Any = None) -> None:
        self.via_chatlist = via_chatlist
        self.invite = invite

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.via_chatlist:
            flags |= (1 << 0)
        writer.write_uint32(flags)
        if self.invite is not None and hasattr(self.invite, 'write'): self.invite.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantJoinByInvite':
        flags = reader.read_uint32()
        via_chatlist = bool(flags & (1 << 0))
        invite = reader.read_object()
        return cls(via_chatlist=via_chatlist, invite=invite)


@register_tl
class ChannelAdminLogEventActionExportedInviteDelete(TLObject):
    ID: int = 0x5a50fca4

    def __init__(self, invite: Any = None) -> None:
        self.invite = invite

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.invite is not None and hasattr(self.invite, 'write'): self.invite.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionExportedInviteDelete':
        invite = reader.read_object()
        return cls(invite=invite)


@register_tl
class ChannelAdminLogEventActionExportedInviteRevoke(TLObject):
    ID: int = 0x410a134e

    def __init__(self, invite: Any = None) -> None:
        self.invite = invite

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.invite is not None and hasattr(self.invite, 'write'): self.invite.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionExportedInviteRevoke':
        invite = reader.read_object()
        return cls(invite=invite)


@register_tl
class ChannelAdminLogEventActionExportedInviteEdit(TLObject):
    ID: int = 0xe90ebb59

    def __init__(self, prev_invite: Any = None, new_invite: Any = None) -> None:
        self.prev_invite = prev_invite
        self.new_invite = new_invite

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_invite is not None and hasattr(self.prev_invite, 'write'): self.prev_invite.write(writer)
        if self.new_invite is not None and hasattr(self.new_invite, 'write'): self.new_invite.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionExportedInviteEdit':
        prev_invite = reader.read_object()
        new_invite = reader.read_object()
        return cls(prev_invite=prev_invite, new_invite=new_invite)


@register_tl
class ChannelAdminLogEventActionParticipantVolume(TLObject):
    ID: int = 0x3e7f6847

    def __init__(self, participant: Any = None) -> None:
        self.participant = participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.participant is not None and hasattr(self.participant, 'write'): self.participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantVolume':
        participant = reader.read_object()
        return cls(participant=participant)


@register_tl
class ChannelAdminLogEventActionChangeHistoryTTL(TLObject):
    ID: int = 0x6e941a38

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_int32(self.prev_value or 0)
        writer.write_int32(self.new_value or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeHistoryTTL':
        prev_value = reader.read_int32()
        new_value = reader.read_int32()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionParticipantJoinByRequest(TLObject):
    ID: int = 0xafb6144a

    def __init__(self, invite: Any = None, approved_by: Any = None) -> None:
        self.invite = invite
        self.approved_by = approved_by

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.invite is not None and hasattr(self.invite, 'write'): self.invite.write(writer)
        writer.write_int64(self.approved_by or 0)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantJoinByRequest':
        invite = reader.read_object()
        approved_by = reader.read_int64()
        return cls(invite=invite, approved_by=approved_by)


@register_tl
class ChannelAdminLogEventActionToggleNoForwards(TLObject):
    ID: int = 0xcb2ac766

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleNoForwards':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionSendMessage(TLObject):
    ID: int = 0x278f2868

    def __init__(self, message: Any = None) -> None:
        self.message = message

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.message is not None and hasattr(self.message, 'write'): self.message.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionSendMessage':
        message = reader.read_object()
        return cls(message=message)


@register_tl
class ChannelAdminLogEventActionChangeAvailableReactions(TLObject):
    ID: int = 0xbe4e0ef8

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_value is not None and hasattr(self.prev_value, 'write'): self.prev_value.write(writer)
        if self.new_value is not None and hasattr(self.new_value, 'write'): self.new_value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeAvailableReactions':
        prev_value = reader.read_object()
        new_value = reader.read_object()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeUsernames(TLObject):
    ID: int = 0xf04fb3a9

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_vector(self.prev_value or [], lambda w, x: w.write_string(x))
        writer.write_vector(self.new_value or [], lambda w, x: w.write_string(x))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeUsernames':
        prev_value = reader.read_vector(lambda r: r.read_string())
        new_value = reader.read_vector(lambda r: r.read_string())
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionToggleForum(TLObject):
    ID: int = 0x2cc6383

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleForum':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionCreateTopic(TLObject):
    ID: int = 0x58707d28

    def __init__(self, topic: Any = None) -> None:
        self.topic = topic

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.topic is not None and hasattr(self.topic, 'write'): self.topic.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionCreateTopic':
        topic = reader.read_object()
        return cls(topic=topic)


@register_tl
class ChannelAdminLogEventActionEditTopic(TLObject):
    ID: int = 0xf06fe208

    def __init__(self, prev_topic: Any = None, new_topic: Any = None) -> None:
        self.prev_topic = prev_topic
        self.new_topic = new_topic

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_topic is not None and hasattr(self.prev_topic, 'write'): self.prev_topic.write(writer)
        if self.new_topic is not None and hasattr(self.new_topic, 'write'): self.new_topic.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionEditTopic':
        prev_topic = reader.read_object()
        new_topic = reader.read_object()
        return cls(prev_topic=prev_topic, new_topic=new_topic)


@register_tl
class ChannelAdminLogEventActionDeleteTopic(TLObject):
    ID: int = 0xae168909

    def __init__(self, topic: Any = None) -> None:
        self.topic = topic

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.topic is not None and hasattr(self.topic, 'write'): self.topic.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionDeleteTopic':
        topic = reader.read_object()
        return cls(topic=topic)


@register_tl
class ChannelAdminLogEventActionPinTopic(TLObject):
    ID: int = 0x5d8d353b

    def __init__(self, prev_topic: Any = None, new_topic: Any = None) -> None:
        self.prev_topic = prev_topic
        self.new_topic = new_topic

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        flags = 0
        if self.prev_topic is not None:
            flags |= (1 << 0)
        if self.new_topic is not None:
            flags |= (1 << 1)
        writer.write_uint32(flags)
        if self.prev_topic is not None:
            if self.prev_topic is not None and hasattr(self.prev_topic, 'write'): self.prev_topic.write(writer)
        if self.new_topic is not None:
            if self.new_topic is not None and hasattr(self.new_topic, 'write'): self.new_topic.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionPinTopic':
        flags = reader.read_uint32()
        prev_topic = reader.read_object() if (flags & (1 << 0)) else None
        new_topic = reader.read_object() if (flags & (1 << 1)) else None
        return cls(prev_topic=prev_topic, new_topic=new_topic)


@register_tl
class ChannelAdminLogEventActionToggleAntiSpam(TLObject):
    ID: int = 0x64f36dfc

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleAntiSpam':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangePeerColor(TLObject):
    ID: int = 0x5796e780

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_value is not None and hasattr(self.prev_value, 'write'): self.prev_value.write(writer)
        if self.new_value is not None and hasattr(self.new_value, 'write'): self.new_value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangePeerColor':
        prev_value = reader.read_object()
        new_value = reader.read_object()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeProfilePeerColor(TLObject):
    ID: int = 0x5e477b25

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_value is not None and hasattr(self.prev_value, 'write'): self.prev_value.write(writer)
        if self.new_value is not None and hasattr(self.new_value, 'write'): self.new_value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeProfilePeerColor':
        prev_value = reader.read_object()
        new_value = reader.read_object()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeWallpaper(TLObject):
    ID: int = 0x31bb5d52

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_value is not None and hasattr(self.prev_value, 'write'): self.prev_value.write(writer)
        if self.new_value is not None and hasattr(self.new_value, 'write'): self.new_value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeWallpaper':
        prev_value = reader.read_object()
        new_value = reader.read_object()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeEmojiStatus(TLObject):
    ID: int = 0x3ea9feb1

    def __init__(self, prev_value: Any = None, new_value: Any = None) -> None:
        self.prev_value = prev_value
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_value is not None and hasattr(self.prev_value, 'write'): self.prev_value.write(writer)
        if self.new_value is not None and hasattr(self.new_value, 'write'): self.new_value.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeEmojiStatus':
        prev_value = reader.read_object()
        new_value = reader.read_object()
        return cls(prev_value=prev_value, new_value=new_value)


@register_tl
class ChannelAdminLogEventActionChangeEmojiStickerSet(TLObject):
    ID: int = 0x46d840ab

    def __init__(self, prev_stickerset: Any = None, new_stickerset: Any = None) -> None:
        self.prev_stickerset = prev_stickerset
        self.new_stickerset = new_stickerset

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_stickerset is not None and hasattr(self.prev_stickerset, 'write'): self.prev_stickerset.write(writer)
        if self.new_stickerset is not None and hasattr(self.new_stickerset, 'write'): self.new_stickerset.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionChangeEmojiStickerSet':
        prev_stickerset = reader.read_object()
        new_stickerset = reader.read_object()
        return cls(prev_stickerset=prev_stickerset, new_stickerset=new_stickerset)


@register_tl
class ChannelAdminLogEventActionToggleSignatureProfiles(TLObject):
    ID: int = 0x60a79c79

    def __init__(self, new_value: Any = None) -> None:
        self.new_value = new_value

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        writer.write_bool(bool(self.new_value))

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionToggleSignatureProfiles':
        new_value = reader.read_bool()
        return cls(new_value=new_value)


@register_tl
class ChannelAdminLogEventActionParticipantSubExtend(TLObject):
    ID: int = 0x64642db3

    def __init__(self, prev_participant: Any = None, new_participant: Any = None) -> None:
        self.prev_participant = prev_participant
        self.new_participant = new_participant

    def write(self, writer: TLWriter) -> None:
        writer.write_uint32(self.ID)
        if self.prev_participant is not None and hasattr(self.prev_participant, 'write'): self.prev_participant.write(writer)
        if self.new_participant is not None and hasattr(self.new_participant, 'write'): self.new_participant.write(writer)

    @classmethod
    def read(cls, reader: TLReader) -> 'ChannelAdminLogEventActionParticipantSubExtend':
        prev_participant = reader.read_object()
        new_participant = reader.read_object()
        return cls(prev_participant=prev_participant, new_participant=new_participant)

