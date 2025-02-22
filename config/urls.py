"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hierarchy/', include('hierarchy.urls')),  # Incluye las URLs de 'hierarchy'
    path("", include("apps.authentication.urls")),  # Rutas de autenticación
    path('', include("apps.home.urls")),  # Rutas de home
]