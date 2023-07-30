from django.urls import include, path

from discoverBulgaria.bulgaria.views import dashboard

urlpatterns = (
    path('dashboard/', dashboard, name='dashboard'),
)


# path('landmarks/<int:pk>/', include([
#             path('details/', landmark_details, name='event details'),
#             path('edit/', landmark_edit, name='event edit'),
#             path('delete/', landmark_delete, name='event delete'),
#         ]))