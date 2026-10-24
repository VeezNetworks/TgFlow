When Routing Engine & Advanced Commands
=========================================

TgFlow features the modern **When** (or **F**) condition engine and an advanced **Command Routing** system, eliminating boilerplate and providing clean, ergonomic routing.

Command Formatting
------------------

TgFlow supports multiple flexible command formats:

1. Zero-Argument Auto-Inference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Decorate your handler without parentheses. The command name is automatically inferred from the async function name:

.. code-block:: python

   @bot.command
   async def ping(client, message):
       await message.reply("pong")

   @bot.command
   async def start(client, message):
       await message.reply("Welcome to TgFlow!")

2. Parameterized & Typed Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify typed arguments using angle brackets ``<param:type>`` for required arguments and square brackets ``[param:type]`` for optional arguments. Supported types include ``int``, ``float``, ``bool``, and ``str``:

.. code-block:: python

   @bot.command("ban <user_id:int> [reason:str]")
   async def ban_user(client, message, user_id: int, reason: str = "Spam"):
       await client.ban_chat_member(message.chat.id, user_id)
       await message.reply(f"Banned user {user_id}. Reason: {reason}")

TgFlow automatically parses incoming message arguments, casts them to the requested types, and injects them directly into the handler parameters.

3. CommandContext (ctx) Handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Handlers can receive a single ``ctx: CommandContext`` object providing convenient shortcuts:

.. code-block:: python

   from tgflow import CommandContext

   @bot.command("info")
   async def bot_info(ctx: CommandContext):
       await ctx.reply(f"Running command: /{ctx.command} in chat {ctx.chat.id}")

   @bot.command("warn <user_id:int> [severity:int]")
   async def warn(ctx: CommandContext, user_id: int, severity: int = 1):
       await ctx.reply(f"Warned user {user_id} with severity level {severity}.")

4. Fluent Command / FlowCommand DSL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build complex commands using the fluent ``Command`` builder with chaining:

.. code-block:: python

   from tgflow import Command, When

   kick_cmd = (
       Command("kick <user_id:int>")
       .desc("Kick a member from the group")
       .prefix("!")
       .alias("k")
       .when(When.group)
   )

   @bot.command(kick_cmd)
   async def handle_kick(client, message, user_id: int):
       await client.ban_chat_member(message.chat.id, user_id)

5. Command Aliases & Flexible Prefixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``@bot.cmd`` decorator is a direct alias for ``@bot.command``. Custom prefixes (e.g. ``!``, ``.``, or prefix-less ``""``) and automatic leading prefix stripping are fully supported:

.. code-block:: python

   # Accepts /status, .status, or !status
   @bot.cmd("/status", prefixes=["/", ".", "!"])
   async def check_status(client, message):
       await message.reply("All systems operational.")

Message Attributes
~~~~~~~~~~~~~~~~~~

When a command matches, the message object is enriched with:

* ``message.command_name``: The matched command name (e.g. ``"ban"``).
* ``message.command``: List containing ``[command_name, *args]``.
* ``message.command_args``: Raw argument string following the command.
* ``message.args``: Alias for ``command_args``.
* ``message.command_kwargs``: Dictionary of parsed and typed parameters.
* ``message.command_context``: The ``CommandContext`` instance.

Routing Decorators
------------------

TgFlow provides expressive decorators for all Telegram event types:

* ``@bot.command(...)`` / ``@bot.cmd(...)``: Command handler with auto-inference or pattern matching.
* ``@bot.message(when=...)``: Handles incoming messages matching filter conditions.
* ``@bot.callback(data=...)``: Matches callback queries by string or filter.
* ``@bot.inline(when=...)``: Handles inline queries.
* ``@bot.raw()``: Handles raw MTProto payload frames.

When Conditions & Combinators
-----------------------------

Combine conditions naturally using bitwise operators ``&`` (AND), ``|`` (OR), and ``~`` (NOT):

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
