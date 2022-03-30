from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.

def postjob(request):
    return render(request, 'postjob.html')


def home(request):
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    return render(request, 'home.html')