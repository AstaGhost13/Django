# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from pyexpat.errors import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from hierarchy.forms import *
from hierarchy.models import *


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
    departments = Department.objects.all()  # Obtener todos los departamentos
    return render(request, 'home/departments_list.html', {'departments': departments})

def positions_list(request):
    positions = Position.objects.all()  # Obtener todos los departamentos
    return render(request, 'home/positions_list.html', {'positions': positions})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def custodiams_list(request):
    custodiams_list = Custodiam.objects.all().order_by('last_name')  # Ordenar por apellido
    paginator = Paginator(custodiams_list, 4)  # Mostrar 10 custodios por página

    page_number = request.GET.get('page')  # Obtener el número de página de la URL
    try:
        custodiams = paginator.page(page_number)
    except PageNotAnInteger:
        custodiams = paginator.page(1)  # Si el parámetro no es un número, mostrar la primera página
    except EmptyPage:
        custodiams = paginator.page(paginator.num_pages)  # Si la página está fuera de rango, mostrar la última página

    return render(request, 'home/custodiams_list.html', {'custodiams': custodiams})