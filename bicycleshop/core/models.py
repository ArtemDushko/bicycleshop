import datetime
from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=10, null=True)
    lastname = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=20, null=True, unique=True)
    email = models.CharField(max_length=40, null=True, unique=True)
    birthday = models.DateField(default=datetime.date(2004, 1, 1))
