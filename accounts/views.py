from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from home.models import Createuser
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
# Create your views here.
def createuser(request):
    if request.method=="POST":
     name = request.POST.get('name')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     password  = request.POST.get('password')

     if User.objects.filter(username=name).exists():

      messages.error(
        request,
        "Username already exists."
      )

      return render(request, 'createuser.html')

     if User.objects.filter(email=email).exists():

      messages.error(
        request,
        "Email already registered."
      )

      return render(request, 'createuser.html')

     user=User.objects.create_user(
       username=name,
       email=email,
       password=password
     )
     UserProfile.objects.create(
            user=user ,
            phone=phone
        )
    #  createuser = Createuser(name=name,email=email,phone=phone)
    #  createuser.save()
     
     messages.success(request, "Account created successfully")
     return redirect('loginuser')
    #  name = request.POST.get('name')
    return render(request,'createuser.html')

def check_username(request):

    username = request.GET.get('name')

    exists = User.objects.filter(
        username=username
    ).exists()

    return JsonResponse({
        'exists': exists
    })

def check_email(request):
   email = request.GET.get('email')

   exists = User.objects.filter(
      email=email
   ).exists()

   return JsonResponse({
      'exists': exists
   })

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect("/")
        else:
          messages.error(request,"Invalid username or password."  )
          return render(request,'login.html' )
 
    # No backend authenticated the credentials
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('loginuser')