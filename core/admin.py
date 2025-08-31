# from django.contrib import admin
# from .models import Country
# from .models import Warehouse, Profile

# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#     list_display = ( 'id' ,'country_name', 'city', 'state', 'zip_code', 'phone_number', 'email')
# # Register your models here.
# admin.site.register(Warehouse)

# admin.site.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'user_id_custom')

from django.contrib import admin
from .models import Country, Warehouse, Profile ,Shipment

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name', 'city', 'state', 'zip_code', 'phone_number', 'email')

# Register Warehouse with default admin
admin.site.register(Warehouse)

# Register Profile with custom admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_id_custom')

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('suit_number', 'tracking_number', 'shipping_company', 'weight', 'arrival_date', 'warehouse')
    list_filter = ('shipping_company', 'package_type', 'arrival_date', 'warehouse')
    search_fields = ('suit_number', 'tracking_number', 'shipping_company')
