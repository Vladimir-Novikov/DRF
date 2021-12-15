from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from userapp.serializers import UserModelSerializer
from .models import Project, Todo


# class ProjectModelSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Project
#         fields = "__all__"


class ProjectModelSerializer(serializers.ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
