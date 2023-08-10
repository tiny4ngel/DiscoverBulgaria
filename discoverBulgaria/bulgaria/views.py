from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, TemplateView

from discoverBulgaria.bulgaria.forms import AddToFavouritesForm
from discoverBulgaria.bulgaria.models import Landmarks, FavouriteLandmarks, HistoricFigure, Leaderboard


class LandmarksView(LoginRequiredMixin, TemplateView):
    """
    Displays a list of landmarks to the user.
    """
    template_name = 'pages/landmarks.html'

    def get_context_data(self, **kwargs):
        """
        Returns context data for rendering landmarks.
        """
        context = super().get_context_data(**kwargs)
        context['all_landmarks'] = Landmarks.objects.all()
        context['is_dashboard_page'] = True
        return context


class LandmarkDetailView(LoginRequiredMixin, DetailView):
    """
    Displays detailed information about a specific landmark.
    """
    model = Landmarks
    template_name = 'pages/landmark_details.html'
    context_object_name = 'landmark'

    def get_context_data(self, **kwargs):
        """
        Returns context data for rendering landmark details.
        """
        context = super().get_context_data(**kwargs)
        context['is_details_page'] = True
        return context


@require_POST
def add_landmark_to_favourites(request, pk):
    """
    Adds a landmark to the user's favourites.

    If the request method is GET, an initial form is presented to the user.
    If the request method is POST and the form is valid, the landmark is added to the user's favourites.

    Notes:
    - This view requires the HTTP method to be POST due to the decorator `@require_POST`.
    """
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


@require_POST
def delete_landmark_from_favourites(request, pk):
    """
    Removes a landmark from the user's favourites list.

    This view tries to fetch the landmark associated with the provided primary key (pk)
    and the currently authenticated user. If found, it deletes the landmark from the
    user's favourites. If not found, an error message is displayed.

    Notes:
    - This view requires the HTTP method to be POST due to the decorator `@require_POST`.
    - If the landmark isn't found in the user's favourites or another error occurs,
      the user is notified via an error message.
    """
    try:
        landmark_to_delete = FavouriteLandmarks.objects.get(pk=pk, traveller=request.user)
        landmark_to_delete.delete()
        messages.success(request, 'Landmark deleted from favorites successfully!')
    except FavouriteLandmarks.DoesNotExist:
        messages.error(request, 'Error! Landmark not found in your favorites.')

    return HttpResponseRedirect(reverse('my profile'))


class HistoricFiguresListView(LoginRequiredMixin, ListView):
    """
    Displays a list of historic figures to the user.
    """
    model = HistoricFigure
    template_name = 'pages/historic_figures.html'
    context_object_name = 'historic_figures_all'

    def get_context_data(self, **kwargs):
        """
        Returns context data for rendering historic figures.
        """
        context = super().get_context_data(**kwargs)
        context['is_figures_page'] = True
        return context


def leaderboard(request):
    """
    Displays the leaderboard with users ordered by points.
    """
    leaderboard_data = Leaderboard.objects.order_by('-points')

    context = {
        'leaderboard_data': leaderboard_data,
    }

    return render(request, 'pages/leaderboard.html', context)


@login_required
def historic_figure_explore(request, pk):
    """
    Allows the user to explore details of a specific historic figure.
    """
    figure = get_object_or_404(HistoricFigure, pk=pk)
    context = {
        'figure': figure,
    }
    return render(request, 'pages/historic_figure_explore.html', context)


@login_required
def display_historic_figure_quiz(request, pk):
    """
    Displays quiz questions related to a specific historic figure.
    """
    figure = get_object_or_404(HistoricFigure, pk=pk)

    if request.user in figure.unlocked_by.all():
        messages.warning(request, 'You have already unlocked this historic figure!')
        return redirect('historic figures')

    questions = figure.quiz_questions.all()

    context = {
        'figure': figure,
        'questions': questions,
    }

    return render(request, 'pages/quiz.html', context)


@login_required
def process_historic_figure_quiz(request, pk):
    """
    Processes the user's answers to the quiz related to a specific historic figure.

    For each correct answer, the user is awarded points. Once the user successfully
    answers all questions, the historic figure is unlocked for the user and their
    points are updated in the leaderboard. If an answer is incorrect, the user is
    notified, and they are redirected to the quiz page to try again.

    Notes:
    - This view expects the HTTP method to be POST as it processes form data.
    """
    figure = get_object_or_404(HistoricFigure, pk=pk)
    questions = figure.quiz_questions.all()

    if request.method == 'POST':
        user_points = 0
        for question in questions:
            selected_answer = request.POST.get(f"question{question.id}")
            correct_choice = question.choices.get(is_correct=True).choice_text
            if selected_answer == correct_choice:
                user_points += 10
            else:
                messages.error(request, f'Incorrect answer for "{question.question_text}". Try again.')
                return redirect('display_historic_figure_quiz', pk=pk)

        leaderboard_entry, created = Leaderboard.objects.get_or_create(user=request.user)
        leaderboard_entry.points += user_points
        leaderboard_entry.save()
        figure.unlocked_by.add(request.user)

        messages.success(request, 'Historic figure unlocked successfully!')
        return redirect('historic figures')
