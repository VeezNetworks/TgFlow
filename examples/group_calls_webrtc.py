import asyncio
import os
from tgflow import TgFlow, CommandContext
from tgflow.types import GroupCall

client = TgFlow(
    session="calls_session",
    api_id=int(os.getenv("API_ID", "12345")),
    api_hash=os.getenv("API_HASH", "0123456789abcdef0123456789abcdef"),
)

@client.command("start_call")
async def start_call_cmd(ctx: CommandContext):
    call: GroupCall = await ctx.client.create_group_call(
        chat_id=ctx.chat.id,
        title="TgFlow Voice & Video Stream",
    )
    await ctx.reply(f"Group call created! Call ID: {call.id}")

@client.command("join_call <call_id:int>")
async def join_call_cmd(ctx: CommandContext, call_id: int):
    webrtc_params = '{"fingerprint": "mock_sdp_fingerprint", "setup": "actpass"}'
    res = await ctx.client.join_group_call(
        call_id=call_id,
        params=webrtc_params,
        muted=False,
        video_stopped=True,
    )
    await ctx.reply(f"Joined group call {call_id} successfully.")

@client.command("leave_call <call_id:int>")
async def leave_call_cmd(ctx: CommandContext, call_id: int):
    await ctx.client.leave_group_call(call_id)
    await ctx.reply(f"Left group call {call_id}.")

async def main():
    async with client:
        await client.idle()

if __name__ == "__main__":
    asyncio.run(main())
