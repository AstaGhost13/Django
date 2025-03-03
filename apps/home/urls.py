# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
app_name = 'home'
urlpatterns = [

    path('', views.index, name='home'),
    path('floors/', views.floors_list, name='floors_list'),
    path('departments/', views.departments_list, name='departments_list'),
    path('positions/', views.positions_list, name='positions_list'),
    path('custodiams/', views.custodiams_list, name='custodiams_list'),
    
    # Coloca la expresión regular al final para evitar conflictos
    re_path(r'^.*\.*', views.pages, name='pages'),

]
