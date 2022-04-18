from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
from app1.models import Student


def home(request):
    return render(request, 'home.html')


def profile_page(request):
    return render(request,'profile_page.html')


def logout_user(request):
    logout(request)
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def editprofile(request):
    email = request.user.email
    print(email)
    profile_info = Student.objects.filter(Q(email__contains=email))
    print(profile_info)
    return render(request, 'editprofile.html', {'profile_info':profile_info})