from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
# warehouse models Cretig by admin 
class Country(models.Model):
    country_logo = models.ImageField(upload_to='country_logos/')
    country_name = models.CharField(max_length=100)
    Warehouse_add = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.FloatField()
    phone_number = PhoneNumberField() 
    email = models.EmailField()
    
