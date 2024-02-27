from django.shortcuts import render, redirect
from django.contrib import messages
from bicycles.models import Bicycle
import json

def import_view(request):
    if request.method == 'POST':
        file = request.FILES.get('importfile', None)
        if file and file.name.endswith('.json'):
            try:
                records = json.load(file)
            except json.JSONDecodeError:
                messages.error(request, "Invalid JSON file. Please check syntax in your file.")
                return render(request, 'import/import.html')
            else:
                updated_count, added_count = process_records(records)
                messages.success(request, f"Records successfully imported/updated. Total records updated: {updated_count}. Total records added: {added_count}.")
        else:
            messages.error(request, "Invalid file. Please select a JSON file.")
    return render(request, 'import/import.html')

def process_records(records):
    updated_count = 0
    added_count = 0
    for record in records:
        make = record.get('make')
        model = record.get('model')
        model_year = record.get('modelyear')
        type_ = record.get('type')
        color = record.get('color')
        price = record.get('price')
        instock = record.get('instock')

        bicycle = Bicycle.objects.filter(make=make, model=model, modelyear=model_year, type=type_, color=color, price=price).first()
        if bicycle:
            bicycle.instock += instock
            bicycle.save()
            updated_count += 1
        else:
            bicycle = Bicycle(make=make, model=model, modelyear=model_year, type=type_, color=color, price=price, instock=instock)
            bicycle.save()
            added_count += 1
    return updated_count, added_count