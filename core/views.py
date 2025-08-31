from django.shortcuts import render,redirect
from .models import Country
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login 
from .models import Warehouse , Profile
from .forms import ShipmentCustomForm
from .models import Shipment
# form .forms import CountryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def basa(request):
    return render(request , 'basa.html')

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
            
            custom_id = user.profile.user_id_custom
            messages.success(request, f"Your User ID is {custom_id}")
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


def warehouse_login(request):
    warehouse_choices = Warehouse.WAREHOUSE_CHOICES

    if request.method == "POST":
        warehouse_id = request.POST.get("warehouse_id")
        try:
            selected_warehouse = Warehouse.objects.get(warehouse_id=warehouse_id)
            # Pass warehouse_id as GET parameter or store in session
            request.session['selected_warehouse_id'] = selected_warehouse.id
            return redirect('warehouse_dashboard')  # Make sure this URL name exists
        except Warehouse.DoesNotExist:
            # Handle invalid warehouse selection
            context = {
                "warehouse_choices": warehouse_choices,
                "error": "Invalid warehouse selected."
            }
            return render(request, "warehouse_login.html", context)

    context = {
        "warehouse_choices": warehouse_choices
    }
    return render(request, "warehouse_login.html", context)

def warehouse_dashboard(request):
    # Example: get warehouse from session
    warehouse_id = request.session.get('selected_warehouse_id')
    selected_warehouse = None
    if warehouse_id:
        from .models import Warehouse
        selected_warehouse = Warehouse.objects.get(id=warehouse_id)
    
    return render(request, 'warehouse_dashboard.html', {
        'selected_warehouse': selected_warehouse
    })
    
# def manage_customers(request):
#     if request.method == "POST":
#         form = ShipmentCustomForm(request.POST)
#         if form.is_valid():
#             # Save data manually
#             data = form.cleaned_data
#             Shipment.objects.create(
#                 suit_number=data['suit_number'],
#                 tracking_number=data['tracking_number'],
#                 shipping_company=data['shipping_company'],
#                 width=data['width'],
#                 height=data['height'],
#                 weight=data['weight'],
#                 package_type=data['package_type'],
#                 arrival_date=data['arrival_date'],
#                 warehouse=data['warehouse']
#             )
#             messages.success(request, f"Shipment {data['suit_number']} saved successfully!")
#             return redirect('manage-customers') 

#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = ShipmentCustomForm()
    
#     return render(request, 'Manage_Customers.html', {'form': form})
def manage_customers(request):
    if request.method == "POST":
        form = ShipmentCustomForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Shipment.objects.create(
                suit_number=data['suit_number'],
                tracking_number=data['tracking_number'],
                shipping_company=data['shipping_company'],
                width=data['width'],
                height=data['height'],
                weight=data['weight'],
                package_type=data['package_type'],
                arrival_date=data['arrival_date'],
                warehouse=data['warehouse']
            )
            messages.success(request, f"Shipment {data['suit_number']} saved successfully!")
            return redirect('manage-customers')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ShipmentCustomForm()
    
    shipments = Shipment.objects.all().order_by('-arrival_date')
    return render(request, 'Manage_Customers.html', {'form': form, 'shipments': shipments})



def shipment_view(request):
    if request.method == "POST":
        form = ShipmentCustomForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Shipment.objects.create(
                suit_number=data['suit_number'],
                tracking_number=data['tracking_number'],
                shipping_company=data['shipping_company'],
                width=data['width'],
                height=data['height'],
                weight=data['weight'],
                package_type=data['package_type'],
                arrival_date=data['arrival_date'],
                warehouse=data['warehouse']
            )
            messages.success(request, f"Shipment {data['suit_number']} saved successfully!")
            return redirect('shipment')  # redirect to the same page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ShipmentCustomForm()
    
    # Fetch all shipments to display
    shipments = Shipment.objects.all().order_by('-arrival_date')
    
    context = {
        'form': form,
        'shipments': shipments
    }
    return render(request, 'Shipment-data.html', context)
