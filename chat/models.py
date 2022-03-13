from django.db.models.deletion import CASCADE
from django.db import models

import account


# Create your models here.
class Chat(models.Model):
    topic = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(account.models.Account, on_delete=CASCADE, related_name='creator')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        db_table = 'chat'
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'


class Message(models.Model):
    sender = models.ForeignKey(account.models.Account, on_delete=CASCADE, related_name='sender')
    receiver = models.ForeignKey(account.models.Account, on_delete=CASCADE, related_name='receiver')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    creation_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    update_time = models.DateTimeField(blank=True, null=True)
    text = models.TextField() 


    def __str__(self):
        return f'{self.chat.topic}  {self.sender.full_name()}  {self.receiver.full_name()}'

    class Meta:
        db_table = 'message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'



