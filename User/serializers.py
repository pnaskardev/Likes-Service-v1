from rest_framework import serializers

from . models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
