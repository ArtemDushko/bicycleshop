from django import forms
from .models import Bicycle
from customers.models import Customer
from employees.models import Employee
from sales.models import Sale

class BicycleForm(forms.ModelForm):

    MAKE_CHOICES = [
        ('Giant', 'Giant'),
        ('Trek', 'Trek'),
        ('Cannondale', 'Cannondale'),
        ('Specialized', 'Specialized'),
        ('Scott', 'Scott'),
        ('Raleigh', 'Raleigh'),
        ('Pinarello', 'Pinarello'),
        ('Bianchi', 'Bianchi'),
        ('Merida', 'Merida'),
        ('Fuji', 'Fuji')
    ]
    
    TYPE_CHOICES = [
        ('Road', 'Road'),
        ('Mountain', 'Mountain'),
        ('Hybrid', 'Hybrid'),
        ('Cruiser', 'Cruiser'),
        ('BMX', 'BMX'),
        ('Folding', 'Folding'),
        ('Recumbent', 'Recumbent'),
        ('Tandem', 'Tandem'),
        ('Cyclocross', 'Cyclocross'),
        ('Touring', 'Touring'),
        ('Electric', 'Electric'),
        ('Trial', 'Trial'),
        ('Fixie', 'Fixie'),
        ('Fat Tire', 'Fat Tire'),
        ('Gravel', 'Gravel'),
        ('Track', 'Track')
    ]

    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Purple', 'Purple'),
        ('Pink', 'Pink'),
        ('Silver', 'Silver')
    ]
    make = forms.ChoiceField(choices=MAKE_CHOICES)
    type = forms.ChoiceField(choices=TYPE_CHOICES)
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    
    class Meta:
        model = Bicycle
        fields = [
            'make',
            'model',
            'modelyear',
            'type',
            'color',
            'instock',
            'price'
        ]

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = '__all__'