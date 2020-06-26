from rest_framework import serializers
from .models import chatbot, Message, Room
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

class chatbotSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    bot_picture = serializers.ImageField(required=False)    
    class Meta:
        model = chatbot
        # fields = '__all__'
        exclude = ['user']

class MessageSerializer(serializers.ModelSerializer):
    room = serializers.StringRelatedField()
    class Meta:
        model = Message
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    messages = MessageSerializer(many=True)
    class Meta:
        model = Room
        fields = ['user', 'consumer', 'messages']

