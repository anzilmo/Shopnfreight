from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'city', 'state', 'zip_code', 'phone_number', 'email')
