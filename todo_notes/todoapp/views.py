from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import Project, Todo
from .serializers import TodoModelSerializer, ProjectModelSerializer
from .filters import ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """класс пагинации для Project"""

    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    """класс пагинации для Todo"""

    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    """модель ToDo: доступны все варианты запросов; при удалении меняем is_active"""

    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_fields = ["project"]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
