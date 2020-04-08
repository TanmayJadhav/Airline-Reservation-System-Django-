from django.contrib import admin
from .models import Airplane_Details,Reservation_Details

class frmto_list(admin.ModelAdmin):
    list_display = ('Source','Destination','Airlines','Fare_Type','Departure_Time','Arrival_Time','Price')
admin.site.register(Airplane_Details,frmto_list)

class frmto_list(admin.ModelAdmin):
    list_display = ('Name','Email','Flight_Date','Returning_Date','Adults','Children')
admin.site.register(Reservation_Details,frmto_list)
