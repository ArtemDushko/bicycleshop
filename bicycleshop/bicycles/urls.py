from django.urls import path
from . import views

app_name = "bicycles"
urlpatterns = [
    path('list/', views.sort_bicycles, name='sort_bicycles'),
    path('edit/<int:pk>/', views.edit_bicycle, name='edit_bicycle'),
    path('sale/<int:pk>/', views.sale_bicycle, name='sale_bicycle'),
    path('add/', views.add_bicycle, name='add_bicycle'),
    path('delete/', views.delete_bicycle, name='delete_bicycle'),
    path('search_by_makes/', views.search_by_makes, name='search_by_makes'),
    path('apply_filters', views.apply_filters, name='apply_filters'),
    path('', views.list_bicycles, name='list_bicycles'),
]