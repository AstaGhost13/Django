
from django.urls import path
from . import views

app_name = 'resources'  # Define the application namespace
urlpatterns = [

    path('add-hardware/', views.add_hardware, name='add_hardware'),
    path('edit-hardware/<uuid:pk>/', views.edit_hardware, name='edit_hardware'),
    path('delete-hardware/<uuid:pk>/', views.delete_hardware, name='delete_hardware'),
]