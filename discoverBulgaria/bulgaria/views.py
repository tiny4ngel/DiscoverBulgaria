from django.shortcuts import render

from discoverBulgaria.bulgaria.models import Landmarks


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
    }
    return render(request, 'classroom/event_details.html', context)