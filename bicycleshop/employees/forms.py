from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    ROLE_CHOICES = [
        ('Sales', 'Sales'),
        ('Service', 'Service'),
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    startdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Employee
        fields = [
            'firstname', 
            'lastname', 
            'email', 
            'birthday', 
            'ssn', 
            'employee_id', 
            'passport', 
            'homeaddr',
            'phone',
            'role', 
            'startdate', 
            'salary'
        ]