# Generated by Django 4.2.11 on 2025-03-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKaraoke', '0031_remove_cancion_generos_alter_cancion_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
