from django.contrib import auth
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
from django.http import HttpResponse

from app1.models import Student


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                email = request.user.email
                profile_info = Student.objects.filter(Q(email__contains=email))
                return render(request, 'profile_page.html', {'profile_info': profile_info})
        else:
            messages.error(request, 'Incorrect credentials.')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')


def home(request):
    return render(request,'home.html')