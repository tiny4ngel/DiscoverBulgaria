# Generated by Django 4.2.3 on 2023-07-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_useressentials_pfp_alter_profile_nationality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(choices=[('BG', 'Bulgarian'), ('EN', 'English'), ('TR', 'Turkish'), ('FR', 'French'), ('ES', 'Spanish'), ('RU', 'Russian'), ('OT', 'Other')], max_length=2),
        ),
        migrations.DeleteModel(
            name='UserEssentials',
        ),
    ]
