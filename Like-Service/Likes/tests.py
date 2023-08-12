from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    PostEventViewSet,
    LikeEventViewSet,
    get_likes_count,
    check_like_status,
)

class TestUrls(SimpleTestCase):
    def test_register_post_url_resolves(self):
        url = reverse("Register PostEvent")
        self.assertEqual(resolve(url).func.cls, PostEventViewSet)

    def test_post_like_url_resolves(self):
        url = reverse("post a like")
        self.assertEqual(resolve(url).func.cls, LikeEventViewSet)

    def test_like_count_url_resolves(self):
        url = reverse("Likes Count")
        self.assertEqual(resolve(url).func, get_likes_count)

    def test_check_like_status_url_resolves(self):
        url = reverse("check like status")
        self.assertEqual(resolve(url).func, check_like_status)
