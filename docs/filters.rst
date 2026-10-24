Filters and Event Routing
==========================

TgFlow provides a composable routing system inspired by Pyrogram and Telethon.

Filter Operators
----------------

You can combine filters using standard Python logical operators:

* ``&``: Logical AND (both conditions must match)
* ``|``: Logical OR (either condition matches)
* ``~``: Logical NOT (inverts the filter condition)

.. code-block:: python

   from tgflow import filters

   # Command ping in private chats only
   my_filter = filters.command("ping") & filters.private

   # Text messages or photo messages
   media_or_text = filters.text | filters.photo

   # All messages except those from bots
   human_only = ~filters.bot

Built-in Filters
----------------

* ``filters.all``: Matches every update.
* ``filters.text``: Matches messages containing non-empty text.
* ``filters.command(commands, prefixes="/")``: Parses command names and arguments into ``message.command``.
* ``filters.regex(pattern)``: Matches text against regular expressions, populating ``message.matches``.
* ``filters.private``: Matches one-on-one direct messages.
* ``filters.group``: Matches group and supergroup chats.
* ``filters.channel``: Matches broadcast channel posts.
* ``filters.bot``: Matches messages sent by bot accounts.
* ``filters.reply``: Matches messages that are replies.
* ``filters.forwarded``: Matches forwarded messages.
* ``filters.media``: Matches messages with attachments.
* ``filters.photo``: Matches photos.
* ``filters.document``: Matches document files.

Custom Filters
--------------

Create custom filters using ``filters.create``:

.. code-block:: python

   from tgflow import filters

   is_admin = filters.create(lambda client, msg: msg.from_user and msg.from_user.id in [1234567, 7654321])

   @bot.on_message(filters.command("ban") & is_admin)
   async def handle_ban(client, message):
       await message.reply("Admin command executed.")
