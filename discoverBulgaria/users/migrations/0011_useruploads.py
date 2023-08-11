# Generated by Django 4.2.4 on 2023-08-11 13:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_nationality_delete_useressentials'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='upload_picture')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]