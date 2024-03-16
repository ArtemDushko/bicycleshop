from django.urls import path
from . import views

app_name = 'reports'
urlpatterns = [
    path('generate/', views.generate_reports, name='generate_reports'),
    # path('export_csv/sales_report/', views.export_csv, {'report_type': 'sales_report'}, name='export_csv_sales_report'),
    # path('export_csv/service_report/', views.export_csv, {'report_type': 'service_report'}, name='export_csv_service_report'),

    path('', views.list_reports, name='list_reports'),
]