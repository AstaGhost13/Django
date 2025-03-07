from django_select2.forms import Select2Widget
from django import forms
from .models import *

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['description', 'tipo']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripción de la marca',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control custom-select',
            }),
        }

class PrototypeForm(forms.ModelForm):
    class Meta:
        model = Prototype
        fields = ['description', 'tipo', 'brand']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del modelo',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control',
            }),
            'brand': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'description': 'Descripción',
            'tipo': 'Tipo de marca',
            'brand': 'Marca asociada',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar marcas según el tipo seleccionado
        if 'tipo' in self.data:
            try:
                tipo = self.data.get('tipo')
                self.fields['brand'].queryset = Brand.objects.filter(tipo=tipo)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # Si es una edición, filtrar marcas según el tipo del modelo
            self.fields['brand'].queryset = Brand.objects.filter(tipo=self.instance.tipo)




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['codigo', 'description', 'serie', 'prototype']
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código del producto',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del producto',
            }),
            'serie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Serie del producto',
            }),
            'prototype': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
        

class ProductAssignmentForm(forms.ModelForm):
    class Meta:
        model = ProductAssignment
        fields = ['product', 'custodiam']
        widgets = {
            'product': Select2Widget(attrs={
                'class': 'form-control form-control-alternative select2',
                'placeholder': 'Seleccione un producto'
            }),
            'custodiam': Select2Widget(attrs={
                'class': 'form-control form-control-alternative select2',
                'placeholder': 'Seleccione un custodio'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar productos activos
        self.fields['product'].queryset = Product.objects.filter(status=True)
        # Filtrar custodios activos
        self.fields['custodiam'].queryset = Custodiam.objects.filter(status=True)
        # Añadir clases adicionales a los campos
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-alternative'})