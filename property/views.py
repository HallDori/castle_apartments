from django.views.generic import ListView, DetailView
from .models import Property


class PropertyListView(ListView):
    model         = Property
    template_name = "property/catalogue.html"
    paginate_by   = 12
    ordering      = ["listing_price"]


class PropertyDetailView(DetailView):
    model         = Property
    template_name = "property/detail.html"