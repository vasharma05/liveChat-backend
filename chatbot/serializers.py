from rest_framework import serializers
from .models import chatbot
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

class chatbotSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    bot_picture = serializers.ImageField(required=False)    
    class Meta:
        model = chatbot
        # fields = '__all__'
        exclude = ['user']