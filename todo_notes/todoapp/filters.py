from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter
from .models import Project, Todo


class ProjectFilter(filters.FilterSet):
    """фильтр по части названия проекта"""

    title = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Project
        fields = ["title"]


class TodoFilter(filters.FilterSet):
    """фильтр по дате создания заметки
    Данные для фильтра нужно указывать в виде - 2021-12-19
    И по проекту (выбор из выпадающего списка)"""

    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Todo
        fields = ["created_at", "project"]
