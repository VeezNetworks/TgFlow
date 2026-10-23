import asyncio
import unittest
from tgflow.tl.parser import TLParser
from tgflow.tl.types import (
    User,
    Chat,
    Message,
    BusinessConnection,
    StoryItem,
    PaidMedia,
    ForumTopic,
    Gift,
)
from tgflow.client import TgFlow
from tgflow.bridge import BridgeServer, BridgeClient


class TestTLAndBridge(unittest.IsolatedAsyncioTestCase):
    def test_tl_schema_parsing(self):
        sample_tl = """
        // Types
        user#8f3aa044 id:long first_name:string last_name:flags.0?string = User;
        message#76145363 flags:# id:int from_id:flags.8?Peer peer_id:Peer message:string = Message;
        
        ---functions---
        messages.sendMessage#983f26ae flags:# peer:InputPeer message:string random_id:long = Updates;
        """
        parser = TLParser()
        parser.parse_string(sample_tl)
        
        self.assertIn("user", parser.constructors)
        self.assertIn("message", parser.constructors)
        self.assertIn("messages.sendMessage", parser.functions)
        
        user_ctor = parser.constructors["user"]
        self.assertEqual(user_ctor.id, 0x8f3aa044)
        self.assertEqual(user_ctor.predicate, "user")
        self.assertEqual(len(user_ctor.params), 3)

    def test_modern_layer_types(self):
        biz = BusinessConnection(
            id="biz_123",
            user_id=987654321,
            dc_id=2,
            can_reply=True,
            is_disabled=False,
        )
        self.assertEqual(biz.user_id, 987654321)
        self.assertTrue(biz.can_reply)
        self.assertFalse(biz.is_disabled)

        gift = Gift(id="gift_1", stars_cost=50, slug="star_gift")
        self.assertEqual(gift.stars_cost, 50)
        self.assertEqual(gift.slug, "star_gift")

        paid_media = PaidMedia(stars_amount=25, media_type="photo")
        self.assertEqual(paid_media.stars_amount, 25)
        self.assertEqual(paid_media.media_type, "photo")

        topic = ForumTopic(id=42, title="General", icon_color=0x6FB9F0)
        self.assertEqual(topic.title, "General")
        self.assertEqual(topic.id, 42)

    async def test_bridge_rpc_dispatch(self):
        client = TgFlow(api_id=123456, api_hash="0123456789abcdef0123456789abcdef")
        bridge = BridgeServer(client, host="127.0.0.1", port=19876)
        await bridge.start()

        rpc_client = BridgeClient(host="127.0.0.1", port=19876)
        await rpc_client.connect()

        # Send test message call through bridge
        resp = await rpc_client.call(
            "sendMessage",
            chat_id=12345,
            text="Hello from IPC bridge test!",
        )
        self.assertTrue(resp.get("ok"))
        self.assertEqual(resp.get("chat_id"), 12345)
        self.assertEqual(resp.get("text"), "Hello from IPC bridge test!")

        # Test error handling
        with self.assertRaises(RuntimeError):
            await rpc_client.call("nonExistentMethod")

        await rpc_client.close()
        await bridge.stop()


if __name__ == "__main__":
    unittest.main()
