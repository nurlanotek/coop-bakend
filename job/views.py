from django.db.models import Q
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import logout
from app1.models import Job

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



