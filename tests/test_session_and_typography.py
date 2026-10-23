import unittest
from tgflow import F, TgFlow, When, decode_session, encode_session, generate_new_session
from tgflow.session import SessionData
from tgflow.tl.types import Chat, Message, User


class TestSessionAndTypography(unittest.IsolatedAsyncioTestCase):
    def test_unique_session_encoding_and_decoding(self):
        # Generate session
        token = generate_new_session(
            api_id=123456,
            user_id=987654321,
            dc_id=4,
            is_bot=False,
            test_mode=False,
        )

        self.assertTrue(token.startswith("tgflow_live_"))
        decoded = decode_session(token)

        self.assertEqual(decoded.api_id, 123456)
        self.assertEqual(decoded.user_id, 987654321)
        self.assertEqual(decoded.dc_id, 4)
        self.assertFalse(decoded.is_bot)
        self.assertFalse(decoded.test_mode)
        self.assertEqual(len(decoded.auth_key), 256)

        # Test corrupt session detection
        corrupted = token[:-2] + "AA"
        with self.assertRaises(ValueError):
            decode_session(corrupted)

        # Test test-mode token
        test_token = generate_new_session(
            api_id=999,
            user_id=111222,
            dc_id=2,
            is_bot=True,
            test_mode=True,
        )
        self.assertTrue(test_token.startswith("tgflow_test_"))
        dec_test = decode_session(test_token)
        self.assertTrue(dec_test.test_mode)
        self.assertTrue(dec_test.is_bot)

    async def test_client_session_bootstrap(self):
        token = generate_new_session(
            api_id=888999,
            user_id=444555,
            dc_id=1,
            is_bot=False,
            test_mode=False,
        )
        client = TgFlow(session=token)
        self.assertEqual(client.api_id, 888999)
        self.assertEqual(client.me_id, 444555)
        self.assertEqual(client.dc_id, 1)

        exported = client.export_session_string()
        self.assertTrue(exported.startswith("tgflow_live_"))
        dec_exp = decode_session(exported)
        self.assertEqual(dec_exp.api_id, 888999)
        self.assertEqual(dec_exp.user_id, 444555)

    async def test_when_and_f_typography(self):
        client = TgFlow(api_id=123, api_hash="abc")
        dispatched = []

        # Route using When typography
        @client.on(When.Command("ban") & When.Group)
        async def on_ban(ctx):
            dispatched.append("ban")

        # Route using F typography
        @client.on(F.command("start") & F.private)
        async def on_start(ctx):
            dispatched.append("start")

        # Route using modern features typography
        @client.on(When.Stars & When.Private)
        async def on_stars(ctx):
            dispatched.append("stars")

        chat_group = Chat(id=-100123, type="supergroup")
        chat_private = Chat(id=456, type="private")
        sender = User(id=789, first_name="Test")

        # Ban message in group
        msg_ban = Message(id=1, chat=chat_group, sender=sender, text="/ban @user", raw={})
        from tgflow.context import Context
        await client.router.dispatch(Context(msg_ban, client))
        self.assertIn("ban", dispatched)

        # Start message in private
        msg_start = Message(id=2, chat=chat_private, sender=sender, text="/start", raw={})
        await client.router.dispatch(Context(msg_start, client))
        self.assertIn("start", dispatched)


if __name__ == "__main__":
    unittest.main()
