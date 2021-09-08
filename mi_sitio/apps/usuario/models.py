from django.db import models

class usuarios(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    puntos_total = models.IntegerField(default=0)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido} {self.localidad} {self.telefono} {self.email} {self.puntos_total}"

def update_db_field(name,field,value):
    usuarios.objects.get(name=name).update(field=value)
