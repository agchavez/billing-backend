from django.urls import include, path
from billing.user.views.seller import SellerLoginAPIView

from rest_framework.routers import DefaultRouter

from billing.user.views import ClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')

urlpatterns = [
    path('',include(router.urls)),
    path('seller/login/', SellerLoginAPIView().as_view(), name='login')
]