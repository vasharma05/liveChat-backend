from django.urls import path
from .views import chatbotView, index, room
urlpatterns = [
    path('api/', chatbotView.as_view(), name='chatbot_api'),
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]