import unittest
from tgflow import TgFlow, raw
from tgflow.tl import functions as fn, types as tl
from tgflow.tl.core import TLReader


class TestAuthAndMethods(unittest.TestCase):
    def test_send_code_serialization(self) -> None:
        settings = tl.CodeSettings(allow_flashcall=True, current_number=True, allow_app_hash=True)
        req = fn.SendCode(phone_number="+1234567890", api_id=12345, api_hash="abcdef", settings=settings)
        data = req.to_bytes()
        r = TLReader(data)
        decoded = r.read_object()
        self.assertIsInstance(decoded, fn.SendCode)
        self.assertEqual(decoded.phone_number, "+1234567890")
        self.assertEqual(decoded.api_id, 12345)
        self.assertEqual(decoded.api_hash, "abcdef")
        self.assertTrue(decoded.settings.allow_flashcall)

    def test_sign_in_and_up_serialization(self) -> None:
        sign_in = fn.SignIn(phone_number="+1234567890", phone_code_hash="hash123", phone_code="12345")
        data = sign_in.to_bytes()
        r = TLReader(data)
        decoded_in = r.read_object()
        self.assertIsInstance(decoded_in, fn.SignIn)
        self.assertEqual(decoded_in.phone_code, "12345")

        sign_up = fn.SignUp(phone_number="+1234567890", phone_code_hash="hash123", first_name="John", last_name="Doe")
        data_up = sign_up.to_bytes()
        r2 = TLReader(data_up)
        decoded_up = r2.read_object()
        self.assertIsInstance(decoded_up, fn.SignUp)
        self.assertEqual(decoded_up.first_name, "John")

    def test_channels_and_messages_rpc(self) -> None:
        join = fn.JoinChannel(channel=tl.InputChannel(channel_id=100123, access_hash=456))
        r = TLReader(join.to_bytes())
        dec_join = r.read_object()
        self.assertIsInstance(dec_join, fn.JoinChannel)
        self.assertEqual(dec_join.channel.channel_id, 100123)

        del_msg = fn.DeleteMessages(id=[1, 2, 3], revoke=True)
        r2 = TLReader(del_msg.to_bytes())
        dec_del = r2.read_object()
        self.assertIsInstance(dec_del, fn.DeleteMessages)
        self.assertTrue(dec_del.revoke)
        self.assertEqual(dec_del.id, [1, 2, 3])

    def test_raw_submodules(self) -> None:
        self.assertTrue(hasattr(raw.functions.auth, "SendCode"))
        self.assertTrue(hasattr(raw.functions.auth, "SignIn"))
        self.assertTrue(hasattr(raw.functions.messages, "SendMessage"))
        self.assertTrue(hasattr(raw.functions.contacts, "ResolveUsername"))
        self.assertTrue(hasattr(raw.functions.channels, "JoinChannel"))
        self.assertTrue(hasattr(raw.functions.account, "UpdateProfile"))

    def test_client_methods_registered(self) -> None:
        client = TgFlow("test_sess", 123, "hash")
        methods = [
            "send_code",
            "sign_in",
            "sign_up",
            "check_password",
            "resend_code",
            "cancel_code",
            "log_out",
            "export_authorization",
            "import_authorization",
            "resolve_username",
            "get_users",
            "get_full_user",
            "join_channel",
            "leave_channel",
            "create_channel",
            "edit_message_text",
            "delete_messages",
            "read_history",
            "forward_messages",
            "send_reaction",
            "set_typing",
            "update_profile",
            "update_status",
        ]
        for m in methods:
            self.assertTrue(callable(getattr(client, m)), f"Method {m} is missing or not callable")


if __name__ == "__main__":
    unittest.main()
