from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from discoverBulgaria.users.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    """
       Custom user model for the application.

       Attributes:
           email (EmailField): The email address of the user (unique).
           is_staff (BooleanField): Indicates if the user is a staff member.
           date_joined (DateTimeField): The date and time when the user joined.
    """
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

    def get_full_name(self):
        """
            Get the full name of the user by combining first name and last name from the profile.
            Returns:
                str: The full name of the user.
        """
        try:
            profile = self.profile
            return f"{profile.first_name} {profile.last_name}"
        except Profile.DoesNotExist:
            return ""

    def get_favorite_landmarks(self):
        """
            Get a string representation of the user's favorite landmarks.
            Returns:
                str: A comma-separated list of favorite landmark titles.
        """
        return ', '.join([fav.landmark.title for fav in self.favouritelandmarks_set.all()])


class Profile(models.Model):
    """
        Model representing user profile information.

        Attributes:
            first_name (CharField): The first name of the user.
            last_name (CharField): The last name of the user.
            nationality (CharField): The nationality of the user.
            user (OneToOneField): The user associated with the profile.
            profile_picture (CloudinaryField): The profile picture of the user.
    """
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
