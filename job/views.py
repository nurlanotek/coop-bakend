from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import logout
from app1.models import Job, Student, Application
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return render(request, 'home.html')

def showjobs(request):
    jobs = Job.objects
    return render(request, 'job.html', { 'jobs':jobs } )

def search(request):
    query = request.GET.get('q')
    results = Job.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(payment__icontains=query))
    return render(request, 'job.html', { 'jobs':results })

def applyfilter(request):
    major = request.GET.getlist('major_checks[]')
    is_online = request.GET.getlist('isonline_checks[]')
    is_remote = request.GET.getlist('isremote_checks[]')
    language = request.GET.getlist('lanuage_checks[]')
    is_paid = request.GET['radioButton']

    if major:
        majors_obj = Job.objects.filter(major__in=major)
    else:
        majors_obj = Job.objects.none()
    if is_online:
        isonline_obj = Job.objects.filter(is_online__in=is_online)
    else:
        isonline_obj = Job.objects.none()
    if is_remote:
        isremote_obj = Job.objects.filter(is_remote__in=is_remote)
    else:
        isremote_obj = Job.objects.none()
    if language:
        language_obj = Job.objects.filter(language__in=language)
    else:
        language_obj = Job.objects.none()
    if is_paid=="Unpaid":
        ispaid_obj = Job.objects.filter(payment__isnull=True)
    else:
        ispaid_obj = Job.objects.none()

    results = majors_obj.union(isonline_obj, isremote_obj,language_obj, ispaid_obj)

    return render(request, 'job.html', {'jobs': results})


def profile(request):
    email = request.user.email
    profile_info = Student.objects.filter(Q(email__contains=email))
    return render(request, 'profile_page.html', {'profile_info': profile_info})


def applyjob(request):

    email = request.user.email
    profile_info = Student.objects.filter(Q(email__contains=email))
    firstname = profile_info.values_list('firstname', flat=True).first()
    lastname = profile_info.values_list('lastname', flat=True).first()
    stdid = profile_info.values_list('stdid', flat=True).first()
    application_date = datetime.date(datetime.now())

    job_title = request.POST['job_title']

    resume = request.FILES.get('resume')
    cover_letter = request.FILES.get('cover_letter')
    transcript = request.FILES.get('transcript')

    print(type(resume))

    application = Application(firstname=firstname, lastname=lastname, email=email, stdid=stdid, application_date=application_date,
                              job_title=job_title, resume=resume,cover_letter=cover_letter,transcript=transcript)
    application.save()

    jobs = Job.objects

    success_message = 'Application for ' + str(job_title) +' was successful'
    messages.success(request, success_message)

    return render(request, 'job.html', { 'jobs':jobs } )