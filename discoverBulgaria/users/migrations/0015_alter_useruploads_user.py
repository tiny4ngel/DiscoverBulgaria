# Generated by Django 4.2.4 on 2023-08-11 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_useruploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useruploads',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]