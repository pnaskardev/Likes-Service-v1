from django.urls import path
from . import views

urlpatterns = [
    path('like/<str:pk>/', views.LikesViewSet.as_view({
        'post': 'create',
    }), name="post a like"),
    path('like/check-like-status/<str:pk>',
         views.check_like_status, name="check like status"),
]
