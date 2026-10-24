Changelog & Release Notes
=========================

All notable changes and architectural milestones of **TgFlow** are documented here.

Version 1.8.0 (2026-10-24)
--------------------------

**Advanced Command Formatting, Typed Arguments & FlowCommand DSL**

* **Zero-Argument Command Decorator**: Support decorating handlers directly with ``@bot.command`` without parentheses. The command name is automatically inferred from the handler function name (e.g. ``async def start(cli, msg)`` routes ``/start``).
* **Parameterized & Typed Commands**: Declarative command argument parsing via syntax like ``@bot.command("ban <user_id:int> [reason:str]")``. Supports ``int``, ``float``, ``bool``, and ``str`` casting with automatic injection into handler parameter signatures.
* **Automatic Argument Injection**: Handler functions receive typed arguments directly as named parameters (e.g. ``async def ban(client, message, user_id, reason="Spam")``).
* **CommandContext (ctx) Handlers**: Handlers can accept a single ``ctx: CommandContext`` parameter providing ``ctx.reply()``, ``ctx.command``, ``ctx.args``, ``ctx.kwargs``, ``ctx.chat``, and ``ctx.from_user``.
* **Fluent Command / FlowCommand DSL**: Chainable builder ``Command("kick <user_id:int>").desc("...").prefix("!").alias("k").when(...)``.
* **Direct Command Aliases**: Added ``@bot.cmd(...)`` decorator alias for ``@bot.command(...)``.
* **Flexible Prefixes**: Full support for custom prefixes (``/``, ``!``, ``.``), prefix-less commands (``""``), and automatic prefix stripping.
* **Update Enrichment**: Every command update is enriched with ``message.command_name``, ``message.command_args``, ``message.args``, ``message.command_kwargs``, and ``message.command_context``.
* **Automated Unit Tests**: Added comprehensive test suite in ``tests/test_command_formats.py`` verifying all command patterns (67 total tests passing).

Version 1.7.0 (2026-10-24)
--------------------------

**Complete Telegram Browser & MTProto 2.0 Integration**

* **Official MTProto Core Schema**: Integrated all 45 types and 9 core RPC functions from ``core.telegram.org/schema/mtproto`` (``ReqPqMulti``, ``ReqDHParams``, ``SetClientDHParams``, ``RpcDropAnswer``, ``GetFutureSalts``, ``Ping``, ``PingDelayDisconnect``, ``DestroySession``, ``DestroyAuthKey``).
* **Secret Chats End-to-End Encryption**: Added all 90 constructors from ``core.telegram.org/schema/end-to-end`` in ``tgflow.tl.types.end_to_end``.
* **24 Raw Namespaces in ``tgflow.raw``**: Dedicated namespace modules for ``account``, ``aicompose``, ``auth``, ``bots``, ``channels``, ``chatlists``, ``contacts``, ``folders``, ``fragment``, ``help``, ``langpack``, ``messages``, ``payments``, ``phone``, ``photos``, ``premium``, ``smsjobs``, ``stats``, ``stickers``, ``stories``, ``updates``, ``upload``, ``users``, and ``root``.
* **Advanced Client Operations**: Added 25+ high-level methods on ``TgFlow`` for Stories, Telegram Stars, Star gifts, Fragment collectibles, Bot menu buttons, Mini apps, and SMS Gateway verification jobs.
* **Full Test Coverage**: Expanded automated unit test suite to 59 tests covering all namespaces and client methods.

Version 1.6.0 (2026-10-24)
--------------------------

**Official Layer 225 Schema Compilation & Animated Scroll UI**

* **Complete Layer 225 Coverage**: Compiled 100% of ``core.telegram.org/schema`` (1,573 TL types and 783 RPC functions).
* **Modular Code Partitioning**: Partitioned types (13 parts) and functions (6 parts) ensuring all files remain clean and manageable.
* **Animated Scroll Rail**: Added smooth animated vertical scroll tracking rail and TOC scrollspy indicator matching modern documentation UX.
* **Dice Reel Scrolling Animation**: Full support for ``inputMediaDice`` and ``messageMediaDice`` with slot machine animated scroll simulation.
* **Zero Comment Enforcement**: Core library verified with zero comment clutter across all Python files.

Version 1.5.0 (2026-10-24)
--------------------------

**RPC Error Hierarchy, Rich Text & AI Assistant**

* **Typed RPC Error Hierarchy**: Added 130+ granular exception classes mapped directly to MTProto 400, 401, 403, 406, 420, and 500 error strings.
* **FloodWait Precision**: Automatic extraction of penalty duration into ``e.seconds``.
* **Fluent RichText Builder**: Chainable DSL for composing bold, italic, code, underline, strikethrough, spoiler, custom animated emoji, and expandable blockquote entities.
* **AIComposer Tool**: Structured text drafting and summarization helper with native translation RPC integration.
* **Ephemeral Message Timers**: High-level ``send_ephemeral()`` and ``set_chat_ttl()`` methods.

Version 1.4.0 (2026-10-24)
--------------------------

**Group & Channel Administration Suite & FlowMarkup DSL**

* **FlowMarkup DSL**: Fluent inline keyboard builder supporting text, callback, url, web app, switch inline, and copy text buttons.
* **Forum Topics**: Full support for creating, editing, closing, reopening, and deleting forum topic history.
* **Member Moderation**: Added ``ban_chat_member``, ``unban_chat_member``, ``restrict_chat_member``, and ``promote_chat_member``.
* **Dialog & Message History**: Added ``search_messages``, ``get_history``, and ``get_dialogs``.

Version 1.3.0 (2026-10-24)
--------------------------

**VoIP & Group Call Coordination (py-tgcalls / ntgcalls)**

* **Phone RPC Calls**: Native support for ``phone.requestCall``, ``phone.acceptCall``, ``phone.confirmCall``, and ``phone.discardCall``.
* **Group Calls & Live Streams**: Added ``create_group_call``, ``join_group_call``, ``leave_group_call``, and ``edit_group_call_participant``.
* **WebRTC & VoIP Compatibility**: Full protocol negotiation support matching ``py-tgcalls`` and ``ntgcalls`` requirements.

Version 1.2.0 (2026-10-23)
--------------------------

**Formatting DSL & Message Entities**

* **HTML Entity Parser**: Fast entity parser supporting ``<b>``, ``<i>``, ``<code>``, ``<pre>``, ``<s>``, ``<u>``, ``<spoiler>``, ``<blockquote>``, and ``<tg-emoji>``.
* **Collapsible Blockquotes**: Expandable quote support for Layer 180+.
* **Custom Animated Emoji**: Support for Telegram Premium custom animated emoji entities.

Version 1.1.0 (2026-10-23)
--------------------------

**High-Level Client API & Declarative Routing**

* **Decorator Routing**: Added ``@client.on_message()``, ``@client.command()``, and ``@client.on_callback_query()``.
* **Composable Filters**: Declarative filter combinators supporting ``&`` (AND), ``|`` (OR), and ``~`` (NOT).
* **Portable Sessions**: Base64 session string export and import with CRC32 checksums.

Version 1.0.0 (2026-10-23)
--------------------------

**Initial Release: Pure Python MTProto 2.0 Engine**

* **Obfuscated2 Framing**: 64-byte randomized header generation avoiding protocol fingerprinting.
* **AES-256 IGE Encryption**: Pure Python symmetric encryption for encrypted data transport.
* **Diffie-Hellman Key Derivation**: Sub-millisecond Pollard's rho prime factorization and 2048-bit DH key exchange.
* **Binary Serialization**: Fast 4-byte aligned TL reader and writer.
