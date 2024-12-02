from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='chatrooms')

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)










from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))


import io from 'socket.io-client';
const socket = io('ws://localhost:8000/ws/chat/room_name/');

socket.on('message', function(data) {
    console.log(data.message);
});



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message

@api_view(['GET'])
def get_message_history(request, room_id):
    messages = Message.objects.filter(chatroom_id=room_id)
    data = [{'sender': msg.sender.username, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages]
    return Response(data)