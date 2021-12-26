import json
import os

from sys import platform


from django.conf import settings
from django.core.management import BaseCommand


from todoapp.models import Project, Todo
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
            User.objects.create_superuser(**_user)
        else:
            _user.pop("superuser")
            User.objects.create_user(**_user)


def load_projects():
    """https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/
    создали запись проекта, и после этого добавляем пользователей к этой записи"""

    print("Загрузка проектов...")
    Project.objects.all().delete()
    projects = load_from_json("projects")

    for project in projects:
        project_record = Project.objects.create(title=project["title"], repo_link=project["repo_link"])
        for user in project["users"]:
            project_record.users.add(user)


def load_todos():
    print("Загрузка задач...")
    Todo.objects.all().delete()
    todos = load_from_json("todos")
    for todo in todos:
        project = Project.objects.get(id=todo["project"])
        user = User.objects.get(id=todo["user"])
        Todo.objects.create(project=project, text=todo["text"], user=user, is_active=todo["is_active"])


class Command(BaseCommand):
    def handle(self, *args, **options):

        create_db()
        load_users()
        load_projects()
        load_todos()

        print("Загрузка данных завершена.")
