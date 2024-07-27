from django.contrib import admin
from .models import Patient,Doctor

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email' ,'contactNo','address','date_of_birth','gender')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email' ,'contactNo','speciality','date_of_birth','gender')

admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
