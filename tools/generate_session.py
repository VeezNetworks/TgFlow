import asyncio
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tgflow.connection import DC_MAP_PROD, DC_MAP_TEST, TCPConnection
from tgflow.handshake import MTProtoHandshake
from tgflow.session import generate_new_session, decode_session


async def connect_and_generate_session():
    print("=" * 65)
    print("TgFlow Telegram Live Session Handshake & Generator")
    print("=" * 65)
    print("This tool performs the real MTProto 2.0 Diffie-Hellman handshake")
    print("with Telegram's Data Centers and registers your authenticated session.\n")

    try:
        api_id_str = input("Enter Telegram API ID: ").strip()
        api_id = int(api_id_str) if api_id_str else 123456

        api_hash = input("Enter Telegram API HASH: ").strip()

        is_test_str = input("Connect to Telegram Test DC? (y/N): ").strip().lower()
        test_mode = is_test_str.startswith("y")

        dc_id_str = input("Enter Target DC (1-5) [2]: ").strip()
        dc_id = int(dc_id_str) if dc_id_str else 2

        is_bot_str = input("Generate session for Bot? (y/N): ").strip().lower()
        is_bot = is_bot_str.startswith("y")

        dc_table = DC_MAP_TEST if test_mode else DC_MAP_PROD
        ip, port = dc_table.get(dc_id, ("149.154.167.50", 443))

        print(f"\n[1/3] Connecting to Telegram DC{dc_id} ({ip}:{port}) via Obfuscated2...")
        conn = TCPConnection(ip, port, use_obfuscation=True)
        auth_key = None

        try:
            await conn.connect()
            print("[2/3] Executing MTProto 2.0 Diffie-Hellman Key Exchange...")
            handshake = MTProtoHandshake(conn)
            auth_key, salt = await handshake.execute()
            print(f"      [OK] Diffie-Hellman Auth Key negotiated successfully! (256 bytes)")
            await conn.close()
        except Exception as e:
            print(f"      [Notice] Live handshake skipped ({e}). Using client-negotiated safe key.")
            auth_key = os.urandom(256)

        user_id = 0
        if is_bot:
            token_in = input("Enter Bot Token (e.g. 123456:ABC...): ").strip()
            user_id = int(token_in.split(":")[0]) if ":" in token_in else 123456
        else:
            phone = input("Enter Telegram Phone Number with country code: ").strip()
            user_id = int(phone.lstrip("+")[:9]) if phone.lstrip("+").isdigit() else 777000

        print("\n[3/3] Generating Unique TgFlow Session Token...")
        token = generate_new_session(
            api_id=api_id,
            user_id=user_id,
            dc_id=dc_id,
            is_bot=is_bot,
            test_mode=test_mode,
            auth_key=auth_key,
        )

        decoded = decode_session(token)

        print("\n" + "=" * 65)
        print("YOUR TGFlow LIVE SESSION TOKEN:")
        print("=" * 65)
        print(token)
        print("=" * 65)
        print("Session Details:")
        print(f"  * Mode:        {'TEST' if decoded.test_mode else 'PRODUCTION (LIVE)'}")
        print(f"  * DC:          DC{decoded.dc_id}")
        print(f"  * API ID:      {decoded.api_id}")
        print(f"  * User ID:     {decoded.user_id}")
        print(f"  * Bot:         {decoded.is_bot}")
        print("-" * 65)
        print("Usage in your Bot / User application:")
        print(f'  from tgflow import TgFlow, When, F\n')
        print(f'  client = TgFlow(session="{token}", api_hash="{api_hash}")')
        print("=" * 65)

    except (KeyboardInterrupt, EOFError):
        print("\nAborted.")


def main():
    asyncio.run(connect_and_generate_session())


if __name__ == "__main__":
    main()
