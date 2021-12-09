from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(verbose_name="Имя", max_length=64, blank=False, null=False)
    last_name = models.CharField(verbose_name="Фамилия", max_length=64, blank=False, null=False)
    username = models.CharField(unique=True, verbose_name="Ник", max_length=64, blank=False, null=False)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name} / {self.email}"