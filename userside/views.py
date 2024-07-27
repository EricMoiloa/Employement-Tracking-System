from django.shortcuts import redirect, render
from django.contrib.auth.models import auth,User
from django.http import HttpResponse
from django.contrib import messages
from .models import Patient,Doctor

# Create your views here.


def index(request):
    if request.session.has_key('id'):
        user = User.objects.filter(email = request.session['id'])
        email = request.session['id']
        if Patient.objects.filter(email = email):
            patient = Patient.objects.get(email = email)
            is_patient = True
            context={'current_user':patient,'user':user,'is_patient':is_patient,'session_id':request.session.has_key('id')}
            return render(request,'index.html',context)
        elif Doctor.objects.filter(email = email):
            doctor = Doctor.objects.get(email = email)
            is_doctor = True
            context={'current_user':doctor,'user':user,'is_doctor':is_doctor,'session_id':request.session.has_key('id')}
            return render(request,'index.html',context)
        # .,,.
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        errorEmail =  ""
        errorUsername = ""
        errorPassword = ""
        Patient.objects.all()
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        contactNo = request.POST['contactNo']
        address = request.POST['address']
        month = request.POST['month']
        day = request.POST['day']
        year = request.POST['year']
        date_of_birth = day+"-"+month+"-"+year
        gender = request.POST['gender']
        password = request.POST['password']
        confirmPassoword = request.POST['confirm_password']

        if password == confirmPassoword:
            if User.objects.filter(email=email).exists():
                errorEmail = 'Email already exists'
                context = {'errorEmail':errorEmail,'errorUsername':errorUsername,'errorPassword':errorPassword,'name':name,'surname':surname,'username':username,'email':email,'contactNo':contactNo, 'address':address,'month':month,'day':day, 'year':year, 'gender':gender,'password':password,'confirmPassoword':confirmPassoword, }
                return render(request,'registration.html',context)
            elif User.objects.filter(username = username).exists():
                errorUsername = 'Username Already Exist Choose another one'
                context = {'errorEmail':errorEmail,'errorUsername':errorUsername,'errorPassword':errorPassword,'name':name,'surname':surname,'username':username,'email':email,'contactNo':contactNo, 'address':address,'month':month,'day':day, 'year':year, 'gender':gender,'password':password,'confirmPassoword':confirmPassoword, }
                return render(request,'registration.html',context)
            else:
                new_user = User.objects.create_user(username=username,email=email,password=password)
                new_patient = Patient(name=name,surname=surname,email=email,contactNo=contactNo,address=address,date_of_birth=date_of_birth,gender=gender)
                new_patient.save()
                return redirect('success')
        else:
            errorPassword = 'Passwords Dont Match'
            context = {'errorEmail':errorEmail,'errorUsername':errorUsername,'errorPassword':errorPassword,'name':name,'surname':surname,'username':username,'email':email,'contactNo':contactNo, 'address':address,'month':month,'day':day, 'year':year, 'gender':gender,'password':password,'confirmPassoword':confirmPassoword, }
            return render(request,'registration.html',context)
    else:
        return render(request,'registration.html')


def success(request):
    return render(request,'account_created.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        is_doctor = False
        is_patient = False
        errorUsername = ""

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            currentUser = User.objects.get(username=username)
            request.session['id'] = currentUser.email
            if currentUser.is_superuser:
                return redirect('admin_login')
            else: 
                if Patient.objects.filter(email = currentUser.email):
                    patient = Patient.objects.get(email = currentUser.email)
                    auth.login(request,user)
                    is_patient = True
                    context={'current_user':patient,'user':user,'is_patient':is_patient,'session_id':request.session.has_key('id')}
                    return render(request,'index.html',context)
                elif Doctor.objects.filter(email = currentUser.email):
                    doctor = Doctor.objects.get(email = currentUser.email)
                    auth.login(request,user)
                    is_doctor = True
                    context={'current_user':doctor,'user':user,'is_doctor':is_doctor,'session_id':request.session.has_key('id')}
                    return render(request,'index.html',context)
        else:
            messages.info(request,'Password or Username incorrect')
            return redirect('login')
    else:
        errorUsername = 'Username or Password not correct'
        return render(request,'login.html')
            

def logout(request):
    del request.session['id']
    auth.logout(request)
    return redirect('index')


def adminside(request):
    return render(request,'admin/adminside.html')

def doctors(request):
    if request.session.has_key('id'):
        doctor = Doctor.objects.filter(email=request.session.has_key('id'))
        if doctor:
            context = {} 
        return render(request,'admin/doctors.html')
    else:
        return render(request,'index.html')
    

def patients(request):
    return render(request,'admin/patients.html')

def add_doctor(request):
    if request.method == 'POST':
        errorEmail =  ""
        errorUsername = ""
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        speciality = request.POST['speciality']
        contactNo = request.POST['contactNo']
        month = request.POST['month']
        day = request.POST['day']
        year = request.POST['year']
        date_of_birth = day+"-"+month+"-"+year
        gender = request.POST['gender']

       
        if User.objects.filter(email=email).exists():
            errorEmail = 'Email already exists'
            context = {'errorEmail':errorEmail,'errorUsername':errorUsername,'name':name,'surname':surname,'username':username,'email':email,'contactNo':contactNo, 'month':month,'day':day, 'year':year, 'gender':gender,}
            return render(request,'admin/add_doctor.html',context)
        elif User.objects.filter(username = username).exists():
            errorUsername = 'Doctor with same id already added'
            context = {'errorEmail':errorEmail,'errorUsername':errorUsername,'name':name,'surname':surname,'username':username,'email':email,'contactNo':contactNo, 'month':month,'day':day, 'year':year, 'gender':gender,}
            return render(request,'admin/add_doctor.html',context)
        else:
            new_user = User.objects.create_user(username=username,email=email,password="12345")
            new_Doctor = Doctor(name=name,surname=surname,email=email,contactNo=contactNo,speciality=speciality,date_of_birth=date_of_birth,gender=gender)
            new_Doctor.save()
            return redirect('doctors')
    else:
        return render(request,'admin/add_doctor.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        errorUsername = ""
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser:
                return redirect('adminside')
            else:
                return render(request,'admin/admin_login.html')
        else:
            return render(request,'admin/admin_login.html')

    else:
        return render(request,'admin/admin_login.html')




     
    
