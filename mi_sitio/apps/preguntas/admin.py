from django.contrib import admin

from .models import categoria, cargar_pregunta, respuesta_correcta, respuesta_incorrecta

class categoriaAdmin(admin.ModelAdmin):
  list_display = ["categoria","id"]
admin.site.register(categoria) #,categoriaAdmin)

class cargar_preguntaAdmin(admin.ModelAdmin):
    list_display = ["pregunta","id"]
admin.site.register(cargar_pregunta, cargar_preguntaAdmin)

admin.site.register(respuesta_correcta)
admin.site.register(respuesta_incorrecta)
