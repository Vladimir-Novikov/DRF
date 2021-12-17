from django.contrib import admin
from .models import User
from todoapp.models import Project, Todo

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Todo)
