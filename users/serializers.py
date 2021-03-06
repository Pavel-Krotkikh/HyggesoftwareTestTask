from rest_framework import serializers
from users.models import User


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email')


class UserFriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id'
