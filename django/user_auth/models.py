from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='imgs')
    greetings = models.TextField(max_length=500, blank=True)
    level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UEmailAuth(models.Model):
    email = models.CharField(max_length=254, primary_key=True)
    auth_num = models.CharField(max_length=6)
    auth_num_check = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
