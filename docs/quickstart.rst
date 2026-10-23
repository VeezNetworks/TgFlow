Quickstart Guide
================

This guide gets you up and running with **TgFlow** in under five minutes.

Installation
------------

TgFlow requires Python 3.10+ and the ``cryptography`` package:

.. code-block:: bash

   pip install cryptography

If installing from source:

.. code-block:: bash

   cd D:\personal\TgFlow
   pip install -e .

Generating a Unique TgFlow Session Token
-----------------------------------------

TgFlow departs from legacy string session formats. It produces a **tamper-evident, CRC32-checksummed Base64URL token** prefixed with ``tgflow_live_`` or ``tgflow_test_``:

.. code-block:: bash

   python tools/generate_session.py

Example output:

.. code-block:: text

   =================================================================
   GENERATED TGFlow SESSION STRING:
   =================================================================
   tgflow_live_VEdGTDECAQAAAAAAAAC1e...
   =================================================================

Bootstrapping Client with Session
---------------------------------

You can instantiate your client instantly with the exported token without requiring local SQLite files:

.. code-block:: python

   import asyncio
   from tgflow import TgFlow, When, F

   client = TgFlow(session="tgflow_live_VEdGTDECAQAAAAAAAAC1e...")

   # Natural typography routing with When
   @client.on(When.Command("start") & When.Private)
   async def handle_start(ctx):
       await ctx.reply(f"Hello, {ctx.sender.first_name}! Welcome to TgFlow.")

   # Short modern typography with F
   @client.on(F.command("help") & F.group)
   async def handle_help(ctx):
       await ctx.reply("Group help commands: /stats, /ban, /info")

   async def main():
       await client.start()
       print("TgFlow client running...")
       await client.idle()

   if __name__ == "__main__":
       asyncio.run(main())

Testing Data Center Handshake
-----------------------------

TgFlow provides a built-in verification script to confirm TCP connectivity and MTProto PQ authorization handshake with Telegram's data centers:

.. code-block:: bash

   python tests/test_dc_connect.py
