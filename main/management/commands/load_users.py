import csv
from django.core.management.base import BaseCommand
from main.models import Comuna
from main.services import crear_user

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        archivo = open('data/users.csv', encoding="utf-8")
        reader = csv.reader(archivo, delimiter= ';')
        next(reader)
        
        for fila in reader:
            crear_user(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            