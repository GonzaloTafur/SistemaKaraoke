# Generated by Django 4.2.11 on 2025-03-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appKaraoke', '0014_alter_producto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='producto/'),
        ),
    ]
