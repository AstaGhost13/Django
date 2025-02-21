from django.urls import path
from .views import add_floor

urlpatterns = [
    path('add-floor/', add_floor, name='add_floor'),
]