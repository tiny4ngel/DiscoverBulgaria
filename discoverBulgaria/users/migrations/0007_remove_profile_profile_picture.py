# Generated by Django 4.2.3 on 2023-07-27 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_appuser_profile_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]
