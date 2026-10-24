import os
import unittest
from tgflow.session import Session


class TestSession(unittest.TestCase):
    def test_export_and_import(self) -> None:
        ak = os.urandom(256)
        s = Session(dc_id=4, auth_key=ak, is_bot=True, user_id=987654)
        token = s.export_string()
        self.assertTrue(token.startswith("tgflow_live_"))

        s2 = Session.from_string(token)
        self.assertEqual(s2.dc_id, 4)
        self.assertEqual(s2.auth_key, ak)
        self.assertTrue(s2.is_bot)
        self.assertEqual(s2.user_id, 987654)

    def test_crc_tamper(self) -> None:
        ak = os.urandom(256)
        s = Session(dc_id=2, auth_key=ak)
        token = s.export_string()
        tampered = token[:-2] + "AA"
        with self.assertRaises(Exception):
            Session.from_string(tampered)


if __name__ == "__main__":
    unittest.main()
