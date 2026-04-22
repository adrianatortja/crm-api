from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class AuthTests(APITestCase):
    def test_user_can_register(self):
        url = reverse("register")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "TestPass123!",
            "password2": "TestPass123!",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, "test@example.com")
        self.assertEqual(User.objects.first().username, "testuser")

    def test_user_can_login(self):
        User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPass123!"
        )

        url = reverse("token_obtain_pair")
        data = {
            "username": "testuser",
            "password": "TestPass123!",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_me_endpoint_requires_authentication(self):
        url = reverse("user-me")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        