from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class chatbot(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chatbotName= models.CharField(max_length=256, unique=True)
    headerBackgroundColor= models.CharField(max_length=256)
    headerTextColor= models.CharField(max_length=256)
    introductionText= models.CharField(max_length=256)
    introductionBackgroundColor= models.CharField(max_length=256)
    introductionTextColor = models.CharField(max_length=256)
    receiverBackground= models.CharField(max_length=256)
    senderBackground= models.CharField(max_length=256)
    receiverTextColor= models.CharField(max_length=256)
    senderTextColor= models.CharField(max_length=256)
    bot_picture = models.ImageField(upload_to='bots/')
    background_color = models.CharField(max_length=256)
    inputBarBackground= models.CharField(max_length=256)
    inputTextColor= models.CharField(max_length=256)

    def __str__(self):
        return self.chatbotName

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    consumer = models.CharField(max_length=64)

    class Meta:
        unique_together = ['user', 'consumer']

    def __str__(self):
        return "{user} {consumer}".format(user = self.user.username,consumer = self.consumer)


class Message(models.Model):
    author = models.CharField(max_length=256, unique = False)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.content

    def get_messages(self, user):
        return Messages.objects.get(user=user).order_by('-created')