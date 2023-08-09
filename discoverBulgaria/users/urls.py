from django.urls import path

from .views import index_no_account, register_user, login_user, UserRegistrationView, logout_user, \
    my_profile, EditProfileView

urlpatterns = (
    path('', index_no_account, name='index no_account'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login_user/', login_user, name='login user'),
    path('logout_user/', logout_user, name='logout user'),
    path('profile/', my_profile, name='my profile'),
    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit profile')
)
