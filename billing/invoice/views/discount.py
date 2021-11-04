# Vista para el apartado de descuento

from billing.invoice.models.discount import Discount
from billing.invoice.serializers.discount import DiscountModelSerializer

from rest_framework import viewsets, mixins

from rest_framework.response import Response
from rest_framework import status


class DiscountViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DiscountModelSerializer
    queryset  = Discount.objects.filter(status = True)

    #Filtrar por el codigo
    lookup_field = ('code')

    def perform_retrive(self, instance):
        if instance.status:
            return Response({
                instance
            }, status=status.HTTP_200_OK)
        return Response({},  status=status.HTTP_400_BAD_REQUEST)