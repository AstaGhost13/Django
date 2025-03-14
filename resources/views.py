from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def add_hardware(request):
    if request.method == 'POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hardware agregado correctamente.")
            return redirect('home:hardwares_list')
        else:
            messages.error(request, "Hubo un error al agregar el hardware.")
    else:
        form = HardwareForm()
    return render(request, 'resources/add_hardware.html', {'form': form})


def edit_hardware(request, pk):
    hardware = get_object_or_404(Hardware, id=pk)
    if request.method == 'POST':
        form = HardwareForm(request.POST, instance=hardware)
        if form.is_valid():
            form.save()
            messages.success(request, "Hardware actualizado correctamente.")
            return redirect('home:hardwares_list')
        else:
            messages.error(request, "Hubo un error al actualizar el hardware.")
    else:
        form = HardwareForm(instance=hardware)
    return render(request, 'resources/edit_hardware.html', {'form': form, 'hardware': hardware})


def delete_hardware(request, pk):
    hardware = get_object_or_404(Hardware, id=pk)
    if request.method == 'POST':
        hardware.status = False
        hardware.save()
        messages.success(request, "Hardware desactivado correctamente.")
        return redirect('home:hardwares_list')
    return render(request, 'resources/delete_hardware.html', {'hardware': hardware})




def add_software(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Software agregado correctamente.")
            return redirect('home:softwares_list')
        else:
            messages.error(request, "Hubo un error al agregar el software.")
    else:
        form = SoftwareForm()
    return render(request, 'resources/add_software.html', {'form': form})


def edit_software(request, pk):
    software = get_object_or_404(Software, id=pk)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            form.save()
            messages.success(request, "Software actualizado correctamente.")
            return redirect('home:softwares_list')
        else:
            messages.error(request, "Hubo un error al actualizar el software.")
    else:
        form = SoftwareForm(instance=software)
    return render(request, 'resources/edit_software.html', {'form': form, 'software': software})


def delete_software(request, pk):
    software = get_object_or_404(Software, id=pk)
    if request.method == 'POST':
        software.status = False
        software.save()
        messages.success(request, "Software desactivado correctamente.")
        return redirect('home:softwares_list')
    return render(request, 'resources/delete_software.html', {'software': software})


def add_displayName(request):
    if request.method == 'POST':
        form = DisplayNameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nombre de máquina agregado correctamente.")
            return redirect('home:displayNames_list')
        else:
            messages.error(request, "Hubo un error al agregar el nombre de máquina.")
    else:
            form = DisplayNameForm()
    return render(request, 'resources/add_displayName.html', {'form': form})
    


def edit_displayName(request, pk):
    displayName = get_object_or_404(DisplayName, id=pk)
    if request.method == 'POST':
        form = DisplayNameForm(request.POST, instance=displayName)
        if form.is_valid():
            form.save()
            messages.success(request, "Nombre de máquina actualizado correctamente.")
            return redirect('home:displayNames_list')
        else:
            messages.error(request, "Hubo un error al actualizar el nombre de máquina.")
    else:
        form = DisplayNameForm(instance=displayName)
    return render(request, 'resources/edit_displayName.html', {'form': form, 'displayName': displayName})


def delete_displayName(request, pk):
    displayName = get_object_or_404(DisplayName, id=pk) 
    if request.method == 'POST':
        displayName.status = False
        displayName.save()
        messages.success(request, "Nombre de máquina desactivado correctamente.")
        return redirect('home:displayNames_list')
    return render(request, 'resources/delete_displayName.html', {'displayName': displayName})



def add_dataOperation(request):
    if request.method == 'POST':
        form = DateOperationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Operación de datos agregada correctamente.")
            return redirect('home:dateOperations_list')
        else:
            messages.error(request, "Hubo un error al agregar la operación de datos.")
    else:
        form = DateOperationForm()
    return render(request, 'resources/add_dateOperation.html', {'form': form})


def edit_dataOperation(request, pk):
    dataOperation = get_object_or_404(DateOperation, id=pk)
    if request.method == 'POST':
        form = DateOperationForm(request.POST, instance=dataOperation)
        if form.is_valid():
            form.save()
            messages.success(request, "Operación de datos actualizada correctamente.")
            return redirect('home:dateOperations_list')
        else:
            messages.error(request, "Hubo un error al actualizar la operación de datos.")
    else:
        form = DateOperationForm(instance=dataOperation)
    return render(request, 'resources/edit_dateOperation.html', {'form': form, 'dataOperation': dataOperation})


def delete_dataOperation(request, pk):
    dataOperation = get_object_or_404(DateOperation, id=pk)
    if request.method == 'POST':
        dataOperation.status = False
        dataOperation.save()
        messages.success(request, "Operación de datos desactivada correctamente.")
        return redirect('home:dateOperations_list')
    return render(request, 'resources/delete_dateOperation.html', {'dataOperation': dataOperation})



def add_ipAssignation(request):
    if request.method == 'POST':
        form = IpAssignationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignación de IP agregada correctamente.")
            return redirect('home:ipAssignations_list')
        else:
            messages.error(request, "Hubo un error al agregar la asignación de IP.")
    else:
        form = IpAssignationForm()
    return render(request, 'resources/add_ipAssignation.html', {'form': form})

def edit_ipAssignation(request, pk):
    ipAssignation = get_object_or_404(IpAssignation, id=pk)
    if request.method == 'POST':
        form = IpAssignationForm(request.POST, instance=ipAssignation)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignación de IP actualizada correctamente.")
            return redirect('home:ipAssignations_list')
        else:
            messages.error(request, "Hubo un error al actualizar la asignación de IP.")
    else:
        form = IpAssignationForm(instance=ipAssignation)
    return render(request, 'resources/edit_ipAssignation.html', {'form': form, 'ipAssignation': ipAssignation})

def delete_ipAssignation(request, pk):
    ipAssignation = get_object_or_404(IpAssignation, id=pk)
    if request.method == 'POST':
        ipAssignation.status = False
        ipAssignation.save()
        messages.success(request, "Asignación de IP desactivada correctamente.")
        return redirect('home:ipAssignations_list')
    return render(request, 'resources/delete_ipAssignation.html', {'ipAssignation': ipAssignation})