import json
import os

from sys import platform


from django.conf import settings
from django.core.management import BaseCommand


from userapp.models import User


def load_from_json(file_name):
    return json.load(open(os.path.join(settings.JSON_PATH, f"fill_db", f"{file_name}.json"), encoding="utf-8"))


def create_db():
    print("Создание и применение миграций...")
    if platform == "win32":
        os.system("py manage.py flush --no-input")
        os.system("py manage.py makemigrations")
        os.system("py manage.py migrate")
    else:
        os.system("python3 manage.py flush --no-input")
        os.system("python3 manage.py makemigrations")
        os.system("python3 manage.py migrate")


def load_users():
    print("Загрузка пользователей...")
    User.objects.all().delete()
    users = load_from_json("users")

    for _user in users:
        if _user["superuser"]:
            _user.pop("superuser")
            user = User.objects.create_superuser(**_user)
        else:
            _user.pop("superuser")
            user = User.objects.create_user(**_user)
        # UserSettings.objects.create(user=user)


class Command(BaseCommand):
    def handle(self, *args, **options):

        create_db()
        load_users()

        print("Загрузка данных завершена.")
