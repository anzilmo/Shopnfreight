import stat
from django.urls import path

from shopnfreight import settings
from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('',views.home, name='home'),
    path('basa/',views.basa , name='basa'),
    path('login/', views.login, name='login'),  
    path("signup/", views. signup, name="signup"),
    path('logout/',views.logout, name='logout'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('warehouse-login/', views.warehouse_login, name='warehouse_login'),
    path('warehouse-dashboard/', views.warehouse_dashboard, name='warehouse_dashboard'),
    path('manage-customers/', views.manage_customers, name='Manage-Customers'),
    path('shipment/', views.shipment_view, name='shipment'),
    path('manage-customers/', views.manage_customers, name='manage-customers'),

    
    

]

