# Generated by Django 5.0.1 on 2024-01-31 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='startdate',
            field=models.DateField(default=datetime.date(2024, 1, 1)),
        ),
    ]
