from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def manager_check(user):
    return user.profile.authority == 'manager'

@login_required
def home_view(request):
    print(request.user.is_authenticated) 
    return render(request, 'core/home.html')