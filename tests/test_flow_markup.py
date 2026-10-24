import unittest
from tgflow import TgFlow, FlowMarkup, FlowButton, raw
from tgflow.tl import functions as fn, types as tl
from tgflow.tl.core import TLReader


class TestFlowMarkup(unittest.TestCase):
    def test_flow_button_factories(self) -> None:
        btn_data = FlowButton.data("Click", "data_123")
        self.assertEqual(btn_data.text, "Click")
        self.assertEqual(btn_data.callback_data, "data_123")

        btn_url = FlowButton.url("Google", "https://google.com")
        self.assertEqual(btn_url.url, "https://google.com")

        btn_copy = FlowButton.copy("Copy Code", "DISCOUNT2026")
        self.assertEqual(btn_copy.copy_text, "DISCOUNT2026")

        btn_user = FlowButton.user("Profile", 998877)
        self.assertEqual(btn_user.user_id, 998877)

    def test_flow_markup_grid(self) -> None:
        buttons = [FlowButton.data(f"Btn {i}", f"val_{i}") for i in range(5)]
        markup = FlowMarkup.grid(buttons, cols=2)
        self.assertEqual(len(markup.inline_keyboard), 3)
        self.assertEqual(len(markup.inline_keyboard[0]), 2)
        self.assertEqual(len(markup.inline_keyboard[1]), 2)
        self.assertEqual(len(markup.inline_keyboard[2]), 1)

    def test_flow_markup_to_tl(self) -> None:
        markup = FlowMarkup.inline([
            FlowMarkup.row(FlowButton.data("One", "1"), FlowButton.url("Two", "https://t.me")),
            FlowMarkup.row(FlowButton.copy("Copy", "TGFLOW")),
        ])
        tl_markup = markup.to_tl()
        self.assertIsInstance(tl_markup, tl.ReplyInlineMarkup)
        self.assertEqual(len(tl_markup.rows), 2)
        self.assertEqual(len(tl_markup.rows[0].buttons), 2)
        self.assertIsInstance(tl_markup.rows[0].buttons[0], tl.KeyboardButtonCallback)
        self.assertIsInstance(tl_markup.rows[0].buttons[1], tl.KeyboardButtonUrl)
        self.assertIsInstance(tl_markup.rows[1].buttons[0], tl.KeyboardButtonCopyText)

    def test_group_admin_rpc_serialization(self) -> None:
        rights = tl.ChatAdminRights(ban_users=True, pin_messages=True, manage_topics=True)
        edit_admin = fn.EditAdmin(
            channel=tl.InputChannel(channel_id=123, access_hash=456),
            user_id=tl.InputUser(user_id=789, access_hash=101),
            admin_rights=rights,
            rank="Moderator",
        )
        data = edit_admin.to_bytes()
        r = TLReader(data)
        decoded = r.read_object()
        self.assertIsInstance(decoded, fn.EditAdmin)
        self.assertEqual(decoded.rank, "Moderator")
        self.assertTrue(decoded.admin_rights.manage_topics)

    def test_forum_rpc_serialization(self) -> None:
        create_topic = fn.CreateForumTopic(
            channel=tl.InputChannel(channel_id=1001, access_hash=2002),
            title="General Chat",
            icon_color=0x6FB9F0,
        )
        r = TLReader(create_topic.to_bytes())
        decoded = r.read_object()
        self.assertIsInstance(decoded, fn.CreateForumTopic)
        self.assertEqual(decoded.title, "General Chat")
        self.assertEqual(decoded.icon_color, 0x6FB9F0)

    def test_client_group_methods_callable(self) -> None:
        client = TgFlow("test_session")
        methods = [
            "get_chat_history",
            "get_chat_administrators",
            "get_chat_members",
            "get_chat_member",
            "get_dialogs",
            "search_messages",
            "pin_chat_message",
            "unpin_chat_message",
            "unpin_all_chat_messages",
            "set_chat_title",
            "set_chat_description",
            "toggle_forum",
            "create_forum_topic",
            "edit_forum_topic",
            "close_forum_topic",
            "reopen_forum_topic",
            "delete_forum_topic",
        ]
        for m in methods:
            self.assertTrue(callable(getattr(client, m)), f"Method {m} is missing on client")


if __name__ == "__main__":
    unittest.main()
