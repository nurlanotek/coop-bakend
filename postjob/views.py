from django.shortcuts import render

# Create your views here.
def postjob(request):
    return render(request, 'postjob.html')


def home(request):
    return render(request, 'home.html')