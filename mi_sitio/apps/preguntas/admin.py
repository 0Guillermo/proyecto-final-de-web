from django.contrib import admin

from .models import categoria, cargar_pregunta, respuesta_correcta, respuesta_incorrecta

class categoriaAdmin(admin.ModelAdmin):
  list_display = ["id","tipo"]
admin.site.register(categoria ,categoriaAdmin)

class respuesta_correctaAdmin(admin.ModelAdmin):
    list_display = ["id","correcta"]
admin.site.register(respuesta_correcta,respuesta_correctaAdmin)

class respuesta_incorrectaAdmin(admin.ModelAdmin):
    list_display = ["id","incorrecta"]
admin.site.register(respuesta_incorrecta,respuesta_incorrectaAdmin)

class cargar_preguntaAdmin(admin.ModelAdmin):
    list_display = ["id","pregunta"]
admin.site.register(cargar_pregunta, cargar_preguntaAdmin)
#respuesta_correctaAdmin,respuesta_incorrectaAdmin,categoriaAdmin