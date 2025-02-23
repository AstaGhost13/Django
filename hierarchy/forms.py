from django import forms
from .models import Floor, Department

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['description', 'status']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['description', 'status', 'parent' , 'id_floor']

        