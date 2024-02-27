# accounts/middleware.py
from django.shortcuts import redirect

# EXEMPT_URLS = [
#     '/login',
#     '/logout',
#     '/register',
#     '/static/'
# ]

def login_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        if not request.user.is_authenticated and 'login' not in request.path:
            return redirect('login')
        return response

    return middleware
