from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomerForm
from .models import Customer

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/list_customers.html', {'customers': customers})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record added.')
            form = CustomerForm()
        else:
            print(form.errors)
    else:
        form = CustomerForm()

    return render(request, 'customers/add_customer.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, customer_id=pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated.')
            form = CustomerForm(instance=customer)
        else:
            messages.error(request, 'Some of the form inputs are not valid.')

    return render(request, 'customers/edit_customer.html', {'form': form, 'title': 'Edit Customer'})

def delete_customer(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('emp-pk') 
        print("delete_customer called with ids:", selected_ids)
        deleted_count, _ = Customer.objects.filter(customer_id__in=selected_ids).delete()
        print(f"{deleted_count} record(s) deleted")
        messages.success(request, f'Record(s) deleted.')
        return redirect('customers:list_customers')
    else:
        messages.error(request, 'Invalid method.')
        return redirect('customers:list_customers')

def sort_customers(request):
    sort = request.GET.get('sort', 'discount')
    order = request.GET.get('order', '')
    print('sorting')
    if order == 'desc':
        sort = '-' + sort
    
    customers = Customer.objects.order_by(sort)

    return render(request, 'customers/list_customers.html', {'customers': customers, 'sort': sort, 'order': order})