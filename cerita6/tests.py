from django.test import Client
from django.test import TestCase
from django.urls import resolve, reverse

from cerita6.forms import formEvent
from cerita6.models import Event, Member
from cerita6.views import addEvent


class Story6Test(TestCase):
    def test_url_listEvent(self):
        response = Client().get('/story6/')
        self.assertEqual(response.status_code, 200)

    def test_url_addEvent(self):
        response = Client().get('/story6/add-event')
        self.assertEqual(response.status_code, 200)

    def test_url_addEvent_resolve(self):
        found = resolve('/story6/add-event')
        self.assertEqual(found.func, addEvent)

    def test_html_listEvent(self):
        response = Client().get('/story6/')
        self.assertTemplateUsed(response, 'list-AllEvent.html')

    def test_html_addEvent(self):
        response = Client().get('/story6/add-event')
        self.assertTemplateUsed(response, "add-Event.html")

    def test_content_listEvent(self):
        response = Client().get('/story6/')
        response = response.content.decode('utf8')
        self.assertIn("EVENTS", response)


class FormTest(TestCase):
    def test_form(self):
        form_event = formEvent()
        self.assertFalse(form_event.is_valid())

    def test_fillform(self):
        form_event = formEvent(data={"title": "z"})
        self.assertTrue(form_event.is_valid())


class ModelTest(TestCase):
    def test_instance(self):
        event = Event.objects.create(title="Bermain")
        member = Member.objects.create(name="ihsan")
        self.assertEqual(len(Event.objects.all()), 1)
        self.assertEqual(len(Member.objects.all()), 1)

    def test_str(self):
        event = Event.objects.create(title="Bermain")
        member = Member.objects.create(name="ihsan")
        self.assertEqual(str(event), "Bermain")
        self.assertEqual(str(member), "ihsan")


class ViewTest(TestCase):
    def test_post_addEvent(self):
        response = Client().post(reverse("add-event"), {"title": "z"})
        self.assertEqual(response.url, "/story6/add-event")

    def test_post_joinEvent(self):
        event = Event.objects.create(title="Bermain")

        response = Client().post(reverse("join-event", kwargs={'pk': event.pk}),
                                 {"name": "az"})
        self.assertEqual(response.status_code, 200)

    def test_post_joinEvent_emptyString(self):
        event = Event.objects.create(title="Bermain")
        response = Client().post(reverse("join-event", kwargs={'pk': event.pk}),
                                 {"name": ""})
        self.assertEqual(response.status_code, 302)


'''
class others(TestCase):
    def test_calculate_age(self):
        self.assertEqual(0, calculate(date.today().year))
'''
