from django import forms
from .models import Custodiam, Floor, Department ,Position

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ['description', 'status']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['description', 'status', 'parent' , 'id_floor']

    
class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['description', 'status', 'department']


class CustodiamForm(forms.ModelForm):
    class Meta:
        model = Custodiam
        fields = ['status','first_name', 'last_name', 'phone_number', 'address', 'reference', 'email', 'position']