from main.models import Comuna, Inmueble, UserProfile
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales_terreno, cantidad_estacionamientos, cantidad_habitaciones, cantidad_baños, precio, direccion, tipo_inmueble, comuna, propietario):
    propietario = User.objects.get(username=propietario)
    comuna=Comuna.objects.get(nombre=comuna)
    ci = Inmueble(nombre=nombre,
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
                  propietario=propietario)
    ci.save()
    return ci

def editar_inmueble(inmueble_id, nombre, descripcion, m2_construidos, m2_totales_terreno, cantidad_estacionamientos, cantidad_habitaciones, cantidad_baños, precio, direccion, tipo_inmueble, comuna, propietario):
    propietario = User.objects.get(username=propietario)
    comuna=Comuna.objects.get(nombre=comuna)
    inmueble = Inmueble.objects.get(id=inmueble_id)
    inmueble.nombre=nombre,
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