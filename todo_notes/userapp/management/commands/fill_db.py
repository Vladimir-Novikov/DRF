import json
import os

from sys import platform

import sqlite3

# import psycopg2

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


def fill_permissions_tables():

    """заполнение таблиц с группами и правами групп пользователей"""

    print("Заполнение таблиц с группами пользователей...")

    groups = [("1", "Администраторы"), ("2", "Разработчики"), ("3", "Владельцы проектов")]

    group_permissions = [
        (1, 1, 32),
        (2, 1, 21),
        (3, 1, 22),
        (4, 1, 23),
        (5, 1, 24),
        (7, 1, 26),
        (8, 1, 27),
        (9, 1, 28),
        (10, 1, 29),
        (11, 1, 30),
        (12, 1, 31),
        (13, 2, 32),
        (14, 2, 24),
        (15, 2, 28),
        (16, 2, 29),
        (17, 2, 30),
        (18, 2, 31),
        (19, 3, 32),
        (20, 3, 24),
        (21, 3, 25),
        (22, 3, 26),
        (23, 3, 27),
        (24, 3, 28),
        (25, 3, 29),
        (26, 3, 30),
        (27, 3, 31),
        (28, 1, 25),
    ]

    user_groups = [(1, 7, 3), (2, 3, 3), (3, 6, 3), (4, 10, 2), (5, 4, 2), (6, 5, 2), (7, 2, 1)]

    # conn = psycopg2.connect(dbname="todo_notes", user="vladimir", password="qwerty", host="127.0.0.1", port="54325")

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO auth_group VALUES(?, ?);", groups)
    conn.commit()

    cursor.executemany("INSERT INTO auth_group_permissions VALUES(?, ?, ?);", group_permissions)
    conn.commit()

    cursor.executemany("INSERT INTO userapp_user_groups VALUES(?, ?, ?);", user_groups)
    conn.commit()


class Command(BaseCommand):
    def handle(self, *args, **options):

        create_db()
        load_users()
        load_projects()
        load_todos()
        fill_permissions_tables()

        print("Загрузка данных завершена.")
