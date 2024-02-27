from django.urls import path
from . import views

app_name = "sales"
urlpatterns = [
    path('list/', views.sort_sales, name='sort_sales'),
    path('delete/', views.delete_sale, name='delete_sale'),
    path('', views.list_sales, name='list_sales'),
    path('invoice/<int:saleid>/', views.invoice_view, name='invoice')
]