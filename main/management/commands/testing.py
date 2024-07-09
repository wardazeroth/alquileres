from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        crear_user('12222222', 'Elcor', 'Chazo', 'elcorchazo@gmail.com', '1234', 'Guillermo Frick 114', 88776677)