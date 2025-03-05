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

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['version', 'edition', 'installation_date', 'licenses', 'product']
        widgets = {
            'version': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Versión del software',
            }),
            'edition': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edición del software',
            }),
            'installation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'licenses': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'product': forms.Select(attrs={
                'class': 'form-control',
            }),
        }