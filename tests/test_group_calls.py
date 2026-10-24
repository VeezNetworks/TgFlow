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

    def test_client_group_call_resolver(self) -> None:
        client = TgFlow(session="test_session")
        resolved = client._resolve_group_call((12345, 67890))
        self.assertIsInstance(resolved, tl.InputGroupCall)
        self.assertEqual(resolved.id, 12345)
        self.assertEqual(resolved.access_hash, 67890)


if __name__ == "__main__":
    unittest.main()
