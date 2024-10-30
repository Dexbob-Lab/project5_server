from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class NoticeModel(models.Model):
    nickname = models.CharField(max_length=30, unique=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=255)
    contents = models.TextField()
    lockon = models.BooleanField(default=False)
    hits = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    