from django.shortcuts import render, redirect, get_object_or_404

from discoverBulgaria.bulgaria.forms import AddToFavouritesForm
from discoverBulgaria.bulgaria.models import Landmarks, FavouriteLandmarks


def dashboard(request):
    all_landmarks = Landmarks.objects.all()
    context = {
        'all_landmarks': all_landmarks,
        'is_dashboard_page': True,
    }

    return render(request, 'pages/landmarks.html', context)


# def landmark_details(request, pk):
#     landmark = Landmarks.objects.filter(pk=pk).get()
#
#     context = {
#         'landmark': landmark,
#         'pk': pk,
#     }
#     return render(request, '#', context)


def add_landmark_to_favourites(request, pk):
    landmark = get_object_or_404(Landmarks, pk=pk)

    if request.method == 'GET':
        form = AddToFavouritesForm(initial={'traveller': request.user,
                                            'landmark': pk})
    else:
        form = AddToFavouritesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'landmark': landmark,
    }

    return render(request, 'pages/landmarks.html', context)
