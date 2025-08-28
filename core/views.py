from django.shortcuts import render,redirect
from .models import Country
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login 
# form .forms import CountryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# User Authitication with django

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login') 

    return render(request, 'Login/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)   
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request , 'Login/login.html')

def logout(request):
    logout(request)
    return redirect(request, 'Login/login.html')     

@login_required
def dashboard(request):
    countries = Country.objects.all()
    return render(request, 'dashboard.html',{'countries': countries})


