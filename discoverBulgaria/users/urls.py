from django.urls import path

from discoverBulgaria.users.views import index_no_account, register_user, login_user, UserRegistrationView, logout_user, \
    my_profile

urlpatterns = (
    path('', index_no_account, name='index no_account'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login_user/', login_user, name='login user'),
    path('logout_user/', logout_user, name='logout user'),
    path('profile/', my_profile, name='my profile')
)