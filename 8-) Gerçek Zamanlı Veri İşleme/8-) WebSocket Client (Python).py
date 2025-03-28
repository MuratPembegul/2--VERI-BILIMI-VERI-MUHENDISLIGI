import asyncio  
import websockets  

async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = await websocket.recv()
            print(f"Alındı: {message}")

asyncio.get_event_loop().run_until_complete(client())
