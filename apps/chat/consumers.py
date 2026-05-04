import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from apps.chat.models import ChatRoom, Message
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'

        print("CONNECTING TO ROOM:", self.room_group_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        print("WEBSOCKET CONNECTED")


    async def disconnect(self, close_code):
        print("WEBSOCKET DISCONNECTED")

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        print("RAW MESSAGE:", text_data)

        data = json.loads(text_data)

        message = data['message']
        username = data['username']

        print("MESSAGE RECEIVED:", message)
        print("FROM USER:", username)

        # Save message
        await self.save_message(username, message)

        print("MESSAGE SAVED TO DATABASE")

        # Send to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

        print("MESSAGE SENT TO GROUP")


    async def chat_message(self, event):
        print("SENDING MESSAGE TO FRONTEND")

        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
        }))


    @sync_to_async
    def save_message(self, username, message):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(id=self.room_id)

        Message.objects.create(
            room=room,
            sender=user,
            message=message
        )