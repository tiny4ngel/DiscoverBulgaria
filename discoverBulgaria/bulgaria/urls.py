from django.urls import include, path

from .views import add_landmark_to_favourites, delete_landmark_from_favourites, \
    leaderboard, historic_figure_explore, \
    display_historic_figure_quiz, process_historic_figure_quiz, HistoricFiguresListView, LandmarkDetailView, \
    LandmarksView
from ..users.views import AddLandmarkView, landmark_edit, landmark_delete

urlpatterns = (
    path('dashboard/', LandmarksView.as_view(), name='dashboard'),
    path('favourites/<int:pk>/', add_landmark_to_favourites, name='add_landmark_to_favourites'),
    path('favourites/delete/<int:pk>/', delete_landmark_from_favourites, name='delete_landmark_from_favourites'),
    path('historic-figures/', HistoricFiguresListView.as_view(), name='historic figures'),
    path('historic-figure/<int:pk>/quiz/', display_historic_figure_quiz, name='display_historic_figure_quiz'),
    path('historic-figure/<int:pk>/quiz/process/', process_historic_figure_quiz,
         name='process_historic_figure_quiz'),
    path('historic-figures/explore/<int:pk>/', historic_figure_explore, name='historic_figure_explore'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('landmarks/<int:pk>/', include([
        path('details/', LandmarkDetailView.as_view(), name='landmark details'),
        path('edit/', landmark_edit, name='edit landmark'),
        path('delete/', landmark_delete, name='landmark delete'),
    ])),
    path('add_landmark/', AddLandmarkView.as_view(), name='add landmark'),

)

"""
URL Patterns

This module defines the URL patterns for the application.

- The 'dashboard/' URL maps to the LandmarksView view for the dashboard.
- The 'favourites/<int:pk>/' URL maps to the add_landmark_to_favourites view for adding a landmark to favorites.
- The 'favourites/delete/<int:pk>/' URL maps to the delete_landmark_from_favourites view for deleting a landmark from favorites.
- The 'historic-figures/' URL maps to the HistoricFiguresListView view for historic figures.
- The 'historic-figure/<int:pk>/quiz/' URL maps to the display_historic_figure_quiz view for displaying the historic figure quiz.
- The 'historic-figure/<int:pk>/quiz/process/' URL maps to the process_historic_figure_quiz view for processing the historic figure quiz.
- The 'historic-figures/explore/<int:pk>/' URL maps to the historic_figure_explore view for exploring a historic figure.
- The 'leaderboard/' URL maps to the leaderboard view for the leaderboard.
- The 'landmarks/<int:pk>/' URL includes several sub-patterns related to managing landmarks:
  - 'details/' URL maps to the LandmarkDetailView view for landmark details.
  - 'edit/' URL maps to the landmark_edit view for editing a landmark.
  - 'delete/' URL maps to the landmark_delete view for deleting a landmark.
- The 'add_landmark/' URL maps to the AddLandmarkView view for adding a landmark.
"""