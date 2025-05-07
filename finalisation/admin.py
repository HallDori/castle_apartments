from django.contrib import admin
from .models import Finalisation

@admin.register(Finalisation)
class FinalisationAdmin(admin.ModelAdmin):
    list_display = ("offer", "payment_method", "confirmed")