Quickstart Guide
================

This guide demonstrates how to install TgFlow and build your first Telegram bot using the MTProto 2.0 protocol.

Installation
------------

Install TgFlow from PyPI:

.. code-block:: bash

   pip install tgflow

Minimal Bot Example
-------------------

Here is a minimal bot that answers the ``/start`` command:

.. code-block:: python

   import asyncio
   from tgflow import TgFlow, filters
   from tgflow.types import Message

   bot = TgFlow(
       session="my_bot",
       bot_token="YOUR_BOT_TOKEN_HERE",
   )

   @bot.on_message(filters.command("start") & filters.private)
   async def handle_start(client: TgFlow, message: Message):
       await message.reply("Hello from TgFlow!")

   asyncio.run(bot.run())

Advanced Message Features
-------------------------

Native Quoted Reply
~~~~~~~~~~~~~~~~~~~

TgFlow allows quoting specific text segments in replies according to official MTProto quote specifications:

.. code-block:: python

   @bot.on_message(filters.command("quote"))
   async def handle_quote(client: TgFlow, message: Message):
       await message.reply_quote(
           text="Replying with a quoted segment.",
           quote=message.text,
       )

Ephemeral Self-Destructing Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Send messages that automatically delete after a specified duration:

.. code-block:: python

   @bot.on_message(filters.command("temp"))
   async def handle_temp(client: TgFlow, message: Message):
       await message.reply_ephemeral(
           text="This message disappears in 5 seconds.",
           ttl_seconds=5,
       )
