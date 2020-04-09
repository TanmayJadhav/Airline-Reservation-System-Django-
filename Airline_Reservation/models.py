from django.db import models


class Airplane_Details(models.Model):
    Airlines=models.CharField(max_length=50)
    Source=models.CharField(max_length=20)
    Destination=models.CharField(max_length=20)
    Departure_Time=models.CharField(max_length=10)
    Arrival_Time=models.CharField(max_length=10)
    Seats=models.IntegerField()
    Fare_Type=models.CharField(max_length=10)
    Price=models.IntegerField()


class Reservation_Details(models.Model):
    key=models.ForeignKey("Airplane_Details",on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=20,null=True)
    Email=models.EmailField(null=True)
     
    Flight_Date=models.DateField(null=True) 
    Returning_Date=models.DateField(null=True)
    Adults=models.IntegerField(null=True)
    Children=models.IntegerField()
    
