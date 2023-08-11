from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('posts/<str:pk>', views.PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('like/like-count/<str:pk>', views.get_like_count, name="get like count"),
]
