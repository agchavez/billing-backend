
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import date
from billing.user.serializers.seller import SellerLoginSerializer, UserModelSerializer

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
