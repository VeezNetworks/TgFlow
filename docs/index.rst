.. image:: _static/logo.png
   :align: center
   :alt: TgFlow Logo
   :width: 220px

====================================
TgFlow: Modern Asynchronous MTProto
====================================

**TgFlow** is an advanced, high-performance Python MTProto library designed from first principles. It combines native MTProto 2.0 cryptographic primitives, full Telegram Layer 225+ schema models (including Telegram Stars, Star Subscriptions, Paid Reactions, Business Connections 2.0, Stories 2.0, Upgraded Gifts, and Forum Topics), a declarative routing engine with inline conversational dialogues, and a multi-language IPC bridge for cross-language bot development.

Key Features
------------

* **Native MTProto 2.0 Cryptography**: In-house pure AES-256 IGE, Pollard's rho PQ factorization, 2048-bit Diffie-Hellman key exchange, and Obfuscated2 framing for DPI evasion.
* **Modern Schema Support**: Integrated Telegram API & TDLib schemas supporting Layer 225+ updates — Telegram Stars, Paid Reactions, Star Subscriptions, Business 2.0, Stories 2.0, Upgraded Collectibles, and Forum Topics.
* **Declarative Template Routing**: Expressive route syntax with typed parameter extraction (``@bot.on("/ban <target> <duration:int=60>")``).
* **Interactive Conversational Flow**: Asynchronous multi-turn dialogues built right into the context (``await m.ask()``, ``await m.choose()``).
* **Multi-Language IPC Bridge**: Built-in JSON-RPC server and protocol client enabling bot logic in Go, Node.js, Rust, or C# without re-implementing MTProto.
* **Async by Design**: Clean, line-by-line asynchronous execution using standard ``asyncio``.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   quickstart
   routing
   architecture
   multilingual
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
