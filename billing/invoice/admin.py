# Django
from django.contrib import admin

from billing.invoice.models import Discount

@admin.register(Discount)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id','describe', 'discount', 'code', 'duration', 'status'
    )

    search_fields = ('id', 'code','status')

