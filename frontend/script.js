const socket = new WebSocket("ws://127.0.0.1:8000/ws")

const username = prompt("Enter your username")

socket.onopen = function(){
    socket.send(username)
}

socket.onmessage = function (event) {

    document.getElementById("output").innerText = event.data

}


function sendMessage() {


    const message = document.getElementById("message").value

    socket.send(username + ": " + message)

}