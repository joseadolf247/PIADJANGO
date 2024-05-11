from django.db import models

# Create your models here.
class Sucursales(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=78)

    def __str__(self):
        return self.nombre