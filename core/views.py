from django.shortcuts import render
from .models import Country
# form .forms import CountryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# User Authitication with django
def login(request):
    return render(request,'Login/login.html')

def signup(request):
    return render(request, 'Login/signup.html')

def dashboard(request):
    countries = Country.objects.all()
    return render(request, 'dashboard.html',{'countries': countries})


