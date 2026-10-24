Voice & Video Calls (Layer 1 to 225)
=====================================

TgFlow provides complete MTProto signaling support for both **1-on-1 End-to-End Encrypted (E2EE) Calls** and **Group Voice Chats & Live Video Streams**, tracking every evolution of Telegram's protocol from Layer 1 all the way to **Layer 225**.

Architecture Overview
---------------------

Telegram MTProto call infrastructure operates on two distinct signaling tiers:

1. **1-on-1 Calls (VoIP & Video)**:
   Negotiated via end-to-end encrypted Diffie-Hellman key exchange directly through Telegram's MTProto signaling layer. Audio and video payloads stream via direct peer-to-peer UDP or encrypted Telegram reflector proxies (and WebRTC TURN/STUN).

2. **Group Calls & Channels (Voice Chats & Live Streams)**:
   Coordinated through centralized Selective Forwarding Units (SFUs). Clients exchange WebRTC Session Description Protocol (SDP) payloads serialized in MTProto ``DataJSON`` structures.

Evolution: Layer 1 to Layer 225
-------------------------------

The table below outlines the chronological evolution of Telegram call capabilities across MTProto layers, all fully supported in TgFlow:

.. list-table::
   :widths: 15 25 60
   :header-rows: 1

   * - Layers
     - Protocol Version
     - Key Capabilities & TL Constructors
   * - **Layer 1 – 64**
     - MTProto 1.0 / Legacy
     - Text, media, and peer data transport. Voice calls were not yet part of native MTProto; audio was communicated via voice messages.
   * - **Layer 65 – 82**
     - VoIP 1.0 (E2EE Audio)
     - Introduction of the ``phone.*`` RPC namespace. Added ``phone.requestCall``, ``phone.acceptCall``, ``phone.confirmCall``, and ``phone.discardCall``. Diffie-Hellman key exchange (2048-bit MODP), visual 4-emoji key fingerprint verification, and UDP reflector proxies (``PhoneConnection``).
   * - **Layer 83 – 110**
     - VoIP 2.0 (libtgvoip)
     - Multi-version library negotiation via ``PhoneCallProtocol`` (``min_layer`` / ``max_layer``). Introduction of user rating feedback via ``phone.setCallRating`` and diagnostic dump uploads via ``phone.saveCallDebug``.
   * - **Layer 111 – 120**
     - Group Calls 1.0
     - Launch of Group Voice Chats in Supergroups and Channels. Introduction of ``phone.createGroupCall``, ``phone.joinGroupCall``, ``phone.leaveGroupCall``, and ``phone.getGroupParticipants``. Dynamic participant volume control and mute state via ``phone.editGroupCallParticipant``.
   * - **Layer 121 – 135**
     - Video Calls & Scheduling
     - Added 1-on-1 video support via the ``video`` bitflag. Scheduled group voice chats introduced via ``schedule_date`` and ``phone.startScheduledGroupCall``. Server-side audio recording enabled via ``phone.toggleGroupCallRecord``.
   * - **Layer 136 – 165**
     - RTMP Broadcasts & Stage
     - RTMP live streaming integration for broadcast channels with unlimited audiences (``rtmp_stream:true``). Speaker permissions, raise hand queue management, and resetable invite hashes via ``phone.toggleGroupCallSettings``.
   * - **Layer 166 – 190**
     - WebRTC HD Multi-Stream
     - 1080p screen sharing with system audio. Video stream track identifiers, active speaker notifications, video thumbnail captures, and participant video endpoint bindings (``GroupCallParticipantVideo``).
   * - **Layer 191 – 225**
     - Modern SFU & Unified WebRTC
     - Full WebRTC multi-candidate gathering, TURN/STUN relay endpoints (``PhoneConnectionWebrtc``), low-latency live streaming protocols, camera angle switches, and standardized signaling compatibility for third-party audio engines like Py-TgCalls and NTgCalls.

1-on-1 End-to-End Encrypted Calls
---------------------------------

Diffie-Hellman Handshake
~~~~~~~~~~~~~~~~~~~~~~~~

1-on-1 calls employ a 2048-bit Diffie-Hellman key exchange over MTProto signaling:

1. **Caller (Alice)**:
   * Generates a random 256-byte private exponent :math:`a` and computes :math:`g_a = g^a \pmod{p}`.
   * Computes :math:`g_{a\_hash} = \text{SHA256}(g_a)`.
   * Sends ``request_call(user_id, g_a_hash)``.

2. **Callee (Bob)**:
   * Receives ``PhoneCallRequested``.
   * Generates a random 256-byte private exponent :math:`b` and computes :math:`g_b = g^b \pmod{p}`.
   * Sends ``accept_call(call, g_b)``.

