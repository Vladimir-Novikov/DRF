import re
import graphene
from graphene_django import DjangoObjectType
from userapp.models import User
from .models import Project, Todo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = "__all__"


class Query(graphene.ObjectType):

    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    user_by_first_name = graphene.List(UserType, first_name=graphene.String(required=False))

    def resolve_user_by_first_name(root, info, first_name=None):
        users = User.objects.all()
        if first_name:
            users = users.filter(first_name=first_name)
        return users

    project_by_id = graphene.List(ProjectType, id=graphene.Int(required=False))

    def resolve_project_by_id(root, info, id=None):
        project = Project.objects.all()
        if id:
            project = project.filter(id=id)
        return project


# Пример запроса и ответа
# Получаем проект с его участниками, а также все связанные заметки с их авторами

# {
#   projectById(id: 6){
#     title
#     todoSet{
#       text
#       user{
#         username
#       }
#     }
#     users{
#       username
#     }
# 	}
# }

# {
#   "data": {
#     "projectById": [
#       {
#         "title": "проект 51",
#         "todoSet": [
#           {
#             "text": "Заметка к проекту_51",
#             "user": {
#               "username": "bubl"
#             }
#           },
#           {
#             "text": "Заметка №3 к проекту_51",
#             "user": {
#               "username": "mark"
#             }
#           },
#           {
#             "text": "заметка № 6",
#             "user": {
#               "username": "petrov"
#             }
#           }
#         ],
#         "users": [
#           {
#             "username": "vasechkin"
#           },
#           {
#             "username": "kohkin"
#           }
#         ]
#       }
#     ]
#   }
# }


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, username, email):
        user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        user.save()
        return UserCreateMutation(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        username = graphene.String(required=False)
        email = graphene.String(required=False)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id, first_name=None, last_name=None, username=None, email=None):
        user = User.objects.get(id=id)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if username:
            user.username = username
        if email:
            user.email = email
        if first_name or last_name or username or email:
            user.save()
        return UserUpdateMutation(user)


class Mutation(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
