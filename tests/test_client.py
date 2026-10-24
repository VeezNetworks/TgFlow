import unittest
from tgflow import TgFlow, filters
from tgflow.types.message import Message
from tgflow.types.chat import Chat


class TestClient(unittest.TestCase):
    def test_client_init(self) -> None:
        client = TgFlow(session="test_session", api_id=12345, api_hash="abcdef", test_mode=True)
        self.assertEqual(client.api_id, 12345)
        self.assertEqual(client.api_hash, "abcdef")
        self.assertTrue(client.test_mode)

    def test_handler_registration(self) -> None:
        client = TgFlow(session="test_session")

        @client.on_message(filters.command("start"))
        async def on_start(cli: TgFlow, msg: Message) -> None:
            pass

        self.assertEqual(len(client._message_handlers), 1)
        handler = client._message_handlers[0]
        test_msg = Message(id=1, text="/start", chat=Chat(id=10))
        self.assertTrue(handler.filter(client, test_msg))


if __name__ == "__main__":
    unittest.main()
