import unittest
from tgflow import formatting


class TestFormatting(unittest.TestCase):
    def test_helpers(self) -> None:
        self.assertEqual(formatting.bold("hello"), "<b>hello</b>")
        self.assertEqual(formatting.italic("world"), "<i>world</i>")
        self.assertEqual(formatting.spoiler("hidden"), "<tg-spoiler>hidden</tg-spoiler>")
        self.assertEqual(formatting.blockquote("quote"), "<blockquote>quote</blockquote>")
        self.assertEqual(formatting.expandable_blockquote("expand"), "<blockquote expandable>expand</blockquote>")

    def test_parse_html(self) -> None:
        raw = "Hello <b>bold</b> and <tg-spoiler>secret</tg-spoiler> and <blockquote expandable>long text</blockquote>"
        text, entities = formatting.parse_html(raw)
        self.assertEqual(text, "Hello bold and secret and long text")
        self.assertEqual(len(entities), 3)
        self.assertEqual(entities[0].type, "bold")
        self.assertEqual(entities[1].type, "spoiler")
        self.assertEqual(entities[2].type, "expandable_blockquote")

    def test_parse_markdown(self) -> None:
        raw = "Hello **bold** and `code` and ||spoiler|| and [link](https://example.com)"
        text, entities = formatting.parse_markdown(raw)
        self.assertEqual(text, "Hello bold and code and spoiler and link")
        self.assertEqual(len(entities), 4)
        self.assertEqual(entities[0].type, "bold")
        self.assertEqual(entities[1].type, "code")
        self.assertEqual(entities[2].type, "spoiler")
        self.assertEqual(entities[3].type, "text_url")

    def test_utf16_offsets(self) -> None:
        raw = "🔥 **fire**"
        text, entities = formatting.parse_markdown(raw)
        self.assertEqual(entities[0].offset, 3)
        self.assertEqual(entities[0].length, 4)

    def test_unparse_html(self) -> None:
        raw = "Hello <b>bold</b> and <tg-spoiler>secret</tg-spoiler>"
        text, entities = formatting.parse_html(raw)
        rendered = formatting.unparse_html(text, entities)
        self.assertEqual(rendered, raw)

    def test_unparse_markdown(self) -> None:
        raw = "Hello **bold** and ||secret||"
        text, entities = formatting.parse_markdown(raw)
        rendered = formatting.unparse_markdown(text, entities)
        self.assertEqual(rendered, raw)


if __name__ == "__main__":
    unittest.main()
