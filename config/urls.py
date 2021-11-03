"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('billing.user.urls', 'clients'), namespace='client')),
    path('', include(('billing.product.urls', 'products'), namespace='product'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
