# Generated by Django 3.2.6 on 2021-08-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadores',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jugadores',
            name='telefono',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
