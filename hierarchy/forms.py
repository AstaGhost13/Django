from django import forms
from .models import Floor

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['description', 'status']
        widgets = {
            'status': forms.Select(choices=[(True, 'Activo'), (False, 'Inactivo')]),
        }