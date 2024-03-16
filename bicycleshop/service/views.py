from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import  Employee, Sale, Service

from .forms import ServiceForm

def list_service(request):
    services = Service.objects.all()
    invoice_id = request.GET.get('invoice_id')
    if invoice_id and invoice_id.isdigit():
        try:
            sale = Sale.objects.get(pk=invoice_id)
            return redirect('service:add_service', pk=sale.id)
        except Sale.DoesNotExist:
            messages.error(request, "Invoice # does not exist.")
   
    return render(request, 'service/list_service.html', {'services': services})

def add_service(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    employees = Employee.objects.filter(role='Service')
    
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            return save_service(request, form, sale)
        messages.error(request, "Please correct any errors and re-submit the form.")
    else:
        form = ServiceForm(initial={'sale': sale})

    return render(request, 'service/add_service.html', {'form': form, 'sale': sale, 'employees': employees})

def save_service(request):
    # print out alert to know which view we are hitting
    print('Now in save_service')

    if request.method == 'POST':
        print('POST data:', request.POST) # DEBUGGING LINE ADDED HERE
        record_id = request.POST.get('id')
        print(f"record_id: {record_id}") # <<< DEBUGGING LINE
        instance = Service.objects.get(id=record_id) if record_id else None
        print(f"instance: {instance}") # <<< DEBUGGING LINE
        
        form = ServiceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            operation = "updated" if instance else "created"
            messages.success(request, f'Service record has been {operation}.')
            return redirect('service:list_service')
        else:
            print(f"form.errors: {form.errors}")  # <<< DEBUGGING LINE

def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)

    print("Service id in edit_service:", service.id)
    sale = service.sale
    bicycle = sale.bicycle
    buyer = sale.buyer
    employees = Employee.objects.filter(role='Service')

    form = ServiceForm(instance=service)

    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service record has been updated.')
            return redirect('service:list_service')

    context = {'form': form, 'sale': sale, 'bicycle': bicycle, 'buyer': buyer, 'employees': employees}
    return render(request, 'service/edit_service.html', context)

def delete_service(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('id')
        selected_ids = [id for id in selected_ids if id != '']
        deleted_count, _ = Service.objects.filter(id__in=selected_ids).delete()
        print(f"{deleted_count} record(s) deleted")
        messages.success(request, f'Record(s) deleted.')
        return redirect('service:list_service')
    else:
        messages.error(request, 'Invalid method.')
        return redirect('service:list_service')