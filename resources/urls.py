
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
]