MTProto 2.0 & Official Schema Specifications
=============================================

TgFlow implements the MTProto 2.0 protocol and official Telegram API schema directly in pure Python without external native wrappers.

Official Telegram Schema
------------------------

TgFlow compiles 100% of the official Telegram schema from `core.telegram.org/schema <https://core.telegram.org/schema>`_:

* **1,573 TL Types**: Complete data structures including peers, users, chats, channels, media, stickers, messages, and reactions.
* **783 RPC Functions**: Full RPC requests covering messages, channels, phone calls, auth, contacts, account, users, photos, and upload operations.
* **Over 2,350 Registered Constructors**: Registered in the global ``REGISTRY`` for binary serialization and deserialization.

MTProto Schema Browser Coverage
-------------------------------

TgFlow incorporates constructors and methods detailed in the `Telegram MTProto Browser <https://core.telegram.org/mtproto/browser>`_:

* **Animated Dice & Slot Reel Scrolling**: Supports ``inputMediaDice`` and ``messageMediaDice`` with emojis such as ``🎲``, ``🎯``, ``🏀``, ``⚽``, ``🎳``, and the slot machine ``🎰`` with animated reel scroll simulation.
* **Full-Screen Message Effects**: Supports ``messages.getAvailableEffects``, returning ``availableEffect`` objects with animated sticker assets and sound effects.
* **Animated Reactions**: Supports ``messages.getAvailableReactions`` and ``messages.sendReaction`` for standard, premium, and custom animated emoji reactions.
* **Group Calls & Streaming**: Full VoIP and WebRTC coordination types including ``PhoneCallProtocol``, ``GroupCallParticipant``, and payload transport.
* **AI Compose Tones**: Support for ``AiComposeTone`` structures for assisted drafting.

Obfuscated2 Transport Framing
-----------------------------

To prevent deep packet inspection (DPI) and protocol fingerprinting, TgFlow wraps all TCP streams in Obfuscated2 framing:

1. A 64-byte pseudorandom header is generated on connection startup.
2. The header guarantees non-reserved initial bytes (avoiding ``0xef``, ``HEAD``, ``POST``, ``GET``).
3. Symmetric AES-CTR 128-bit ciphers are initialized for separate send and receive streams.
4. Intermediate framing (``0xeeeeeeee``) handles 4-byte length-delimited payload packets.

Diffie-Hellman Key Exchange
---------------------------

During authentication handshake:

1. Client sends ``req_pq_multi`` with a 128-bit random nonce.
2. Server responds with ``resPQ`` containing the 64-bit composite number ``pq``.
3. TgFlow factors ``pq`` into primes ``p`` and ``q`` using Pollard's rho algorithm in sub-millisecond time.
4. Server DH parameters are validated and the 2048-bit shared secret ``auth_key`` is computed via ``pow(g_b, a, dh_prime)``.

Message Encryption and Integrity
--------------------------------

Every encrypted MTProto 2.0 packet consists of:

* ``auth_key_id`` (8 bytes): Lower 64 bits of ``SHA1(auth_key)``.
* ``msg_key`` (16 bytes): Middle 16 bytes of ``SHA256(auth_key_part + plaintext + padding)``.
* ``ciphertext``: AES-256 IGE encrypted block using keys derived from ``auth_key`` and ``msg_key``.

Message IDs and Ordering
------------------------

Client message IDs are monotonically strictly increasing 64-bit integers with the lowest bit set to 1 (odd for client messages, even for server responses).

UI Scroll Indicator & Navigation
--------------------------------

TgFlow documentation features a custom animated scroll rail on the right margin with dynamic position tracking and smooth scrolling matching high-end documentation layouts.
