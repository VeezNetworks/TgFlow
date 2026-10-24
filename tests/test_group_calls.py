import unittest
from tgflow import TgFlow, raw
from tgflow.tl import functions as fn, types as tl
from tgflow.types import GroupCall, GroupCallParticipant


class TestGroupCalls(unittest.TestCase):
    def test_tl_serialization(self) -> None:
        call = tl.InputGroupCall(id=1122334455, access_hash=9988776655)
        raw_bytes = call.to_bytes()
        from tgflow.tl.core import TLReader
        r = TLReader(raw_bytes)
        rec = r.read_object()
        self.assertIsInstance(rec, tl.InputGroupCall)
        self.assertEqual(rec.id, 1122334455)
        self.assertEqual(rec.access_hash, 9988776655)

    def test_raw_phone_imports(self) -> None:
        self.assertTrue(hasattr(raw.functions.phone, "JoinGroupCall"))
        self.assertTrue(hasattr(raw.functions.phone, "LeaveGroupCall"))
        self.assertTrue(hasattr(raw.functions.phone, "GetGroupCall"))
        self.assertTrue(hasattr(raw.functions.phone, "GetGroupParticipants"))
        self.assertTrue(hasattr(raw.functions.phone, "EditGroupCallParticipant"))
        self.assertTrue(hasattr(raw.functions.phone, "RequestCall"))
        self.assertTrue(hasattr(raw.functions.phone, "AcceptCall"))
        self.assertTrue(hasattr(raw.functions.phone, "ConfirmCall"))
        self.assertTrue(hasattr(raw.functions.phone, "DiscardCall"))

        join_req = raw.functions.phone.JoinGroupCall(
            call=tl.InputGroupCall(id=1, access_hash=2),
            join_as=tl.InputPeerSelf(),
            params=tl.DataJSON(data="{}"),
            muted=True,
        )
        self.assertEqual(join_req.ID, 0xB132FF7B)
        self.assertTrue(join_req.muted)

    def test_group_call_participant_serialization(self) -> None:
        part = tl.GroupCallParticipant(
            peer=tl.PeerUser(user_id=777),
            date=123456,
            source=54321,
            muted=True,
            volume=15000,
        )
        data = part.to_bytes()
        from tgflow.tl.core import TLReader
        r = TLReader(data)
        rec = r.read_object()
        self.assertIsInstance(rec, tl.GroupCallParticipant)
        self.assertTrue(rec.muted)
        self.assertEqual(rec.source, 54321)
        self.assertEqual(rec.volume, 15000)

    def test_phone_call_serialization(self) -> None:
        proto = tl.PhoneCallProtocol(min_layer=65, max_layer=225, udp_p2p=True, udp_reflector=True, library_versions=["1.0.0"])
        proto_bytes = proto.to_bytes()
        from tgflow.tl.core import TLReader
        r = TLReader(proto_bytes)
        rec = r.read_object()
        self.assertIsInstance(rec, tl.PhoneCallProtocol)
        self.assertEqual(rec.min_layer, 65)
        self.assertEqual(rec.max_layer, 225)
        self.assertTrue(rec.udp_p2p)
        self.assertEqual(rec.library_versions, ["1.0.0"])

        phone_call = tl.InputPhoneCall(id=987654321, access_hash=123456789)
        pc_bytes = phone_call.to_bytes()
        r2 = TLReader(pc_bytes)
        rec2 = r2.read_object()
        self.assertIsInstance(rec2, tl.InputPhoneCall)
        self.assertEqual(rec2.id, 987654321)
        self.assertEqual(rec2.access_hash, 123456789)

    def test_request_and_confirm_call_rpc(self) -> None:
        proto = tl.PhoneCallProtocol(min_layer=65, max_layer=225, udp_p2p=True, udp_reflector=True, library_versions=["1.0.0"])
        req = raw.functions.phone.RequestCall(
            user_id=tl.InputUser(user_id=123, access_hash=456),
            random_id=999,
            g_a_hash=b"dummy_hash_32_bytes_long_exact!",
            protocol=proto,
            video=True,
        )
        data = req.to_bytes()
        from tgflow.tl.core import TLReader
        r = TLReader(data)
        decoded = r.read_object()
        self.assertIsInstance(decoded, raw.functions.phone.RequestCall)
        self.assertTrue(decoded.video)
        self.assertEqual(decoded.random_id, 999)

    def test_client_call_resolvers(self) -> None:
        client = TgFlow(session="test_session")
        resolved_gc = client._resolve_group_call((12345, 67890))
        self.assertIsInstance(resolved_gc, tl.InputGroupCall)
        self.assertEqual(resolved_gc.id, 12345)
        self.assertEqual(resolved_gc.access_hash, 67890)

        resolved_pc = client._resolve_phone_call((54321, 98765))
        self.assertIsInstance(resolved_pc, tl.InputPhoneCall)
        self.assertEqual(resolved_pc.id, 54321)
        self.assertEqual(resolved_pc.access_hash, 98765)

        self.assertTrue(callable(getattr(client, "request_call")))
        self.assertTrue(callable(getattr(client, "accept_call")))
        self.assertTrue(callable(getattr(client, "confirm_call")))
        self.assertTrue(callable(getattr(client, "discard_call")))
        self.assertTrue(callable(getattr(client, "invite_to_group_call")))


if __name__ == "__main__":
    unittest.main()
