from django.shortcuts import render
from .models import Sucursales 

# Create your views here.
def index(request):
    datos={
        "sucursales":Sucursales.objects.all()
    }
    return render(request,"index.html",context=datos)

