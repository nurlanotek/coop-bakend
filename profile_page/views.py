from django.contrib import auth
from django.shortcuts import render, redirect

from django.contrib.auth import logout
# Create your views here.
from django.template import RequestContext


def profile_page(request):
    return render(request, 'profile_page.html')

def home(request):
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    return render(request, 'home.html')