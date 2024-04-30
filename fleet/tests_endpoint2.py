from django.test import TestCase, Client
from fleet.models import Trajectories, Taxis
from django.utils.timezone import make_aware
from django.urls import reverse
import json
'''
Es necesario importar el modelo para acceder a la clase del modelo y usar el metodo create
'''
from datetime import datetime
from django.core.paginator import Paginator

# Tests unitarios 
class TestViewListTrajectories(TestCase):
    def setUp(self):
        #Crear instancias ficticias de taxis 

        taxi1 = Taxis.objects.create(id = 4578, plate = "JFUA-9384")
        taxi2 = Taxis.objects.create(id = 2730, plate = "WQRX-0977")
        taxi3 = Taxis.objects.create(id = 2237, plate = "JHJH-3444")
        taxi4 = Taxis.objects.create(id = 4431, plate = "CBNX-9667")

        #Crear instancias ficticias de trayectorias para usarlas en el test

        #Taxi 1
        #make_aware es una funcion que se usa para convertir un objeto datetime en un datetime pero con zona horaria 
        date_time_taxi1 = make_aware(datetime(2024, 4, 29, 10, 30, 0))
        Trajectories.objects.create(latitude = 123.4567, longitude = 12.3456, date = date_time_taxi1, taxi = taxi1)
        #Taxi 2
        date_time_taxi2 = make_aware(datetime(2024, 4, 28, 12, 35, 9 ))
        Trajectories.objects.create(latitude = 987.6543, longitude = 76.5432, date = date_time_taxi2, taxi = taxi2)
        #Taxi 3 
        date_time_taxi3 = make_aware(datetime(2024, 4, 27, 19, 44, 23))
        Trajectories.objects.create(latitude = 567.0987, longitude = 45.1203, date = date_time_taxi3, taxi = taxi3)
        #Taxi 4
        date_time_taxi4 = make_aware(datetime(2024, 4, 26, 11, 22, 22))
        Trajectories.objects.create(latitude = 539.0586, longitude = 33.9648, date = date_time_taxi4, taxi = taxi4)

        # Test para la paginación 
    def test_trajectories_pagination(self):
        trajectories = Trajectories.objects.all()
        page_size = 2
        paginador = Paginator(trajectories, page_size)
        

        self.assertEqual(paginador.num_pages, 2)

# Tests end2end

class TestE2eTrajectories(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_trajectories(self):
        taxi_id = 4578
        response = self.client.get(reverse('list_trajectories', kwargs={'taxi_id': taxi_id}))

        self.assertEqual(response.status_code, 200)

        #Comprobar obtener el tipo de dato correcto en la respuesta 

        expected_data = [{
            'latitud': taxi.latitude,
            'longitud': taxi.longuitude,
            'fecha': taxi.date
        } for taxi in Taxis.objects.all()]

        data = json.loads(response.content)
        self.assertEqual(data, expected_data)


