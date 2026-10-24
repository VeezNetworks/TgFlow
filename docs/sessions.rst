Session Management
==================

TgFlow features a portable, tamper-evident session format with CRC32 integrity verification.

Session String Structure
------------------------

A TgFlow session string contains:

* **Prefix**: ``tgflow_live_`` for production DCs or ``tgflow_test_`` for test DCs.
* **Payload**:
  * DC ID (1 byte)
  * Port (2 bytes)
  * Bot flag (1 byte)
  * User ID (8 bytes)
  * Server IP length and IP string
  * 2048-bit Authentication Key (256 bytes)
  * CRC32 Checksum (4 bytes)

Exporting and Importing
-----------------------

Exporting a session:

.. code-block:: python

   from tgflow import TgFlow

   client = TgFlow(session="my_session", api_id=12345, api_hash="abcdef")
   # after client is started and auth_key is established
   token = client.export_session_string()
   print(token)

Reusing the exported string on serverless or cloud platforms:

.. code-block:: python

   client = TgFlow(session=token)
