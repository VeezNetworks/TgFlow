Raw MTProto Namespaces & Types
==============================

TgFlow exposes every official Telegram MTProto constructor and RPC method via ``tgflow.raw`` and ``tgflow.tl``, giving you complete low-level control while adhering to official Telegram MTProto specifications.

Architecture & Organization
---------------------------

Telegram's API is divided into distinct namespaces. In TgFlow, all 783 API functions and 1,573 types from Layer 225 are organized by namespace under:

* ``tgflow.raw.functions.<namespace>``: RPC functions for calling Telegram servers.
* ``tgflow.raw.types.<namespace>``: Return types and payload data structures.
* ``tgflow.tl.types.mtproto``: Core MTProto transport and handshake types.
* ``tgflow.tl.functions.mtproto``: Core MTProto transport RPCs (e.g. ``ReqPqMulti``, ``Ping``, ``DestroySession``).
* ``tgflow.tl.types.end_to_end``: Secret Chats end-to-end encrypted message constructors.

Namespace Reference (24 API Namespaces)
---------------------------------------

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Namespace
     - Methods
     - Description & Key Functions
   * - ``account``
     - 123
     - Account settings, privacy rules, 2FA cloud passwords, wallpapers, profile info, business hours.
   * - ``aicompose``
     - 7
     - AI compose tones, styles, and prompt examples (``GetTones``, ``GetToneExample``, ``CreateTone``).
   * - ``auth``
     - 26
     - User and bot authentication, QR login, password verification, signup, authorization export/import.
   * - ``bots``
     - 37
     - Bot commands, menu buttons, descriptions, custom bot info, web app verification.
   * - ``channels``
     - 58
     - Channel and supergroup administration, forum topics, participant permissions, invite links.
   * - ``chatlists``
     - 11
     - Shared chat folder invite links, join requests, filter subscriptions.
   * - ``contacts``
     - 28
     - Contact list management, username resolution (``ResolveUsername``), top peers.
   * - ``folders``
     - 1
     - Peer folder organization and sorting (``EditPeerFolders``).
   * - ``fragment``
     - 1
     - Fragment collectible numbers and usernames lookup (``GetCollectibleInfo``).
   * - ``help``
     - 25
     - Datacenter configuration (``GetConfig``), app updates, terms of service, reporting.
   * - ``langpack``
     - 5
     - Localization packs, translations, and localized strings.
   * - ``messages``
     - 255
     - Sending, editing, deleting, forwarding, searching messages, inline queries, reactions, effects.
   * - ``payments``
     - 65
     - Telegram Stars balance, Star gifts, recurring subscriptions, invoices, and payment forms.
   * - ``phone``
     - 43
     - VoIP 1-on-1 calls, group voice chats, live video broadcasts, WebRTC parameters.
   * - ``photos``
     - 5
     - Profile photos, avatar uploads, and deletion.
   * - ``premium``
     - 5
     - Telegram Premium subscriptions, channel boosts, and gift codes.
   * - ``smsjobs``
     - 7
     - Telegram SMS Gateway peer-to-peer relay jobs (``IsEligibleToJoin``, ``GetSmsJob``, ``FinishJob``).
   * - ``stats``
     - 8
     - Supergroup and broadcast channel engagement statistics and graphs.
   * - ``stickers``
     - 11
     - Custom sticker sets, animated dice configurations, suggested stickers.
   * - ``stories``
     - 33
     - Telegram Stories posting, views, expiration timers, privacy settings, reactions.
   * - ``updates``
     - 3
     - Difference fetching and sequence synchronization (``GetDifference``, ``GetState``).
   * - ``upload``
     - 8
     - Low-level file uploads and downloads (``SaveFilePart``, ``GetFile``, ``SaveBigFilePart``).
   * - ``users``
     - 7
     - User profiles, full user objects (``GetFullUser``), secure value verification.
   * - ``root``
     - 11
     - Query execution wrappers (``InitConnection``, ``InvokeWithLayer``, ``InvokeWithoutUpdates``).

Invoking Raw Functions
----------------------

You can invoke any raw MTProto RPC function directly using ``client.invoke(request)``:

.. code-block:: python

   from tgflow import TgFlow, raw

   bot = TgFlow("session_name", api_id=12345, api_hash="0123456789abcdef0123456789abcdef")

   async def main():
       await bot.start()

       # Call messages.sendMessage via raw namespace
       req = raw.functions.messages.SendMessage(
           peer=raw.types.InputPeerSelf(),
           message="Hello from raw MTProto!",
           random_id=123456789,
       )
       result = await bot.invoke(req)
       print("Raw result:", result)

       # Check Telegram Stars status
       stars_req = raw.functions.payments.GetStarsStatus(
           peer=raw.types.InputPeerSelf()
       )
       stars_status = await bot.invoke(stars_req)
       print("Stars balance:", stars_status.balance)

MTProto Core Handshake & Transport
----------------------------------

TgFlow implements the pure MTProto 2.0 handshake and transport definitions found in `core.telegram.org/schema/mtproto <https://core.telegram.org/schema/mtproto>`_:

.. code-block:: python

   from tgflow.tl import functions as fn, types as tl

   # Step 1: Request PQ with 128-bit nonce
   req_pq = fn.ReqPqMulti(nonce=b"\x00" * 16)
   pq_bytes = req_pq.to_bytes()

   # Step 2: Keep-alive ping
   ping_req = fn.Ping(ping_id=987654321)

   # Step 3: Session termination
   term_req = fn.DestroySession(session_id=11223344)

Secret Chats (End-to-End Encryption)
------------------------------------

Secret chats use the client-to-client MTProto schema from `core.telegram.org/schema/end-to-end <https://core.telegram.org/schema/end-to-end>`_. All 90 constructors are accessible via ``tgflow.tl.types.end_to_end``:

.. code-block:: python

   from tgflow.tl import types as tl

   # Configure secret chat self-destruct timer
   ttl_action = tl.DecryptedMessageActionSetMessageTTL(ttl_seconds=30)

   # Encrypted media payload
   media_photo = tl.DecryptedMessageMediaPhoto(
       thumb=b"...",
       thumb_w=90,
       thumb_h=90,
       w=800,
       h=600,
       size=45000,
       key=b"\x01" * 32,
       iv=b"\x02" * 16,
   )
