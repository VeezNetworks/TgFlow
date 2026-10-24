import unittest
from tgflow.tl.core import TLWriter, TLReader
from tgflow.tl import types as tl


class TestTL(unittest.TestCase):
    def test_primitives(self) -> None:
        w = TLWriter()
        w.write_int32(-123)
        w.write_int64(9876543210)
        w.write_double(3.14159)
        w.write_string("hello telegram")
        w.write_bool(True)
        w.write_bool(False)

        r = TLReader(w.getvalue())
        self.assertEqual(r.read_int32(), -123)
        self.assertEqual(r.read_int64(), 9876543210)
        self.assertAlmostEqual(r.read_double(), 3.14159, places=4)
        self.assertEqual(r.read_string(), "hello telegram")
        self.assertTrue(r.read_bool())
        self.assertFalse(r.read_bool())

    def test_constructor_roundtrip(self) -> None:
        peer = tl.InputPeerUser(user_id=8888, access_hash=9999)
        raw = peer.to_bytes()
        r = TLReader(raw)
        recovered = r.read_object()
        self.assertIsInstance(recovered, tl.InputPeerUser)
        self.assertEqual(recovered.user_id, 8888)
        self.assertEqual(recovered.access_hash, 9999)

    def test_vector(self) -> None:
        w = TLWriter()
        items = [10, 20, 30]
        w.write_vector(items, lambda wr, x: wr.write_int32(x))

        r = TLReader(w.getvalue())
        recovered = r.read_vector(lambda rd: rd.read_int32())
        self.assertEqual(recovered, items)


if __name__ == "__main__":
    unittest.main()
