from django.urls import path
from . import views

urlpatterns = [
    path('like/<str:pk>', views.LikesViewSet.as_view({
        'post': 'create',
    })),
    path('like/check-like-status', views.LikesViewSet.as_view({
        'post': 'create',
    })),
]
