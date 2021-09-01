from django.contrib import admin
from .models import estadisticas

class EstadisticasAdmin(admin.ModelAdmin):
    list_display = ["id","participante","feche_ingreso","fecha_salida","Puntuacion","estado","nivel"]
admin.site.register(estadisticas,EstadisticasAdmin)


# Register your models here.
