import unittest
from tgflow import TgFlow, GroupCall, PhoneCall


class TestCalls(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = TgFlow(api_id=123456, api_hash="abcdef0123456789")
        await self.client.start(bot_token="123456:ABC-DEF")

    async def asyncTearDown(self):
        await self.client.stop()

    async def test_group_calls_and_live_streams(self):
        # Create voice chat in supergroup
        group_call = await self.client.create_group_call(chat_id=-100123456789, title="Townhall Live")
        self.assertIsInstance(group_call, GroupCall)
        self.assertEqual(group_call.title, "Townhall Live")
        self.assertTrue(group_call.is_active)

        # Join call
        res = await group_call.join(muted=False)
        self.assertTrue(res["ok"])
        self.assertFalse(res["muted"])

        # Fetch participants
        participants = await group_call.get_participants()
        self.assertGreater(len(participants), 0)

        # Leave call
        self.assertTrue(await group_call.leave())

        # Video chat alias
        vc = await self.client.start_video_chat(chat_id=-100123456789, title="Video Stream")
        self.assertIsInstance(vc, GroupCall)
        self.assertTrue(await self.client.end_video_chat(chat_id=-100123456789))

    async def test_one_on_one_voip_calls(self):
        # Initiate private VoIP call
        call = await self.client.start_call(user_id=987654321, video=True)
        self.assertIsInstance(call, PhoneCall)
        self.assertTrue(call.is_video)
        self.assertEqual(call.state, "ringing")

        # Accept call
        self.assertTrue(await call.accept())
        self.assertEqual(call.state, "active")

        # Discard call
        self.assertTrue(await call.discard(reason="hangup"))
        self.assertEqual(call.state, "discarded")


if __name__ == "__main__":
    unittest.main()
