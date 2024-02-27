from django.urls import path
from . import views

app_name = "bicycles"
urlpatterns = [
    path('list/', views.sort_bicycles, name='sort_bicycles'),
    path('edit/<int:pk>/', views.edit_bicycle, name='edit_bicycle'),
    path('sale/<int:pk>/', views.sale_bicycle, name='sale_bicycle'),
    path('add/', views.add_bicycle, name='add_bicycle'),
    path('delete/', views.delete_bicycle, name='delete_bicycle'),
    path('', views.list_bicycles, name='list_bicycles'),
]