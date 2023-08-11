from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"register", views.UserViewSet)

urlpatterns = [
    path('user/', include(router.urls)),
    path('user/me/', views.CurrentUserView.as_view(), name="me"),
    path('user/login/', TokenObtainPairView.as_view(), name="token-obtain"),
    path('user/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
]
