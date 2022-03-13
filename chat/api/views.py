from os import abort
from django.http import request
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from chat.api.serializers import ChatListSerializer, MessageCreateSerializer, MessageSerializer, ChatCreateSerializer
from chat.models import Chat, Message


class ChatListAPIView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer


class MyChatListAPIView(ListAPIView):
    serializer_class = ChatListSerializer
    permission_class = (IsAuthenticated,)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Chat.objects.filter(Q(messages__receiver_id=self.request.user.id) | 
            Q(messages__sender_id=self.request.user.id) | Q(creator_id=self.request.user.id)) .all()
        return []
   
class MyMessageListAPIView(ListAPIView):
    serializer_class = MessageSerializer
    permission_class = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Message.objects.filter(Q(receiver_id=self.request.user.id) | 
            Q(sender_id=self.request.user.id)) .all()
        return []


class MessageListAPIView(ListAPIView):

    serializer_class = MessageSerializer
    permission_class = (IsAuthenticated,)

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat_id=chat_id, is_deleted=False) .all()


class ChatCreateView(CreateAPIView):
    model = Chat.objects.all()
    serializer_class = ChatCreateSerializer


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class MessageCreateView(CreateAPIView):
    model = Message.objects.all()
    serializer_class = MessageCreateSerializer


    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
