from django.contrib import admin
from django.urls import path, include
from . import  views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('job',views.showjobs, name='job'),
    path('search',views.search, name='search'),
    path('profile_page/', include('profile_page.urls')),
    path('postjob/', include('postjob.urls')),
    path('logout', views.logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
