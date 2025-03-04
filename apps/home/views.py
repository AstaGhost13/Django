# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from pyexpat.errors import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.db.models import Q
from django.urls import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from hierarchy.forms import *
from hierarchy.models import *
from inventory.models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    


def floors_list(request):
    floors = Floor.objects.all()  # Obtener todos los pisos
    return render(request, 'home/floors_list.html', {'floors': floors})

def departments_list(request):
    departments_list = Department.objects.all().order_by('id_floor')  
    paginator = Paginator(departments_list, 4) 

    page_number = request.GET.get('page')  
    try:
        departments = paginator.page(page_number)
    except PageNotAnInteger:
        departments = paginator.page(1)  
    except EmptyPage:
        departments = paginator.page(paginator.num_pages)  

    return render(request, 'home/departments_list.html', {'departments': departments})

def positions_list(request):
    positions_list = Position.objects.all().order_by('department') 
    paginator = Paginator(positions_list, 5)  

    page_number = request.GET.get('page')  
    try:
        positions = paginator.page(page_number)
    except PageNotAnInteger:
        positions = paginator.page(1)  
    except EmptyPage:
        positions = paginator.page(paginator.num_pages)  

    return render(request, 'home/positions_list.html', {'positions': positions})




def custodiams_list(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    sort_field = request.GET.get('sort', 'last_name')  # Campo por defecto para ordenar
    sort_order = request.GET.get('order', 'asc')  # Orden por defecto (ascendente)

    # Obtener todos los custodios activos
    custodiams_list = Custodiam.objects.filter(status="True")

    # Filtrar por búsqueda
    if query:
        custodiams_list = custodiams_list.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )

    # Ordenar los resultados
    if sort_order == 'desc':
        sort_field = f'-{sort_field}'  # Agregar el prefijo '-' para orden descendente
    custodiams_list = custodiams_list.order_by(sort_field)

    # Paginación
    paginator = Paginator(custodiams_list, 4)  # Mostrar 4 custodios por página
    page_number = request.GET.get('page')

    try:
        custodiams = paginator.page(page_number)
    except PageNotAnInteger:
        custodiams = paginator.page(1)  # Página por defecto si no es un número entero
    except EmptyPage:
        custodiams = paginator.page(paginator.num_pages)  # Última página si la página solicitada está vacía

    return render(request, 'home/custodiams_list.html', {
        'custodiams': custodiams,
        'query': query,
        'sort_field': sort_field.lstrip('-'),  # Eliminar el prefijo '-' para el template
        'sort_order': sort_order,
    })


#para inventario

def brands_list(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    

    # Filtrar marcas activas y ordenar por descripción
    brands_list = Brand.objects.filter(status=True).order_by('description')
    
    # Si hay un término de búsqueda, filtrar por descripción
    if query:
        brands_list = brands_list.filter(description__icontains=query)

    # Paginación: 10 marcas por página
    paginator = Paginator(brands_list, 4)  
    page_number = request.GET.get('page')  

    try:
        brands = paginator.page(page_number)
    except PageNotAnInteger:
        brands = paginator.page(1)  # Página por defecto si no es un número entero
    except EmptyPage:
        brands = paginator.page(paginator.num_pages)  # Última página si la página solicitada está vacía

    return render(request, 'home/brands_list.html', {'brands': brands, 'query': query})


def prototypes_list(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda

    # Filtrar modelos activos y ordenar por descripción
    prototypes_list = Prototype.objects.filter(status=True).order_by('description')
    
    # Si hay un término de búsqueda, filtrar por descripción
    if query:
        prototypes_list = prototypes_list.filter(description__icontains=query)

    # Paginación: 10 modelos por página
    paginator = Paginator(prototypes_list, 3)  
    page_number = request.GET.get('page')  

    try:
        prototypes = paginator.page(page_number)
    except PageNotAnInteger:
        prototypes = paginator.page(1)  # Página por defecto si no es un número entero
    except EmptyPage:
        prototypes = paginator.page(paginator.num_pages)  # Última página si la página solicitada está vacía

    return render(request, 'home/prototypes_list.html', {'prototypes': prototypes, 'query': query})



def products_list(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(status=True).order_by('description')
    
    if query:
        products = products.filter(description__icontains=query)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')


    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)  # Página por defecto si no es un número entero
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # Última página si la página solicitada está vacía

    return render(request, 'home/products_list.html', {'products': products, 'query': query})



def productAssignments_list(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    sort_field = request.GET.get('sort', 'product__description')  # Campo de ordenación
    sort_order = request.GET.get('order', 'asc')  # Orden (asc o desc)

    # Filtrar asignaciones activas
    asignaciones_list = ProductAssignment.objects.filter(status=True)

    # Si hay un término de búsqueda, filtrar por descripción del producto
    if query:
        asignaciones_list = asignaciones_list.filter(product__description__icontains=query)

    # Ordenar las asignaciones
    if sort_order == 'asc':
        asignaciones_list = asignaciones_list.order_by(sort_field)
    else:
        asignaciones_list = asignaciones_list.order_by(f'-{sort_field}')

    # Paginación: 10 asignaciones por página
    paginator = Paginator(asignaciones_list, 4)  
    page_number = request.GET.get('page')  

    try:
        asignaciones = paginator.page(page_number)
    except PageNotAnInteger:
        asignaciones = paginator.page(1)  # Página por defecto si no es un número entero
    except EmptyPage:
        asignaciones = paginator.page(paginator.num_pages)  # Última página si la página solicitada está vacía

    return render(request, 'home/productAssignments_list.html', {
        'asignaciones': asignaciones,
        'query': query,
        'sort_field': sort_field,
        'sort_order': sort_order,
    })


