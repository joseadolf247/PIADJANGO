from django.db import models

# Create your models here.
class Sucursales(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=78)
    encargado = models.CharField(max_length=80)
    numEmpleados = models.IntegerField()
    telefono = models.IntegerField()


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'sucursales'
        verbose_name ='Sucursal'
        verbose_name_plural = 'Sucursales'
        ordering = ['id']

class Autos(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.IntegerField()
    propietario = models.CharField(max_length=80)
    placas = models.CharField(max_length=80)
    estado =models.CharField(max_length=80)

    def __str__(self):
        return self.marca
    
    class Meta:
        db_table = 'autos'
        verbose_name ='Auto'
        verbose_name_plural = 'Autos'
        ordering = ['id']
    
class Empleados(models.Model):
    nombresempleado = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    departamento = models.CharField(max_length=80)
    salario = models.IntegerField()
    
    def __str__(self):
        return self.nombresempleado
    
    class Meta:
        db_table = 'empleados'
        verbose_name ='Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
    
class Servicios(models.Model):
    nombreservicios = models.CharField(max_length=80)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=80)
    tiempo = models.IntegerField()
    garantia = models.BooleanField()
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombreservicios
    
    class Meta:
        db_table = 'servicios'
        verbose_name ='Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['id']




    
