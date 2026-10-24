Authentication & Userbots
===========================

TgFlow provides full MTProto authentication capabilities for both **Userbots** (logging in via phone number, SMS / Telegram login codes, and 2FA cloud passwords) and **Bot Accounts** (authenticating via Botfather tokens).

Interactive User Login
----------------------

Signing into a user account over MTProto follows a standard three-stage flow:

1. **Send Verification Code**
   Request a confirmation code to the user's phone number via Telegram or SMS.
2. **Sign In with Code**
   Verify the received numeric code together with the ``phone_code_hash``.
3. **2-Step Verification (2FA)**
   If a Cloud Password is set on the account, complete the Diffie-Hellman SRP handshake to finalize login.

Full Authentication Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   from tgflow import TgFlow

   async def main():
       # Initialize client with API credentials from my.telegram.org
       client = TgFlow(
           session="user_session",
           api_id=1234567,
           api_hash="0123456789abcdef0123456789abcdef",
       )
       await client.connect()

       phone = "+1234567890"

       # 1. Request verification code
       sent_code = await client.send_code(phone)
       print(f"Code sent! Timeout: {sent_code.timeout}s")

       code = input("Enter the login code you received: ")

       try:
           # 2. Attempt login
           auth = await client.sign_in(
               phone_number=phone,
               phone_code_hash=sent_code.phone_code_hash,
               phone_code=code,
           )
           print(f"Successfully logged in as {client.me.first_name} (@{client.me.username})")

       except Exception as e:
           # 3. Check if 2FA password is required
           if "PASSWORD_HASH_INVALID" in str(e) or "SESSION_PASSWORD_NEEDED" in str(e):
               password = input("Enter your 2FA Cloud Password: ")
               auth = await client.check_password(password)
               print(f"Successfully logged in with 2FA as {client.me.first_name}")
           else:
               raise

       # 4. Export session string for headless deployment
       session_string = client.export_session_string()
       print(f"Portable Session String: {session_string}")

   if __name__ == "__main__":
       asyncio.run(main())

Signing Up New Users
--------------------

If the phone number is not registered yet, Telegram requires first and last names to create the account:

.. code-block:: python

   auth = await client.sign_up(
       phone_number=phone,
       phone_code_hash=sent_code.phone_code_hash,
       first_name="Alice",
       last_name="Smith",
   )

Resending and Cancelling Codes
------------------------------

.. code-block:: python

   # Request code via alternative channel (e.g. phone call or SMS)
   await client.resend_code(phone_number=phone, phone_code_hash=sent_code.phone_code_hash)

   # Cancel pending authorization code
   await client.cancel_code(phone_number=phone, phone_code_hash=sent_code.phone_code_hash)

Logging Out & Terminating Sessions
----------------------------------

.. code-block:: python

   # Invalidate current session on Telegram servers
   await client.log_out()

Bot Token Authentication
------------------------

For standard Telegram bots, supply ``bot_token`` directly to ``TgFlow``:

.. code-block:: python

   bot = TgFlow(
       session="my_bot",
       api_id=1234567,
       api_hash="0123456789abcdef0123456789abcdef",
       bot_token="123456789:ABCdefGHIjklMNOpqrSTUvwxYZ",
   )

   @bot.command("start")
   async def on_start(cli, message):
       await message.reply("Bot is online via MTProto 2.0!")

   bot.run()

Low-Level MTProto Raw RPC
-------------------------

Direct raw access is available via ``tgflow.raw.functions.auth``:

* ``raw.functions.auth.SendCode``
* ``raw.functions.auth.SignIn``
* ``raw.functions.auth.SignUp``
* ``raw.functions.auth.CheckPassword``
* ``raw.functions.auth.LogOut``
* ``raw.functions.auth.ResendCode``
* ``raw.functions.auth.CancelCode``
* ``raw.functions.auth.ExportAuthorization``
* ``raw.functions.auth.ImportAuthorization``
