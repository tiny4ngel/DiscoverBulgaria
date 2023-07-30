from django.contrib import admin
from django.contrib.auth import get_user_model

from discoverBulgaria.users.models import Profile

CustomUser = get_user_model()

admin.site.register(CustomUser)
admin.site.register(Profile)
