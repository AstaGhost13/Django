
from django.urls import path
from . import views


app_name = 'inventory' 
urlpatterns = [
    #para marcas
    path('add-brand/', views.add_brand, name='add_brand'),
    path('edit-brand/<uuid:pk>/', views.edit_brand, name='edit_brand'),
    path('delete-brand/<uuid:pk>/', views.delete_brand, name='delete_brand'),
    #para modelos
    path('add-prototype/', views.add_prototype, name='add_prototype'),
    path('edit-prototype/<uuid:pk>/', views.edit_prototype, name='edit_prototype'),
    path('delete-prototype/<uuid:pk>/', views.delete_prototype, name='delete_prototype'),

    #para productos
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<uuid:pk>/', views.edit_product, name='edit_product'),
    path('delete-product/<uuid:pk>/', views.delete_product, name='delete_product'),
    path('product-details/', views.product_details, name='product_details'),

     #para asignaciones
    path('add-productAssignment/', views.add_productAssignment, name='add_productAssignment'),
    path('edit-productAssignment/<uuid:pk>/', views.edit_productAssignment, name='edit_productAssignment'),
    path('delete-productAssignment/<uuid:pk>/', views.delete_productAssignment, name='delete_productAssignment'),
    
]
