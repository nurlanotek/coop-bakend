from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return render(request, 'home.html')