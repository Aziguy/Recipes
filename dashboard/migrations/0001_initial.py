# Generated by Django 3.1.4 on 2021-01-16 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('recipe_id', models.IntegerField()),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_photo', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(blank=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]