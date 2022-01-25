from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User

# добавил поле id для корректной работы фронта (урок_11) в App.js
class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class UserSerializerVersionTwo(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "is_staff", "is_superuser"]
