import asyncio
import dataclasses
import json
from typing import Any, Optional
from tgflow.client import TgFlow


def _json_default(obj: Any) -> Any:
    if dataclasses.is_dataclass(obj):
        d = dataclasses.asdict(obj)
        if hasattr(obj, "chat_id"):
            d["chat_id"] = obj.chat_id
        if hasattr(obj, "sender_id"):
            d["sender_id"] = obj.sender_id
        d["ok"] = True
        return d
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if isinstance(obj, (set, tuple)):
        return list(obj)
    if isinstance(obj, bytes):
        return obj.hex()
    return str(obj)


class MultiLangBridge:
    def __init__(self, client: TgFlow, host: str = "127.0.0.1", port: int = 9180):
        self.client = client
        self.host = host
        self.port = port
        self.server: Optional[asyncio.Server] = None
        self._clients: set[asyncio.StreamWriter] = set()

    async def handle_request(self, payload: dict[str, Any]) -> dict[str, Any]:
        method = payload.get("method")
        params = payload.get("params", {})
        req_id = payload.get("id")

        try:
            if method in ("ping_dc", "pingDc"):
                dc_id = params.get("dc_id", 2)
                res = await self.client.ping_dc(dc_id=dc_id)
                return {"id": req_id, "result": res}

            elif method in ("send_message", "sendMessage"):
                chat_id = params.get("chat_id")
                text = params.get("text", "")
                res = await self.client.send_message(chat_id, text)
                return {"id": req_id, "result": _json_default(res)}

            elif method in ("ban_chat_member", "banChatMember"):
                chat_id = params.get("chat_id")
                user_id = params.get("user_id")
                duration = params.get("duration", 0)
                res = await self.client.ban_chat_member(chat_id, user_id, until_date=duration)
                return {"id": req_id, "result": res}

            elif method in ("process_update", "processUpdate"):
                await self.client.process_update(params)
                return {"id": req_id, "result": {"processed": True}}

            elif method in ("send_stars", "sendStars"):
                chat_id = params.get("chat_id")
                amount = params.get("amount", 0)
                res = await self.client.send_stars(chat_id, amount=amount)
                return {"id": req_id, "result": res}

            elif method in ("get_me", "getMe"):
                me = await self.client.get_me()
                return {"id": req_id, "result": _json_default(me)}

            else:
                return {"id": req_id, "error": f"Unknown method: {method}"}
        except Exception as e:
            return {"id": req_id, "error": str(e)}

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self._clients.add(writer)
        try:
            while True:
                line = await reader.readline()
                if not line:
                    break
                try:
                    payload = json.loads(line.decode("utf-8").strip())
                    response = await self.handle_request(payload)
                    data = json.dumps(response, default=_json_default) + "\n"
                    writer.write(data.encode("utf-8"))
                    await writer.drain()
                except json.JSONDecodeError:
                    writer.write(b'{"error": "Invalid JSON"}\n')
                    await writer.drain()
        finally:
            self._clients.discard(writer)
            writer.close()

    async def start(self) -> None:
        self.server = await asyncio.start_server(self._handle_connection, self.host, self.port)

    async def stop(self) -> None:
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        for w in list(self._clients):
            try:
                w.close()
            except Exception:
                pass
        self._clients.clear()

    async def idle(self) -> None:
        if self.server:
            await self.server.serve_forever()

    async def broadcast_event(self, event_type: str, data: Any) -> None:
        msg = (json.dumps({"event": event_type, "data": data}, default=_json_default) + "\n").encode("utf-8")
        for w in list(self._clients):
            try:
                w.write(msg)
                await w.drain()
            except Exception:
                self._clients.discard(w)


BridgeServer = MultiLangBridge


class BridgeClient:
    def __init__(self, host: str = "127.0.0.1", port: int = 9180):
        self.host = host
        self.port = port
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None
        self._req_id = 0

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

    async def call(self, method: str, **params) -> Any:
        if not self.writer or not self.reader:
            raise RuntimeError("Bridge client is not connected")
        self._req_id += 1
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self._req_id,
        }
        self.writer.write((json.dumps(payload, default=_json_default) + "\n").encode("utf-8"))
        await self.writer.drain()

        line = await self.reader.readline()
        if not line:
            raise RuntimeError("Connection closed by server")
        res = json.loads(line.decode("utf-8").strip())
        if "error" in res and res["error"]:
            raise RuntimeError(res["error"])
        return res.get("result")

    async def close(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
