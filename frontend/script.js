let socket;
let currentUsername = "";


/* =========================
   Connect to WebSocket
   ========================= */

function connect() {

    currentUsername = document
        .getElementById("username")
        .value
        .trim();


    /* Check username */

    if (currentUsername === "") {

        alert("Please enter username");

        return;
    }


    /* Create WebSocket connection */

    socket = new WebSocket("ws://127.0.0.1:8000/ws");


    /* =========================
       Connection Open
       ========================= */

    socket.onopen = function () {

        /* Send username to server */

        socket.send(currentUsername);

        console.log("Connected to server");


        /* Connection status */

        const status = document.getElementById("status");

        status.innerText = "🟢 Connected";

        status.className = "status connected";


        /* Disable Connect button */

        document.getElementById("connectButton").disabled = true;


        /* Disable Username input */

        document.getElementById("username").disabled = true;


        /* Enable Message input */

        document.getElementById("message").disabled = false;


        /* Enable Send button */

        document.getElementById("sendButton").disabled = false;

    };


    /* =========================
       Receive Message
       ========================= */

    socket.onmessage = function (event) {

        /* Convert JSON string to JavaScript object */

        const data = JSON.parse(event.data);

        const output = document.getElementById("output");


        /* =========================
           User Joined
           ========================= */

        if (data.type === "join") {

            output.innerHTML += `
                <div class="notification join">
                    🟢 <b>${data.username}</b> joined the chat
                </div>
            `;

        }


        /* =========================
           User Left
           ========================= */

        else if (data.type === "leave") {

            output.innerHTML += `
                <div class="notification leave">
                    🔴 <b>${data.username}</b> left the chat
                </div>
            `;

        }


        /* =========================
           Online Users
           ========================= */

        else if (data.type === "online") {

            document.getElementById("onlineUsers").innerText =
                data.count;

        }


        /* =========================
           Chat Message
           ========================= */

        else if (data.type === "message") {


            /* My message */

            if (data.username === currentUsername) {

                output.innerHTML += `
                    <div class="message my-message">

                        <div class="username">
                            You
                        </div>

                        <div class="text">
                            ${data.message}
                        </div>

                    </div>
                `;

            }


            /* Other user's message */

            else {

                output.innerHTML += `
                    <div class="message other-message">

                        <div class="username">
                            ${data.username}
                        </div>

                        <div class="text">
                            ${data.message}
                        </div>

                    </div>
                `;

            }

        }


        /* Scroll chat to bottom */

        output.scrollTop = output.scrollHeight;

    };


    /* =========================
       Connection Closed
       ========================= */

    socket.onclose = function () {

        console.log("Disconnected from server");


        /* Connection status */

        const status = document.getElementById("status");

        status.innerText = "🔴 Disconnected";

        status.className = "status disconnected";


        /* Enable Connect button */

        document.getElementById("connectButton").disabled = false;


        /* Enable Username input */

        document.getElementById("username").disabled = false;


        /* Disable Message input */

        document.getElementById("message").disabled = true;


        /* Disable Send button */

        document.getElementById("sendButton").disabled = true;

    };

}


/* =========================
   Send Message
   ========================= */

function sendMessage() {

    const messageInput = document.getElementById("message");

    const message = messageInput.value.trim();


    /* Don't send empty message */

    if (message === "") {

        return;

    }


    /* Check WebSocket connection */

    if (socket && socket.readyState === WebSocket.OPEN) {

        /* Send message to server */

        socket.send(message);


        /* Clear input */

        messageInput.value = "";

    }

}


/* =========================
   Send Message Using Enter
   ========================= */

document
    .getElementById("message")
    .addEventListener("keydown", function (event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    });