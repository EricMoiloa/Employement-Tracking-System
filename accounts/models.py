from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import  UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_jobseeker = models.BooleanField(default=False,null=True)
    is_employer = models.BooleanField(default=False,null=True)
    gender = models.CharField(max_length=40,blank=True,default="-")
    nationality = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=100,null=True)
    qualification = models.CharField(max_length=100,null=True)
    specialities = models.JSONField(default = list,null=True)
    picture = models.ImageField(null=True,blank=True,default="-")


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return '%s' % (self.email)
    

