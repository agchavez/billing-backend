#django rest framework
from rest_framework import viewsets, mixins

from rest_framework.response import Response
from rest_framework import status

from billing.invoice.models import InvoicesDetail
from billing.invoice.serializers import InvoiceDetailModelSerializer
class InvoiceDetailViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = InvoiceDetailModelSerializer
    queryset  = InvoicesDetail.objects.all()
    lookup_field = ('id')
