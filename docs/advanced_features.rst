Advanced Features & Modern MTProto Updates
=============================================

TgFlow provides direct native support for modern Telegram MTProto updates (Layer 1 through **Layer 225**), including typed RPC error handling, rich message builders, AI composing, ephemeral timers, and Telegram Premium integrations.

MTProto RPC Error Handling (Layer 1–225)
----------------------------------------

TgFlow automatically parses raw MTProto RPC failure codes and error strings into type-safe, granular Python exceptions:

.. list-table::
   :widths: 15 35 50
   :header-rows: 1

   * - HTTP Code
     - Exception Class
     - Common Causes / MTProto Error Strings
   * - **400**
     - ``BadRequest``
     - ``PEER_ID_INVALID``, ``MESSAGE_NOT_MODIFIED``, ``MESSAGE_EMPTY``, ``MEDIA_INVALID``, ``CHANNEL_PRIVATE``, ``TOPIC_CLOSED``, ``PREMIUM_ACCOUNT_REQUIRED``
   * - **401**
     - ``Unauthorized``
     - ``SESSION_PASSWORD_NEEDED`` (2FA), ``AUTH_KEY_UNREGISTERED``, ``USER_DEACTIVATED``, ``SESSION_REVOKED``
   * - **403**
     - ``Forbidden``
     - ``CHAT_WRITE_FORBIDDEN``, ``CHAT_SEND_MEDIA_FORBIDDEN``, ``USER_RESTRICTED``, ``USER_BANNED_IN_CHANNEL``
   * - **406**
     - ``NotAcceptable``
     - ``AUTH_KEY_DUPLICATED``, ``FILEREF_UPGRADE_NEEDED``
   * - **420**
     - ``FloodWait``
     - ``FLOOD_WAIT_X``, ``SLOWMODE_WAIT_X``, ``FLOOD_PREMIUM_WAIT_X``. Exposes ``.seconds`` attribute with exact penalty duration.
   * - **500**
     - ``InternalServerError``
     - ``RPC_CALL_FAIL``, ``INTERDC_CALL_ERROR``

Graceful Flood Handling Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from tgflow import TgFlow, FloodWait, ChatAdminRequired

   async def send_broadcast(bot: TgFlow, chat_ids: list[int], text: str):
       for chat_id in chat_ids:
           try:
               await bot.send_message(chat_id, text)
           except FloodWait as e:
               print(f"Rate limited by Telegram DC. Sleeping for {e.seconds} seconds...")
               await asyncio.sleep(e.seconds)
               await bot.send_message(chat_id, text)
           except ChatAdminRequired:
               print(f"Skipping chat {chat_id}: Admin rights required.")

Fluent Rich Text Builder (``RichText``)
---------------------------------------

Construct rich text with custom animated emojis, expandable blockquotes, and spoilers without managing fragile HTML tag nesting:

.. code-block:: python

   from tgflow import TgFlow, RichText

   bot = TgFlow("bot_session", api_id=12345, api_hash="0123456789abcdef0123456789abcdef")

   @bot.command("rich")
   async def on_rich(cli, msg):
       content = (
           RichText("Announcing ")
           .bold("TgFlow 2.0")
           .text(" featuring ")
           .custom_emoji("🚀", emoji_id=543210987654321)
           .line()
           .line()
           .blockquote(
               "TgFlow delivers pure Python MTProto 2.0 without bloat.\n"
               "Fully compatible with Layer 225 specifications.",
               collapsed=True,  # Expandable Blockquote (Layer 180+)
           )
           .line()
           .text("Confidential access code: ")
           .spoiler("BETA-2026-TOKEN")
       )

       # RichText can be passed directly to send_message
       await msg.reply(content)

AI Compose & Text Assistant (``AIComposer``)
--------------------------------------------

TgFlow provides high-level text drafting, summarization, and translation tools leveraging Telegram's native text translation RPCs:

.. code-block:: python

   from tgflow import AIComposer

   # Generate a structured draft with tone formatting
   draft = AIComposer.compose(
       prompt="Scheduled system maintenance tonight from 02:00 to 03:00 UTC",
       tone="professional",
       bullet_points=True,
   )

   # Summarize long text articles into numbered key points
   summary = AIComposer.summarize(long_article_text, max_points=3)

   # Translate message via MTProto translateText RPC
   translated = await bot.translate_text("Привет мир", to_lang="en")

Ephemeral & View-Once Messages
------------------------------

Send auto-deleting ephemeral messages or configure chat-wide self-destruct timers:

.. code-block:: python

   # Send self-destructing ephemeral message
   await bot.send_ephemeral(
       chat_id=123456789,
       text="This message will self-destruct in 10 seconds.",
       ttl_seconds=10,
   )

   # Configure chat auto-delete timer (e.g. 1 day = 86400 seconds)
   await bot.set_chat_ttl(chat_id=123456789, period=86400)

Telegram Premium Features (Layer 140–225)
-----------------------------------------

* **Custom Animated Emoji Reactions**: Use ``ReactionTypeCustomEmoji(custom_emoji_id="...")`` to react with Telegram Premium emojis.
* **Expandable Blockquotes**: ``RichText.blockquote(text, collapsed=True)`` generates native Telegram collapsible quotes.
* **Star Gifts & Paid Media**: Direct compatibility with Telegram Stars paid media (``PaidMedia``) and gift items (``Gift``).
* **Booster Recognition**: Inspect channel boost thresholds with ``chat.boosts_count``.
