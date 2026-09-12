from fastapi import FastAPI , WebSocket

app = FastAPI()
connected_user = []

@app.websocket("/ws")

async def websocket_endpoint(websocket:WebSocket):

    await websocket.accept()

    connected_user.append(websocket)

    username = await websocket.receive_text()

    for user in connected_user:
        await user.send_text(
            f"{username} joined the chat"
        )

    while True:
        message = await websocket.receive_text()

        for user in connected_user:

            await user.send_text(
                f"server received : {message}"
            )

        online_users = len(connected_user)

        for user in connected_user:
            await user.send_text(
                f"online users: {online_users}"
            )

