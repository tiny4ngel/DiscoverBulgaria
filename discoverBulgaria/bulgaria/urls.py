from django.urls import include, path

from discoverBulgaria.bulgaria.views import dashboard, add_landmark_to_favourites


urlpatterns = (
    path('dashboard/', dashboard, name='dashboard'),
    path('favourites/<int:pk>/', add_landmark_to_favourites, name='add_landmark_to_favourites'),
)

# path('landmarks/<int:pk>/', include([
#             path('details/', landmark_details, name='event details'),
#             path('edit/', landmark_edit, name='event edit'),
#             path('delete/', landmark_delete, name='event delete'),
#         ]))
