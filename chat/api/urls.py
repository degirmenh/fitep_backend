from django.urls import path

from chat.api.views import ChatListAPIView, MyChatListAPIView, MyMessageListAPIView, MessageListAPIView, \
    ChatCreateView, MessageCreateView

urlpatterns = [
    path('list', ChatListAPIView.as_view(), name='list'),
    path('my-list', MyChatListAPIView.as_view(), name='my-list'),
    path('message/list', MyMessageListAPIView.as_view(), name='my-message-list'),
    path('list/<int:chat_id>', MessageListAPIView.as_view(), name='list-message'),
    path('create', ChatCreateView.as_view(), name='create'),
    path('message-create', MessageCreateView.as_view(), name='message-create'),

]
