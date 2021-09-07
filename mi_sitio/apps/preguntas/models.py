from django.db import models

class categoria(models.Model):
    tipo = models.CharField(max_length=255)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.tipo

class respuesta_correcta(models.Model):
    correcta = models.CharField(max_length=255)

    class Meta:
        db_table = 'respuesta_correcta'

    def __str__(self):
        return f"{self.id}), {self.correcta}"

class respuesta_incorrecta(models.Model):
    incorrecta = models.CharField(max_length=255)

    class Meta:
        db_table = 'respuesta_incorrecta'

    def __str__(self):
        return f"{self.id}, {self.incorrecta}"

class cargar_pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    categoria = models.ManyToManyField(categoria, related_name="categorias")
    respuesta_incorrecta = models.ManyToManyField(respuesta_incorrecta,related_name="respuesta_incorrectas")
    respuesta_correcta = models.ManyToManyField(respuesta_correcta,related_name="respuesta_correctas")

##cambiar este modelo y hacer que en un solo atributo se guarde las preguntas
    # y en el segundo que se guarde la que es correcta de del primer atributo

## o borrar de aca este tributo "respuesta_correcta" y ponerlo en la tabla jugar

## ooo hacer que el atributo respuesta_incorrecta tenga su propia tabla aparte no la default
    # y en esa tabla que se crea agregar la respuesta que es correcta

    class Meta:
        db_table = 'cargar_pregunta'

    def __str__(self):
        return f"{self.id}, {self.pregunta} {self.categoria} {self.respuesta_incorrecta} {self.respuesta_correcta}"

# poner que en respuesta incorrecta se cargen todas las respuestas
# y que en respuestas correcta se cargue la pregunta que es correcta de las preguntas incorrectas