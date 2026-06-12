from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

from home.models import Createuser
from django.contrib import messages


# Create your views here.
def index(request):
    
    if request.user.is_anonymous:
       return redirect('loginuser')
   
    
    
    return render(request,'index.html')
@login_required
    #return HttpResponse("this is a homepage")
def about(request):
    return render(request,'about.html')

