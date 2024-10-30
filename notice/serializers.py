from rest_framework import serializers
from .models import NoticeModel

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeModel
        fields = ['id', 'nickname', 'password', 'title', 'contents', 'lockon', 'hits', 'created', 'updated']


class NoticeHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeModel
        fields = ['id', 'hits']