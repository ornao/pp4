# Generated by Django 3.2.19 on 2023-07-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0006_alter_accomodation_price_per_night'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accomodation',
            options={'ordering': ['accomodation_type']},
        ),
    ]
