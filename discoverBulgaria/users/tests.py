from django.test import TestCase
from django.urls import resolve
from discoverBulgaria.users.views import index_no_account


class HomepageTests(TestCase):
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_view_connected_correctly(self):
        match = resolve('/')

        self.assertEqual(match.func.__name__, index_no_account.__name__)

    def test_contains_in_html(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertInHTML('A Brief Historical Overview', response.content.decode())
