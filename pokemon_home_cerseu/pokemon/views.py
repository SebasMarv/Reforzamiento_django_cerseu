from django.shortcuts import render
from django.http import HttpResponse
from pokemon.models import Pokemon

# Create your views here.

def list_pokemon(request):
    # data_contex = {
    #     'nombre_owner': 'Luis Pardo',
    #     'edad': 56,
    #     'pais': 'Croacia'
    # }
    # catalogs = Catalog.objects.all()
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html', context={'data': pokemons})