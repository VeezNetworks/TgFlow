When Routing Engine
===================

TgFlow features the **When** (or **F**) condition engine, replacing outdated verbose filter syntax with clean, natural routing.

Routing Decorators
------------------

Instead of wrapping everything in generic handlers, TgFlow provides direct decorators on the client:

* ``@bot.command("start")``: Directly handles the ``/start`` command.
* ``@bot.command(["start", "help"], when=When.private)``: Multi-command handling with optional chat conditions.
* ``@bot.callback("confirm")``: Matches callback queries with data equal to ``confirm``.
* ``@bot.message(When.text)``: Handles messages matching specific conditions.
* ``@bot.inline()``: Handles inline queries.
* ``@bot.raw()``: Handles raw MTProto payload frames.

When Conditions & Combinators
-----------------------------

Combine conditions naturally using Python's bitwise operators ``&`` (AND), ``|`` (OR), and ``~`` (NOT):

.. code-block:: python

   from tgflow import When

   # Command in private chats only
   @bot.command("profile", when=When.private)
   async def handle_profile(client, msg):
       ...

   # Messages with photos or videos from non-bots
   @bot.message((When.photo | When.video) & ~When.bot)
   async def handle_media(client, msg):
       ...

Available Conditions
--------------------

* ``When.all``: Matches any update.
* ``When.text``: Non-empty text messages.
* ``When.command(cmds, prefixes="/")``: Custom command filter.
* ``When.regex(pattern)``: Matches text against regular expressions.
* ``When.private``: Direct 1-on-1 messages.
* ``When.group``: Group or supergroup messages.
* ``When.channel``: Channel broadcast posts.
* ``When.bot``: Messages from bot users.
* ``When.reply``: Messages replying to another message.
* ``When.forwarded``: Forwarded messages.
* ``When.media``: Messages with any media attachment.
* ``When.photo``: Photo messages.
* ``When.video``: Video messages.
* ``When.audio``: Audio files.
* ``When.document``: Document files.
* ``When.voice``: Voice audio messages.
* ``When.animation``: GIF/Animations.
* ``When.sticker``: Stickers.
* ``When.poll``: Polls.
* ``When.user(ids_or_usernames)``: Filter by specific users.
* ``When.chat(ids_or_usernames)``: Filter by specific chats.
* ``When.data(callback_data)``: Filter callback queries by exact payload.
* ``When.custom(func)``: Custom user-defined evaluation function.
