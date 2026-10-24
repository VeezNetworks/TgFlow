<div align="center">
  <img src="assets/logo.png" alt="TgFlow Logo" width="180"/>
  <h1>TgFlow</h1>
  <p><b>Pure Python MTProto 2.0 Telegram Framework</b></p>
  <p>Line-by-line compliance with official Telegram MTProto rules, modern clean architecture inspired by Pyrogram and Telethon, zero bloated dependencies.</p>
</div>

---

## Highlights

- **Pure MTProto 2.0 Engine**: Built from scratch adhering to official Telegram MTProto specifications.
- **Obfuscated2 TCP Framing**: Resilient TCP transport with 64-byte random payload handshakes avoiding traffic filtering.
- **AES-256 IGE & Diffie-Hellman Handshake**: Cryptographic primitives including Pollard's rho prime factorization, SHA-256 key derivation, and hardware-accelerated AES.
- **Full Layer TL Schema**: Comprehensive catalog of 547 official Telegram constructors and methods with 4-byte aligned binary TL serialization.
- **Composable Filter Architecture**: Expressive routing using `&`, `|`, and `~` combinators (`filters.command("start") & filters.private`).
- **Rich Telegram Formatting**: Full support for expandable blockquotes, spoilers, custom emoji, clickable links, and copy-text buttons.
- **Tamper-Evident Sessions**: Base64 session format with CRC32 integrity validation.
- **Zero Comments In Core Code**: Pure, self-explanatory idiomatic Python.

---

## Installation

```bash
pip install tgflow
```

Or install with documentation dependencies:

```bash
pip install tgflow[docs]
```

---

## Quickstart

### Building a Modern Telegram Bot

```python
import asyncio
from tgflow import TgFlow, filters
from tgflow.types import Message

bot = TgFlow(
    session="my_bot",
    bot_token="123456789:ABCDefghIJKLmnOPQRstuvWXYZ",
)

@bot.on_message(filters.command("start") & filters.private)
async def handle_start(client: TgFlow, message: Message):
    await message.reply(
        "<b>Welcome to TgFlow!</b>\n\n"
        "Experience modern Telegram MTProto 2.0 bots in pure Python.",
        parse_mode="html",
    )

@bot.on_message(filters.command("quote"))
async def handle_quote(client: TgFlow, message: Message):
    await message.reply_quote(
        text="Here is a quoted reply using native MTProto quote semantics.",
        quote=message.text,
    )

@bot.on_message(filters.command("secret"))
async def handle_secret(client: TgFlow, message: Message):
    await message.reply_ephemeral(
        text="This message will self-destruct in 10 seconds.",
        ttl_seconds=10,
    )

asyncio.run(bot.run())
```

---

## Architecture Overview

| Component | Module | Responsibility |
|---|---|---|
| **Crypto** | `tgflow.crypto` | AES-IGE, Pollard's rho PQ factorization, Obfuscated2 framing, DH exchange |
| **Transport** | `tgflow.transport` | Non-blocking async TCP stream framing |
| **RPC** | `tgflow.rpc` | Monotonic `msg_id` generator, sequence numbers, packet packing/unpacking |
| **TL Schema** | `tgflow.tl` | Binary `TLReader`/`TLWriter`, 547 constructors and functions |
| **Filters** | `tgflow.filters` | Composable event routing with `&`, `|`, and `~` |
| **Types** | `tgflow.types` | High-level `Message`, `User`, `Chat`, `CallbackQuery` |
| **Session** | `tgflow.session` | Unique session format with CRC32 checksum |

---

## Building Documentation

TgFlow uses Sphinx with the modern Furo UI theme:

```bash
sphinx-build -b html docs docs/_build/html
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
