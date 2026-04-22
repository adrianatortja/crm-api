from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from clients.models import Client
from .models import Lead


class LeadTests(APITestCase):
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

        self.my_client = Client.objects.create(
            user=self.user,
            name="My Client",
            email="myclient@example.com",
            phone="111111111",
            company="My Company",
            status="active",
            notes="Mine",
        )

        self.other_client = Client.objects.create(
            user=self.other_user,
            name="Other Client",
            email="otherclient@example.com",
            phone="222222222",
            company="Other Company",
            status="active",
            notes="Not mine",
        )

        self.client.force_authenticate(user=self.user)

    def test_user_can_create_lead_for_own_client(self):
        url = "/api/leads/"
        data = {
            "client": self.my_client.id,
            "title": "New Lead",
            "status": "new",
            "source": "website",
            "notes": "Interested in product",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lead.objects.count(), 1)
        self.assertEqual(Lead.objects.first().client, self.my_client)

    def test_user_cannot_create_lead_for_another_users_client(self):
        url = "/api/leads/"
        data = {
            "client": self.other_client.id,
            "title": "Hack Lead",
            "status": "new",
            "source": "website",
            "notes": "Should fail",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Lead.objects.count(), 0)
        