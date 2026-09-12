from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

connected_users = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    connected_users.append(websocket)

    username = await websocket.receive_text()

    for user in connected_users:
        await user.send_text(
            f"{username} joined the chat"
        )

    for user in connected_users:
        await user.send_text(
            f"Online users: {len(connected_users)}"
        )

    try:
        while True:

            message = await websocket.receive_text()

            for user in connected_users:
                await user.send_text(
                    f"{username}: {message}"
                )

    except WebSocketDisconnect:

        connected_users.remove(websocket)

        for user in connected_users:
            await user.send_text(
                f"{username} left the chat"
            )

        for user in connected_users:
            await user.send_text(
                f"Online users: {len(connected_users)}"
            )