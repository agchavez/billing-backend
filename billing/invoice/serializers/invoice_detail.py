#  definicion del serializer de facturacion

# Django REST Framework
from rest_framework import serializers

# Model
from billing.invoice.models import InvoicesDetail 

class InvoiceDetailModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoicesDetail
        fields = (
            'id','total_line', 'product', 'amount'
        )
        
    