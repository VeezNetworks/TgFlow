<div align="center">
  <img src="assets/logo.png" alt="TgFlow Logo" width="180"/>
  <h1>TgFlow</h1>
  <p><b>Pure Python MTProto 2.0 Telegram Framework</b></p>
  <p>Engineered for speed, intuitive routing typography, full Telegram Layer 225 schema, 24 raw namespaces, and zero comment clutter.</p>
</div>

---

## Highlights

- **Pure MTProto 2.0 Engine**: Built from scratch adhering strictly to official Telegram MTProto specifications.
- **Complete Official Schema (Layer 225)**: Exactly 1,573 TL types and 783 RPC methods compiled into type-safe Python classes with exact 4-byte aligned serialization.
- **24 Raw Namespaces**: Direct low-level access via `tgflow.raw.functions.<namespace>` and `tgflow.raw.types.<namespace>` (`messages`, `channels`, `phone`, `payments`, `stories`, `aicompose`, `smsjobs`, etc.).
- **MTProto Core & E2E Secret Chats**: Native implementations of `core.telegram.org/schema/mtproto` (45 types, 9 functions) and `core.telegram.org/schema/end-to-end` (90 constructors).
- **Obfuscated2 TCP Framing**: Live-verified transport connection to Telegram DC2 with 64-byte random payload handshakes.
- **Advanced Routing Typography**: Replaces cumbersome filter syntax with concise, direct decorators:
  - `@bot.command("start")`
  - `@bot.callback("confirm")`
  - `@bot.message(When.photo)`
  - `@bot.inline()`
- **Expressive When Condition Engine**: Intuitive condition combinators via `When` (or `F`): `When.photo | When.video`, `When.private & ~When.bot`.
- **Comprehensive Telegram Client API**: Over 110 client methods covering media sending, polls, chat management, forum topics, stories, stars, collectibles, reactions, and VoIP/group calls.
- **Rich Telegram Formatting**: Full support for expandable blockquotes, spoilers, custom emoji, clickable links, and copy-text buttons.
- **Interactive Documentation**: Sphinx documentation featuring a dynamic animated scroll rail and TOC scrollspy.
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
| **Client & Methods** | `tgflow.client` | 110+ methods: send media, stories, stars, gifts, forum topics, group calls |
| **Raw Namespaces** | `tgflow.raw` | 24 namespaces: `messages`, `channels`, `phone`, `payments`, `stories`, `aicompose`, etc. |
| **Typography & Routing** | `tgflow.filters` | Direct decorators `@bot.command`, `@bot.callback`, `When` & `F` engine |
| **Rich Types** | `tgflow.types` | `Message`, `User`, `Chat`, `Photo`, `Poll`, `InlineKeyboardMarkup`, `ChatMember` |
| **MTProto Transport** | `tgflow.transport` | Obfuscated2 framing, intermediate protocol (`0xeeeeeeee`) |
| **Crypto & Handshake** | `tgflow.crypto` | AES-256 IGE, Pollard's rho PQ factorization, DH key exchange |
| **Binary TL Schema** | `tgflow.tl` | `TLReader`/`TLWriter`, 2,356 constructors, 4-byte aligned serialization |
| **Sessions** | `tgflow.session` | Portable string sessions with CRC32 integrity verification |

---

## Documentation

Interactive documentation is built using Sphinx with the Furo UI and custom animated scroll tracking:

```bash
sphinx-build -b html docs docs/_build/html
```

Preview locally:
```bash
python -m http.server 8000 --directory docs/_build/html
```

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for full release notes and version history.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
