from django.urls import path
from . import views

app_name = 'hierarchy' 
urlpatterns = [
    path('add-floor/', views.add_floor, name='add_floor'),
    path('add-department/', views.add_department, name='add_department'),
    path('add-position/', views.add_position, name='add_position'),
    path('add-custodiam/', views.add_custodiam, name='add_custodiam'),
    path('edit-custodian/<uuid:pk>/', views.edit_custodiam, name='edit_custodian'),
    path('delete-custodian/<uuid:pk>/', views.delete_custodian, name='delete_custodian'),
    path('custodiam-details/', views.custodiam_details, name='custodiam_details'),
    
]

