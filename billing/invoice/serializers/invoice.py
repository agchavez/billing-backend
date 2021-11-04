#  definicion del serializer de facturacion

# Django REST Framework
from billing.invoice.serializers.invoice_detail import InvoiceDetailModelSerializer
from rest_framework import serializers

# Model
from billing.invoice.models import Invoices 
from  billing.user.serializers import ClienteModelSerializer

class InvoiceModelSerializer(serializers.ModelSerializer):
    invoices = InvoiceDetailModelSerializer(many=True, read_only=True)
    class Meta:
        model = Invoices
        fields = [
            'id','total','invoices', 'client', 'seller', 'isv', 'discount', 'status','created'
        ]
        
    