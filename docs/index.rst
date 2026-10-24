TgFlow Documentation
====================

Welcome to **TgFlow**, a pure Python MTProto 2.0 Telegram framework engineered for speed, clean line-by-line architecture, and modern bot development.

TgFlow is crafted from the ground up to strictly obey official Telegram MTProto rules while incorporating the ergonomic API design of leading frameworks like Pyrogram and Telethon.

Key Architectural Pillars
-------------------------

* **Zero-bloat MTProto 2.0**: Native implementation of Obfuscated2 transport, AES-256 IGE, Pollard's rho PQ factorization, and Diffie-Hellman key derivation.
* **Complete TL Schema**: Over 540 official Telegram TL constructors and methods compiled directly into type-safe Python classes with exact 4-byte aligned binary serialization.
* **Composable Routing**: Expressive filter combinators supporting ``&`` (AND), ``|`` (OR), and ``~`` (NOT) for declarative event routing.
* **Modern Messaging**: Built-in support for expandable blockquotes, spoilers, custom animated emoji, ephemeral auto-deleting timers, and quote replies.
* **Tamper-Evident Sessions**: Portable base64 sessions with CRC32 integrity checks.
* **Pure Clean Code**: Core library implemented without comment clutter, ensuring clean maintainability and rapid debugging.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   quickstart
   auth
   methods
   keyboards
   calls
   mtproto
   filters
   formatting
   sessions
   api
