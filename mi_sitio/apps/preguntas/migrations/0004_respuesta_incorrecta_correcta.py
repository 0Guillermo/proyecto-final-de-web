# Generated by Django 3.2.6 on 2021-09-08 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0003_alter_cargar_pregunta_respuesta_incorrecta'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta_incorrecta',
            name='correcta',
            field=models.CharField(max_length=255, null=True),
        ),
    ]