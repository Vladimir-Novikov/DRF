from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from userapp.serializers import UserModelSerializer
from .models import Project, Todo


# class ProjectModelSerializer(HyperlinkedModelSerializer):
# """Отображение url юзера -> форма post отображается корректно"""
#     class Meta:
#         model = Project
#         fields = "__all__"


class ProjectModelSerializer(serializers.ModelSerializer):
    """Отображение ID юзера -> форма post отображается корректно"""

    # если раскомментировать, то будет полная инфо о юзере, но форма некорректная
    # users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
