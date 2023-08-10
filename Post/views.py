from rest_framework import viewsets

from .models import Post
from . serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PostSerializer
    queryset = Post.objects.all()
