# Generated by Django 4.1.4 on 2023-01-18 22:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
    ]
