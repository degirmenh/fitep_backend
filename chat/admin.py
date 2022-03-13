from django.contrib import admin


from chat.models import *


class ChatAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
