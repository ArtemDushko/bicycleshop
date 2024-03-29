# Generated by Django 5.0.1 on 2024-02-04 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_remove_person_homeaddr_remove_person_passport_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.person')),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('discount', models.IntegerField()),
            ],
            bases=('core.person',),
        ),
    ]
