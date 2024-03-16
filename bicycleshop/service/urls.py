from django.urls import path
from . import views

app_name = "service"
urlpatterns = [
    path('add/<int:pk>/', views.add_service, name='add_service'),
    path('save/', views.save_service, name='save_service'),
    path('edit/<int:pk>/', views.edit_service, name='edit_service'),
    path('delete/', views.delete_service, name='delete_service'),
    path('', views.list_service, name='list_service'),
]