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
    lookup_field = ('invoice')
    
    def retrieve(self, request, invoice=None):
        try:
            invoice_details = InvoicesDetail.objects.filter(invoice=invoice)
        except:
            Response({'msg':"No se tiene  registros de  la factura %s" % invoice},  status=status.HTTP_400_BAD_REQUEST)
        invoicedata  = InvoiceDetailModelSerializer(invoice_details, many=True)
        
        if invoice_details.count() == 0:
            return Response({'msg':"No se tiene  registros de  la factura %s" % invoice},  status=status.HTTP_400_BAD_REQUEST)
        return Response(invoicedata.data,  status=status.HTTP_200_OK)
