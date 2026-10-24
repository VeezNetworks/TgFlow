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


if __name__ == "__main__":
    unittest.main()
