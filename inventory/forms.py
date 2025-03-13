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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'tipo' in self.data:
            tipo = self.data.get('tipo')
            if tipo in dict(TipoMarca.OPCIONES).keys():
                self.fields['brand'].queryset = Brand.objects.filter(tipo=tipo)
        elif self.instance.pk:
            self.fields['brand'].queryset = Brand.objects.filter(tipo=self.instance.tipo)

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        brand = cleaned_data.get('brand')

        print(f"Tipo seleccionado en clean: {tipo}")  # Depuración
        print(f"Marca seleccionada en clean: {brand}")  # Depuración

        if brand and tipo:
            if brand.tipo != tipo:
                raise forms.ValidationError(
                    f"La marca '{brand.description}' no pertenece al tipo seleccionado '{dict(TipoMarca.OPCIONES).get(tipo)}'."
                )
        elif not tipo and brand:
            raise forms.ValidationError("Debes seleccionar un tipo antes de elegir una marca.")

        return cleaned_data

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