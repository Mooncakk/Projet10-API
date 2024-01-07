from rest_framework import serializers

from accounts.models import CustomUser


class UsersSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ['email']


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

