# Generated by Django 5.0.6 on 2024-06-27 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.PositiveIntegerField()),
                ('marca', models.CharField(max_length=100)),
                ('precio_detal', models.DecimalField(decimal_places=2, max_digits=20)),
                ('precio_mayor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_app.linea')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario_app.proveedor')),
            ],
        ),
    ]
