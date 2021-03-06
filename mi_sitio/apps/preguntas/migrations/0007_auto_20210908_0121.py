# Generated by Django 3.2.6 on 2021-09-08 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0006_auto_20210908_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargar_pregunta',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='cargar_pregunta',
            name='respuestas',
            field=models.ManyToManyField(related_name='respuesta_correctas', to='preguntas.respuesta_correcta'),
        ),
        migrations.AddField(
            model_name='respuesta_correcta',
            name='estado',
            field=models.CharField(choices=[('0', 'NO ES CORRECTA'), ('1', 'ES CORRECTA')], default=0, max_length=2),
        ),
        migrations.DeleteModel(
            name='respuesta',
        ),
        migrations.DeleteModel(
            name='respuesta_incorrecta',
        ),
    ]
