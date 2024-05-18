from django.shortcuts import render
from .models import Sucursales 

# Create your views here.
def index(request):
    datos={
        "sucursales":Sucursales.objects.all()
    }
    return render(request,"index.html",context=datos)
def contacto(request):
    return render(request,"contacto.html")
def quienessomos(request):
    return render(request,"quienessomos.html")
def servicios(request):
    return render(request,"servicios.html")
def ubicacion(request):
    return render(request,"ubicacion.html")