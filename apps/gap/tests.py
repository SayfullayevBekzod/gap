from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from apps.gap.models import Opinion, Comment


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('gap:login-page')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='secret')

    def test_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'secret'})
        self.assertEqual(response.status_code, 302)  # 302 - Redirect status code
        self.assertRedirects(response, reverse('landing_page'))  # Ensure redirection to the landing page


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('gap:register-page')

    def test_register(self):
        response = self.client.post(self.register_url,
                                    {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200)


