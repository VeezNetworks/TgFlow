TgFlow Documentation
====================

Welcome to **TgFlow**, a pure Python MTProto 2.0 Telegram framework engineered for speed, clean line-by-line architecture, and modern bot development.

TgFlow is crafted from the ground up to strictly obey official Telegram MTProto rules while incorporating the ergonomic API design of leading frameworks like Pyrogram and Telethon.

Key Architectural Pillars
-------------------------

* **Zero-bloat MTProto 2.0**: Native implementation of Obfuscated2 transport, AES-256 IGE, Pollard's rho PQ factorization, and Diffie-Hellman key derivation.
* **Complete Official TL Schema**: Exactly 1,573 official Telegram TL types and 783 RPC functions (2,356 total constructors) from ``core.telegram.org/schema`` compiled directly into type-safe Python classes with exact 4-byte aligned binary serialization.
* **24 Raw Namespaces in ``tgflow.raw``**: Dedicated namespaces for ``messages``, ``channels``, ``phone``, ``payments``, ``stories``, ``aicompose``, ``smsjobs``, etc.
* **MTProto Core & E2E Secret Chats**: Complete coverage of ``core.telegram.org/schema/mtproto`` (45 types, 9 functions) and ``core.telegram.org/schema/end-to-end`` (90 constructors).
* **Smooth Animated Scroll Rail**: Dynamic vertical scroll progress indicator with animated tracking thumb and scrollspy matching modern documentation UI.
* **Composable Routing**: Expressive filter combinators supporting ``&`` (AND), ``|`` (OR), and ``~`` (NOT) for declarative event routing.
* **Modern Messaging**: Built-in support for expandable blockquotes, spoilers, custom animated emoji, ephemeral auto-deleting timers, and quote replies.
* **Tamper-Evident Sessions**: Portable base64 sessions with CRC32 integrity checks.
* **Strict Code Quality**: Zero comment clutter in the implementation and verified test suite.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   quickstart
   auth
   methods
   raw_namespaces
   keyboards
   advanced_features
   calls
   mtproto
   filters
   formatting
   sessions
   api
   changelog
