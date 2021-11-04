# Django
from django.contrib import admin

from billing.product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id','name', 'price', 'amount', 'code', 'description', 'status'
    )

    search_fields = ('id', 'code','status')

