import unittest
from tgflow import (
    LAYER,
    TgFlow,
    PaidReaction,
    StarSubscription,
    StarsRevenueStatus,
    BusinessIntro,
    BusinessLocation,
    Gift,
)
from tgflow.raw.types import LAYER as RAW_LAYER
from tgflow.raw.functions import InvokeWithLayer, GetStarsRevenue, SendPaidReaction


class TestLayer225(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = TgFlow(api_id=123456, api_hash="abcdef0123456789")
        await self.client.start(bot_token="123456:ABC-DEF")

    async def asyncTearDown(self):
        await self.client.stop()

    def test_layer_constant(self):
        self.assertEqual(LAYER, 225)
        self.assertEqual(RAW_LAYER, 225)

    def test_raw_invoke_with_layer(self):
        invoke_req = InvokeWithLayer(
            layer=225,
            query=GetStarsRevenue(),
        )
        self.assertEqual(invoke_req.layer, 225)
        self.assertEqual(invoke_req.ID, 0xDA9B0D0D)

    async def test_layer_225_stars_and_monetization(self):
        # Paid reactions (Layer 225)
        reaction = await self.client.send_paid_reaction(
            chat_id=-100123456789,
            message_id=42,
            stars_count=50,
            is_anonymous=True,
        )
        self.assertIsInstance(reaction, PaidReaction)
        self.assertEqual(reaction.stars_count, 50)
        self.assertTrue(reaction.is_anonymous)

        # Stars revenue (Layer 225)
        rev = await self.client.get_stars_revenue()
        self.assertIsInstance(rev, StarsRevenueStatus)
        self.assertEqual(rev.current_balance, 2500)
        self.assertTrue(rev.can_withdraw)

        # Star subscriptions (Layer 225)
        subs = await self.client.get_star_subscriptions()
        self.assertGreater(len(subs), 0)
        self.assertEqual(subs[0].stars_amount, 250)

        # Upgraded & collectible gifts (Layer 225)
        upgraded_gifts = await self.client.get_upgraded_gifts()
        self.assertGreater(len(upgraded_gifts), 0)
        gift = upgraded_gifts[0]
        self.assertTrue(gift.is_upgraded)
        self.assertTrue(gift.is_limited)
        self.assertEqual(gift.gift_number, 42)

    async def test_layer_225_business_management(self):
        # Business intro
        intro = await self.client.set_business_intro(
            title="Official Veez Store",
            description="24/7 Digital Services",
        )
        self.assertIsInstance(intro, BusinessIntro)
        self.assertEqual(intro.title, "Official Veez Store")

        # Business location
        loc = await self.client.set_business_location(
            address="100 Tech Park Blvd",
            latitude=37.7749,
            longitude=-122.4194,
        )
        self.assertIsInstance(loc, BusinessLocation)
        self.assertEqual(loc.address, "100 Tech Park Blvd")


if __name__ == "__main__":
    unittest.main()
