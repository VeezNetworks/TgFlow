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
     - Uploads and sends compressed or spoiler-masked photos.
   * - ``send_document(chat_id, document, caption, ...)``
     - Sends arbitrary files, archives, and uncompressed media.
   * - ``send_poll(chat_id, question, options, ...)``
     - Creates public or anonymous polls and quizzes.
   * - ``send_dice(chat_id, emoji)``
     - Sends animated dice, dart, basketball, or slot machine emojis.
   * - ``send_location(chat_id, latitude, longitude)``
     - Shares geographic coordinates.
   * - ``send_contact(chat_id, phone_number, first_name, ...)``
     - Shares vCard contact cards.

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
