from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from main.models import Inmueble, Region, Comuna
from main.services import crear_inmueble as crear_inmueble_service

#vamos a crear un filtro que solo pasan los arrendadores
def solo_arrendadores(user):
    if user.usuario.rol == 'arrendador' or user.is_staff == True:
        return True
    else:
        return False

# Create your views here.
@user_passes_test(solo_arrendadores)
def nuevo_inmueble(req):
    #pasar los datos requeridos por el formulario
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    context = {
        'tipos_inmueble': Inmueble.tipos,
        'regiones': regiones,
        'comunas': comunas
    }
    return render(req, 'nuevo_inmueble.html', context)

@user_passes_test(solo_arrendadores)
def crear_inmueble(req):
    #obtener el rut del propietario
    propietario_rut = req.user.username
    crear_inmueble_service(
        req.POST['nombre'], 
        req.POST['descripcion'], 
        int(req.POST['m2_construidos']), 
        int(req.POST['m2_totales_terreno']), 
        int(req.POST['cantidad_estacionamientos']), 
        int(req.POST['cantidad_habitaciones']), 
        int(req.POST['cantidad_baños']), 
        int(req.POST['precio']), 
        req.POST['direccion'], 
        req.POST['tipo_inmueble'], 
        req.POST['comuna_cod'], 
        propietario_rut)

    messages.success(req, '¡La propiedad se creó exitosamente!')
    return redirect('/')