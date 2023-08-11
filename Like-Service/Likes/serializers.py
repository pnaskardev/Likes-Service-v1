from rest_framework import serializers

from . models import LikeEvent, PostEvent


class LikeEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeEvent
        fields = '__all__'


class PostEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostEvent
        fields = ['post_id', 'created_by_id', 'likes_count']
