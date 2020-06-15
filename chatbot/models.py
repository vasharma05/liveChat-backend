from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class chatbot(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chatbotName= models.CharField(max_length=256)
    headerBackgroundColor= models.CharField(max_length=256)
    headerTextColor= models.CharField(max_length=256)
    introductionText= models.CharField(max_length=256)
    introductionBackgroundColor= models.CharField(max_length=256)
    introductionTextColor = models.CharField(max_length=256)
    receiverBackground= models.CharField(max_length=256)
    senderBackground= models.CharField(max_length=256)
    receiverTextColor= models.CharField(max_length=256)
    senderTextColor= models.CharField(max_length=256)
    bot_picture = models.FileField(upload_to='bots/')
    background_picture = models.FileField(upload_to='background_images/')
    inputBarBackground= models.CharField(max_length=256)
    inputTextColor= models.CharField(max_length=256)

    def __str__(self):
        return self.chatbotName