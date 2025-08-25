from channels.generic.websocket import AsyncWebsocketConsumer
import json

class SubscribeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "Connected! You can now subscribe to topics."
        }))

    async def disconnect(self, close_code):
        print("Disconnected:", close_code)

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")
        topic_id = data.get("topic_id")

        if action == "subscribe":
            group_name = f"topic_{topic_id}"
            await self.channel_layer.group_add(group_name, self.channel_name)
            await self.send(text_data=json.dumps({
                "message": f"Subscribed to {group_name}"
            }))

        elif action == "unsubscribe":
            group_name = f"topic_{topic_id}"
            await self.channel_layer.group_discard(group_name, self.channel_name)
            await self.send(text_data=json.dumps({
                "message": f"Unsubscribed from {group_name}"
            }))

        elif action == "send_post":
            group_name = f"topic_{topic_id}"
            post = data.get("post", "No content")
            await self.channel_layer.group_send(
                group_name,
                {
                    "type": "post_message",
                    "topic_id": topic_id,
                    "post": post
                }
            )

    async def post_message(self, event):
        await self.send(text_data=event["post"])