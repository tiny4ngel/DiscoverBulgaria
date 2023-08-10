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
