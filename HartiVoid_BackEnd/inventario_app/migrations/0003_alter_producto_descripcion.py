# Generated by Django 5.0.6 on 2024-06-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_app', '0002_producto_custom_id_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='Descripción', max_length=350),
        ),
    ]