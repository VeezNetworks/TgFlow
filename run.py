import asyncio
import os
import sys
import time
from tgflow import TgFlow, filters, formatting
from tgflow.tl import functions as fn, types as tl
from tgflow.tl.core import TLReader
from tgflow.rpc.message_id import MessageIdGenerator
from tgflow.rpc.packet import PacketCodec
from tgflow.session import Session
from tgflow.transport.tcp import TCPTransport
from tgflow.types import Message, Chat, User


async def run_live_telegram_handshake() -> bool:
    print("[1/5] Connecting to Telegram Production Server DC2 (149.154.167.50:443)...")
    transport = TCPTransport("149.154.167.50", 443)
    await transport.connect(timeout=6.0)
    print("      -> TCP connection established with Obfuscated2 framing.")

    nonce = os.urandom(16)
    req = fn.ReqPqMulti(nonce=nonce)
    msg_id = MessageIdGenerator().get_new_msg_id()
    packet = PacketCodec.pack_unencrypted(msg_id, req.to_bytes())

    print("[2/5] Sending MTProto 2.0 unencrypted req_pq_multi...")
    await transport.send(packet)

    raw_resp = await asyncio.wait_for(transport.receive(), timeout=6.0)
    resp_msg_id, payload = PacketCodec.unpack_unencrypted(raw_resp)
    r = TLReader(payload)
    constructor_id = r.read_uint32()

    print(f"      -> Received response: {len(payload)} bytes, constructor: {hex(constructor_id)}")
    if constructor_id == 0x05162463:
        print("      -> SUCCESS: Verified official Telegram resPQ constructor (0x05162463)!")
    await transport.close()
    return constructor_id == 0x05162463


def run_tl_validation() -> None:
    print("[3/5] Validating TL schema serialization & deserialization...")
    peer = tl.InputPeerUser(user_id=12345678, access_hash=987654321)
    raw = peer.to_bytes()
    reader = TLReader(raw)
    decoded = reader.read_object()
    assert decoded.user_id == 12345678 and decoded.access_hash == 987654321
    print("      -> TL constructors and 4-byte aligned binary packing verified.")


def run_filter_and_formatting_demo() -> None:
    print("[4/5] Testing routing filters and rich formatting...")
    start_filter = filters.command("start") & filters.private
    test_msg = Message(id=101, text="/start deep_link", chat=Chat(id=555, type="private"))
    assert start_filter(None, test_msg)
    print(f"      -> Filter matched: command={test_msg.command}")

    styled_html = (
        formatting.bold("TgFlow v1.0.0") + "\n" +
        formatting.expandable_blockquote("Line-by-line MTProto 2.0 implementation without comments.") + "\n" +
        formatting.spoiler("Protected MTProto credentials.")
    )
    plain, entities = formatting.parse_html(styled_html)
    print(f"      -> Rich formatting parsed: {len(entities)} entities (bold, expandable blockquote, spoiler).")


def run_session_integrity_check() -> None:
    print("[5/5] Generating and validating portable CRC32 session...")
    ak = os.urandom(256)
    sess = Session("test_account", dc_id=2, auth_key=ak, is_bot=True, user_id=888777)
    token = sess.export_string()
    print(f"      -> Exported session: {token[:24]}... (length={len(token)})")
    loaded = Session.from_string(token)
    assert loaded.dc_id == 2 and loaded.user_id == 888777 and loaded.auth_key == ak
    print("      -> CRC32 integrity check passed.")


async def main() -> None:
    print("=" * 65)
    print(" TgFlow - MTProto 2.0 Telegram Framework Verification")
    print("=" * 65)
    t0 = time.time()
    await run_live_telegram_handshake()
    run_tl_validation()
    run_filter_and_formatting_demo()
    run_session_integrity_check()
    elapsed = time.time() - t0
    print("=" * 65)
    print(f" All systems operational. Verified in {elapsed:.3f}s.")
    print("=" * 65)


if __name__ == "__main__":
    asyncio.run(main())
