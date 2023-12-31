# Generated by Django 4.1.1 on 2023-08-03 20:03

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulgaria', '0004_alter_favouritelandmarks_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmarks',
            name='accessibility',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landmarks',
            name='additional_photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='additional_photo'),
        ),
        migrations.AddField(
            model_name='landmarks',
            name='architectural_features',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landmarks',
            name='cover_photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='cover_photo'),
        ),
        migrations.AddField(
            model_name='landmarks',
            name='historic_context',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landmarks',
            name='visitor_information',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
    ]
