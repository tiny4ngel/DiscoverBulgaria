from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from discoverBulgaria.bulgaria.forms import LandmarksForm, LandmarksEditForm, DeleteLandmark
from discoverBulgaria.bulgaria.models import FavouriteLandmarks, Landmarks
from discoverBulgaria.users.forms import UserRegistrationForm, UserUploadsForm
from discoverBulgaria.users.models import Profile, UserUploads

UserModel = get_user_model()


def index_no_account(request):
    """
    Renders the main index page.
    """
    context = {
        'is_index_page': True
    }
    return render(request, 'index.html', context)


def register_user(request):
    """
    Renders the user registration page.
    """
    context = {
        'is_register_page': True
    }
    return render(request, 'registration/register.html', context)


def login_user(request):
    """
    Handles user login functionality.
    If the method is POST, it tries to authenticate the user.
    If the method is GET, it displays the login page.
    """
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
            return redirect('login user')

    else:
        return render(request, 'registration/login.html', context)


class UserLogoutView(LogoutView):
    """
    Logs out the user and redirects to the main index page.
    Also, displays a success message upon logging out.
    """
    next_page = 'index no_account'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You were successfully logged out!')
        return super().dispatch(request, *args, **kwargs)


@login_required
def my_profile(request):
    """
    Displays the logged-in user's profile page including their favorite landmarks.
    """
    uploads = UserUploads.objects.all()
    picture_count = UserUploads.objects.count()
    favorite_landmarks = FavouriteLandmarks.objects.filter(traveller=request.user)
    context = {
        'is_profile_page': True,
        'favorite_landmarks': favorite_landmarks,
        'uploads': uploads,
        'picture_count': picture_count,
    }
    return render(request, 'pages/profile.html', context)


class UserRegistrationView(CreateView):
    """
    Handles the user registration process using a form.
    Upon successful registration, logs in the user and redirects to the main index page.
    """
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'

    success_url = reverse_lazy('index no_account')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Registration successful!')
        return result


class EditProfileView(generic.UpdateView):
    """
    Allows the user to edit their profile details, such as first name, last name, and profile picture.
    """
    model = Profile
    template_name = 'pages/edit_profile.html'
    fields = ['first_name', 'last_name', 'profile_picture']
    success_url = reverse_lazy('my profile')


class AddLandmarkView(CreateView):
    """
    Allows staff to add a new landmark.
    On successful addition, redirects to the dashboard with a success message.
    """
    model = Landmarks
    form_class = LandmarksForm
    template_name = 'pages/add_landmark.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Successfully created Landmark - {self.object.title}")
        return response


def landmark_edit(request, pk):
    """
    Provides functionality for staff to edit details of a specific landmark.
    """
    landmark = Landmarks.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = LandmarksEditForm(instance=landmark)
    else:
        form = LandmarksEditForm(request.POST, instance=landmark)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'landmark': landmark,
    }
    return render(request, 'pages/landmark_edit.html', context)


def landmark_delete(request, pk):
    """
    Allows staff to delete a specific landmark.
    """
    landmark = Landmarks.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteLandmark(instance=landmark)
    else:
        form = DeleteLandmark(request.POST, instance=landmark)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'landmark': landmark,
        'form': form,
    }
    return render(request, 'pages/landmarks.html', context)


def upload_view(request):
    """
    View for uploading user photos.

    This view handles the process of allowing users to upload photos along with a title.
    If the request method is POST, the form is validated and the uploaded photo is associated with the user.
    If the request method is GET, the form is displayed for the user to fill out.
    """
    if request.method == 'POST':
        form = UserUploadsForm(request.POST, request.FILES)
        if form.is_valid():
            user_uploads = form.save(commit=False)
            user_uploads.user = request.user
            user_uploads.save()
            return redirect('my profile')
    else:
        form = UserUploadsForm()

    context = {
        'form': form
    }
    return render(request, 'pages/upload_picture.html', context)
