from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        x = auth.authenticate(username=username1, password=password1)

        if x is None:
            auth.login(request,x)
            return redirect('login')
        else:
            return render(request,'profile_page.html')
    else:
        return render(request,'login.html')

