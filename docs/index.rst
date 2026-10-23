.. image:: _static/logo.png
   :align: center
   :alt: TgFlow Logo
   :width: 220px

====================================
TgFlow: Modern Asynchronous MTProto
====================================

**TgFlow** is an advanced, high-performance Python MTProto library designed from first principles. It combines native MTProto 2.0 cryptographic primitives, full TDLib Layer 190+ schema models (including Telegram Stars, Business Connections, Stories, and Paid Media), a declarative routing engine with inline conversational dialogues, and a multi-language IPC bridge for cross-language bot development.

Key Features
------------

* **Native MTProto 2.0 Cryptography**: In-house pure AES-256 IGE, Pollard's rho PQ factorization, 2048-bit Diffie-Hellman key exchange, and Obfuscated2 framing for DPI evasion.
* **Modern Schema Support**: Integrated TDLib schemas supporting Layer 190+ updates — Telegram Stars, Business Connections, Stories, Gifts, and Forum Topics.
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
