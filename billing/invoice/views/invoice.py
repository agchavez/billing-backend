#django rest framework
from rest_framework import viewsets, mixins

from rest_framework.response import Response
from rest_framework import status

from billing.invoice.models import Invoices
from billing.invoice.serializers import InvoiceModelSerializer
class InvoiceViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = InvoiceModelSerializer
    queryset  = Invoices.objects.filter(status = True)
    lookup_field = ('id')
