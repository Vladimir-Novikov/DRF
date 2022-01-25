from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import Project, Todo
from .serializers import TodoModelSerializer, ProjectModelSerializer, ProjectSerializer
from .filters import ProjectFilter, TodoFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """класс пагинации для Project"""

    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    """класс пагинации для Todo"""

    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    # def get_serializer_class(self):
    #     # если get получаем полную информацию о юзере, либо только его ID при POST PUT и тд.
    #     if self.request.method in ["GET"]:
    #         return ProjectSerializer
    #     return ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    """модель ToDo: доступны все варианты запросов; при удалении меняем is_active"""

    # queryset = Todo.objects.all()

    # queryset = Todo.objects.filter(is_active=True)   # показ только активных заметок

    queryset = Todo.objects.get_queryset().order_by("-is_active")  # показываем все заметки - сверху активные
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
