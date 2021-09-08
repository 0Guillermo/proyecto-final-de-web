from django.contrib import admin
from .models import usuarios


class usuariosAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre','apellido','localidad','telefono', 'email', 'puntos_total']
admin.site.register(usuarios, usuariosAdmin)