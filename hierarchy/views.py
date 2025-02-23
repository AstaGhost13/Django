from django.contrib import messages
from django.shortcuts import render, redirect
from hierarchy.forms import DepartmentForm, FloorForm

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