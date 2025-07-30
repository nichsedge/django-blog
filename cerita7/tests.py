from django.apps import apps
from django.test import TestCase, Client
from django.urls import resolve

from cerita7.apps import Cerita7Config
from cerita7.views import story7


# Create your tests here.
class UrlTest(TestCase):
    def test_url(self):
        response = Client().get('/story7/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = Client().get('/story7/')
        self.assertTemplateUsed(response, 'cerita7/story-7.html')

    def test_story7_func(self):
        found = resolve('/story7/')
        self.assertEqual(found.func, story7)


class Story7_Functional_Test(TestCase):
    def test_content(self):
        response = Client().get('/story7/')
        response = response.content.decode('utf8')
        # self.assertIn("Aktivitas", response)
        # self.assertIn("Pengalaman", response)
        # self.assertIn("Prestasi", response)


class TestApp(TestCase):
    def test_apps(self):
        self.assertEqual(Cerita7Config.name, 'cerita7')
        self.assertEqual(apps.get_app_config('cerita7').name, 'cerita7')
