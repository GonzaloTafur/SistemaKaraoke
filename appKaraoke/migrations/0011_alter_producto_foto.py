# Generated by Django 4.2.11 on 2025-03-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKaraoke', '0010_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img/prod/'),
        ),
    ]
