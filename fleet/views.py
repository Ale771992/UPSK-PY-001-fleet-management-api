from django.shortcuts import render
# El paginador ayuda a gestionar la respuesta
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.http import JsonResponse
from .models import Taxis
# Create your views here.
'''
En Django las vistas son funciones que reciben una solicitud web y devuelven una respuesta.
Estas vistas acceden a la base de datos para recuperar la información, procesarla y devolverla.
La vista es responsable de procesar la solicitud HTTP y devolver una respuesta. 
'''

def list_taxis(request):
    all_taxis = Taxis.objects.all() # Realiza una consulta a la base de datos para obtener todos los objetos de modelo de taxis
# Numero de elementos por pagina
    page_size = 10

    paginator = Paginator(all_taxis, page_size)

    page_number = request.GET.get('page')
    try:
        taxis_page = paginator.page(page_number)
    except  PageNotAnInteger:
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