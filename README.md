<div align="center">
  <img src="assets/logo.png" alt="TgFlow Logo" width="180"/>
  <h1>TgFlow</h1>
  <p><b>Pure Python MTProto 2.0 Telegram Framework</b></p>
  <p>Engineered for speed, intuitive routing typography, full Telegram types and methods, and zero comment clutter.</p>
</div>

---

## Highlights

- **Pure MTProto 2.0 Engine**: Built from scratch adhering strictly to official Telegram MTProto specifications.
- **Obfuscated2 TCP Framing**: Live-verified transport connection to Telegram DC2 with 64-byte random payload handshakes.
- **Advanced Routing Typography**: Replaces cumbersome filter syntax with concise, direct decorators:
  - `@bot.command("start")`
  - `@bot.callback("confirm")`
  - `@bot.message(When.photo)`
  - `@bot.inline()`
- **Expressive When Condition Engine**: Intuitive condition combinators via `When` (or `F`): `When.photo | When.video`, `When.private & ~When.bot`.
- **Comprehensive Telegram Types & Methods**: 40+ client methods covering media sending, polls, chat management, permissions, and reactions.
- **Rich Telegram Formatting**: Full support for expandable blockquotes, spoilers, custom emoji, clickable links, and copy-text buttons.
- **Zero Comments In Core Code**: Self-explanatory, line-by-line clean idiomatic Python.

---

## Installation

```bash
pip install tgflow
```

---

## Quickstart

```python
import asyncio
from tgflow import TgFlow, When
from tgflow.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

bot = TgFlow(
    session="my_bot",
    bot_token="YOUR_BOT_TOKEN_HERE",
)

@bot.command("start", when=When.private)
async def handle_start(client: TgFlow, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="GitHub", url="https://github.com/VeezNetworks/TgFlow")],
        [InlineKeyboardButton(text="Verify", callback_data="verify_user")]
    ])
    await message.reply(
        "<b>Welcome to TgFlow!</b>\n\nExperience clean, modern MTProto 2.0 in Python.",
        parse_mode="html",
        reply_markup=keyboard,
    )

@bot.callback("verify_user")
async def handle_callback(client: TgFlow, query):
    await query.answer("Account verified!", show_alert=True)

@bot.command("quote")
async def handle_quote(client: TgFlow, message: Message):
    await message.reply_quote(
        text="Native MTProto quote reply.",
        quote=message.text,
    )

@bot.command("secret")
async def handle_secret(client: TgFlow, message: Message):
    await message.reply_ephemeral(
        text="This message will self-destruct in 10 seconds.",
        ttl_seconds=10,
    )

asyncio.run(bot.run())
```

---

## Comprehensive Architecture

| Domain | Module | Highlights |
|---|---|---|
| **Client & Methods** | `tgflow.client` | 40+ methods: send media, edit, delete, pin, polls, reactions, members |
| **Typography & Routing** | `tgflow.filters` | Direct decorators `@bot.command`, `@bot.callback`, `When` & `F` engine |
| **Rich Types** | `tgflow.types` | `Message`, `User`, `Chat`, `Photo`, `Poll`, `InlineKeyboardMarkup`, `ChatMember` |
| **MTProto Transport** | `tgflow.transport` | Obfuscated2 framing, intermediate protocol (`0xeeeeeeee`) |
| **Crypto & Handshake** | `tgflow.crypto` | AES-256 IGE, Pollard's rho PQ factorization, DH key exchange |
| **Binary TL Schema** | `tgflow.tl` | `TLReader`/`TLWriter`, 547 constructors, 4-byte aligned serialization |
| **Sessions** | `tgflow.session` | Portable string sessions with CRC32 integrity verification |

---

## Documentation

Interactive documentation is built using Sphinx with the Furo UI:

```bash
sphinx-build -b html docs docs/_build/html
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
