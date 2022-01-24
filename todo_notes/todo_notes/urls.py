"""todo_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pipes import Template
from re import template
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from userapp.views import UserModelViewSet
from todoapp.views import ProjectModelViewSet, TodoModelViewSet
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from graphene_django.views import GraphQLView
from django.views.generic import TemplateView

# ошибка импорта «force_text» из «django.utils.encoding»
# https://stackoverflow.com/questions/70382084/import-error-force-text-from-django-utils-encoding

schema_view = get_schema_view(
    openapi.Info(
        title="Todo_notes",
        default_version="v1",
        description="Документация к проекту",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)
...


router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todo", TodoModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # re_path(r"^api/(?P<version>v\d)/users/$", UserModelViewSet.as_view({"get": "list"})),
    # path("api/v1/users/", include("userapp.urls", namespace="v1")),
    # path("api/v2/users/", include("userapp.urls", namespace="v2")),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path("", TemplateView.as_view(template_name="index.html")),
]
