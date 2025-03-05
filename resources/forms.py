from django import forms
from .models import *

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['processor', 'memory', 'tamanio', 'tipo_disco', 'product']
        widgets = {
            'processor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Procesador del hardware',
            }),
            'memory': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Memoria RAM del hardware',
            }),
            'tamanio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tamaño del disco',
            }),
            'tipo_disco': forms.Select(attrs={
                'class': 'form-control',
            }),
            'product': forms.Select(attrs={
                'class': 'form-control',
            }),
        }