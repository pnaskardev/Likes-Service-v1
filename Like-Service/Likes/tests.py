from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import LikeEvent, PostEvent

class PostEventTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_data = {
            "post_id": 1,
            "created_by_id": 1
        }

    def test_create_post_event(self):
        response = self.client.post('/register-post/', self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PostEvent.objects.count(), 1)

    def test_list_post_events(self):
        response = self.client.get('/register-post/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LikeEventTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.like_data = {
            "user_id": 1,
            "post_id": 1
        }

    def test_create_like_event(self):
        response = self.client.post('/post-like/', self.like_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LikeEvent.objects.count(), 1)

    def test_get_likes_count(self):
        post_event = PostEvent.objects.create(post_id=1, created_by_id=1)
        response = self.client.get('/like/like-count/', {"post_id": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["like_count"], post_event.likes_count)

    def test_check_like_status(self):
        LikeEvent.objects.create(user_id=1, post_id=1)
        response = self.client.get('/like/check-like-status/', {"user_id": 1, "post_id": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "User has already liked the post")

        response = self.client.get('/like/check-like-status/', {"user_id": 2, "post_id": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "User has not liked the post yet")
