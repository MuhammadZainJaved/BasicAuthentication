from django.urls import path, include
from .schema import schema
from graphene_django.views import GraphQLView
from oauth2_provider.views.base import TokenView
from .views import *

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('token/', TokenView.as_view(), name='token'),
]

urlpatterns += [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
]