from http import HTTPStatus
from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.guest_client.get('/second/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_page_shows_correct_context(self):
        """Проверка контекста страниц."""
        response = self.guest_client.get('/')
        self.assertContains(response, 'У меня получилось!')


        # response = self.guest_client.get('/second_page/')
        response = self.guest_client.get('/second/')
        self.assertContains(response, 'А это вторая страница')
