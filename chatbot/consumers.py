# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import Message, Room
from .serializers import MessageSerializer, RoomSerializer

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        self.consumer = self.scope['url_route']['kwargs']['consumer']
        self.room_group_name = 'chat_%s_%s' % (self.username, self.consumer)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.user = User.objects.get(username=self.username)
        self.room = Room.objects.get(user=self.user, consumer = self.consumer)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    
    def fetch_messages(self, data):
        serialized_data = MessageSerializer(self.room.messages.all(), many=True)
        data = {
            'command': 'messages',
            'messages': serialized_data.data
        }
        self.send(text_data=json.dumps(data))



    def new_message(self, data):
        print(self.room)
        message = MessageSerializer(data = data['message'])
        if message.is_valid():
            message.save(room = self.room)
        else:
            print(message.errors)
        response = {
            'command': 'new_message',
            'message': message.data
        }
        self.send_chat_message(response)



    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message 
    }
    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
        # message = text_data_json['message']


    def send_chat_message(self, data):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': data
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        data = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(data))


class RoomConsumer(WebsocketConsumer):

    def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        self.room_group_name = 'chat_%s' % self.username

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        user = User.objects.get(username=self.username)
        rooms = user.rooms.all()
        serialized_data = RoomSerializer(rooms, many=True)
        js = json.dumps(serialized_data.data)
        self.send(text_data = js)

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))