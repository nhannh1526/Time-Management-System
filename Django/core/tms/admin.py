from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Request)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'owner', 'request_type')
    prepopulated_fields = {'slug': ('owner',), }


admin.site.register(models.RequestType)
admin.site.register(models.Reason)
