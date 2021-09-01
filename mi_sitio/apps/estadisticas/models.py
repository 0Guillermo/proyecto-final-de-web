from django.db import models
from apps.jugadores.models import jugadore
from apps.jugar_preguntas.models import jugar
ESTADO_CHOICE =(
    ("1","gano"),
    ("0","perdio")
)
class estadisticas(models.Model):
    participante = models.ForeignKey(jugadore, on_delete=models.CASCADE)
    juegos = models.ManyToManyField(jugar)
    feche_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    Puntuacion = models.IntegerField()
    estado = models.CharField(max_length=6,choices=ESTADO_CHOICE)
    nivel = models.IntegerField()

    class Meta:
        db_table = "estadisticas"

    def __str__(self):
        return self.participante
