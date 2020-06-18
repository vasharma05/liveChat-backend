from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework.response import Response
from .models import chatbot
from .serializers import chatbotSerializer

# Create your views here.
class chatbotView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        try:
            chat = chatbot.objects.get(user = request.user)
            serialized_chat = chatbotSerializer(chat)
            message = {}
            message['detail'] = 'success'
            message['chatbot_details'] = serialized_chat.data
            return Response(message)
        except:
            message = {}
            message['detail'] = 'No chatbot details found'
            return Response(message)
    
    def post(self, request, format=None):
        try: 
            chat = chatbot.objects.get(user = request.user)
            data = dict(**request.data, **request.FILES)
            serializer = chatbotSerializer(chat, data=request.data)
            if(serializer.is_valid()):
                serializer.save(user = request.user)
            else:
                print('hello')
                print(serializer.errors)
                return Response(serializer.errors)
        except: 
            serializer = chatbotSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save(user = request.user)
            else:
                print(serializer.errors)
                return Response(serializer.errors)
        return Response({'detail': 'success'}, status = 200)
        # chatbot.save()