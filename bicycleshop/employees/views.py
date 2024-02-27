from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employee

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list_employees.html', {'employees': employees})

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee record added.')
            form = EmployeeForm()
        else:
            print(form.errors)
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, employee_id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated.')
            form = EmployeeForm(instance=employee)
        else:
            messages.error(request, 'Some of the form inputs are not valid.')

    return render(request, 'employees/edit_employee.html', {'form': form, 'title': 'Edit Employee'})

def delete_employee(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('emp-pk')
        selected_ids = [id for id in selected_ids if id != '']
        deleted_count, _ = Employee.objects.filter(employee_id__in=selected_ids).delete()
        print(f"{deleted_count} record(s) deleted")
        messages.success(request, f'Record(s) deleted.')
        return redirect('employees:list_employees')
    else:
        messages.error(request, 'Invalid method.')
        return redirect('employees:list_employees')
   
def sort_employees(request):
    sort = request.GET.get('sort', 'startdate')
    order = request.GET.get('order', '')
    print('sorting')
    if order == 'desc':
        sort = '-' + sort
    
    employees = Employee.objects.order_by(sort)

    return render(request, 'employees/list_employees.html', {'employees': employees, 'sort': sort, 'order': order})