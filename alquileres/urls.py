"""
URL configuration for alquileres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import register, indexView, profile, edit_user, change_password
from inmuebles.views import nuevo_inmueble, crear_inmueble, editar_inmueble, eliminar_inmueble, detalleInmueble
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', profile, name='profile'),
    path('accounts/change-pass', change_password, name='change-password'),
    path('', indexView, name='home'),
    path('accounts/register/', register, name = 'register'),
    path('', include('main.urls')),
    path('edit-user/', edit_user, name='edit_user'),
    path('inmuebles/nuevo/', nuevo_inmueble, name='nuevo_inmueble'),
    path('inmuebles/crear/', crear_inmueble, name='crear_inmueble'),
    path('inmuebles/editar/<id>/', editar_inmueble, name='editar_inmueble'),
    path('inmuebles/eliminar/<id>/', eliminar_inmueble, name='eliminar_inmueble'),
    path('<id>/', detalleInmueble, name= 'detalle_inmueble')
]
