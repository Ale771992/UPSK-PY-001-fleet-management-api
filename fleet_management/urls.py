"""
URL configuration for fleet_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# Importa la función path del módulo django.urls, que se usa para definir URL en una app Django.
from django.urls import path
from fleet.views import list_taxis
'''
Toca asociar la vista creada a una URL especifica
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/taxis/', list_taxis, name='list_taxis'),
]
'''
Cuando se accede a esta URL en el navegador, Django llamará a la función list_taxis definida. 
El parámetro name='list_taxis' proporciona un nombre único a esta URL, que puede ser utilizado para referirse a 
esta URL desde otras partes del código Django 
'''
