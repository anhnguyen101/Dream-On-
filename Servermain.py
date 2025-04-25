from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import uvicorn

app = FastAPI()

class Server:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

server = Server()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await server.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await server.broadcast(data)
    except WebSocketDisconnect:
        server.disconnect(websocket)
        await server.broadcast("A user disconnected.")

def main():
    uvicorn.run("Servermain:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()