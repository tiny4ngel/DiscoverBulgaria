from django.test import TestCase
from django.urls import resolve, reverse

from discoverBulgaria.bulgaria.models import Landmarks
from discoverBulgaria.bulgaria.views import HistoricFiguresListView, LandmarksView, LandmarkDetailView
from discoverBulgaria.users.models import AppUser, Profile


class BaseTest(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
        )
        self.client.login(email=self.user.email, password='testpassword')
        self.profile = Profile.objects.create(
            first_name="Test",
            last_name="User",
            nationality="BG",
            user=self.user,
        )

    def check_user_authenticated(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def check_template_used(self, response, template_name):
        self.assertTemplateUsed(response, template_name)


class LandmarksGeneralTests(BaseTest):
    url = '/bulgaria/dashboard/'
    template_name = 'pages/landmarks.html'
    view_name = LandmarksView.as_view().__name__

    def test_status_code(self):
        response = self.client.get(self.url)
        self.check_user_authenticated(response)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.check_template_used(response, self.template_name)

    def test_view_connected_correctly(self):
        match = resolve(self.url)
        self.assertEqual(match.func.__name__, self.view_name)

    def test_contains_in_html(self):
        response = self.client.get(self.url)
        self.check_user_authenticated(response)
        self.assertInHTML('Landmarks', response.content.decode())


class HistoricFiguresTests(BaseTest):
    url = '/bulgaria/historic-figures/'
    template_name = 'pages/historic_figures.html'
    view_name = HistoricFiguresListView.as_view().__name__

    def test_status_code(self):
        response = self.client.get(self.url)
        self.check_user_authenticated(response)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.check_template_used(response, self.template_name)

    def test_view_connected_correctly(self):
        match = resolve(self.url)
        self.assertEqual(match.func.__name__, self.view_name)

    def test_contains_in_html(self):
        response = self.client.get(self.url)
        self.check_user_authenticated(response)
        self.assertInHTML('Historic figures', response.content.decode())


class LandmarkDetailTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.landmark = Landmarks.objects.create(
            title="Test Landmark",
            location="Test Location",
            landmark_photo=None,
            trip_time="1 hour",
            historic_context="Test historic context",
            architectural_features="Test architectural features",
            visitor_information="Test visitor information",
            accessibility="Test accessibility information",
            cover_photo=None,
            additional_photo=None
        )
        self.url = reverse('landmark details', args=[self.landmark.pk])
        self.template_name = 'pages/landmark_details.html'
        self.view_name = LandmarkDetailView.as_view().__name__

    def test_status_code(self):
        response = self.client.get(self.url)
        self.check_user_authenticated(response)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.check_template_used(response, self.template_name)

    def test_view_connected_correctly(self):
        match = resolve(self.url)
        self.assertEqual(match.func.__name__, self.view_name)

    def test_contains_in_html(self):
        response = self.client.get(self.url)
        self.check_user_authenticated(response)
        self.assertInHTML(self.landmark.title, response.content.decode())
