from django.apps import apps
from django.test import TestCase, Client

from cerita8.apps import Cerita8Config


class UnitTest(TestCase):
    def test_story8_using_the_right_template(self):
        response = Client().get('/story8/list')
        self.assertTemplateUsed(response, 'cerita8/books.html')

    # def test_story8_JSON_views(self):
    #     response = Client().get('/story8/list/emyu')
    #     self.assertEqual(response.status_code, 200)


class TestApp(TestCase):
    def test_apps(self):
        self.assertEqual(Cerita8Config.name, 'cerita8')
        self.assertEqual(apps.get_app_config('cerita8').name, 'cerita8')
