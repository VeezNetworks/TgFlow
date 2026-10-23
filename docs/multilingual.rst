Multi-Language IPC Bridge
==========================

TgFlow includes a built-in JSON-RPC 2.0 Inter-Process Communication (IPC) bridge. This allows you to write your bot or automation logic in **Go**, **Node.js / TypeScript**, **Rust**, or **C#**, while letting TgFlow handle MTProto 2.0 network transports, sessions, and cryptography.

Starting the Bridge
-------------------

You can start the bridge directly from Python or via the CLI:

.. code-block:: python

   import asyncio
   from tgflow import TgFlow
   from tgflow.bridge import BridgeServer

   async def main():
       client = TgFlow(api_id=123456, api_hash="abcdef...")
       bridge = BridgeServer(client, host="127.0.0.1", port=9000)
       await bridge.start()
       print("TgFlow Multi-Language Bridge listening on port 9000...")
       await bridge.idle()

   if __name__ == "__main__":
       asyncio.run(main())

Calling from Go
---------------

.. code-block:: go

   package main

   import (
       "bufio"
       "encoding/json"
       "fmt"
       "net"
   )

   type RPCRequest struct {
       JSONRPC string      `json:"jsonrpc"`
       Method  string      `json:"method"`
       Params  interface{} `json:"params"`
       ID      int         `json:"id"`
   }

   func main() {
       conn, err := net.Dial("tcp", "127.0.0.1:9000")
       if err != nil {
           panic(err)
       }
       defer conn.Close()

       req := RPCRequest{
           JSONRPC: "2.0",
           Method:  "sendMessage",
           Params: map[string]interface{}{
               "chat_id": 12345678,
               "text":    "Hello from Golang via TgFlow!",
           },
           ID: 1,
       }

       data, _ := json.Marshal(req)
       conn.Write(append(data, '\n'))

       reader := bufio.NewReader(conn)
       line, _ := reader.ReadString('\n')
       fmt.Println("TgFlow Response:", line)
   }

Calling from Node.js / TypeScript
---------------------------------

.. code-block:: typescript

   import * as net from "net";

   const client = net.createConnection({ port: 9000, host: "127.0.0.1" }, () => {
     const request = {
       jsonrpc: "2.0",
       method: "sendMessage",
       params: { chat_id: 12345678, text: "Hello from TypeScript!" },
       id: 1,
     };
     client.write(JSON.stringify(request) + "\n");
   });

   client.on("data", (data) => {
     console.log("Response:", data.toString());
     client.end();
   });

Supported Bridge Methods
------------------------

* ``sendMessage``: Send text or markdown messages.
* ``editMessage``: Edit existing message text or media caption.
* ``deleteMessages``: Delete messages in a chat.
* ``banChatMember``: Restrict or ban members from groups and channels.
* ``sendStars``: Send Telegram Stars to users or buy star media.
* ``getMe``: Retrieve profile information for the authenticated user/bot.
