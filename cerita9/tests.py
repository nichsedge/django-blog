from django.apps import apps
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from cerita9.apps import Cerita9Config


class UnitTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='hantu', password='hantu123')

    def test_story9_using_the_right_template(self):
        response = self.client.get('/story9/')
        self.assertTemplateUsed(response, 'cerita9/index.html')

    def test_register_form(self):
        response = self.client.get('/story9/register/')
        self.assertTemplateUsed(response, 'cerita9/registrasi.html')

    def test_register(self):
        response = self.client.post("/story9/register/", follow=True, data={
            "username": "jaaa",
            "password1": "kenapa123",
            "password2": "kenapa123"
        })

        count = User.objects.count()
        self.assertEqual(count, 2)

    def test_login_not_authenticated(self):
        response = Client().get('/story9/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_post_success(self):
        user = User.objects.create_user(username="orang", password="orang123")
        user.save()

        response2 = self.client.post(reverse("login"), {"username": "orang", "password": "orang123"})
        self.assertEqual(response2.status_code, 302)

    def test_login_post_is_authenticated(self):
        user = User.objects.create_user(username="orang", password="orang123")
        user.save()

        response1 = self.client.post(reverse("login"), {"username": "orang", "password": "orang123"})
        response2 = self.client.get(reverse("login"))

        self.assertEqual(response2.status_code, 302)

    def test_logout(self):
        response = self.client.get('/story9/logout/')
        self.assertEqual(response.status_code, 302)


class TestApp(TestCase):
    def test_apps(self):
        self.assertEqual(Cerita9Config.name, 'cerita9')
        self.assertEqual(apps.get_app_config('cerita9').name, 'cerita9')
