from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User
from .serializers import UserSerializer

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        url = reverse("user-list")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email="test@example.com")
        self.assertEqual(user.username, "testuser")

    def test_get_current_user(self):
        user = User.objects.create_user(
            email="user@example.com", username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=user)
        url = reverse("me")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = UserSerializer(user).data
        self.assertEqual(response.data, expected_data)

    def test_token_obtain(self):
        User.objects.create_user(
            email="user@example.com", username="testuser", password="testpassword"
        )
        url = reverse("token-obtain")
        data = {"email": "user@example.com", "password": "testpassword"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_token_refresh(self):
        User.objects.create_user(
            email="user@example.com", username="testuser", password="testpassword"
        )
        refresh_url = reverse("token-refresh")
        obtain_url = reverse("token-obtain")
        obtain_data = {"email": "user@example.com", "password": "testpassword"}
        obtain_response = self.client.post(obtain_url, obtain_data, format="json")
        refresh_data = {"refresh": obtain_response.data["refresh"]}
        refresh_response = self.client.post(refresh_url, refresh_data, format="json")
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)
