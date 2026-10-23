Declarative Routing & Dialogues
=================================

TgFlow eliminates repetitive command argument parsing and complex state machines by providing expressive template matching and inline async dialogue prompts.

Filter Typography: Expressive & Modern (``When`` & ``F``)
---------------------------------------------------------

TgFlow introduces dedicated, human-styled routing typography. Choose between expressive natural sentences with ``When`` or compact modern shorthand with ``F``:

.. code-block:: python

   from tgflow import When, F

   # Natural English phrasing
   @client.on(When.Command("ban") & When.Group)
   async def handle_group_ban(ctx):
       await ctx.reply("Ban workflow initiated.")

   # Concise shorthand
   @client.on(F.command("start") & F.private)
   async def handle_start(ctx):
       await ctx.reply("Welcome to our private bot interface.")

   # Modern Layer 190+ features
   @client.on(When.Stars & When.Private)
   async def handle_stars_payment(ctx):
       await ctx.reply("Thank you for your Telegram Stars!")

   @client.on(F.topic & F.supergroup)
   async def handle_forum_thread(ctx):
       await ctx.reply_in_topic("Replied directly in this forum thread.")

Template Route Syntax
---------------------

Define routes using path-like parameter patterns:

.. code-block:: python

   @client.on("/ban <target> <duration:int=60> <reason*>")
   async def ban_handler(ctx, target, duration: int, reason: str = "Rule violation"):
       """
       Matches:
         /ban @spammer 30 Repeated spam
         /ban 12345678
         /ban (while replying to a user's message)
       """
       await ctx.reply(f"Banning {target} for {duration}m. Reason: {reason}")

Parameter Types
~~~~~~~~~~~~~~~

1. **Named Positional**: ``<target>`` captures a single whitespace-delimited token.
2. **Typed Positional**: ``<duration:int>`` casts the parameter to ``int`` (or ``float``).
3. **Default Value**: ``<duration:int=60>`` applies a default when omitted.
4. **Catch-All**: ``<reason*>`` captures the remainder of the message as a string.

Smart Reply Target Extraction
-----------------------------

When a command expects a target (e.g. ``<target>``) but the user executes the command in reply to another message without typing a username or ID:

.. code-block:: python

   @client.on("/warn <target> <reason*>")
   async def warn_user(ctx, target, reason: str = "Warning"):
       # If invoked as a reply to Alice, `target` is automatically
       # populated with Alice's User object!
       await ctx.reply(f"Warned user ID {target}: {reason}")

TgFlow inspects ``ctx.reply_to`` and extracts the referenced user or sender ID automatically.

Interactive Multi-Turn Dialogues
--------------------------------

Forget about writing external state machines or finite-state automata (FSM) for multi-step prompts. TgFlow allows waiting for user responses directly in the handler flow.

Asking for Input
~~~~~~~~~~~~~~~~

.. code-block:: python

   @client.on("/feedback")
   async def handle_feedback(ctx):
       response = await ctx.ask("Please share your thoughts on the new feature:", timeout=120)
       await ctx.reply(f"Thank you! We received your feedback: {response.text}")

Presenting Choices
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   @client.on("/settings")
   async def handle_settings(ctx):
       choice = await ctx.choose(
           "Select your preferred language:",
           options=["English", "Spanish", "German", "Japanese"]
       )
       await ctx.reply(f"Preference set to {choice}.")
