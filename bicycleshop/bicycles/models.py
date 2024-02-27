from django.db import models

class Bicycle(models.Model):
    bicycle_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=15, null=True)
    model = models.CharField(max_length=20, null=True)
    modelyear = models.IntegerField()
    type = models.CharField(max_length=15, null=True)
    color = models.CharField(max_length=20, null=True)
    instock = models.IntegerField()
    price = models.FloatField()

