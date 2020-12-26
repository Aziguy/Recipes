# Generated by Django 3.1.4 on 2020-12-17 14:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201217_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre1', models.CharField(max_length=20)),
                ('titre2', models.CharField(max_length=20)),
                ('description', ckeditor.fields.RichTextField()),
                ('image1', models.ImageField(upload_to='abouts/')),
                ('image2', models.ImageField(upload_to='abouts/')),
                ('image3', models.ImageField(upload_to='abouts/')),
            ],
        ),
    ]
