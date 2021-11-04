# definicion del serializer del cliente

# Django REST Framework
from rest_framework import serializers

# Model
from billing.user.models import Client

class ClienteModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'id','name', 'rtn', 'created'
        )
    