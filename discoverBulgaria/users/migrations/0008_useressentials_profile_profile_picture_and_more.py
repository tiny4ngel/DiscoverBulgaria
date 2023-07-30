# Generated by Django 4.2.3 on 2023-07-30 11:03

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEssentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality_dropdown', models.CharField(max_length=100)),
                ('pfp', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile_picture')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_profile_pictures', to='users.useressentials'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='users.useressentials'),
        ),
    ]
