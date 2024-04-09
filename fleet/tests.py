from django.test import TestCase, Client
from django.urls import reverse
import json
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
