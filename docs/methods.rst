Client Methods & Operations
===========================

TgFlow provides an ergonomic suite of high-level client methods that map directly to MTProto 2.0 RPC calls.

Authentication & Profile
------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``send_code(phone_number)``
     - Requests a login verification code via Telegram or SMS.
   * - ``sign_in(phone_number, phone_code_hash, phone_code)``
     - Completes login with the received code.
   * - ``sign_up(phone_number, phone_code_hash, first_name, last_name)``
     - Registers a new user account.
   * - ``check_password(password)``
     - Authenticates 2-Step Verification Cloud Password.
   * - ``resend_code(phone_number, phone_code_hash)``
     - Resends verification code via alternative channel.
   * - ``cancel_code(phone_number, phone_code_hash)``
     - Cancels pending authentication code.
   * - ``log_out()``
     - Terminates the session on Telegram servers.
   * - ``get_me()``
     - Returns information about the current authenticated user/bot.
   * - ``update_profile(first_name, last_name, about)``
     - Updates account name and bio.
   * - ``update_status(offline)``
     - Sets online/offline presence status.

Messaging & Content
-------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``send_message(chat_id, text, ...)``
     - Sends text messages with rich formatting, spoilers, blockquotes, and reply quotes.
   * - ``edit_message_text(chat_id, message_id, text, ...)``
     - Edits existing message content and inline markup.
   * - ``delete_messages(chat_id, message_ids, revoke=True)``
     - Deletes one or multiple messages for all participants.
   * - ``forward_messages(from_chat_id, to_chat_id, message_ids)``
     - Forwards messages between chats with optional author anonymity.
   * - ``read_history(chat_id, max_id)``
     - Marks chat messages as read up to ``max_id``.
   * - ``send_reaction(chat_id, message_id, emoji)``
     - Reacts to a message with standard or custom emoji.
   * - ``set_typing(chat_id, action)``
     - Broadcasts typing, recording, or uploading presence indicator.

Media & Interactive Content
---------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``send_photo(chat_id, photo, caption, ...)``
     - Sends compressed photo image files.
   * - ``send_video(chat_id, video, caption, ...)``
     - Sends MP4/MKV video files with streaming attributes.
   * - ``send_audio(chat_id, audio, performer, title, ...)``
     - Sends music tracks with ID3 tags.
   * - ``send_voice(chat_id, voice, duration, waveform, ...)``
     - Sends voice notes encoded in OGG Opus format.
   * - ``send_document(chat_id, document, caption, ...)``
     - Sends arbitrary file attachments.
   * - ``send_animation(chat_id, animation, caption, ...)``
     - Sends soundless MP4 animations and GIFs.
   * - ``send_dice(chat_id, emoji)``
     - Rolls animated dice, dartboard, basketball, football, bowling, or slot machine (``🎰``).
   * - ``send_ephemeral(chat_id, text, ttl_seconds, ...)``
     - Sends auto-deleting ephemeral messages with self-destruct timers.

Stories & Highlights
--------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``send_story(chat_id, media, caption, period, ...)``
     - Posts a new story with custom privacy rules and expiration duration.
   * - ``edit_story(chat_id, story_id, media, caption, ...)``
     - Updates media or caption on an active story.
   * - ``delete_stories(chat_id, story_ids)``
     - Deletes stories by ID.
   * - ``get_stories(chat_id, story_ids)``
     - Retrieves full story objects.
   * - ``get_peer_stories(chat_id)``
     - Fetches active stories posted by a peer.
   * - ``get_story_views(chat_id, story_id)``
     - Fetches view list and reactions for a story.

Stars, Gifts & Collectibles
---------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``get_stars_status(peer)``
     - Checks Telegram Stars balance and status.
   * - ``get_stars_transactions(peer, offset, limit)``
     - Retrieves history of Stars purchases and gifts.
   * - ``get_star_gifts(hash)``
     - Lists all currently available collectible and standard gifts.
   * - ``send_star_gift(peer, gift_id, hide_name, message)``
     - Sends a Telegram Star gift to a peer.
   * - ``get_collectible_info(type, query)``
     - Queries Fragment collectible numbers or usernames.

Bots & Mini Apps
----------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``set_bot_commands(commands, scope, language_code)``
     - Registers command suggestions in the bot command menu.
   * - ``get_bot_commands(scope, language_code)``
     - Fetches active bot command list.
   * - ``delete_bot_commands(scope, language_code)``
     - Resets bot commands to default.
   * - ``set_bot_menu_button(user_id, menu_button)``
     - Sets custom web app or default menu button for users.
   * - ``get_bot_menu_button(user_id)``
     - Retrieves active menu button for a chat.
   * - ``set_bot_info(bot, lang_code, name, about, description)``
     - Updates bot descriptive text, about, and display name.
   * - ``get_bot_info(bot, lang_code)``
     - Fetches bot profile description.
   * - ``answer_web_app_query(web_app_query_id, result)``
     - Delivers result of Mini App query to chat.

