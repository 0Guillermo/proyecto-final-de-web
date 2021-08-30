"""from django.db import models
from apps.preguntas.models import cargar_pregunta,  respuesta_correcta, respuesta_incorrecta, categoria

sum = 1
for y in categoria.objects.all():
    A = y

    sum += 1

    print(A, "=============================")

print(categoria.objects.all())
print(type(cargar_pregunta.objects.all()), "*++++++++++++++++++++++++++++++++++++++")


prueba =cargar_pregunta.objects.filter(categoria).all()
for b in prueba:
    print("=====================================================")
    print(b, ".................................")




CATEGORIA_CHOICES = (
    ("1","A"),
    ("2","B"),
)

class jugar(models.Model):
    cargar_pregunta = models.ManyToManyField(cargar_pregunta, related_name="cargar_pregunta")
    puntaje = models.CharField(max_length=255,null=True) #esto tiene que ser un metodo creo.
    estado = models.CharField(max_length=255,null=True)                                    # si hacierta la preguntas suma alguna clase de puntos
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, null=True)


    class Meta: 
        db_table = 'jugar'

    def __str__(self):
        return f"{self.cargar_pregunta} {self.puntaje}{self.estado}"


"""