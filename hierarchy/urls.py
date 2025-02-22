from django.urls import path
from . import views

app_name = 'hierarchy' 
urlpatterns = [
    path('add-floor/', views.add_floor, name='add_floor'),
]