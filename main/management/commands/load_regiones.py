import csv
from django.core.management.base import BaseCommand
from main.models import Region



class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        archivo = open('data/comunas.csv', encoding="utf-8")
        reader = csv.reader(archivo, delimiter= ';')
        next(reader)
        
        nombres_regiones = []
        for fila in reader:
            #Si no tenemos el nombre de la región previamente guardada, agregamos a la base de datos
            if fila[2] not in nombres_regiones:
                Region.objects.create(nombre=fila[2], cod=fila[3])
                #guardamos su nombre para no volver a agregarla
                nombres_regiones.append(fila[2])
                