from django.db import models

class jugar(models.Model):
    respuesta_correcta = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'jugar'

# cargar un objeto de preguntas para que despues se pueda exporta a la carpeta views
# donde se tendra acceso para que se pueda ver en la pagina