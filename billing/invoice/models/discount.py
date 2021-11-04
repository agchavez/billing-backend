# Modelo para el apartado de productos

from django.db import models

from billing.utils.models import BaseModel
class Discount(BaseModel):
    describe    = models.TextField(
                'Descripcion',
                blank=True,
                null=True,
                help_text='Descripcion del descuento'
                )
    discount  = models.IntegerField(
                'Descuento de',
                help_text='Cantidad de productos'
                )
    code    = models.CharField(
                'Codigo',
                max_length=11,
                unique=True
                )
    duration = models.DateTimeField(
                'Duracion',
                help_text='Fecha en la que fue modificado el registro.'
                )
    status      = models.BooleanField(default=True)
    def __str__(self):
        return self.code
        
