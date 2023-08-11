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

    path('check-like/', views.check_like, name="Check like status"),

    path('like-count/', views.like_count, name="Check like status"),

]
