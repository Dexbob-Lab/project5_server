from django.contrib import admin
from .models import QuestionModel

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'title', 'created', 'updated']

admin.site.register(QuestionModel, QuestionAdmin)