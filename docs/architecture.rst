Architecture & Cryptography
=============================

TgFlow implements Telegram's MTProto 2.0 transport and security protocol natively using Python asynchronous sockets and standard cryptographic primitives.

.. contents:: Table of Contents
   :local:
   :depth: 2

Transport Layer & Anti-DPI Obfuscation
--------------------------------------

Standard MTProto TCP connections may be intercepted or throttled by network firewalls. TgFlow provides an **Obfuscated2** wrapper (Padded Intermediate transport ``0xdddddddd``) that encrypts the transport framing itself using random AES-CTR streams.

Key features:
* 64-byte random handshake payload with anti-signature verification.
* Bidirectional independent AES-256 CTR state for incoming and outgoing byte streams.
* Prevents deep packet inspection (DPI) from recognizing Telegram transport signatures.

MTProto 2.0 Cryptographic Pipeline
----------------------------------

1. **Pollard's Rho PQ Factorization**:
   Telegram's authorization handshake requires factoring a 64-bit semi-prime `pq` into primes `p` and `q` (`p < q`). TgFlow uses Pollard's rho algorithm with Brent's cycle detection, solving the challenge in sub-millisecond time without external C dependencies.

2. **2048-bit Diffie-Hellman Key Exchange**:
   Generates a safe 2048-bit random exponent `b` and computes the shared authentication key:

   .. math::

      \text{auth\_key} = g_a^b \pmod{p_{dh}}

3. **AES-256 IGE (Infinite Garble Extension)**:
   The core payload encryption of MTProto 2.0 uses AES-256 in IGE mode:

   .. math::

      C_i = E_K(P_i \oplus C_{i-1}) \oplus P_{i-1}

   TgFlow provides a pure-Python and ``cryptography`` backed AES-IGE implementation operating on 16-byte aligned blocks.

4. **Message Key Derivation**:
   For client-to-server messages:

   .. math::

      \text{msg\_key} = \text{SHA256}(\text{auth\_key}_{88..120} + \text{plaintext} + \text{padding})_{0..16}

Telegram Schema Layer 225+
--------------------------

TgFlow integrates modern schemas directly extracted from official TDLib and Telegram API definitions (``tgflow/scheme/``):

* **Telegram Stars & Subscriptions**: Full ecosystem support for paid media purchases, star subscriptions, star giveaways, and star revenue balances (``PaidMedia``, ``PaidReaction``, ``StarSubscription``, ``StarsRevenueStatus``).
* **Telegram Business 2.0**: First-class handling of business connections, business intro cards, opening hours, locations, quick replies, and business bot greetings (``BusinessConnection``, ``BusinessIntro``, ``BusinessLocation``).
* **Stories 2.0**: Full support for personal and channel stories, story albums, story reactions, and story stealth mode (``StoryItem``).
* **Collectible & Upgraded Gifts**: Native types for limited-edition numbered gifts, upgraded gifts, and star gifts (``Gift``).
* **Forum Topics 2.0**: Topic creation, editing, icon formatting, thread-specific message routing, and topic reaction management (``ForumTopic``).
* **Bot Verification & Affiliates**: Custom organization verification badges and affiliate star revenue programs (``BotVerification``, ``AffiliateProgram``).
