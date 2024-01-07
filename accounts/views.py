from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from accounts.models import CustomUser
from accounts.serializers import UsersSerializer, UserDetailsSerializer


# Create your views here.

class UsersViewSet(ModelViewSet):

    serializer_class = UsersSerializer
    details_serializer_class = UserDetailsSerializer

    #authentication_classes = [authentication.JWTTokenUserAuthentication]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        return CustomUser.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return self.details_serializer_class
        return super().get_serializer_class()

