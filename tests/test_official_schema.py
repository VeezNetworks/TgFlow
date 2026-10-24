import unittest
from tgflow.tl import types as tl, functions as fn
from tgflow.tl.core import REGISTRY, TLReader, TLWriter


class TestOfficialSchemaAndMtproto(unittest.TestCase):
    def test_total_constructors_count(self) -> None:
        self.assertGreaterEqual(len(REGISTRY), 2300)

    def test_dice_scrolling_animation_schema(self) -> None:
        media_dice = tl.InputMediaDice(emoticon="🎰")
        self.assertEqual(media_dice.emoticon, "🎰")
        b = media_dice.to_bytes()
        r = TLReader(b)
        res = r.read_object()
        self.assertEqual(res.emoticon, "🎰")

        msg_dice = tl.MessageMediaDice(value=6, emoticon="🎯")
        b2 = msg_dice.to_bytes()
        r2 = TLReader(b2)
        res2 = r2.read_object()
        self.assertEqual(res2.value, 6)
        self.assertEqual(res2.emoticon, "🎯")

    def test_message_effects_and_reactions(self) -> None:
        eff_req = fn.MessagesGetAvailableEffects(hash=123456)
        self.assertEqual(eff_req.hash, 123456)
        b = eff_req.to_bytes()
        r = TLReader(b)
        res = r.read_object()
        self.assertEqual(res.hash, 123456)

        react_req = fn.MessagesGetAvailableReactions(hash=987654)
        self.assertEqual(react_req.hash, 987654)
        b2 = react_req.to_bytes()
        r2 = TLReader(b2)
        res2 = r2.read_object()
        self.assertEqual(res2.hash, 987654)

    def test_ai_compose_tones_schema(self) -> None:
        self.assertTrue(hasattr(tl, "AiComposeTone"))

    def test_schema_browser_peers_and_media(self) -> None:
        peer_user = tl.InputPeerUser(user_id=12345, access_hash=67890)
        self.assertEqual(peer_user.user_id, 12345)
        self.assertEqual(peer_user.access_hash, 67890)
        b = peer_user.to_bytes()
        res = TLReader(b).read_object()
        self.assertEqual(res.user_id, 12345)
        self.assertEqual(res.access_hash, 67890)

        peer_channel = tl.InputPeerChannel(channel_id=999888, access_hash=777666)
        b_ch = peer_channel.to_bytes()
        res_ch = TLReader(b_ch).read_object()
        self.assertEqual(res_ch.channel_id, 999888)
        self.assertEqual(res_ch.access_hash, 777666)

    def test_handshake_and_transport(self) -> None:
        req_pq = fn.ReqPqMulti(nonce=b"\x01" * 16)
        b = req_pq.to_bytes()
        res = TLReader(b).read_object()
        self.assertEqual(res.nonce, b"\x01" * 16)

        ping = fn.Ping(ping_id=123456789)
        b2 = ping.to_bytes()
        res2 = TLReader(b2).read_object()
        self.assertEqual(res2.ping_id, 123456789)


if __name__ == "__main__":
    unittest.main()
