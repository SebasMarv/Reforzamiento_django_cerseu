from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from owner.models import Owner
from django.db.models import Q
from owner.forms import OwnerForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.

def list_owner(request):
    # data_contex = {
    #     'nombre_owner': 'Luis Pardo',
    #     'edad': 17,
    #     'pais': 'España'
    # }
    owners = Owner.objects.all()

    count_peru = Owner.objects.filter(pais='Peru').count()
    count_argentina = Owner.objects.filter(pais='Argentina').count()

    return render(request, 'owner/owner_list.html', context={'data': owners,'peru':count_peru,'arg':count_argentina})

def search_owner(request):
    consult = request.GET.get('q', '')

    print("Query: {}".format(consult))

    results = (
        Q(pais__icontains=consult)
    )

    if consult:
        data_context = Owner.objects.filter(results).distinct()
    else:
        data_context = ''

    return render(request, 'owner/owner_search.html', context={'data': data_context, 'query': consult})

def owner_delete(request, id_owner):
    print("ID: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()

    return redirect('owner_list')


def owner_edit(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre': owner.nombre, 'pais': owner.pais, 'edad': owner.edad, 'identificacion': owner.identificacion})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list')

    return render(request, 'owner/owner_update.html', context={'form': form})

class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_class.html'

class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_create.html'
    success_url = reverse_lazy('owner_list_class')

class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update.html'
    success_url = reverse_lazy('owner_list_class')

class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_class')
    template_name = 'owner/owner_confirm_delete.html'
