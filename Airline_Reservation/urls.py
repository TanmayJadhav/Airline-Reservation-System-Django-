
from django.conf.urls import url
from . import views
app_name='Airline_Reservation'

urlpatterns = [
    url('^$',views.login,name='login_page'),
    url('about/',views.about,name='about_page'),
    url('signup/',views.signup,name='signup_page'),
    url('homepage/',views.homepage,name='home_page'),
    url('logout/',views.logout,name='logout_page'),
    url('back/',views.back,name='back_page'),
    url('forgotpassword/',views.forgotpassword,name='forgot_password_page'),
    url('bookingform/',views.bookingform,name='booking_form'),
    url('bookingpage/(?P<flight_id>[−\w]+)/$', views.bookingpage,name='booking_page'),
    url('reservationdetails/', views.reservationdetails,name='reservation_page'),
    url('fulldetails/(?P<user>[−\w]+)/$', views.fulldetails,name='full_details'),
    url('deletedetails/(?P<user>[−\w]+)/$', views.deletedetails,name='delete_details'),
    
]


