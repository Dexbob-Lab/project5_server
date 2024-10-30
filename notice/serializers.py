from rest_framework import serializers
from .models import NoticeModel

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeModel
        fields = ['id', 'nickname', 'password', 'title', 'contents', 'is_lock', 'view_count', 'created', 'updated']