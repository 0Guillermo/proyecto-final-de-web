# Generated by Django 3.2.6 on 2021-08-30 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0010_alter_cargar_pregunta_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargar_pregunta',
            name='categoria',
        ),
        migrations.AddField(
            model_name='cargar_pregunta',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='preguntas.categoria'),
        ),
    ]
