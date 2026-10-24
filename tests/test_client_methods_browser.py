import unittest
import asyncio
from unittest.mock import AsyncMock
from tgflow import TgFlow, raw
from tgflow.tl import types as tl


class TestClientMethodsBrowser(unittest.TestCase):
    def test_client_browser_methods_presence(self) -> None:
        client = TgFlow(api_id=12345, api_hash="mock_hash")
        expected_methods = [
            "send_story",
            "edit_story",
            "delete_stories",
            "get_stories",
            "get_peer_stories",
            "get_story_views",
            "get_ai_tones",
            "get_ai_tone_example",
            "get_collectible_info",
            "get_stars_status",
            "get_stars_transactions",
            "get_star_gifts",
            "send_star_gift",
            "set_bot_commands",
            "get_bot_commands",
            "delete_bot_commands",
            "set_bot_menu_button",
            "get_bot_menu_button",
            "set_bot_info",
            "get_bot_info",
            "answer_web_app_query",
            "get_available_effects",
            "get_available_reactions",
            "set_default_reaction",
            "get_sticker_set",
            "get_custom_emoji_stickers",
            "get_featured_sticker_sets",
            "get_privacy_rules",
            "set_privacy_rules",
            "get_dialog_filters",
            "update_dialog_filter",
            "check_chatlist_invite",
            "join_chatlist_invite",
            "leave_chatlist",
            "is_sms_job_eligible",
            "get_sms_job",
            "finish_sms_job",
        ]
        for m in expected_methods:
            self.assertTrue(hasattr(client, m), f"Missing client method: {m}")

    def test_client_browser_methods_invocation(self) -> None:
        client = TgFlow(api_id=12345, api_hash="mock_hash")
        client.invoke = AsyncMock(return_value=tl.BoolTrue())

        async def run_calls() -> None:
            r1 = await client.get_available_effects()
            self.assertIsInstance(r1, tl.BoolTrue)

            r2 = await client.get_available_reactions()
            self.assertIsInstance(r2, tl.BoolTrue)

            r3 = await client.get_stars_status()
            self.assertIsInstance(r3, tl.BoolTrue)

            r4 = await client.get_dialog_filters()
            self.assertIsInstance(r4, tl.BoolTrue)

            r5 = await client.is_sms_job_eligible()
            self.assertIsInstance(r5, tl.BoolTrue)

            r6 = await client.get_ai_tones()
            self.assertIsInstance(r6, tl.BoolTrue)

        asyncio.run(run_calls())


if __name__ == "__main__":
    unittest.main()
