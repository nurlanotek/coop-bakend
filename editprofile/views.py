from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.
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
    return render(request, 'editprofile.html')