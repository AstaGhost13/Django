from django.shortcuts import render, redirect
from .models import Floor

def add_floor(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        description = request.POST.get('description')
        status = request.POST.get('status') == 'True'  # Convierte el valor a booleano

        # Crea un nuevo objeto Floor y guárdalo en la base de datos
        Floor.objects.create(
            description=description,
            status=status
        )
        return redirect('#')  # Redirige a la lista de pisos (o a donde desees)
    
    # Si no es una solicitud POST, simplemente renderiza el formulario
    return render(request, 'home/icons.html')