import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from oauth2_provider.decorators import protected_resource
from django.contrib.auth import authenticate
from oauth2_provider.models import AccessToken as Token

import graphene
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

# class Query(graphene.ObjectType):
#     me = graphene.Field(UserType)

#     @protected_resource()
#     def resolve_me(self, info):
#         user = info.context.user
#         return user

class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return CreateUser(user=user)


class Login(graphene.Mutation):
    token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if user is None:
            raise Exception('Invalid login')
        token, created = Token.objects.get_or_create(user=user)
        return Login(token=token.key)

# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field()
#     login = Login.Field()

# schema = graphene.Schema(query=Query, mutation=Mutation)


class RegisterMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return RegisterMutation(user=user)

class LoginMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if user is not None:
            login(info.context, user)
            return LoginMutation(user=user)
        else:
            raise Exception("Invalid credentials")

class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in")
        return user

class Mutation(graphene.ObjectType):
    register = RegisterMutation.Field()
    login = LoginMutation.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
