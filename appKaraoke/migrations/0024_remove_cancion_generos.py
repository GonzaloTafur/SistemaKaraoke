# Generated by Django 4.2.11 on 2025-03-27 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appKaraoke', '0023_cancion_generos_alter_cancion_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancion',
            name='generos',
        ),
    ]
