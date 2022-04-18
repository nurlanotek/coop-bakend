from django.contrib import auth
from django.shortcuts import render, redirect

from django.contrib.auth import logout
# Create your views here.
from django.template import RequestContext
from app1.models import Student
from django.contrib.auth.models import User
from django.db.models import Q

def profile_page(request):
    email = request.user.email
    print(email)
    profile_info = Student.objects.filter(Q(email__contains=email))
    print(profile_info)
    return render(request, 'profile_page.html', {'profile_info':profile_info})

def home(request):
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    return render(request, 'home.html')


def editprofile(request):
    email = request.user.email
    print(email)
    profile_info = Student.objects.filter(Q(email__contains=email))
    print(profile_info)
    return render(request, 'editprofile.html', {'profile_info':profile_info})