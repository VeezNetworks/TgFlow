import unittest
from tgflow import (
    F,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    LinkPreviewOptions,
    MessageQuote,
    TgFlow,
    When,
    blockquote,
    bold,
    custom_emoji,
    spoiler,
)
from tgflow.tl.types import Chat, Message, User


class TestRichEphemeralQuotes(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = TgFlow(api_id=123456, api_hash="abcdef0123456789")
        await self.client.start(bot_token="123456:ABC-DEF")

    async def asyncTearDown(self):
        await self.client.stop()

    def test_rich_formatting_helpers(self):
        self.assertEqual(bold("hello"), "<b>hello</b>")
        self.assertEqual(spoiler("secret"), "<tg-spoiler>secret</tg-spoiler>")
        self.assertIn("tg-emoji", custom_emoji("star", emoji_id="5368324170671202286"))

        # Collapsible / Expandable blockquote (Layer 180–225)
        collapsed_bq = blockquote("Long legal disclaimer text...", expandable=True)
        self.assertIn('expandable="true"', collapsed_bq)
        self.assertIn("blockquote", collapsed_bq)

    def test_rich_keyboards_copy_text(self):
        # 1-Click Copy Text button (Layer 210+)
        btn = InlineKeyboardButton(text="Copy Referral Code", copy_text="REFERRAL_2026")
        self.assertEqual(btn.copy_text, "REFERRAL_2026")

        kb = InlineKeyboardMarkup().add_row(btn)
        self.assertEqual(len(kb.inline_keyboard), 1)

    async def test_quotes_functionality(self):
        # Send reply quoting specific text
        sent = await self.client.send_message(
            chat_id=12345,
            text="I agree with this specific point!",
            reply_to_message_id=99,
            quote_text="important sentence in original message",
            quote_offset=15,
        )
        self.assertIsNotNone(sent.quote)
        self.assertEqual(sent.quote.text, "important sentence in original message")
        self.assertEqual(sent.quote.position, 15)

    async def test_ephemeral_ttl_messages(self):
        # Send auto-deleting ephemeral message
        sent = await self.client.send_message(
            chat_id=12345,
            text="This OTP self-destructs in 30 seconds",
            ttl_period=30,
        )
        self.assertTrue(sent.is_ephemeral)
        self.assertEqual(sent.ttl_period, 30)

        # View-once media
        sent_vo = await self.client.send_message(
            chat_id=12345,
            text="Confidential media",
            is_view_once=True,
        )
        self.assertTrue(sent_vo.is_view_once)
        self.assertTrue(sent_vo.is_ephemeral)

    async def test_context_shortcuts_and_filters(self):
        chat = Chat(id=12345, type="supergroup")
        sender = User(id=999, first_name="Alice")
        msg = Message(
            id=10,
            chat=chat,
            sender=sender,
            text="Full user statement containing key details",
            quote=MessageQuote(text="key details"),
            ttl_period=60,
        )

        from tgflow.context import Context
        ctx = Context(msg, self.client)

        self.assertEqual(ctx.quote, "key details")
        self.assertTrue(ctx.is_ephemeral)

        # Reply with quote shortcut
        q_reply = await ctx.reply_quote("Understood!", quote_text="key details")
        self.assertEqual(q_reply.quote.text, "key details")

        # Reply with ephemeral shortcut
        e_reply = await ctx.reply_ephemeral("Quick secret", ttl=15)
        self.assertEqual(e_reply.ttl_period, 15)

        # Filter verification
        self.assertTrue(await When.Quote(self.client, msg))
        self.assertTrue(await F.ephemeral(self.client, msg))


if __name__ == "__main__":
    unittest.main()
