import asyncio
import websockets
import json
import random

from websockets.legacy.client import WebSocketClientProtocol

ws_url = "wss://gateway.discord.gg/?v=9&encoding=json"

from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")

identity = {
    "op": 2,
    "d": {
        "token": token,
        "intents": 1<<25,
        "properties": {
            "$os": "linux",
            "$browser": "chromium",
            "$device": "pcidklol",
        }
    }
}

class Gateway:
    def __init__(self) -> None:
        self._identification = identity
        self._d = None
    
    async def _handle_message(self, websocket, msg):
        message = json.loads(msg)
        op_code = message["op"]
        print(op_code)
        match op_code:
            case 10:
                heartbeat = message["d"]["heartbeat_interval"]
                asyncio.create_task(self._heartbeat_send(heartbeat, websocket, True))
            case 11:
                asyncio.create_task(self._heartbeat_send(self._interval, websocket))
    
    async def _init_connection(self):
        async with websockets.connect(ws_url) as ws:
            while True:
                response = await ws.recv()
                await self._handle_message(ws, response)
                print(response)
                print(type(ws))
    
    async def _heartbeat_send(self, interval: int, websocket: WebSocketClientProtocol, initial_connection = False):
        self._interval = interval
        if initial_connection:
            jitter = random.random()
            await asyncio.sleep(interval*jitter/1000)
        else:
            await asyncio.sleep(interval/1000)
        print("chicanery")
        payload = {
            "op": 1,
            "d": self._d
        }
        json_payload = json.dumps(payload)
        await websocket.send(json_payload)
        
        
         

    def connect(self):
        asyncio.get_event_loop().run_until_complete(self._init_connection())

if __name__ == "__main__":
    a = Gateway()
    a.connect()
    
