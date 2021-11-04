
from  django.db import models

from billing.utils.models import BaseModel
from billing.product.models import Product
from .invoice import Invoices

class InvoicesDetail(BaseModel):

    total_line  = models.FloatField('Total factura: ')
    product      = models.ForeignKey(Product,  on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    invoice      = models.ForeignKey(Invoices,on_delete=models.CASCADE, related_name='invoice_detail')
    amount      = models.IntegerField('cantidad')


    def __str__(self) :
        return str(self.total_line)