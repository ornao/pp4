# Generated by Django 3.2.19 on 2023-06-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
