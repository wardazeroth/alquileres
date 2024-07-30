from main.models import Comuna, Inmueble, UserProfile
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db.models import Q
from django.contrib import messages
from django.db import connection

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales_terreno, cantidad_estacionamientos, cantidad_habitaciones, cantidad_baños, precio, direccion, tipo_inmueble, comuna_cod, propietario_rut,imagen1= None, imagen2= None, imagen3= None):
    
    propietario = User.objects.get(username=propietario_rut)
    comuna=Comuna.objects.get(cod=comuna_cod)
    
    Inmueble.objects.create(nombre=nombre,
                descripcion=descripcion,
                m2_construidos= m2_construidos,
                m2_totales_terreno=m2_totales_terreno,
                cantidad_estacionamientos=cantidad_estacionamientos,
                cantidad_habitaciones=cantidad_habitaciones,
                cantidad_baños=cantidad_baños,
                precio=precio,
                direccion=direccion,
                tipo_inmueble=tipo_inmueble,
                comuna=comuna,
                propietario=propietario,
                imagen1=imagen1,
                imagen2=imagen2,
                imagen3=imagen3,)

def editar_inmueble(inmueble_id, nombre, descripcion, m2_construidos, m2_totales_terreno, cantidad_estacionamientos, cantidad_habitaciones, cantidad_baños, precio, direccion, tipo_inmueble, comuna_cod, propietario, imagen1, imagen2, imagen3):
    propietario = User.objects.get(username=propietario)
    comuna=Comuna.objects.get(cod=comuna_cod)
    inmueble = Inmueble.objects.get(id=inmueble_id)
    inmueble.nombre=nombre
    inmueble.descripcion=descripcion
    inmueble.m2_construidos=m2_construidos
    inmueble.m2_totales_terreno=m2_totales_terreno
    inmueble.cantidad_estacionamientos=cantidad_estacionamientos
    inmueble.cantidad_habitaciones=cantidad_habitaciones
    inmueble.cantidad_baños=cantidad_baños
    inmueble.precio=precio
    inmueble.direccion=direccion
    inmueble.tipo_inmueble=tipo_inmueble
    inmueble.comuna=comuna
    inmueble.propietario=propietario
    if imagen1 is not None:
        inmueble.imagen1= imagen1
    if imagen2 is not None:
        inmueble.imagen2=imagen2
    if imagen3 is not None:
        inmueble.imagen3= imagen3
    inmueble.save()

def eliminar_inmueble(inmueble_id):
    Inmueble.objects.get(id=inmueble_id).delete()

def crear_user(username, first_name, last_name, email, password, pass_confirm, direccion, telefono= None)-> list[bool, str]:
    #1. Validamos si las password coinciden
    if password != pass_confirm:
        return False
    #2. creamos el objeto user
    try:
        user = User.objects.create_user(
        username, email, password,
        first_name=first_name,
        last_name=last_name,
    )
    except IntegrityError:
        #se le da feedback al usuario
        return False, 'RUT DUPLICADO'
        #3.  Creamos el UserProfile
    UserProfile.objects.create(
        direccion=direccion,
        telefono=telefono,
        user=user
        )
    return True, None

def eliminar_user(user_id):
    User.objects.get(id=user_id).delete()

def editar_user(rut, first_name, last_name, email, password, direccion, telefono= None)->list[bool, str]:   
    user = User.objects.get(username=rut)
    # Actualizar los campos del usuario utilizando update
    User.objects.filter(username=rut).update(
        first_name=first_name,
        last_name=last_name,
        email=email       
    )
    user.set_password(password)
    user.save()
    # Actualizar el perfil del usuario utilizando update
    UserProfile.objects.filter(user=user).update(
        direccion=direccion,
        telefono=telefono
    )
    return user

def editar_user_sin_password(rut, first_name, last_name, email, direccion, rol, telefono= None)->list[bool, str]:
    user = User.objects.get(username=rut)
    # Actualizar los campos del usuario utilizando update
    User.objects.filter(username=rut).update(
    first_name=first_name,
    last_name=last_name,
    email=email)
        # Actualizar el perfil del usuario utilizando update
    UserProfile.objects.filter(user=user).update(
        direccion=direccion,
        telefono=telefono,
        rol=rol
    )
    return user

def obtener_inmuebles_comunas(filtro):

    if filtro is None:
        return Inmueble.objects.all().order_by('comuna')
    
    #Si llegamos acá significa que SI HAY un filtro
    return Inmueble.objects.filter(Q(nombre__icontains=filtro) | Q(descripcion__icontains=filtro)).order_by('comuna')
        

def obtener_inmuebles_regiones(filtro):
    consulta = 'select * from main_inmueble as I join main_comuna as C on I.comuna_id = C.cod join main_region as R on C.region_id = R.cod order by R.cod'
    if filtro is not None:
        consulta = f"select * from main_inmueble as I join main_comuna as C on I.comuna_id = C.cod join main_region as R on C.region_id = R.cod where I.nombre like'%{filtro}%' or I.descripcion like '%{filtro}%' order by R.cod"
        #return Inmueble.objects.raw(consulta)
        cursor =connection.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        return registros
        #return Inmueble.objects.filter(nombre__icontains=filtro).order_by('comuna')
        
def change_pass(req, password, pass_repeat):
    #2. Valido que ambas contraseñas coincidan
    if password != pass_repeat:
        messages.error(req, 'Las contraseñas no coinciden')
        return
    else:
    #3. Actualizamos la contraseña
        req.user.set_password(password)
        req.user.save()
        #4. Le avisamos al usuario que el cambio fue exitoso
        messages.success(req, 'Contraseña actualizada')
        
        

    