from django_filters import rest_framework as filters
from .models import Project


class ProjectFilter(filters.FilterSet):
    """фильтр по части названия"""

    title = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Project
        fields = ["title"]
