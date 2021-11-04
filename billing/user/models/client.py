# Modelo para los clientes

#Django
from django.db import models

#utils 
from billing.utils.models import BaseModel

class Client(BaseModel):
    name = models.CharField(
                    'Nombre', 
                    max_length=50, 
                    help_text='Nmbre del cliente o empresa')
    rtn  = models.CharField(
                    'RTN', 
                    unique=True,
                    max_length=16, 
                    help_text='RTN de la empresa' )
    def __str__(self):
        return str(self.rtn)