import asyncio
from typing import Any
import unittest
from tgflow import TgFlow, When, F
from tgflow.types import (
    Message,
    Chat,
    User,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Photo,
    Document,
    ChatPermissions,
)


class TestClient(unittest.TestCase):
    def test_client_init(self) -> None:
        client = TgFlow(session="test_session", api_id=12345, api_hash="abcdef", test_mode=True)
        self.assertEqual(client.api_id, 12345)
        self.assertEqual(client.api_hash, "abcdef")
        self.assertTrue(client.test_mode)

    def test_command_decorator(self) -> None:
        client = TgFlow(session="test_session")

        @client.command("start", when=When.private)
        async def on_start(cli: TgFlow, msg: Message) -> None:
            pass

        self.assertEqual(len(client._message_handlers), 1)
        handler = client._message_handlers[0]
        test_msg = Message(id=1, text="/start", chat=Chat(id=10, type="private"))
        self.assertTrue(handler.filter(client, test_msg))

        group_msg = Message(id=2, text="/start", chat=Chat(id=10, type="group"))
        self.assertFalse(handler.filter(client, group_msg))

    def test_callback_decorator(self) -> None:
        client = TgFlow(session="test_session")

        @client.callback("confirm")
        async def on_confirm(cli: TgFlow, query: Any) -> None:
            pass

        self.assertEqual(len(client._callback_handlers), 1)

    def test_methods_execution(self) -> None:
        client = TgFlow(session="test_session")

        async def run_methods() -> None:
            msg = await client.send_message(chat_id=123, text="Hello TgFlow")
            self.assertEqual(msg.text, "Hello TgFlow")

            edited = await client.edit_message_text(chat_id=123, message_id=msg.id, text="Updated")
            self.assertEqual(edited.text, "Updated")

            poll_msg = await client.send_poll(chat_id=123, question="Vote?", options=["Yes", "No"])
            self.assertIsNotNone(poll_msg.media)

            photo_msg = await client.send_photo(chat_id=123, photo="test.png", caption="Photo caption")
            self.assertEqual(photo_msg.caption, "Photo caption")

            perm = ChatPermissions(can_send_messages=True)
            res = await client.restrict_chat_member(chat_id=123, user_id=456, permissions=perm)
            self.assertTrue(res)

        asyncio.run(run_methods())


if __name__ == "__main__":
    unittest.main()
