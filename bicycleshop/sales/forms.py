from django import forms
from customers.models import Customer
from bicycles.models import Bicycle
from .models import Sale
import datetime

class SaleForm(forms.ModelForm):
    
    sale_date = forms.DateField(initial=datetime.date.today, disabled=True)

    class Meta:
        model = Sale
        fields = ['buyer', 'bicycle', 'itemssold', 'employee']
        widgets = {
            'buyer': forms.Select(attrs={'id': 'buyer-selector'}),
            'bicycle': forms.Select(attrs={'id': 'bicycle-selector'}),
            'employee': forms.Select(attrs={'id': 'employee-selector'}),
            'itemssold': forms.NumberInput(attrs={'id': 'itemssold-input'}),
            # 'totalcost': forms.NumberInput(attrs={'id': 'totalcost-input'}), 
        }