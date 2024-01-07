from django.db import transaction
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from API.models import Project, Contributor
from API.serializers import ProjectListSerializer, ProjectDetailsSerializer
from accounts.serializers import UsersSerializer
from accounts.models import CustomUser

# Create your views here.


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectListSerializer
    details_serializer_class = ProjectDetailsSerializer

    def get_queryset(self):

        return Project.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return self.details_serializer_class
        return super().get_serializer_class()

    """@transaction.atomic
    @action(detail=True, method=['get'])
    def project_users(self, pk):

        project = Project.objects.get(id=pk)
        users = project.user"""

    @action(detail=True, methods=['get'])
    def get_user(self, request, pk=None):
        project = Contributor.objects.filter(project_id=pk)
        project_user = [user.user for user in project]
        print(project_user)
        return project_user


class ProjectUserViewSet(ModelViewSet):

    serializer_class = UsersSerializer

    def get_queryset(self):

        project = Project.objects.get(id=pk)
        projects_users = [user for user in project.user]
        return projects_users


