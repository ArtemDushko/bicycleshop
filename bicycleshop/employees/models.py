import datetime
from django.db import models
from core.models import Person

class Employee(Person):
    employee_id = models.AutoField(primary_key=True)
    startdate = models.DateField(default=datetime.date(2024, 1, 1))
    salary = models.IntegerField()
    ssn = models.IntegerField(default='000000000000', unique=True)
    homeaddr = models.CharField(max_length=40, null=True)
    passport = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.role}"