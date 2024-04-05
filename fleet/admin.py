from django.contrib import admin

# Register your models here.
from fleet.models import Taxis, Trajectories

admin.site.register(Taxis)
admin.site.register(Trajectories)
