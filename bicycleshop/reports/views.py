from django.shortcuts import render, redirect
from django.http import HttpResponse
from sales.models import Sale
from service.models import Service
from django.db.models import Sum
import csv, datetime

def list_reports(request):
    return render(request, 'reports/list_reports.html')

def generate_reports(request):
    if request.method == "POST":
        reports_option = request.POST.get('statistic')

        if reports_option == 'sales_report':
            sales = Sale.objects.all()
            total_cost = sales.aggregate(total=Sum('totalcost'))['total'] or 0
            total_items_sold = sales.aggregate(total=Sum('itemssold'))['total'] or 0
            now = datetime.datetime.now()
            date_generated = now.strftime("%Y-%m-%d %H:%M:%S")

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="sales_report.csv"'
            
            writer = csv.writer(response)
            writer.writerow(["Date Generated:", date_generated])
            writer.writerow([''])

            writer.writerow(['Sale Date', 'Bicycle', 'Customer', 'Employee', 'Warranty Ends','Items Sold', 'Subtotal', 'Total Cost',])

            for sale in sales:
                writer.writerow([
                    sale.sale_date,
                    sale.bicycle.make + ' ' + sale.bicycle.model,
                    sale.buyer.firstname + ' ' + sale.buyer.lastname,
                    sale.employee.firstname + ' ' + sale.employee.lastname,
                    sale.warranty_end,
                    sale.itemssold,
                    sale.subtotal,
                    sale.totalcost,
                ])

            writer.writerow(["Totals:", '', '', '', '', total_items_sold, '', total_cost])
            
            return response

        elif reports_option == 'service_report':
            services = Service.objects.all()
            total_service_cost = services.aggregate(total=Sum('service_cost'))['total'] or 0
            now = datetime.datetime.now()
            date_generated = now.strftime("%Y-%m-%d %H:%M:%S")

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="service_report.csv"'

            writer = csv.writer(response)
            writer.writerow(["Date Generated:", date_generated])
            writer.writerow([''])

            writer.writerow(['Bicycle', 'Specialist', 'Service Start Date', 'Service End Date', 'Status', 'Service Cost'])

            for service in services:
                writer.writerow([
                    service.sale.bicycle.make + ' ' + service.sale.bicycle.model,
                    service.specialist.firstname + ' ' + service.specialist.lastname,
                    service.service_startdate,
                    service.service_enddate,
                    service.status,
                    service.service_cost
                ])

            writer.writerow(["Totals:", '', '', '', '', total_service_cost])
            
            return response

    return redirect('reports:list_reports')
