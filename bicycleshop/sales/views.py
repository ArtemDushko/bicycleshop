from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SaleForm
from .models import Sale

def list_sales(request):
    sales = Sale.objects.all()
    return render(request, 'sales/list_sales.html', {'sales': sales})

# def add_sale(request):
#     if request.method == "POST":
#         form = SaleForm(request.POST)
#         if form.is_valid():
#             sale = form.save(commit=False)
#             discount = sale.customer.discount
#             sub_total = sale.bicycle.price * sale.number
#             total_cost = sub_total - (sub_total * discount / 100)
#             sale.sub_total = sub_total
#             sale.total_cost = total_cost
#             sale.save()
#     else:
#         form = SaleForm()
#     return render(request, 'sale/sale_form.html', {'form': form})

def delete_sale(request):
    if request.method == "POST":
        sale_ids = request.POST.getlist('id')
        sale_ids = [id for id in sale_ids if id != '']
        deleted_count, _ = Sale.objects.filter(id__in=sale_ids).delete()
        print(f"{deleted_count} record(s) deleted")
        
        messages.success(request, f'{deleted_count} record(s) deleted successfully.')
        return redirect('sales:list_sales')
    
    else:
        messages.error(request, 'Invalid method.')
        return redirect('sales:list_sales')
   
def sort_sales(request):
    sort = request.GET.get('sort', 'price')
    order = request.GET.get('order', '')
    print('sorting')
    if order == 'desc':
        sort = '-' + sort
    
    sales = Sale.objects.order_by(sort)

    return render(request, 'sales/list_sales.html', {'sales': sales, 'sort': sort, 'order': order})

def invoice_view(request, saleid):
        sale = get_object_or_404(Sale, pk=saleid)
        return render(request, 'sales/invoice.html', {'sale': sale})