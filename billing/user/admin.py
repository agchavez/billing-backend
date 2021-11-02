# Django
from django.contrib import admin
from billing.user.models import Client, Seller

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name','rtn'
    )

    search_fields = ('rtn', 'name')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name','last_name', 'code'
    )

    search_fields = ('code','first_name')