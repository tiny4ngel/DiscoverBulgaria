# Generated by Django 4.2.4 on 2023-08-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulgaria', '0013_historicfigure_quote_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualFavouriteLandmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traveller_name', models.CharField(max_length=255)),
                ('landmarks_list', models.TextField()),
            ],
            options={
                'managed': False,
            },
        ),
    ]
