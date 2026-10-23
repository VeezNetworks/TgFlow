<p align="center">
  <img src="assets/logo.png" alt="TgFlow Logo" width="220"/>
</p>

<h1 align="center">TgFlow</h1>

<p align="center">
  <b>Modern Asynchronous MTProto 2.0 Telegram Framework for Python & Polyglot Backends</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square" alt="Python Version"/>
  <img src="https://img.shields.io/badge/MTProto-2.0-blueviolet?style=flat-square" alt="MTProto 2.0"/>
  <img src="https://img.shields.io/badge/Telegram%20Schema-Layer%20225%2B-brightgreen?style=flat-square" alt="Schema Layer"/>
  <img src="https://img.shields.io/badge/License-MIT-orange?style=flat-square" alt="License"/>
</p>

---

## Highlights

* **Pure Native MTProto 2.0**: In-house cryptographic core supporting AES-256 IGE, Pollard's rho PQ factorization, 2048-bit Diffie-Hellman key exchange, and Obfuscated2 anti-DPI transport.
* **Telegram Layer 225+ Schemas**: Direct first-class support for modern Telegram features including Telegram Stars, Star Subscriptions, Paid Reactions, Star Revenue, Upgraded & Collectible Gifts, Telegram Business 2.0, Stories 2.0, and Forum Topics.
* **Declarative Template Routing**: Expressive route patterns with typed parameters (`@client.on("/ban <target> <duration:int=60> <reason*>")`).
* **Interactive Multi-Turn Dialogues**: Built-in conversational flows without complex state machines (`await ctx.ask()`, `await ctx.choose()`).
* **Multi-Language IPC Bridge**: Built-in JSON-RPC 2.0 bridge allowing bots in Go, Node.js, Rust, or C# to leverage TgFlow's MTProto session.
* **Human-Readable Codebase**: Clean asynchronous architecture without AI comment boilerplate or bloated abstractions.

---

## Quick Example

```python
import asyncio
from tgflow import TgFlow, filters, raw

client = TgFlow(api_id=123456, api_hash="0123456789abcdef0123456789abcdef")

# Simple command with typed parameter and default
@client.on("/ban <target> <duration:int=60> <reason*>")
async def ban_handler(ctx, target, duration: int, reason: str = "Rule violation"):
    await ctx.reply(f"Banning {target} for {duration}m. Reason: {reason}")

# Composable filter routing
@client.on(filters.command("stats") & filters.group)
async def group_stats(ctx):
    await ctx.reply(f"Group statistics for chat ID: {ctx.chat_id}")

# Raw MTProto invocation
@client.on("/raw_topic")
async def create_topic_raw(ctx):
    req = raw.functions.CreateForumTopic(
        channel=raw.types.InputPeerChannel(channel_id=ctx.chat_id, access_hash=0),
        title="Engineering Discussions",
        icon_color=0x6FB9F0,
    )
    result = await client.invoke(req)
    await ctx.reply("Forum topic created via raw MTProto RPC!")

# Interactive dialogue flow
@client.on("/feedback")
async def feedback_handler(ctx):
    response = await ctx.ask("What feature would you like to see next?")
    rating = await ctx.choose("Rate your experience:", options=["Great", "Okay", "Poor"])
    await ctx.reply(f"Thanks! Received: {response.text} (Rating: {rating})")

async def main():
    await client.start()
    await client.idle()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Verifying DC Handshake

TgFlow comes with an automated handshake tester to verify connection to Telegram's Data Centers:

```bash
python tests/test_dc_connect.py
```

Output:
```text
============================================================
TgFlow MTProto 2.0 - Live DC Connection & Handshake Test
============================================================
[1/3] Connecting to DC2 (149.154.167.40:443)...
[2/3] Sending req_pq_multi packet (nonce: 69c0d11f...)...
[3/3] Received res_pq from Telegram DC2!
      Nonce match: True
      Fingerprints: [0x8b857700a9faec1c]
[SUCCESS] Telegram DC2 handshake verified successfully!
```

---

## Polyglot IPC Bridge (Go, Node.js, Rust, C#)

Start the bridge server in Python:

```python
from tgflow import TgFlow
from tgflow.bridge import BridgeServer

client = TgFlow(api_id=123456, api_hash="abcdef...")
bridge = BridgeServer(client, host="127.0.0.1", port=9000)
await bridge.start()
```

Connect and call any MTProto method from **Go**:

```go
package main

import (
    "bufio"
    "encoding/json"
    "fmt"
    "net"
)

func main() {
    conn, _ := net.Dial("tcp", "127.0.0.1:9000")
    defer conn.Close()

    req, _ := json.Marshal(map[string]interface{}{
        "jsonrpc": "2.0",
        "method":  "sendMessage",
        "params":  map[string]interface{}{"chat_id": 12345, "text": "Hello from Go!"},
        "id":      1,
    })
    conn.Write(append(req, '\n'))

    resp, _ := bufio.NewReader(conn).ReadString('\n')
    fmt.Println(resp)
}
```

---

## Architecture Overview

```
              User Code (Python / Go / Node.js / Rust / C#)
                                    │
                         ┌──────────┴──────────┐
                         │   TgFlow Client     │
                         │ (Router & Context)  │
                         └──────────┬──────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
        ┌────────▼────────┐ ┌───────▼────────┐ ┌───────▼────────┐
        │  TL Generator   │ │ Cryptography   │ │ JSON-RPC IPC   │
        │  & Type Models  │ │ AES-IGE / DH   │ │ Bridge Server  │
        │ (TDLib Scheme)  │ │ Pollard's rho  │ │ (Polyglot)     │
        └─────────────────┘ └───────┬────────┘ └────────────────┘
                                    │
                         ┌──────────▼──────────┐
                         │  Obfuscated2 TCP    │
                         │ (Padded 0xdddddddd) │
                         └──────────┬──────────┘
                                    │
                               Telegram DC
```

---

## Documentation

Full documentation is available in `docs/`:

```bash
sphinx-build -b html docs docs/_build/html
```

Or open `docs/_build/html/index.html` in your browser.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
