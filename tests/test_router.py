import asyncio
import unittest
from tgflow.context import Context
from tgflow.router import Router, RouteTemplate
from tgflow.tl.types import Chat, Message, User


class TestRouter(unittest.TestCase):
    def test_route_template_matching(self):
        tmpl = RouteTemplate("/ban <target> <duration:int=60> <reason*>")

        # 1. Full text
        matched = tmpl.match("/ban @spammer 120 posting ads in chat")
        self.assertIsNotNone(matched)
        self.assertEqual(matched["target"], "@spammer")
        self.assertEqual(matched["duration"], 120)
        self.assertEqual(matched["reason"], "posting ads in chat")

        # 2. Defaults
        matched_default = tmpl.match("/ban @spammer")
        self.assertIsNotNone(matched_default)
        self.assertEqual(matched_default["target"], "@spammer")
        self.assertEqual(matched_default["duration"], 60)
        self.assertIsNone(matched_default["reason"])

    def test_replied_target_inference(self):
        tmpl = RouteTemplate("/ban <target> <duration:int=60>")
        replied_user = User(id=999, first_name="Offender")
        reply_msg = Message(id=1, chat=Chat(id=-100, type="supergroup"), sender=replied_user)

        # Message is just "/ban 30" (no target in text)
        matched = tmpl.match("/ban 30", reply_to=reply_msg)
        self.assertIsNotNone(matched)
        self.assertEqual(matched["target"].id, 999)
        self.assertEqual(matched["duration"], 30)

    def test_router_dispatch(self):
        router = Router()
        dispatched_payload = {}

        @router.on("/kick <target> <reason*>")
        async def kick_handler(ctx, target, reason):
            dispatched_payload["target"] = target
            dispatched_payload["reason"] = reason

        chat = Chat(id=10, type="group")
        sender = User(id=1, first_name="Admin")
        msg = Message(id=100, chat=chat, sender=sender, text="/kick @badguy violating rules")
        ctx = Context(msg, client=None)

        asyncio.run(router.dispatch(ctx))

        self.assertEqual(dispatched_payload["target"], "@badguy")
        self.assertEqual(dispatched_payload["reason"], "violating rules")


if __name__ == "__main__":
    unittest.main()
