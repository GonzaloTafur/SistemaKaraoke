# Generated by Django 5.1.7 on 2025-03-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKaraoke', '0019_alter_cancion_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='genero',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
