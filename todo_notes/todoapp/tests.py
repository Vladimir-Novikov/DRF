import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase

from mixer.backend.django import mixer

from userapp.views import UserModelViewSet
from .views import ProjectModelViewSet, TodoModelViewSet
from userapp.models import User
from .models import Project, Todo


class TestUserModelViewSet(TestCase):
    def test_get_list(self):
        """APIRequestFactory получение списка юзеров"""
        factory = APIRequestFactory()
        request = factory.get("/api/users/")
        view = UserModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        """APIClient получение детальной информации, с предварительным созданием юзера"""
        user = User.objects.create(
            first_name="Александр", last_name="Пушкин", username="test_user", email="test_1@mail.ru"
        )
        client = APIClient()
        response = client.get(f"/api/users/{user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_unauthorized(self):
        """APIClient редактирование записи неавторизванным юзером"""
        user = User.objects.create(
            first_name="Александр", last_name="Пушкин", username="test_user", email="test_1@mail.ru"
        )
        client = APIClient()
        response = client.put(
            f"/api/users/{user.id}/",
            {"first_name": "Александр", "last_name": "Блок", "username": "test_user", "email": "test_1@mail.ru"},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        """APIClient редактирование записи админом, с созданием админа и его авторизацией"""
        user = User.objects.create(
            first_name="Александр", last_name="Пушкин", username="test_user", email="test_1@mail.ru"
        )
        client = APIClient()
        User.objects.create_superuser("admin", "admin@admin.com", "admin123456")
        client.login(username="admin", password="admin123456")
        response = client.put(
            f"/api/users/{user.id}/",
            {"first_name": "Александр", "last_name": "Блок", "username": "test_user", "email": "test_1@mail.ru"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.last_name, "Блок")
        self.assertEqual(user.first_name, "Александр")
        client.logout()


class TestProjectModelViewSet(TestCase):
    def test_create_project_unauthorized(self):
        """APIRequestFactory создание проекта неавторизованным юзером"""
        factory = APIRequestFactory()
        request = factory.post(
            "/api/projects/", {"title": "Проект тест_1", "repo_link": "http://test.ts", "users": [1]}, format="json"
        )
        view = ProjectModelViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        """APIRequestFactory создание проекта админом, с использованием force_authenticate"""
        factory = APIRequestFactory()
        request = factory.post(
            "/api/projects/", {"title": "Проект тест_1", "repo_link": "http://test.ts", "users": [1]}, format="json"
        )
        admin = User.objects.create_superuser("admin", "admin@admin.com", "admin123456")
        force_authenticate(request, admin)
        view = ProjectModelViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestProjectViewSet(APITestCase):
    def test_get_list(self):
        """APITestCase получение списка проектов"""
        response = self.client.get("/api/projects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        """APITestCase создали проект, юзера, админа, залогинились. Внесли изменения в проект"""
        user = User.objects.create(
            first_name="Александр", last_name="Пушкин", username="test_user", email="test_1@mail.ru"
        )
        project = Project.objects.create(title="Проект API")
        project.users.add(user)
        admin = User.objects.create_superuser("admin", "admin@admin.com", "admin123456")
        self.client.login(username="admin", password="admin123456")
        response = self.client.patch(f"/api/projects/{project.id}/", {"title": "Руслан и Людмила"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.title, "Руслан и Людмила")

    def test_edit_mixer(self):
        """APITestCase + MIXER создали проект, юзера, админа, залогинились. Внесли изменения в проект
        Mixer создал проект и связанные модели сам"""
        project = mixer.blend(Project)
        admin = User.objects.create_superuser("admin", "admin@admin.com", "admin123456")
        self.client.login(username="admin", password="admin123456")
        response = self.client.patch(f"/api/projects/{project.id}/", {"title": "Руслан и Людмила"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.title, "Руслан и Людмила")


class TestTodoViewsSet(APITestCase):
    def test_create_todo_unauthorized(self):
        """APIRequestFactory создание заметки неавторизованным юзером"""
        factory = APIRequestFactory()
        request = factory.post("/api/todo/", {"project": 1, "text": "Тестовые данные"}, format="json")
        view = TodoModelViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list(self):
        """APITestCase получение списка заметок"""
        response = self.client.get("/api/todo/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_mixer(self):
        """APITestCase + MIXER создали заметку, админа, залогинились. Внесли изменения в проект
        Mixer создал заметку и связанные модели сам"""
        todo = mixer.blend(Todo)
        admin = User.objects.create_superuser("admin", "admin@admin.com", "admin123456")
        self.client.login(username="admin", password="admin123456")
        response = self.client.patch(f"/api/todo/{todo.id}/", {"text": "Внести правки в проект_1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = Todo.objects.get(id=todo.id)
        self.assertEqual(todo.text, "Внести правки в проект_1")
