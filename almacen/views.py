# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Almacen
from .forms import AlmacenForm
import pprint
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
############################################Views Almacen########################
class AlmacenList(ListView):
    model = Almacen
    fields = ['id', 'codigo', 'descripcion', 'medida', 'unidad', 'existencia', 'cantidad_caja', 'cantidad_rb', 'proveedor', 'ubicacion', 'imagen']
class AlmacenDetail(DetailView):
    model = Almacen
    fields = ['id', 'codigo', 'descripcion', 'medida', 'unidad', 'existencia', 'cantidad_caja', 'cantidad_rb', 'proveedor', 'ubicacion', 'imagen']
class AlmacenCreation(CreateView):
    model = Almacen
    success_url = reverse_lazy('almacen:list_almacen')
    fields = ['id', 'codigo', 'descripcion', 'medida', 'unidad', 'existencia', 'cantidad_caja', 'cantidad_rb', 'proveedor', 'ubicacion', 'imagen']
class AlmacenUpdate(UpdateView):
    model = Almacen
    success_url = reverse_lazy('almacen:list_almacen')
    fields = ['id', 'codigo', 'descripcion', 'medida', 'unidad', 'existencia', 'cantidad_caja', 'cantidad_rb', 'proveedor', 'ubicacion', 'imagen']
class AlmacenDelete(DeleteView):
    model = Almacen
    fields = ['id', 'codigo', 'descripcion', 'medida', 'unidad', 'existencia', 'cantidad_caja', 'cantidad_rb', 'proveedor', 'ubicacion']

def AgregaraStock(request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST, request.FILES)
        if form.is_valid():
            Almacen = form.save()
            Almacen.save()
            return HttpResponseRedirect('/AlmacenList')
    else:
        form = AlmacenForm()
    template = loader.get_template('almacen/nuevo.html')
    context = {
        'form': form
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/AlmacenList/')

def AlmacenList(request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST, request.FILES)
        if form.is_valid():
            almacen = form.save()
            almacen.save()
            return HttpResponseRedirect('/AlmacenList')
    else:
        form = AlmacenForm()
    template = loader.get_template('almacen/almacen_list.html')
    queryset = Almacen.objects.all().order_by('id')
    context = {
        'queryset':queryset,
        'form':form

    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return render(request, "almacen/almacen_list.html",context)

def AlmacenDetail(request,pk):
    almacen = get_object_or_404(Almacen, pk=pk)
    template = loader.get_template('almacen/almacen_detail.html')
    context = {
        'almacen': almacen
        }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/AlmacenList/')
