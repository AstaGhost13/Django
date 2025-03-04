
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

