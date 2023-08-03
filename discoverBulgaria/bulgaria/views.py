from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from discoverBulgaria.bulgaria.forms import AddToFavouritesForm
from discoverBulgaria.bulgaria.models import Landmarks, FavouriteLandmarks

from django.http import HttpResponseRedirect
from django.contrib import messages


def dashboard(request):
    all_landmarks = Landmarks.objects.all()
    context = {
        'all_landmarks': all_landmarks,
        'is_dashboard_page': True,
    }

    return render(request, 'pages/landmarks.html', context)


def landmark_details(request, pk):
    landmark = Landmarks.objects.filter(pk=pk).get()
    context = {
        'landmark': landmark,
        'pk': pk,
        'is_details_page': True,
    }
    return render(request, 'pages/landmark_details.html', context)


def add_landmark_to_favourites(request, pk):
    landmark = get_object_or_404(Landmarks, pk=pk)

    already_favourite = FavouriteLandmarks.objects.filter(traveller=request.user, landmark=landmark).exists()

    if already_favourite:
        messages.warning(request, 'This landmark is already in your favorites!')
        return redirect('dashboard')

    if request.method == 'GET':
        form = AddToFavouritesForm(initial={'traveller': request.user,
                                            'landmark': pk})
    else:
        form = AddToFavouritesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Landmark added to favorites successfully!')
            return redirect('dashboard')

    context = {
        'form': form,
        'landmark': landmark,
    }

    return render(request, 'pages/landmarks.html', context)


def delete_landmark_from_favourites(request, pk):
    try:
        landmark_to_delete = FavouriteLandmarks.objects.get(pk=pk, traveller=request.user)
        landmark_to_delete.delete()
        messages.success(request, 'Landmark deleted from favorites successfully!')
    except FavouriteLandmarks.DoesNotExist:
        messages.error(request, 'Error! Landmark not found in your favorites.')

    return HttpResponseRedirect(reverse('my profile'))
