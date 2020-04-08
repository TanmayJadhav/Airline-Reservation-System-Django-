# Generated by Django 3.0.3 on 2020-04-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airline_Reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Airlines', models.CharField(max_length=50)),
                ('Source', models.CharField(max_length=20)),
                ('Destination', models.CharField(max_length=20)),
                ('Departure_Time', models.CharField(max_length=10)),
                ('Arrival_Time', models.CharField(max_length=10)),
                ('Flight_Date', models.DateField()),
                ('Returning_Date', models.DateField()),
                ('Adults', models.IntegerField()),
                ('Children', models.IntegerField()),
                ('Fare_Type', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
