from django.db import models
from apps.jugadores.models import jugadore
from apps.jugar_preguntas.models import jugar
ESTADO_CHOICE =(
    ("1","gano"),
    ("0","perdio")
)

class estadisticas(models.Model):
    participante = models.ForeignKey(jugadore, on_delete=models.CASCADE)
    juegos = models.ForeignKey(jugar, on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=2,choices=ESTADO_CHOICE,null=True)
    puntaje = models.IntegerField(null=True)
    nivel = models.IntegerField(null=True)
    puntos_total = models.IntegerField(null=True)

    class Meta:
        db_table = "estadisticas"

    def __str__(self):
        return self.estado
