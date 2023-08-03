from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Landmarks(models.Model):
    title = models.CharField(max_length=100, )
    location = models.CharField(max_length=100, )
    landmark_photo = CloudinaryField('landmark_photo', null=True, blank=True)
    trip_time = models.CharField(max_length=100, )
    historic_context = models.CharField(max_length=1000)
    architectural_features = models.CharField(max_length=1000)
    visitor_information = models.CharField(max_length=1000)
    accessibility = models.CharField(max_length=1000)
    cover_photo = CloudinaryField('cover_photo', null=True, blank=True)
    additional_photo = CloudinaryField('additional_photo', null=True, blank=True)



class FavouriteLandmarks(models.Model):
    traveller = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    landmark = models.ForeignKey(Landmarks, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        unique_together = ['traveller', 'landmark']
