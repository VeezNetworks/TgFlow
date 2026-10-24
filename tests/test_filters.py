import unittest
from tgflow import filters
from tgflow.types.message import Message
from tgflow.types.chat import Chat
from tgflow.types.user import User


class TestFilters(unittest.TestCase):
    def test_text_filter(self) -> None:
        msg = Message(id=1, text="Hello world")
        self.assertTrue(filters.text(None, msg))

        empty_msg = Message(id=2, text="")
        self.assertFalse(filters.text(None, empty_msg))

    def test_command_filter(self) -> None:
        f = filters.command(["start", "help"])
        msg1 = Message(id=1, text="/start bot_arg")
        self.assertTrue(f(None, msg1))
        self.assertEqual(msg1.command, ["start", "bot_arg"])

        msg2 = Message(id=2, text="/stop")
        self.assertFalse(f(None, msg2))

    def test_regex_filter(self) -> None:
        f = filters.regex(r"^order_(\d+)$")
        msg = Message(id=1, text="order_999")
        self.assertTrue(f(None, msg))
        self.assertEqual(msg.matches[0].group(1), "999")

    def test_combinators(self) -> None:
        c1 = filters.command("ping")
        c2 = filters.private
        combined = c1 & c2
        msg = Message(id=1, text="/ping", chat=Chat(id=123, type="private"))
        self.assertTrue(combined(None, msg))

        inverted = ~c2
        self.assertFalse(inverted(None, msg))


if __name__ == "__main__":
    unittest.main()
