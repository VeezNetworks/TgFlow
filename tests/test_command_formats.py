import asyncio
import unittest
from typing import Any
from tgflow import TgFlow, Command, FlowCommand, CommandContext, When
from tgflow.types import Message, Chat, User


class TestCommandFormats(unittest.TestCase):
    def test_zero_argument_command_decorator(self) -> None:
        client = TgFlow(session="test_sess")

        @client.command
        async def ping(cli: TgFlow, msg: Message) -> str:
            return "pong"

        self.assertEqual(len(client._message_handlers), 1)
        handler = client._message_handlers[0]

        valid_msg = Message(id=1, text="/ping", chat=Chat(id=10, type="private"))
        invalid_msg = Message(id=2, text="/pong", chat=Chat(id=10, type="private"))

        self.assertTrue(asyncio.run(handler.check(client, valid_msg)))
        self.assertFalse(asyncio.run(handler.check(client, invalid_msg)))

        res = asyncio.run(handler.execute(client, valid_msg))
        self.assertEqual(res, "pong")

    def test_cmd_alias_decorator(self) -> None:
        client = TgFlow(session="test_sess")

        @client.cmd("info")
        async def bot_info(cli: TgFlow, msg: Message) -> str:
            return "info_result"

        self.assertEqual(len(client._message_handlers), 1)
        handler = client._message_handlers[0]
        test_msg = Message(id=1, text="/info", chat=Chat(id=10, type="private"))

        self.assertTrue(asyncio.run(handler.check(client, test_msg)))
        res = asyncio.run(handler.execute(client, test_msg))
        self.assertEqual(res, "info_result")

    def test_typed_command_format_and_injection(self) -> None:
        client = TgFlow(session="test_sess")

        results = {}

        @client.command("ban <user_id:int> [reason:str]")
        async def ban_handler(cli: TgFlow, msg: Message, user_id: int, reason: str = "Spam") -> None:
            results["user_id"] = user_id
            results["reason"] = reason

        handler = client._message_handlers[0]

        msg1 = Message(id=1, text="/ban 12345 Flood", chat=Chat(id=10, type="group"))
        self.assertTrue(asyncio.run(handler.check(client, msg1)))
        self.assertEqual(msg1.command_name, "ban")
        self.assertEqual(msg1.command_kwargs["user_id"], 12345)
        self.assertEqual(msg1.command_kwargs["reason"], "Flood")

        asyncio.run(handler.execute(client, msg1))
        self.assertEqual(results["user_id"], 12345)
        self.assertEqual(results["reason"], "Flood")

        msg2 = Message(id=2, text="/ban 99999", chat=Chat(id=10, type="group"))
        self.assertTrue(asyncio.run(handler.check(client, msg2)))
        asyncio.run(handler.execute(client, msg2))
        self.assertEqual(results["user_id"], 99999)
        self.assertEqual(results["reason"], "Spam")

    def test_command_context_handler(self) -> None:
        client = TgFlow(session="test_sess")

        results = {}

        @client.command("start")
        async def start_handler(ctx: CommandContext) -> str:
            results["cmd"] = ctx.command
            results["chat_id"] = ctx.chat.id
            return "welcome"

        handler = client._message_handlers[0]
        msg = Message(id=1, text="/start payload_123", chat=Chat(id=777, type="private"))
        self.assertTrue(asyncio.run(handler.check(client, msg)))

        res = asyncio.run(handler.execute(client, msg))
        self.assertEqual(res, "welcome")
        self.assertEqual(results["cmd"], "start")
        self.assertEqual(results["chat_id"], 777)

    def test_command_context_with_typed_params(self) -> None:
        client = TgFlow(session="test_sess")

        captured = {}

        @client.command("warn <user_id:int> [severity:int]")
        async def warn_handler(ctx: CommandContext, user_id: int, severity: int = 1) -> None:
            captured["ctx_cmd"] = ctx.command
            captured["user_id"] = user_id
            captured["severity"] = severity

        handler = client._message_handlers[0]
        msg = Message(id=1, text="/warn 456 3", chat=Chat(id=10, type="group"))
        self.assertTrue(asyncio.run(handler.check(client, msg)))

        asyncio.run(handler.execute(client, msg))
        self.assertEqual(captured["ctx_cmd"], "warn")
        self.assertEqual(captured["user_id"], 456)
        self.assertEqual(captured["severity"], 3)

    def test_flow_command_builder(self) -> None:
        client = TgFlow(session="test_sess")

        kick_cmd = (
            Command("kick <user_id:int>")
            .desc("Kick a member from group")
            .prefix("!")
            .alias("k")
        )

        @client.command(kick_cmd)
        async def kick_handler(cli: TgFlow, msg: Message, user_id: int) -> int:
            return user_id

        handler = client._message_handlers[0]

        msg_excl = Message(id=1, text="!kick 888", chat=Chat(id=10, type="group"))
        self.assertTrue(asyncio.run(handler.check(client, msg_excl)))
        res1 = asyncio.run(handler.execute(client, msg_excl))
        self.assertEqual(res1, 888)

        msg_alias = Message(id=2, text="!k 999", chat=Chat(id=10, type="group"))
        self.assertTrue(asyncio.run(handler.check(client, msg_alias)))
        res2 = asyncio.run(handler.execute(client, msg_alias))
        self.assertEqual(res2, 999)

        msg_slash = Message(id=3, text="/kick 888", chat=Chat(id=10, type="group"))
        self.assertFalse(asyncio.run(handler.check(client, msg_slash)))

    def test_prefix_stripping_and_custom_prefixes(self) -> None:
        client = TgFlow(session="test_sess")

        @client.command("/status", prefixes=["/", ".", "!"])
        async def status_handler(cli: TgFlow, msg: Message) -> str:
            return "operational"

        handler = client._message_handlers[0]

        for text in ("/status", ".status", "!status"):
            msg = Message(id=1, text=text, chat=Chat(id=10, type="private"))
            self.assertTrue(asyncio.run(handler.check(client, msg)))
            self.assertEqual(msg.command_name, "status")

    def test_dispatch_message(self) -> None:
        client = TgFlow(session="test_sess")
        dispatched = []

        @client.command("test")
        async def on_test(cli: TgFlow, msg: Message) -> None:
            dispatched.append(msg.id)

        msg = Message(id=101, text="/test", chat=Chat(id=10, type="private"))
        asyncio.run(client.dispatch_message(msg))
        self.assertEqual(dispatched, [101])


if __name__ == "__main__":
    unittest.main()
