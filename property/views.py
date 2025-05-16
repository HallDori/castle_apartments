# property/views.py
from decimal import Decimal
from django.views.generic import ListView, DetailView
from .models import Property

class PropertyDetailView(DetailView):
    model = Property
    template_name = "property/detail.html"

class PropertyListView(ListView):
    model = Property
    template_name = "property/catalogue.html"
    context_object_name = "properties"
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        postal_values = (
            self.request.GET.getlist("postal") or
            self.request.GET.get("postal", "").split(",")
        )
        postal_values = [p.strip() for p in postal_values if p.strip()]
        if postal_values:
            qs = qs.filter(postal__in=postal_values)

        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        if min_price:
            qs = qs.filter(listing_price__gte=Decimal(min_price))
        if max_price:
            qs = qs.filter(listing_price__lte=Decimal(max_price))

        types = self.request.GET.getlist("type")
        if types:
            qs = qs.filter(property_type__in=types)

        q = self.request.GET.get("q", "")
        if q:
            qs = qs.filter(street__icontains=q)

        order = self.request.GET.get("order")
        allowed = {
            "price": "listing_price",
            "-price": "-listing_price",
            "name": "street",
            "-name": "-street",
        }
        qs = qs.order_by(allowed.get(order, "-listing_date"))  # newest first
        return qs

    # so we can repopulate the form and keep filters when paginating
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filter_params"] = self.request.GET
        ctx["selected_types"] = self.request.GET.getlist("type")
        return ctx



