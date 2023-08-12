from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
# router = DefaultRouter()

# router.register('quotes', views.QuoteViewset, basename='quotes')
urlpatterns = [
    # path('', include(router.urls)),
    path('quotes/', views.QuoteViewset.as_view({
        'get': 'list',
        'post': 'create',
    }), name='quotes'),
    path('like/',views.post_like, name='post_like'),
    path('auth/', include('rest_framework.urls')),
    path('users', views.UserAPIView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(),name='user-details')
]