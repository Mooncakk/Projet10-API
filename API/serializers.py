from rest_framework import serializers

from API.models import Project


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Project
        fields = ['id', 'title', 'type', 'description', 'author_user', ]


class ProjectDetailsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Project
        fields = ['id', 'title', 'type', 'description', 'author_user', 'user', ]
