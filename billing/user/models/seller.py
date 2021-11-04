# Modelo para usuarios vendedores

# Django
from django.db import models

# Utils
from billing.utils.models import BaseModel

class Seller(BaseModel):
    # clase para los vendedres 
    first_name = models.CharField(
                    'Nombre',
                    max_length=20,
                    help_text='Primer nombre del vendedor')
    last_name  = models.CharField(
                    'Apellido',
                    max_length=20,
                    help_text='Apellido del vendedor')
    code       = models.CharField(
                    'Codigo de acceso',
                    max_length=8,
                    unique=True,
                    error_messages={'unique':'El codigo debe ser unico'})

    def __str__(self):
        return self.first_name