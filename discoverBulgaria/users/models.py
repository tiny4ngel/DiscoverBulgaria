from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from discoverBulgaria.users.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    NATIONALITY_CHOICES = [
        ('BG', 'Bulgarian'),
        ('EN', 'English'),
        ('TR', 'Turkish'),
        ('FR', 'French'),
        ('ES', 'Spanish'),
        ('RU', 'Russian'),
        ('OT', 'Other'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)
    profile_picture = CloudinaryField('profile_picture', null=True, blank=True)


