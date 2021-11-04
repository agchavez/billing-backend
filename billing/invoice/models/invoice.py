
from  django.db import models

from billing.utils.models import BaseModel
from billing.user.models import Client, Seller
from .discount import Discount

class Invoices(BaseModel):

    total       = models.FloatField('Total factura: ')
    client      = models.ForeignKey(Client,  on_delete=models.CASCADE, blank=True, null=True, related_name='invoicesclient')
    seller      = models.ForeignKey(Seller,on_delete=models.CASCADE, related_name='invoicesseller')
    isv         = models.FloatField('ISV 15%')
    discount    = models.ForeignKey(Discount,on_delete=models.CASCADE, blank=True, null=True, related_name='invoicesdicount')
    status      = models.BooleanField('Estado', default=True)
    def __str__(self) :
        return str(self.total)