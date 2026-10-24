import asyncio
import sys
import time

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from tgflow import (
    LAYER,
    F,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    LinkPreviewOptions,
    MessageQuote,
    TgFlow,
    When,
    blockquote,
    bold,
    code,
    custom_emoji,
    italic,
    spoiler,
)
from tgflow.tl.types import Chat, Message, User


async def run_live_demo():
    print("=" * 70)
    print(f"🚀 TgFlow Live Framework Demonstration (Telegram Layer {LAYER}+)")
    print("=" * 70)

    # 1. Initialize Bot Client
    bot = TgFlow(
        api_id=123456,
        api_hash="0123456789abcdef0123456789abcdef",
        bot_token="123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ",
    )
    await bot.start()
    print(f"✅ Bot initialized: @{bot.me.username} (ID: {bot.me_id}) | Layer: {LAYER}\n")

    # 2. Register Routes

    # Route A: /start command with Natural English typography (When)
    @bot.on(When.Command("start") & When.Private)
    async def handle_start(ctx):
        custom_star = custom_emoji("⭐", emoji_id="5368324170671202286")
        welcome_text = (
            f"👋 {bold(f'Hello {ctx.sender.first_name}!')}\n"
            f"{custom_star} Welcome to {bold('TgFlow')} (Layer {LAYER}+ Engine).\n\n"
            f"Features demonstrated in this live session:\n"
            f"• Parameterized routes & smart auto-reply targeting\n"
            f"• 1-Click Copy buttons & Web App inline keyboards\n"
            f"• Snippet quoting & Ephemeral self-destructing messages\n"
            f"• Collapsible / Expandable blockquotes\n"
            f"• Interactive conversational flows (ctx.ask / ctx.choose)\n"
            f"• Telegram Stars & Paid Reactions"
        )
        kb = InlineKeyboardMarkup().add_row(
            InlineKeyboardButton(text="📋 Copy Promo Code", copy_text="TGF_2026_LIVE"),
            InlineKeyboardButton(text="🌐 Docs", url="http://localhost:8000/"),
        )
        res = await ctx.reply_rich(welcome_text, reply_markup=kb)
        print(f"  [BOT REPLY -> /start] Message #{res.id} sent with 1-click copy keyboard.")

    # Route B: Parameterized command with auto-reply targeting
    @bot.on("/ban <target> <duration:int=60> <reason*>")
    async def handle_ban(ctx, target, duration: int = 60, reason: str = "Rule violation"):
        clean_reason = reason or "Rule violation"
        target_name = getattr(target, "first_name", str(target))
        res = await ctx.reply(
            f"🔨 {bold('Ban Action Executed')}:\n"
            f"• Target: {code(target_name)}\n"
            f"• Duration: {duration} minutes\n"
            f"• Reason: {italic(clean_reason)}"
        )
        print(f"  [BOT REPLY -> /ban] Message #{res.id} Banned target '{target_name}' for {duration}m (Reason: {clean_reason})")

    # Route C: Snippet Quote Reply
    @bot.on(When.Command("quote"))
    async def handle_quote(ctx):
        res = await ctx.reply_quote(
            text="✅ We verified this specific highlighted claim.",
            quote_text="important fact from user message",
        )
        print(f"  [BOT REPLY -> /quote] Quoted snippet: '{res.quote.text}'")

    # Route D: Ephemeral Self-Destructing Message (Auto-Delete)
    @bot.on(When.Command("secret"))
    async def handle_secret(ctx):
        res = await ctx.reply_ephemeral(
            text="🔐 Secret Passkey: 9812-4411 (Auto-deletes in 30 seconds)",
            ttl=30,
        )
        print(f"  [BOT REPLY -> /secret] Ephemeral message #{res.id} sent with TTL: {res.ttl_period}s")

    # Route E: Expandable Blockquote & Spoilers
    @bot.on(When.Command("terms"))
    async def handle_terms(ctx):
        long_terms = blockquote(
            "Terms of Service & Rules:\n"
            "1. No spamming or unsolicited mass messaging.\n"
            "2. All payments use Telegram Stars (Layer 225+).\n"
            "3. Collectible gifts can be upgraded on Fragment.\n"
            "4. Respect rate limits and community standards.",
            expandable=True,
        )
        res = await ctx.reply(f"📜 {bold('TgFlow Policy')}:\n\n{long_terms}")
        print(f"  [BOT REPLY -> /terms] Expandable blockquote sent.")

    # Route F: Modern Telegram Stars & Paid Reactions
    @bot.on(When.Command("support"))
    async def handle_support(ctx):
        stars_res = await bot.send_stars(chat_id=ctx.chat_id, amount=100, purpose="Developer Tip")
        reaction = await bot.send_paid_reaction(chat_id=ctx.chat_id, message_id=ctx.message.id, stars_count=25)
        res = await ctx.reply(f"⭐ Sent {stars_res['stars_transferred']} Telegram Stars! Reaction: {reaction.stars_count} Stars.")
        print(f"  [BOT REPLY -> /support] Stars transferred: {stars_res['stars_transferred']} | Reaction: {reaction.stars_count}⭐")

    # 3. Simulate Live Incoming Telegram Events
    print("-" * 70)
    print("⚡ SIMULATING LIVE INCOMING TELEGRAM UPDATES:")
    print("-" * 70)

    chat_p = Chat(id=98765, type="private", username="alice_dev")
    chat_g = Chat(id=-1001234567, type="supergroup", title="Developers Lounge")
    alice = User(id=98765, first_name="Alice", username="alice_dev")
    bob = User(id=555444, first_name="Bob", username="bob_spammer")

    # Test 1: /start
    print("[1] Alice sends '/start' in private:")
    await bot.process_update({"message": {"message_id": 101, "chat": {"id": chat_p.id, "type": "private"}, "from": {"id": alice.id, "first_name": "Alice"}, "text": "/start"}})

    # Test 2: /ban @spammer 30 Spamming links
    print("\n[2] Admin sends '/ban @spammer 30 Spamming promotional links' in group:")
    await bot.process_update({"message": {"message_id": 102, "chat": {"id": chat_g.id, "type": "supergroup"}, "from": {"id": 1, "first_name": "Admin"}, "text": "/ban @spammer 30 Spamming promotional links"}})

    # Test 3: /ban while replying to Bob without typing username
    print("\n[3] Admin sends '/ban' while REPLYING to Bob's message (Smart Target Injection):")
    await bot.process_update({
        "message": {
            "message_id": 103,
            "chat": {"id": chat_g.id, "type": "supergroup"},
            "from": {"id": 1, "first_name": "Admin"},
            "text": "/ban",
            "reply_to_message": {
                "message_id": 99,
                "from": {"id": bob.id, "first_name": "Bob"},
                "text": "Check out my spam website!",
            },
        }
    })

    # Test 4: /quote
    print("\n[4] User sends '/quote':")
    await bot.process_update({"message": {"message_id": 104, "chat": {"id": chat_p.id, "type": "private"}, "from": {"id": alice.id, "first_name": "Alice"}, "text": "/quote"}})

    # Test 5: /secret (Ephemeral message)
    print("\n[5] User sends '/secret':")
    await bot.process_update({"message": {"message_id": 105, "chat": {"id": chat_p.id, "type": "private"}, "from": {"id": alice.id, "first_name": "Alice"}, "text": "/secret"}})

    # Test 6: /terms (Expandable blockquote)
    print("\n[6] User sends '/terms':")
    await bot.process_update({"message": {"message_id": 106, "chat": {"id": chat_p.id, "type": "private"}, "from": {"id": alice.id, "first_name": "Alice"}, "text": "/terms"}})

    # Test 7: /support (Telegram Stars)
    print("\n[7] User sends '/support':")
    await bot.process_update({"message": {"message_id": 107, "chat": {"id": chat_p.id, "type": "private"}, "from": {"id": alice.id, "first_name": "Alice"}, "text": "/support"}})

    print("\n" + "=" * 70)
    print("✅ All live demo handlers executed successfully!")
    print("=" * 70)

    await bot.stop()


if __name__ == "__main__":
    asyncio.run(run_live_demo())
