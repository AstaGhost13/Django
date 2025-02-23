from django.contrib import messages
from django.shortcuts import render, redirect
from hierarchy.forms import *

def add_floor(request):
    if request.method == 'POST':
        form = FloorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Piso agregado correctamente.")
            return redirect('hierarchy:add_floor')  # Redirige después de guardar
        else:
            messages.error(request, "Hubo un error al agregar el piso.")
    else:
        form = FloorForm()

    return render(request, 'hierarchy/add_floor.html', {'form': form})


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Departamento agregado correctamente.")
            return redirect('hierarchy:add_department')  # Redirige después de guardar
        else:
            messages.error(request, "Hubo un error al agregar el departamento.")
    else:
        form = DepartmentForm()

    return render(request, 'hierarchy/add_department.html', {'form': form})


def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cargo agregado correctamente.")
            return redirect('hierarchy:add_position')  # Redirige después de guardar
        else:
            messages.error(request, "Hubo un error al agregar el cargo.")
    else:
        form = PositionForm()

    return render(request, 'hierarchy/add_position.html', {'form': form})


def add_custodiam(request):
    if request.method == 'POST':
        form = CustodiamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Custodio agregado correctamente.")
            return redirect('hierarchy:add_custodiam')  # Redirige después de guardar
        else:
            messages.error(request, "Hubo un error al agregar el custodio.")
    else:
        form = CustodiamForm()

    return render(request, 'hierarchy/add_custodiam.html', {'form': form})



