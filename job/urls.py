from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('job',views.job, name='job'),
    path('profile_page/', include('profile_page.urls')),
    path('postjob/', include('postjob.urls')),
    path('logout', views.logout_user, name='logout')
]