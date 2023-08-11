from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from discoverBulgaria.bulgaria.models import Landmarks


class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.login(email=self.user.email, password='testpassword')
        self.add_landmark_permission = Permission.objects.get(codename='add_landmarks')
        self.user.user_permissions.add(self.add_landmark_permission)

    def test_add_landmark_view(self):
        response = self.client.get(reverse('add landmark'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/add_landmark.html')


def test_edit_landmark_view(self):
    landmark = Landmarks.objects.create(title='Test Landmark', description='Description')
    response = self.client.get(reverse('landmark edit', args=[landmark.pk]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'pages/landmark_edit.html')


def test_delete_landmark_view(self):
    landmark = Landmarks.objects.create(title='Test Landmark', description='Description')
    response = self.client.get(reverse('landmark delete', args=[landmark.pk]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'pages/landmarks.html')


def test_delete_landmark_success(self):
    landmark = Landmarks.objects.create(title='Test Landmark', description='Description')
    response = self.client.post(reverse('landmark delete', args=[landmark.pk]))
    self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
    self.assertEqual(Landmarks.objects.count(), 0)  # Ensure the object was deleted


class AddLandmarkViewTest(TestCase):
    def test_add_landmark(self):
        data = {
            'title': 'Test Landmark',
            'location': 'Test Location',
            'trip_time': 'Test Trip Time',
            'historic_context': 'Test Historic Context',
            'architectural_features': 'Test Architectural Features',
            'visitor_information': 'Test Visitor Information',
            'accessibility': 'Test Accessibility',
        }
        response = self.client.post(reverse('add landmark'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(Landmarks.objects.count(), 1)  # Ensure the object was created
        new_landmark = Landmarks.objects.first()
        self.assertEqual(new_landmark.title, 'Test Landmark')
        self.assertEqual(new_landmark.location, 'Test Location')
        self.assertEqual(new_landmark.trip_time, 'Test Trip Time')
        self.assertEqual(new_landmark.historic_context, 'Test Historic Context')
        self.assertEqual(new_landmark.architectural_features, 'Test Architectural Features')
        self.assertEqual(new_landmark.visitor_information, 'Test Visitor Information')
        self.assertEqual(new_landmark.accessibility, 'Test Accessibility')

    def test_add_landmark_invalid_data(self):
        data = {
            'title': 43,
            'location': 44444,
            'trip_time': 55,
            'historic_context': 43342,
            'architectural_features': 423234,
            'visitor_information': True,
            'accessibility': False,
        }
        response = self.client.post(reverse('add landmark'), data)
        self.assertEqual(response.status_code, 200)  # Form submission should fail, returning to the same page
        self.assertEqual(Landmarks.objects.count(), 0)  # No new objects should be created
