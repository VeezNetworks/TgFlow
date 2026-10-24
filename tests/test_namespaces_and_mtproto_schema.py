import unittest
from tgflow import raw
from tgflow.tl import types as tl, functions as fn
from tgflow.tl.core import REGISTRY, TLReader, TLWriter


class TestNamespacesAndMtprotoSchema(unittest.TestCase):
    def test_all_24_raw_function_namespaces(self) -> None:
        namespaces = [
            "account",
            "aicompose",
            "auth",
            "bots",
            "channels",
            "chatlists",
            "contacts",
            "folders",
            "fragment",
            "help",
            "langpack",
            "messages",
            "payments",
            "phone",
            "photos",
            "premium",
            "smsjobs",
            "stats",
            "stickers",
            "stories",
            "updates",
            "upload",
            "users",
            "root",
        ]
        for ns in namespaces:
            self.assertTrue(
                hasattr(raw.functions, ns),
                f"Missing namespace {ns} in raw.functions",
            )

    def test_all_raw_type_namespaces(self) -> None:
        type_namespaces = [
            "account",
            "aicompose",
            "auth",
            "bots",
            "channels",
            "chatlists",
            "contacts",
            "fragment",
            "help",
            "messages",
            "payments",
            "phone",
            "photos",
            "premium",
            "smsjobs",
            "stats",
            "stickers",
            "storage",
            "stories",
            "updates",
            "upload",
            "users",
        ]
        for ns in type_namespaces:
            self.assertTrue(
                hasattr(raw.types, ns),
                f"Missing namespace {ns} in raw.types",
            )

    def test_mtproto_core_schema_functions(self) -> None:
        self.assertTrue(hasattr(fn, "ReqPqMulti"))
        self.assertTrue(hasattr(fn, "ReqDHParams"))
        self.assertTrue(hasattr(fn, "SetClientDHParams"))
        self.assertTrue(hasattr(fn, "RpcDropAnswer"))
        self.assertTrue(hasattr(fn, "GetFutureSalts"))
        self.assertTrue(hasattr(fn, "Ping"))
        self.assertTrue(hasattr(fn, "PingDelayDisconnect"))
        self.assertTrue(hasattr(fn, "DestroySession"))
        self.assertTrue(hasattr(fn, "DestroyAuthKey"))

        drop = fn.RpcDropAnswer(req_msg_id=12345678)
        b = drop.to_bytes()
        res = TLReader(b).read_object()
        self.assertEqual(res.req_msg_id, 12345678)

        salts_req = fn.GetFutureSalts(num=5)
        b2 = salts_req.to_bytes()
        res2 = TLReader(b2).read_object()
        self.assertEqual(res2.num, 5)

        destroy_s = fn.DestroySession(session_id=987654321)
        b3 = destroy_s.to_bytes()
        res3 = TLReader(b3).read_object()
        self.assertEqual(res3.session_id, 987654321)

    def test_mtproto_core_schema_types(self) -> None:
        salt = tl.FutureSalt(valid_since=1000, valid_until=2000, salt=55555)
        self.assertEqual(salt.valid_since, 1000)
        self.assertEqual(salt.valid_until, 2000)
        self.assertEqual(salt.salt, 55555)
        b = salt.to_bytes()
        res = TLReader(b).read_object()
        self.assertEqual(res.valid_since, 1000)
        self.assertEqual(res.salt, 55555)

        pong = tl.Pong(msg_id=111, ping_id=222)
        b_pong = pong.to_bytes()
        res_pong = TLReader(b_pong).read_object()
        self.assertEqual(res_pong.msg_id, 111)
        self.assertEqual(res_pong.ping_id, 222)

        bad_salt = tl.BadServerSalt(
            bad_msg_id=123,
            bad_msg_seqno=456,
            error_code=16,
            new_server_salt=999888,
        )
        b_bs = bad_salt.to_bytes()
        res_bs = TLReader(b_bs).read_object()
        self.assertEqual(res_bs.new_server_salt, 999888)

    def test_e2e_secret_chats_schema(self) -> None:
        self.assertTrue(hasattr(tl, "DecryptedMessage"))
        self.assertTrue(hasattr(tl, "DecryptedMessageActionSetMessageTTL"))
        self.assertTrue(hasattr(tl, "DecryptedMessageMediaPhoto"))

        ttl_action = tl.DecryptedMessageActionSetMessageTTL(ttl_seconds=30)
        self.assertEqual(ttl_action.ttl_seconds, 30)
        b = ttl_action.to_bytes()
        res = TLReader(b).read_object()
        self.assertEqual(res.ttl_seconds, 30)

    def test_root_invocation_wrappers(self) -> None:
        self.assertTrue(hasattr(raw.functions.root, "InitConnection"))
        self.assertTrue(hasattr(raw.functions.root, "InvokeWithLayer"))
        self.assertTrue(hasattr(raw.functions.root, "InvokeWithoutUpdates"))
        self.assertTrue(hasattr(raw.functions.root, "InvokeWithBusinessConnection"))
        self.assertTrue(hasattr(raw.functions.root, "InvokeWithReCaptcha"))


if __name__ == "__main__":
    unittest.main()
