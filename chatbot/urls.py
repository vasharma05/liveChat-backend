from django.urls import path
from .views import chatbotView
urlpatterns = [
    path('api/', chatbotView.as_view(), name='chatbot_api')
]