Stickers, Reactions & Effects
-----------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``get_available_effects(hash)``
     - Fetches full-screen animated message effects.
   * - ``get_available_reactions(hash)``
     - Retrieves available standard, premium, and custom emoji reactions.
   * - ``set_default_reaction(reaction)``
     - Configures default quick-reaction emoji.
   * - ``get_sticker_set(stickerset, hash)``
     - Retrieves sticker pack details and items.
   * - ``get_custom_emoji_stickers(document_ids)``
     - Fetches custom emoji sticker objects.

Channels & Administration
-------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``create_channel(title, about, megagroup=True)``
     - Creates a new supergroup or broadcast channel.
   * - ``join_channel(channel)``
     - Joins a public or private channel.
   * - ``leave_channel(channel)``
     - Leaves a chat or channel.
   * - ``get_chat(chat_id)``
     - Fetches chat details, photo, and permissions.
   * - ``ban_chat_member(chat_id, user_id, until_date)``
     - Removes and blacklists a member from a chat.
   * - ``unban_chat_member(chat_id, user_id)``
     - Lifts bans and allows rejoining.
   * - ``restrict_chat_member(chat_id, user_id, permissions)``
     - Granularly restricts media, link, or message sending rights.
   * - ``promote_chat_member(chat_id, user_id, ...)``
     - Grants custom admin privileges and titles.
   * - ``export_chat_invite_link(chat_id)``
     - Generates a new primary invite link.

Voice & Video Calls
-------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``request_call(user_id, g_a_hash, video=False)``
     - Initiates 1-on-1 E2EE Diffie-Hellman call.
   * - ``accept_call(call, g_b)``
     - Accepts incoming call with public key exchange.
   * - ``confirm_call(call, g_a, key_fingerprint)``
     - Finalizes E2EE verification and initiates media stream.
   * - ``discard_call(call, duration, reason)``
     - Hangs up or rejects 1-on-1 call.
   * - ``create_group_call(chat_id, title, rtmp_stream)``
     - Launches supergroup voice chat or live video broadcast.
   * - ``join_group_call(call, params, muted)``
     - Connects WebRTC SDP session to voice chat.
   * - ``leave_group_call(call)``
     - Disconnects from voice chat.
   * - ``get_group_call_participants(call, limit)``
     - Fetches active speaker list and states.
   * - ``edit_group_call_participant(call, participant, ...)``
     - Mutes, unmutes, or adjusts volume of participants.
   * - ``invite_to_group_call(call, users)``
     - Invites peers to join voice chat.

Privacy, Folders & Gateway Jobs
-------------------------------

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Method
     - Description
   * - ``get_privacy_rules(key)``
     - Retrieves privacy rules for phone, last seen, forwards, etc.
   * - ``set_privacy_rules(key, rules)``
     - Updates privacy rules with allow/disallow lists.
   * - ``get_dialog_filters()``
     - Fetches user folder tabs.
   * - ``update_dialog_filter(filter_id, filter_obj)``
     - Updates custom chat folder filter.
   * - ``check_chatlist_invite(slug)``
     - Validates shared chat folder invite link.
   * - ``join_chatlist_invite(slug, peers)``
     - Joins shared folder and selected chats.
   * - ``leave_chatlist(chatlist, peers)``
     - Leaves shared folder.
   * - ``is_sms_job_eligible()``
     - Checks eligibility for Telegram SMS gateway relay.
   * - ``get_sms_job()``
     - Retrieves pending SMS verification job.
   * - ``finish_sms_job(job_id, error)``
     - Confirms delivery of SMS gateway message.

Raw Namespaces Reference
------------------------

In addition to client methods, all 783 API functions and 1,573 types are accessible via ``tgflow.raw``:

* **Functions**: ``raw.functions.messages.*``, ``raw.functions.channels.*``, ``raw.functions.auth.*``, ``raw.functions.phone.*``, ``raw.functions.payments.*``, ``raw.functions.stories.*``, ``raw.functions.aicompose.*``, ``raw.functions.chatlists.*``, ``raw.functions.smsjobs.*``, etc.
* **Types**: ``raw.types.messages.*``, ``raw.types.channels.*``, ``raw.types.phone.*``, ``raw.types.auth.*``, etc.
* **MTProto Core**: ``tl.types.mtproto.*`` and ``tl.functions.mtproto.*`` (``ReqPqMulti``, ``ReqDHParams``, ``SetClientDHParams``, ``Ping``, ``DestroySession``, ``RpcDropAnswer``, ``GetFutureSalts``).
* **Secret Chats**: ``tl.types.end_to_end.*`` (``DecryptedMessage``, ``DecryptedMessageService``, etc.).
