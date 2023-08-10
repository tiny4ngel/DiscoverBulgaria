from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from discoverBulgaria.bulgaria.forms import AddToFavouritesForm
from discoverBulgaria.bulgaria.models import Landmarks, FavouriteLandmarks, HistoricFigure, Leaderboard

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


def historic_figures(request):
    historic_figures_all = HistoricFigure.objects.all()
    context = {'historic_figures_all': historic_figures_all,
               'is_figures_page': True}
    return render(request, 'pages/historic_figures.html', context)


def leaderboard(request):
    leaderboard_data = Leaderboard.objects.order_by('-points')

    context = {
        'leaderboard_data': leaderboard_data,
    }

    return render(request, 'pages/leaderboard.html', context)


def historic_figure_explore(request, pk):
    figure = get_object_or_404(HistoricFigure, pk=pk)
    context = {
        'figure': figure,
    }
    return render(request, 'pages/historic_figure_explore.html', context)


def historic_figure_unlock(request, pk):
    figure = get_object_or_404(HistoricFigure, pk=pk)

    # Check if the user has already unlocked the historic figure
    if request.user in figure.unlocked_by.all():
        messages.warning(request, 'You have already unlocked this historic figure!')
        return redirect('historic figures')

    # Get all the quiz questions for this historic figure
    questions = figure.quiz_questions.all()

    context = {
        'figure': figure,
        'questions': questions,
    }

    if request.method == 'POST':
        user_points = 0
        for question in questions:
            selected_answer = request.POST.get(f"question{question.id}")
            correct_choice = question.choices.get(is_correct=True).choice_text
            if selected_answer == correct_choice:
                user_points += 10
            else:
                # If any answer is incorrect, display an error message and return to the quiz page
                messages.error(request, f'Incorrect answer for "{question.question_text}". Try again.')
                return render(request, 'pages/quiz.html', context)

        # Update the leaderboard entry for the user
        leaderboard_entry, created = Leaderboard.objects.get_or_create(user=request.user)
        leaderboard_entry.points += user_points
        leaderboard_entry.save()
        figure.unlocked_by.add(request.user)

        messages.success(request, 'Historic figure unlocked successfully!')
        # Redirect to the leaderboard page or a page showing quiz results
        return redirect('historic figures')

    return render(request, 'pages/quiz.html', context)



