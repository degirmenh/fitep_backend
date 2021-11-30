from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from account.models import *


admin.site.register(Account)
admin.site.register(Coach)
admin.site.register(Member)