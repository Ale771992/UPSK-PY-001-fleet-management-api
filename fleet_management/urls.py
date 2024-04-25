"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Importa la función path del módulo django.urls, que se usa para definir URL en una app Django.
from django.urls import path, include
from fleet.views import list_taxis
from fleet.views import list_trajectories
# from drf_yasg.views import 
'''
Toca asociar la vista creada a una URL especifica
'''
# Define el prefijo base para todas las URLs de tu API
base_api_path = 'fleet-managment/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{base_api_path}api/taxis/', list_taxis, name='list_taxis'),
    path(f'{base_api_path}api/trajectories/<int:taxi_id>/', list_trajectories, name='list_trajectories')
]
'''
Cuando se accede a esta URL en el navegador, Django llamará a la función list_taxis definida. 
El parámetro name='list_taxis' proporciona un nombre único a esta URL, que puede ser utilizado para referirse a 
esta URL desde otras partes del código Django 
'''
