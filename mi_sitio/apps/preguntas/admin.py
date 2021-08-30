from django.contrib import admin

from .models import categoria, cargar_pregunta, respuesta_correcta, respuesta_incorrecta

class categoriaAdmin(admin.ModelAdmin):
  list_display = ["categoria_name","id"]
admin.site.register(categoria ,categoriaAdmin)

class cargar_preguntaAdmin(admin.ModelAdmin):
    list_display = ["pregunta","id"]
admin.site.register(cargar_pregunta, cargar_preguntaAdmin)

class respuesta_correctaAdmin(admin.ModelAdmin):
    list_display = ["respuesta_correcta","id"]
admin.site.register(respuesta_correcta,respuesta_correctaAdmin)

class respuesta_incorrectaAdmin(admin.ModelAdmin):
    list_display = ["respuesta_incorrecta","id"]
admin.site.register(respuesta_incorrecta,respuesta_incorrectaAdmin)
