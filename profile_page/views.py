from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.

def profile_page(request):
    return render(request, 'profile_page.html')


def home(request):
    return render(request, 'home.html')