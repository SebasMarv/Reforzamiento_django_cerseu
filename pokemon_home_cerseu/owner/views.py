from django.shortcuts import render
from django.http import HttpResponse
from owner.models import Owner

# Create your views here.

def list_owner(request):
    # data_contex = {
    #     'nombre_owner': 'Luis Pardo',
    #     'edad': 17,
    #     'pais': 'España'
    # }
    owners = Owner.objects.all()
    return render(request, 'owner/owner_list.html', context={'data': owners})