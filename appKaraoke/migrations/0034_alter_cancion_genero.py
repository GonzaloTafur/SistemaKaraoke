# Generated by Django 4.2.11 on 2025-03-27 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appKaraoke', '0033_alter_cancion_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appKaraoke.genero'),
        ),
    ]
