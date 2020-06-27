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
            serialized_chat = chatbotSerializer(chat, context={'request': request})
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
            serializer = chatbotSerializer(chat, data=request.data)
            if(serializer.is_valid()):
                serializer.save(user = request.user)
            else:
                print(serializer.errors)
                return Response(serializer.errors)
        except: 
            serializer = chatbotSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save(user = request.user)
            else:
                # print(serializer.errors)
                return Response(serializer.errors)
        return Response({'detail': 'success'}, status = 200)
        # chatbot.save()

def index(request):
    return render(request, 'chatbot/index.html', {})

def room(request,username, room_name):
    return render(request, 'chatbot/room.html', {
        'room_name': room_name,
        'username': username
    })