3. **Caller (Alice)**:
   * Receives ``PhoneCallAccepted``.
   * Validates :math:`g_b` and calculates the shared secret key :math:`K = (g_b)^a \pmod{p}`.
   * Computes the 64-bit key fingerprint :math:`\text{fingerprint} = \text{SHA256}(K)[:8]`.
   * Sends ``confirm_call(call, g_a, key_fingerprint)``.

4. **Media Session**:
   * Both endpoints receive ``PhoneCall`` containing connection endpoints: either direct UDP peer-to-peer reflectors (``PhoneConnection``) or WebRTC TURN/STUN relays (``PhoneConnectionWebrtc``).

Signaling Example
~~~~~~~~~~~~~~~~~

Initiating and confirming a call using TgFlow:

.. code-block:: python

   import os
   from hashlib import sha256
   from tgflow import TgFlow
   from tgflow.tl import types as tl

   bot = TgFlow("bot_session", api_id=12345, api_hash="0123456789abcdef0123456789abcdef")

   async def start_call():
       await bot.start()

       # 1. Generate DH parameters
       dh_a = os.urandom(256)
       g_a = pow(3, int.from_bytes(dh_a, "big"), tl.DH_PRIME_2048).to_bytes(256, "big")
       g_a_hash = sha256(g_a).digest()

       # 2. Request Call
       call = await bot.request_call(
           user_id=987654321,
           g_a_hash=g_a_hash,
           video=False,
       )

       # 3. Discard when finished
       await bot.discard_call(call, duration=42)

Group Calls & Voice Chats
-------------------------

TgFlow provides full management methods for Telegram Group Calls in Supergroups and Channels.

Creating a Voice Chat
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   async def main():
       # Create an immediate voice chat in a supergroup
       group_call = await bot.create_group_call(chat_id=-1001234567890, title="Community Music Lounge")

       # Create a scheduled live stream with RTMP broadcast support
       scheduled_call = await bot.create_group_call(
           chat_id=-1001234567890,
           title="Weekly Keynote",
           rtmp_stream=True,
           schedule_date=1710000000,
       )

Joining a Voice Chat
~~~~~~~~~~~~~~~~~~~~

To join an existing group call and negotiate WebRTC SDP:

.. code-block:: python

   import json

   async def join():
       sdp_offer = {
           "sdp": "v=0\r\no=- 12345 2 IN IP4 127.0.0.1...",
           "type": "offer",
       }

       res = await bot.join_group_call(
           call=group_call_id,
           params=json.dumps(sdp_offer),
           muted=False,
       )

Managing Participants
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Fetch active participants
   participants = await bot.get_group_call_participants(call=group_call_id, limit=50)

   # Mute or change participant volume (10000 = 100%)
   await bot.edit_group_call_participant(
       call=group_call_id,
       participant=987654321,
       volume=12000,
       raise_hand=False,
   )

   # Invite additional users
   await bot.invite_to_group_call(
       call=group_call_id,
       users=[987654321, 112233445],
   )

Integration with Py-TgCalls and NTgCalls
----------------------------------------

TgFlow is explicitly designed to integrate natively with Python WebRTC media engines such as **Py-TgCalls** and **NTgCalls**.

Through the ``tgflow.raw`` module, TgFlow exposes identical TL type and function namespaces expected by call clients:

.. code-block:: python

   from tgflow import TgFlow, raw

   # raw.functions.phone provides all required call signaling primitives:
   # - raw.functions.phone.JoinGroupCall
   # - raw.functions.phone.LeaveGroupCall
   # - raw.functions.phone.GetGroupCall
   # - raw.functions.phone.GetGroupParticipants
   # - raw.functions.phone.EditGroupCallParticipant
   # - raw.functions.phone.CreateGroupCall
   # - raw.functions.phone.DiscardGroupCall

Streaming Audio with Py-TgCalls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from pytgcalls import PyTgCalls
   from pytgcalls.types import AudioPiped
   from tgflow import TgFlow

   client = TgFlow("music_bot", api_id=12345, api_hash="0123456789abcdef0123456789abcdef")
   call_app = PyTgCalls(client)

   @client.command("play")
   async def play_audio(msg):
       chat_id = msg.chat.id
       await call_app.join_group_call(
           chat_id,
           AudioPiped("audio.mp3"),
       )
       await msg.reply("Now streaming audio in voice chat!")

   async def main():
       await client.start()
       await call_app.start()
       await asyncio.Event().wait()

   if __name__ == "__main__":
       asyncio.run(main())
