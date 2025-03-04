
from django.urls import path
from . import views


app_name = 'inventory' 
urlpatterns = [
    #para marcas
    path('add-brand/', views.add_brand, name='add_brand'),
    path('edit-brand/<uuid:pk>/', views.edit_brand, name='edit_brand'),
    path('delete-brand/<uuid:pk>/', views.delete_brand, name='delete_brand'),
    #para modelos
    #path('add-prototype/', views.add_prototype, name='add_prototype'),
    #path('edit-prototype/<uuid:pk>/', views.edit_prototype, name='edit_prototype'),
    #path('delete-prototype/<uuid:pk>/', views.delete_prototype, name='delete_prototype'),
]
