from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from inventory.enums.tipo_marca import TipoMarca
from inventory.forms import *
from inventory.models import *

# Create your views here.

def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marca agregada correctamente.")
            return redirect('inventory:add_brand')  # Redirige después de guardar
        else:
            messages.error(request, "Hubo un error al agregar la marca.")
    else:
        form = BrandForm()

    return render(request, 'inventory/add_brand.html', {'form': form})


def edit_brand(request, pk):
    brand = get_object_or_404(Brand, id=pk)  # Obtener la marca por su ID (UUID)

    if request.method == 'POST':
        # Obtener los datos del formulario
        brand.description = request.POST.get('description')
        brand.tipo = request.POST.get('tipo')

        # Guardar el objeto
        try:
            brand.save()  # Guardar la marca
            messages.success(request, "Marca actualizada correctamente.")
            return redirect('home:brands_list')  # Redirigir a la lista de marcas
        except Exception as e:
            messages.error(request, f"Error al guardar la marca: {e}")

    # Pasar las opciones de TipoMarca a la plantilla
    tipo_opciones = TipoMarca.OPCIONES
    return render(request, 'inventory/edit_brand.html', {'brand': brand, 'tipo_opciones': tipo_opciones})



def delete_brand(request, pk):
    brand = get_object_or_404(Brand, id=pk)  # Obtener la marca por su ID (UUID)
    
    if request.method == "POST":
        try:
            brand.status = False  # Cambiar el estado a inactivo
            brand.save()  # Guardar el objeto
            messages.success(request, "La marca ha sido desactivada correctamente.")
        except Exception as e:
            messages.error(request, f"Error al desactivar la marca: {e}")
        
        return redirect('home:brands_list')  # Redirigir a la lista de marcas
    
    return render(request, 'inventory/delete_brand.html', {'brand': brand})

