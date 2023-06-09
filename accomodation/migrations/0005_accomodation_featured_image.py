# Generated by Django 3.2.19 on 2023-06-19 13:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0004_alter_accomodation_accomodation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
