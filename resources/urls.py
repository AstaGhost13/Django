
from django.urls import path
from . import views

app_name = 'resources'  # Define the application namespace
urlpatterns = [

    path('add-hardware/', views.add_hardware, name='add_hardware'),
    path('edit-hardware/<uuid:pk>/', views.edit_hardware, name='edit_hardware'),
    path('delete-hardware/<uuid:pk>/', views.delete_hardware, name='delete_hardware'),

    #para software
    path('add-software/', views.add_software, name='add_software'),
    path('edit-software/<uuid:pk>/', views.edit_software, name='edit_software'),
    path('delete-software/<uuid:pk>/', views.delete_software, name='delete_software'),

    #para nombre maquina
    path('add-displayName/', views.add_displayName, name='add_displayName'),
    path('edit-displayName/<uuid:pk>/', views.edit_displayName, name='edit_displayName'),
    path('delete-displayName/<uuid:pk>/', views.delete_displayName, name='delete_displayName'),

    #para dataOperation
    path('add-dataOperation/', views.add_dataOperation, name='add_dataOperation'),
    path('edit-dataOperation/<uuid:pk>/', views.edit_dataOperation, name='edit_dataOperation'),
    path('delete-dataOperation/<uuid:pk>/', views.delete_dataOperation, name='delete_dataOperation'),

    #para ip 
    path('add-ipAssignation/', views.add_ipAssignation, name='add_ipAssignation'),
    path('edit-ipAssignation/<uuid:pk>/', views.edit_ipAssignation, name='edit_ipAssignation'),
    path('delete-ipAssignation/<uuid:pk>/', views.delete_ipAssignation, name='delete_ipAssignation'),
]