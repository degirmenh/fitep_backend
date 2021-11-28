from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from account.models import *

# Register your models here.


class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('username', 'email')


class CoachAdmin(admin.ModelAdmin):
    model = Coach



class MemberAdmin(admin.ModelAdmin):
    model = Member



admin.site.register(Account, AccountAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Member, MemberAdmin)