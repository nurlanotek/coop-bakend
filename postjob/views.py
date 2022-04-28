from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.
from app1.models import Job, Student


def postjob(request):
    return render(request, 'postjob.html')


def home(request):
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    return render(request, 'home.html')


def addjob(request):
    if request.method=='POST':
        title = request.POST['title']
        location = request.POST['location']
        description = request.POST['description']
        position = request.POST['position']
        payment = request.POST['payment']
        starting_date = request.POST['starting_date']
        finishing_date = request.POST['finishing_date']
        restrictions = request.POST['restrictions']
        requirements = request.POST['requirements']
        deadline = request.POST['deadline']
        job_image = request.FILES['job_image']

        major = request.POST.getlist('major_checks[]')
        is_online = request.POST['inlineRadioOptions']
        is_remote = request.POST['inlineRadioOptions1']
        languages = request.POST.getlist('lang_checks[]')

        major = ' '.join([str(elem) for elem in major])
        languages = ' '.join([str(elem) for elem in languages])


        print(major)
        print(is_online)
        print(is_remote)
        print(languages)

        posting = Job(title=title,location=location,description=description,position=position,payment=payment,major=major, is_online=is_online, is_remote=is_remote,
                      language=languages,start=starting_date,end=finishing_date,restrictions=restrictions,requirements=requirements,deadline=deadline,job_img=job_image)
        posting.save()

        success_message = 'job posted successfully'
        messages.success(request, success_message)

        return render(request, 'postjob.html')

def profile(request):
    email = request.user.email
    profile_info = Student.objects.filter(Q(email__contains=email))
    return render(request, 'profile_page.html', {'profile_info': profile_info})