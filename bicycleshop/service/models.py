import datetime
from django.db import models
from sales.models import Sale
from employees.models import Employee

class Service(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    service_startdate = models.DateField()
    service_enddate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comment = models.CharField(max_length=150, null=True, blank=True)