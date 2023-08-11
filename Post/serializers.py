from rest_framework import serializers

from . models import Post
from User.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'created_by']

    def create(self, validated_data):
        user = self.context.get('request').user
        extra_data = {
            'created_by': user
        }
        validated_data.update(extra_data)
        return super().create(validated_data)
