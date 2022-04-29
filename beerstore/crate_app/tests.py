from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

class HomepageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home_page.html')

    def test_homepage_contains_certain_text(self):
        response = self.client.get('/')
        self.assertContains(response, 'HOMEPAGE')

    def test_homepage_does_not_contain_certain_text(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'I\'m not there.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'ABOUT US')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'I\'m not there.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )