from django.urls import path
from . import views

app_name = "employees"
urlpatterns = [
    path('list/', views.sort_employees, name='sort_employees'),
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('add/', views.add_employee, name='add_employee'),
    path('delete/', views.delete_employee, name='delete_employee'),
    path('', views.list_employees, name='list_employees'),
]