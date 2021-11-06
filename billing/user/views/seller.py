
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import date
from billing.user.serializers.seller import SellerLoginSerializer, UserModelSerializer

from billing.user.models import Seller
from rest_framework import serializers

from django.conf import settings

import jwt
class SellerLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = SellerLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user , token = serializer.save()
        data= {
                    'user': UserModelSerializer(user).data,
                    'token':token
                }
        return Response(data, status = status.HTTP_201_CREATED) 
    def get(self, request, *args, **kwargs):
        try:
            token = request.headers['token']
        except :
            return  Response({"msg":"No hay token en la peticion"}, status = status.HTTP_400_BAD_REQUEST)
       
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Toekn expirado')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Token invalido')
        
        code = payload['code']
        
        try: 
            seller = Seller.objects.get(
                code = code
            )
            
            data = {
                **UserModelSerializer(seller).data
            }
            return Response(data, status = status.HTTP_200_OK)
        except Seller.DoesNotExist:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)

