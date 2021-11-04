#  definicion del serializer de facturacion

# Django REST Framework
from rest_framework import serializers

# Model
from billing.invoice.models import Invoices 

class InvoiceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoices
        fields = (
            'id','total', 'client', 'seller', 'isv', 'discount', 'status','created'
        )
        
    