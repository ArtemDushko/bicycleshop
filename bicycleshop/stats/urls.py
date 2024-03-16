from django.urls import path
from . import views

app_name = 'stats'
urlpatterns = [
    path('generate/', views.generate_stats, name='generate_stats'),
    path('export_csv/most_popular_models/', views.export_csv, {'report_type': 'most_popular_models'}, name='export_csv_most_popular_models'),
    path('export_csv/top_sales_managers/', views.export_csv, {'report_type': 'top_sales_managers'}, name='export_csv_top_sales_managers'),
    path('export_csv/inactive_customers/', views.export_csv, {'report_type': 'inactive_customers'}, name='export_csv_inactive_customers'),
    path('export_csv/months_with_most_purchases/', views.export_csv, {'report_type': 'months_with_most_purchases'}, name='export_csv_months_with_most_purchases'),
    path('export_csv/most_reliable_models/', views.export_csv, {'report_type': 'most_reliable_models'}, name='export_csv_most_reliable_models'),

    path('', views.display_stats, name='display_stats'),
]