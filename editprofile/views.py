from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
from app1.models import Student


def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')


def editprofile(request):
    email = request.user.email
    profile_info = Student.objects.filter(Q(email__contains=email))
    return render(request, 'editprofile.html', {'profile_info':profile_info})

def save(request):

    email = request.user.email
    profile_info = Student.objects.filter(Q(email__contains=email))


    save_form = {}

    major = request.GET.get('major')
    gpa = request.GET.get('gpa')
    phone = request.GET.get('phone')
    stdid = request.GET.get('stdid')

    save_form['major'] = str(major)

    try:
        save_form['gpa'] = float(gpa)
    except:
        save_form['gpa'] = None

    if phone.isdecimal():
        save_form['phone'] = phone
    else:
        save_form['phone'] = ''

    if stdid.isdecimal():
        save_form['stdid'] = stdid
    else:
        save_form['stdid'] = ''


    s = Student.objects.get(email=email)
    s.__dict__.update(save_form)
    s.save()

    success_message = 'Profile successfully updated.'
    messages.success(request, success_message)

    return render(request,'profile_page.html', {'profile_info': profile_info})

