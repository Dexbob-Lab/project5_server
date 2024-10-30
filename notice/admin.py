from django.contrib import admin
from .models import NoticeModel

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'title', 'created', 'updated']

admin.site.register(NoticeModel, NoticeAdmin)
