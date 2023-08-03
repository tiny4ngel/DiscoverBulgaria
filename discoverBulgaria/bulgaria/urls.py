from django.urls import include, path

from discoverBulgaria.bulgaria.views import dashboard, add_landmark_to_favourites, delete_landmark_from_favourites, \
    landmark_details

urlpatterns = (
    path('dashboard/', dashboard, name='dashboard'),
    path('favourites/<int:pk>/', add_landmark_to_favourites, name='add_landmark_to_favourites'),
    path('favourites/delete/<int:pk>/', delete_landmark_from_favourites, name='delete_landmark_from_favourites'),
    path('landmarks/<int:pk>/', include([
        path('details/', landmark_details, name='landmark details'),
        # path('edit/', landmark_edit, name='landmark edit'),
        # path('delete/', landmark_delete, name='landmark delete'),
    ]))
)
