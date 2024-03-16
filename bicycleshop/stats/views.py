from django.shortcuts import render, redirect
from django.http import HttpResponse
from sales.models import Sale
from customers.models import Customer
from django.db.models import Count, Q, Sum
from django.db.models.functions import TruncMonth
import csv

def display_stats(request):
    sales = Sale.objects.all()
    context = {'sales': sales}

    return render(request, 'stats/list_stats.html', context)

def generate_stats(request):
    if request.method == "POST":
        stats_option = request.POST.get('statistic')
        from_year = int(request.POST.get('from_year'))
        to_year = int(request.POST.get('to_year'))

        context = {}

        if stats_option == 'most_popular_models':
            most_popular_models = Sale.objects.filter(sale_date__year__range=[from_year, to_year])\
                .values('bicycle__make', 'bicycle__modelyear','bicycle__model', 'bicycle__type', 'bicycle__color')\
                .annotate(total_items_sold=Sum('itemssold'))\
                .order_by('-total_items_sold')[:10]
            request.session['most_popular_models'] = list(most_popular_models)
            context['most_popular_models'] = most_popular_models

        elif stats_option == 'top_sales_managers':
            top_sales_managers = Sale.objects.filter(sale_date__year__range=[from_year, to_year])\
                .values('employee__firstname', 'employee__lastname')\
                .annotate(total_items_sold=Sum('itemssold'))\
                .order_by('-total_items_sold')[:10]
            request.session['top_sales_managers'] = list(top_sales_managers)
            context['top_sales_managers'] = top_sales_managers

        elif stats_option == 'inactive_customers':
            active_customer_ids = Sale.objects.filter(sale_date__year__range=[from_year, to_year])\
                .values_list('buyer_id', flat=True)\
                .distinct()
            if active_customer_ids.exists():
                inactive_customers = Customer.objects.exclude(customer_id__in=active_customer_ids)\
                    .values('person_ptr__firstname', 'person_ptr__lastname', 'person_ptr__phone', 'person_ptr__email')\
                    .order_by('person_ptr__lastname')
                request.session['inactive_customers'] = list(inactive_customers)
            else:
                inactive_customers = Customer.objects.none()
                request.session['inactive_customers'] = list(inactive_customers) 
            context['inactive_customers'] = inactive_customers

        elif stats_option == 'months_with_most_purchases':
            months_with_most_purchases = Sale.objects.filter(
                sale_date__year__range=[from_year, to_year])\
                .annotate(month=TruncMonth('sale_date'))\
                .values('month')\
                .annotate(total_items_sold=Sum('itemssold'))\
                .order_by('-total_items_sold')[:10]

            for dict_item in months_with_most_purchases:
                dict_item["month"] = dict_item["month"].strftime("%B, %Y")

            request.session['months_with_most_purchases'] = list(months_with_most_purchases)
            context['months_with_most_purchases'] = months_with_most_purchases

        elif stats_option == 'most_reliable_models':
            most_reliable_models = Sale.objects\
                .values('bicycle__make', 'bicycle__modelyear', 'bicycle__model', 'bicycle__type', 'bicycle__color')\
                .annotate(service_count=Count('service'))\
                .order_by('service_count')[:10]

            request.session['most_reliable_models'] = list(most_reliable_models)
            context['most_reliable_models'] = most_reliable_models

        return render(request, 'stats/list_stats.html', context)

    else:
        return redirect('stats:display_stats')

def export_csv(request, report_type):
    response = HttpResponse(content_type='text/csv')

    if report_type == 'most_popular_models':
        response['Content-Disposition'] = 'attachment; filename="most_popular_models.csv"'
        data_set = request.session.get('most_popular_models', [])
        headers = ['Make', 'Model Year', 'Model', 'Type', 'Color', 'Total Items Sold']

    elif report_type == 'top_sales_managers':
        response['Content-Disposition'] = 'attachment; filename="top_sales_managers.csv"'
        data_set = request.session.get('top_sales_managers', [])
        headers = ['Firstname', 'Lastname', 'Total Items Sold']

    elif report_type == 'inactive_customers':
        response['Content-Disposition'] = 'attachment; filename="inactive_customers.csv"'
        data_set = request.session.get('inactive_customers', [])
        headers = ['Firstname', 'Lastname', 'Phone', 'Email']

    elif report_type == 'months_with_most_purchases':
        response['Content-Disposition'] = 'attachment; filename="months_with_most_purchases.csv"'
        data_set = request.session.get('months_with_most_purchases', [])
        headers = ['Month', 'Itemssold']

    elif report_type == 'most_reliable_models':
        response['Content-Disposition'] = 'attachment; filename="most_reliable_models.csv"'
        data_set = request.session.get('most_reliable_models', [])
        headers = ['Make', 'Model Year', 'Model', 'Type', 'Color', 'Service count']
        
    else:
        return HttpResponse("Unknown report type: {}".format(report_type))


    writer = csv.writer(response)
    writer.writerow(headers)
    for data_item in data_set:
        writer.writerow(data_item.values())

    return response