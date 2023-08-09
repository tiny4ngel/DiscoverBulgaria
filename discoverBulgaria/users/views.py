from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from discoverBulgaria.bulgaria.models import FavouriteLandmarks
from discoverBulgaria.users.forms import UserRegistrationForm
from discoverBulgaria.users.models import Profile

UserModel = get_user_model()


def index_no_account(request):
    context = {
        'is_index_page': True
    }
    return render(request, 'index.html', context)


def register_user(request):
    context = {
        'is_register_page': True
    }
    return render(request, 'registration/register.html', context)


@login_required
def my_profile(request):
    favorite_landmarks = FavouriteLandmarks.objects.filter(traveller=request.user)
    context = {
        'is_profile_page': True,
        'favorite_landmarks': favorite_landmarks,
    }
    return render(request, 'pages/profile.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You were successfully logged out!')
    return redirect('index no_account')


class UserRegistrationView(CreateView):
    # form_class=UserCreationForm
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'

    success_url = reverse_lazy('index no_account')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Registration successful!')
        return result


def login_user(request):
    context = {
        'is_login': True
    }
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index no_account')
        else:
            messages.success(request, "There was an error logging in, Try again...")
            return redirect('register user')

    else:
        return render(request, 'registration/login.html', context)


class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'pages/edit_profile.html'
    fields = ['first_name', 'last_name', 'profile_picture']
    success_url = reverse_lazy('my profile')
