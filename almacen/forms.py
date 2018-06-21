# This Python file uses the following encoding: utf-8
from django import forms
from .models import Almacen
from django.forms import Textarea,TextInput,NumberInput,FileInput,Select
choicesunidad=(('','-------'),('metros','metros'),('pieza','pieza'))
choicesproveedor=(('','-------'),('LG','LG'),('Tubo Qualtek','Tubo Qualtek'),('Tubo Ecoline','Tubo Ecoline'),('Tubo W','Tubo W'),('Vidrios','Vidrios'),('Q-Ties','Q-Ties'),('Vidrios','Vidrios'),('Steren','Steren'),)
choicesubicacion=(('','-------'),('PB','PB'),('P1','P1'),('P2','P2'),('1E','1E'),('1B','1B'),('2B','2B'),('PB1','PB1'),('PB2','PB2'),('PB3','PB3'),('PB4','PB4'),('PB5','PB5'),('PB6','PB6'),('PBE','PBE'),('PBC','PBC'),('PBO','PBO'),)
class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = '__all__'
        labels = {
            'codigo': 'Código',
            'descripcion': 'Descripción',
            'medida' : 'Medida (mts/pza)',
            'unidad' : 'Unidad',
            'existencia' : 'Existencia',
            'cantidad_caja' : 'Cantidad (Caja)',
            'cantidad_rb' : 'Cantidad (Rollo/Bolsa)',
            'proveedor' : 'Proveedor',
            'ubicacion' : 'Ubicación',
            'imagen' : 'Miniatura',
            }
        widgets = { 'codigo': TextInput(attrs={
                                        'class':'form-control input-lg',
                                        'id': 'codigo',
                                        'name': 'codigo',
                                        'placeholder':'Código...'
                                        }),
                    'descripcion': TextInput(attrs={
                                                    'class':'form-control',
                                                    'id': 'descripcion',
                                                    'name': 'descripcion',
                                                    'placeholder':'Descripción...'
                                                    }),
                    'unidad': forms.Select(attrs={
                                                'id': 'unidad',
                                                'name': 'unidad',
                                                'class':'form-control',
                                                },
                                                choices=choicesunidad),
                    'medida': TextInput(attrs={
                                                    'class':'form-control',
                                                    'id': 'medida',
                                                    'name': 'medida',
                                                    'placeholder':'Medida...'
                                                    }),
                    'existencia': NumberInput(attrs={
                                                    'class':'form-control',
                                                    'id': 'unidad',
                                                    'name': 'unidad',
                                                    'placeholder':'Unidad...'
                                                    }),
                    'cantidad_caja': NumberInput(attrs={
                                                    'class':'form-control',
                                                    'id': 'cantidad_caja',
                                                    'name': 'cantidad_caja',
                                                    'placeholder':'0,000'
                                                    }),
                    'cantidad_rb': NumberInput(attrs={
                                                    'class':'form-control',
                                                    'id': 'cantidad_rb',
                                                    'name': 'cantidad_rb',
                                                    'placeholder':'0,000'
                                                    }),
                    'proveedor': forms.Select(attrs={
                                                'id': 'proveedor',
                                                'name': 'proveedor',
                                                'class':'form-control',
                                                },
                                                choices=choicesproveedor),
                    'ubicacion': forms.Select(attrs={
                                                'id': 'ubicacion',
                                                'name': 'ubicacion',
                                                'class':'form-control',
                                                },
                                                choices=choicesubicacion),
                    }
