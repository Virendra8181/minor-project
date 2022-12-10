

from email import message
from email.mime import image
from operator import concat
from pyexpat.errors import messages
from django.contrib import messages
from typing import OrderedDict
from urllib import request
from django.shortcuts import render,redirect
from products.models import Products
from Review.models import Reviewss
from order.models import Customer
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.views import View

class Login(View):
    def login(request):
            return render (request,"login.html")
    def signup(request):
        return render (request,"signup.html")
    def handelsignup(request):
        if request.method == "POST":
            
            username=request.POST['Username']
            gmail=request.POST['Email']
            password=request.POST['Password']
            myuser=User.objects.create_user(username,gmail,password)
            myuser.save()
            messages.success(request,"your account is success signup")
            return render(request,"signup.html")
        else:

            return HttpResponse("404 - not found")

    def loginpage(request):
        if request.method=="POST":
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']
        
            user=authenticate(username=loginusername,password=loginpassword)
            if user is not None:
                login(request,user)
                messages.success(request,"success fully login page ")
                return redirect('home')
            else:
               messages.error(request,"please enter your right id and password")

              
        return  render(request,"login.html")
    def logout(request):
        logout(request)
        messages.success(request,"log out is suceesfully ")
        return redirect('home')

def home(request):
    data=Products.objects.all()
   
    dic={"data":data}
    return render(request,"index.html",dic)
def search(request):
    if request.method == 'POST':
      n1= request.POST['val']
    data = Products.objects.all().filter( Name= n1 )
    dic={"data":data}
    return render(request,"search.html",dic)

def product(request):
    data=Products.objects.all()
    dic={"data":data}
    return render(request,"products.html",dic)
def cat(request):
    return render(request,"catagrious.html")
def contactus(request):
    return render(request,"contactus.html")
def cart(request):
     data={}
     if request.method == "POST":
        Name= request.POST['Name']
        price=request.POST['price']
        price=request.POST['ID']
        img=request.POST['img']
        data={"Name":Name,"price":price,"image":img} 

        return render (request,"cart.html",data)



def veg (request):
    data=Products.objects.all().filter(Products_type="Vegetable")
    dic={"data":data}
    return render(request,"veg.html",dic)
def Food(request):
    data=Products.objects.all().filter(Products_type="Food")
    dic={"data":data}
    return render(request,"veg.html",dic)
def Dairy(request):
    data=Products.objects.all().filter(Products_type="Dairy")
    dic={"data":data}
    return render(request,"veg.html",dic)

def Review(request):
    if request.method == 'POST':
        Name=request.POST.get('name')
        Email=request.POST.get('Email')
        Subject=request.POST.get('Subject')
        message=request.POST.get('local')
        
        en = Reviewss(Name=Name,Email=Email,Subject=Subject,message=message)
        en.save()
    return redirect('contactus')
def order(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
        data={}
        if request.method == 'POST':
            Name= request.POST.get('name')
            price=request.POST.get('price')
            id=request.POST.get('price')
            user=request.user.username
            print(user)
            
            data={"Name":Name,"price":price,"user":user,"id":id }
        return render(request,"order.html",data)
       
    else:
        return render(request,"login.html",data)