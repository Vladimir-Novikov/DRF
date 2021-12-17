from django.db import models
from userapp.models import User


class Project(models.Model):
    """Модель проекта, для которого записаны TODO"""

    title = models.TextField(verbose_name="Название", max_length=128, blank=False, null=False)
    repo_link = models.URLField(verbose_name="Ссылка на репозиторий", max_length=128, blank=True, null=True)
    users = models.ManyToManyField(User, verbose_name="Работают с проектом")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"


class Todo(models.Model):
    """Модель заметка"""

    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст заметки", max_length=512, blank=False, null=False)
    created_at = models.DateTimeField(verbose_name="Создано", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True)
    user = models.ForeignKey(User, verbose_name="Автор заметки", on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Заметка активна", default=True)

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.text}"
