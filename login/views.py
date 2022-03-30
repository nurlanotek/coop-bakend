from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
from django.http import HttpResponse

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request,'profile_page.html')
        else:
            messages.error(request, 'Incorrect credentials.')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')


def home(request):
    return render(request,'home.html')