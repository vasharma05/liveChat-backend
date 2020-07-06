from django.urls import path
from .views import chatbotView, index, room, MessageFileView, ConsumerEmailView, getChatBotDetails
urlpatterns = [
    path('api/', chatbotView.as_view(), name='chatbot_api'),
    path('', index, name='index'),
    path('chat/<str:username>/<str:room_name>/', room, name='room'),
    path('message/file/upload/', MessageFileView.as_view(), name='message_file_upload'),
    path('consumeremail/', ConsumerEmailView.as_view(), name="consumer_email"),
    path('details/', getChatBotDetails, name='chatbot_details')
]