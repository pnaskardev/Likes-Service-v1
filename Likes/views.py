from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


from . models import Like
from .serializers import LikeSerializer


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, pk, *args, **kwargs):
        userId = request.user.id
        post_id = pk

        like_exists = Like.objects.filter(
            userId=userId, post_id=post_id).exists()

        if (like_exists):
            return Response("ALready liked this post", status=status.HTTP_208_ALREADY_REPORTED)

        like = Like.objects.create(userId=userId, post_id=post_id)
        serializer = LikeSerializer(like)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_like_status(request, pk):
    user_id = request.user.id
    post_id = pk
    if Like.objects.filter(user_id=user_id, post_id=post_id).exists():
        return Response("User has already liked the post")
    return Response("User has not liked the post yet")
