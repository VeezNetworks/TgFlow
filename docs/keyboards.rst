Keyboards & Callback Queries
============================

TgFlow introduces a dedicated, modern declarative markup system via **``FlowMarkup``** and **``FlowButton``**, supporting every Telegram keyboard evolution from Layer 1 through **Layer 225**.

Key Features
------------

* **Native MTProto 2.0 Binary Mapping**: Translates directly into official Telegram TL objects (``ReplyInlineMarkup``, ``ReplyKeyboardMarkup``, ``KeyboardButton*``).
* **Grid Auto-Layout**: Easily arrange arbitrary buttons into responsive grids with ``FlowMarkup.grid(buttons, cols=2)``.
* **Layer 180+ & 190+ Capabilities**: First-class support for **One-Click Text Copying** (``copy_text``), **User Profile Deep-Linking** (``user_id``), and **Telegram Mini Apps** (``web_app``).
* **Asynchronous Callback Answering**: Built-in alert toasts, URL redirects, and cache time negotiation via ``query.answer()``.

Inline Keyboards (FlowMarkup & FlowButton)
------------------------------------------

Basic Grid Layout
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from tgflow import TgFlow, FlowMarkup, FlowButton

   bot = TgFlow("bot_session", api_id=12345, api_hash="0123456789abcdef0123456789abcdef")

   @bot.command("menu")
   async def show_menu(cli, msg):
       markup = FlowMarkup.grid([
           FlowButton.data("Settings", "settings"),
           FlowButton.data("Help", "help"),
           FlowButton.url("Website", "https://veez.net"),
           FlowButton.copy("Copy Referral", "REF_TGFLOW_2026"),
           FlowButton.web_app("Open MiniApp", "https://app.veez.net"),
           FlowButton.user("Support Agent", 987654321),
       ], cols=2)

       await msg.reply("Welcome to TgFlow Control Center:", reply_markup=markup)

Manual Row Layout
~~~~~~~~~~~~~~~~~

.. code-block:: python

   markup = FlowMarkup.inline([
       FlowMarkup.row(
           FlowButton.data("Accept", "order_accept"),
           FlowButton.data("Decline", "order_decline"),
       ),
       FlowMarkup.row(
           FlowButton.copy("Promo Code", "TGFLOW50"),
       ),
   ])

Handling Callback Queries
-------------------------

TgFlow provides intuitive event listeners for inline button clicks:

.. code-block:: python

   from tgflow import F

   # Match exact callback data
   @bot.callback("settings")
   async def on_settings(cli, query):
       # Show pop-up alert
       await query.answer("Opening settings...", show_alert=False)
       await query.edit_message_text("Settings Panel:\n- Notifications: ON\n- Theme: Dark")

   # Match using regex or filter expression
   @bot.callback(F.data.startswith("order_"))
   async def on_order_action(cli, query):
       action = query.data.split("_")[1]
       if action == "accept":
           await query.answer("Order accepted successfully!", show_alert=True)
           await query.edit_message_text("Order Status: CONFIRMED")
       else:
           await query.answer("Order declined.", show_alert=True)
           await query.edit_message_text("Order Status: CANCELLED")

Reply Keyboards
---------------

Persistent and resizable custom input keyboards:

.. code-block:: python

   reply_kb = FlowMarkup.reply([
       [FlowButton.text("Send Contact"), FlowButton.text("Share Location")],
       [FlowButton.contact("Verify Phone"), FlowButton.location("Live Location")],
   ], resize=True, persistent=True, placeholder="Select an option...")

   await msg.reply("Choose verification step:", reply_markup=reply_kb)

Removing Reply Keyboards
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   await msg.reply("Keyboard closed.", reply_markup=FlowMarkup.remove())

Force Reply
~~~~~~~~~~~

.. code-block:: python

   await msg.reply("Please type your username:", reply_markup=FlowMarkup.force_reply(placeholder="@username"))

Button Type Catalog (Layer 1–225)
---------------------------------

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Constructor
     - Method Signature
     - Description
   * - **Callback**
     - ``FlowButton.data(text, callback_data)``
     - Triggers an inline callback query to the bot.
   * - **URL**
     - ``FlowButton.url(text, url)``
     - Opens an external hyperlink or Telegram deep-link.
   * - **Copy Text**
     - ``FlowButton.copy(text, copy_text)``
     - Copies specified text to user clipboard in one click (Layer 180+).
   * - **User Profile**
     - ``FlowButton.user(text, user_id)``
     - Directly opens a user profile card by user ID (Layer 190+).
   * - **Web App**
     - ``FlowButton.web_app(text, url)``
     - Launches an interactive Telegram Mini App inside the client.
   * - **Switch Inline**
     - ``FlowButton.switch_inline(text, query, current_chat)``
     - Prompts user to choose a chat and inserts inline query.
   * - **Contact**
     - ``FlowButton.contact(text)``
     - Requests phone number verification via reply keyboard.
   * - **Location**
     - ``FlowButton.location(text)``
     - Requests geographic GPS coordinates from user.
   * - **Poll**
     - ``FlowButton.poll(text, poll_type)``
     - Prompts user to create and send a poll / quiz.
