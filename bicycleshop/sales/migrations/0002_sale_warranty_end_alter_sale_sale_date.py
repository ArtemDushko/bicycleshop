# Generated by Django 5.0.1 on 2024-02-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='warranty_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]