# Generated by Django 3.2.6 on 2021-09-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_alter_cargar_pregunta_respuesta_incorrecta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargar_pregunta',
            name='respuesta_incorrecta',
            field=models.ManyToManyField(related_name='respuesta_incorrectas', to='preguntas.respuesta_incorrecta'),
        ),
    ]
