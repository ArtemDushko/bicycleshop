# Generated by Django 5.0.1 on 2024-01-31 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.person')),
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField()),
                ('salary', models.IntegerField()),
            ],
            bases=('core.person',),
        ),
    ]
