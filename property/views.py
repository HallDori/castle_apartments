from django.views.generic import ListView, DetailView
from .models import Property

class PropertyListView(ListView):
    model = Property
    template_name = "property/catalogue.html"
    context_object_name = "properties"
    paginate_by = 12

class PropertyDetailView(DetailView):
    model = Property
    template_name = "property/detail.html"