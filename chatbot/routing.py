from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/chat/<str:username>/<str:consumer>', consumers.ChatConsumer),
    path(r'ws/room/<str:username>', consumers.RoomConsumer)
]