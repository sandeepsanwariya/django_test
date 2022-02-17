from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import *
def register(request):
    if request.method=="POST":
        res = request.POST
        print(res)
        if User.objects.filter(username=res['username']):
            return messages.info(request,'username already exists')
        if User.objects.filter(email=res['email']):
            return messages.info(request,'email already exists')
        user = User.objects.create_user(username=res['username'],first_name=res['first_name'],last_name=res['last_name'],email=res['email'],password=res['password'])
        user.save()
        return  redirect('/')
    else:
        return render(request,'register.html')

def login(request):

    if request.method=="POST":
        res=request.POST
        print(res)
        email=res['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('okkkkk')
            messages.info(request,'invalid credentials')
    else:
        return render(request,'login.html')
def logout(request):
    if request.method=="POST":
        logout(request)
        redirect('/login')
    else:
        return render(request,'index.html')
@login_required(login_url='/login')
def index(request):
    cat = Product.objects.all()
    context = {
        'product': cat
    }
    return render(request,'index.html',context)


@login_required(login_url='/login')
def createproduct(request):
    if request.method=="POST":
        res = request.POST
        print(res)
        user = Product.objects.create(content=res['content'],category_id=res['category'])
        user.save()
        return  redirect('/')
    else:
        cat=Category.objects.all()
        context={
            'category': cat
        }
        return render(request,'createproduct.html',context)