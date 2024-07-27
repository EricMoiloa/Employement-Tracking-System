from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    contactNo = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.name} - {self.surname}  - {self.contactNo}'
    

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    contactNo = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.name} - {self.surname}  - {self.contactNo}'
    
