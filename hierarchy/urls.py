from django.urls import path
from . import views

app_name = 'hierarchy' 
urlpatterns = [
    path('add-floor/', views.add_floor, name='add_floor'),
    path('edit-floor/<uuid:pk>/', views.edit_floor, name='edit_floor'),
    path('delete-floor/<uuid:pk>/', views.delete_floor, name='delete_floor'),
    path('add-department/', views.add_department, name='add_department'),
    path('edit-department/<uuid:pk>/', views.edit_department, name='edit_department'),
    path('delete-department/<uuid:pk>/', views.delete_department, name='delete_department'),
    path('add-position/', views.add_position, name='add_position'),
    path('add-custodiam/', views.add_custodiam, name='add_custodiam'),
    path('edit-position/<uuid:pk>/', views.edit_position, name='edit_position'),
    path('delete-position/<uuid:pk>/', views.delete_position, name='delete_position'),
    path('edit-custodian/<uuid:pk>/', views.edit_custodiam, name='edit_custodian'),
    path('delete-custodian/<uuid:pk>/', views.delete_custodian, name='delete_custodian'),
    path('custodiam-details/', views.custodiam_details, name='custodiam_details'),
    
    
]

