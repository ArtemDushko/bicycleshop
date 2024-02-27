from django.db import models
from core.models import Person

class Customer(Person):
    customer_id = models.AutoField(primary_key=True)
    discount = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.phone} {self.email}"