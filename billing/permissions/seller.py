
from rest_framework.permissions import BasePermission
from billing.user.models import Seller
from rest_framework import serializers

from django.conf import settings

# Utilities
import jwt

class SellerToken(BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario es administrador 
        try:
            token = request.headers['token']
        except :
            return False
       
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Toekn expirado')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Token invalido')
        
        code = payload['code']
        
        try: 
            Seller.objects.get(
                code = code
            )
        except Seller.DoesNotExist:
            return False
        return True