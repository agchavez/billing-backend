#  definicion del serializer del producto

# Django REST Framework
from rest_framework import serializers

# Model
from billing.product.models import Product

class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id','name', 'price', 'amount', 'code', 'description', 'status', 'created'
        )
        
    