from django.contrib import admin
from django.urls import path, include
from discoverBulgaria.users.views import index_no_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bulgaria/', include('discoverBulgaria.bulgaria.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('discoverBulgaria.users.urls')),
    path('', index_no_account, name='index no_account')
]
