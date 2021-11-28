from django.contrib import admin

from address.models import UserLocation

class UserLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserLocation, UserLocationAdmin)