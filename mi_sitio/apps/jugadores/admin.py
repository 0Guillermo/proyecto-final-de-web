from django.contrib import admin

from .models import jugadore

class jugadoreAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido","localidad","telefono","email"]

admin.site.register(jugadore, jugadoreAdmin)