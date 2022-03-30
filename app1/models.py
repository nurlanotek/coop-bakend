from django.db import models
from django.contrib.auth.models import User
from datetime import date,time

# Create your models here.
class Student(models.Model):
    name=models.CharField('Name',max_length=255)
    email=models.CharField('Email',max_length=255)
    phone=models.IntegerField('Phone')
    stdid=models.IntegerField('StudentID')
    major=models.CharField('Major',max_length=255)
    year=models.IntegerField('Year')

    def __str__(self):
        return self.name

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
