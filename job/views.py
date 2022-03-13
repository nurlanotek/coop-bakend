from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def job(request):
    return render(request, 'job.html')