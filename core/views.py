from django.shortcuts import render,redirect
from core.models import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pasword']

        requested_username  = User.objects.filter(username=username)

        if requested_username.exists():
            if requested_username.password == password:
                return redirect('')
            
        else:
            return redirect('/login')
        
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists() == False and password == password2:
                final_user = User(username,first_name,last_name,password,password2)
                final_user.save()

        else:
            return redirect('/signup')

        

    return render(request,'signup.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def shop(request):
    return render(request,'shop.html')

def vegetables(request):
    return render(request,'vegetables.html')


