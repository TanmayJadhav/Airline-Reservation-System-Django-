from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Airplane_Details,Reservation_Details

def login(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/homepage')

    else:    
        if request.method == 'POST':
            username =request.POST['username']
            password =request.POST['password']

            User = auth.authenticate(username=username,password=password)

            if User is not None: # username and password exits and is correct
                auth.login(request,User)
                return redirect('homepage/')
            else:
                messages.info(request,'Invalid Details')
                # return redirect('/')

    return render(request,"login.html",{'title':'Login Page'})


def about(request):
    return render(request,"about.html",{'title':'About Page'})

def signup(request):

    if request.method == 'POST':
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('http://127.0.0.1:8000/signup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('http://127.0.0.1:8000/signup/')
            else:    
                new_user = User.objects.create_user(username=username,email=email,password=password1)
                new_user.save()
                messages.info(request,'User Created')
        else:
            messages.info(request,'Password did not match')
            return redirect('http://127.0.0.1:8000/signup/')
        return redirect('/')    
    else:        
        return render(request,"signup.html",{'title':'Signup Page'})    


def logout(request):
    auth.logout(request);
    return redirect('/')

def homepage(request):
    return render(request, "homepage.html",{'title':'Home Page'})

def back(request):
    return redirect('http://127.0.0.1:8000/homepage/')

def forgotpassword(request):
    if request.method == 'POST':
        username =request.POST['username']
        newpassword =request.POST['newpassword']
        
        
        if User.objects.filter(username=username).exists():
            u = User.objects.get(username=username)
            u.set_password(newpassword)
            u.save()
            messages.info(request,'Password Changed')
            return redirect('http://127.0.0.1:8000/forgotpassword/')

        else:
            messages.info(request,'Username not found!!!')
            return render(request,"forgotpassword.html")
        
    else:
        return render(request,"forgotpassword.html")

def bookingform (request):
    if request.method =='POST':
       
            if request.POST['Show flights']=='Show flights':

                            
                source=request.POST['source']
                destination=request.POST['destination']
                faretype=request.POST['FareType']
                                                                                                                            
                details = Airplane_Details.objects.filter(Source=source).filter(Destination=destination).filter(Fare_Type=faretype)
               
                return render(request,"test.html",{'details':details})

    return render(request,"bookingform.html")


def bookingpage(request,flight_id):
    current_user = request.user
   
    if request.method == 'POST':
        data=Reservation_Details()
        data.Name=request.POST['name']
        data.Email =current_user.email
        data.Adults=request.POST.get('adult',0)
        data.Childern=request.POST.get('children',0)
        data.Flight_Date=request.POST['departing']
        data.Returning_Date=request.POST['returning']
        data.key_id=flight_id

        data.save()

    return render(request,"bookingpage.html",{'user':current_user})


def reservationdetails(request):
    current_user = request.user
    
    users=Reservation_Details.objects.filter(Email=current_user.email)


    return render(request,"reservationdetails.html",{'users':users})


def fulldetails(request,user):
    user_info=Reservation_Details.objects.get(id=user)
    flight_info = Airplane_Details.objects.get(id=user_info.key_id)


    price =int(flight_info.Price)
    adults= int(user_info.Adults)
    children=int(user_info.Adults)
    Total_price=price*adults+price*children
    print(Total_price)

    

    return render(request,"fulldetails.html",{'user':user_info,'fl':flight_info,'price':Total_price})    