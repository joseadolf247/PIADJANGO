from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name="index"),
    path('contacto/',views.contacto ,name="contacto"),
    path('quienessomos/',views.quienessomos ,name="quienessomos"),
    path('servicios/',views.servicios ,name="servicios"),
    path('ubicacion/',views.ubicacion ,name="ubicacion")
]

