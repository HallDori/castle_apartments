# property/views.py
from decimal import Decimal
from django.views.generic import ListView, DetailView
from .models import Property


class PropertyListView(ListView):
    model = Property
    template_name = "property/catalogue.html"
    context_object_name = "properties"
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()

        # --- postal code ----------------------------------------------------
        # ?postal=101&postal=220  or   ?postal=101,220
        postal_values = (
            self.request.GET.getlist("postal") or
            self.request.GET.get("postal", "").split(",")
        )
        postal_values = [p.strip() for p in postal_values if p.strip()]
        if postal_values:
            qs = qs.filter(postal__in=postal_values)

        # --- price range ----------------------------------------------------
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        if min_price:
            qs = qs.filter(listing_price__gte=Decimal(min_price))
        if max_price:
            qs = qs.filter(listing_price__lte=Decimal(max_price))

        # --- property type ---------------------------------------------------
        # ?type=villa&type=house
        types = self.request.GET.getlist("type")
        if types:
            qs = qs.filter(property_type__in=types)

        # --- free-text search  ----------------------------------------------
        q = self.request.GET.get("q", "")
        if q:
            qs = qs.filter(street__icontains=q)

        # --- ordering --------------------------------------------------------
        order = self.request.GET.get("order")
        allowed = {
            "price": "listing_price",
            "-price": "-listing_price",
            "name": "street",
            "-name": "-street",
        }
        qs = qs.order_by(allowed.get(order, "-listing_date"))  # default newest first
        return qs

    # so we can repopulate the form and keep filters when paginating
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filter_params"] = self.request.GET  # already there
        ctx["selected_types"] = self.request.GET.getlist("type")  # <-- NEW
        return ctx

class PropertyDetailView(DetailView):                   # ← NEW
    """
    Shows the information for a single property (template already exists
    at property/detail.html).
    """
    model = Property
    template_name = "property/detail.html"

