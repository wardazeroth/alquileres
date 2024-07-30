from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django import forms

# Create your models here.

class UserProfile(models.Model):
    roles =(('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario'), ('admin', 'Admin'))
    user = models.OneToOneField(User, related_name = 'usuario', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True, blank=True)   
    rol = models.CharField(max_length=255, choices=roles, default = 'arrendatario')
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {(self.rol)}'
    
# class Region pendiente
class Region(models.Model):
    cod = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.nombre}({self.cod})'

class Comuna(models.Model):
    cod = models.CharField(max_length=5, primary_key = True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT,related_name= 'comunas')
    
    def __str__(self) -> str:
        return f'{self.nombre}({self.cod})'
    
class Inmueble(models.Model):
    tipos = (('casa', 'Casa'), ('parcela', 'Parcela'), ('departamento', 'Departamento'))
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales_terreno = models.IntegerField(validators=[MinValueValidator(1)])
    cantidad_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default= 0)
    cantidad_habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default = 1)
    cantidad_baños = models.IntegerField(validators=[MinValueValidator(0)], default= 0)
    imagen1 = models.URLField(blank=True, null=True, max_length=500)
    imagen2 = models.URLField(blank=True, null=True, max_length=500)
    imagen3 = models.URLField(blank=True, null=True, max_length=500)
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
        