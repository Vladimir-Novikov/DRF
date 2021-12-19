from django.shortcuts import render

from .models import User
from .serializers import UserModelSerializer
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class UserModelViewSet(UpdateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """модель User: есть возможность просмотра списка и каждого пользователя в
    отдельности, можно вносить изменения, нельзя удалять и создавать;
    """

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
