# Modelo para el apartado de productos

from django.db import models
from django.db.models.fields import BooleanField, TextField

from billing.utils.models import BaseModel
class Product(BaseModel):
    name    = models.CharField(
                'Nombre',
                max_length=100,
                help_text='Nombre del producto'
                )
    price   = models.IntegerField(
                'Precio',
                help_text='Precio del producto'
                )
    amount  = models.IntegerField(
                'Cantidad',
                help_text='Cantidad de productos'
                )
    code    = models.CharField(
                'Codigo',
                max_length=11,
                unique=True
                )
    description = TextField(
                    'Descripcion del producto',
                    blank=True,
                    null=True,
                    )
    status      = BooleanField(default=True)
    def __str__(self):
        return self.name
        
