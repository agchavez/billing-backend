#  definicion del serializer de promocion

# Django REST Framework
from rest_framework import serializers

# Model
from billing.invoice.models.discount import Discount 

class DiscountModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = (
            'id','describe', 'discount', 'code', 'duration', 'status'
        )
        
    