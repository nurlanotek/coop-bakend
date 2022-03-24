from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
from django.views import View
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator
from django.template.loader import render_to_string

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.is_active = False
                user.save()

                domain = get_current_site(request).domain
                email_subject = 'Activate your Account'
                email_body = render_to_string("activate.html",
                                              {
                                                'user':user,
                                                'domain':domain,
                                                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                                'token': token_generator.make_token(user)
                                              }
                                              )
                send_mail(
                    email_subject,
                    email_body,
                    'ucaco4350@gmail.com',
                    [str(email)],
                    fail_silently=False
                )
                success_message = 'Verification email sent to ' + str(email)
                messages.success(request, success_message)
                return render(request,'login.html')
        else:
            messages.error(request, 'UserID or Email already in use.')
            return render(request, 'signup.html')

    else:
        return render(request,'signup.html')


def login(request):
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')

class ActivateAccountView(View):
    def get(self,request, uidb64,token):
        try:
            uid = force_text((urlsafe_base64_decode(uidb64)))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user=None

        if user is not None and token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            messages.add_message(request,messages.INFO,'account successfully activated')
            return render(request, 'login.html')
        return render(request, 'activate_failed.html', status=401)
