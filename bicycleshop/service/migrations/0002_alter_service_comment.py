# Generated by Django 5.0.1 on 2024-03-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='comment',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]