Quickstart Guide
================

This guide demonstrates how to install TgFlow and build your first Telegram bot using modern and concise routing.

Installation
------------

Install TgFlow from PyPI:

.. code-block:: bash

   pip install tgflow

Modern Bot Example
------------------

TgFlow eliminates the verbose ``filters.command(...)`` syntax, providing direct decorators and expressive ``When`` conditions:

.. code-block:: python

   import asyncio
   from tgflow import TgFlow, When
   from tgflow.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

   bot = TgFlow(
       session="my_bot",
       bot_token="YOUR_BOT_TOKEN_HERE",
   )

   # Direct command routing
   @bot.command("start", when=When.private)
   async def handle_start(client: TgFlow, message: Message):
       keyboard = InlineKeyboardMarkup([
           [InlineKeyboardButton(text="Docs", url="https://tgflow.veez.dev")],
           [InlineKeyboardButton(text="Click Me", callback_data="btn_click")]
       ])
       await message.reply("Welcome to TgFlow! Choose an option:", reply_markup=keyboard)

   # Direct callback query routing
   @bot.callback("btn_click")
   async def handle_callback(client: TgFlow, query):
       await query.answer("Button clicked!", show_alert=True)

   # Direct message routing by condition
   @bot.message(When.photo)
   async def handle_photo(client: TgFlow, message: Message):
       await message.reply("Nice photo!")

   asyncio.run(bot.run())

Advanced Message Features
-------------------------

Native Quoted Reply
~~~~~~~~~~~~~~~~~~~

TgFlow allows quoting specific text segments in replies according to official MTProto quote specifications:

.. code-block:: python

   @bot.command("quote")
   async def handle_quote(client: TgFlow, message: Message):
       await message.reply_quote(
           text="Replying with a quoted segment.",
           quote=message.text,
       )

Ephemeral Self-Destructing Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Send messages that automatically delete after a specified duration:

.. code-block:: python

   @bot.command("temp")
   async def handle_temp(client: TgFlow, message: Message):
       await message.reply_ephemeral(
           text="This message disappears in 5 seconds.",
           ttl_seconds=5,
       )
