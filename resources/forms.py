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

class DisplayNameForm(forms.ModelForm):
    class Meta:
        model = DisplayName
        fields = ['name', 'product']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la máquina',
            }),
            'product': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

class DateOperationForm(forms.ModelForm):
    class Meta:
        model = DateOperation
        fields = ['product', 'date', 'running_time']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'running_time': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class IpAssignationForm(forms.ModelForm):
    class Meta:
        model = IpAssignation
        fields = ['product', 'ip']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control',
            }),
            'ip': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 192.168.1.1',
            }),
        }