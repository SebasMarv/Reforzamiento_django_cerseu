from django.urls import path
from . import views

urlpatterns = [
    path("pokemon_list/", views.list_pokemon, name="pokemon_list")
]