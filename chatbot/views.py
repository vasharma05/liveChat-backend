from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import chatbot, Message, Room
from .serializers import chatbotSerializer, MessageSerializer
from django.contrib.auth.models import User

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
                return Response({'detail':serializer.errors}, status=200)
        return Response({'detail': 'success'}, status = 200)
        # chatbot.save()

def index(request):
    return render(request, 'chatbot/index.html', {})

def room(request,username, room_name):
    return render(request, 'chatbot/room.html', {
        'room_name': room_name,
        'username': username
    })

class MessageFileView(APIView):
    def post(self, request, format=None):
        serialized_message = MessageSerializer(data = request.data)
        if serialized_message.is_valid():
            user = User.objects.get(username = request.data['room'].split()[0])
            room = Room.objects.get(user = user, consumer = request.data['room'].split()[1])
            serialized_message.save(room = room)
        else:
            return Response(serialized_message.errors, status=400)
        id = serialized_message.data['id']
        data = MessageSerializer(Message.objects.get(id=id))
        return Response(data.data, status = 200)

class ConsumerEmailView(APIView):
    def post(self, request, format=None):
        try:
            user = User.objects.get(username=request.data['user'])
            ind = request.data['email'].find('@')
            consumer = request.data['email'][:ind]
            try:
                r = Room.objects.get(user=user, consumer=consumer)
            except:
                r = Room.objects.create(user=user, consumer=consumer, consumer_email=request.data['email'])
            data = {
                'message':'success',
                'consumer': consumer
            }
            return Response(data, status= 200)
        except:
            return Response({'message':'Something went wrong'}, status = 203)

@api_view(['POST'])
def getChatBotDetails(request,format=None):
    print(request.data)
    try:
        username = request.data['username']
        user = User.objects.get(username=username)
    except:
        return Response({'detail':'Incorrect Username'}, status=200)
    try:
        serialized_data = chatbotSerializer(chatbot.objects.get(user=user), context={'request':request})
        message = dict()
        message['detail']='success'
        message['chatbot'] = serialized_data.data
        return Response(message,  status=200)
    except:
        return Response({'detail':'No chatbot details found'}, status=200)
    