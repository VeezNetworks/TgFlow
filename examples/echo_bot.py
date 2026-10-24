import asyncio
import os
from tgflow import TgFlow, CommandContext, When
from tgflow.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

bot = TgFlow(
    session="echo_bot",
    bot_token=os.getenv("BOT_TOKEN", "123456789:ABCDEF_PlaceholderToken"),
)

@bot.command
async def start(ctx: CommandContext):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Documentation", url="https://tgflow.veez.dev")],
        [InlineKeyboardButton(text="Ping", callback_data="ping_callback")]
    ])
    await ctx.reply(
        "<b>Hello from TgFlow!</b>\n\nSend any text message to echo it back.",
        reply_markup=keyboard,
    )

@bot.command
async def ping(client: TgFlow, message: Message):
    await message.reply("pong!")

@bot.callback("ping_callback")
async def on_ping_callback(client: TgFlow, query):
    await query.answer("Pong received from server!", show_alert=True)

@bot.message(When.text & ~When.bot)
async def echo(client: TgFlow, message: Message):
    await message.reply(f"Echo: {message.text}")

if __name__ == "__main__":
    asyncio.run(bot.run())
