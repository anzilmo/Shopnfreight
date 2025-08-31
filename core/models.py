from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User



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
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id_custom = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.user_id_custom:
            last_profile = Profile.objects.all().order_by('id').last()
            if last_profile:
                last_id = int(last_profile.user_id_custom.replace("USR", ""))
                new_id = f"USR{last_id+1:03d}"
            else:
                new_id = "USR001"
            self.user_id_custom = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.user_id_custom}"
    
    
class Warehouse(models.Model):
    WAREHOUSE_CHOICES = [
        ('ChW001', 'ChW001'),
        ('TUW002', 'TUW002'),
        ('QRW003', 'QRW003'),
        ('UAEW04', 'UAEW04'),
        ('USAW05', 'USAW05'),
        ('BAW006', 'BAW006'),
    ]

    country_name = models.CharField(max_length=100)
    warehouse_id = models.CharField(max_length=10, choices=WAREHOUSE_CHOICES, unique=True)

    def __str__(self):
        return f"{self.country_name} - {self.warehouse_id}"   

class Shipment(models.Model):
    suit_number = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=50)
    shipping_company = models.CharField(max_length=100)
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    package_type = models.CharField(max_length=50)
    arrival_date = models.DateField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.suit_number} - {self.tracking_number}"