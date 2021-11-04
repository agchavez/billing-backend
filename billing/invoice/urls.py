from django.urls import include, path
from billing.invoice.views import DiscountViewSet, InvoiceViewSet
from billing.invoice.views.invoice_detail import InvoiceDetailViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'discounts',DiscountViewSet, basename='discount')
router.register(r'invoices',InvoiceViewSet, basename='invoice')
router.register(r'invoice-details',InvoiceDetailViewSet, basename='invoice-detail')

urlpatterns = [
    path('', include(router.urls))
]