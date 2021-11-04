
from billing.user.models import Seller
#django
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
#jwt
import jwt
# Django rest_framework
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class."""

        model = Seller
        fields = (
            'first_name',
            'last_name',
        )
class SellerLoginSerializer(serializers.Serializer):
    
    code = serializers.CharField(min_length=8, max_length=8)

    def validate(self, data):
        try:
            seller = Seller.objects.get(code = data['code'])
        except:
            raise serializers.ValidationError('Codigo de acceso no valido')
        self.context['seller'] = seller
        return data
        
    def create(self, data):
        seller = self.context['seller']
        exp_date = timezone.now() + timedelta(days=3)
        print(seller)
        payload = {
        'code': data['code'],
        'exp': int(exp_date.timestamp())
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return self.context['seller'], token.decode()
