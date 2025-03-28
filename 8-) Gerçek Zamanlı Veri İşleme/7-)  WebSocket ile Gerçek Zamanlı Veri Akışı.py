import asyncio  
import websockets  

async def server(websocket, path):
    while True:
        await websocket.send("Gerçek zamanlı mesaj!")
        await asyncio.sleep(1)

start_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
