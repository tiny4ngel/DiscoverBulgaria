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

"""
URL Patterns

This module defines the URL patterns for user-related views.

- The '' URL maps to the index_no_account view for the main index page.
- The 'register/' URL maps to the UserRegistrationView view for user registration.
- The 'login_user/' URL maps to the login_user view for user login.
- The 'logout_user/' URL maps to the UserLogoutView view for user logout.
- The 'profile/' URL maps to the my_profile view for the user's profile page.
- The 'edit_profile/<int:pk>/' URL maps to the EditProfileView view for editing the user's profile.
"""