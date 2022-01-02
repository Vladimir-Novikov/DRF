from django.shortcuts import render

from .models import User
from .serializers import UserModelSerializer
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class UserModelViewSet(UpdateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """модель User: есть возможность просмотра списка и каждого пользователя в
    отдельности, можно вносить изменения, нельзя удалять и создавать;
    настройка сортировки см https://stackoverflow.com/questions/44033670/python-django-rest-framework-unorderedobjectlistwarning/44036414
    """

    # queryset = User.objects.all()
    queryset = User.objects.get_queryset().order_by("id")
    serializer_class = UserModelSerializer
