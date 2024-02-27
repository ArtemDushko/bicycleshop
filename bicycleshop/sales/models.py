from django.db import models
from bicycles.models import Bicycle
from customers.models import Customer
from employees.models import Employee

class Sale(models.Model):
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    itemssold = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    sale_date = models.DateField(auto_now_add=True)
    warranty_end = models.DateField(blank=True, null=True)
    subtotal = models.FloatField(editable=False)
    totalcost = models.DecimalField(max_digits=10, decimal_places=2)
