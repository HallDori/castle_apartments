from django.contrib import admin
from .models import PurchaseOffer

@admin.register(PurchaseOffer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("property", "buyer", "price", "status", "created")
    list_filter  = ("status",)