# Generated by Django 4.1 on 2022-11-28 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barberApp', '0010_alter_cita_descripcion_alter_cita_hora'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
