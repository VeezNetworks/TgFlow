import asyncio
import os
from tgflow import TgFlow, RichText, raw
from tgflow.types import Message

client = TgFlow(
    session="user_session",
    api_id=int(os.getenv("API_ID", "12345")),
    api_hash=os.getenv("API_HASH", "0123456789abcdef0123456789abcdef"),
)

@client.command("rich")
async def send_rich(cli: TgFlow, message: Message):
    text = (
        RichText()
        .bold("TgFlow v1.8.0")
        .text("\n\nPure Python ")
        .code("MTProto 2.0")
        .text(" implementation.\n")
        .spoiler("Hidden secret details here!")
        .text("\n\n")
        .blockquote("Fully typed and high performance.", expandable=True)
    )
    await message.reply(text)

@client.command("disappear")
async def self_destruct(cli: TgFlow, message: Message):
    await message.reply_ephemeral(
        text="This message will self-destruct in 7 seconds.",
        ttl_seconds=7,
    )

@client.command("history")
async def get_history_sample(cli: TgFlow, message: Message):
    dialogs = await cli.get_dialogs(limit=5)
    report = [f"Dialogs count: {len(dialogs)}"]
    for d in dialogs:
        report.append(f"- ID: {d.id} | Type: {d.type}")
    await message.reply("\n".join(report))

async def main():
    async with client:
        print("Connected as user:", client.me.id if client.me else "Unknown")
        await client.idle()

if __name__ == "__main__":
    asyncio.run(main())
