from rest_framework import serializers

from .models import CustomUser

from rest_framework.authentication import TokenAuthentication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'age']

class LikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']