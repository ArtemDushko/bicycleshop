# Generated by Django 5.0.1 on 2024-02-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='discount',
            field=models.IntegerField(),
        ),
    ]
