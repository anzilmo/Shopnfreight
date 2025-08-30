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
    

]

