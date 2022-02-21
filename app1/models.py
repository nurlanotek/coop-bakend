from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    stdid=models.IntegerField()
    major=models.CharField(max_length=20)
    password = models.CharField(max_length=30, default="")
    year=models.IntegerField()
