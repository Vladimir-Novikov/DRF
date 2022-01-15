from django.urls import path
from .views import UserModelViewSet


app_name = "userapp"

urlpatterns = [
    path(r"", UserModelViewSet.as_view({"get": "list"})),
]
