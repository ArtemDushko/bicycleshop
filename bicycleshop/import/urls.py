from django.urls import path
from . import views

app_name = "bicycles"
urlpatterns = [
    path('', views.import_view, name='import')
]