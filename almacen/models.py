# -*- coding: utf-8 -*-
from django.db import models
import random
import os

# Create your models here.
def get_filename_ext(filepath):
    nombre_base = os.path.basename(filepath)
    nombre, ext = os.path.splitext(nombre_base)
    return nombre, ext


def upload_image_path(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "productos/modelo/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

class Almacen(models.Model):
    codigo = models.CharField(max_length=50,blank=False,null=False)
    descripcion = models.CharField(max_length=50,blank=False,null=False)
    medida = models.CharField(max_length=50,blank=False,null=False)
    unidad = models.CharField(max_length=50,blank=False,null=False)
    existencia = models.PositiveIntegerField(default=0)
    cantidad_caja = models.PositiveIntegerField(default=0)
    cantidad_rb = models.PositiveIntegerField(default=0)
    proveedor = models.CharField(max_length=50,blank=False,null=True)
    ubicacion = models.CharField(max_length=50,blank=False,null=True)
    imagen = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    def __str__(self):
        return self.codigo
