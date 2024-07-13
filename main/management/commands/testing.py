from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        #crear_user('1444444', 'Elcor', 'Chazo', 'elcorchazo@gmail.com', '1234', 'Guillermo Frick 114', 88776677)
        # def handle(self, *args, **kwargs):
        #crear_inmueble('Casa de Piedra', 'Amoblada amplio espacio', 80, 300, 1, 3, 2, 500000, 'Los Pellines 115', 'chalet', '05606', '123456-4')  
        #crear_inmueble('Casa en el cerro', 'Amoblada amplio espacio', 100, 300, 1, 3, 2, 500000, 'Los Laureles 444', 'parcela', 'Paillaco', '12222222')
        #eliminar_inmueble(7)
        #editar_user('12222222', 'Elcar', 'Nassa', 'elkarnazza@blackmail.com', 'nemesis', 'Los RObles 334') 
        #crear_user('123456-4', 'Pedro', 'Picapiedra', 'ppiedra@gmail.com', '1234', '1234', 'Av. Rocadura 45')
        #eliminar_user(5)  
        #editar_inmueble(8, 'Casa en el lago', 'Sin amoblar', 80, 300, 1, 3, 2, 500000, 'Diolon s/n', 'parcela', 'Corral', '1444444')
        
        inmuebles = obtener_inmuebles_comunas()
        
        