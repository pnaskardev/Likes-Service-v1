from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


from . models import LikeEvent, PostEvent
from .serializers import LikeEventSerializer, PostEventSerializer


class PostEventViewSet(viewsets.ModelViewSet):
    queryset = PostEvent.objects.all()
    serializer_class = PostEventSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = PostEvent.objects.all()
        serializer = PostEventSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        post_id = request.data["post_id"]
        created_by_id = request.data["created_by_id"]
        serializer = PostEventSerializer(
            post_id=post_id, created_by_id=created_by_id)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Response(status=status.HTTP_201_CREATED)


class LikeEventViewSet(viewsets.ModelViewSet):
    queryset = LikeEvent.objects.all()
    serializer_class = LikeEventSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = LikeEvent.objects.all()
        serializer = LikeEventSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        userId = request.data['user_id']
        post_id = request.data['post_id']

        like_exists = LikeEvent.objects.filter(
            user_id=userId, post_id=post_id).exists()

        if (like_exists):
            return Response("ALready liked this post", status=status.HTTP_208_ALREADY_REPORTED)

        data = {
            'user_id': userId,
            'post_id': post_id
        }
        post_event = PostEvent.objects.get(post_id=post_id)

        serializer = LikeEventSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        post_event.likes_count = post_event.likes_count+1
        post_event.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def post_like(request):
#     userId = request.data['user_id']
#     post_id = request.data['post_id']

#     like_exists = LikeEvent.objects.filter(
#         user_id=userId, post_id=post_id).exists()

#     if (like_exists):
#         return Response("ALready liked this post", status=status.HTTP_208_ALREADY_REPORTED)

#     data = {
#         'user_id': userId,
#         'post_id': post_id
#     }
#     post_event = PostEvent.objects.get(post_id=post_id)

#     serializer = LikeEventSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     post_event.likes_count = post_event.likes_count+1
#     post_event.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_likes_count(request):
    post_id = request.data["post_id"]
    post_event = PostEvent.objects.get(post_id=post_id)
    return Response({"like_count": post_event.likes_count})


@api_view(['GET'])
@permission_classes([AllowAny])
def check_like_status(request):
    user_id = request.data["user_id"]
    post_id = request.data["post_id"]
    if LikeEvent.objects.filter(user_id=user_id, post_id=post_id).exists():
        return Response("User has already liked the post")
    return Response("User has not liked the post yet")
