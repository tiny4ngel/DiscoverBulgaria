# Generated by Django 4.2.3 on 2023-08-01 18:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bulgaria', '0003_alter_favouritelandmarks_landmark'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favouritelandmarks',
            unique_together={('traveller', 'landmark')},
        ),
    ]
