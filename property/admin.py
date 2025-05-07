from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1               # one empty slot to add more images

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]
    list_display = ("street", "city", "listing_price", "property_type", "is_sold")
    list_filter  = ("city", "property_type")
    search_fields = ("street", "city", "postal")