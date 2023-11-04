from .models import *
from django.shortcuts import render, redirect, HttpResponse
import datetime
import jwt
import traceback  
from django.contrib.auth.hashers import check_password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.db.models import Count

from django.db import models
from django.apps import apps
# Create your views here.

def home(request):
    return render(request,"index.html")

def register(request):
    d={}
    try:
        d["name"]=""
        d["username"]=""
        d["gender"]=""
        d["age"]=""
        d["contactno"]=""
        d["email"]=""
        d["password"]=""
        d["confirmpassword"]=""
        d["message"]=""
        if request.method=="POST":
            name = request.POST.get("name").strip()
            username=request.POST.get("username").strip()
            age = request.POST.get("age").strip()
            contactno = request.POST.get("contactno").strip()
            email = request.POST.get("email").strip()
            gender = request.POST.get("gender").strip()
            password = request.POST.get("password").strip()
            confirmpassword = request.POST.get("confirmpassword").strip()
            d["name"]=name
            d["username"]=username
            d["gender"]=gender
            d["age"]=age
            d["contactno"]=contactno
            d["email"]=email
            d["password"]=password
            d["confirmpassword"]=confirmpassword
            d["message"]=""
            temp = User.objects.filter(email=email)
            message=None
            if password and  len(password)<8:
                message="Password length should be greater than 8"
            elif not name or not age or not contactno or not email or not password:
                message="Please fill all the fields"
            elif len(name)>50 or len(age)>2 or len(contactno)>20 or len(email)>200 or len(password)>20:
                message="Field lengths should not cross the limit"
            elif password!=confirmpassword:
                message="Password does not match confirm password"
            d["message"]=message
            if message:
                return render(request, "register.html", d)
            if temp:
                d["show"]=1
                return render(request, "register.html",d)
            verification_token = get_random_string(length=32)
            verification_url = request.build_absolute_uri(reverse('verify_email')) + f'?token={verification_token}&email={email}'
            print(d)
            User.objects.create(name=name, username=username ,email=email, password=password, gender=gender ,contactno=contactno, age=age, token=verification_token, is_verified=False)
            send_mail(
                'Verify your email',
                f'You have successfully created an account on VoyageShare. Click this link to verify your email: {verification_url}\n\nRegards,\nVoyageShare',
                settings.EMAIL_HOST_USER, 
                [email],
                fail_silently=False,
            )
            
            return redirect("login")
        return render(request, "register.html",d)
    except Exception as e:
        print(e)
        d["show"]=2
        return render(request, "register.html", d)

def login(request):
    try:
        d={}
        d["email"]=""
        d["password"]=""
        d["show"]=0
        if request.method=="POST":
            email=request.POST.get("email")
            password = request.POST.get("password")
            d["email"]=email
            d["password"]=password
            temp = User.objects.filter(email=email, is_verified=True)
            print(temp.values())
            if temp:
                if check_password(password,temp[0].password):
                    payload = {
                        'id':temp[0].id,
                        'exp':datetime.datetime.utcnow() + datetime.timedelta(days=7),
                        'iat':datetime.datetime.utcnow()
                    } 
                    token = jwt.encode(payload, 'sanjay@123', algorithm='HS256')
                    response = redirect("/")
                    response.set_cookie(key='jwt', value=token, httponly=True)
                    return response
                else:
                    d["show"]=1
                    return render(request,"login.html", d)

            else:
                d["show"]=1
                return render(request,"login.html", d)

        else:
            return render(request,"login.html", d)
        return render(request,"login.html", d)
    except Exception as e:
        return HttpResponse(f"<h1>Unexpected Error:{e}</h1>")

def logout(request):
    try:
        response = redirect("/auth/login")
        response.delete_cookie('jwt')
        return response
    except Exception as e:
        print(e)
        return HttpResponse("Some error occurred")

def verify_email(request):
    try:
        token = request.GET.get('token')
        email = request.GET.get('email')
        if not token:
            return HttpResponse('<h1>Verification Failed</h1>')
        temp = User.objects.get(email=email)

        if not temp:
            return HttpResponse('<h1>Verification Failed</h1>')
        
        if temp.is_verified:
            return HttpResponse("<h1>Already Verified</h1>")

        if temp.token != token:
            return HttpResponse('<h1>Verification Failed</h1>')

        temp.is_verified = True
        temp.save()

        # return HttpResponse('<h1>Successfully Verified Mail Now you can go login and go to the app</h1>')
        return redirect("login")
    except:
        return HttpResponse('<h1>Verification Failed</h1>')