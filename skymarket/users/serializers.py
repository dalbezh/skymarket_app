from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'phone')

    def create(self, validated_data):
        """ Использовать метод create_user, который мы
        написали ранее, для создания нового пользователя. """
        return User.objects.create_user(**validated_data)


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone')


# class UserUpdateSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = '__all__'