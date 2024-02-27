from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]