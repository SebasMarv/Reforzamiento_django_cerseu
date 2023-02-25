from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Catalog

# Create your views here.

def list_catalog(request):
    data_contex = {
            'nombre_owner': 'Luis Pardo',
            'edad': 24,
            'pais': 'Perú'
        }
    catalogs = Catalog.objects.all()
    return render(request, 'catalog/catalog_list.html', context={'data': catalogs})