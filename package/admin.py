from django.contrib import admin

from package.models import PackageType, Package

# Register your models here.
admin.site.register(PackageType)
admin.site.register(Package)