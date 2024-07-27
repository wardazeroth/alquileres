from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from main.models import Inmueble, Region, Comuna
from main.services import crear_inmueble as crear_inmueble_service, editar_inmueble as editar_inmueble_service, eliminar_inmueble as eliminar_inmueble_service
from inmuebles.forms import InmuebleForm

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

@user_passes_test(solo_arrendadores)
def editar_inmueble(req, id):
    if req.method == 'GET':
        #1. Obtengo el inmueble a editar
        inmueble = Inmueble.objects.get(id=id)
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()
        #2.5 Obtengo el código de la region
        cod_region = inmueble.comuna.region.cod
        #3. creo el 'context' con toda la info que necesite el template
        context = {
            'inmueble': inmueble,
            'regiones': regiones,
            'comunas': comunas,
            'cod_region': cod_region
        }
        return render(req, 'editar_inmueble.html', context)
    else:
        inmueble_id = id
        propietario = req.user.username
        editar_inmueble_service(
        inmueble_id,
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
        propietario)

    messages.success(req, '¡Inmueble actualizado con éxito!')
    return redirect('/')

@user_passes_test(solo_arrendadores)
def eliminar_inmueble(req, id):
    
    eliminar_inmueble_service(id)
    messages.error(req, '¡Inmueble eliminado!')
    return redirect('/accounts/profile')

def detalleInmueble(req, id):
    inmueble_hallado = Inmueble.objects.get(id=id)

    context = {
        'inmueble_hallado': inmueble_hallado
    }
    return render(req, 'detalle.html', context)