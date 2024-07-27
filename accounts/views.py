import datetime
from tkinter.messagebox import Message
from turtle import st
from django.shortcuts import redirect, render
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer,LoggedUserSerializer
from django.contrib.auth.models import auth
from rest_framework.parsers import MultiPartParser, FormParser





def index(request):
    if request.session.has_key('id'):
        user = User.objects.filter(email = request.session['id'])
        email = request.session['id']
        if User.objects.filter(email = email):
            user = User.objects.get(email = email)
            is_patient = True
            context={'user':user,'session_id':request.session.has_key('id')}
            return render(request,'index.html',context)
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        
        password = request.POST['password']
        confirmPassoword = request.POST['cpassword']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        if password == confirmPassoword:
            errorPassword = 'Passwords Dont Match'
            context = {'errorPassword':errorPassword,}
            return render(request,'registration.html',context)
        if User.objects.filter(email = email).exists():
            errorPassword = 'Email already registered'
            context = {'errorPassword':errorPassword,}
            return render(request,'registration.html',context)
        print("fsgsdg")
        print("fsgsdg")
        print("fsgsdg")
        print("fsgsdg")
        if User.objects.filter(phone_number = phone_number).exists():
            errorPassword = 'Phone number already registered'
            context = {'errorPassword':errorPassword,}
            return render(request,'registration.html',context)
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            User.objects.create_user(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                phone_number = request.POST['phone_number'],
                nationality = request.POST['nationality'],
                is_jobseeker= True,
                is_employer= False,
                gender = request.POST['gender'],
                password = request.POST['password']
            )
            return redirect('success')
    else:
        return render(request,'registration.html')


def success(request):
    return render(request,'account_created.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(rmail=email,password=password)
        if user is not None:
            currentUser = User.objects.get(email=email)
            request.session['id'] = currentUser.email
            user = User.objects.get(email = currentUser.email)
            auth.login(request,user)
            is_patient = True
            context={'current_user':user,'session_id':request.session.has_key('id')}
            return render(request,'index.html',context)
        else:
            Message.info(request,'Password or Username incorrect')
            return redirect('login')
    else:
        return render(request,'login.html')
            

def logout(request):
    del request.session['id']
    auth.logout(request)
    return redirect('index')


