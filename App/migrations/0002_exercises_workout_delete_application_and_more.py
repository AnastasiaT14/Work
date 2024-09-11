# Generated by Django 5.1 on 2024-09-11 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=100)),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_of_body', models.CharField(max_length=100)),
                ('quantity_of_workouts', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.AddField(
            model_name='exercises',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='App.workout'),
        ),
    ]
