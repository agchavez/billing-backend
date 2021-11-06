#django rest framework
from billing.permissions.seller import SellerToken
from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAuthenticated

from billing.user.models.client import Client
from billing.user.serializers.client import ClienteModelSerializer
class ClientViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    
    serializer_class = ClienteModelSerializer
    queryset  = Client.objects.all()
    lookup_field = ('rtn')
    def get_permissions(self):
        permissions = [SellerToken]
        return [permission() for permission in permissions]

    
    
 