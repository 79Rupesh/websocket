import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

connected_users = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    connected_users.append(websocket)

    print("user connected")
    print("Total users:", len(connected_users))

    # Receive username

    username = await websocket.receive_text()

    print("username : ", username)

    # Check username

    if username.strip() == "":
        await websocket.close()
        return

    # join notification

    join_data = {
        "type":"join",
        "username":username
    }

    for user in connected_users:
        await user.send_text(
            json.dumps(join_data)
        )


    # online users

    online_data = {
        "type": "online",
        "count": len(connected_users)
    }

    for user in connected_users:
        await user.send_text(
        json.dumps(online_data)
        )

    try:
        while True:

            # Receive message

            message = await websocket.receive_text()

            print("message receive : ", message)

            # create message data

            message_data = {
                "type": "message",
                "username": username,
                "message": message
            }

            print("Broadcasting:", message_data)

            # Broadcast message


            for user in connected_users:
                await user.send_text(
                    json.dumps(message_data)
                )

    except WebSocketDisconnect:

        print("User disconnected:", username)
        if websocket in connected_users:
            connected_users.remove(websocket)


        # Leave notification

        leave_data = {
            "type":"leave",
            "username": username
        }

        for user in connected_users:

            await user.send_text(
                json.dumps(leave_data)
            )

            # update online count

            online_data =  {
                "type":"online",
                "count": len(connected_users)

            }

            for user in connected_users:
                await user.send_text(
                    json.dumps(online_data)
                )