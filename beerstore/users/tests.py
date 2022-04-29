from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from beerstore.users.forms import CustomUserCreationForm
from beerstore.users.models import CustomUser
from beerstore.users.views import SignUpPageView


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
        username='niki',
        email='n.rizov@gmail.com',
        password='Passw0rd!'
        )
        self.assertEqual(user.username, 'niki')
        self.assertEqual(user.email, 'n.rizov@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='Passw0rd!'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse('sign_up')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'sign_up.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'I\'m not there.')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/sign_up/')
        self.assertEqual(
            view.func.__name__,
            SignUpPageView.as_view().__name__
        )