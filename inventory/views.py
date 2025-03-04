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



def add_prototype(request):
    if request.method == 'POST':
        form = PrototypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Modelo agregado correctamente.")
            return redirect('inventory:add_prototype')
        else:
            messages.error(request, "Hubo un error al agregar el modelo.")
    else:
        form = PrototypeForm()
    return render(request, 'inventory/add_prototype.html', {'form': form})



def edit_prototype(request, pk):
    prototype = get_object_or_404(Prototype, id=pk)

    if request.method == 'POST':
        form = PrototypeForm(request.POST, instance=prototype)
        if form.is_valid():
            form.save()
            messages.success(request, "Modelo actualizado correctamente.")
            return redirect('home:prototypes_list')
        else:
            messages.error(request, "Hubo un error al actualizar el modelo.")
    else:
        form = PrototypeForm(instance=prototype)

    return render(request, 'inventory/edit_prototype.html', {
        'form': form,
        'prototype': prototype,
    })




def delete_prototype(request, pk):
    prototype = get_object_or_404(Prototype, id=pk)
    if request.method == 'POST':
        prototype.status = False
        prototype.save()
        messages.success(request, "Modelo desactivado correctamente.")
        return redirect('home:prototypes_list')
    return render(request, 'inventory/delete_prototype.html', {'prototype': prototype})




def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto agregado correctamente.")
            return redirect('inventory:add_product')
        else:
            messages.error(request, "Hubo un error al agregar el producto.")
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})



def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado correctamente.")
            return redirect('home:products_list')
        else:
            messages.error(request, "Hubo un error al actualizar el producto.")
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit_product.html', {'form': form, 'product': product})


def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product.status = False
        product.save()
        messages.success(request, "Producto desactivado correctamente.")
        return redirect('home:products_list')
    return render(request, 'inventory/delete_product.html', {'product': product})




def add_productAssignment(request):
    if request.method == 'POST':
        form = ProductAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignación agregada correctamente.")
            return redirect('home:productAssignments_list')
        else:
            messages.error(request, "Hubo un error al agregar la asignación.")
    else:
        form = ProductAssignmentForm()
    return render(request, 'inventory/add_productAssignment.html', {'form': form})


def edit_productAssignment(request, pk):
    asignacion = get_object_or_404(ProductAssignment, id=pk)
    if request.method == 'POST':
        form = ProductAssignmentForm(request.POST, instance=asignacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignación actualizada correctamente.")
            return redirect('home:productAssignments_list')
        else:
            messages.error(request, "Hubo un error al actualizar la asignación.")
    else:
        form = ProductAssignmentForm(instance=asignacion)
    return render(request, 'inventory/edit_productAssignment.html', {'form': form, 'asignacion': asignacion})


def delete_productAssignment(request, pk):
    asignacion = get_object_or_404(ProductAssignment, id=pk)
    if request.method == 'POST':
        asignacion.status = False
        asignacion.save()
        messages.success(request, "Asignación desactivada correctamente.")
        return redirect('home:productAssignments_list')
    return render(request, 'inventory/delete_productAssignment.html', {'asignacion': asignacion})