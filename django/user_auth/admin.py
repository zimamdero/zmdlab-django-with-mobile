from django.contrib import admin
from user_auth.models import UserProfile, UEmailAuth


admin.site.register(UserProfile)
admin.site.register(UEmailAuth)
