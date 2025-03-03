from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
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

def edit_custodiam(request, pk):
    custodiam = get_object_or_404(Custodiam, id=pk)  # Usamos el campo `id` que es UUID
    positions = Position.objects.all()  

    if request.method == 'POST':
        # Obtener los datos del formulario
        custodiam.first_name = request.POST.get('first_name')
        custodiam.last_name = request.POST.get('last_name')
        custodiam.phone_number = request.POST.get('phone_number')
        custodiam.address = request.POST.get('address')
        custodiam.reference = request.POST.get('reference')
        custodiam.email = request.POST.get('email')

        # Asegurarse de que la posición esté correctamente asignada
        position_id = request.POST.get('position')
        if position_id:
            custodiam.position = get_object_or_404(Position, id=position_id)
        else:
            custodiam.position = None  # Si no se selecciona ninguna posición

        # Guardar el objeto
        try:
            custodiam.save()
            messages.success(request, "Custodio actualizado correctamente.")
            return redirect('home:custodiams_list')
        except Exception as e:
            messages.error(request, f"Error al guardar el custodio: {e}")

    return render(request, 'hierarchy/edit_custodian.html', {'custodiam': custodiam, 'positions': positions})

def delete_custodian(request, pk):
    custodiam = get_object_or_404(Custodiam, id=pk)
    
    if request.method == "POST":
        try:
            custodiam.status = False  # Cambiar el estado a inactivo
            custodiam.save()  # Guardar el objeto
            messages.success(request, "El custodio ha sido desactivado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al desactivar el custodio: {e}")
        
        return redirect('home:custodiams_list')  # Redirigir a la lista de custodios
    
    return render(request, 'hierarchy/delete_custodian.html', {'custodiam': custodiam})