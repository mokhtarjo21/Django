from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Myuser(User):

class Myuser(models.Model):
    id=models.AutoField(primary_key=True)
    age=models.IntegerField()
    username=models.CharField(max_length=100)

class Usernative(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isactive=models.BooleanField(default=False)