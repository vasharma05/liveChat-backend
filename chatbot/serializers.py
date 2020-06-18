from rest_framework import serializers
from .models import chatbot
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

class chatbotSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = chatbot
        fields = ['chatbotName','headerBackgroundColor','headerTextColor','introductionText','introductionBackgroundColor','introductionTextColor' , 'receiverBackground','senderBackground', 'receiverTextColor','senderTextColor']