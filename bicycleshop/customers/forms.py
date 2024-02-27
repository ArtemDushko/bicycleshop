from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Customer
        fields = [
            'customer_id',
            'firstname', 
            'lastname', 
            'email',
            'phone',
            'birthday',
            'discount'
        ]