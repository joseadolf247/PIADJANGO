from django.contrib import admin
from .models import Sucursales,Autos,Empleados,Servicios
# Register your models here.
admin.site.register(Sucursales)
admin.site.register(Autos)
admin.site.register(Empleados)
admin.site.register(Servicios)