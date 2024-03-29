# Generated by Django 5.0.1 on 2024-01-31 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10, null=True)),
                ('lastname', models.CharField(max_length=10, null=True)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=40, null=True)),
                ('ssn', models.IntegerField(default='000000000000')),
                ('homeaddr', models.CharField(max_length=40, null=True)),
                ('passport', models.CharField(max_length=50, null=True)),
                ('birthday', models.DateField(default=datetime.date(2024, 1, 1))),
                ('role', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
