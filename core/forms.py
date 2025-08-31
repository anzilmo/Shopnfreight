from django import forms
from .models import Country
from .models import Warehouse

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        
        
PACKAGE_CHOICES = [
    ('Box', 'Box'),
    ('Envelope', 'Envelope'),
    ('Crate', 'Crate'),
]            


class ShipmentCustomForm(forms.Form):
    suit_number = forms.CharField(max_length=50, label="Suit Number", widget=forms.TextInput(attrs={'class':'form-control'}))
    tracking_number = forms.CharField(max_length=50, label="Tracking Number", widget=forms.TextInput(attrs={'class':'form-control'}))
    shipping_company = forms.CharField(max_length=100, label="Shipping Company", widget=forms.TextInput(attrs={'class':'form-control'}))
    width = forms.FloatField(label="Width (cm)", widget=forms.NumberInput(attrs={'class':'form-control'}))
    height = forms.FloatField(label="Height (cm)", widget=forms.NumberInput(attrs={'class':'form-control'}))
    weight = forms.FloatField(label="Weight (kg)", widget=forms.NumberInput(attrs={'class':'form-control'}))
    package_type = forms.ChoiceField(label="Package Type", choices=PACKAGE_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    arrival_date = forms.DateField(label="Arrival Date", widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(), label="Select Warehouse", widget=forms.Select(attrs={'class':'form-control'}))
    
    # Custom validation example
    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight <= 0:
            raise forms.ValidationError("Weight must be greater than zero.")
        return weight