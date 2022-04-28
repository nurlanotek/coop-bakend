from django.contrib import admin
from .models import Student,Job, Application

# Register your models here.

admin.site.register(Job)
admin.site.register(Student)
admin.site.register(Application)