from cloudinary.models import CloudinaryField
from django.db import models


class Landmarks(models.Model):
    title = models.CharField(max_length=100, )
    location = models.CharField(max_length=100, )
    landmark_photo = CloudinaryField('landmark_photo', null=True, blank=True)
    trip_time = models.CharField(max_length=100, )
