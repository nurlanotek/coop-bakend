from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('postjob/',views.postjob, name='postjob'),
    path('logout', views.logout_user, name='logout')

]