from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone
from .forms import BicycleForm
from .models import Bicycle
from sales.models import Sale
from sales.forms import SaleForm
from employees.models import Employee
from customers.models import Customer
from datetime import datetime, timedelta

def list_bicycles(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycles/list_bicycles.html', {'bicycles': bicycles})

def add_bicycle(request):
    if request.method == "POST":
        form = BicycleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bicycle record added.')
            form = BicycleForm()
        else:
            print(form.errors)
    else:
        form = BicycleForm()

    return render(request, 'bicycles/add_bicycle.html', {'form': form})

def edit_bicycle(request, pk):
    bicycle = get_object_or_404(Bicycle, bicycle_id=pk)
    form = BicycleForm(instance=bicycle)

    if request.method == "POST":
        form = BicycleForm(request.POST, instance=bicycle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated.')
            form = BicycleForm(instance=bicycle)
        else:
            messages.error(request, 'Some of the form inputs are not valid.')

    return render(request, 'bicycles/edit_bicycle.html', {'form': form, 'title': 'Edit Bicycle'})

def delete_bicycle(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('emp-pk')
        selected_ids = [id for id in selected_ids if id != '']
        deleted_count, _ = Bicycle.objects.filter(bicycle_id__in=selected_ids).delete()
        print(f"{deleted_count} record(s) deleted")
        messages.success(request, f'Record(s) deleted.')
        return redirect('bicycles:list_bicycles')
    else:
        messages.error(request, 'Invalid method.')
        return redirect('bicycles:list_bicycles')
   
def sort_bicycles(request):
    sort = request.GET.get('sort', 'price')
    order = request.GET.get('order', '')
    if order == 'desc':
        sort = '-' + sort
    
    bicycles = Bicycle.objects.order_by(sort)

    return render(request, 'bicycles/list_bicycles.html', {'bicycles': bicycles, 'sort': sort, 'order': order})

def sale_bicycle(request, pk):
    bicycle = get_object_or_404(Bicycle, bicycle_id=pk)

    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.bicycle = bicycle
            sale.subtotal = sale.itemssold * bicycle.price
            sale.totalcost = sale.subtotal * (1 - sale.buyer.discount / 100)

            if sale.itemssold > bicycle.instock:
                messages.error(request, 'There is insufficient amount of items in stock.')
            else:
                sale.sale_date = timezone.now()
                sale.warranty_end = sale.sale_date + timedelta(days=int(24*30.5))
                bicycle.instock -= sale.itemssold
                bicycle.save()
                sale.save()
                messages.success(request, 'Sale successful. Record added to Sales page.')
                return redirect('bicycles:sale_bicycle', pk=bicycle.bicycle_id)
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        form = SaleForm()

    return render(request, 'bicycles/sale_bicycle.html', {'form': form, 'bicycle': bicycle})

@csrf_exempt
def search_by_makes(request):
    query = request.GET.get('query', '')
    matching_bicycles = Bicycle.objects.filter(make__icontains=query).values_list('bicycle_id', flat=True)
    
    return JsonResponse(list(matching_bicycles), safe=False)

def apply_filters(request):
    price_from = request.GET.get("price_from")
    price_to = request.GET.get("price_to")

    bicycles = Bicycle.objects.all()

    if price_from:
        price_from = float(price_from)
        bicycles = bicycles.filter(price__gte=price_from)

    if price_to:
        price_to = float(price_to)
        bicycles = bicycles.filter(price__lte=price_to)

    return render(request, 'bicycles/list_bicycles.html', {'bicycles': bicycles})