from django.db import models
from django.contrib.auth.models import User
from datetime import date,time

# Create your models here.
class Student(models.Model):
    firstname=models.CharField('First Name',max_length=255,default='')
    lastname=models.CharField('Last Name',max_length=255, default='')
    email=models.CharField('Email',max_length=255,default='')
    phone=models.CharField('Phone',max_length=255,default='')
    stdid=models.CharField('StudentID',max_length=255,default='')
    major=models.CharField('Major',max_length=255,default='')
    gpa=models.FloatField('GPA', null=True, blank=True)
    profile_img = models.ImageField('Profile Image', null=True, blank=True, upload_to="profile_img/")
    activated = models.BooleanField('User Activated',default=False)

    def __str__(self):
        return self.lastname

class Job(models.Model):
    title = models.CharField('Title',max_length=255)
    location = models.CharField('Location',max_length=255)
    description = models.CharField('Description',max_length=5000)
    position = models.CharField('Position', max_length=255)
    payment = models.CharField('Payment', max_length=255)
    start=models.DateField('Start Date')
    end=models.DateField('End Date')
    restrictions = models.CharField('Restrictions', max_length=5000)
    requirements = models.CharField('Requirements', max_length=5000)
    deadline = models.DateField('Deadline')
    job_img = models.ImageField('Job Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
