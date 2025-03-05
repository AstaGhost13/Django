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