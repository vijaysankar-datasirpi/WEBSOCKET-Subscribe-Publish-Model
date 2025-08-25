let socket = new WebSocket("ws://127.0.0.1:8000/ws/subscribe/");

socket.send(JSON.stringify({"action": "subscribe", "topic_id": 1}));
socket.send(JSON.stringify({"action": "unsubscribe", "topic_id": 1}));

socket.send(JSON.stringify({
    "action": "send_post",
    "topic_id": 47,
    "post": "ABCD"
}));

socket.onmessage = (e) => {
    console.log(e.data);
};
