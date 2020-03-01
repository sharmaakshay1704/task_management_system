from django.shortcuts import render
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        username=request.POST['username']   
        email=request.POST['email'] 
        user= User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
        user.save()
        print('user created')
        return render(request,'login.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print('user authenticated')
            return render(request,'todo.html',{'username':username})
        else:
            username=None
            return render(request,'login.html',{'error':'No username found!!!'})
        
    else:
        return render(request,'login.html')