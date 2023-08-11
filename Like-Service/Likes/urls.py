from django.urls import path
from . import views

urlpatterns = [
    path('register-post/', views.PostEventViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name="Register PostEvent"),

    path('like/', views.post_like, name="post a like"),

    path('like/like-count/', views.get_likes_count, name='Likes Count'),

    path('like/check-like-status/',
         views.check_like_status, name="check like status"),
]
