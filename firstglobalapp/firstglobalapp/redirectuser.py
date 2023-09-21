from django.shortcuts import redirect
from django.urls import reverse

class RedirectUnregisteredUsersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Redirect unauthenticated users to the sign-up page
            return redirect(reverse('signUp'))  # Replace 'signup' with your actual sign-up URL name
        
        response = self.get_response(request)
        return response