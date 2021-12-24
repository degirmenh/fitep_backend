from django.contrib import admin


from branch.models import *


class BranchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Branch, BranchAdmin)
admin.site.register(Category)
