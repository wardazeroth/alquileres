from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class UserProfile(models.Model):
    # usuarios= (('1', 'Arrendador'), ('2', 'Arrendatario'))
    user = models.OneToOneField(User, related_name = 'usuario', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True)   
    # rut = models.CharField(max_length=9, primary_key=True)
    # nombres = models.CharField(max_length=50)
    # direccion = models.CharField(max_length=50)
    # telefono_personal = models.IntegerField()
    # correo_electronico = models.EmailField(unique=True)
    # tipo_de_usuario = models.CharField(max_length=15, choices=usuarios)
    
# class Region pendiente
class Comuna(models.Model):
    nombre = models.CharField(max_length=255)
    
class Inmueble(models.Model):
    tipos = (('casa', 'Casa'), ('parcela', 'Parcela'), ('departamento', 'Departamento'))
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales_terreno = models.IntegerField(validators=[MinValueValidator(1)])
    cantidad_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default= 0)
    cantidad_habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default = 1)
    cantidad_baños = models.IntegerField(validators=[MinValueValidator(0)], default= 0)
    precio = models.IntegerField(validators=[MinValueValidator(1000)])
    direccion = models.CharField(max_length=255)
    tipo_inmueble = models.CharField(max_length=255, choices = tipos)
    comuna = models.ForeignKey(Comuna, related_name = 'inmuebles', on_delete=models.RESTRICT)
    propietario = models.ForeignKey(User, on_delete =models.RESTRICT, related_name='inmuebles')

class Solicitud(models.Model):
    estados = (('pendiente', 'Pendiente'), ('departamento', 'Departamento'), ('parcela', 'Parcela'))
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
    arrendador = models.ForeignKey(User, related_name='solicitudes', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=estados)
        