from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Taxis
from .models import Trajectories
from datetime import datetime

# from rest_framework.decorators import api_view
# Create your views here.
'''
En Django las vistas son funciones que reciben una solicitud web y devuelven una respuesta.
Estas vistas acceden a la base de datos para recuperar la información, procesarla y devolverla.
La vista es responsable de procesar la solicitud HTTP y devolver una respuesta. 
'''

# Obtener los taxis

def list_taxis(request):
    # Realiza una consulta a la base de datos para obtener todos los objetos de modelo de taxis
    all_taxis = Taxis.objects.all()
# Numero de elementos por pagina
    page_size = 10

    paginator = Paginator(all_taxis, page_size)

    page_number = request.GET.get('page')
    try:
        taxis_page = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el parametro de pagina no es un entero, mostrar la pagina 1
        taxis_page = paginator.page(1)
    except EmptyPage:
        # Si el numero de pagina esta fuera de rango mostrar la ultima pagina
        taxis_page = paginator.page(paginator.num_pages)
    taxis_data = [{
        'id': taxi.id,
        'placa': taxi.plate
    } for taxi in taxis_page]

    return JsonResponse(taxis_data, safe=False)

# Obtener las trayectorias de los taxis dado un ID y una fecha; la informacion de respuesta sera latitud, longitud y timestamp.

# 'request' es el objeto que representa la solicitud http
def list_trajectories(request, taxi_id):
    info_taxis = Trajectories.objects.filter(taxi_id=taxi_id)
# El filtro de date, filtra los resultados de info_taxis, para que se muestren los resultados que tienen la fecha especificada

    # Paginamos los resultados
    page_size = 10
    paginator = Paginator(info_taxis, page_size)
    page_number = request.GET.get('page')
    try:
        trajectories_page = paginator.page(page_number)
    except EmptyPage:
        trajectories_page = paginator.page(paginator.num_pages)
    # Crear lista de datos de las trayectorias (latitud, longitud, timestamp)
    trajectories_data = []
    for taxi in trajectories_page:
        trajectories_info = {
            'latitud': taxi.latitude,
            'longitud': taxi.longitude,
            'fecha': taxi.date, 
        }
        trajectories_data.append(trajectories_info)

    return JsonResponse(trajectories_data, safe=False)

'''
Django, para devolver una respuesta en JSON, solo considera datos seguros o safe a los diccionarios o listas.
Si mi respuesta, no es ni lista ni diccionario, le debo indicar a Django que no es safe, pero que aun asi 
redenrice mi respuesta.
'''
