# Generated by Django 4.2.4 on 2023-08-09 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulgaria', '0011_remove_choice_choice_text2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicfigure',
            name='unlock_quiz_url',
        ),
    ]
