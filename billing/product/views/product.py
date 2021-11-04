#django rest framework
from rest_framework import viewsets, mixins

from rest_framework.response import Response
from rest_framework import status

from billing.product.models.product import Product
from billing.product.serializers import ProductModelSerializer
class ProductViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    
    
    serializer_class = ProductModelSerializer
    queryset  = Product.objects.filter(status = True)
    lookup_fields = ('code','id')

    def perform_destroy(self, instance):
        instance.status = False
        instance.save()
        
   
            
            

        
    
 