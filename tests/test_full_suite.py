import asyncio
import unittest
from tgflow import TgFlow, filters, raw
from tgflow.tl.types import Chat, Message, User


class TestFullSuite(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = TgFlow(api_id=123456, api_hash="abcdef0123456789abcdef0123456789")
        await self.client.start(bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")

    async def asyncTearDown(self):
        await self.client.stop()

    def test_raw_tl_serialization(self):
        writer = raw.TLWriter()
        writer.write_int(42)
        writer.write_long(1234567890123)
        writer.write_string("hello tgflow")
        writer.write_bool(True)

        data = writer.getvalue()
        reader = raw.TLReader(data)

        self.assertEqual(reader.read_int(), 42)
        self.assertEqual(reader.read_long(), 1234567890123)
        self.assertEqual(reader.read_string(), "hello tgflow")
        self.assertTrue(reader.read_bool())

    def test_raw_functions_and_types(self):
        peer = raw.types.InputPeerUser(user_id=987654, access_hash=123456789)
        req = raw.functions.SendMessage(
            peer=peer,
            message="Test message from raw",
            random_id=999888,
        )

        writer = raw.TLWriter()
        req.write(writer)
        encoded = writer.getvalue()
        self.assertGreater(len(encoded), 0)

        # Topic creation
        topic_req = raw.functions.CreateForumTopic(
            channel=raw.types.InputPeerChannel(channel_id=100111222, access_hash=555),
            title="Dev Discussions",
            icon_color=0x6FB9F0,
        )
        writer2 = raw.TLWriter()
        topic_req.write(writer2)
        self.assertGreater(len(writer2.getvalue()), 0)

    async def test_filters_composition(self):
        # Construct test update
        chat = Chat(id=12345, type="private")
        sender = User(id=999, first_name="Alice", username="alice_test")
        msg = Message(id=1, chat=chat, sender=sender, text="/hello world", raw={})

        f_cmd = filters.command("hello")
        f_private = filters.private
        f_user = filters.user("alice_test")

        self.assertTrue(await f_cmd(self.client, msg))
        self.assertTrue(await f_private(self.client, msg))
        self.assertTrue(await f_user(self.client, msg))

        # Test & (and)
        comb_and = f_cmd & f_private & f_user
        self.assertTrue(await comb_and(self.client, msg))

        # Test | (or)
        f_group = filters.group
        comb_or = f_group | f_private
        self.assertTrue(await comb_or(self.client, msg))

        # Test ~ (invert)
        comb_not = ~filters.group
        self.assertTrue(await comb_not(self.client, msg))

    async def test_router_with_filters(self):
        dispatched = []

        @self.client.on(filters.command("ping") & filters.private)
        async def on_ping(ctx):
            dispatched.append("ping_received")

        # Process update matching filter
        chat = Chat(id=12345, type="private")
        sender = User(id=999, first_name="Alice")
        msg_ping = Message(id=1, chat=chat, sender=sender, text="/ping", raw={})

        from tgflow.context import Context
        ctx = Context(msg_ping, self.client)
        await self.client.router.dispatch(ctx)

        self.assertIn("ping_received", dispatched)

    async def test_full_client_methods(self):
        # Messaging
        sent = await self.client.send_message(chat_id=12345, text="Unit test message")
        self.assertEqual(sent.text, "Unit test message")
        self.assertGreater(sent.id, 0)

        edited = await self.client.edit_message_text(chat_id=12345, message_id=sent.id, text="Updated")
        self.assertEqual(edited.text, "Updated")

        forwarded = await self.client.forward_messages(chat_id=54321, from_chat_id=12345, message_ids=[sent.id])
        self.assertEqual(len(forwarded), 1)

        # Media methods
        photo_msg = await self.client.send_photo(chat_id=12345, photo=b"fakephoto", caption="Caption")
        self.assertEqual(photo_msg.text, "Caption")
        self.assertTrue(photo_msg.raw.get("photo"))

        doc_msg = await self.client.send_document(chat_id=12345, document=b"fakedoc", file_name="test.txt")
        self.assertTrue(doc_msg.raw.get("document"))

        dice_msg = await self.client.send_dice(chat_id=12345, emoji="🎯")
        self.assertEqual(dice_msg.raw.get("dice"), "🎯")

        # Telegram Stars
        stars_res = await self.client.send_stars(chat_id=12345, amount=100, purpose="Donation")
        self.assertTrue(stars_res["ok"])
        self.assertEqual(stars_res["stars_transferred"], 100)

        paid_media_msg = await self.client.send_paid_media(chat_id=12345, stars_amount=50, media=b"content")
        self.assertEqual(paid_media_msg.raw["paid_media"].stars_amount, 50)

        # Telegram Business
        biz = await self.client.get_business_connection("biz_connection_77")
        self.assertEqual(biz.id, "biz_connection_77")
        biz_msg = await self.client.send_business_message("biz_connection_77", 12345, "Hello business client")
        self.assertEqual(biz_msg.raw["business_connection_id"], "biz_connection_77")

        # Stories
        story = await self.client.post_story(chat_id=12345, media=b"storymedia", caption="My Day")
        self.assertEqual(story.caption, "My Day")
        self.assertTrue(await self.client.send_story_reaction(12345, story.id, "🔥"))

        # Forum Topics
        topic = await self.client.create_forum_topic(chat_id=-1001234567, title="General Discussions")
        self.assertEqual(topic.title, "General Discussions")
        self.assertTrue(await self.client.close_forum_topic(-1001234567, topic.id))

        # Gifts
        gift = await self.client.send_gift(user_id=12345, gift_id="gift_star_1")
        self.assertEqual(gift.id, "gift_star_1")
        gifts_list = await self.client.get_available_gifts()
        self.assertGreater(len(gifts_list), 0)

        # Admin & Members
        self.assertTrue(await self.client.ban_chat_member(12345, 999))
        self.assertTrue(await self.client.unban_chat_member(12345, 999))
        self.assertTrue(await self.client.set_chat_title(12345, "New Title"))

        # User & Profile
        me = await self.client.get_me()
        self.assertIsNotNone(me)
        self.assertTrue(self.client.export_session_string().startswith("tgflow_live_"))

    async def test_context_shortcuts(self):
        chat = Chat(id=12345, type="supergroup")
        sender = User(id=999, first_name="Bob")
        msg = Message(id=10, chat=chat, sender=sender, text="/action", raw={"message_thread_id": 42})

        from tgflow.context import Context
        ctx = Context(msg, self.client)

        reply_msg = await ctx.reply_text("Replying!")
        self.assertEqual(reply_msg.text, "Replying!")

        topic_reply = await ctx.reply_in_topic("In Topic!")
        self.assertEqual(topic_reply.raw.get("message_thread_id"), 42)

        self.assertTrue(await ctx.ban())
        self.assertTrue(await ctx.unban())
        self.assertTrue(await ctx.pin())
        self.assertTrue(await ctx.target(888).ban())


if __name__ == "__main__":
    unittest.main()
