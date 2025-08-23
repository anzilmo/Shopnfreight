from django.urls import path
from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('',views.home, name='home'),
    path('login/', views.login, name='login'),  
    path("signup/", views. signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboardx"),

    
]
