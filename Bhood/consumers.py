import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.template.loader import render_to_string
from .models import Messenger
from asgiref.sync import sync_to_async

class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.chatroom_name = self.scope['url_route']['kwargs']['cname']
        await self.channel_layer.group_add(
            self.chatroom_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.message = text_data_json['message']
        fmessage = await sync_to_async(Messenger.objects.create)(author=self.user, message=self.message)
        event = {
            'type': 'message_handler',
            'message_id': fmessage.id
        }
        await self.channel_layer.group_send(
            self.chatroom_name,
            event
        )

    async def message_handler(self, event):
        message_id = event['message_id']
        message = await sync_to_async(Messenger.objects.get)(id=message_id)
        context = {
            'message': message,
            'user': self.user,
        }
        html = await sync_to_async(render_to_string)('message.html', context=context)
        await self.send(text_data=json.dumps({
            'message': html
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chatroom_name,
            self.channel_name
        )