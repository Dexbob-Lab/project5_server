from rest_framework import serializers
from .models import QuestionModel

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ['id', 'nickname', 'password', 'title', 'contents', 'lockon', 'hits', 'created', 'updated']


class QuestionHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ['id', 'hits']