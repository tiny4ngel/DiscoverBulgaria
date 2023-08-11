from django.contrib import admin
from django.urls import path, include
from .users.views import index_no_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bulgaria/', include('discoverBulgaria.bulgaria.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('discoverBulgaria.users.urls')),
    path('', index_no_account, name='index no_account'),
]

"""
General URL Patterns

This module defines the general URL patterns for the entire application.

- The 'admin/' URL maps to the Django admin site.
- The 'bulgaria/' URL maps to the URL patterns defined in the 'discoverBulgaria.bulgaria.urls' module.
- The 'users/' URL maps to Django's built-in authentication views.
- The 'users/' URL also maps to the URL patterns defined in the 'discoverBulgaria.users.urls' module.
- The '' URL maps to the index_no_account view for the main index page.
"""
