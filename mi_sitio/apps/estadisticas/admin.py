from django.contrib import admin
from .models import estadisticas

class EstadisticasAdmin(admin.ModelAdmin):
    list_display = ["id","participante","estado"]
admin.site.register(estadisticas,EstadisticasAdmin)


# Register your models here.
