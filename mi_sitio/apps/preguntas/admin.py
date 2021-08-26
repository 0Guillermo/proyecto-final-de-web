from django.contrib import admin

from .models import cargar_pregunta, cargar_respuesta

admin.site.register(cargar_pregunta)
admin.site.register(cargar_respuesta)