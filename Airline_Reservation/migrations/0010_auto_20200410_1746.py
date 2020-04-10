# Generated by Django 3.0.3 on 2020-04-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline_Reservation', '0009_auto_20200407_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation_details',
            name='Status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reservation_details',
            name='Children',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
