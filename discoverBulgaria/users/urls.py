from django.urls import path

from .views import index_no_account, UserRegistrationView, my_profile, EditProfileView, UserLogoutView, \
    login_user

urlpatterns = (
    path('', index_no_account, name='index no_account'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login_user/', login_user, name='login user'),
    path('logout_user/', UserLogoutView.as_view(), name='logout user'),
    path('profile/', my_profile, name='my profile'),
    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit profile')
)
