from email import message
from django.forms import ValidationError
from rest_framework import serializers
from account.api.serializers import AccountSerializer

from chat.models import Chat, Message

class MessageSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format="%Y-%m-%d%H:%M:%S", required=False, read_only=True)
    creation_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    text = serializers.CharField(allow_blank=True, required=False)
    sender = AccountSerializer(many=False)
    receiver = AccountSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'

class ChatListSerializer(serializers.ModelSerializer):
    
    messages = MessageSerializer(many=True)
    
    class Meta:
        model = Chat
        fields = '__all__'




class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['topic']


    def create(self, validated_data):
        print(validated_data)
        chat = Chat.objects.create(
            creator=validated_data['creator'],
            topic=validated_data['topic'],
            is_deleted=False,     
        )
        chat.save()
        return chat



class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['receiver', "text", 'chat']
        extra_kwargs = {
            "chat": {"required": False}
        }

    def validate(self, attr):
        if attr.get('chat') and attr.get('chat').messages.first():  
            receiver, sender = attr.get('chat').messages.first().receiver, attr.get('chat').messages.first().sender
            if attr.get('sender') not in [receiver, sender]:
                raise ValidationError("Invalid Chat")
            if attr.get("receiver") not in [receiver, sender]:
                raise ValidationError("Invalid Receiver")
        return attr 

    def create(self, validated_data):
        chat = validated_data.get('chat')
        if not chat:
            chat = Chat(topic=validated_data['text'][:255], 
                        creator= validated_data['sender'])
            
            chat.save()
        print(validated_data)
        message = Message.objects.create(
            sender=validated_data['sender'],
            receiver=validated_data['receiver'],
            text=validated_data['text'],
            is_deleted=False,    
            chat=chat 
        )
        message.save()
        return message
