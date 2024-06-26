# Generated by Django 5.0.4 on 2024-05-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=80)),
                ('modelo', models.IntegerField()),
                ('propietario', models.CharField(max_length=80)),
                ('placas', models.CharField(max_length=80)),
                ('estado', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
                'db_table': 'autos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombresempleado', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=80)),
                ('departamento', models.CharField(max_length=80)),
                ('salario', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleados',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreservicios', models.CharField(max_length=80)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=80)),
                ('tiempo', models.IntegerField()),
                ('garantia', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'servicios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=78)),
                ('encargado', models.CharField(max_length=80)),
                ('numEmpleados', models.IntegerField()),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'db_table': 'sucursales',
                'ordering': ['id'],
            },
        ),
    ]
