from django.contrib import admin
from .models import jugar

class jugarAdmin(admin.ModelAdmin):
    list_display = ["id","estado"]
admin.site.register(jugar,jugarAdmin)

# Register your models here.
