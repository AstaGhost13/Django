from django.urls import path
from . import views

app_name = 'hierarchy' 
urlpatterns = [
    path('add-floor/', views.add_floor, name='add_floor'),
    path('add-department/', views.add_department, name='add_department'),
]