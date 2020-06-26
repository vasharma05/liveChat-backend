from django.contrib import admin
from .models import chatbot, Room, Message

# Register your models here.
admin.site.register(chatbot)
admin.site.register(Room)
admin.site.register(Message)