import unittest
from tgflow import (
    TgFlow,
    RichText,
    AIComposer,
    EphemeralMessage,
    RPCError,
    FloodWait,
    SlowmodeWait,
    PeerIdInvalid,
    PremiumAccountRequired,
    SessionPasswordNeeded,
    ChatWriteForbidden,
)
from tgflow.tl import types as tl


class TestErrorsAndRich(unittest.TestCase):
    def test_rpc_error_factory(self) -> None:
        err_flood = RPCError.from_rpc_error(420, "FLOOD_WAIT_45")
        self.assertIsInstance(err_flood, FloodWait)
        self.assertEqual(err_flood.value, 45)
        self.assertEqual(err_flood.seconds, 45)

        err_slow = RPCError.from_rpc_error(420, "SLOWMODE_WAIT_10")
        self.assertIsInstance(err_slow, SlowmodeWait)
        self.assertEqual(err_slow.value, 10)

        err_peer = RPCError.from_rpc_error(400, "PEER_ID_INVALID")
        self.assertIsInstance(err_peer, PeerIdInvalid)

        err_prem = RPCError.from_rpc_error(400, "PREMIUM_ACCOUNT_REQUIRED")
        self.assertIsInstance(err_prem, PremiumAccountRequired)

        err_pwd = RPCError.from_rpc_error(401, "SESSION_PASSWORD_NEEDED")
        self.assertIsInstance(err_pwd, SessionPasswordNeeded)

        err_perm = RPCError.from_rpc_error(403, "CHAT_WRITE_FORBIDDEN")
        self.assertIsInstance(err_perm, ChatWriteForbidden)

    def test_rich_text_builder(self) -> None:
        rich = (
            RichText("Hello ")
            .bold("World")
            .text("! Check out this ")
            .spoiler("secret code")
            .line()
            .blockquote("Expandable telegram quote", collapsed=True)
            .custom_emoji("🌟", emoji_id=987654321)
        )
        plain_text, entities = rich.build()
        self.assertIn("Hello World!", plain_text)
        self.assertIn("secret code", plain_text)
        self.assertIn("Expandable telegram quote", plain_text)
        self.assertEqual(len(entities), 4)

        self.assertIsInstance(entities[0], tl.MessageEntityBold)
        self.assertIsInstance(entities[1], tl.MessageEntitySpoiler)
        self.assertIsInstance(entities[2], tl.MessageEntityBlockquote)
        self.assertTrue(entities[2].collapsed)
        self.assertIsInstance(entities[3], tl.MessageEntityCustomEmoji)
        self.assertEqual(entities[3].document_id, 987654321)

    def test_ai_composer(self) -> None:
        draft = AIComposer.compose("Please join our community meeting. We will discuss updates.", tone="professional", bullet_points=True)
        self.assertIn("AI Draft", draft.plain_text)
        self.assertIn("• Please join our community meeting", draft.plain_text)

        summary = AIComposer.summarize("First point. Second point. Third point. Fourth point.", max_points=2)
        self.assertIn("Summary:", summary.plain_text)
        self.assertIn("1. First point", summary.plain_text)
        self.assertIn("2. Second point", summary.plain_text)

    def test_ephemeral_client_methods(self) -> None:
        client = TgFlow("test_session")
        self.assertTrue(callable(getattr(client, "send_ephemeral")))
        self.assertTrue(callable(getattr(client, "set_chat_ttl")))
        self.assertTrue(callable(getattr(client, "translate_text")))
        self.assertTrue(callable(getattr(client, "ai_compose")))

        ephemeral = EphemeralMessage("Temporary text", ttl_seconds=15)
        self.assertEqual(ephemeral.ttl_seconds, 15)
        self.assertEqual(ephemeral.to_dict()["ttl_seconds"], 15)


if __name__ == "__main__":
    unittest.main()
