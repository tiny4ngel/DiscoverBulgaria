# Generated by Django 4.2.3 on 2023-07-27 14:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='appuser',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile_picture'),
        ),
    ]
