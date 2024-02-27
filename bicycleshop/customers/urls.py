from django.urls import path
from . import views

app_name = "customers"
urlpatterns = [
    path('list/', views.sort_customers, name='sort_customers'),
    path('edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('add/', views.add_customer, name='add_customer'),
    path('delete/', views.delete_customer, name='delete_customer'),
    path('', views.list_customers, name='list_customers'),
]