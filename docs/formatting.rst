Rich Message Formatting
========================

TgFlow supports all Telegram text styling entities, including modern Telegram features like expandable blockquotes, spoilers, and custom emoji.

HTML Tags
---------

.. list-table::
   :header-rows: 1

   * - Style
     - HTML Tag
     - Entity Type
   * - Bold
     - ``<b>text</b>``
     - ``MessageEntityBold``
   * - Italic
     - ``<i>text</i>``
     - ``MessageEntityItalic``
   * - Underline
     - ``<u>text</u>``
     - ``MessageEntityUnderline``
   * - Strikethrough
     - ``<s>text</s>``
     - ``MessageEntityStrike``
   * - Code
     - ``<code>code</code>``
     - ``MessageEntityCode``
   * - Preformatted
     - ``<pre>code</pre>``
     - ``MessageEntityPre``
   * - Spoiler
     - ``<tg-spoiler>secret</tg-spoiler>``
     - ``MessageEntitySpoiler``
   * - Blockquote
     - ``<blockquote>quote</blockquote>``
     - ``MessageEntityBlockquote``
   * - Expandable Blockquote
     - ``<blockquote expandable>text</blockquote>``
     - ``MessageEntityExpandableBlockquote``
   * - Custom Emoji
     - ``<tg-emoji emoji-id="123">🔥</tg-emoji>``
     - ``MessageEntityCustomEmoji``
   * - Clickable Link
     - ``<a href="https://example.com">link</a>``
     - ``MessageEntityTextUrl``

Formatting Helpers
------------------

Use convenient helper functions from ``tgflow.formatting``:

.. code-block:: python

   from tgflow import formatting

   text = (
       formatting.bold("Announcement:") + "\n\n" +
       formatting.expandable_blockquote("This is a collapsed expandable blockquote that users can expand.") + "\n\n" +
       formatting.spoiler("Hidden spoiler content")
   )

   await message.reply(text, parse_mode="html")
