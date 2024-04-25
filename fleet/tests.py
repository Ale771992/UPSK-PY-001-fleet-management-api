from django.test import TestCase, Client
from django.urls import reverse
import json
from django.core.paginator import Paginator
from fleet.models import Taxis  # Importo el modelo

# Test para verificar que el endpoint de la API devuelve el codigo HTTP correcto.
'''
reverse es una función de django que se usa para obtener la URL asociada al patron con el 
nombre 'list_taxis'.
'''
class TestTaxisList(TestCase):
    def setUp(self):
        # Método setUp: creamos un cliente que usaremos para hacer solicitudes a nuestra aplicación.
        self.client = Client()

    def test_list_taxis(self):
        # Hacer una solicitud GET al endpoint
        response = self.client.get(reverse('list_taxis'))

        # Verificar que la respuesta tiene un codigo HTTP 200
        self.assertEqual(response.status_code, 200)

        # Verificar que el contenido es JSON
        self.assertEqual(response['Content-Type'], 'application/json')

        # Obtener los datos esperados de los taxis
        expected_data = [{
            'id': taxi.id,
            'placa': taxi.plate
        } for taxi in Taxis.objects.all()]

        # Obtener los datos reales de la respuesta
        '''responde.content es el contenido de la respuesta HTTP.
        json.loads() se usa para cargar una cadena JSON y covertirla en un 
        objeto Python.
        '''
        data = json.loads(response.content)

        # Verificar que los datos devueltos coinciden con los datos esperados
        self.assertEqual(data, expected_data)

#Tests unitarios (views)
class TestViewListTaxis(TestCase):
    def setUp(self):
        # Creo instancias ficticias de taxis para ser usadas en el test 
        Taxis.objects.create(id = 4578, plate = "JFUA-9384")
        Taxis.objects.create(id = 2730, plate = "WQRX-0977")
        Taxis.objects.create(id = 2237, plate = "JHJH-3444")
        Taxis.objects.create(id = 4431, plate = "CBNX-9667")
    def testView_taxis_pagination(self): 
        taxis = Taxis.objects.all()
        page_size = 2
        paginador = Paginator(taxis, page_size)
        # Verificar el numero de paginas
        self.assertEqual(paginador.num_pages, 2)

        # Verificar los taxis de la primera página
        first_taxis_page = paginador.page(1).object_list 
        self.assertEqual(len(first_taxis_page), page_size)

        # Verificar los datos especificos de la primera pagina 
        expected_plates_firstPage = ["JFUA-9384","WQRX-0977"]
        actual_plates = [taxi.plate for taxi in first_taxis_page]
        self.assertEqual(actual_plates, expected_plates_firstPage)