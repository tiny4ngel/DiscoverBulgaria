# Generated by Django 4.1.1 on 2023-08-04 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulgaria', '0006_historicfigure_leaderboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('choice1', models.CharField(max_length=100)),
                ('choice2', models.CharField(max_length=100)),
                ('correct_choice', models.CharField(max_length=100)),
                ('historic_figure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='bulgaria.historicfigure')),
            ],
        ),
    ]
