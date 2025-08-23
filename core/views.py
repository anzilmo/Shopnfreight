from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# User Authitication with django
def login(request):
    return render(request,'Login/login.html')

def signup(request):
    return render(request, 'Login/signup.html')

def dashboard(request):
    
    return render(request, 'dashboard.html')


