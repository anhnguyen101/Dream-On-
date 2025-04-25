import asyncio
import websockets

def get_username():
    return input("Enter your name: ")

async def send_message(websocket, username):
    loop = asyncio.get_event_loop()
    while True:
        msg = await loop.run_in_executor(None, input)  # run blocking input() in a thread
        await websocket.send(f"{username}: {msg}")

async def receive_message(websocket, username):
    while True:
        message = await websocket.recv()
        if not message.startswith(f"{username}:"):
            print(f"\n{message}")

async def chat_client(username):
    uri = "ws://localhost:8000/ws/chat"
    async with websockets.connect(uri) as websocket:
        await asyncio.gather(
            send_message(websocket, username),
            receive_message(websocket),
        )

def main():
    username = get_username()
    asyncio.run(chat_client(username))

if __name__ == "__main__":
    main()