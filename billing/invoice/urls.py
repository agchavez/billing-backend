from django.urls import include, path
from billing.invoice.views import DiscountViewSet, InvoiceViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'discounts',DiscountViewSet, basename='discount')
router.register(r'invoices',InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('', include(router.urls))
]