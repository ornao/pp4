# Generated by Django 3.2.19 on 2023-06-06 17:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]