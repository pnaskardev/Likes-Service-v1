from rest_framework import viewsets, status
from rest_framework import response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Post
from . serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return response.Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return response.Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        post.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_like_count(request, pk):
    like_count = Post.objects.get(pk=pk).likes_count
    return response.Response({"likes_count": like_count})
