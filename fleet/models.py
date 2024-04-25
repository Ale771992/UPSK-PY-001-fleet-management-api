# La clase models de Django, se utiliza para definir modelos de base de datos.
from django.db import models

# Create your models here.


class Taxis(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=20)

    class Meta:
        '''
        verbose_name_plural: Especifica el nombre plural amigable para el modelo en el panel de 
        administración de Django. Por ejemplo, en lugar de "taxis", se mostrará "Taxis" en el 
        panel de administración.
        '''
        verbose_name_plural = "taxis"

    def __str__(self):
        return self.plate


'''
__str__:
Este método define cómo se representa el objeto cuando se convierte a una cadena.
'''


class Trajectories(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    taxi = models.ForeignKey(Taxis, on_delete=models.CASCADE)
   

    '''
    El argumento on_delete=models.CASCADE indica que si un registro relacionado en taxis se elimina, 
    todas las instancias relacionadas en trajectories también se eliminarán.
    '''

    class Meta:
        verbose_name_plural = "trajectories"

    def __str__(self):
        return self.date.strftime('%Y-%m-%d %H:%M:%S')
