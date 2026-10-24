import asyncio
import os
from tgflow import TgFlow, Command, CommandContext, When
from tgflow.types import FlowMarkup, FlowButton, Message, ChatPermissions

bot = TgFlow(
    session="mod_bot",
    bot_token=os.getenv("BOT_TOKEN", "123456789:ABCDEF_PlaceholderToken"),
)

@bot.command("ban <user_id:int> [reason:str]", when=When.group)
async def ban_command(client: TgFlow, message: Message, user_id: int, reason: str = "Spam"):
    await client.ban_chat_member(message.chat.id, user_id)
    await message.reply(f"User {user_id} has been banned.\nReason: {reason}")

@bot.command("unban <user_id:int>", when=When.group)
async def unban_command(client: TgFlow, message: Message, user_id: int):
    await client.unban_chat_member(message.chat.id, user_id)
    await message.reply(f"User {user_id} unbanned.")

@bot.command("mute <user_id:int> [duration:int]", when=When.group)
async def mute_command(client: TgFlow, message: Message, user_id: int, duration: int = 3600):
    until_date = int(message.date + duration)
    permissions = ChatPermissions(can_send_messages=False)
    await client.restrict_chat_member(message.chat.id, user_id, permissions=permissions, until_date=until_date)
    await message.reply(f"User {user_id} muted for {duration} seconds.")

kick_cmd = (
    Command("kick <user_id:int>")
    .desc("Kick member from chat")
    .prefix("!")
    .alias("k")
    .when(When.group)
)

@bot.command(kick_cmd)
async def kick_handler(ctx: CommandContext, user_id: int):
    await ctx.client.ban_chat_member(ctx.chat.id, user_id)
    await ctx.client.unban_chat_member(ctx.chat.id, user_id)
    await ctx.reply(f"Kicked user {user_id}.")

@bot.command("menu")
async def show_menu(ctx: CommandContext):
    markup = (
        FlowMarkup()
        .row(FlowButton.text("Rules", callback_data="rules_cb"))
        .row(FlowButton.url("Official Channel", url="https://t.me/telegram"))
    )
    await ctx.reply("Select an administrative option:", reply_markup=markup.build())

if __name__ == "__main__":
    asyncio.run(bot.run())
