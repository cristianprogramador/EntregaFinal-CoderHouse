from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),
    path('iniciosesion/',iniciosesion, name='iniciosesion'),
    path('registro/',registro, name='registro'),
]