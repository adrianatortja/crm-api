from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import Client


class ClientTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPass123!"
        )
        self.other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="TestPass123!"
        )
        self.client.force_authenticate(user=self.user)

    def test_authenticated_user_can_create_client(self):
        url = "/api/clients/"
        data = {
            "name": "Client One",
            "email": "client@example.com",
            "phone": "123456789",
            "company": "Test Company",
            "status": "active",
            "notes": "Important client",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.first().user, self.user)
        self.assertEqual(Client.objects.first().name, "Client One")

    def test_user_only_sees_their_own_clients(self):
        Client.objects.create(
            user=self.user,
            name="My Client",
            email="myclient@example.com",
            phone="111111111",
            company="My Company",
            status="active",
            notes="Mine",
        )
        Client.objects.create(
            user=self.other_user,
            name="Other Client",
            email="otherclient@example.com",
            phone="222222222",
            company="Other Company",
            status="inactive",
            notes="Not mine",
        )

        url = "/api/clients/"
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "My Client")

    def test_user_can_filter_clients_by_status(self):
        Client.objects.create(
            user=self.user,
            name="Active Client",
            email="active@example.com",
            phone="111111111",
            company="Active Company",
            status="active",
            notes="Active one",
        )
        Client.objects.create(
            user=self.user,
            name="Inactive Client",
            email="inactive@example.com",
            phone="222222222",
            company="Inactive Company",
            status="inactive",
            notes="Inactive one",
        )

        url = "/api/clients/?status=active"
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Active Client")
        self.assertEqual(response.data[0]["status"], "active")
        