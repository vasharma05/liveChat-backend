from rest_framework import serializers
from .models import chatbot
from accounts.serializers import UserSerializer

class chatbotSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatbot
        fields = [ 'chatbotName','headerBackgroundColor','headerTextColor','introductionText','introductionBackgroundColor','introductionTextColor' , 'receiverBackground','senderBackground','receiverTextColor','senderTextColor','bot_picture' , 'background_picture', 'inputBarBackground','inputTextColor']