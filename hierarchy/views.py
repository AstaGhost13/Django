import uuid
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
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

def edit_floor(request, pk):
    # Obtener el objeto Floor o devolver un error 404 si no existe
    floor = get_object_or_404(Floor, id=pk)  # Usamos el campo `id` que es UUID

    if request.method == 'POST':
        # Obtener los datos del formulario
        description = request.POST.get('description')
        status = request.POST.get('status') == 'true'  # Convertir a booleano

        # Validar los datos
        if not description:
            messages.error(request, "La descripción es obligatoria.")
        else:
            # Actualizar el objeto
            floor.description = description
            floor.status = status

            # Guardar el objeto
            try:
                floor.save()
                messages.success(request, "Piso actualizado correctamente.")
                return redirect('home:floors_list')  # Redirigir a la lista de pisos
            except Exception as e:
                messages.error(request, f"Error al guardar el piso: {e}")

    # Renderizar el formulario de edición
    return render(request, 'hierarchy/edit_floor.html', {'floor': floor})
def edit_position(request, pk):
    position = get_object_or_404(Position, id=pk)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.success(request, "Posición actualizada correctamente.")
            return redirect('home:positions_list')
        else:
            messages.error(request, "Hubo un error al actualizar la posición.")
    else:
        form = PositionForm(instance=position)

    return render(request, 'hierarchy/edit_position.html', {
        'form': form,
        'position': position,
    })
def delete_position(request, pk):
    position = get_object_or_404(Position, id=pk)
    
    if request.method == "POST":
        try:
            position.status = False  # Cambiar el estado a inactivo
            position.save()  # Guardar el objeto
            messages.success(request, "La posición ha sido desactivada correctamente.")
        except Exception as e:
            messages.error(request, f"Error al desactivar la posición: {e}")
        
        return redirect('home:positions_list')  # Redirigir a la lista de posiciones
    
    return render(request, 'home/delete_position.html', {'position': position})

def delete_floor(request, pk):
    # Obtener el objeto Floor o devolver un error 404 si no existe
    floor = get_object_or_404(Floor, id=pk)  # Usamos el campo `id` que es UUID

    if request.method == 'POST':
        try:
            # Cambiar el estado del piso a inactivo (soft delete)
            floor.status = False
            floor.save()
            messages.success(request, "Piso desactivado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al desactivar el piso: {e}")

        return redirect('home:floors_list')  # Redirigir a la lista de pisos

    # Si no es una solicitud POST, redirigir a la lista de pisos
    return redirect('home:floors_list')

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
def edit_department(request, pk):
    department = get_object_or_404(Department, id=pk)
    floors = Floor.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        print("ID de piso recibido:", request.POST.get('id_floor'))  # Depuración
        print("ID de departamento padre recibido:", request.POST.get('parent'))  # Depuración
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, "Departamento actualizado correctamente.")
            return redirect('home:departments_list')
        else:
            messages.error(request, "Hubo un error al actualizar el departamento.")
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'hierarchy/edit_department.html', {
        'form': form,
        'department': department,
        'floors': floors,
        'departments': departments,
    })
    
    
def delete_department(request, pk):
    # Obtener el departamento a desactivar
    department = get_object_or_404(Department, id=pk)
    
    if request.method == "POST":
        try:
            department.status = False  # Cambiar el estado a inactivo
            department.save()  # Guardar el objeto
            messages.success(request, "El departamento ha sido desactivado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al desactivar el departamento: {e}")
        
        return redirect('home:departments_list')  # Redirigir a la lista de departamentos
    
    return render(request, 'hierarchy/delete_department.html', {'department': department})
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

def custodiam_details(request):
    custodiam_id = request.GET.get('custodiam_id')
    if custodiam_id:
        try:
            custodiam = Custodiam.objects.get(pk=custodiam_id)

            # Obtener la descripción de la posición, departamento y piso
            position_name = custodiam.position.description if custodiam.position else "No Position"
            department_name = custodiam.position.department.description if custodiam.position and custodiam.position.department else "No Department"
            floor_name = custodiam.position.department.id_floor.description if custodiam.position and custodiam.position.department and custodiam.position.department.id_floor else "No Floor"

            # Formatear la respuesta con la información solicitada
            response_data = {
                'name': f"{custodiam.first_name} {custodiam.last_name}",
                'position': position_name,
                'department': department_name,
                'floor': floor_name,  # Añadir la descripción del piso
                'phone': custodiam.phone_number,
                'address': custodiam.address,
            }

            return JsonResponse(response_data)
        except Custodiam.DoesNotExist:
            return JsonResponse({'error': 'Custodio no encontrado'}, status=404)
    return JsonResponse({'error': 'ID de custodio no proporcionado'}, status=400)